import sqlite3
import json
import os
import secrets
from datetime import datetime
from questions_seed import CATEGORIES, QUESTIONS, FLASHCARDS

ORIGINAL_DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "notariado.db"))
DB_PATH = ORIGINAL_DB_PATH

# En entornos Serverless de Vercel / Lambda, habilitar /tmp/notariado.db con permisos de escritura
if os.environ.get("VERCEL") or os.environ.get("AWS_LAMBDA_FUNCTION_NAME") or os.environ.get("VERCEL_ENV"):
    try:
        tmp_db = "/tmp/notariado.db"
        if not os.path.exists(tmp_db) and os.path.exists(ORIGINAL_DB_PATH):
            import shutil
            shutil.copyfile(ORIGINAL_DB_PATH, tmp_db)
        if os.path.exists(tmp_db):
            DB_PATH = tmp_db
    except Exception as e:
        print(f"[DATABASE] /tmp init warning: {e}")

# --- INICIALIZACIÓN DE FIREBASE FIRESTORE ---
HAS_FIREBASE = False
firestore_client = None

try:
    import firebase_admin
    from firebase_admin import credentials, firestore

    cred_env = os.environ.get("FIREBASE_SERVICE_ACCOUNT")
    cred_file = os.path.join(os.path.dirname(__file__), "serviceAccountKey.json")

    if cred_env:
        try:
            cred_dict = json.loads(cred_env)
            cred = credentials.Certificate(cred_dict)
            if not firebase_admin._apps:
                firebase_admin.initialize_app(cred)
            firestore_client = firestore.client()
            HAS_FIREBASE = True
            print("[DATABASE] [OK] Conectado a Firebase Firestore (vía FIREBASE_SERVICE_ACCOUNT)")
        except Exception as ex:
            print(f"[DATABASE] Error en credencial env Firebase: {ex}")
    elif os.path.exists(cred_file):
        try:
            cred = credentials.Certificate(cred_file)
            if not firebase_admin._apps:
                firebase_admin.initialize_app(cred)
            firestore_client = firestore.client()
            HAS_FIREBASE = True
            print("[DATABASE] [OK] Conectado a Firebase Firestore (vía serviceAccountKey.json)")
        except Exception as ex:
            print(f"[DATABASE] Error en archivo serviceAccountKey.json: {ex}")
    else:
        print("[DATABASE] Modo local: SQLite activado (notariado.db)")
except Exception as e:
    print(f"[DATABASE] Fallback a SQLite: {e}")
    HAS_FIREBASE = False

def get_db_connection():
    global DB_PATH
    if os.environ.get("VERCEL") or os.environ.get("AWS_LAMBDA_FUNCTION_NAME") or os.environ.get("VERCEL_ENV") or not os.access(os.path.dirname(DB_PATH) or ".", os.W_OK):
        try:
            tmp_db = "/tmp/notariado.db"
            if not os.path.exists(tmp_db) and os.path.exists(ORIGINAL_DB_PATH):
                import shutil
                shutil.copyfile(ORIGINAL_DB_PATH, tmp_db)
            if os.path.exists(tmp_db):
                DB_PATH = tmp_db
        except Exception as e:
            print(f"[DATABASE] /tmp get_db_connection warning: {e}")
    conn = sqlite3.connect(DB_PATH, timeout=30.0)
    conn.row_factory = sqlite3.Row
    return conn


