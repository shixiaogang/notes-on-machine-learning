"""高斯与Rademacher复杂度的对照：函数值向量为 {±e_i} 的类。"""
# ---- 共同样式（各图目录各存一份，便于独立复现） ----
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from matplotlib import font_manager
HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'build.sh').exists())
for f in ['SourceHanSansSC-Normal.otf', 'LXGWWenKai-Regular.ttf', 'FiraMath-Regular.otf', 'STIXTwoMath-Regular.otf']:
    font_manager.fontManager.addfont(str(ROOT / 'fonts' / f))
# 只使用项目 fonts/ 中的字体文件，排除系统中同名字体。
font_manager.fontManager.ttflist = [e for e in font_manager.fontManager.ttflist
    if not (e.name in ('Source Han Sans SC', 'Fira Math', 'LXGW WenKai') and not e.fname.startswith(str(ROOT / 'fonts')))]
plt.rcParams.update({
    'font.family': ['Fira Math', 'Source Han Sans SC'],
    'mathtext.fontset': 'custom', 'mathtext.rm': 'Fira Math', 'mathtext.it': 'Fira Math',
    'mathtext.bf': 'Fira Math', 'mathtext.fallback': 'stix',
    'font.size': 8, 'axes.labelsize': 8, 'xtick.labelsize': 7.5, 'ytick.labelsize': 7.5,
    'legend.fontsize': 7.5, 'axes.linewidth': .75, 'xtick.major.width': .6, 'ytick.major.width': .6,
    'axes.edgecolor': '#4C4D4F', 'axes.labelcolor': '#3B4252', 'xtick.color': '#3B4252', 'ytick.color': '#3B4252',
    'text.color': '#3B4252', 'axes.spines.top': False, 'axes.spines.right': False,
    'pdf.fonttype': 3, 'legend.frameon': False,
})
BLUE, BLUEF = '#7188A3', '#E5EAF0'
GREEN, GREENF = '#829C8B', '#E8EEE9'
YELLOW, YELLOWF = '#B4A16F', '#F1ECDD'
RED, REDF = '#A7787D', '#F0E5E6'
PURPLE, PURPLEF = '#9588A5', '#ECE8F0'
INK, MUTED, LINE, GRID = '#3B4252', '#6B7280', '#4C4D4F', '#D8DCE2'
MM = 1 / 25.4
def save(fig, data, generation):
    fig.savefig(HERE / 'figure.pdf')
    (HERE / 'data.json').write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')
    generation.update({'method': 'matplotlib', 'script': str((HERE / 'render.py').relative_to(ROOT)),
                       'data': str((HERE / 'data.json').relative_to(ROOT)), 'date': '2026-10-30',
                       'fonts': 'fonts/SourceHanSansSC-Normal.otf, fonts/FiraMath-Regular.otf (STIX fallback)',
                       'size_mm': [round(fig.get_size_inches()[0] / MM, 1), round(fig.get_size_inches()[1] / MM, 1)]})
    (HERE / 'generation.json').write_text(json.dumps(generation, ensure_ascii=False, indent=1) + '\n')
# ---- 样式结束 ----
from math import erf, sqrt, pi, log
# 函数类在固定样本上的取值向量为 {±e_1,...,±e_n}。
# n*R_hat = E max_i |sigma_i| = 1；n*G_hat = E max_i |xi_i|，用数值积分计算：
# E max|xi| = ∫_0^∞ [1 - (2Φ(t)-1)^n] dt。
t = np.linspace(0, 12, 120001); dt = t[1] - t[0]
Phi2 = np.array([erf(v / sqrt(2)) for v in t])
ns = np.array([1, 2, 3, 5, 10, 20, 50, 100, 200, 500, 1000])
emax = np.array([float(np.sum(1 - Phi2 ** n) * dt) for n in ns])
fig, axes = plt.subplots(1, 2, figsize=(150 * MM, 52 * MM), gridspec_kw={'width_ratios': [1.15, 1]})
ax = axes[0]
rng = np.random.default_rng(7)
n0 = 10
sig = rng.choice([-1, 1], n0); xi = rng.standard_normal(n0)
x = np.arange(1, n0 + 1)
ax.bar(x - .18, np.abs(sig), width=.34, color=BLUEF, edgecolor=BLUE, lw=.6, label=r'$|\sigma_i|$')
ax.bar(x + .18, np.abs(xi), width=.34, color=YELLOWF, edgecolor=YELLOW, lw=.6, label=r'$|\xi_i|$')
ax.axhline(1, color=BLUE, lw=.8, ls='--'); ax.axhline(np.abs(xi).max(), color=YELLOW, lw=.8, ls='--')
ax.set_xticks(x); ax.set_xlabel('样本位置 i'); ax.set_ylabel('幅度')
ax.legend(loc='upper left', ncol=2); ax.set_ylim(0, max(2.6, np.abs(xi).max() + .5))
ax.text(n0 + .6, np.abs(xi).max(), r'$\mathrm{max}_i|\xi_i|$', color=INK, va='center', fontsize=7.5)
ax.set_xlim(.4, n0 + 2.4)
ax = axes[1]
ax.plot(ns, np.ones_like(ns, float), color=BLUE, lw=1.1, marker='o', ms=2.5, label=r'Rademacher: $n\hat{R}_S=1$')
ax.plot(ns, emax, color=YELLOW, lw=1.1, marker='o', ms=2.5, label=r'Gaussian: $n\hat{G}_S=E\,\mathrm{max}_i|\xi_i|$')
ax.plot(ns, np.sqrt(2 * np.log(2 * ns)), color=MUTED, lw=.6, ls=':', label=r'$\sqrt{2\log(2n)}$')
ax.set_xscale('log'); ax.set_xlabel('样本量 n'); ax.set_ylabel('复杂度乘以样本量')
ax.legend(loc='upper left'); ax.set_ylim(0, 4.6); ax.grid(color=GRID, lw=.4)
fig.tight_layout(w_pad=2)
save(fig, {'class': 'values {±e_i}', 'n': ns.tolist(), 'n_times_rademacher': [1.0] * len(ns),
           'n_times_gaussian': [round(v, 4) for v in emax], 'left_panel_seed': 7, 'left_n': n0,
           'left_sigma': sig.tolist(), 'left_xi': [round(v, 4) for v in xi]},
     {'label': 'fig:lt7a-gaussian-rademacher', 'source': 'analytic: E max|sigma_i|=1; E max|xi_i| by numerical integration of 1-(2Phi(t)-1)^n'})
