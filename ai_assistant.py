"""
ai_assistant.py
Asistente Jurídico Notarial con Inteligencia Artificial para SuficienciaSV.
Especializado en la Ley de Notariado y legislación de la República de El Salvador.
Incluye detección de intenciones de soporte técnico y escalamiento a humano vía WhatsApp.
"""

import os
import re
import json
import urllib.request
import urllib.parse
from datetime import datetime
from questions_seed import QUESTIONS, CATEGORIES, FLASHCARDS
from payment_config import WHATSAPP_PHONE

# SYSTEM PROMPT PARA MODELOS LLM (GEMINI)
SYSTEM_PROMPT = """Eres el Asistente Jurídico Notarial IA de SuficienciaSV, la plataforma oficial de preparación para el Examen de Suficiencia Notarial de la Corte Suprema de Justicia (CSJ) de El Salvador.

Tu misión es:
1. Explicar con precisión técnica los casos y preguntas del examen notarial.
2. Citar los artículos y leyes salvadoreñas aplicables (Ley de Notariado, Código Civil, Código de Comercio, Código de Familia, CPCM, Ley de Inquilinato, etc.).
3. Desglosar por qué una respuesta es correcta y por qué las demás son distractores o trampas comunes de la CSJ.
4. Responder dudas sobre formalidades de escrituras matrices, testimonios, actas notariales, libros de protocolo, inhabilitaciones, plazos perentorios y testigos instrumentales.
5. Ser pedagógico, formal, respetuoso del lenguaje jurídico forense salvadoreño y directo.
6. Si el usuario solicita ayuda técnica con licencias, pagos, activación o errores del sistema, debes indicarle con amabilidad que puede contactar a soporte humano por WhatsApp.
"""