def generate_key_code(prefix="NOT"):
    chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789" # Excluded O, 0, I, 1 to prevent reading confusion
    part1 = "".join(secrets.choice(chars) for _ in range(4))
    part2 = "".join(secrets.choice(chars) for _ in range(4))
    return f"{prefix}-{part1}-{part2}"

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        icon TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id TEXT NOT NULL,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_option TEXT NOT NULL,
        legal_basis TEXT NOT NULL,
        justification TEXT NOT NULL,
        distractors_analysis TEXT NOT NULL,
        difficulty TEXT DEFAULT 'Media',
        FOREIGN KEY (category_id) REFERENCES categories (id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS flashcards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id TEXT NOT NULL,
        title TEXT NOT NULL,
        prompt TEXT NOT NULL,
        legal_answer TEXT NOT NULL,
        legal_article TEXT NOT NULL,
        FOREIGN KEY (category_id) REFERENCES categories (id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exam_attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TEXT NOT NULL,
        score REAL NOT NULL,
        total_questions INTEGER NOT NULL,
        correct_count INTEGER NOT NULL,
        incorrect_count INTEGER NOT NULL,
        time_spent_seconds INTEGER NOT NULL,
        passed INTEGER NOT NULL,
        answers_json TEXT NOT NULL
    );
    """)

    # Table for licenses and single-device lock binding
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS licenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        license_key TEXT UNIQUE NOT NULL,
        plan_type TEXT NOT NULL,
        duration_days INTEGER NOT NULL,
        created_at TEXT NOT NULL,
        is_active INTEGER DEFAULT 1,
        is_claimed INTEGER DEFAULT 0,
        claimed_at TEXT,
        device_id TEXT,
        last_seen_at TEXT,
        notes TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id TEXT UNIQUE NOT NULL,
        buyer_name TEXT NOT NULL,
        buyer_email TEXT NOT NULL,
        buyer_phone TEXT,
        plan_type TEXT NOT NULL,
        amount_usd REAL NOT NULL,
        license_key TEXT NOT NULL,
        payment_method TEXT DEFAULT 'tarjeta',
        payment_reference TEXT DEFAULT '',
        created_at TEXT NOT NULL,
        status TEXT DEFAULT 'COMPLETADO'
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_profile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_id TEXT UNIQUE NOT NULL,
        full_name TEXT NOT NULL,
        university TEXT,
        lawyer_id TEXT,
        target_exam_date TEXT,
        email TEXT,
        phone TEXT,
        updated_at TEXT NOT NULL
    );
    """)

    # Table for Ambassadors / Referrals (Commissions via Strike)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ambassadors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        email TEXT,
        strike_handle TEXT NOT NULL,
        wallet_type TEXT DEFAULT 'strike',
        discount_usd REAL DEFAULT 5.0,
        commission_vitalicia REAL DEFAULT 5.0,
        commission_trimestral REAL DEFAULT 5.0,
        commission_mensual REAL DEFAULT 3.0,
        total_earned REAL DEFAULT 0.0,
        total_paid REAL DEFAULT 0.0,
        created_at TEXT NOT NULL,
        is_active INTEGER DEFAULT 1
    );
    """)

    # Table for Commission payouts ledger (Strike / Blink)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS commissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id TEXT NOT NULL,
        ambassador_code TEXT NOT NULL,
        buyer_name TEXT NOT NULL,
        plan_type TEXT NOT NULL,
        amount_usd REAL NOT NULL,
        strike_handle TEXT NOT NULL,
        wallet_type TEXT DEFAULT 'strike',
        status TEXT DEFAULT 'PENDIENTE',
        created_at TEXT NOT NULL,
        paid_at TEXT,
        payout_reference TEXT
    );
    """)

    # Ensure orders and ambassador columns exist for backwards compatibility
    try:
        cursor.execute("ALTER TABLE orders ADD COLUMN payment_method TEXT DEFAULT 'tarjeta';")
    except Exception:
        pass
    try:
        cursor.execute("ALTER TABLE orders ADD COLUMN payment_reference TEXT DEFAULT '';")
    except Exception:
        pass
    try:
        cursor.execute("ALTER TABLE orders ADD COLUMN referral_code TEXT DEFAULT '';")
    except Exception:
        pass
    try:
        cursor.execute("ALTER TABLE ambassadors ADD COLUMN wallet_type TEXT DEFAULT 'strike';")
    except Exception:
        pass
    try:
        cursor.execute("ALTER TABLE commissions ADD COLUMN wallet_type TEXT DEFAULT 'strike';")
    except Exception:
        pass

    # Auto-migrate vitalicia commissions and ambassador defaults to $5.00
    try:
        cursor.execute("UPDATE commissions SET amount_usd = 5.0 WHERE plan_type = 'vitalicia' AND amount_usd = 10.0")
        cursor.execute("UPDATE ambassadors SET commission_vitalicia = 5.0 WHERE commission_vitalicia = 10.0")
    except Exception:
        pass

    # Seed default Ambassador if none exist
    cursor.execute("SELECT COUNT(*) FROM ambassadors")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO ambassadors (code, name, email, strike_handle, wallet_type, discount_usd, commission_vitalicia, commission_trimestral, commission_mensual, created_at)
            VALUES (?, ?, ?, ?, 'strike', ?, ?, ?, ?, ?)
        """, ('SUFICIENCIA-VIP', 'Embajador Fundador', 'miltonrb@strike.me', 'miltonrb', 5.0, 5.0, 5.0, 3.0, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # Check if categories table is populated
    cursor.execute("SELECT COUNT(*) FROM categories")
    if cursor.fetchone()[0] == 0:
        for cat in CATEGORIES:
            cursor.execute(
                "INSERT INTO categories (id, name, description, icon) VALUES (?, ?, ?, ?)",
                (cat["id"], cat["name"], cat["description"], cat["icon"])
            )

    # Check if questions table is populated
    cursor.execute("SELECT COUNT(*) FROM questions")
    if cursor.fetchone()[0] == 0:
        for q in QUESTIONS:
            cursor.execute("""
                INSERT INTO questions (
                    category_id, question, option_a, option_b, option_c, option_d,
                    correct_option, legal_basis, justification, distractors_analysis, difficulty
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                q["category_id"], q["question"], q["option_a"], q["option_b"],
                q["option_c"], q["option_d"], q["correct_option"], q["legal_basis"],
                q["justification"], q["distractors_analysis"], q["difficulty"]
            ))

    # Check if flashcards table is populated
    cursor.execute("SELECT COUNT(*) FROM flashcards")
    if cursor.fetchone()[0] == 0:
        for f in FLASHCARDS:
            cursor.execute("""
                INSERT INTO flashcards (category_id, title, prompt, legal_answer, legal_article)
                VALUES (?, ?, ?, ?, ?)
            """, (f["category_id"], f["title"], f["prompt"], f["legal_answer"], f["legal_article"]))

    # Seed 10 Promotional Lifetime Keys if none exist
    cursor.execute("SELECT COUNT(*) FROM licenses WHERE notes LIKE '%Promocional%'")
    if cursor.fetchone()[0] == 0:
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for i in range(1, 11):
            key = generate_key_code(prefix="NOT-VITA")
            cursor.execute("""
                INSERT INTO licenses (license_key, plan_type, duration_days, created_at, is_active, is_claimed, notes)
                VALUES (?, ?, ?, ?, 1, 0, ?)
            """, (key, "vitalicia", -1, now_str, f"Promocional Vitalicia VIP #{i}"))

    conn.commit()
    conn.close()

