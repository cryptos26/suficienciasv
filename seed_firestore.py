"""
seed_firestore.py
Script de migración y sembrado masivo de datos a Google Firebase Firestore
para el Simulador de Notariado de El Salvador.
"""
import os
import sys
import json
from datetime import datetime

try:
    import firebase_admin
    from firebase_admin import credentials, firestore
except ImportError:
    print("Error: 'firebase-admin' no está instalado. Ejecuta: pip install firebase-admin")
    sys.exit(1)

from questions_seed import CATEGORIES, QUESTIONS, FLASHCARDS

# 10 Claves Oficiales Promocionales Vitalicias
PROMO_KEYS = [
    "NOT-VITA-ZTMA-BUQM",
    "NOT-VITA-PXSW-ERUT",
    "NOT-VITA-VP45-NZKP",
    "NOT-VITA-UYAN-5RB3",
    "NOT-VITA-EKUT-64X8",
    "NOT-VITA-RNB7-QJNK",
    "NOT-VITA-9P3A-MW2S",
    "NOT-VITA-ZFZM-DKMJ",
    "NOT-VITA-SGNS-Q9NE",
    "NOT-VITA-PLVL-4T8V"
]

def get_firestore_client():
    if firebase_admin._apps:
        return firestore.client()

    cred_env = os.environ.get("FIREBASE_SERVICE_ACCOUNT")
    cred_file = os.path.join(os.path.dirname(__file__), "serviceAccountKey.json")

    if cred_env:
        try:
            cred_dict = json.loads(cred_env)
            cred = credentials.Certificate(cred_dict)
            firebase_admin.initialize_app(cred)
            print("[OK] Conectado a Firebase mediante FIREBASE_SERVICE_ACCOUNT")
            return firestore.client()
        except Exception as e:
            print(f"Error parseando FIREBASE_SERVICE_ACCOUNT: {e}")
            sys.exit(1)
    elif os.path.exists(cred_file):
        cred = credentials.Certificate(cred_file)
        firebase_admin.initialize_app(cred)
        print("[OK] Conectado a Firebase mediante serviceAccountKey.json")
        return firestore.client()
    else:
        print("\n[!] No se encontraron credenciales de Firebase.")
        print("    Por favor coloca tu archivo 'serviceAccountKey.json' en esta carpeta")
        print("    o define la variable de entorno 'FIREBASE_SERVICE_ACCOUNT'.")
        sys.exit(1)

def seed():
    db = get_firestore_client()
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n--- INICIANDO SEMBRADO DE FIRESTORE ---")

    # 1. Categorías
    print(f"Subiendo {len(CATEGORIES)} categorías...")
    for cat in CATEGORIES:
        db.collection("categories").document(cat["id"]).set({
            "id": cat["id"],
            "name": cat["name"],
            "description": cat["description"],
            "icon": cat["icon"]
        }, merge=True)
    print("[OK] Categorías cargadas con éxito.")

    # 2. Preguntas
    print(f"Subiendo {len(QUESTIONS)} casos prácticos forenses...")
    for i, q in enumerate(QUESTIONS, start=1):
        doc_id = str(i)
        db.collection("questions").document(doc_id).set({
            "id": i,
            "category_id": q["category_id"],
            "question": q["question"],
            "option_a": q["option_a"],
            "option_b": q["option_b"],
            "option_c": q["option_c"],
            "option_d": q["option_d"],
            "correct_option": q["correct_option"],
            "legal_basis": q["legal_basis"],
            "justification": q["justification"],
            "distractors_analysis": q["distractors_analysis"],
            "difficulty": q.get("difficulty", "Media")
        }, merge=True)
    print("[OK] Banco de preguntas cargado con éxito.")

    # 3. Flashcards
    print(f"Subiendo {len(FLASHCARDS)} fichas mnemotécnicas de plazos...")
    for i, f in enumerate(FLASHCARDS, start=1):
        doc_id = str(i)
        db.collection("flashcards").document(doc_id).set({
            "id": i,
            "category_id": f["category_id"],
            "title": f["title"],
            "prompt": f["prompt"],
            "legal_answer": f["legal_answer"],
            "legal_article": f["legal_article"]
        }, merge=True)
    print("[OK] Fichas mnemotécnicas cargadas con éxito.")

    # 4. 10 Claves Promocionales Vitalicias
    print(f"Sembrando las 10 claves promocionales vitalicias...")
    for i, key in enumerate(PROMO_KEYS, start=1):
        doc_ref = db.collection("licenses").document(key)
        doc = doc_ref.get()
        if not doc.exists:
            doc_ref.set({
                "license_key": key,
                "plan_type": "vitalicia",
                "duration_days": -1,
                "created_at": now_str,
                "is_active": True,
                "is_claimed": False,
                "claimed_at": None,
                "device_id": None,
                "last_seen_at": None,
                "notes": f"Promocional Vitalicia VIP #{i}"
            })
    print("[OK] 10 Claves promocionales vitalicias sembradas con éxito.")

    print("\n¡Sembrado completado exitosamente en Google Firebase Firestore!")

if __name__ == "__main__":
    seed()
