#!/usr/bin/env python3
"""
Genera PDF profesional del Kit de Arranque para Entramados Estudio
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# Colores de marca
PURPLE = HexColor('#6366F1')
NAVY = HexColor('#1E1B4B')
LIGHT_PURPLE = HexColor('#E8E4F0')
CREAM = HexColor('#FAF8F5')
GRAY = HexColor('#6B7280')
CHARCOAL = HexColor('#1F2937')
GREEN = HexColor('#10B981')
ORANGE = HexColor('#F97316')

# Configuración
OUTPUT = "KIT_ARRANQUE_Entramados.pdf"
PAGE_SIZE = A4

def crear_pdf():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=PAGE_SIZE,
        rightMargin=1.5*cm,
        leftMargin=1.5*cm,
        topMargin=1.5*cm,
        bottomMargin=1.5*cm
    )
    
    # Estilos
    styles = getSampleStyleSheet()
    
    style_title = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=NAVY,
        alignment=TA_CENTER,
        spaceAfter=6,
        fontName='Helvetica-Bold'
    )
    
    style_subtitle = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=PURPLE,
        alignment=TA_CENTER,
        spaceAfter=30,
        fontName='Helvetica'
    )
    
    style_heading = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=NAVY,
        spaceBefore=20,
        spaceAfter=12,
        fontName='Helvetica-Bold',
        borderColor=PURPLE,
        borderWidth=2,
        borderPadding=5
    )
    
    style_subheading = ParagraphStyle(
        'CustomSubheading',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=PURPLE,
        spaceBefore=15,
        spaceAfter=8,
        fontName='Helvetica-Bold'
    )
    
    style_body = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        textColor=CHARCOAL,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
        leading=14,
        fontName='Helvetica'
    )
    
    style_body_small = ParagraphStyle(
        'CustomBodySmall',
        parent=styles['Normal'],
        fontSize=9,
        textColor=GRAY,
        alignment=TA_LEFT,
        spaceAfter=4,
        leading=12,
        fontName='Helvetica'
    )
    
    style_bullet = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontSize=10,
        textColor=CHARCOAL,
        leftIndent=20,
        spaceAfter=4,
        leading=13,
        fontName='Helvetica',
        bulletIndent=10
    )
    
    style_check = ParagraphStyle(
        'CustomCheck',
        parent=styles['Normal'],
        fontSize=10,
        textColor=CHARCOAL,
        leftIndent=15,
        spaceAfter=3,
        leading=13,
        fontName='Helvetica'
    )
    
    style_code = ParagraphStyle(
        'CustomCode',
        parent=styles['Normal'],
        fontSize=9,
        textColor=NAVY,
        backColor=LIGHT_PURPLE,
        leftIndent=10,
        rightIndent=10,
        spaceAfter=10,
        leading=13,
        fontName='Courier'
    )
    
    style_footer = ParagraphStyle(
        'CustomFooter',
        parent=styles['Normal'],
        fontSize=8,
        textColor=GRAY,
        alignment=TA_CENTER,
        spaceAfter=0,
        fontName='Helvetica-Oblique'
    )
    
    # Contenido
    story = []
    
    # === PORTADA ===
    story.append(Spacer(1, 3*cm))
    
    # Logo/Nombre
    story.append(Paragraph("🏠", ParagraphStyle('Emoji', parent=styles['Normal'], fontSize=40, alignment=TA_CENTER)))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("ENTRAMADOS ESTUDIO", style_title))
    story.append(Paragraph("KIT DE ARRANQUE", ParagraphStyle(
        'KitTitle',
        parent=styles['Heading1'],
        fontSize=22,
        textColor=PURPLE,
        alignment=TA_CENTER,
        spaceAfter=5,
        fontName='Helvetica-Bold'
    )))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("Guía de implementación para transformar tu presencia digital", style_subtitle))
    
    story.append(Spacer(1, 1*cm))
    
    # Info caja
    info_data = [
        ['📅 Fecha', '21 de marzo de 2026'],
        ['👤 Para', 'Mauri / Entramados Estudio'],
        ['⏱️ Tiempo de implementación', '2-3 horas'],
        ['📁 Incluye', 'Checklist + Captions + Calendario'],
    ]
    info_table = Table(info_data, colWidths=[5*cm, 10*cm])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), LIGHT_PURPLE),
        ('TEXTCOLOR', (0, 0), (0, -1), NAVY),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('BOX', (0, 0), (-1, -1), 1, PURPLE),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, HexColor('#DDD')),
    ]))
    story.append(info_table)
    
    story.append(Spacer(1, 2*cm))
    
    # Resumen
    story.append(Paragraph("🚀 Resumen Ejecutivo", style_heading))
    story.append(Paragraph(
        "Este kit contiene todo lo necesario para implementar los fundamentos de tu estrategia digital en "
        "una tarde. Está diseñado para ejecución inmediata — sin excusas.",
        style_body
    ))
    
    story.append(Paragraph("✨ Lo que lograrás:", style_subheading))
    
    beneficios = [
        "✅ Bio de Instagram optimizada y con CTA claro",
        "✅ Linktree configurado con todos tus canales",
        "✅ Google Business Profile activo (crítico para Ecuador)",
        "✅ Página de Facebook reconstruida",
        "✅ 5 posts listos para publicar",
        "✅ Calendario de contenido para la Semana 1",
        "✅ Respuestas automáticas de WhatsApp configuradas",
    ]
    for b in beneficios:
        story.append(Paragraph(b, style_bullet))
    
    story.append(PageBreak())
    
    # === SECCIÓN 1: CHECKLIST ===
    story.append(Paragraph("📋 CHECKLIST RÁPIDO", style_heading))
    
    checklist = [
        ("☐", "Actualizar bio de Instagram", "5 min"),
        ("☐", "Crear Linktree", "10 min"),
        ("☐", "Configurar Google Business Profile", "30 min"),
        ("☐", "Rebuild página de Facebook", "20 min"),
        ("☐", "Configurar WhatsApp Business", "10 min"),
        ("☐", "Publicar 5 posts iniciales", "1 hora"),
        ("☐", "Programar stories diarios", "10 min"),
    ]
    
    check_data = [['Estado', 'Acción', 'Tiempo']] + [[c[0], c[1], c[2]] for c in checklist]
    check_table = Table(check_data, colWidths=[1.5*cm, 11*cm, 2.5*cm])
    check_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (1, 1), (1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#DDD')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, CREAM]),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(check_table)
    
    # === SECCIÓN 2: BIO INSTAGRAM ===
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("1️⃣ ACTUALIZAR BIO INSTAGRAM", style_heading))
    
    story.append(Paragraph("Bio optimizada (copiar y pegar):", style_subheading))
    
    bio_text = """🏠 Diseño arquitectónico + Interiores<br/>
