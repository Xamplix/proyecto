from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Colores minimalistas
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BLACK = RGBColor(0x1A, 0x1A, 0x1A)
DARK_GRAY = RGBColor(0x33, 0x33, 0x33)
MID_GRAY = RGBColor(0x66, 0x66, 0x66)
LIGHT_GRAY = RGBColor(0x99, 0x99, 0x99)
ACCENT = RGBColor(0x00, 0x66, 0xCC)  # azul sobrio
RED_ACCENT = RGBColor(0xCC, 0x33, 0x33)
GREEN_ACCENT = RGBColor(0x22, 0x88, 0x44)
BG = RGBColor(0xFA, 0xFA, 0xFA)


def set_bg(slide):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = BG


def add_text(slide, left, top, width, height, text, size=18,
             color=DARK_GRAY, bold=False, align=PP_ALIGN.LEFT, name="Calibri"):
    box = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = name
    p.alignment = align
    return box


def add_body(slide, left, top, width, height, lines, size=16, color=DARK_GRAY):
    """Add multiple lines as separate paragraphs with bullet-style."""
    box = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = line
        p.font.size = Pt(size)
        p.font.color.rgb = color
        p.font.name = "Calibri"
        p.space_before = Pt(8)
        p.space_after = Pt(4)
    return box


