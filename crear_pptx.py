"""
Genera el PPTX del Grupo 7 renderizando cada slide desde HTML a PNG
usando Playwright + Chromium, luego las inserta como imagenes full-slide.
"""
import subprocess
import os
from pptx import Presentation
from pptx.util import Inches

SLIDES_DIR = '/home/user/proyecto/slides_html'
IMG_DIR = '/tmp/pptx_slides'
os.makedirs(IMG_DIR, exist_ok=True)

# Orden de slides
slides = [
    'slide_portada',
    'slide_problema',
    'slide_diagnostico',
    'slide_correccion',
    'slide_tabla',
    'slide_representation',
    'slide_negocio',
    'slide_bonus1',
    'slide_bonus2',
    'slide_conclusiones',
]

# 1. Render each HTML to PNG via Playwright
print("Renderizando slides HTML a PNG...")
for name in slides:
    html_path = os.path.join(SLIDES_DIR, f'{name}.html')
    png_path = os.path.join(IMG_DIR, f'{name}.png')

    cmd = [
        'npx', 'playwright', 'screenshot',
        '--viewport-size', '1920,1080',
    ]
    cmd += ['--wait-for-timeout', '2000']
    cmd += [f'file://{html_path}', png_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ERROR {name}: {result.stderr}")
    else:
        size = os.path.getsize(png_path)
        print(f"  {name}.png ({size // 1024} KB)")

# 2. Build PPTX from PNG images
print("\nCreando PPTX...")
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

for name in slides:
    png_path = os.path.join(IMG_DIR, f'{name}.png')
    if not os.path.exists(png_path):
        print(f"  SKIP {name} (no PNG)")
        continue

    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
    slide.shapes.add_picture(
        png_path,
        Inches(0), Inches(0),
        Inches(13.333), Inches(7.5)
    )
    print(f"  + {name}")

out_path = '/home/user/proyecto/Grupo7_La_Memoria_de_Pez.pptx'
prs.save(out_path)
print(f"\nPPTX guardado: {out_path}")
print(f"Total slides: {len(prs.slides)}")
