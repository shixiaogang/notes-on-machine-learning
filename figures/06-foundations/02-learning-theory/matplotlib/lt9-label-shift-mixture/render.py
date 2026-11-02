"""第9章：标签偏移下目标输入分布是类条件分布的混合。

P_T^X(b) = K_0(b) + [K_1(b) - K_0(b)] q_1，三组类内比例：(K_0(b),K_1(b)) = (0.2,0.8)、(0.45,0.55)、(0.5,0.5)。
观测带 P_T^X(b) in [0.47, 0.53]（例如频率估计误差 0.03），反解出的 q_1 区间分别为
[0.45,0.55]、[0.2,0.8]、[0,1]（后者不可识别）。
"""
from pathlib import Path
import sys, json
import numpy as np
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0, str(ROOT/'figures/06-foundations/00-shared/academic-drawing'))
from plot_style import *
import matplotlib.pyplot as plt
configure()
import matplotlib as mpl
mpl.rcParams['pdf.fonttype'] = 3  # Type 3 outlines; fonttype 42 garbles CJK in the book and in gs
OUT = Path(__file__).resolve().parent
q = np.linspace(0, 1, 201)
cases = [((.2, .8), BLUE, '-'), ((.45, .55), GREEN, '--'), ((.5, .5), RED, ':')]
lo, hi = .47, .53
MM = 1/25.4
fig, (ax, bx) = plt.subplots(2, 1, figsize=(104*MM, 64*MM), sharex=True, gridspec_kw={'height_ratios': [4, 1.1], 'hspace': .12})
ax.axhspan(lo, hi, color=YELLOW_FILL, zorder=0)
intervals = {}
for k, ((k0, k1), color, ls) in enumerate(cases):
    ax.plot(q, k0+(k1-k0)*q, color=color, ls=ls, lw=1.1,
            label=f'$K_0(b)={k0:g},\\ K_1(b)={k1:g}$')
    if k1 != k0:
        a, b = sorted([(lo-k0)/(k1-k0), (hi-k0)/(k1-k0)]); a, b = max(a, 0), min(b, 1)
    else:
        a, b = 0, 1
    intervals[f'{k0},{k1}'] = [round(a, 3), round(b, 3)]
    bx.plot([a, b], [2-k, 2-k], color=color, lw=2.2, solid_capstyle='butt')
bx.set_ylim(-.6, 2.6); bx.set_yticks([]); bx.spines['left'].set_visible(False)
note(bx.text(1.02, 1, '反解出的\n$q_1$ 范围', fontsize=7.5, va='center', clip_on=False))
note(ax.text(.02, hi+.015, '观测到的 $\mathscr{P}_T^X(b)$ 范围', fontsize=7.5))
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1])
bx.set_xlabel('目标诈骗比例 $q_1$'); ax.set_ylabel('$\mathscr{P}_T^X(b)$')
ax.legend(loc='upper left', fontsize=7.5)
fig.subplots_adjust(left=.12, right=.8, bottom=.17, top=.97)
prepare_figure(fig)
fig.savefig(OUT/'figure.pdf'); fig.savefig(OUT/'figure.png', dpi=300)
json.dump({'method': 'matplotlib', 'figure': 'lt9-label-shift-mixture',
  'source': 'analytic: P_T^X(b)=K_0(b)+(K_1(b)-K_0(b))q_1; observed band [0.47,0.53]',
  'intervals_q1': intervals, 'size_mm': [104, 58], 'style': style_record(), 'date': '2026-10-30'},
  open(OUT/'generation.json', 'w'), ensure_ascii=False, indent=2)
