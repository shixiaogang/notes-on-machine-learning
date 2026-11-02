"""收缩引理的Lipschitz几何：坡道间隔损失与坐标逐一收缩。"""
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
rho = 1.0
def ramp(u):  # 间隔损失 ell_rho(u)，u 为带符号间隔 y f(x)
    return np.clip(1 - u / rho, 0, 1)
fig, axes = plt.subplots(1, 2, figsize=(150 * MM, 56 * MM))
ax = axes[0]
u = np.linspace(-1.5, 2.5, 801)
ax.plot(u, (u <= 0).astype(float), color=RED, lw=1.1, label='零一损失', drawstyle='steps-post')
ax.plot(u, ramp(u), color=BLUE, lw=1.1, label='间隔损失')
pairs = [(0.2, 0.7), (1.3, 2.0)]
for a, b in pairs:
    ax.plot([a, b], [ramp(a), ramp(b)], 'o', color=YELLOW, ms=3.2)
    ax.annotate('', xy=(b, -0.08), xytext=(a, -0.08), arrowprops=dict(arrowstyle='<->', color=MUTED, lw=.6))
ax.text(0.45, ramp(0.45) + .12, '斜率至多 1/ρ', color=INK, fontsize=7.5)
ax.text(1.65, .1, '差为 0', color=INK, fontsize=7.5, ha='center')
ax.set_xlabel('带符号间隔 yf(x)'); ax.set_ylabel('损失'); ax.set_ylim(-.2, 1.25)
ax.legend(loc='upper right'); ax.axvline(rho, color=GRID, lw=.6); ax.text(rho, 1.17, 'ρ', ha='center', color=MUTED)
ax = axes[1]
# 两个样本点上的得分向量 (u1,u2)：取半径 1 的圆上 12 个点（教学构造）
th = np.linspace(0, 2 * np.pi, 13)[:-1]
U = np.c_[0.5 + 1.0 * np.cos(th), 0.5 + 1.0 * np.sin(th)]
V = ramp(U)
ax.fill(U[:, 0], U[:, 1], color=BLUEF, ec=BLUE, lw=.8, label='得分向量')
ax.fill(V[:, 0], V[:, 1], color=YELLOWF, ec=YELLOW, lw=.8, alpha=1, label='逐坐标作用损失后')
for p, q in zip(U, V):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=GRID, lw=.5, zorder=0)
ax.set_aspect('equal'); ax.set_xlabel('样本 1 上的值'); ax.set_ylabel('样本 2 上的值')
ax.legend(loc='upper left', fontsize=7); ax.set_xlim(-.8, 2.0); ax.set_ylim(-.8, 2.0)
fig.tight_layout(w_pad=2.5)
save(fig, {'rho': rho, 'pairs': pairs, 'score_points': U.round(4).tolist(), 'loss_points': V.round(4).tolist()},
     {'label': 'fig:lt7a-contraction-geometry', 'source': 'analytic ramp loss ell(u)=clip(1-u/rho,0,1); score points on circle centre (0.5,0.5) radius 1'})
