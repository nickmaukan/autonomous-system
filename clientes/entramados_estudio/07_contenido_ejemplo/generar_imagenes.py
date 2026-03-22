#!/usr/bin/env python3
"""Genera imágenes de ejemplo para Entramados Estudio"""

from PIL import Image, ImageDraw, ImageFont
import os

# Colores de marca
PURPLE = "#6366F1"
NAVY = "#1E1B4B"
CREAM = "#FAF8F5"
CHARCOAL = "#1F2937"
GRAY = "#6B7280"

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/imagenes"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_gradient(width, height, color1, color2, direction='vertical'):
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    c1 = hex_to_rgb(color1)
    c2 = hex_to_rgb(color2)
    for i in range(height if direction == 'vertical' else width):
        ratio = i / (height if direction == 'vertical' else width)
        r = int(c1[0] + (c2[0] - c1[0]) * ratio)
        g = int(c1[1] + (c2[1] - c1[1]) * ratio)
        b = int(c1[2] + (c2[2] - c1[2]) * ratio)
        if direction == 'vertical':
            draw.line([(0, i), (width, i)], fill=(r, g, b))
        else:
            draw.line([(i, 0), (i, height)], fill=(r, g, b))
    return img

def add_text_centered(draw, text, y, width, font, color):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) // 2
    draw.text((x, y), text, fill=color, font=font)

# ============================================================
# IMAGE 1: Quote Card Template (1080x1080)
# ============================================================
def create_quote_card():
    img = create_gradient(1080, 1080, CREAM, "#E8E4F0", 'vertical')
    draw = ImageDraw.Draw(img)
    
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 52)
        font_medium = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 28)
        font_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 20)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Línea decorativa superior
    draw.rectangle([440, 200, 640, 210], fill=hex_to_rgb(PURPLE))
    
    # Quote principal
    quote = '"Cada espacio tiene potencial."'
    add_text_centered(draw, quote, 260, 1080, font_large, CHARCOAL)
    
    # Subtítulo
    subtitle = '"Solo necesita alguien que lo vea."'
    add_text_centered(draw, subtitle, 340, 1080, font_medium, GRAY)
    
    # Attribution
    draw.rectangle([440, 420, 640, 430], fill=hex_to_rgb(PURPLE))
    
    # Instagram handle
    add_text_centered(draw, "@entramados_estudio78", 480, 1080, font_small, PURPLE)
    add_text_centered(draw, "Arquitectura · Interiores · Mobiliario", 520, 1080, font_small, GRAY)
    
    # Decorative corner elements
    draw.rectangle([40, 40, 80, 50], fill=hex_to_rgb(PURPLE))
    draw.rectangle([1000, 40, 1040, 50], fill=hex_to_rgb(PURPLE))
    draw.rectangle([40, 1030, 80, 1040], fill=hex_to_rgb(PURPLE))
    draw.rectangle([1000, 1030, 1040, 1040], fill=hex_to_rgb(PURPLE))
    
    img.save(f"{OUTPUT_DIR}/Quote_Card_01.png")
    print(f"✅ Creado: Quote_Card_01.png")

# ============================================================
# IMAGE 2: Carousel Cover - Tendencias 2026 (1080x1080)
# ============================================================
def create_carousel_cover():
    img = Image.new('RGB', (1080, 1080), hex_to_rgb(NAVY))
    draw = ImageDraw.Draw(img)
    
    # Grid pattern sutil
    for x in range(0, 1080, 60):
        draw.line([(x, 0), (x, 1080)], fill=(30, 27, 75), width=1)
    for y in range(0, 1080, 60):
        draw.line([(0, y), (1080, y)], fill=(30, 27, 75), width=1)
    
    # Barra lateral decorativa
    draw.rectangle([40, 200, 60, 880], fill=hex_to_rgb(PURPLE))
    
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 80)
        font_medium = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 32)
        font_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 18)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Título principal
    add_text_centered(draw, "TENDENCIAS", 300, 1080, font_large, "#FFFFFF")
    add_text_centered(draw, "2026", 400, 1080, font_large, hex_to_rgb(PURPLE))
    
    # Subtítulo
    add_text_centered(draw, "5 colores que van a dominar", 530, 1080, font_medium, GRAY)
    add_text_centered(draw, "el interiorismo", 570, 1080, font_medium, GRAY)
    
    # Indicador de slide
    draw.ellipse([980, 950, 1040, 1010], fill=hex_to_rgb(PURPLE))
    add_text_centered(draw, "1/5", 948, 1080, font_small, "#FFFFFF")
    
    img.save(f"{OUTPUT_DIR}/Carousel_Cover_Tendencias.png")
    print(f"✅ Creado: Carousel_Cover_Tendencias.png")