# --- LICENSE AND SINGLE-DEVICE RESTRICTION FUNCTIONS ---

def validate_or_activate_license(license_key, device_id, max_devices=2):
    """
    Validates a license key and binds it to up to `max_devices` (default 2) devices.
    Supports Firestore first, with fallback to SQLite.
    """
    if not license_key or not device_id:
        return {"success": False, "error": "Clave de licencia y dispositivo requeridos."}

    license_key = license_key.strip().upper()
    device_id = device_id.strip()
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def parse_devices(dev_field):
        if not dev_field:
            return []
        return [d.strip() for d in str(dev_field).split(",") if d.strip()]

    # --- 1. Firestore Attempt ---
    if HAS_FIREBASE:
        try:
            doc_ref = firestore_client.collection("licenses").document(license_key)
            doc = doc_ref.get()
            if doc.exists:
                lic = doc.to_dict()
                if not lic.get("is_active", True):
                    return {"success": False, "error": "Esta clave de licencia ha sido desactivada por el administrador."}

                current_devices = parse_devices(lic.get("device_id"))

                # Already verified on this device
                if device_id in current_devices:
                    doc_ref.update({"last_seen_at": now_str})
                    return {
                        "success": True,
                        "message": f"Licencia verificada en este dispositivo ({len(current_devices)} de {max_devices} autorizados).",
                        "plan_type": lic.get("plan_type", "vitalicia"),
                        "duration_days": lic.get("duration_days", -1),
                        "claimed_at": lic.get("claimed_at"),
                        "device_count": len(current_devices),
                        "max_devices": max_devices
                    }

                # New device, capacity available (< max_devices)
                if len(current_devices) < max_devices:
                    current_devices.append(device_id)
                    new_dev_str = ",".join(current_devices)
                    doc_ref.update({
                        "is_claimed": True,
                        "claimed_at": lic.get("claimed_at") or now_str,
                        "device_id": new_dev_str,
                        "last_seen_at": now_str
                    })
                    return {
                        "success": True,
                        "message": f"¡Licencia activada con éxito en este dispositivo ({len(current_devices)} de {max_devices} autorizados)!",
                        "plan_type": lic.get("plan_type", "vitalicia"),
                        "duration_days": lic.get("duration_days", -1),
                        "claimed_at": lic.get("claimed_at") or now_str,
                        "device_count": len(current_devices),
                        "max_devices": max_devices
                    }

                # Maximum reached (>= max_devices)
                return {
                    "success": False,
                    "error": f"Esta clave de licencia ya ha alcanzado el límite máximo de {max_devices} dispositivos autorizados (ej. tu computadora y tu celular). Si necesitas transferir tu acceso a un nuevo equipo, por favor contacta a soporte técnico.",
                    "is_locked_other_device": True,
                    "device_count": len(current_devices),
                    "max_devices": max_devices
                }
        except Exception as e:
            print(f"[FIREBASE ERROR] validate_or_activate_license: {e}")

    # --- 2. SQLite Fallback ---
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM licenses WHERE license_key = ?", (license_key,))
        lic = cursor.fetchone()

        if not lic:
            conn.close()
            return {"success": False, "error": "La clave de licencia ingresada no existe."}

        lic = dict(lic)
        if not lic["is_active"]:
            conn.close()
            return {"success": False, "error": "Esta clave de licencia ha sido desactivada por el administrador."}

        current_devices = parse_devices(lic.get("device_id"))

        # Case A: This device is already registered
        if device_id in current_devices:
            try:
                cursor.execute("UPDATE licenses SET last_seen_at = ? WHERE id = ?", (now_str, lic["id"]))
                conn.commit()
            except Exception:
                pass
            conn.close()
            return {
                "success": True,
                "message": f"Licencia verificada en este dispositivo ({len(current_devices)} de {max_devices} autorizados).",
                "plan_type": lic["plan_type"],
                "duration_days": lic["duration_days"],
                "claimed_at": lic["claimed_at"],
                "device_count": len(current_devices),
                "max_devices": max_devices
            }

        # Case B: New device, capacity available (< max_devices)
        if len(current_devices) < max_devices:
            current_devices.append(device_id)
            new_dev_str = ",".join(current_devices)
            first_claimed_at = lic["claimed_at"] or now_str
            try:
                cursor.execute("""
                    UPDATE licenses
                    SET is_claimed = 1,
                        claimed_at = COALESCE(claimed_at, ?),
                        device_id = ?,
                        last_seen_at = ?
                    WHERE id = ?
                """, (first_claimed_at, new_dev_str, now_str, lic["id"]))
                conn.commit()
            except Exception as ex:
                print(f"[DATABASE WRITE ERROR] {ex}")
            conn.close()

            # If Firebase is active, also sync to Firestore
            if HAS_FIREBASE:
                try:
                    firestore_client.collection("licenses").document(license_key).set({
                        "license_key": license_key,
                        "plan_type": lic["plan_type"],
                        "duration_days": lic["duration_days"],
                        "created_at": lic.get("created_at", now_str),
                        "is_active": True,
                        "is_claimed": True,
                        "claimed_at": first_claimed_at,
                        "device_id": new_dev_str,
                        "last_seen_at": now_str,
                        "notes": lic.get("notes", "")
                    })
                except Exception:
                    pass

            return {
                "success": True,
                "message": f"¡Licencia activada con éxito en este dispositivo ({len(current_devices)} de {max_devices} autorizados)!",
                "plan_type": lic["plan_type"],
                "duration_days": lic["duration_days"],
                "claimed_at": first_claimed_at,
                "device_count": len(current_devices),
                "max_devices": max_devices
            }

        # Case C: Reached max devices (>= max_devices)
        conn.close()
        return {
            "success": False,
            "error": f"Esta clave de licencia ya ha alcanzado el límite máximo de {max_devices} dispositivos autorizados (ej. tu computadora y tu celular). Si necesitas transferir tu acceso a un nuevo equipo, por favor contacta a soporte técnico.",
            "is_locked_other_device": True,
            "device_count": len(current_devices),
            "max_devices": max_devices
        }
    except Exception as e:
        print(f"[DATABASE ERROR] validate_or_activate_license: {e}")
        return {"success": False, "error": "Error interno al procesar licencia."}

