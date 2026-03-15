"""Render LaTeX formulas to PNG with matplotlib, then base64-encode for HTML embedding."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
import os

OUT = '/home/user/proyecto/slides_html/img'
os.makedirs(OUT, exist_ok=True)

formulas = [
    ('f1', r'\theta_{t+1} = \theta_t - \eta \, \nabla L(\theta_t)', 26, 8, 0.8),
    ('f2', r'\theta_{t+1} = (1 - \eta\lambda)\,\theta_t \;-\; \eta \, \nabla L(\theta_t)', 26, 10, 0.8),
    ('f2_label', r'\uparrow\; \mathrm{factor\;de\;encogimiento}', 18, 5, 0.5),
    ('f3a', r'h_i = 0 \quad \mathrm{con\;probabilidad}\;\; p', 24, 8, 0.7),
    ('f3b', r'h_i = \frac{x_i}{1-p} \quad \mathrm{con\;probabilidad}\;\; 1-p', 24, 9, 0.8),
    ('f4', r'L_{\mathrm{total}} = L_{\mathrm{BCE}}(\hat{y}, y) \;+\; \lambda \sum_i \|w_i\|^2', 26, 10, 0.8),
    ('f4_label1', r'\mathrm{perdida\;original}', 16, 4, 0.4),
    ('f4_label2', r'\mathrm{penalizacion\;L2}', 16, 4, 0.4),
]

for name, latex, fs, fw, fh in formulas:
    fig, ax = plt.subplots(figsize=(fw, fh))
    ax.text(0.5, 0.5, f'${latex}$', fontsize=fs, ha='center', va='center',
            color='#222', family='serif')
    ax.axis('off')
    fig.patch.set_alpha(0)
    path = os.path.join(OUT, f'{name}.png')
    fig.savefig(path, dpi=200, transparent=True, bbox_inches='tight', pad_inches=0.1)
    plt.close()
    print(f'  {name}.png OK')

print('\nAll formulas rendered.')