✨ Transformamos espacios vacíos en hogares soñados<br/>
🪵 Mobiliario custom a tu medida<br/>
📍 Ecuador | General Torres y Pedro León<br/>
📲 WhatsApp: [tu número]<br/>
🔗 linktr.ee/entramados"""
    
    story.append(Paragraph(bio_text, style_code))
    story.append(Paragraph("💡 Cómo cambiarlo: Ir a Instagram → Perfil → Editar perfil → Borrar todo → Copiar la bio → Cambiar el link", style_body_small))
    
    # === SECCIÓN 3: LINKTREE ===
    story.append(Paragraph("2️⃣ LINKTREE (Gratis)", style_heading))
    story.append(Paragraph("Pasos:", style_subheading))
    
    linktree_steps = [
        "1. Ir a <b>linktr.ee</b>",
        "2. Crear cuenta gratis",
        "3. Añadir estos enlaces:",
    ]
    for s in linktree_steps:
        story.append(Paragraph(s, style_bullet))
    
    link_data = [['Plataforma', 'URL'], ['WhatsApp', 'wa.me/[tu-número]'], ['Instagram', '@entramados_estudio78'], ['Facebook', 'Entramados Estudio'], ['Teléfono', 'tel:[tu-número]']]
    link_table = Table(link_data, colWidths=[4*cm, 11*cm])
    link_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PURPLE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#DDD')),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(Spacer(1, 0.2*cm))
    story.append(link_table)
    story.append(Paragraph("4. Poner el link en la bio de Instagram", style_body_small))
    
    # === SECCIÓN 4: GOOGLE BUSINESS ===
    story.append(PageBreak())
    story.append(Paragraph("3️⃣ GOOGLE BUSINESS PROFILE", style_heading))
    
    story.append(Paragraph("⚠️ Por qué es crítico:", style_subheading))
    reasons = ["Aparece en búsquedas locales 'cerca de mí'", "Reviews en Google = más confianza que Facebook", "Gratis y toma 30 minutos"]
    for r in reasons:
        story.append(Paragraph(f"• {r}", style_bullet))
    
    story.append(Paragraph("Pasos:", style_subheading))
    gb_steps = [
        "1. Ir a <b>business.google.com</b>",
        "2. Click 'Gestionar ahora'",
        "3. Buscar 'Entramados Estudio'",
        "4. Si no existe, click 'Añadir tu negocio'",
        "5. Rellenar con los datos del negocio",
        "6. Verificar por teléfono/correo"
    ]
    for s in gb_steps:
        story.append(Paragraph(s, style_bullet))
    
    gb_data = [['Campo', 'Valor'], ['Nombre', 'Entramados Estudio'], ['Categoría', 'Estudio de diseño arquitectónico'], ['Dirección', 'General Torres y Pedro León, Ecuador'], ['Teléfono', '[tu número]']]
    gb_table = Table(gb_data, colWidths=[4*cm, 11*cm])
    gb_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), GREEN),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#DDD')),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, CREAM]),
    ]))
    story.append(Spacer(1, 0.2*cm))
    story.append(gb_table)
    
    # === SECCIÓN 5: WHATSAPP ===
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("4️⃣ WHATSAPP BUSINESS - Respuesta Automática", style_heading))
    
    story.append(Paragraph("Mensaje de ausencia (copiar):", style_subheading))
    
    wa_text = """¡Hola! 👋 Gracias por contactar a Entramados Estudio.

