from flask import Flask, render_template, request, jsonify, redirect, url_for, session, make_response
from datetime import datetime
import database as db
import payment_config
import urllib.parse
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)
app.secret_key = "notariado_sv_secret_key_2026_super_secure"
ADMIN_PIN = "notario2026"

class VercelPathMiddleware:
    """WSGI middleware ensuring proper path resolution when running under Vercel Serverless."""
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '')
        for prefix in ['/api/index.py', '/api/index']:
            if path.startswith(prefix):
                path = path[len(prefix):]
                break
        environ['PATH_INFO'] = path if (path and path.startswith('/')) else ('/' + path if path else '/')
        return self.wsgi_app(environ, start_response)

app.wsgi_app = VercelPathMiddleware(app.wsgi_app)

# Ensure DB is initialized
db.init_db()

def get_device_id_from_request():
    """Extracts device_id from header, cookie or query param."""
    return request.headers.get("X-Device-Id") or request.cookies.get("notariado_device_id") or request.args.get("device_id")

def is_device_licensed(device_id):
    if not device_id:
        return False
    lic = db.check_device_license(device_id)
    return lic is not None

@app.route("/")
@app.route("/api")
@app.route("/api/index")
@app.route("/api/index.py")
def index():
    stats = db.get_dashboard_stats()
    categories = db.get_categories()
    history = db.get_exam_history(limit=5)
    device_id = get_device_id_from_request()
    license_info = db.check_device_license(device_id) if device_id else None
    return render_template(
        "index.html", 
        stats=stats, 
        categories=categories, 
        recent_history=history,
        license_info=license_info
    )

@app.route("/activar", methods=["GET", "POST"])
def activar():
    device_id = get_device_id_from_request()
    if request.method == "POST":
        data = request.get_json() or {}
        key = data.get("license_key", "").strip()
        client_device_id = data.get("device_id") or device_id

        if not key:
            return jsonify({"success": False, "error": "Por favor ingresa tu clave de licencia."}), 400
        if not client_device_id:
            return jsonify({"success": False, "error": "No se pudo identificar el dispositivo. Habilite cookies/almacenamiento local."}), 400

        result = db.validate_or_activate_license(key, client_device_id)
        if result["success"]:
            # Set cookie for persistence
            resp = make_response(jsonify(result))
            resp.set_cookie("notariado_device_id", client_device_id, max_age=365*24*3600, httponly=False)
            return resp
        return jsonify(result), 400

    license_info = db.check_device_license(device_id) if device_id else None
    return render_template("activate.html", license_info=license_info)

@app.route("/api/license/status", methods=["GET"])
def api_license_status():
    device_id = get_device_id_from_request()
    lic = db.check_device_license(device_id) if device_id else None
    if lic:
        return jsonify({
            "is_licensed": True,
            "plan_type": lic["plan_type"],
            "duration_days": lic["duration_days"],
            "claimed_at": lic["claimed_at"],
            "notes": lic["notes"]
        })
    return jsonify({"is_licensed": False})

@app.route("/simulador")
def simulador():
    device_id = get_device_id_from_request()
    license_info = db.check_device_license(device_id) if device_id else None
    return render_template("exam.html", license_info=license_info)

@app.route("/api/exam/generate", methods=["GET"])
def api_generate_exam():
    device_id = get_device_id_from_request()
    is_licensed = is_device_licensed(device_id)

    # Free demo: allow 10 questions if not licensed, full 20 questions if licensed
    limit = 20 if is_licensed else 10

    raw_questions = db.get_random_exam_questions(limit=limit)
    sanitized = []
    for q in raw_questions:
        sanitized.append({
            "id": q["id"],
            "category_id": q["category_id"],
            "question": q["question"],
            "option_a": q["option_a"],
            "option_b": q["option_b"],
            "option_c": q["option_c"],
            "option_d": q["option_d"],
            "difficulty": q["difficulty"]
        })

    return jsonify({
        "success": True,
        "is_licensed": is_licensed,
        "total": len(sanitized),
        "duration_minutes": 25 if is_licensed else 15,
        "questions": sanitized
    })

