import os
from PIL import Image, ImageDraw, ImageFont
import database as db

# Output directories
DIR_OUTPUT = os.path.join(os.path.dirname(__file__), "tarjetas_promocionales")
DIR_STATIC = os.path.join(os.path.dirname(__file__), "static", "cards")
os.makedirs(DIR_OUTPUT, exist_ok=True)
os.makedirs(DIR_STATIC, exist_ok=True)

# Colors
COLOR_BG_TOP = (11, 22, 42)       # Dark luxury navy
COLOR_BG_BOTTOM = (18, 35, 68)    # Royal navy
COLOR_GOLD = (212, 175, 55)        # Classic gold
COLOR_GOLD_LIGHT = (245, 218, 128)# Light gold
COLOR_GOLD_DARK = (160, 125, 30)  # Deep gold
COLOR_WHITE = (255, 255, 255)
COLOR_SLATE_200 = (226, 232, 240)
COLOR_SLATE_400 = (148, 163, 184)
COLOR_EMERALD = (52, 211, 153)
COLOR_CARD_BG = (7, 14, 28)

WIDTH = 1200
HEIGHT = 675

def get_font(name, size):
    font_path = os.path.join("C:/Windows/Fonts", name)
    try:
        return ImageFont.truetype(font_path, size)
    except Exception:
        return ImageFont.load_default()

# Load fonts
font_title = get_font("georgiab.ttf", 40)
font_subtitle = get_font("georgia.ttf", 22)
font_badge = get_font("arialbd.ttf", 16)
font_key_label = get_font("arialbd.ttf", 15)
font_key = get_font("arialbd.ttf", 46)
font_key_sub = get_font("arial.ttf", 15)
font_features = get_font("segoeui.ttf", 18)
font_footer = get_font("arialbd.ttf", 17)
font_footer_sub = get_font("arial.ttf", 14)

