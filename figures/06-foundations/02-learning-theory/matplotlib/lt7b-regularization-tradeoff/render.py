"""Upper bound of strongly convex regularisation as a function of lambda.

U_n(lambda) = 2 L^2 / (lambda n) + lambda B^2 / 2, with L = B = 1,
n in {100, 1000, 10000}. Minimiser lambda* = 2L/(B sqrt n), value 2LB/sqrt n.
For n = 1000 the two components are also drawn.
"""
from pathlib import Path
import json, sys
import numpy as np
import matplotlib.pyplot as plt

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').exists())
D_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'figures/06-foundations/00-shared/academic-drawing'))
from plot_style import configure, prepare_figure, note, style_record, BLUE, GREEN, RED, PURPLE, MUTED

configure()
L = B = 1.0
lam = np.logspace(-3, 0.3, 400)
fig, ax = plt.subplots(figsize=(107 / 25.4, 60 / 25.4), layout='constrained')
rec = {}
for n, c in zip([100, 1000, 10000], [RED, BLUE, GREEN]):
    U = 2 * L ** 2 / (lam * n) + lam * B ** 2 / 2
    ax.loglog(lam, U, color=c, label=r'$n=%d$' % n)
    ls = 2 * L / (B * np.sqrt(n))
    ax.plot([ls], [2 * L * B / np.sqrt(n)], marker='o', ms=3, color=c)
    rec[n] = {'lambda_star': ls, 'bound_at_star': 2 * L * B / np.sqrt(n)}
n = 1000
ax.loglog(lam, 2 * L ** 2 / (lam * n), color=MUTED, lw=0.6, ls='--')
ax.loglog(lam, lam * B ** 2 / 2, color=MUTED, lw=0.6, ls=':')
note(ax.text(1.2e-3, 0.0105, r'虚线：$2L^2/(\lambda n)$，$n=1000$', fontsize=7, color=MUTED))
note(ax.text(1.2e-3, 0.0065, r'点线：$\lambda B^2/2$', fontsize=7, color=MUTED))
ax.set(xlabel=r'正则强度 $\lambda$', ylabel='超额风险上界', ylim=(5e-3, 3))
ax.legend(loc='upper center', bbox_to_anchor=(0.62, 1.0), fontsize=7.5)
prepare_figure(fig)
for ext in ['pdf', 'png']:
    fig.savefig(D_DIR / ('figure.' + ext), dpi=300)
plt.close(fig)
(D_DIR / 'data.json').write_text(json.dumps({'L': L, 'B': B, 'optima': rec}, indent=2) + '\n')
gen = {'method': 'Matplotlib', 'date': '2026-10-30', 'source': 'analytic bound 2L^2/(lambda n)+lambda B^2/2',
       'parameters': {'L': L, 'B': B, 'n': [100, 1000, 10000]}, 'physical_size_mm': [107, 60], 'style': style_record()}
(D_DIR / 'generation.json').write_text(json.dumps(gen, ensure_ascii=False, indent=2) + '\n')
print(rec)