@app.route("/api/exam/submit", methods=["POST"])
def api_submit_exam():
    data = request.get_json() or {}
    user_answers = data.get("answers", {})
    time_spent = int(data.get("time_spent_seconds", 0))

    if not user_answers:
        return jsonify({"success": False, "error": "No se recibieron respuestas"}), 400

    q_ids = [int(qid) for qid in user_answers.keys()]
    
    conn = db.get_db_connection()
    cursor = conn.cursor()
    placeholders = ",".join("?" for _ in q_ids)
    cursor.execute(f"""
        SELECT q.*, c.name as category_name
        FROM questions q
        JOIN categories c ON q.category_id = c.id
        WHERE q.id IN ({placeholders})
    """, q_ids)
    questions_map = {row["id"]: dict(row) for row in cursor.fetchall()}
    conn.close()

    total = len(q_ids)
    correct_count = 0
    detailed_results = []
    cat_stats = {}

    for qid_str, user_choice in user_answers.items():
        qid = int(qid_str)
        q = questions_map.get(qid)
        if not q:
            continue

        cat_id = q["category_id"]
        if cat_id not in cat_stats:
            cat_stats[cat_id] = {"name": q["category_name"], "total": 0, "correct": 0}
        cat_stats[cat_id]["total"] += 1

        is_correct = (user_choice == q["correct_option"])
        if is_correct:
            correct_count += 1
            cat_stats[cat_id]["correct"] += 1

        detailed_results.append({
            "id": q["id"],
            "category_id": q["category_id"],
            "category_name": q["category_name"],
            "question": q["question"],
            "option_a": q["option_a"],
            "option_b": q["option_b"],
            "option_c": q["option_c"],
            "option_d": q["option_d"],
            "user_choice": user_choice,
            "correct_option": q["correct_option"],
            "is_correct": is_correct,
            "legal_basis": q["legal_basis"],
            "justification": q["justification"],
            "distractors_analysis": q["distractors_analysis"],
            "difficulty": q["difficulty"]
        })

    incorrect_count = total - correct_count
    score = round((correct_count / total) * 10.0, 1) if total > 0 else 0.0
    passed = score >= 7.0

    attempt_id = db.save_exam_attempt(
        score=score,
        total=total,
        correct=correct_count,
        incorrect=incorrect_count,
        time_spent=time_spent,
        passed=passed,
        answers_detail={
            "results": detailed_results,
            "cat_stats": cat_stats
        }
    )

    return jsonify({
        "success": True,
        "attempt_id": attempt_id,
        "score": score,
        "passed": passed,
        "redirect_url": f"/resultado/{attempt_id}"
    })

@app.route("/resultado/<int:attempt_id>")
def resultado_examen(attempt_id):
    attempt = db.get_exam_attempt_by_id(attempt_id)
    if not attempt:
        return redirect(url_for("index"))
    device_id = get_device_id_from_request()
    license_info = db.check_device_license(device_id) if device_id else None
    return render_template("results.html", attempt=attempt, license_info=license_info)

@app.route("/practica")
def practica():
    categories = db.get_categories()
    device_id = get_device_id_from_request()
    license_info = db.check_device_license(device_id) if device_id else None
    return render_template("practice.html", categories=categories, license_info=license_info)

@app.route("/api/practice/questions", methods=["GET"])
def api_practice_questions():
    category_id = request.args.get("category", "all")
    device_id = get_device_id_from_request()
    is_licensed = is_device_licensed(device_id)

    questions = db.get_questions_by_category(category_id)
    # If not licensed, limit practice questions as sample
    if not is_licensed:
        questions = questions[:4]

    return jsonify({
        "success": True,
        "is_licensed": is_licensed,
        "questions": questions
    })

