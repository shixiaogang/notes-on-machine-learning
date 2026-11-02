"""Bayes risk teaching figure for chapter 4 (volume 6, learning theory).

Analytic setting (teaching example, not data):
  x ~ Uniform[0, 1];
  eta(x) = P(y = 1 | x) = 0.1 on [0, 0.4], 0.1 + 2(x - 0.4) on [0.4, 0.8], 0.9 on [0.8, 1].
Left panel: eta(x), 1 - eta(x) and the pointwise minimum min{eta, 1 - eta};
  Bayes risk = integral of the minimum = 0.04 + 0.12 + 0.02 = 0.18.
  eta(x) >= 1/2 exactly when x >= 0.6, so the Bayes rule is h*(x) = 1{x >= 0.6}.
Right panel: extra error of the threshold rule h_{0.4} relative to the Bayes rule;
  on [0.4, 0.6) h_{0.4} predicts 1 (error 1 - eta) while h* predicts 0 (error eta);
  extra error = integral_{0.4}^{0.6} (1 - 2 eta(x)) dx = 0.08, so R(h_{0.4}) = 0.26.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np


def project_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "tex" / "volumes.json").exists():
            return parent
    raise RuntimeError("project root not found")


ROOT = project_root()
OUT = Path(__file__).resolve().parent
FONTS = ROOT / "fonts"
for name in ("SourceHanSansSC-Normal.otf", "LXGWWenKai-Regular.ttf", "FiraMath-Regular.otf"):
    font_manager.fontManager.addfont(str(FONTS / name))
CJK = font_manager.FontProperties(fname=str(FONTS / "SourceHanSansSC-Normal.otf"), size=8)
CJK_NOTE = font_manager.FontProperties(fname=str(FONTS / "LXGWWenKai-Regular.ttf"), size=7.5)
MATH = font_manager.FontProperties(fname=str(FONTS / "FiraMath-Regular.otf")).get_name()

BLUE, BLUE_FILL = "#7188A3", "#E5EAF0"
GREEN, GREEN_FILL = "#829C8B", "#E8EEE9"
YELLOW, YELLOW_FILL = "#B4A16F", "#F1ECDD"
RED, RED_FILL = "#A7787D", "#F0E5E6"
INK, MUTED, LINE, GRID = "#3B4252", "#6B7280", "#4C4D4F", "#D8DCE2"

plt.rcParams.update({
    "font.family": [MATH],
    "font.size": 8,
    "axes.edgecolor": LINE,
    "axes.linewidth": 0.75,
    "axes.labelcolor": INK,
    "xtick.color": LINE,
    "ytick.color": LINE,
    "xtick.labelcolor": INK,
    "ytick.labelcolor": INK,
    "xtick.major.width": 0.75,
    "ytick.major.width": 0.75,
    "pdf.fonttype": 3,
})


def eta(x):
    return np.clip(0.1 + 2.0 * (x - 0.4), 0.1, 0.9)


x = np.linspace(0.0, 1.0, 1001)
e = eta(x)
m = np.minimum(e, 1 - e)

MM = 1 / 25.4
fig, axes = plt.subplots(1, 2, figsize=(150 * MM, 56 * MM), sharey=True)
fig.subplots_adjust(left=0.085, right=0.975, bottom=0.19, top=0.8, wspace=0.12)

ax = axes[0]
ax.fill_between(x, 0, m, color=YELLOW_FILL, linewidth=0)
ax.plot(x, e, color=BLUE, lw=1.1, label="η(x)")
ax.plot(x, 1 - e, color=RED, lw=1.1, ls="--", label="1 − η(x)")
ax.plot(x, m, color=YELLOW, lw=1.1)
ax.axhline(0.5, color=GRID, lw=0.6)
ax.axvline(0.6, color=MUTED, lw=0.6, ls=":")
ax.text(0.6, 1.02, "x = 0.6", ha="center", va="bottom", color=INK)
ax.text(0.3, 0.62, "预测 0", ha="center", color=INK, fontproperties=CJK)
ax.text(0.85, 0.62, "预测 1", ha="center", color=INK, fontproperties=CJK)
ax.text(0.3, 0.04, "阴影面积 0.18", ha="center", color=MUTED, fontproperties=CJK_NOTE)
ax.set_title("逐点最小错误", fontproperties=CJK, color=INK, pad=14)
ax.legend(loc="lower left", bbox_to_anchor=(0.66, 0.16), frameon=False, fontsize=7.5, handlelength=2.2)

ax = axes[1]
seg = (x >= 0.4) & (x <= 0.6)
ax.fill_between(x[seg], e[seg], 1 - e[seg], color=RED_FILL, linewidth=0)
ax.fill_between(x, 0, m, color=YELLOW_FILL, linewidth=0)
ax.plot(x, e, color=BLUE, lw=1.1)
ax.plot(x, 1 - e, color=RED, lw=1.1, ls="--")
ax.axhline(0.5, color=GRID, lw=0.6)
ax.axvline(0.6, color=MUTED, lw=0.6, ls=":")
ax.axvline(0.4, color=GREEN, lw=0.8, ls="-.")
ax.text(0.4, 1.02, "t = 0.4", ha="center", va="bottom", color=INK)
ax.annotate("额外错误 0.08", xy=(0.47, 0.55), xytext=(0.64, 0.74), color=INK, fontproperties=CJK,
            arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6))
ax.set_title("阈值 0.4 的额外错误", fontproperties=CJK, color=INK, pad=14)

for ax in axes:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("邮件分数 x", fontproperties=CJK)
    ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.spines[["top", "right"]].set_visible(False)
axes[0].set_ylabel("条件错误概率", fontproperties=CJK)

for ext in ("pdf", "png"):
    fig.savefig(OUT / f"figure.{ext}", dpi=300)
# Numerical check of the stated values.
print("bayes risk", np.trapezoid(m, x), "extra(0.6)", np.trapezoid(np.abs(2 * e[seg] - 1), x[seg]))
