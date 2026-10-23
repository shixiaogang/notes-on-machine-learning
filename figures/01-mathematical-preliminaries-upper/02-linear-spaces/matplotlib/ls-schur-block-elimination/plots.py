"""教学图：Schur 补的 2x2 分块消元过程。

解析式固定构造：M=[[2,1],[1,2]]，右端 (1,3)。
左上块 A=2 可逆；先用第一行把 x1=(1-x2)/2 表示出来，代入第二行消去 x1，
右下角残留 S = D - C A^{-1} B = 2 - 1*(1/2)*1 = 3/2，
约化系统 (3/2) x2 = 3 - 1/2 = 5/2，得 x2=1，回代 x1=0。
det M = 3 = det A * det S = 2 * 3/2。无随机数，不调用 LaTeX。
运行：python3 plots.py
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

HERE = Path(__file__).resolve().parent
NAME = HERE.name
ROOT = next(p for p in Path(__file__).resolve().parents
            if (p / "build.sh").is_file() and (p / "tex/book.tex").is_file())
for fname in ["SourceHanSansSC-Normal.otf", "LXGWWenKai-Regular.ttf"]:
    font_manager.fontManager.addfont(ROOT / "fonts" / fname)

BLUE, GREEN, YELLOW, RED = "#7188A3", "#829C8B", "#B4A16F", "#A7787D"
INK, STROKE = "#3B4252", "#4C4D4F"
BLUE_FILL, GREEN_FILL, YELLOW_FILL = "#E5EAF0", "#E8EEE9", "#F1ECDD"
CN, EN = "Source Han Sans SC", "LXGW WenKai"
matplotlib.rcParams.update({
    "font.family": [EN, CN], "font.size": 8, "axes.unicode_minus": False,
    "text.color": INK, "axes.edgecolor": STROKE, "axes.linewidth": .75,
    "xtick.color": STROKE, "ytick.color": STROKE,
    "pdf.fonttype": 3, "svg.fonttype": "path", "figure.facecolor": "white",
})

# 关键精确值
M = np.array([[2, 1], [1, 2]], dtype=float)
A, B, C, D = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
S = D - C * A ** (-1) * B          # 3/2
b = np.array([1, 3.0])
x2 = (b[1] - C * A ** (-1) * b[0]) / S   # 1
x1 = A ** (-1) * (b[0] - B * x2)         # 0

fig, axes = plt.subplots(1, 2, figsize=(11, 3.4))

# 左：分块矩阵 + 消元箭头
ax = axes[0]
ax.set_title("分块：左上块 A=2 可逆，先消去 x₁", fontsize=9)
cells = [("2", BLUE_FILL), ("1", "white"), ("1", YELLOW_FILL), ("2", "white")]
for (r, c), (txt, fc) in zip([(0, 0), (0, 1), (1, 0), (1, 1)], cells):
    ax.add_patch(plt.Rectangle((c, 1 - r), 1, 1, facecolor=fc, edgecolor=STROKE, lw=.8))
    ax.text(c + .5, 1 - r + .5, txt, ha="center", va="center", fontsize=11)
ax.annotate("", xy=(1.02, 0.5), xytext=(.98, 0.5),
            arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.4))
ax.text(.5, 1.18, r"$A=2$", color=BLUE, ha="center", fontsize=9)
ax.text(1.5, 1.18, r"$B=1$", color=INK, ha="center", fontsize=9)
ax.text(.5, -0.22, r"$C=1$", color=YELLOW, ha="center", fontsize=9)
ax.text(1.5, -0.22, r"$D=2$", color=INK, ha="center", fontsize=9)
ax.text(.5, -.6, r"第一行：$2x_1+x_2=1\Rightarrow x_1=(1-x_2)/2$",
        ha="center", fontsize=8, color=INK)
ax.set_xlim(-.2, 2.2); ax.set_ylim(-.8, 1.5); ax.set_aspect("equal"); ax.axis("off")

# 右：Schur 补约化系统
ax = axes[1]
ax.set_title("代入第二行：残留 Schur 补 S=3/2", fontsize=9)
ax.text(.5, .62, r"$S\,x_2=\,b_2-CA^{-1}b_1$", ha="center", fontsize=10,
        transform=ax.transAxes)
ax.text(.5, .40,
        r"$\frac{3}{2}\,x_2=3-\frac{1}{2}=\frac{5}{2}\ \Rightarrow\ x_2=\frac{5}{3}$",
        ha="center", fontsize=10, transform=ax.transAxes, color=GREEN)
ax.text(.5, .18, r"回代 $x_1=-1/3$；$\det M=3=2\cdot\frac{3}{2}$",
        ha="center", fontsize=8.5, transform=ax.transAxes)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

fig.tight_layout()
out = HERE / f"{NAME}.pdf"
fig.savefig(out)
fig.savefig(HERE / f"{NAME}.png", dpi=160)

record = {"M": M.tolist(), "A": A, "B": B, "C": C, "D": D,
          "S": S, "x1": x1, "x2": x2,
          "detM": float(np.linalg.det(M)), "detA_detS": A * S}
(HERE / "sources.json").write_text(json.dumps(record, ensure_ascii=False, indent=2))
print("wrote", out)
print(json.dumps(record, ensure_ascii=False))