@app.route("/flashcards")
def flashcards():
    categories = db.get_categories()
    device_id = get_device_id_from_request()
    license_info = db.check_device_license(device_id) if device_id else None
    return render_template("flashcards.html", categories=categories, license_info=license_info)

@app.route("/api/flashcards", methods=["GET"])
def api_get_flashcards():
    category_id = request.args.get("category", "all")
    device_id = get_device_id_from_request()
    is_licensed = is_device_licensed(device_id)

    cards = db.get_flashcards(category_id)
    if not is_licensed:
        cards = cards[:3] # sample for free users

    return jsonify({
        "success": True,
        "is_licensed": is_licensed,
        "flashcards": cards
    })

@app.route("/historial")
def historial():
    history = db.get_exam_history(limit=50)
    stats = db.get_dashboard_stats()
    device_id = get_device_id_from_request()
    license_info = db.check_device_license(device_id) if device_id else None
    return render_template("history.html", history=history, stats=stats, license_info=license_info)

@app.route("/perfil")
def perfil():
    device_id = get_device_id_from_request()
    profile = db.get_user_profile(device_id)
    license_info = db.check_device_license(device_id) if device_id else None
    stats = db.get_dashboard_stats()
    history = db.get_exam_history(limit=10)

    # Calculate days remaining to target exam
    days_left = None
    if profile.get("target_exam_date"):
        try:
            target_dt = datetime.strptime(profile["target_exam_date"], "%Y-%m-%d").date()
            today = datetime.now().date()
            days_left = max(0, (target_dt - today).days)
        except Exception:
            days_left = None

    return render_template(
        "profile.html",
        profile=profile,
        license_info=license_info,
        stats=stats,
        history=history,
        days_left=days_left,
        device_id=device_id
    )

@app.route("/api/profile/update", methods=["POST"])
def api_profile_update():
    data = request.get_json() or {}
    device_id = data.get("device_id") or get_device_id_from_request()
    if not device_id:
        return jsonify({"success": False, "error": "Dispositivo no identificado"}), 400

    db.save_user_profile(device_id, data)
    return jsonify({"success": True, "message": "Perfil actualizado correctamente"})

@app.route("/terminos")
def terminos():
    return render_template("terms.html")

@app.route("/comprar")
def comprar():
    plan = request.args.get("plan", "vitalicia")
    device_id = get_device_id_from_request()
    license_info = db.check_device_license(device_id) if device_id else None
    payments = payment_config.get_payment_summary()
    return render_template("checkout.html", selected_plan=plan, license_info=license_info, payment_config=payments)

@app.route("/api/referral/validate", methods=["GET"])
def api_referral_validate():
    code = request.args.get("code", "").strip()
    plan = request.args.get("plan", "vitalicia")
    if not code:
        return jsonify({"valid": False, "error": "Ingresa un código"}), 400

    amb = db.get_ambassador(code)
    if not amb:
        return jsonify({"valid": False, "error": "El código colegiado no existe o no está activo."}), 404

    discount = 5.0 if plan in ["vitalicia", "90_dias"] else 3.0
    prices = {"30_dias": 19.99, "90_dias": 34.99, "vitalicia": 49.99}
    base_price = prices.get(plan, 49.99)
    discounted = max(0.0, round(base_price - discount, 2))

    return jsonify({
        "valid": True,
        "code": amb["code"],
        "ambassador_name": amb.get("name", "Embajador Notarial"),
        "strike_handle": amb.get("strike_handle", ""),
        "discount": discount,
        "original_price": base_price,
        "discounted_price": discounted,
        "message": f"¡Código colegiado aplicado! Descuento de ${discount:.2f} gracias a {amb.get('name', 'Embajador')}."
    })

@app.route("/embajadores")
def embajadores():
    ambassadors = db.get_all_ambassadors()
    return render_template("embajadores.html", ambassadors=ambassadors)