# ============================================================
# IMAGE 3: Reel Thumbnail - Transformación (1080x1920)
# ============================================================
def create_reel_thumbnail():
    img = Image.new('RGB', (1080, 1920), hex_to_rgb(NAVY))
    draw = ImageDraw.Draw(img)
    
    # Gradiente sutil en la parte superior
    overlay = create_gradient(1080, 600, "#2D2D3A", NAVY, 'vertical')
    img.paste(overlay, (0, 0))
    
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 90)
        font_medium = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 36)
        font_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 20)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Texto principal
    add_text_centered(draw, "TRANSFORMA", 500, 1080, font_large, "#FFFFFF")
    add_text_centered(draw, "TU ESPACIO", 620, 1080, font_large, "#FFFFFF")
    
    # Línea decorativa
    draw.rectangle([290, 760, 790, 780], fill=hex_to_rgb(PURPLE))
    
    # Subtítulo
    add_text_centered(draw, "BEFORE / AFTER", 820, 1080, font_medium, hex_to_rgb(PURPLE))
    
    # Indicador de tiempo
    draw.rounded_rectangle([900, 50, 1030, 100], radius=20, fill=hex_to_rgb(PURPLE))
    add_text_centered(draw, "15 seg", 65, 1080, font_small, "#FFFFFF")
    
    # Logo en esquina
    add_text_centered(draw, "@entramados_estudio78", 1800, 1080, font_small, GRAY)
    
    # Flechas decorativas
    draw.polygon([(200, 1300), (300, 1400), (200, 1500)], fill=hex_to_rgb(PURPLE))
    draw.polygon([(880, 1300), (780, 1400), (880, 1500)], fill=hex_to_rgb(PURPLE))
    
    img.save(f"{OUTPUT_DIR}/Reel_Thumbnail_Transformacion.png")
    print(f"✅ Creado: Reel_Thumbnail_Transformacion.png")

# ============================================================
# IMAGE 4: Post Template - Tips (1080x1080)
# ============================================================
def create_tips_post():
    img = Image.new('RGB', (1080, 1080), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    
    # Borde decorativo
    draw.rectangle([20, 20, 1060, 1060], outline=hex_to_rgb(PURPLE), width=4)
    
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 48)
        font_medium = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 32)
        font_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 20)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Header
    draw.rectangle([40, 40, 1040, 120], fill=hex_to_rgb(PURPLE))
    add_text_centered(draw, "TIP DEL DÍA", 65, 1080, font_medium, "#FFFFFF")
    
    # Título del tip
    add_text_centered(draw, "La luz natural", 200, 1080, font_large, CHARCOAL)
    add_text_centered(draw, "es tu mejor aliada", 260, 1080, font_large, CHARCOAL)
    
    # Iconos decorativos (círculos como placeholders)
    icons_y = 450
    for i, x in enumerate([240, 440, 640]):
        draw.ellipse([x-50, icons_y-50, x+50, icons_y+50], fill=hex_to_rgb(PURPLE))
    
    # Labels bajo iconos
    add_text_centered(draw, "Ventanas", 510, 1080, font_small, GRAY)
    add_text_centered(draw, "Espejos", 510, 1080, font_small, GRAY)
    add_text_centered(draw, "Lámparas", 510, 1080, font_small, GRAY)
    
    # Footer con CTA
    draw.rectangle([40, 850, 1040, 870], fill=hex_to_rgb(CREAM))
    add_text_centered(draw, "Guarda para después 💾", 890, 1080, font_small, GRAY)
    add_text_centered(draw, "@entramados_estudio78", 940, 1080, font_small, PURPLE)
    
    img.save(f"{OUTPUT_DIR}/Post_Tips_01.png")
    print(f"✅ Creado: Post_Tips_01.png")

# ============================================================
# IMAGE 5: Story Template - Engagement (1080x1920)
# ============================================================
def create_story_engagement():
    img = create_gradient(1080, 1920, "#FFFFFF", "#F0EFFF", 'vertical')
    draw = ImageDraw.Draw(img)
    
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 60)
        font_medium = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 32)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
    
    # Question mark grande
    draw.ellipse([390, 300, 690, 600], fill=hex_to_rgb(PURPLE))
    add_text_centered(draw, "?", 350, 1080, font_large, "#FFFFFF")
    
    # Texto principal
    add_text_centered(draw, "Cuéntanos 👇", 700, 1080, font_medium, CHARCOAL)
    
    # Pregunta
    add_text_centered(draw, "¿Qué espacio", 800, 1080, font_large, CHARCOAL)
    add_text_centered(draw, "transformarías", 870, 1080, font_large, CHARCOAL)
    add_text_centered(draw, "en tu hogar?", 940, 1080, font_large, CHARCOAL)
    
    # Área de respuesta (caja punteada)
    draw.rectangle([140, 1150, 940, 1300], outline=GRAY, width=2)
    add_text_centered(draw, "Tu respuesta aquí...", 1220, 1080, font_medium, GRAY)
    
    # CTA inferior
    add_text_centered(draw, "Responde y síguenos para más 💡", 1650, 1080, font_medium, PURPLE)
    
    img.save(f"{OUTPUT_DIR}/Story_Engagement_01.png")
    print(f"✅ Creado: Story_Engagement_01.png")

