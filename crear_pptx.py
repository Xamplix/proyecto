from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Colores
DARK_BG = RGBColor(0x0F, 0x0C, 0x29)
RED_BG = RGBColor(0x1A, 0x00, 0x00)
ORANGE_BG = RGBColor(0x1A, 0x10, 0x00)
GREEN_BG = RGBColor(0x00, 0x1A, 0x0A)
BLUE_BG = RGBColor(0x0A, 0x0A, 0x2E)
PURPLE_BG = RGBColor(0x1A, 0x0A, 0x2E)
NAVY_BG = RGBColor(0x0A, 0x1A, 0x2E)
YELLOW_BG = RGBColor(0x1A, 0x1A, 0x00)

WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY = RGBColor(0xCC, 0xCC, 0xCC)
GRAY = RGBColor(0x88, 0x88, 0x88)
RED = RGBColor(0xFF, 0x44, 0x44)
RED_LIGHT = RGBColor(0xFF, 0x66, 0x66)
GREEN = RGBColor(0x44, 0xFF, 0x88)
GREEN_LIGHT = RGBColor(0x66, 0xFF, 0xAA)
BLUE = RGBColor(0x44, 0xAA, 0xFF)
BLUE_LIGHT = RGBColor(0x88, 0xAA, 0xFF)
ORANGE = RGBColor(0xFF, 0xAA, 0x00)
ORANGE_LIGHT = RGBColor(0xFF, 0xCC, 0x44)
PURPLE = RGBColor(0xCC, 0x88, 0xFF)
YELLOW = RGBColor(0xFF, 0xDD, 0x44)


def set_slide_bg(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_text_box(slide, left, top, width, height, text, font_size=18,
                 color=WHITE, bold=False, alignment=PP_ALIGN.LEFT, font_name="Calibri"):
    txBox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = font_name
    p.alignment = alignment
    return txBox


def add_paragraph(text_frame, text, font_size=18, color=WHITE, bold=False,
                  alignment=PP_ALIGN.LEFT, space_before=Pt(6)):
    p = text_frame.add_paragraph()
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = "Calibri"
    p.alignment = alignment
    p.space_before = space_before
    return p


def add_rounded_rect(slide, left, top, width, height, fill_color, border_color=None):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(left), Inches(top), Inches(width), Inches(height)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.5)
    else:
        shape.line.fill.background()
    return shape


# ============================================================
# SLIDE 1: PORTADA
# ============================================================
slide1 = prs.slides.add_slide(prs.slide_layouts[6])  # blank
set_slide_bg(slide1, DARK_BG)

add_text_box(slide1, 1, 1.2, 11.3, 1.2, "Grupo 7", 28, GRAY, alignment=PP_ALIGN.CENTER)
add_text_box(slide1, 1, 2.0, 11.3, 1.5, "La Memoria de Pez", 54, WHITE, bold=True, alignment=PP_ALIGN.CENTER)
add_text_box(slide1, 1, 3.3, 11.3, 0.8, "Deep Learning Audit  -  El Rescate de HealthTech", 24, BLUE_LIGHT, alignment=PP_ALIGN.CENTER)

add_text_box(slide1, 3, 4.8, 7.3, 1.5,
             "Universidad Privada del Norte - Escuela de Posgrado\n"
             "Modelos de Deep Learning - Sesion N 2",
             16, GRAY, alignment=PP_ALIGN.CENTER)

# ============================================================
# SLIDE 2: EL PROBLEMA
# ============================================================
slide2 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide2, RED_BG)

add_text_box(slide2, 0.8, 0.4, 11.7, 0.9, "El Sabotaje: Sin Regularizacion", 40, RED, bold=True)

# Card 1: Sintoma
add_rounded_rect(slide2, 0.8, 1.5, 5.7, 2.5, RGBColor(0x2A, 0x05, 0x05), RED_LIGHT)
add_text_box(slide2, 1.1, 1.7, 5.1, 0.5, "Sintoma Principal", 20, RED_LIGHT, bold=True)
add_text_box(slide2, 1.1, 2.3, 5.1, 1.5,
             "El modelo alcanza ~100% accuracy en entrenamiento pero falla en datos nuevos. "
             "Ha MEMORIZADO cada muestra en vez de aprender patrones reales.\n\n"
             "\"La perdida de train baja a 0, pero la de test sube sin parar.\"",
             14, LIGHT_GRAY)

