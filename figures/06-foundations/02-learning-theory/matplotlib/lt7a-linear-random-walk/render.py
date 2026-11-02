"""线性类中随机符号和的随机游走长度。"""
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
rng = np.random.default_rng(2026)
nmax = 400
ang = rng.uniform(0, 2 * np.pi, nmax)
X = np.c_[np.cos(ang), np.sin(ang)]  # 固定的单位输入 x_i
fig, axes = plt.subplots(1, 2, figsize=(150 * MM, 60 * MM), gridspec_kw={'width_ratios': [1, 1.15]})
ax = axes[0]
cols = [BLUE, YELLOW, GREEN]
for k in range(3):
    sig = rng.choice([-1, 1], nmax)
    P = np.vstack([[0, 0], np.cumsum(sig[:, None] * X, 0)])
    ax.plot(P[:, 0], P[:, 1], color=cols[k], lw=.6)
    ax.plot(P[-1, 0], P[-1, 1], 'o', color=cols[k], ms=3)
t = np.linspace(0, 2 * np.pi, 200)
ax.plot(np.sqrt(nmax) * np.cos(t), np.sqrt(nmax) * np.sin(t), color=MUTED, lw=.6, ls='--')
ax.text(0, np.sqrt(nmax) + 2.5, r'$\sqrt{n}=20$', ha='center', color=MUTED)
ax.set_aspect('equal'); ax.set_xlim(-34, 34); ax.set_ylim(-34, 34)
ax.set_xlabel('第一坐标'); ax.set_ylabel('第二坐标')
ax = axes[1]
ns = np.array([1, 2, 5, 10, 20, 50, 100, 200, 400])
reps = 4000
mean_len = []
for n in ns:
    sig = rng.choice([-1, 1], (reps, n))
    mean_len.append(float(np.sqrt(((sig[:, :, None] * X[None, :n, :]).sum(1) ** 2).sum(1)).mean()))
ax.plot(ns, ns, color=RED, lw=1.1, label=r'$\sum_i\|x_i\|=n$')
ax.plot(ns, np.sqrt(ns), color=MUTED, lw=.9, ls='--', label=r'$\sqrt{\sum_i\|x_i\|^2}=\sqrt{n}$')
ax.plot(ns, mean_len, 'o', color=BLUE, ms=3, label=r'$E\,\|\sum_i\sigma_i x_i\|$')
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlabel('样本量 n'); ax.set_ylabel('长度')
ax.legend(loc='upper left'); ax.grid(color=GRID, lw=.4)
fig.tight_layout(w_pad=2)
save(fig, {'seed': 2026, 'n_paths': 400, 'inputs': 'unit vectors at uniform random angles', 'ns': ns.tolist(),
           'mean_length_mc': [round(v, 3) for v in mean_len], 'reps': reps},
     {'label': 'fig:lt7a-linear-random-walk', 'source': 'Monte Carlo with numpy default_rng(2026); unit inputs, Rademacher signs'})