# BASE DE CONOCIMIENTO EXPERTO LOCAL SALVADOREÑO
LEGAL_TOPICS = {
    "plazos_protocolo": {
        "keywords": ["plazo", "protocolo", "entrega", "agotado", "año", "15 días", "razón de cierre", "sección del notariado", "entregar libro"],
        "title": "Plazos Fatales sobre el Libro de Protocolo (Ley de Notariado)",
        "content": (
            "⚖️ **Reglas Perentorias sobre el Libro de Protocolo (Ley de Notariado de El Salvador):**\n\n"
            "• **Protocolo Agotado antes del año (Art. 21 inc. 2° LN):** Una vez concluido el libro (ej. las 25 hojas), el notario debe poner la razón de cierre inmediatamente y entregarlo a la Sección del Notariado dentro de los **quince (15) días siguientes** a la fecha en que se agotó. La omisión acarrea multas impuestas por la Corte Suprema.\n\n"
            "• **Vencimiento del año de vigencia (Art. 24 LN):** Si no se agotare el libro, vence exactamente al cumplirse un año desde la fecha de entrega. El notario dispone de **quince (15) días perentorios** siguientes a dicho vencimiento para entregarlo a la Sección del Notariado.\n\n"
            "• **Custodia Temporal:** En El Salvador los protocolos son propiedad del Estado; el notario es un mero depositario temporal. La retención indebida puede derivar en suspensión en el ejercicio de la función notarial (Art. 54 LN)."
        )
    },
    "testigos_instrumentales": {
        "keywords": ["testigo", "testigos", "instrumentales", "analfabeto", "no sabe firmar", "huella", "firma a ruego", "art 34", "art 32"],
        "title": "Presencia de Testigos Instrumentales y Firma a Ruego (Arts. 32 y 34 LN)",
        "content": (
            "⚖️ **Reglas de Testigos Instrumentales (Ley de Notariado):**\n\n"
            "• **Obligatoriedad de DOS Testigos (Art. 34 inc. 1° LN):** Es estrictamente imperativa la concurrencia de **dos testigos instrumentales** cuando alguno de los otorgantes **no supiere o no pudiere firmar**, fuere ciego, mudo o sordo.\n\n"
            "• **Firma a Ruego y Huella Digital (Art. 32 ord. 12° LN):** Si el otorgante no sabe o no puede firmar, estampará la **huella dactilar** de uno de sus dedos (de preferencia el pulgar derecho), y a su ruego **firmará otra persona**, que válidamente puede ser uno de los testigos instrumentales.\n\n"
            "• **Sanción por Omisión:** Si se autoriza una escritura pública donde un otorgante no firma y se omiten los dos testigos instrumentales, el instrumento adolece de **NULIDAD ABSOLUTA** (Art. 34 LN), además de generar responsabilidad disciplinaria e indemnizatoria contra el notario."
        )
    },
    "prohibiciones_parentesco": {
        "keywords": ["prohibicion", "prohibiciones", "pariente", "parentesco", "conyuge", "hermano", "cuarto grado", "segundo de afinidad", "art 9", "art 10", "nulidad"],
        "title": "Prohibiciones Legales por Parentesco (Arts. 9 y 10 LN)",
        "content": (
            "⚖️ **Prohibiciones Absolutas del Notario (Arts. 9 y 10 Ley de Notariado):**\n\n"
            "• **Alcance del Art. 9 LN:** El notario está terminantemente inhibido de autorizar instrumentos en que resulte o pueda resultar algún provecho directo para él, para su **cónyuge**, para sus parientes dentro del **cuarto grado de consanguinidad** (hijos, padres, hermanos, tíos, sobrinos, primos hermanos) o **segundo de afinidad** (suegros, yernos, nueras, cuñados).\n\n"
            "• **Sanción Taxativa (Art. 10 LN):** Los instrumentos autorizados en contravención al Art. 9 adolecen de **NULIDAD ABSOLUTA de pleno derecho**.\n\n"
            "• **Excepción Clave:** El notario sí puede autorizar su propio testamento cuando nombre herederos a personas distintas de las comprendidas en la prohibición."
        )
    },
    "enmiendas_y_testaduras": {
        "keywords": ["enmendar", "testar", "salvar", "entrerrenglonadura", "raspadura", "error escritura", "art 35", "art 36", "después de firmar"],
        "title": "Subsanación de Errores en la Escritura Matriz (Arts. 35 y 36 LN)",
        "content": (
            "⚖️ **Régimen de Salvaturas y Correcciones en el Protocolo:**\n\n"
            "• **Antes de las Firmas (Art. 35 LN):** Si se advierte un error, omisión o lapsus antes de que los otorgantes y el notario firmen, las palabras que deban borrarse se **testarán** trazando una línea sobre ellas, y las adiciones se harán entre renglones (**entrerrenglonaduras**). Todas deben **salvarse al final de la escritura y ANTES de las firmas** (ej. *'Vale lo testado', 'Vale lo entrerrenglonado'*).\n\n"
            "• **Después de Firmada (Art. 36 LN):** Una vez estampadas las firmas y autorizada por el notario, está **prohibido hacer cualquier alteración, raspadura o nota marginal**. La deficiencia únicamente puede subsanarse mediante el otorgamiento de una **NUEVA escritura pública de rectificación o aclaración** con comparecencia de las partes interesadas."
        )
    },
    "testimonios_y_copias": {
        "keywords": ["testimonio", "testimonios", "primera copia", "ulteriores", "segundo testimonio", "art 43", "art 44", "sello"],
        "title": "Expedición de Testimonios y Ulteriores Copias (Arts. 43 y 44 LN)",
        "content": (
            "⚖️ **Expedición de Testimonios:**\n\n"
            "• **Testimonio Original (Art. 43 LN):** Es la copia fiel de la escritura matriz autorizada con la firma y sello del notario, expedida a favor de la parte interesada.\n\n"
            "• **Ulteriores Testimonios (Art. 44 LN):** El notario está facultado por ley para expedir ulteriores testimonios (segundas o terceras copias) a petición de los otorgantes o sus sucesores legítimos, sin necesidad de que el primero le sea devuelto o justificar pérdida ante juez, haciendo constar en la razón el número de testimonio que se expide."
        )
    }
}

# DETECCIÓN DE INTENCIÓN DE ESCALAMIENTO A HUMANO / SOPORTE TÉCNICO
ESCALATION_KEYWORDS = [
    "humano", "persona", "asesor", "hablar con alguien", "soporte tecnico", "soporte técnico",
    "contactar", "contacto", "telefono", "teléfono", "whatsapp", "licencia bloqueada",
    "cambiar equipo", "cambio de equipo", "transferir licencia", "desvincular", "resetear",
    "error en el pago", "comprobante", "banco agricola", "banco agrícola", "transferencia 365",
    "no me funciona", "falla el sistema", "reclamar clave", "no llego la clave", "no llegó mi clave"
]


