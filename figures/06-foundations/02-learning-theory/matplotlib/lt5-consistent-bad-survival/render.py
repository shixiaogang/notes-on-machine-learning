"""Probability that bad hypotheses survive a consistent-sample check.

Teaching setting (chapter 5, section 5.1.1): four candidate thresholds; a bad
rule is one with population error at least eps=0.1. Which candidates are bad is
unknown, so the union bound pays for all four. Curves are exact analytic
expressions, no sampling:
  single fixed rule with error 0.1   0.9**n
  union over four candidates         4 * 0.9**n      (union bound, capped at 1)
  theorem bound |H| e^{-n eps}       4 * exp(-0.1 n) (capped at 1)
Reference line delta = 0.01.
"""
from pathlib import Path
import sys, json, math
import numpy as np
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0, str(ROOT/'figures/06-foundations/00-shared/academic-drawing'))
from plot_style import *  # noqa: F401,F403  exact fonts and palette
import matplotlib.pyplot as plt
configure()
OUT = Path(__file__).resolve().parent
MM = 1/25.4
n = np.arange(0, 71)
single = 0.9**n
union = np.minimum(1, 4*0.9**n)
theorem = np.minimum(1, 4*np.exp(-0.1*n))
delta = 0.01
first = {name: int(next(k for k in n if v[k] <= delta)) for name, v in
         [('single', single), ('union', union), ('theorem', theorem)]}
fig, ax = plt.subplots(figsize=(107*MM, 62*MM))
ax.plot(n, single, color=BLUE, label=r'单个固定规则 $0.9^n$')
ax.plot(n, union, color=GREEN, ls='--', label=r'四个候选的并集界 $4\times0.9^n$')
ax.plot(n, theorem, color=RED, ls=':', label=r'定理上界 $4e^{-0.1n}$')
ax.axhline(delta, color=MUTED, lw=.6)
note(ax.text(70, delta*1.25, r'$\delta=0.01$', ha='right', va='bottom', color=MUTED))
for name, color, ha, dx in [('single', BLUE, 'center', 0), ('union', GREEN, 'right', -0.6), ('theorem', RED, 'left', 0.6)]:
    k = first[name]
    ax.plot([k], [delta], 'o', ms=3.2, color=color, zorder=5)
    ax.text(k+dx, delta/1.6, str(k), ha=ha, va='top', color=color, fontsize=7.5)
ax.plot([10], [0.9**10], 'o', ms=3.2, color=BLUE, zorder=5)
note(ax.text(2, 0.065, r'$n=10$：$0.9^{10}\approx0.349$', ha='left', va='top'))
ax.set_yscale('log')
ax.set(xlim=(0, 70), ylim=(2e-4, 1.3), xlabel='训练样本数 $n$', ylabel='坏规则通过全部检验的概率')
ax.grid(axis='y', which='major')
ax.legend(loc='lower left', fontsize=7.5)
fig.tight_layout()
prepare_figure(fig)
fig.savefig(OUT/'figure.pdf')
fig.savefig(OUT/'figure.png', dpi=200)
(OUT/'data.json').write_text(json.dumps({'n': n.tolist(), 'single': single.tolist(),
    'union': union.tolist(), 'theorem': theorem.tolist(), 'delta': delta,
    'first_n_below_delta': first}, ensure_ascii=False, indent=1)+'\n')
print(first)
