"""PAC–Bayes中先验与后验的KL代价与经验风险的权衡。"""
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
from math import log, sqrt
tau, n, delta, d = 1.0, 1000, 0.05, 20
th = 2.0  # 中心到先验均值的距离 ||theta_hat||_2
def emp(s):   # d 维后验 N(theta_hat, s^2 I) 下的经验风险：教学构造 0.05 + 0.05*||theta-theta_hat||^2 的后验平均 = 0.05 + 0.05*d*s^2（截到 1）
    return np.minimum(0.05 + 0.05 * d * s ** 2, 1.0)
def kl(s):    # KL(N(theta_hat, s^2 I_d) || N(0, tau^2 I_d))
    return d * (np.log(tau / s) + s ** 2 / (2 * tau ** 2) - 0.5) + th ** 2 / (2 * tau ** 2)
def comp(s):
    return np.sqrt((kl(s) + log((n + 1) / delta)) / (2 * n))
fig, axes = plt.subplots(1, 2, figsize=(150 * MM, 56 * MM), gridspec_kw={'width_ratios': [1, 1.15]})
ax = axes[0]
x = np.linspace(-3, 4, 1401)
pdf = lambda m, s: np.exp(-(x - m) ** 2 / (2 * s * s)) / (s * np.sqrt(2 * np.pi))
ax.fill_between(x, pdf(0, tau), color=BLUEF, lw=0); ax.plot(x, pdf(0, tau), color=BLUE, lw=1.1, label='先验 P')
for s, c in [(0.6, GREEN), (0.15, YELLOW), (0.05, RED)]:
    ax.plot(x, np.minimum(pdf(th, s), 3.0), color=c, lw=1.0, label=f'后验 σ={s}')
ax.set_ylim(0, 3.1); ax.set_xlabel('沿中心方向的一个坐标'); ax.set_ylabel('密度'); ax.legend(loc='upper left', fontsize=7)
ax = axes[1]
ss = np.logspace(np.log10(0.01), np.log10(1.0), 400)
tot = emp(ss) + comp(ss); k = int(np.argmin(tot))
ax.plot(ss, emp(ss), color=BLUE, lw=1.1, label='后验经验风险')
ax.plot(ss, comp(ss), color=RED, lw=1.1, label='KL 代价项')
ax.plot(ss, tot, color=INK, lw=1.1, label='风险上界')
ax.plot(ss[k], tot[k], 'o', color=INK, ms=3.5)
ax.annotate(f'σ≈{ss[k]:.2f}，上界≈{tot[k]:.3f}', (ss[k], tot[k]), xytext=(0.011, tot[k] + .2), fontsize=7.5,
            arrowprops=dict(arrowstyle='-', color=MUTED, lw=.6))
ax.set_xscale('log'); ax.set_xlabel('后验宽度 σ'); ax.set_ylabel('数值'); ax.set_ylim(0, 0.75)
ax.legend(loc='upper center'); ax.grid(color=GRID, lw=.4)
fig.tight_layout(w_pad=2)
table = {str(s): {'emp': round(float(emp(np.array(s))), 4), 'kl': round(float(kl(np.array(s))), 4),
                  'comp': round(float(comp(np.array(s))), 4)} for s in [0.01, 0.05, 0.1, 0.15, 0.2, 0.3, 0.6]}
save(fig, {'tau': tau, 'theta_hat': th, 'n': n, 'delta': delta, 'd': d, 'emp': '0.05+0.05*d*sigma^2', 'argmin_sigma': round(float(ss[k]), 4),
           'min_bound': round(float(tot[k]), 4), 'table': table},
     {'label': 'fig:lt7a-pac-bayes-tradeoff', 'source': 'analytic Gaussian KL; d=20 isotropic Gaussians, prior N(0,I), ||theta_hat||=2; teaching empirical-risk curve 0.05+0.05 d sigma^2; square-root PAC-Bayes form with log((n+1)/delta)'})