def check_device_license(device_id):
    """Checks if a device has an active bound license (supports multiple devices per key)."""
    if not device_id:
        return None

    dev_clean = str(device_id).strip()

    if HAS_FIREBASE:
        try:
            docs = firestore_client.collection("licenses").where("is_active", "==", True).where("is_claimed", "==", True).stream()
            for doc in docs:
                data = doc.to_dict()
                dev_list = [d.strip() for d in str(data.get("device_id", "")).split(",") if d.strip()]
                if dev_clean in dev_list:
                    return data
        except Exception as e:
            print(f"[FIREBASE ERROR] check_device_license: {e}")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM licenses 
            WHERE (device_id = ? OR instr(',' || device_id || ',', ',' || ? || ',') > 0)
              AND is_active = 1 AND is_claimed = 1
            ORDER BY id DESC LIMIT 1
        """, (dev_clean, dev_clean))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None
    except Exception as e:
        print(f"[DATABASE ERROR] check_device_license: {e}")
        return None

def get_promotional_keys():
    """Returns seeded promotional lifetime keys."""
    if HAS_FIREBASE:
        try:
            docs = firestore_client.collection("licenses").stream()
            promo = []
            for d in docs:
                dt = d.to_dict()
                if "Promocional" in dt.get("notes", "") or "Tarjeta" in dt.get("notes", ""):
                    promo.append(dt)
            if promo:
                promo.sort(key=lambda x: str(x.get("license_key", "")))
                return promo
        except Exception as e:
            print(f"[FIREBASE ERROR] get_promotional_keys: {e}")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, license_key, plan_type, duration_days, created_at, is_claimed, claimed_at, notes 
            FROM licenses 
            WHERE notes LIKE '%Promocional%' OR notes LIKE '%Tarjeta%'
            ORDER BY id ASC
        """)
        rows = cursor.fetchall()
        conn.close()
        return [dict(r) for r in rows]
    except Exception:
        return []

def admin_get_all_licenses():
    if HAS_FIREBASE:
        try:
            docs = firestore_client.collection("licenses").stream()
            results = [d.to_dict() for d in docs]
            if results:
                results.sort(key=lambda x: str(x.get("created_at", "")), reverse=True)
                return results
        except Exception as e:
            print(f"[FIREBASE ERROR] admin_get_all_licenses: {e}")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, license_key, plan_type, duration_days, created_at, is_active, 
                   is_claimed, claimed_at, device_id, last_seen_at, notes
            FROM licenses
            ORDER BY id DESC
        """)
        rows = cursor.fetchall()
        conn.close()
        return [dict(r) for r in rows]
    except Exception:
        return []

def admin_create_license(plan_type="60_dias", duration_days=None, notes=""):
    if duration_days is None:
        if plan_type == "vitalicia":
            duration_days = -1
        elif plan_type == "60_dias" or plan_type == "90_dias":
            duration_days = 60
        else:
            duration_days = 30

    prefix_map = {
        "vitalicia": "NOT-VITA",
        "60_dias": "NOT-BIME",
        "90_dias": "NOT-TRIM",
        "30_dias": "NOT-MENS"
    }
    prefix = prefix_map.get(plan_type, "NOT")
    key = generate_key_code(prefix=prefix)
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lic_data = {
        "license_key": key,
        "plan_type": plan_type,
        "duration_days": duration_days,
        "created_at": now_str,
        "is_active": True,
        "is_claimed": False,
        "claimed_at": None,
        "device_id": None,
        "last_seen_at": None,
        "notes": notes
    }

    if HAS_FIREBASE:
        try:
            firestore_client.collection("licenses").document(key).set(lic_data)
        except Exception as e:
            print(f"[FIREBASE ERROR] admin_create_license: {e}")

    lic_id = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO licenses (license_key, plan_type, duration_days, created_at, is_active, is_claimed, notes)
            VALUES (?, ?, ?, ?, 1, 0, ?)
        """, (key, plan_type, duration_days, now_str, notes))
        lic_id = cursor.lastrowid
        conn.commit()
        conn.close()
    except Exception as ex:
        print(f"[DATABASE WRITE ERROR] admin_create_license: {ex}")

    return {"id": lic_id or key, "key": key, "plan_type": plan_type, "duration_days": duration_days}

