"""教学图：张量积的槽位结构与秩一张量的外积矩阵。

固定构造：两个二维基的乘积基 e_i⊗f_j 排成 2×2 槽位网格；
秩一张量 u⊗v 取 u=(1,2)，v=(3,1)，外积矩阵 [[3,1],[6,2]]。
无随机数，不调用 LaTeX。
从任意目录运行：python3 plots.py [--only ls-tensor-product-slots]
"""
from pathlib import Path
import argparse
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle, FancyArrowPatch
from matplotlib.text import Text

HERE = Path(__file__).resolve().parent
NAME = HERE.name
ROOT = next(p for p in Path(__file__).resolve().parents
            if (p / "build.sh").is_file() and (p / "tex/book.tex").is_file())

for fname in ["SourceHanSansSC-Normal.otf", "LXGWWenKai-Regular.ttf", "FiraMath-Regular.otf"]:
    font_manager.fontManager.addfont(ROOT / "fonts" / fname)

BLUE, GREEN, YELLOW, RED = "#7188A3", "#829C8B", "#B4A16F", "#A7787D"
INK, MUTED = "#3B4252", "#6B7280"
BLUE_FILL, GREEN_FILL, RED_FILL = "#E5EAF0", "#E8EEE9", "#F0E5E6"
CN_MAIN, CN_AUX, EN = "Source Han Sans SC", "LXGW WenKai", "Fira Math"

matplotlib.rcParams.update({
    "font.family": [EN, CN_MAIN], "font.size": 8,
    "mathtext.fontset": "custom", "mathtext.rm": EN, "mathtext.it": EN,
    "mathtext.bf": EN, "mathtext.sf": EN,
    "axes.unicode_minus": False, "text.color": INK,
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
    "pdf.fonttype": 3, "svg.fonttype": "path",
})

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--only", default=NAME, choices=[NAME],
                    help="本目录仅一幅图；保留参数以统一调用方式。")
selection = parser.parse_args().only

U = [1, 2]
V = [3, 1]
M = [[U[0] * V[0], U[0] * V[1]], [U[1] * V[0], U[1] * V[1]]]  # [[3,1],[6,2]]


def finalize(fig):
    for t in fig.findobj(Text):
        s = t.get_text()
        has_cjk = any(("⺀" <= ch <= "鿿") or ("＀" <= ch <= "￯") for ch in s)
        t.set_fontfamily([CN_MAIN, EN] if has_cjk else [EN, CN_MAIN])
        t.set_fontweight("normal")


fig, ax = plt.subplots(figsize=(112 / 25.4, 96 / 25.4))
ax.set_xlim(-1.4, 4.6); ax.set_ylim(-.4, 5.4); ax.axis("off")

# ---- 上半：乘积基槽位网格（行 i=e 红轴，列 j=f 蓝轴）----
slots = [("e_1\\otimes f_1", 0, 3), ("e_1\\otimes f_2", 1, 3),
         ("e_2\\otimes f_1", 0, 2), ("e_2\\otimes f_2", 1, 2)]
for lab, cx, cy in slots:
    ax.add_patch(Rectangle((cx, cy), 1, 1, facecolor=BLUE_FILL,
                          edgecolor=BLUE, lw=1.0))
    ax.text(cx + .5, cy + .5, f"${lab}$", fontsize=8, ha="center", va="center")
ax.text(-.55, 3.5, "$e_1$", fontsize=8, color=RED, ha="center")
ax.text(-.55, 2.5, "$e_2$", fontsize=8, color=RED, ha="center")
ax.text(.5, 1.72, "$f_1$", fontsize=8, color=BLUE, ha="center")
ax.text(1.5, 1.72, "$f_2$", fontsize=8, color=BLUE, ha="center")
ax.text(.5, 5.15, "乘积基槽位：$\\{e_i\\otimes f_j\\}$，一个张量就是四块上的数",
        fontsize=8, color=INK, ha="center")

# ---- 下半：秩一张量 u⊗v 的外积矩阵 ----
ax.text(3.36, 2.05, "秩一张量 $u\\otimes v$：$u=(1,2)$，$v=(3,1)$",
        fontsize=7.5, color=INK, ha="center")
for i in range(2):
    for j in range(2):
        ax.add_patch(Rectangle((2.7 + j * .66, 1.05 - i * .66), .66, .66,
                               facecolor=GREEN_FILL, edgecolor=GREEN, lw=.9))
        ax.text(2.7 + j * .66 + .33, 1.05 - i * .66 + .33, str(M[i][j]),
                fontsize=8, ha="center", va="center", color=INK)
ax.text(3.36, .12, "$(u\\otimes v)_{ij}=u_i v_j$",
        fontsize=7.5, color=MUTED, ha="center")

finalize(fig)
fig.tight_layout()
for ext in ("pdf", "svg", "png"):
    if selection == NAME:
        fig.savefig(HERE / f"{NAME}.{ext}", dpi=300)
plt.close(fig)

record = {
    "kind": "analytical teaching construction, not observed experimental data",
    "reader_question": "一个二阶张量为什么能拆成“基槽位网格”上的一组数？",
    "formula": "basis slots e_i⊗f_j, i,j∈{1,2}; rank-one tensor u⊗v with u=(1,2), v=(3,1); "
               "outer product matrix M_ij=u_i v_j = [[3,1],[6,2]].",
    "parameters": {"u": U, "v": V},
    "evaluated_data": {"outer_product_matrix": M},
    "processing": "外积逐分量相乘；无随机采样。",
    "width_mm": 112, "height_mm": 96, "png_dpi": 300,
    "outputs": [f"{NAME}.pdf", f"{NAME}.svg", f"{NAME}.png"],
}
(HERE / "sources.json").write_text(
    json.dumps({"style": "figures.md 统一色板：蓝#7188A3 绿#829C8B 黄#B4A16F 红#A7787D",
                "fonts": {"Chinese": "fonts/SourceHanSansSC-Normal.otf",
                          "Chinese_aux": "fonts/LXGWWenKai-Regular.ttf",
                          "math": "fonts/FiraMath-Regular.otf"},
                "figures": {NAME: record}}, ensure_ascii=False, indent=2) + "\n")
print("generated", NAME)
