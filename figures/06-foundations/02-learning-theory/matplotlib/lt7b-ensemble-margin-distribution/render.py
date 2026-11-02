"""Normalised voting margins of the AdaBoost run in lt7b-adaboost-weights-training.

Same 10-point sample and exact weighted threshold stumps. For each T the
normalised score is f_T = sum_t a_t h_t with a_t = alpha_t / sum_s alpha_s,
margin_i = y_i f_T(x_i) in [-1, 1]. Plotted: empirical CDF of the 10 margins
for T in {1, 5, 10, 30, 200}.
"""
from pathlib import Path
import json, sys
import numpy as np
import matplotlib.pyplot as plt

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').exists())
D_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'figures/06-foundations/00-shared/academic-drawing'))
from plot_style import configure, prepare_figure, note, style_record, BLUE, GREEN, YELLOW, RED, PURPLE, MUTED, GRID

configure()
x = np.arange(1, 11).astype(float)
y = np.array([1, 1, 1, -1, 1, 1, -1, -1, 1, -1])
n = len(x)
thr = np.concatenate([[0.5], x + 0.5])


def stump(D):
    best = None
    for t in thr:
        for s in [1, -1]:
            h = np.where(x > t, s, -s)
            e = D[h != y].sum()
            if best is None or e < best[0] - 1e-12:
                best = (e, t, s, h)
    return best


SHOW = [1, 5, 10, 30, 200]
D = np.ones(n) / n
F = np.zeros(n)
A = 0.0
margins = {}
for T in range(1, max(SHOW) + 1):
    e, t, s, h = stump(D)
    a = 0.5 * np.log((1 - e) / e)
    F += a * h
    A += a
    D = D * np.exp(-a * y * h)
    D /= D.sum()
    if T in SHOW:
        margins[T] = (y * F / A)

fig, ax = plt.subplots(figsize=(107 / 25.4, 60 / 25.4), layout='constrained')
cols = [MUTED, BLUE, GREEN, PURPLE, RED]
styles = [':', '--', '-.', '-', '-']
for T, c, ls in zip(SHOW, cols, styles):
    m = np.sort(margins[T])
    xs = np.concatenate([[-1.05], m, [1.05]])
    ys = np.concatenate([[0.0], np.arange(1, n + 1) / n, [1.0]])
    ax.step(xs, ys, where='post', color=c, ls=ls, lw=1.1, label=r'$T=%d$，最小间隔 %.3f' % (T, m[0]))
ax.axvline(0, color=GRID, lw=0.6)
note(ax.text(-0.05, 0.93, '分错', ha='right', fontsize=7, color=MUTED))
note(ax.text(0.05, 0.93, '分对', ha='left', fontsize=7, color=MUTED))
ax.set(xlabel=r'归一化间隔 $y_i f_T(x_i)$', ylabel=r'间隔 $\leq$ 横坐标的样本比例', xlim=(-1.05, 1.05), ylim=(0, 1.02))
ax.legend(loc='upper left', bbox_to_anchor=(0.0, 0.88), fontsize=7)
prepare_figure(fig)
for ext in ['pdf', 'png']:
    fig.savefig(D_DIR / ('figure.' + ext), dpi=300)
plt.close(fig)

data = {T: np.round(np.sort(margins[T]), 4).tolist() for T in SHOW}
(D_DIR / 'data.json').write_text(json.dumps({'sorted_margins': data}, ensure_ascii=False, indent=2) + '\n')
gen = {'method': 'Matplotlib', 'date': '2026-10-30', 'source': 'exact AdaBoost run, same sample as lt7b-adaboost-weights-training',
       'parameters': {'rounds_shown': SHOW}, 'physical_size_mm': [107, 60], 'style': style_record()}
(D_DIR / 'generation.json').write_text(json.dumps(gen, ensure_ascii=False, indent=2) + '\n')
for T in SHOW:
    print(T, np.round(np.sort(margins[T]), 3))