# Card 2: Numeros
add_rounded_rect(slide2, 6.8, 1.5, 5.7, 2.5, RGBColor(0x2A, 0x05, 0x05), RED_LIGHT)
add_text_box(slide2, 7.1, 1.7, 5.1, 0.5, "Los Numeros", 20, RED_LIGHT, bold=True)
add_text_box(slide2, 7.1, 2.3, 5.1, 1.5,
             "~19,000 parametros en el modelo\n"
             "60 muestras de entrenamiento (de 100 totales)\n"
             "Ratio ~300:1\n\n"
             "El modelo puede memorizar TODO sin esfuerzo",
             14, LIGHT_GRAY)

# Card 3: Lo que falta
add_rounded_rect(slide2, 0.8, 4.3, 5.7, 2.5, RGBColor(0x2A, 0x05, 0x05), RED_LIGHT)
add_text_box(slide2, 1.1, 4.5, 5.1, 0.5, "Lo que falta", 20, RED_LIGHT, bold=True)
add_text_box(slide2, 1.1, 5.1, 5.1, 1.5,
             "- No hay Weight Decay (penalizacion L2)\n"
             "- No hay Dropout\n"
             "- No hay Early Stopping\n"
             "- Red sobredimensionada para tan pocos datos",
             14, LIGHT_GRAY)

# Card 4: Impacto
add_rounded_rect(slide2, 6.8, 4.3, 5.7, 2.5, RGBColor(0x2A, 0x05, 0x05), RED_LIGHT)
add_text_box(slide2, 7.1, 4.5, 5.1, 0.5, "Impacto en HealthTech", 20, RED_LIGHT, bold=True)
add_text_box(slide2, 7.1, 5.1, 5.1, 1.5,
             "En produccion, el modelo no detectaria patologias nuevas "
             "correctamente. Solo \"recuerda\" los casos que ya vio.\n\n"
             "Un paciente nuevo = diagnostico poco confiable.",
             14, LIGHT_GRAY)

# ============================================================
# SLIDE 3: DIAGNOSTICO
# ============================================================
slide3 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide3, ORANGE_BG)

add_text_box(slide3, 0.8, 0.4, 11.7, 0.9, "Diagnostico", 40, ORANGE, bold=True)

diagnosticos = [
    ("Sintoma:", "Train accuracy converge a ~100% mientras test accuracy se estanca o cae. La perdida de test diverge."),
    ("Causa raiz:", "Sin regularizacion, los pesos crecen sin control. Con muchos parametros y pocos datos, la red memoriza cada muestra incluyendo el ruido."),
    ("Evidencia:", "Los pesos del modelo muestran valores grandes y dispersos (alta varianza), senal de que el modelo codifica ruido en vez de patrones."),
    ("Analogia:", "Es como un estudiante que memoriza las respuestas del examen de practica en vez de aprender la materia - perfecto en lo visto, pesimo en preguntas nuevas."),
    ("Indicador:", "La brecha (gap) entre train accuracy y test accuracy. Con overfitting violento, esta brecha supera el 20-30%."),
]

y_pos = 1.5
for titulo, desc in diagnosticos:
    add_rounded_rect(slide3, 0.8, y_pos, 11.7, 0.95, RGBColor(0x2A, 0x1A, 0x00), ORANGE)
    tb = add_text_box(slide3, 1.1, y_pos + 0.15, 11.1, 0.7, "", 14, LIGHT_GRAY)
    tf = tb.text_frame
    tf.paragraphs[0].text = ""
    run1 = tf.paragraphs[0].add_run()
    run1.text = titulo + " "
    run1.font.bold = True
    run1.font.color.rgb = ORANGE_LIGHT
    run1.font.size = Pt(15)
    run2 = tf.paragraphs[0].add_run()
    run2.text = desc
    run2.font.color.rgb = LIGHT_GRAY
    run2.font.size = Pt(14)
    y_pos += 1.1

# ============================================================
# SLIDE 4: LA CORRECCION
# ============================================================
slide4 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide4, GREEN_BG)

add_text_box(slide4, 0.8, 0.4, 11.7, 0.9, "El Interruptor: Regularizacion", 40, GREEN, bold=True)

# 3 cards
cards = [
    ("Weight Decay (L2)", "Penaliza pesos grandes anadiendo\nlambda*||w||^2 a la perdida.\nEncoge los pesos hacia cero\nen cada actualizacion.", "weight_decay=0.01"),
    ("Dropout", "Apaga neuronas al azar durante\nel entrenamiento (p=0.3).\nImpide que la red dependa\nde neuronas individuales.", "nn.Dropout(0.3)"),
    ("Reducir Capacidad", "Menos capas y neuronas para que\nla red no pueda memorizar todo.\nAdecuamos la complejidad al\ntamano del dataset.", "64->16 neuronas"),
]