def admin_reset_device(license_id):
    """Allows admin to unbind a license from a device if customer legitimately changed device."""
    lic_id_str = str(license_id).strip()

    if HAS_FIREBASE:
        try:
            # Check by doc ID (license_key) or search
            lic_ref = firestore_client.collection("licenses").document(lic_id_str)
            if lic_ref.get().exists:
                lic_ref.update({
                    "device_id": None,
                    "is_claimed": False,
                    "claimed_at": None
                })
                return True
            else:
                # Query by field
                docs = firestore_client.collection("licenses").where("license_key", "==", lic_id_str).stream()
                for d in docs:
                    d.reference.update({
                        "device_id": None,
                        "is_claimed": False,
                        "claimed_at": None
                    })
                    return True
        except Exception as e:
            print(f"[FIREBASE ERROR] admin_reset_device: {e}")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE licenses
            SET device_id = NULL,
                is_claimed = 0,
                claimed_at = NULL
            WHERE id = ? OR license_key = ?
        """, (license_id, lic_id_str))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(f"[DATABASE ERROR] admin_reset_device: {ex}")
        return True

# --- EXAM AND QUESTIONS FUNCTIONS ---

def get_categories():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.*, COUNT(q.id) as question_count 
        FROM categories c
        LEFT JOIN questions q ON c.id = q.category_id
        GROUP BY c.id
        ORDER BY c.rowid
    """)
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_random_exam_questions(limit=20):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, category_id, question, option_a, option_b, option_c, option_d,
               correct_option, legal_basis, justification, distractors_analysis, difficulty
        FROM questions
        ORDER BY RANDOM()
        LIMIT ?
    """, (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_questions_by_category(category_id=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    if category_id and category_id != "all":
        cursor.execute("""
            SELECT q.*, c.name as category_name
            FROM questions q
            JOIN categories c ON q.category_id = c.id
            WHERE q.category_id = ?
            ORDER BY q.id
        """, (category_id,))
    else:
        cursor.execute("""
            SELECT q.*, c.name as category_name
            FROM questions q
            JOIN categories c ON q.category_id = c.id
            ORDER BY q.id
        """)
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_flashcards(category_id=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    if category_id and category_id != "all":
        cursor.execute("""
            SELECT f.*, c.name as category_name
            FROM flashcards f
            JOIN categories c ON f.category_id = c.id
            WHERE f.category_id = ?
            ORDER BY f.id
        """, (category_id,))
    else:
        cursor.execute("""
            SELECT f.*, c.name as category_name
            FROM flashcards f
            JOIN categories c ON f.category_id = c.id
            ORDER BY f.id
        """)
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def save_exam_attempt(score, total, correct, incorrect, time_spent, passed, answers_detail):
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    answers_json = json.dumps(answers_detail, ensure_ascii=False) if isinstance(answers_detail, (dict, list)) else str(answers_detail)
    attempt_data = {
        "created_at": now_str,
        "score": score,
        "total_questions": total,
        "correct_count": correct,
        "incorrect_count": incorrect,
        "time_spent_seconds": time_spent,
        "passed": 1 if passed else 0,
        "answers_json": answers_json
    }

    if HAS_FIREBASE:
        try:
            doc_ref = firestore_client.collection("exam_attempts").document()
            attempt_data_fs = dict(attempt_data)
            attempt_data_fs["id"] = doc_ref.id
            doc_ref.set(attempt_data_fs)
            
            # Persist locally in SQLite if writable
            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO exam_attempts (
                        created_at, score, total_questions, correct_count, incorrect_count,
                        time_spent_seconds, passed, answers_json
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    now_str, score, total, correct, incorrect, time_spent, 1 if passed else 0,
                    answers_json
                ))
                conn.commit()
                conn.close()
            except Exception:
                pass
                
            return doc_ref.id
        except Exception as e:
            print(f"[FIREBASE ERROR] save_exam_attempt: {e}")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO exam_attempts (
                created_at, score, total_questions, correct_count, incorrect_count,
                time_spent_seconds, passed, answers_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            now_str, score, total, correct, incorrect, time_spent, 1 if passed else 0,
            answers_json
        ))
        attempt_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return attempt_id
    except Exception as ex:
        print(f"[DATABASE ERROR] save_exam_attempt SQLite: {ex}")
        import uuid
        return f"local_{uuid.uuid4().hex[:8]}"

def get_exam_history(limit=20):
    if HAS_FIREBASE:
        try:
            docs = firestore_client.collection("exam_attempts").stream()
            results = []
            for d in docs:
                item = d.to_dict()
                if "id" not in item:
                    item["id"] = d.id
                results.append(item)
            if results:
                results.sort(key=lambda x: str(x.get("created_at", "")), reverse=True)
                return results[:limit]
        except Exception as e:
            print(f"[FIREBASE ERROR] get_exam_history: {e}")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, created_at, score, total_questions, correct_count,
                   incorrect_count, time_spent_seconds, passed
            FROM exam_attempts
            ORDER BY id DESC
            LIMIT ?
        """, (limit,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(r) for r in rows]
    except Exception:
        return []