def check_support_escalation(query_text):
    """Detecta si el mensaje amerita enlazar con un asesor humano."""
    q_lower = query_text.lower()
    for kw in ESCALATION_KEYWORDS:
        if kw in q_lower:
            return True
    return False


def build_whatsapp_link(reason="Consulta Técnica", device_id=None, license_key=None, custom_msg=""):
    """Construye un enlace pre-llenado de WhatsApp para atención humana."""
    lines = [
        "¡Hola! Necesito asistencia con la plataforma SuficienciaSV ⚖️🇸🇻",
        f"• Motivo: {reason}",
    ]
    if license_key:
        lines.append(f"• Clave: {license_key}")
    if device_id:
        lines.append(f"• Dispositivo ID: {device_id[:16]}...")
    if custom_msg:
        lines.append(f"• Detalle: {custom_msg[:120]}")
    lines.append("Agradezco su apoyo técnico para continuar mi preparación.")

    text = "\n".join(lines)
    encoded = urllib.parse.quote(text)
    return f"https://wa.me/{WHATSAPP_PHONE}?text={encoded}"


def call_gemini_api(prompt, system_instruction=SYSTEM_PROMPT):
    """
    Invoca la API de Gemini mediante petición HTTP directa si la clave API está presente.
    Compatible con entornos serverless de Vercel sin dependencias pesadas.
    """
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return None

    # Models: gemini-2.5-flash -> fallback to gemini-1.5-flash
    models = ["gemini-2.5-flash", "gemini-1.5-flash"]
    for model in models:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}]
                }
            ],
            "systemInstruction": {
                "parts": [{"text": system_instruction}]
            },
            "generationConfig": {
                "temperature": 0.2,
                "maxOutputTokens": 1024
            }
        }
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=12) as response:
                if response.status == 200:
                    res_data = json.loads(response.read().decode("utf-8"))
                    candidates = res_data.get("candidates", [])
                    if candidates:
                        text_parts = candidates[0].get("content", {}).get("parts", [])
                        if text_parts:
                            return text_parts[0].get("text", "")
        except Exception as e:
            print(f"[AI ASSISTANT] Error calling Gemini ({model}): {e}")
            continue

    return None


def match_question_by_id_or_text(query_text, question_id=None):
    """Busca en el banco oficial de preguntas de la CSJ si la consulta refiere a un caso específico."""
    target_id = None
    if question_id:
        try:
            target_id = int(question_id)
        except Exception:
            pass

    if not target_id:
        m = re.search(r'(?:pregunta|caso|reactivo|ejercicio)\s*(?:n[uú]mero|no\.?|#)?\s*(\d+)', query_text, re.IGNORECASE)
        if m:
            try:
                target_id = int(m.group(1))
            except Exception:
                pass

    if target_id and 1 <= target_id <= len(QUESTIONS):
        q = dict(QUESTIONS[target_id - 1])
        q["id"] = target_id
        return q

    # Also match by keywords in question text
    q_words = [w for w in query_text.lower().split() if len(w) > 4]
    if len(q_words) >= 3:
        for idx, item in enumerate(QUESTIONS, 1):
            q_text = item.get("question", "").lower()
            matches = sum(1 for w in q_words if w in q_text)
            if matches >= 3:
                q = dict(item)
                q["id"] = idx
                return q

    return None


