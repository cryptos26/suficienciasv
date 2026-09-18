"""
payment_config.py
Configuración centralizada de pasarelas y métodos de cobro
para el Simulador de Notariado de El Salvador.
"""
import os

WHATSAPP_PHONE = os.environ.get("PAYMENT_WHATSAPP_PHONE", "50372659216")

STRIKE_USERNAME = os.environ.get("PAYMENT_STRIKE_USER", "miltonrb")
STRIKE_LIGHTNING_ADDRESS = f"{STRIKE_USERNAME}@strike.me"
STRIKE_PROFILE_URL = f"https://strike.me/{STRIKE_USERNAME}"

BLINK_USERNAME = os.environ.get("PAYMENT_BLINK_USER", "miltonrb")
BLINK_LIGHTNING_ADDRESS = f"{BLINK_USERNAME}@blink.sv"
BLINK_PAY_URL = f"https://pay.blink.sv/{BLINK_USERNAME}"

NEQUI_PHONE = os.environ.get("PAYMENT_NEQUI_PHONE", "7265-9216")
NEQUI_HOLDER = os.environ.get("PAYMENT_NEQUI_HOLDER", "Milton R.")

# Configuración futura de Wompi (Banco Agrícola)
WOMPI_ENABLED = False
WOMPI_PAYMENT_LINK = os.environ.get("PAYMENT_WOMPI_LINK", "")

BANK_ACCOUNTS = [
    {
        "bank_name": "Banco Agrícola",
        "account_type": "Cuenta de Ahorros / Corriente",
        "account_number": "3115009033",
        "mobile_transfer": "7265-9216 (Transferencia 365 Móvil)",
        "holder_name": "Milton R.",
        "instructions": "Transferencia a Cuenta # 3115009033, Transferencia 365 Móvil al 7265-9216 o App Banco Agrícola."
    },
    {
        "bank_name": "BAC Credomatic",
        "account_type": "Transferencia Interbancaria 365",
        "account_number": "Disponible a solicitud",
        "mobile_transfer": "7265-9216",
        "holder_name": "Milton R.",
        "instructions": "Transferencia UNI / 365 hacia Banco Agrícola o consultar vía WhatsApp."
    }
]

PLANS = {
    "30_dias": {
        "name": "Plan 30 Días",
        "price_usd": 19.99,
        "duration_days": 30,
        "description": "Repaso intensivo final para el mes previo a la prueba CSJ."
    },
    "90_dias": {
        "name": "Plan 90 Días",
        "price_usd": 34.99,
        "duration_days": 90,
        "description": "3 meses de preparación integral con todas las materias y casos."
    },
    "vitalicia": {
        "name": "Acceso Vitalicio",
        "price_usd": 49.99,
        "duration_days": -1,
        "description": "Acceso ilimitado sin caducidad hasta aprobar el examen de la CSJ."
    }
}

def get_payment_summary():
    return {
        "whatsapp_phone": WHATSAPP_PHONE,
        "strike": {
            "username": STRIKE_USERNAME,
            "profile_url": STRIKE_PROFILE_URL,
            "lightning_address": STRIKE_LIGHTNING_ADDRESS
        },
        "blink": {
            "username": BLINK_USERNAME,
            "pay_url": BLINK_PAY_URL,
            "lightning_address": BLINK_LIGHTNING_ADDRESS
        },
        "nequi": {
            "phone": NEQUI_PHONE,
            "holder": NEQUI_HOLDER
        },
        "wompi": {
            "enabled": WOMPI_ENABLED,
            "link": WOMPI_PAYMENT_LINK
        },
        "banks": BANK_ACCOUNTS,
        "plans": PLANS
    }
