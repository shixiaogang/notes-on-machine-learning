"""第9章：重加权前后候选排序变化（100封源邮件的教学计数）。

源样本：a 90封（标签1有9封），b 10封（标签1有9封）。权重 w(a)=0.1/0.9=1/9, w(b)=0.9/0.1=9。
g0 的错误是标签1邮件，g1 的错误是标签0邮件。每段高度 = 该类错误数 × 权重 / 100。
"""
from pathlib import Path
import sys, json
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0, str(ROOT/'figures/06-foundations/00-shared/academic-drawing'))
from plot_style import *
import matplotlib.pyplot as plt
configure()
import matplotlib as mpl
mpl.rcParams['pdf.fonttype'] = 3  # Type 3 outlines; fonttype 42 garbles CJK in the book and in gs
OUT = Path(__file__).resolve().parent
counts = {('a', 0): 81, ('a', 1): 9, ('b', 0): 1, ('b', 1): 9}
w = {'a': 1/9, 'b': 9.0}
err_label = {'$g_0$': 1, '$g_1$': 0}
data = {}
for weighted in [False, True]:
    for g, lab in err_label.items():
        data[(weighted, g)] = {x: counts[(x, lab)]*(w[x] if weighted else 1)/100 for x in 'ab'}
MM = 1/25.4
fig, axs = plt.subplots(1, 2, figsize=(104*MM, 52*MM), sharey=True)
for ax, weighted, title in [(axs[0], False, '未加权源经验风险'), (axs[1], True, '加权经验风险 $\\widehat R_w$')]:
    for i, g in enumerate(err_label):
        va, vb = data[(weighted, g)]['a'], data[(weighted, g)]['b']
        ax.bar(i, va, width=.55, color=BLUE_FILL, edgecolor=BLUE, linewidth=.8, label='来自 $a$' if i == 0 else None)
        ax.bar(i, vb, bottom=va, width=.55, color=RED_FILL, edgecolor=RED, linewidth=.8, label='来自 $b$' if i == 0 else None)
        ax.text(i, va+vb+.02, f'{va+vb:.2f}', ha='center', va='bottom', fontsize=7.5)
    ax.set_xticks([0, 1], list(err_label)); ax.set_xlim(-.6, 1.6)
    ax.set_title(title, fontsize=8)
axs[0].set_ylim(0, 1); axs[0].set_yticks([0, .5, 1])
axs[0].legend(loc='upper left', fontsize=7.5, frameon=False)
fig.subplots_adjust(left=.1, right=.98, bottom=.14, top=.86, wspace=.15)
prepare_figure(fig)
fig.savefig(OUT/'figure.pdf'); fig.savefig(OUT/'figure.png', dpi=300)
json.dump({'method': 'matplotlib', 'figure': 'lt9-reweighting-ranking',
  'source': 'teaching counts in chapter 9: a 90 (9 positive), b 10 (9 positive); w(a)=1/9, w(b)=9',
  'values': {f'{"weighted" if k[0] else "unweighted"} {k[1]}': v for k, v in data.items()},
  'size_mm': [104, 52], 'style': style_record(), 'date': '2026-10-30'},
  open(OUT/'generation.json', 'w'), ensure_ascii=False, indent=2)