@app.route("/api/ambassadors/register", methods=["POST"])
def api_ambassadors_register():
    data = request.get_json() or {}
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    strike_handle = data.get("strike_handle", "").strip()
    desired_code = data.get("code", "").strip().upper()
    wallet_type = data.get("wallet_type", "strike").strip().lower()

    if "blink" in wallet_type or "blink.sv" in strike_handle.lower():
        wallet_type = "blink"
    else:
        wallet_type = "strike"

    if not name or not strike_handle or not desired_code:
        wallet_name = "Blink (@blink.sv)" if wallet_type == "blink" else "Strike (@strike.me)"
        return jsonify({"success": False, "error": f"Por favor completa tu nombre, usuario de {wallet_name} y código deseado."}), 400

    existing = db.get_ambassador(desired_code)
    if existing:
        return jsonify({"success": False, "error": "Ese código ya está en uso. Por favor elige otro."}), 400

    db.create_or_update_ambassador(
        code=desired_code,
        name=name,
        strike_handle=strike_handle,
        email=email,
        discount_usd=5.0,
        commission_vitalicia=10.0,
        commission_trimestral=5.0,
        commission_mensual=3.0,
        wallet_type=wallet_type
    )
    amb_saved = db.get_ambassador(desired_code)
    clean_saved_handle = amb_saved.get("strike_handle") if amb_saved else strike_handle
    wallet_label = "Blink Wallet (@blink.sv)" if wallet_type == "blink" else "Strike (@strike.me)"
    return jsonify({
        "success": True,
        "message": f"¡Felicidades Lic. {name}! Tu código {desired_code} está activo. Recibirás tus comisiones directamente a tu cuenta de {wallet_label} (@{clean_saved_handle})."
    })

