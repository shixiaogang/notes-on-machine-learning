"""Sufficient sample sizes of the two finite-class theorems versus accuracy.

Analytic expressions from chapter 5 (no data, no sampling):
  realizable  n_real(eps) = ceil((log|H| + log(1/delta)) / eps)
  agnostic    n_agn(eps)  = ceil(2 (log(2|H|) + log(1/delta)) / eps**2)
with |H| = 4 thresholds and delta = 0.01; eps on a log grid in [0.01, 0.5].
Marked points: eps = 0.1 and eps = 0.05.
"""
from pathlib import Path
import sys, json, math
import numpy as np
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0, str(ROOT/'figures/06-foundations/00-shared/academic-drawing'))
from plot_style import *  # noqa: F401,F403
import matplotlib.pyplot as plt
configure()
OUT = Path(__file__).resolve().parent
MM = 1/25.4
H, delta = 4, 0.01
def real(e): return math.ceil((math.log(H)+math.log(1/delta))/e)
def agn(e): return math.ceil(2*(math.log(2*H)+math.log(1/delta))/e**2)
eps = np.geomspace(0.01, 0.5, 200)
r = (math.log(H)+math.log(1/delta))/eps
a = 2*(math.log(2*H)+math.log(1/delta))/eps**2
marks = {e: (real(e), agn(e)) for e in [0.1, 0.05]}
fig, ax = plt.subplots(figsize=(107*MM, 62*MM))
ax.plot(eps, r, color=BLUE, label=r'可实现：$(\log|\mathcal{H}|+\log(1/\delta))/\varepsilon$')
ax.plot(eps, a, color=RED, ls='--', label=r'不可知：$2(\log(2|\mathcal{H}|)+\log(1/\delta))/\varepsilon^2$')
for e, (nr, na) in marks.items():
    ax.plot([e], [nr], 'o', ms=3.2, color=BLUE, zorder=5)
    ax.plot([e], [na], 'o', ms=3.2, color=RED, zorder=5)
    ax.text(e*1.08, nr/1.5, f'{nr}', color=BLUE, fontsize=7.5, ha='left', va='top')
    ax.text(e/1.1, na/1.25, f'{na}', color=RED, fontsize=7.5, ha='left', va='top')
ax.set_xscale('log'); ax.set_yscale('log')
ax.set_xticks([0.01, 0.02, 0.05, 0.1, 0.2, 0.5], ['0.01', '0.02', '0.05', '0.1', '0.2', '0.5'])
ax.set(xlim=(0.01, 0.5), ylim=(8, 3e5), xlabel=r'容许误差 $\varepsilon$', ylabel='充分样本量 $n$')
ax.invert_xaxis()
ax.grid(axis='y', which='major')
ax.legend(loc='upper left', fontsize=7.5)
note(ax.text(0.0105, 12, r'$|\mathcal{H}|=4$，$\delta=0.01$', ha='right', va='bottom'))
fig.tight_layout()
prepare_figure(fig)
fig.savefig(OUT/'figure.pdf'); fig.savefig(OUT/'figure.png', dpi=200)
(OUT/'data.json').write_text(json.dumps({'H': H, 'delta': delta,
    'marks': {str(k): {'realizable': v[0], 'agnostic': v[1]} for k, v in marks.items()}}, indent=1)+'\n')
print(marks)
