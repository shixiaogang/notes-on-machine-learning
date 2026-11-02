"""第9章：两输入比例互换后候选风险排序改变（教学构造，解析计算）。

eta(a)=0.1, eta(b)=0.9；源域 P^X(a)=0.9, 目标域 P^X(a)=0.1。零一损失：
R(g0)=sum P^X(x) eta(x)，R(g1)=sum P^X(x)(1-eta(x))，R(h01)=sum P^X(x) min(eta,1-eta)。
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
eta = {'a': .1, 'b': .9}
px = {'源域（三月）': {'a': .9, 'b': .1}, '目标域（四月）': {'a': .1, 'b': .9}}
cands = {'$g_0$\n恒判 0': lambda e: e, '$g_1$\n恒判 1': lambda e: 1-e,
         '$h_{01}$\n$a\\to0,\\ b\\to1$': lambda e: min(e, 1-e)}
risks = {d: [round(sum(p[x]*f(eta[x]) for x in 'ab'), 4) for f in cands.values()] for d, p in px.items()}
MM = 1/25.4
fig, ax = plt.subplots(figsize=(104*MM, 50*MM))
xs = range(len(cands)); w = .34
for k, (d, color, fill, hatch) in enumerate([('源域（三月）', BLUE, BLUE, ''), ('目标域（四月）', RED, 'white', '')]):
    pos = [x + (k-.5)*w for x in xs]
    bars = ax.bar(pos, risks[d], width=w, color=fill, edgecolor=color, linewidth=.8,
                  linestyle='-' if k == 0 else '--', label=d)
    for p, v in zip(pos, risks[d]):
        ax.text(p, v+.02, f'{v:.2f}', ha='center', va='bottom', fontsize=7.5)
ax.set_xticks(list(xs), list(cands.keys()))
ax.set_ylim(0, 1); ax.set_yticks([0, .5, 1]); ax.set_ylabel('零一风险')
ax.legend(loc='upper left', fontsize=7.5, ncol=2, bbox_to_anchor=(0, 1.08))
fig.subplots_adjust(left=.12, right=.98, bottom=.24, top=.9)
prepare_figure(fig)
fig.savefig(OUT/'figure.pdf'); fig.savefig(OUT/'figure.png', dpi=300)
json.dump({'method': 'matplotlib', 'figure': 'lt9-proportion-swap-ranking',
  'source': 'analytic teaching construction in chapter 9 (eta(a)=0.1, eta(b)=0.9; P_S^X(a)=0.9, P_T^X(a)=0.1)',
  'values': risks, 'size_mm': [104, 50], 'style': style_record(), 'date': '2026-10-30'},
  open(OUT/'generation.json', 'w'), ensure_ascii=False, indent=2)