def generate_local_expert_response(query_text, matched_question=None):
    """Generador heurístico de alta precisión en derecho notarial salvadoreño."""
    # 1. Si el usuario pregunta por un caso concreto del examen:
    if matched_question:
        q = matched_question
        correct_letter = q.get("correct_option", "")
        opt_text = q.get(f"option_{correct_letter.lower()}", "")
        return (
            f"⚖️ **Análisis Jurídico de la Pregunta #{q.get('id')}:**\n\n"
            f"**Enunciado:**\n_{q.get('question')}_\n\n"
            f"✅ **Opción Correcta:** **Opción {correct_letter}**\n"
            f"_{opt_text}_\n\n"
            f"🏛️ **Fundamentación Jurídica (Ley de El Salvador):**\n"
            f"• **Base Legal:** `{q.get('legal_basis')}`\n"
            f"• **Justificación Doctrinal:** {q.get('justification')}\n\n"
            f"🔍 **Análisis de Distractores y Trampas:**\n"
            f"{q.get('distractors_analysis')}\n\n"
            f"💡 **Consejo de Examen CSJ:** Pon especial atención a los términos perentorios y la presencia obligatoria de testigos instrumentales, pues son las trampas de descalificación más comunes de la Corte."
        )

    q_lower = query_text.lower()

    # 2. Búsqueda por temas clave de la Ley de Notariado:
    for topic_id, data in LEGAL_TOPICS.items():
        for kw in data["keywords"]:
            if kw in q_lower:
                return f"{data['content']}\n\n💡 *¿Deseas profundizar en algún artículo o caso práctico específico? Puedes consultarme con toda confianza.*"

    # 3. Búsqueda en flashcards de plazos:
    for fc in FLASHCARDS:
        if fc.get("title", "").lower() in q_lower or any(word in q_lower for word in fc.get("title", "").lower().split() if len(word) > 5):
            return (
                f"⚖️ **Ficha Mnemotécnica de Plazos Notariales:**\n\n"
                f"**Tema:** {fc.get('title')}\n"
                f"• **Regla Legal:** {fc.get('legal_answer')}\n"
                f"• **Artículo Base:** `{fc.get('legal_article')}`\n\n"
                f"💡 Este plazo es evaluado con frecuencia como distractor numérico en la prueba oficial de la CSJ."
            )

    # 4. Respuesta general orientativa si no hubo coincidencia exacta:
    return (
        "⚖️ **Asistente Jurídico Notarial CSJ:**\n\n"
        "Comprendo tu consulta jurídica. En el Examen de Suficiencia Notarial de El Salvador, las materias evaluadas son:\n\n"
        "1. **Ley de Notariado:** Formalidades de la matriz (Art. 32), testigos instrumentales (Art. 34), razón de cierre y plazos del protocolo (Arts. 21 y 24), prohibiciones de parentesco (Art. 9) y régimen de nulidades (Art. 10).\n"
        "2. **Derecho Civil:** Donaciones entre vivos, compraventas de inmuebles, hipotecas y sucesiones.\n"
        "3. **Derecho Mercantil:** Constitución de sociedades, títulos valores y prendas.\n"
        "4. **Derecho de Familia:** Capitulaciones matrimoniales, divorcios por mutuo acuerdo y reconocimientos.\n\n"
        "Puedes preguntarme sobre **cualquier artículo**, pedirme **explicar una pregunta del simulacro** (ej. *'Explícame la pregunta 4'*), o consultar **plazos específicos**."
    )


def process_ai_query(user_query, question_context=None, device_id=None, license_key=None):
    """
    Función principal de procesamiento:
    1. Evalúa si amerita escalamiento humano.
    2. Responde con Gemini si hay API Key.
    3. Si no, responde con el motor jurídico local experto.
    """
    user_query_clean = (user_query or "").strip()
    if not user_query_clean:
        return {
            "success": False,
            "response": "Por favor escribe una consulta jurídica o técnica para poder ayudarte."
        }

    # A. Chequeo de Escalamiento a Soporte Humano
    needs_escalation = check_support_escalation(user_query_clean)
    whatsapp_url = None
    if needs_escalation:
        whatsapp_url = build_whatsapp_link(
            reason="Asistencia Técnica y Soporte de Licencia",
            device_id=device_id,
            license_key=license_key,
            custom_msg=user_query_clean
        )

    # B. Intentar con Gemini LLM si hay API Key
    gemini_resp = None
    prompt_for_llm = user_query_clean
    if question_context:
        prompt_for_llm = f"Contexto de la pregunta del examen:\n{json.dumps(question_context, ensure_ascii=False)}\n\nConsulta del aspirante:\n{user_query_clean}"

    gemini_resp = call_gemini_api(prompt_for_llm)

    # C. Si Gemini respondió satisfactoriamente:
    if gemini_resp:
        response_text = gemini_resp
    else:
        # D. Usar el motor local experto
        matched_q = match_question_by_id_or_text(user_query_clean, question_context.get("id") if question_context else None)
        response_text = generate_local_expert_response(user_query_clean, matched_q)

    # Si hay escalamiento a humano, agregamos la tarjeta de atención directa
    if needs_escalation:
        response_text += (
            f"\n\n---\n"
            f"👨‍💼 **¿Necesitas asistencia técnica personalizada?**\n"
            f"Un asesor humano del equipo de SuficienciaSV puede revisar tu caso de forma inmediata (liberación de dispositivos, dudas de pago o soporte de cuenta)."
        )

    return {
        "success": True,
        "response": response_text,
        "escalate": needs_escalation,
        "whatsapp_url": whatsapp_url,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