# ============================================================
# IMAGE 6: Highlight Cover - Proyectos (1080x1920)
# ============================================================
def create_highlight_cover():
    img = Image.new('RGB', (1080, 1920), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    
    # Círculo grande decorativo
    draw.ellipse([290, 460, 790, 960], fill=hex_to_rgb(PURPLE))
    
    # Icono de casa (simplificado)
    house_points = [
        (540, 550),  # techo arriba
        (450, 650),  # techo izquierda
        (450, 800),  # pared izq
        (630, 800),  # pared der
        (630, 650),  # techo der
    ]
    draw.polygon(house_points, fill="#FFFFFF")
    
    # Texto
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 56)
    except:
        font_large = ImageFont.load_default()
    
    add_text_centered(draw, "Proyectos", 1050, 1080, font_large, CHARCOAL)
    
    img.save(f"{OUTPUT_DIR}/Highlight_Proyectos.png")
    print(f"✅ Creado: Highlight_Proyectos.png")

# ============================================================
# IMAGE 7: Before/After Mockup Banner (1200x630)
# ============================================================
def create_before_after_banner():
    img = Image.new('RGB', (1200, 630), hex_to_rgb(NAVY))
    draw = ImageDraw.Draw(img)
    
    # División central
    draw.line([(600, 0), (600, 630)], fill="#FFFFFF", width=3)
    
    # Labels
    try:
        font_medium = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 40)
        font_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 24)
    except:
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # BEFORE label
    draw.rectangle([200, 280, 400, 350], fill="#666666")
    add_text_centered(draw, "ANTES", 290, 600, font_medium, "#FFFFFF")
    
    # AFTER label
    draw.rectangle([800, 280, 1000, 350], fill=hex_to_rgb(PURPLE))
    add_text_centered(draw, "DESPUÉS", 290, 1200, font_medium, "#FFFFFF")
    
    # Flecha
    draw.polygon([(550, 315), (650, 315), (600, 265)], fill=PURPLE)
    
    # Texto inferior
    add_text_centered(draw, "Transformación completa", 500, 1200, font_small, GRAY)
    add_text_centered(draw, "@entramados_estudio78", 560, 1200, font_small, PURPLE)
    
    img.save(f"{OUTPUT_DIR}/BeforeAfter_Banner.png")
    print(f"✅ Creado: BeforeAfter_Banner.png")

# ============================================================
# IMAGE 8: Facebook Cover (1640x624)
# ============================================================
def create_fb_cover():
    img = create_gradient(1640, 624, NAVY, "#2D2D3A", 'horizontal')
    draw = ImageDraw.Draw(img)
    
    # Grid pattern sutil
    for x in range(0, 1640, 80):
        draw.line([(x, 0), (x, 624)], fill=(30, 27, 75), width=1)
    for y in range(0, 624, 80):
        draw.line([(0, y), (1640, y)], fill=(30, 27, 75), width=1)
    
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 90)
        font_medium = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 36)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
    
    # Logo/Nombre
    add_text_centered(draw, "ENTRAMADOS", 180, 1640, font_large, "#FFFFFF")
    add_text_centered(draw, "ESTUDIO", 280, 1640, font_large, hex_to_rgb(PURPLE))
    
    # Subtítulo
    add_text_centered(draw, "Arquitectura · Interiores · Mobiliario Custom", 400, 1640, font_medium, GRAY)
    
    # Línea decorativa
    draw.rectangle([620, 480, 1020, 490], fill=hex_to_rgb(PURPLE))
    
    # Ubicación
    add_text_centered(draw, "📍 Ecuador", 510, 1640, font_medium, GRAY)
    
    img.save(f"{OUTPUT_DIR}/FB_Cover_Principal.png")
    print(f"✅ Creado: FB_Cover_Principal.png")

# ============================================================
# EJECUTAR TODAS LAS IMÁGENES
# ============================================================
if __name__ == "__main__":
    print("🎨 Generando imágenes para Entramados Estudio...\n")
    create_quote_card()
    create_carousel_cover()
    create_reel_thumbnail()
    create_tips_post()
    create_story_engagement()
    create_highlight_cover()
    create_before_after_banner()
    create_fb_cover()
    print(f"\n✅ Imágenes guardadas en: {OUTPUT_DIR}")
    print("📁 Archivos creados:")
    import os
    for f in sorted(os.listdir(OUTPUT_DIR)):
        size = os.path.getsize(f"{OUTPUT_DIR}/{f}") / 1024
        print(f"   - {f} ({size:.1f} KB)")