for i, (titulo, desc, code) in enumerate(cards):
    x = 0.8 + i * 4.1
    add_rounded_rect(slide4, x, 1.5, 3.8, 4.0, RGBColor(0x05, 0x2A, 0x10), GREEN_LIGHT)
    add_text_box(slide4, x + 0.2, 1.7, 3.4, 0.5, titulo, 22, GREEN_LIGHT, bold=True, alignment=PP_ALIGN.CENTER)
    add_text_box(slide4, x + 0.2, 2.4, 3.4, 2.0, desc, 14, LIGHT_GRAY, alignment=PP_ALIGN.CENTER)
    add_rounded_rect(slide4, x + 0.5, 4.5, 2.8, 0.5, RGBColor(0x00, 0x15, 0x05))
    add_text_box(slide4, x + 0.6, 4.55, 2.6, 0.4, code, 14, GREEN_LIGHT, alignment=PP_ALIGN.CENTER, font_name="Consolas")

add_text_box(slide4, 0.8, 6.0, 11.7, 0.6,
             "ANTES: 5 capas, ~19K params, sin regularizacion    -->    DESPUES: 3 capas, ~300 params, con Dropout + L2",
             15, GREEN_LIGHT, alignment=PP_ALIGN.CENTER)

# ============================================================
# SLIDE 5: ANTES vs DESPUES (tabla)
# ============================================================
slide5 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide5, BLUE_BG)

add_text_box(slide5, 0.8, 0.4, 11.7, 0.9, "Antes vs Despues", 40, BLUE_LIGHT, bold=True)

# Table
rows_data = [
    ("Metrica", "Saboteado", "Corregido"),
    ("Train Accuracy", "~100%", "~90-94%"),
    ("Test Accuracy", "~65-75%", "~87-93%"),
    ("Gap (Train - Test)", "~25-35%", "~3-7%"),
    ("Perdida de Test", "Diverge", "Estable"),
    ("Pesos (Std)", "Alto (disperso)", "Bajo (compacto)"),
    ("Weight Decay", "0.0 (OFF)", "0.01 (ON)"),
    ("Dropout", "NO", "p = 0.3"),
    ("Parametros", "~19,000", "~300"),
]

table = slide5.shapes.add_table(len(rows_data), 3, Inches(1.5), Inches(1.5), Inches(10.3), Inches(5.2)).table
table.columns[0].width = Inches(3.8)
table.columns[1].width = Inches(3.25)
table.columns[2].width = Inches(3.25)

for row_idx, (c1, c2, c3) in enumerate(rows_data):
    for col_idx, text in enumerate([c1, c2, c3]):
        cell = table.cell(row_idx, col_idx)
        cell.text = text
        for paragraph in cell.text_frame.paragraphs:
            paragraph.font.size = Pt(15)
            paragraph.font.name = "Calibri"
            if row_idx == 0:
                paragraph.font.bold = True
                if col_idx == 0:
                    paragraph.font.color.rgb = GRAY
                elif col_idx == 1:
                    paragraph.font.color.rgb = RED_LIGHT
                else:
                    paragraph.font.color.rgb = GREEN_LIGHT
            else:
                if col_idx == 0:
                    paragraph.font.color.rgb = LIGHT_GRAY
                    paragraph.font.bold = True
                elif col_idx == 1:
                    paragraph.font.color.rgb = RGBColor(0xFF, 0x88, 0x88)
                else:
                    paragraph.font.color.rgb = RGBColor(0x88, 0xFF, 0xBB)
        # Cell background
        cell_fill = cell.fill
        cell_fill.solid()
        if row_idx == 0:
            if col_idx == 0:
                cell_fill.fore_color.rgb = RGBColor(0x1A, 0x1A, 0x3E)
            elif col_idx == 1:
                cell_fill.fore_color.rgb = RGBColor(0x2A, 0x0A, 0x0A)
            else:
                cell_fill.fore_color.rgb = RGBColor(0x0A, 0x2A, 0x15)
        else:
            cell_fill.fore_color.rgb = RGBColor(0x12, 0x12, 0x30)

# ============================================================
# SLIDE 6: REPRESENTATION LEARNING
# ============================================================
slide6 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide6, PURPLE_BG)

add_text_box(slide6, 0.8, 0.4, 11.7, 0.9, "Anatomia del Exito: Representation Learning", 36, PURPLE, bold=True)