def get_exam_attempt_by_id(attempt_id):
    if not attempt_id:
        return None
    attempt_id_str = str(attempt_id).strip()

    if HAS_FIREBASE:
        try:
            doc = firestore_client.collection("exam_attempts").document(attempt_id_str).get()
            if doc.exists:
                data = doc.to_dict()
                if "id" not in data:
                    data["id"] = doc.id
                if "answers_json" in data and isinstance(data["answers_json"], str):
                    try:
                        data["answers_detail"] = json.loads(data["answers_json"])
                    except Exception:
                        data["answers_detail"] = {}
                elif "answers_detail" not in data:
                    data["answers_detail"] = {}
                return data

            if attempt_id_str.isdigit():
                docs = firestore_client.collection("exam_attempts").where("id", "==", int(attempt_id_str)).stream()
                for d in docs:
                    data = d.to_dict()
                    data["id"] = d.id
                    if "answers_json" in data and isinstance(data["answers_json"], str):
                        try:
                            data["answers_detail"] = json.loads(data["answers_json"])
                        except Exception:
                            data["answers_detail"] = {}
                    return data
        except Exception as e:
            print(f"[FIREBASE ERROR] get_exam_attempt_by_id: {e}")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exam_attempts WHERE id = ?", (attempt_id_str,))
        row = cursor.fetchone()
        conn.close()
        if row:
            data = dict(row)
            try:
                data["answers_detail"] = json.loads(data["answers_json"])
            except Exception:
                data["answers_detail"] = {}
            return data
    except Exception as ex:
        print(f"[DATABASE ERROR] get_exam_attempt_by_id SQLite: {ex}")

    return None

def get_dashboard_stats():
    total_attempts = 0
    total_score = 0.0
    passed_count = 0

    if HAS_FIREBASE:
        try:
            docs = list(firestore_client.collection("exam_attempts").stream())
            total_attempts = len(docs)
            for d in docs:
                data = d.to_dict()
                total_score += float(data.get("score", 0))
                if data.get("passed") in (1, True, "1"):
                    passed_count += 1
        except Exception as e:
            print(f"[FIREBASE ERROR] get_dashboard_stats: {e}")

    if total_attempts == 0:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*), AVG(score), SUM(passed) FROM exam_attempts")
            row = cursor.fetchone()
            if row and row[0]:
                total_attempts = row[0]
                total_score = (row[1] or 0.0) * total_attempts
                passed_count = row[2] or 0
            conn.close()
        except Exception:
            pass

    total_questions = len(QUESTIONS)
    total_flashcards = len(FLASHCARDS)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM questions")
        tq = cursor.fetchone()[0]
        if tq > 0:
            total_questions = tq
        cursor.execute("SELECT COUNT(*) FROM flashcards")
        tf = cursor.fetchone()[0]
        if tf > 0:
            total_flashcards = tf
        conn.close()
    except Exception:
        pass

    avg_score = round(total_score / total_attempts, 1) if total_attempts > 0 else 0.0
    pass_rate = round((passed_count / total_attempts) * 100, 1) if total_attempts > 0 else 0.0

    return {
        "total_attempts": total_attempts,
        "avg_score": avg_score,
        "passed_count": passed_count,
        "pass_rate": pass_rate,
        "total_questions": total_questions,
        "total_flashcards": total_flashcards
    }