Estoy viendo tu mensaje y te respondo lo antes posible.

Mientras tanto, puedes ver nuestro trabajo en:
📸 Instagram: @entramados_estudio78
📘 Facebook: Entramados Estudio

¡Gracias por tu paciencia! 🏠"""
    
    story.append(Paragraph(wa_text.replace('\n', '<br/>'), style_code))
    
    story.append(Paragraph("💡 Cómo activar: WhatsApp Business → Ajustes → Mensajes automáticos → Activar", style_body_small))
    
    # === SECCIÓN 6: CAPTIONS ===
    story.append(PageBreak())
    story.append(Paragraph("📝 PLANTILLAS DE CAPTIONS", style_heading))
    
    # Caption 1
    story.append(Paragraph("Caption — Antes/Después:", style_subheading))
    cap1 = """La diferencia entre un espacio vacío y un hogar soñado está en los detalles ✨<br/><br/>
[Descripción breve del proyecto]<br/><br/>
¿Tienes un espacio que necesita una segunda oportunidad? Escríbenos 💬<br/><br/>
🏠 @entramados_estudio78<br/>
📍 Diseño en Ecuador<br/><br/>
#ArquitecturaEcuador #InteriorismoEcuador #DiseñoDeInteriores #AntesYDespués #MueblesCustom"""
    story.append(Paragraph(cap1, style_code))
    
    # Caption 2
    story.append(Paragraph("Caption — Tips:", style_subheading))
    cap2 = """5 reglas de diseño que nunca fallan 👇<br/><br/>
1. La luz natural es tu mejor aliada<br/>
2. Menos es más<br/>
3. Los textiles dan calidez<br/>
4. Un punto focal<br/>
5. Personalidad en los detalles<br/><br/>
¿Cuál vas a aplicar? 💾 Guardar para después<br/><br/>
#TipsDeDiseño #InteriorismoEcuador #ArquitecturaDeInteriores"""
    story.append(Paragraph(cap2, style_code))
    
    # Caption 3
    story.append(Paragraph("Caption — Mobiliario:", style_subheading))
    cap3 = """Muebles que se adaptan a ti, no al revés 🪵<br/><br/>
Diseñamos closets, cocinas y muebles que maximizan cada centímetro y reflejan tu estilo.<br/><br/>
📩 Escríbenos: [link bio]<br/><br/>
#MueblesCustom #DiseñoDeMuebles #CarpinteriaEcuador"""
    story.append(Paragraph(cap3, style_code))
    
    # === SECCIÓN 7: CALENDARIO ===
    story.append(PageBreak())
    story.append(Paragraph("📅 CALENDARIO SEMANA 1", style_heading))
    
    cal_data = [
        ['Día', 'Qué publicar', 'Tiempo', 'Estado'],
        ['Lunes', 'Reel Before/After (usar imagen Leonardo)', '15 min', '☐'],
        ['Martes', 'Post Tips (5 reglas)', '10 min', '☐'],
        ['Miércoles', 'Stories (detrás de cámaras)', '10 min', '☐'],
        ['Jueves', 'Post Mobiliario', '10 min', '☐'],
        ['Viernes', 'Post Before/After (otra habitación)', '10 min', '☐'],
        ['Sábado', 'Stories interactivos (pregunta)', '10 min', '☐'],
        ['Domingo', 'Planificar semana 2', '30 min', '☐'],
    ]
    cal_table = Table(cal_data, colWidths=[2*cm, 8*cm, 2*cm, 1.5*cm])
    cal_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (1, 1), (1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#DDD')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, CREAM]),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(cal_table)
    
    # === SECCIÓN 8: MÉTRICAS ===
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("📊 MÉTRICAS A SEGUIR", style_heading))
    
    story.append(Paragraph("Qué medir cada semana:", style_subheading))
    
    met_data = [
        ['Métrica', 'Herramienta', 'Meta Semana 1'],
        ['Seguidores IG', 'Instagram Insights', '+10-15'],
        ['Engagement', 'Instagram Insights', '3%+'],
        ['Alcance', 'Instagram Insights', '500+'],
        ['Mensajes WhatsApp', 'WhatsApp Business', '3-5'],
        ['Visitas Google', 'Google Business', '+20'],
    ]
    met_table = Table(met_data, colWidths=[5*cm, 5*cm, 4*cm])
    met_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PURPLE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#DDD')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, CREAM]),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(met_table)
    
    # === FOOTER ===
    story.append(Spacer(1, 1*cm))
    story.append(HRFlowable(width="100%", thickness=1, color=PURPLE))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("Kit creado por AI Company System — Mauri Esp | 21 de marzo de 2026", style_footer))
    
    # Construir PDF
    doc.build(story)
    print(f"✅ PDF creado: {OUTPUT}")

if __name__ == "__main__":
    crear_pdf()