@app.route("/api/checkout/process", methods=["POST"])
def api_checkout_process():
    data = request.get_json() or {}
    plan_type = data.get("plan_type", "vitalicia")
    buyer_name = data.get("buyer_name", "").strip() or "Aspirante Notario"
    buyer_email = data.get("buyer_email", "").strip() or "cliente@notariado.sv"
    buyer_phone = data.get("buyer_phone", "").strip() or "N/D"
    payment_method = data.get("payment_method", "tarjeta")
    payment_reference = data.get("payment_reference", "").strip()
    referral_code = data.get("referral_code", "").strip()
    client_device_id = data.get("device_id") or get_device_id_from_request()

    if not client_device_id:
        return jsonify({"success": False, "error": "No se pudo identificar el dispositivo del comprador."}), 400

    prices = {
        "30_dias": 19.99,
        "90_dias": 34.99,
        "vitalicia": 49.99
    }
    durations = {
        "30_dias": 30,
        "90_dias": 90,
        "vitalicia": -1
    }

    amount = prices.get(plan_type, 49.99)
    duration = durations.get(plan_type, -1)

    # Check for Ambassador Referral Code & apply discount
    ambassador = db.get_ambassador(referral_code) if referral_code else None
    discount_usd = 0.0
    if ambassador:
        discount_usd = 5.0 if plan_type in ["vitalicia", "90_dias"] else 3.0
        amount = max(0.0, round(amount - discount_usd, 2))

    # 1. Generate unique license key automatically
    ref_note = f" [Embajador: {ambassador['code']}]" if ambassador else ""
    lic_data = db.admin_create_license(
        plan_type=plan_type,
        duration_days=duration,
        notes=f"Compra Online [{payment_method.upper()}]: {buyer_name} ({buyer_email}) Ref: {payment_reference}{ref_note}"
    )
    new_key = lic_data["key"]

    # 2. Immediately bind to this single device!
    act_result = db.validate_or_activate_license(new_key, client_device_id)

    # 3. Record order
    order_id = f"ORD-{db.secrets.token_hex(4).upper()}"
    db.create_order(
        order_id=order_id,
        buyer_name=buyer_name,
        buyer_email=buyer_email,
        buyer_phone=buyer_phone,
        plan_type=plan_type,
        amount_usd=amount,
        license_key=new_key,
        payment_method=payment_method,
        payment_reference=payment_reference,
        referral_code=ambassador["code"] if ambassador else ""
    )

    # 4. Record Ambassador Commission for Strike Payout!
    comm_record = None
    if ambassador:
        comm_record = db.record_commission(
            order_id=order_id,
            ambassador_code=ambassador["code"],
            buyer_name=buyer_name,
            plan_type=plan_type
        )

    # 5. Generate WhatsApp notification link
    wa_phone = payment_config.WHATSAPP_PHONE
    amb_lines = ""
    if ambassador:
        comm_val = comm_record["amount_usd"] if comm_record else 10.0
        w_type = ambassador.get("wallet_type", "strike").capitalize()
        amb_lines = (
            f"🎁 *Descuento Colegiado Aplicado:* -${discount_usd:.2f} (Código: {ambassador['code']})\n"
            f"🤝 *Embajador:* {ambassador.get('name')} ({w_type}: @{ambassador.get('strike_handle')})\n"
            f"⚡ *Comisión Lightning Registrada:* ${comm_val:.2f} USD\n"
        )

    wa_msg = (
        f"🏛️ *COMPROBANTE DE COMPRA - SIMULADOR NOTARIAL CSJ*\n\n"
        f"📋 *Orden:* {order_id}\n"
        f"👤 *Aspirante:* {buyer_name}\n"
        f"📧 *Correo:* {buyer_email}\n"
        f"📱 *Teléfono:* {buyer_phone}\n"
        f"📦 *Plan:* {plan_type.upper()} (${amount} USD)\n"
        f"{amb_lines}"
        f"💳 *Método de Pago:* {payment_method.upper()}\n"
        f"🔢 *Referencia/Voucher:* {payment_reference or 'Pago en línea'}\n"
        f"🔑 *Clave Generada:* {new_key}\n\n"
        f"Adjunto mi comprobante para respaldo de activación. ¡Muchas gracias!"
    )
    whatsapp_url = f"https://wa.me/{wa_phone}?text={urllib.parse.quote(wa_msg)}"

    resp = make_response(jsonify({
        "success": True,
        "order_id": order_id,
        "license_key": new_key,
        "plan_type": plan_type,
        "amount_usd": amount,
        "discount_usd": discount_usd,
        "referral_code": ambassador["code"] if ambassador else "",
        "payment_method": payment_method,
        "payment_reference": payment_reference,
        "whatsapp_url": whatsapp_url,
        "message": "¡Pago procesado con éxito! Tu clave ha sido generada y vinculada a este dispositivo automáticamente."
    }))
    resp.set_cookie("notariado_device_id", client_device_id, max_age=365*24*3600, httponly=False)
    return resp

@app.route("/api/webhook/wompi", methods=["POST"])
def api_webhook_wompi():
    """Webhook listener for live Wompi (Banco Agrícola) payment events."""
    payload = request.get_json() or {}
    event_type = payload.get("event")
    # For live Wompi events: check status == 'APPROVED'
    # Generate key and store order
    return jsonify({"received": True}), 200

# --- ADMIN PANEL ROUTES ---

@app.route("/admin", methods=["GET", "POST"])
def admin_panel():
    if request.method == "POST":
        pin = request.form.get("admin_pin", "").strip()
        if pin == ADMIN_PIN:
            session["admin_logged_in"] = True
            return redirect(url_for("admin_panel"))
        return render_template("admin.html", error="PIN o contraseña incorrecta.", is_logged=False)

    is_logged = session.get("admin_logged_in", False)
    if not is_logged:
        return render_template("admin.html", is_logged=False)

    licenses = db.admin_get_all_licenses()
    promotional_keys = db.get_promotional_keys()
    orders = db.admin_get_orders()
    commissions = db.get_commissions()
    ambassadors = db.get_all_ambassadors()

    # Calculate commission stats
    pending_comm_total = sum(float(c.get("amount_usd", 0.0)) for c in commissions if c.get("status") == "PENDIENTE")
    paid_comm_total = sum(float(c.get("amount_usd", 0.0)) for c in commissions if c.get("status") == "PAGADO")

    return render_template(
        "admin.html", 
        is_logged=True, 
        licenses=licenses, 
        promotional_keys=promotional_keys,
        orders=orders,
        commissions=commissions,
        ambassadors=ambassadors,
        pending_comm_total=pending_comm_total,
        paid_comm_total=paid_comm_total
    )