def draw_gradient(draw, width, height):
    """Draws vertical smooth gradient background."""
    for y in range(height):
        ratio = y / height
        r = int(COLOR_BG_TOP[0] * (1 - ratio) + COLOR_BG_BOTTOM[0] * ratio)
        g = int(COLOR_BG_TOP[1] * (1 - ratio) + COLOR_BG_BOTTOM[1] * ratio)
        b = int(COLOR_BG_TOP[2] * (1 - ratio) + COLOR_BG_BOTTOM[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

def draw_diamond(draw, cx, cy, size=7, color=COLOR_GOLD):
    pts = [
        (cx, cy - size),
        (cx + int(size * 0.65), cy),
        (cx, cy + size),
        (cx - int(size * 0.65), cy)
    ]
    draw.polygon(pts, fill=color)

def draw_check_icon(draw, x, y, size=18, color=COLOR_GOLD):
    # Golden checkmark
    p1 = (x, y + int(size * 0.55))
    p2 = (x + int(size * 0.35), y + int(size * 0.85))
    p3 = (x + int(size * 0.95), y + int(size * 0.15))
    draw.line([p1, p2], fill=color, width=3)
    draw.line([p2, p3], fill=color, width=3)

def create_promotional_card(index, key_code, plan_notes):
    img = Image.new("RGB", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)

    # 1. Background gradient
    draw_gradient(draw, WIDTH, HEIGHT)

    # 2. Luxury Golden Borders
    border_margin = 24
    draw.rectangle(
        [(border_margin, border_margin), (WIDTH - border_margin, HEIGHT - border_margin)],
        outline=COLOR_GOLD,
        width=2
    )
    inner_margin = 30
    draw.rectangle(
        [(inner_margin, inner_margin), (WIDTH - inner_margin, HEIGHT - inner_margin)],
        outline=COLOR_GOLD_DARK,
        width=1
    )

    # Decorative Corner Crosses / Dots
    for cx, cy in [
        (border_margin, border_margin),
        (WIDTH - border_margin, border_margin),
        (border_margin, HEIGHT - border_margin),
        (WIDTH - border_margin, HEIGHT - border_margin)
    ]:
        draw.rectangle([(cx - 5, cy - 5), (cx + 5, cy + 5)], fill=COLOR_GOLD)

    # 3. Top VIP Badge Pill
    badge_text = f"TARJETA PROMOCIONAL VIP #{index} • ACCESO VITALICIO"
    badge_w = draw.textlength(badge_text, font=font_badge)
    badge_x = (WIDTH - badge_w) / 2
    badge_y = 52
    pill_padding_x = 36
    pill_padding_y = 7
    draw.rounded_rectangle(
        [(badge_x - pill_padding_x, badge_y - pill_padding_y),
         (badge_x + badge_w + pill_padding_x, badge_y + 18 + pill_padding_y)],
        radius=14,
        fill=COLOR_CARD_BG,
        outline=COLOR_GOLD,
        width=1
    )
    # Draw diamonds flanking the badge
    draw_diamond(draw, badge_x - 18, badge_y + 9, size=6, color=COLOR_GOLD)
    draw.text((badge_x, badge_y), badge_text, fill=COLOR_GOLD_LIGHT, font=font_badge)
    draw_diamond(draw, badge_x + badge_w + 18, badge_y + 9, size=6, color=COLOR_GOLD)

    # 4. Main Title & Subtitle
    title_text = "SIMULADOR DE NOTARIADO DE EL SALVADOR"
    title_w = draw.textlength(title_text, font=font_title)
    draw.text(((WIDTH - title_w) / 2, 98), title_text, fill=COLOR_WHITE, font=font_title)

    sub_text = "Examen de Suficiencia para la Función Notarial • Corte Suprema de Justicia (CSJ)"
    sub_w = draw.textlength(sub_text, font=font_subtitle)
    draw.text(((WIDTH - sub_w) / 2, 148), sub_text, fill=COLOR_SLATE_200, font=font_subtitle)

    # 5. Central Golden Box with License Key
    box_w = 880
    box_h = 160
    box_x = (WIDTH - box_w) / 2
    box_y = 200

    # Glow / shadow behind box
    draw.rounded_rectangle(
        [(box_x - 3, box_y - 3), (box_x + box_w + 3, box_y + box_h + 3)],
        radius=20,
        fill=None,
        outline=COLOR_GOLD_LIGHT,
        width=2
    )
    draw.rounded_rectangle(
        [(box_x, box_y), (box_x + box_w, box_y + box_h)],
        radius=18,
        fill=COLOR_CARD_BG,
        outline=COLOR_GOLD,
        width=2
    )

    lbl_key = "TU CLAVE DE ACCESO PERSONAL E INTRANSFERIBLE:"
    lbl_w = draw.textlength(lbl_key, font=font_key_label)
    draw.text(((WIDTH - lbl_w) / 2, box_y + 18), lbl_key, fill=COLOR_GOLD_LIGHT, font=font_key_label)

    # The Key itself in huge bold text
    key_w = draw.textlength(key_code, font=font_key)
    draw.text(((WIDTH - key_w) / 2, box_y + 48), key_code, fill=COLOR_WHITE, font=font_key)

    sub_key = "Vinculación Automática a 1 Dispositivo • Sin Caducidad • 100% Gratuita para Ti"
    sub_key_w = draw.textlength(sub_key, font=font_key_sub)
    draw.text(((WIDTH - sub_key_w) / 2, box_y + 118), sub_key, fill=COLOR_EMERALD, font=font_key_sub)

    # 6. Feature Bullets in 2 Columns
    col1_x = 150
    col2_x = 630
    feat_y1 = 390
    feat_y2 = 428
    feat_y3 = 466

    features = [
        (col1_x, feat_y1, "20 Casos Prácticos Ponderados CSJ"),
        (col1_x, feat_y2, "Cronómetro Oficial de 25 Minutos"),
        (col1_x, feat_y3, "Fundamentación con Leyes y Artículos"),
        (col2_x, feat_y1, "Desglose de Distractores y Trampas"),
        (col2_x, feat_y2, "Fichas Mnemotécnicas de Plazos"),
        (col2_x, feat_y3, "Diagnóstico por Ramas del Derecho")
    ]

    for fx, fy, ftext in features:
        draw_check_icon(draw, fx, fy + 2, size=18, color=COLOR_GOLD)
        draw.text((fx + 28, fy), ftext, fill=COLOR_SLATE_200, font=font_features)

    # Horizontal divider line
    div_y = 520
    draw.line([(100, div_y), (WIDTH - 100, div_y)], fill=COLOR_GOLD_DARK, width=1)

    # 7. Activation Instructions in Footer
    instr_text = "ACTÍVALA HOY MISMO INGRESANDO A:  https://suficienciasv.vercel.app/activar"
    instr_w = draw.textlength(instr_text, font=font_footer)
    draw.text(((WIDTH - instr_w) / 2, 545), instr_text, fill=COLOR_GOLD_LIGHT, font=font_footer)

    disclaimer_text = "Iniciativa académica independiente de entrenamiento forense • Derechos Reservados República de El Salvador"
    disc_w = draw.textlength(disclaimer_text, font=font_footer_sub)
    draw.text(((WIDTH - disc_w) / 2, 580), disclaimer_text, fill=COLOR_SLATE_400, font=font_footer_sub)

    # Save to both folders
    filename = f"tarjeta_promocional_{index:02d}_{key_code}.png"
    path_output = os.path.join(DIR_OUTPUT, filename)
    path_static = os.path.join(DIR_STATIC, filename)

    img.save(path_output, "PNG", quality=95)
    img.save(path_static, "PNG", quality=95)

    return filename

def generate_all_cards():
    keys = db.get_promotional_keys()
    print(f"Generando {len(keys)} tarjetas promocionales en alta resolución...")
    generated_files = []
    for i, k in enumerate(keys, start=1):
        fname = create_promotional_card(i, k["license_key"], k["notes"])
        generated_files.append(fname)
        print(f"[{i:02d}/10] Tarjeta creada: {fname}")
    print(f"\n¡Todas las tarjetas se han guardado con éxito en:\n{DIR_OUTPUT}")
    return generated_files

if __name__ == "__main__":
    generate_all_cards()
