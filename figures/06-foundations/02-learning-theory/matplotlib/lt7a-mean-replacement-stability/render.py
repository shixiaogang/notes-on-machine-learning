"""替换一个样本后两次均值输出的损失差。"""
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
S = np.array([0.1, 0.3, 0.4, 0.8, 0.9]); Sp = S.copy(); Sp[4] = 0.0
w, wp = S.mean(), Sp.mean()   # 0.5 与 0.32
z = np.linspace(0, 1, 501)
fig, axes = plt.subplots(1, 2, figsize=(150 * MM, 56 * MM))
for ax, kind in zip(axes, ['abs', 'sq']):
    f = (lambda a: np.abs(a - z)) if kind == 'abs' else (lambda a: (a - z) ** 2)
    L, Lp = f(w), f(wp)
    ax.fill_between(z, L, Lp, color=YELLOWF, lw=0)
    ax.plot(z, L, color=BLUE, lw=1.1, label=r'$A(S)=0.50$')
    ax.plot(z, Lp, color=RED, lw=1.1, label=r"$A(S')=0.32$")
    ax.plot(S, np.full(5, -0.04), 'o', color=BLUE, ms=3, clip_on=False)
    ax.plot([0.0], [-0.04], 'o', mfc='white', mec=RED, ms=3.5, clip_on=False)
    gap = np.abs(L - Lp).max()
    ax.set_xlabel('测试观测 z'); ax.set_ylim(-0.06, 0.8 if kind == 'abs' else 0.62)
    ax.set_title('绝对损失：最大差 0.18' if kind == 'abs' else '平方损失：最大差 0.21', fontsize=8, color=INK)
    ax.legend(loc='upper center', ncol=2)
axes[0].set_ylabel('损失')
fig.tight_layout(w_pad=2)
gaps = [float(np.abs(np.abs(w - z) - np.abs(wp - z)).max()), float(np.abs((w - z) ** 2 - (wp - z) ** 2).max())]
save(fig, {'S': S.tolist(), 'S_replaced': Sp.tolist(), 'mean': w, 'mean_replaced': wp,
           'max_gap_abs': round(gaps[0], 4), 'max_gap_sq': round(gaps[1], 4), 'bound_abs': 0.2, 'bound_sq': 0.4},
     {'label': 'fig:lt7a-mean-replacement-stability', 'source': 'analytic; sample (0.1,0.3,0.4,0.8,0.9), z5 replaced by 0'})