def create_order(order_id, buyer_name, buyer_email, buyer_phone, plan_type, amount_usd, license_key, payment_method="tarjeta", payment_reference="", referral_code=""):
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ref_clean = str(referral_code).strip().upper() if referral_code else ""

    if HAS_FIREBASE:
        try:
            firestore_client.collection("orders").document(order_id).set({
                "order_id": order_id,
                "buyer_name": buyer_name,
                "buyer_email": buyer_email,
                "buyer_phone": buyer_phone,
                "plan_type": plan_type,
                "amount_usd": float(amount_usd),
                "license_key": license_key,
                "payment_method": payment_method,
                "payment_reference": payment_reference,
                "referral_code": ref_clean,
                "created_at": now_str,
                "status": "COMPLETADO"
            })
            return True
        except Exception as e:
            print(f"[FIREBASE ERROR] create_order: {e}")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO orders (order_id, buyer_name, buyer_email, buyer_phone, plan_type, amount_usd, license_key, payment_method, payment_reference, referral_code, created_at, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'COMPLETADO')
    """, (order_id, buyer_name, buyer_email, buyer_phone, plan_type, amount_usd, license_key, payment_method, payment_reference, ref_clean, now_str))
    conn.commit()
    conn.close()
    return True

# --- PROGRAMA DE EMBAJADORES Y COMISIONES STRIKE ---

def get_ambassador(code):
    if not code:
        return None
    code_clean = str(code).strip().upper()
    if HAS_FIREBASE:
        try:
            doc = firestore_client.collection("ambassadors").document(code_clean).get()
            if doc.exists:
                data = doc.to_dict()
                if data.get("is_active", True):
                    return data
            return None
        except Exception as e:
            print(f"[FIREBASE ERROR] get_ambassador: {e}")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ambassadors WHERE UPPER(code) = ? AND is_active = 1", (code_clean,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def create_or_update_ambassador(code, name, strike_handle, email="", discount_usd=5.0, commission_vitalicia=5.0, commission_trimestral=5.0, commission_mensual=3.0, wallet_type="strike"):
    code_clean = str(code).strip().upper()
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Auto-detect wallet type if handle includes domain or if specified
    raw_handle = str(strike_handle).strip()
    w_type = str(wallet_type).strip().lower() if wallet_type else "strike"
    if "blink" in raw_handle.lower() or "blink" in w_type:
        w_type = "blink"
    else:
        w_type = "strike"

    clean_handle = raw_handle
    for pfx in ["https://pay.blink.sv/", "http://pay.blink.sv/", "pay.blink.sv/", "https://strike.me/", "http://strike.me/", "strike.me/"]:
        clean_handle = clean_handle.replace(pfx, "")
    for sfx in ["@blink.sv", "blink.sv", "@strike.me", "strike.me"]:
        if clean_handle.endswith(sfx):
            clean_handle = clean_handle[:-len(sfx)]
    clean_handle = clean_handle.replace("@", "").strip("/ ")

    doc_data = {
        "code": code_clean,
        "name": name.strip(),
        "email": email.strip(),
        "strike_handle": clean_handle,
        "wallet_type": w_type,
        "discount_usd": float(discount_usd),
        "commission_vitalicia": float(commission_vitalicia),
        "commission_trimestral": float(commission_trimestral),
        "commission_mensual": float(commission_mensual),
        "total_earned": 0.0,
        "total_paid": 0.0,
        "created_at": now_str,
        "is_active": 1
    }

    if HAS_FIREBASE:
        try:
            firestore_client.collection("ambassadors").document(code_clean).set(doc_data, merge=True)
            return True
        except Exception as e:
            print(f"[FIREBASE ERROR] create_ambassador: {e}")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ambassadors (code, name, email, strike_handle, wallet_type, discount_usd, commission_vitalicia, commission_trimestral, commission_mensual, total_earned, total_paid, created_at, is_active)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0.0, 0.0, ?, 1)
        ON CONFLICT(code) DO UPDATE SET
            name = excluded.name,
            email = excluded.email,
            strike_handle = excluded.strike_handle,
            wallet_type = excluded.wallet_type,
            discount_usd = excluded.discount_usd,
            commission_vitalicia = excluded.commission_vitalicia,
            commission_trimestral = excluded.commission_trimestral,
            commission_mensual = excluded.commission_mensual
    """, (code_clean, doc_data["name"], doc_data["email"], doc_data["strike_handle"], doc_data["wallet_type"], doc_data["discount_usd"], doc_data["commission_vitalicia"], doc_data["commission_trimestral"], doc_data["commission_mensual"], now_str))
    conn.commit()
    conn.close()
    return True