@app.route("/admin/commissions/mark-paid/<comm_id>", methods=["POST"])
def admin_mark_commission_paid(comm_id):
    if not session.get("admin_logged_in"):
        return jsonify({"success": False, "error": "No autorizado"}), 403
    data = request.get_json() or {}
    payout_ref = data.get("payout_reference", "Pago vía Lightning (Strike/Blink)")
    db.mark_commission_paid(comm_id, payout_ref)
    return jsonify({"success": True, "message": "Comisión marcada como pagada con éxito"})

@app.route("/admin/ambassadors/create", methods=["POST"])
def admin_create_ambassador():
    if not session.get("admin_logged_in"):
        return jsonify({"success": False, "error": "No autorizado"}), 403
    data = request.get_json() or {}
    code = data.get("code", "").strip().upper()
    name = data.get("name", "").strip()
    strike_handle = data.get("strike_handle", "").strip().replace("@", "")
    email = data.get("email", "").strip()
    wallet_type = data.get("wallet_type", "strike").strip().lower()
    discount_usd = float(data.get("discount_usd", 5.0))
    comm_vitalicia = float(data.get("commission_vitalicia", 10.0))

    if "blink" in wallet_type or "blink.sv" in strike_handle.lower():
        wallet_type = "blink"
    else:
        wallet_type = "strike"

    if not code or not name or not strike_handle:
        return jsonify({"success": False, "error": "Código, nombre y usuario de billetera (Strike o Blink) son obligatorios."}), 400

    db.create_or_update_ambassador(
        code=code,
        name=name,
        strike_handle=strike_handle,
        email=email,
        discount_usd=discount_usd,
        commission_vitalicia=comm_vitalicia,
        wallet_type=wallet_type
    )
    return jsonify({"success": True, "message": f"Embajador {code} ({wallet_type.upper()}) guardado con éxito."})

@app.route("/admin/generar", methods=["POST"])
def admin_generar_licencia():
    if not session.get("admin_logged_in"):
        return jsonify({"success": False, "error": "No autorizado"}), 403

    data = request.get_json() or {}
    plan_type = data.get("plan_type", "30_dias")
    notes = data.get("notes", "Generada desde panel")
    count = int(data.get("count", 1))

    duration_map = {
        "vitalicia": -1,
        "90_dias": 90,
        "30_dias": 30
    }
    duration = duration_map.get(plan_type, 30)

    generated = []
    for _ in range(count):
        lic = db.admin_create_license(plan_type=plan_type, duration_days=duration, notes=notes)
        generated.append(lic)

    return jsonify({"success": True, "licenses": generated})

@app.route("/admin/reset-device/<int:license_id>", methods=["POST"])
def admin_reset_device_route(license_id):
    if not session.get("admin_logged_in"):
        return jsonify({"success": False, "error": "No autorizado"}), 403
    db.admin_reset_device(license_id)
    return jsonify({"success": True, "message": "Dispositivo desvinculado con éxito."})

@app.route("/admin/logout")
def admin_logout():
    session.pop("admin_logged_in", None)
    return redirect(url_for("admin_panel"))

@app.errorhandler(404)
def handle_404(e):
    if request.path.startswith('/api/'):
        return jsonify({"error": "Endpoint not found", "path": request.path}), 404
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