# Card izquierda
add_rounded_rect(slide6, 0.8, 1.6, 5.7, 4.5, RGBColor(0x20, 0x0A, 0x30), RED_LIGHT)
add_text_box(slide6, 1.1, 1.8, 5.1, 0.5, "Sin Regularizacion", 24, RED_LIGHT, bold=True)
add_text_box(slide6, 1.1, 2.5, 5.1, 3.2,
             "La red construye representaciones hiper-especificas "
             "de cada muestra individual.\n\n"
             "-> Memoriza el ruido y artefactos de cada dato\n"
             "-> Las features internas no son transferibles\n"
             "-> No aprende \"conceptos\" como bordes o formas\n"
             "-> Cada neurona se sobreactiva para casos puntuales",
             14, LIGHT_GRAY)

# Card derecha
add_rounded_rect(slide6, 6.8, 1.6, 5.7, 4.5, RGBColor(0x0A, 0x20, 0x15), GREEN_LIGHT)
add_text_box(slide6, 7.1, 1.8, 5.1, 0.5, "Con Regularizacion", 24, GREEN_LIGHT, bold=True)
add_text_box(slide6, 7.1, 2.5, 5.1, 3.2,
             "La red aprende representaciones generalizables "
             "- patrones que aplican a datos nuevos.\n\n"
             "-> Captura estructura real: distribuciones, correlaciones\n"
             "-> Features compartidas entre muestras similares\n"
             "-> Capas intermedias actuan como detectores de patrones\n"
             "-> Jerarquia: features simples -> features complejas",
             14, LIGHT_GRAY)

add_text_box(slide6, 0.8, 6.4, 11.7, 0.6,
             "La regularizacion fuerza a la red a buscar patrones compartidos en vez de memorizar caso por caso.",
             16, PURPLE, bold=True, alignment=PP_ALIGN.CENTER)

# ============================================================
# SLIDE 7: DECISION DE NEGOCIO
# ============================================================
slide7 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide7, NAVY_BG)

add_text_box(slide7, 0.8, 0.4, 11.7, 0.9, "Decision de Negocio", 40, BLUE, bold=True)

add_rounded_rect(slide7, 0.8, 1.5, 11.7, 1.3, RGBColor(0x0A, 0x20, 0x3A), BLUE)
add_text_box(slide7, 1.1, 1.6, 11.1, 0.4, "Si tuvieramos mas presupuesto, donde invertirlo?", 20, BLUE_LIGHT, bold=True)
add_text_box(slide7, 1.1, 2.1, 11.1, 0.5, "Recomendacion: Invertir en DATOS + NAVEGACION (optimizacion), no solo en mejores activaciones.", 16, RGBColor(0x88, 0xDD, 0xFF), bold=True)

# Card 1
add_rounded_rect(slide7, 0.8, 3.2, 5.7, 3.0, RGBColor(0x0A, 0x20, 0x3A), BLUE)
add_text_box(slide7, 1.1, 3.4, 5.1, 0.5, "Prioridad 1: Mas Datos", 20, BLUE_LIGHT, bold=True)
add_text_box(slide7, 1.1, 4.0, 5.1, 2.0,
             "Con un dataset pequeno, ninguna regularizacion "
             "es tan buena como tener mas muestras.\n\n"
             "Data Augmentation, recopilacion de mas imagenes "
             "medicas, o tecnicas como Transfer Learning "
             "con modelos pre-entrenados.",
             14, LIGHT_GRAY)

# Card 2
add_rounded_rect(slide7, 6.8, 3.2, 5.7, 3.0, RGBColor(0x0A, 0x20, 0x3A), BLUE)
add_text_box(slide7, 7.1, 3.4, 5.1, 0.5, "Prioridad 2: Mejor Regularizacion", 20, BLUE_LIGHT, bold=True)
add_text_box(slide7, 7.1, 4.0, 5.1, 2.0,
             "Combinar multiples tecnicas:\n"
             "L2 + Dropout + Batch Normalization + Early Stopping.\n\n"
             "Usar validacion cruzada (k-fold) dado el tamano "
             "limitado del dataset para estimar el rendimiento real.",
             14, LIGHT_GRAY)

add_text_box(slide7, 0.8, 6.5, 11.7, 0.5,
             "En medicina, un modelo que memoriza es PELIGROSO - puede dar falsos negativos en pacientes nuevos.",
             15, RGBColor(0x88, 0xCC, 0xFF), alignment=PP_ALIGN.CENTER)

# ============================================================
# SLIDE 8: BONUS MATEMATICO
# ============================================================
slide8 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide8, YELLOW_BG)

add_text_box(slide8, 0.8, 0.4, 11.7, 0.9, "Bonus Matematico", 40, YELLOW, bold=True)