def get_all_ambassadors():
    if HAS_FIREBASE:
        try:
            docs = firestore_client.collection("ambassadors").stream()
            results = [d.to_dict() for d in docs]
            results.sort(key=lambda x: str(x.get("name", "")))
            return results
        except Exception as e:
            print(f"[FIREBASE ERROR] get_all_ambassadors: {e}")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ambassadors ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def record_commission(order_id, ambassador_code, buyer_name, plan_type):
    amb = get_ambassador(ambassador_code)
    if not amb:
        return None

    # Calculate commission based on plan
    if plan_type == "vitalicia":
        comm_amount = float(amb.get("commission_vitalicia", 5.0))
    elif plan_type == "90_dias":
        comm_amount = float(amb.get("commission_trimestral", 5.0))
    else:
        comm_amount = float(amb.get("commission_mensual", 3.0))

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    strike_handle = amb.get("strike_handle", "")
    wallet_type = amb.get("wallet_type", "strike")
    if wallet_type == "blink":
        payout_url = f"https://pay.blink.sv/{strike_handle}"
    else:
        payout_url = f"https://strike.me/{strike_handle}"

    comm_id = f"COM-{secrets.token_hex(4).upper()}"

    comm_data = {
        "comm_id": comm_id,
        "order_id": order_id,
        "ambassador_code": amb["code"],
        "ambassador_name": amb.get("name", "Embajador"),
        "buyer_name": buyer_name,
        "plan_type": plan_type,
        "amount_usd": comm_amount,
        "strike_handle": strike_handle,
        "wallet_type": wallet_type,
        "payout_url": payout_url,
        "status": "PENDIENTE",
        "created_at": now_str,
        "paid_at": "",
        "payout_reference": ""
    }

    if HAS_FIREBASE:
        try:
            firestore_client.collection("commissions").document(comm_id).set(comm_data)
            # update ambassador total_earned
            amb_ref = firestore_client.collection("ambassadors").document(amb["code"])
            amb_doc = amb_ref.get()
            if amb_doc.exists:
                cur_earned = float(amb_doc.to_dict().get("total_earned", 0.0))
                amb_ref.update({"total_earned": cur_earned + comm_amount})
            return comm_data
        except Exception as e:
            print(f"[FIREBASE ERROR] record_commission: {e}")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO commissions (order_id, ambassador_code, buyer_name, plan_type, amount_usd, strike_handle, wallet_type, status, created_at, paid_at, payout_reference)
        VALUES (?, ?, ?, ?, ?, ?, ?, 'PENDIENTE', ?, '', '')
    """, (order_id, amb["code"], buyer_name, plan_type, comm_amount, strike_handle, wallet_type, now_str))
    cursor.execute("""
        UPDATE ambassadors SET total_earned = total_earned + ? WHERE code = ?
    """, (comm_amount, amb["code"]))
    conn.commit()
    conn.close()
    return comm_data

def get_commissions(status=None):
    if HAS_FIREBASE:
        try:
            query = firestore_client.collection("commissions")
            if status:
                query = query.where("status", "==", status)
            docs = query.stream()
            results = [d.to_dict() for d in docs]
            results.sort(key=lambda x: str(x.get("created_at", "")), reverse=True)
            return results
        except Exception as e:
            print(f"[FIREBASE ERROR] get_commissions: {e}")

    conn = get_db_connection()
    cursor = conn.cursor()
    if status:
        cursor.execute("SELECT * FROM commissions WHERE status = ? ORDER BY id DESC", (status,))
    else:
        cursor.execute("SELECT * FROM commissions ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def mark_commission_paid(commission_id, payout_reference="Pago vía Lightning"):
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if HAS_FIREBASE:
        try:
            # Check by doc id or search
            comm_ref = firestore_client.collection("commissions").document(str(commission_id))
            comm_doc = comm_ref.get()
            if comm_doc.exists:
                c_data = comm_doc.to_dict()
                amount = float(c_data.get("amount_usd", 0.0))
                amb_code = c_data.get("ambassador_code")
                comm_ref.update({
                    "status": "PAGADO",
                    "paid_at": now_str,
                    "payout_reference": payout_reference
                })
                if amb_code:
                    amb_ref = firestore_client.collection("ambassadors").document(amb_code)
                    a_doc = amb_ref.get()
                    if a_doc.exists:
                        cur_paid = float(a_doc.to_dict().get("total_paid", 0.0))
                        amb_ref.update({"total_paid": cur_paid + amount})
                return True
        except Exception as e:
            print(f"[FIREBASE ERROR] mark_commission_paid: {e}")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM commissions WHERE id = ? OR order_id = ?", (commission_id, commission_id))
    row = cursor.fetchone()
    if row:
        r_dict = dict(row)
        cursor.execute("""
            UPDATE commissions SET status = 'PAGADO', paid_at = ?, payout_reference = ? WHERE id = ?
        """, (now_str, payout_reference, r_dict["id"]))
        cursor.execute("""
            UPDATE ambassadors SET total_paid = total_paid + ? WHERE code = ?
        """, (r_dict["amount_usd"], r_dict["ambassador_code"]))
        conn.commit()
    conn.close()
    return True

def admin_get_orders():
    if HAS_FIREBASE:
        try:
            docs = firestore_client.collection("orders").stream()
            results = [d.to_dict() for d in docs]
            results.sort(key=lambda x: str(x.get("created_at", "")), reverse=True)
            return results
        except Exception as e:
            print(f"[FIREBASE ERROR] admin_get_orders: {e}")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM orders ORDER BY id DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_user_profile(device_id):
    default_prof = {
        "device_id": device_id or "",
        "full_name": "Licenciado(a) Aspirante",
        "university": "Facultad de Jurisprudencia y Ciencias Sociales",
        "lawyer_id": "En trámite / Pendiente",
        "target_exam_date": "2026-11-20",
        "email": "",
        "phone": ""
    }
    if not device_id:
        return default_prof

    if HAS_FIREBASE:
        try:
            doc = firestore_client.collection("user_profile").document(device_id).get()
            if doc.exists:
                res = default_prof.copy()
                res.update(doc.to_dict())
                return res
            return default_prof
        except Exception as e:
            print(f"[FIREBASE ERROR] get_user_profile: {e}")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_profile WHERE device_id = ?", (device_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return default_prof

def save_user_profile(device_id, data):
    if not device_id:
        return False
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    doc_data = {
        "device_id": device_id,
        "full_name": data.get("full_name", "Licenciado(a) Aspirante"),
        "university": data.get("university", ""),
        "lawyer_id": data.get("lawyer_id", ""),
        "target_exam_date": data.get("target_exam_date", ""),
        "email": data.get("email", ""),
        "phone": data.get("phone", ""),
        "updated_at": now_str
    }

    if HAS_FIREBASE:
        try:
            firestore_client.collection("user_profile").document(device_id).set(doc_data, merge=True)
            return True
        except Exception as e:
            print(f"[FIREBASE ERROR] save_user_profile: {e}")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO user_profile (device_id, full_name, university, lawyer_id, target_exam_date, email, phone, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(device_id) DO UPDATE SET
            full_name = excluded.full_name,
            university = excluded.university,
            lawyer_id = excluded.lawyer_id,
            target_exam_date = excluded.target_exam_date,
            email = excluded.email,
            phone = excluded.phone,
            updated_at = excluded.updated_at
    """, (
        device_id,
        doc_data["full_name"],
        doc_data["university"],
        doc_data["lawyer_id"],
        doc_data["target_exam_date"],
        doc_data["email"],
        doc_data["phone"],
        now_str
    ))
    conn.commit()
    conn.close()
    return True

if __name__ == "__main__":
    init_db()
    print("Database and licenses initialized successfully!")
