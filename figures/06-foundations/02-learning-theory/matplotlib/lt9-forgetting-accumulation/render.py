"""第9章：累计遗忘逐步相加。

左：每步风险增量上界 gamma_j，累计上界 sum_{j<=t} gamma_j。常数 gamma_j=0.01 线性增长；
    几何递减 gamma_j=0.01*0.9^{j-1} 的累计上界为 0.1(1-0.9^t) < 0.1。
右：估计误差部分。每步经验增量控制都付 2a（a=0.01），t 步后为 2at；
    直接约束最终历史经验风险只付一次 a。
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
t = np.arange(0, 61)
const = .01*t
geom = .1*(1-.9**t)
a = .01
MM = 1/25.4
fig, axs = plt.subplots(1, 2, figsize=(104*MM, 50*MM), sharey=True)
axs[0].step(t, const, where='post', color=RED, ls='--', label='$\\gamma_j=0.01$')
axs[0].step(t, geom, where='post', color=BLUE, label='$\\gamma_j=0.01\\times0.9^{j-1}$')
axs[0].axhline(.1, color=MUTED, lw=.6, ls=':')
axs[0].set_title('风险增量逐项相加', fontsize=8)
axs[1].step(t, 2*a*t, where='post', color=RED, ls='--', label='逐步各付 $2a$')
axs[1].plot(t, np.full_like(t, a, dtype=float), color=BLUE, label='直接约束：付一次 $a$')
axs[1].set_title('估计误差部分（$a=0.01$）', fontsize=8)
for ax in axs:
    ax.set_xlim(0, 60); ax.set_xticks([0, 30, 60]); ax.set_xlabel('更新步数 $t$')
    ax.legend(loc='upper left', fontsize=7)
axs[0].set_ylim(0, 1.25); axs[0].set_yticks([0, .6, 1.2])
note(axs[0].text(60, .13, '0.1', ha='right', fontsize=7)); axs[0].set_ylabel('累计上界')
fig.subplots_adjust(left=.11, right=.98, bottom=.22, top=.88, wspace=.12)
prepare_figure(fig)
fig.savefig(OUT/'figure.pdf'); fig.savefig(OUT/'figure.png', dpi=300)
json.dump({'method': 'matplotlib', 'figure': 'lt9-forgetting-accumulation',
  'source': 'analytic sums: 0.01 t; 0.1(1-0.9^t); 2at and a with a=0.01; t=0..60',
  'size_mm': [104, 50], 'style': style_record(), 'date': '2026-10-30'},
  open(OUT/'generation.json', 'w'), ensure_ascii=False, indent=2)