# 4 cards (2x2)
math_cards = [
    ("Sin Weight Decay",
     "theta(t+1) = theta(t) - n * grad(L)",
     "Los pesos se actualizan solo por el gradiente. No hay limite al crecimiento de los pesos."),
    ("Con Weight Decay (L2)",
     "theta(t+1) = (1-n*lambda)*theta(t) - n*grad(L)",
     "El factor (1-n*lambda) encoge los pesos en cada paso. Pesos grandes se penalizan mas."),
    ("Efecto del Dropout",
     "h_i = x_i/(1-p) con prob (1-p), o 0 con prob p",
     "Equivale a entrenar un ensemble de sub-redes. Cada forward pass usa una red diferente."),
    ("Grafo de Computacion",
     "L_total = L_BCE + lambda * sum(||w_i||^2)",
     "El termino de regularizacion anade gradiente 2*lambda*w_i que controla la magnitud de cada peso."),
]

positions = [(0.8, 1.5), (6.8, 1.5), (0.8, 4.2), (6.8, 4.2)]
for (titulo, formula, desc), (x, y_p) in zip(math_cards, positions):
    add_rounded_rect(slide8, x, y_p, 5.7, 2.4, RGBColor(0x2A, 0x2A, 0x05), YELLOW)
    add_text_box(slide8, x + 0.2, y_p + 0.15, 5.3, 0.4, titulo, 18, RGBColor(0xFF, 0xEE, 0x88), bold=True)
    # Formula box
    add_rounded_rect(slide8, x + 0.3, y_p + 0.65, 5.1, 0.55, RGBColor(0x10, 0x10, 0x00))
    add_text_box(slide8, x + 0.4, y_p + 0.7, 4.9, 0.45, formula, 14, RGBColor(0xFF, 0xDD, 0x88), font_name="Consolas", alignment=PP_ALIGN.CENTER)
    add_text_box(slide8, x + 0.2, y_p + 1.35, 5.3, 0.9, desc, 13, LIGHT_GRAY)

# ============================================================
# SLIDE 9: CONCLUSIONES
# ============================================================
slide9 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide9, DARK_BG)

add_text_box(slide9, 0.8, 0.4, 11.7, 0.9, "Conclusiones", 44, GREEN, bold=True, alignment=PP_ALIGN.CENTER)

conclusiones = [
    ("Diagnostico:", "El modelo memorizaba el dataset de entrenamiento (Train ~100%, Test ~65-75%). Overfitting violento por falta de regularizacion con dataset pequeno."),
    ("El Interruptor:", "Activamos Weight Decay (L2 = 0.01), Dropout (p = 0.3) y redujimos la capacidad de la red de ~19K a ~300 parametros."),
    ("Anatomia del Exito:", "El modelo paso de memorizar ruido a aprender representaciones generalizables. Ahora detecta patrones reales en datos no vistos."),
    ("Resultado:", "La brecha train-test se redujo de ~30% a menos del 7%. El modelo ahora GENERALIZA en vez de memorizar."),
    ("Leccion para HealthTech:", "En medicina, un modelo con overfitting puede dar diagnosticos falsos en pacientes nuevos. La regularizacion no es opcional, es esencial."),
]

y_pos = 1.6
for titulo, desc in conclusiones:
    add_rounded_rect(slide9, 1.5, y_pos, 10.3, 0.85, RGBColor(0x15, 0x12, 0x35))
    # Green left bar
    add_rounded_rect(slide9, 1.5, y_pos, 0.08, 0.85, GREEN)
    tb = add_text_box(slide9, 1.9, y_pos + 0.1, 9.7, 0.65, "", 14, LIGHT_GRAY)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].text = ""
    run1 = tf.paragraphs[0].add_run()
    run1.text = titulo + " "
    run1.font.bold = True
    run1.font.color.rgb = GREEN_LIGHT
    run1.font.size = Pt(15)
    run2 = tf.paragraphs[0].add_run()
    run2.text = desc
    run2.font.color.rgb = LIGHT_GRAY
    run2.font.size = Pt(14)
    y_pos += 1.0

add_text_box(slide9, 1, 6.6, 11.3, 0.5,
             "Grupo 7 - La Memoria de Pez  |  Bloque 3: Problemas de Estrategia",
             14, GRAY, alignment=PP_ALIGN.CENTER)


# ============================================================
# GUARDAR
# ============================================================
prs.save('/home/user/proyecto/Grupo7_La_Memoria_de_Pez.pptx')
print("Presentacion PPTX creada exitosamente!")