def add_line(slide, left, top, width):
    """Thin horizontal line."""
    shape = slide.shapes.add_shape(
        1,  # rectangle
        Inches(left), Inches(top), Inches(width), Pt(2)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = ACCENT
    shape.line.fill.background()


# ============================================================
# SLIDE 1: PORTADA
# ============================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(s)

add_text(s, 1.5, 1.8, 10.3, 0.6, "GRUPO 7", 20, LIGHT_GRAY, align=PP_ALIGN.LEFT)
add_text(s, 1.5, 2.4, 10.3, 1.0, "La Memoria de Pez", 48, BLACK, bold=True)
add_line(s, 1.5, 3.5, 3.0)
add_text(s, 1.5, 3.8, 10.3, 0.5, "Deep Learning Audit: El Rescate de HealthTech", 22, ACCENT)
add_text(s, 1.5, 5.0, 10.3, 0.8,
         "Universidad Privada del Norte  |  Escuela de Posgrado\nModelos de Deep Learning  |  Sesion 2",
         14, LIGHT_GRAY)

# ============================================================
# SLIDE 2: EL PROBLEMA
# ============================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(s)

add_text(s, 1.5, 0.6, 10.3, 0.7, "El Problema", 40, BLACK, bold=True)
add_line(s, 1.5, 1.3, 2.0)

add_text(s, 1.5, 1.6, 10.3, 0.5, "Sabotaje: dataset pequeno sin regularizacion ni weight decay", 18, RED_ACCENT, bold=True)

add_body(s, 1.5, 2.3, 10.3, 4.5, [
    "El modelo tiene ~19,000 parametros pero solo 60 muestras de entrenamiento",
    "Ratio parametros/muestras: ~300:1  (puede memorizar todo sin esfuerzo)",
    "",
    "Lo que falta:",
    "    -  No hay Weight Decay (penalizacion L2)",
    "    -  No hay Dropout",
    "    -  No hay Early Stopping",
    "    -  Red sobredimensionada para tan pocos datos",
    "",
    "Resultado: el modelo alcanza ~100% en train pero falla en datos nuevos.",
    "Ha memorizado cada muestra en vez de aprender patrones.",
], size=17)

# ============================================================
# SLIDE 3: DIAGNOSTICO
# ============================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(s)

add_text(s, 1.5, 0.6, 10.3, 0.7, "Diagnostico", 40, BLACK, bold=True)
add_line(s, 1.5, 1.3, 2.0)

add_body(s, 1.5, 1.7, 10.3, 5.5, [
    "Sintoma: Train accuracy ~100%, test accuracy ~65-75%.",
    "La perdida de test diverge mientras la de train baja a cero.",
    "",
    "Causa raiz: sin regularizacion, los pesos crecen sin control.",
    "Con muchos parametros y pocos datos, la red memoriza cada",
    "muestra incluyendo el ruido.",
    "",
    "Evidencia: los pesos muestran valores grandes y dispersos",
    "(alta varianza), codificando ruido en vez de patrones.",
    "",
    "Analogia: un estudiante que memoriza las respuestas del examen",
    "de practica en vez de aprender la materia.",
], size=17)

# ============================================================
# SLIDE 4: LA CORRECCION
# ============================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(s)

add_text(s, 1.5, 0.6, 10.3, 0.7, "La Correccion", 40, BLACK, bold=True)
add_line(s, 1.5, 1.3, 2.0)

add_text(s, 1.5, 1.7, 10.3, 0.4, "1. Weight Decay (L2)", 22, ACCENT, bold=True)
add_body(s, 1.8, 2.2, 9.5, 0.9, [
    "Penaliza pesos grandes sumando lambda*||w||^2 a la perdida.",
    "weight_decay = 0.01 en el optimizador Adam.",
], size=16)

add_text(s, 1.5, 3.2, 10.3, 0.4, "2. Dropout", 22, ACCENT, bold=True)
add_body(s, 1.8, 3.7, 9.5, 0.9, [
    "Apaga neuronas al azar durante el entrenamiento (p=0.3).",
    "Impide que la red dependa de neuronas individuales.",
], size=16)

add_text(s, 1.5, 4.7, 10.3, 0.4, "3. Reducir capacidad", 22, ACCENT, bold=True)
add_body(s, 1.8, 5.2, 9.5, 0.9, [
    "De 5 capas (~19K params) a 3 capas (~300 params).",
    "Adecuamos la complejidad al tamano del dataset.",
], size=16)

# ============================================================
# SLIDE 5: ANTES vs DESPUES
# ============================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(s)

add_text(s, 1.5, 0.6, 10.3, 0.7, "Antes vs Despues", 40, BLACK, bold=True)
add_line(s, 1.5, 1.3, 2.0)

rows = [
    ("Metrica",           "Saboteado",       "Corregido"),
    ("Train Accuracy",    "~100%",           "~90-94%"),
    ("Test Accuracy",     "~65-75%",         "~87-93%"),
    ("Gap (Train-Test)",  "~25-35%",         "~3-7%"),
    ("Loss de Test",      "Diverge",         "Estable"),
    ("Weight Decay",      "0.0 (OFF)",       "0.01 (ON)"),
    ("Dropout",           "NO",              "p = 0.3"),
    ("Parametros",        "~19,000",         "~300"),
]

tbl = s.shapes.add_table(len(rows), 3, Inches(1.5), Inches(1.7), Inches(10.3), Inches(4.8)).table
tbl.columns[0].width = Inches(3.5)
tbl.columns[1].width = Inches(3.4)
tbl.columns[2].width = Inches(3.4)

for r, (c1, c2, c3) in enumerate(rows):
    for c, txt in enumerate([c1, c2, c3]):
        cell = tbl.cell(r, c)
        cell.text = txt
        cell.fill.solid()
        for p in cell.text_frame.paragraphs:
            p.font.name = "Calibri"
            p.font.size = Pt(15)
            if r == 0:
                p.font.bold = True
                p.font.color.rgb = WHITE
                cell.fill.fore_color.rgb = ACCENT if c == 0 else (RED_ACCENT if c == 1 else GREEN_ACCENT)
            else:
                p.font.color.rgb = DARK_GRAY
                cell.fill.fore_color.rgb = WHITE if r % 2 == 1 else RGBColor(0xF0, 0xF0, 0xF0)

# ============================================================
# SLIDE 6: REPRESENTATION LEARNING
# ============================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(s)

add_text(s, 1.5, 0.6, 10.3, 0.7, "Representation Learning", 40, BLACK, bold=True)
add_line(s, 1.5, 1.3, 2.0)

add_text(s, 1.5, 1.7, 5.0, 0.4, "Sin regularizacion", 22, RED_ACCENT, bold=True)
add_body(s, 1.5, 2.2, 5.0, 3.0, [
    "-  Memoriza ruido y artefactos",
    "-  Features no transferibles",
    "-  No aprende conceptos generales",
    "-  Neuronas sobreactivadas para",
    "   casos puntuales",
], size=16)

add_text(s, 7.3, 1.7, 5.0, 0.4, "Con regularizacion", 22, GREEN_ACCENT, bold=True)
add_body(s, 7.3, 2.2, 5.0, 3.0, [
    "-  Captura patrones reales",
    "-  Features compartidas entre muestras",
    "-  Detectores de patrones en capas",
    "   intermedias",
    "-  Jerarquia: simple a complejo",
], size=16)

add_text(s, 1.5, 5.5, 10.3, 0.6,
         "La regularizacion fuerza a la red a buscar patrones compartidos\nen vez de memorizar caso por caso.",
         17, MID_GRAY, align=PP_ALIGN.CENTER)

# ============================================================
# SLIDE 7: DECISION DE NEGOCIO
# ============================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(s)

add_text(s, 1.5, 0.6, 10.3, 0.7, "Decision de Negocio", 40, BLACK, bold=True)
add_line(s, 1.5, 1.3, 2.0)

add_text(s, 1.5, 1.7, 10.3, 0.5, "Con mas presupuesto, invertir en datos + regularizacion.", 18, ACCENT, bold=True)

add_text(s, 1.5, 2.5, 10.3, 0.4, "Prioridad 1: Mas datos", 22, DARK_GRAY, bold=True)
add_body(s, 1.8, 3.0, 9.5, 1.2, [
    "Con un dataset pequeno, ninguna tecnica supera tener mas muestras.",
    "Data Augmentation, Transfer Learning, recopilacion de imagenes medicas.",
], size=16)

add_text(s, 1.5, 4.2, 10.3, 0.4, "Prioridad 2: Mejor regularizacion", 22, DARK_GRAY, bold=True)
add_body(s, 1.8, 4.7, 9.5, 1.2, [
    "Combinar L2 + Dropout + Batch Normalization + Early Stopping.",
    "Validacion cruzada (k-fold) para estimar rendimiento real.",
], size=16)

add_text(s, 1.5, 6.0, 10.3, 0.5,
         "En medicina, un modelo que memoriza es peligroso:\npuede dar falsos negativos en pacientes nuevos.",
         16, RED_ACCENT)

# ============================================================
# SLIDE 8: BONUS MATEMATICO
# ============================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(s)

add_text(s, 1.5, 0.6, 10.3, 0.7, "Bonus Matematico", 40, BLACK, bold=True)
add_line(s, 1.5, 1.3, 2.0)

add_text(s, 1.5, 1.7, 10.3, 0.4, "Sin Weight Decay:", 18, DARK_GRAY, bold=True)
add_text(s, 1.8, 2.2, 9.0, 0.4, "theta(t+1)  =  theta(t) - n * grad(L)", 16, MID_GRAY, name="Consolas")

add_text(s, 1.5, 2.9, 10.3, 0.4, "Con Weight Decay (L2):", 18, DARK_GRAY, bold=True)
add_text(s, 1.8, 3.4, 9.0, 0.4, "theta(t+1)  =  (1 - n*lambda) * theta(t) - n * grad(L)", 16, MID_GRAY, name="Consolas")
add_text(s, 1.8, 3.9, 9.0, 0.4, "El factor (1 - n*lambda) encoge los pesos en cada paso.", 15, MID_GRAY)

add_text(s, 1.5, 4.6, 10.3, 0.4, "Dropout:", 18, DARK_GRAY, bold=True)
add_text(s, 1.8, 5.1, 9.0, 0.4, "h_i = x_i/(1-p) con prob (1-p),  o  0 con prob p", 16, MID_GRAY, name="Consolas")
add_text(s, 1.8, 5.6, 9.0, 0.4, "Equivale a entrenar un ensemble de sub-redes.", 15, MID_GRAY)

add_text(s, 1.5, 6.3, 10.3, 0.4, "Loss total:", 18, DARK_GRAY, bold=True)
add_text(s, 1.8, 6.7, 9.0, 0.4, "L_total = L_BCE + lambda * sum(||w_i||^2)", 16, MID_GRAY, name="Consolas")

# ============================================================
# SLIDE 9: CONCLUSIONES
# ============================================================
s = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(s)

add_text(s, 1.5, 0.6, 10.3, 0.7, "Conclusiones", 40, BLACK, bold=True)
add_line(s, 1.5, 1.3, 2.0)

add_body(s, 1.5, 1.7, 10.3, 5.5, [
    "1.  Diagnostico: el modelo memorizaba el dataset de entrenamiento.",
    "     Train ~100%, Test ~65-75%. Overfitting violento.",
    "",
    "2.  Interruptor: activamos Weight Decay (L2=0.01), Dropout (p=0.3)",
    "     y redujimos la red de ~19K a ~300 parametros.",
    "",
    "3.  Resultado: la brecha train-test se redujo de ~30% a <7%.",
    "     El modelo ahora generaliza en vez de memorizar.",
    "",
    "4.  Leccion: en medicina, un modelo con overfitting puede dar",
    "     diagnosticos falsos. La regularizacion no es opcional.",
], size=18, color=DARK_GRAY)

add_text(s, 1.5, 6.5, 10.3, 0.4,
         "Grupo 7  |  La Memoria de Pez  |  Bloque 3: Problemas de Estrategia",
         13, LIGHT_GRAY, align=PP_ALIGN.LEFT)

# ============================================================
prs.save('/home/user/proyecto/Grupo7_La_Memoria_de_Pez.pptx')
print("PPTX minimalista creado.")
