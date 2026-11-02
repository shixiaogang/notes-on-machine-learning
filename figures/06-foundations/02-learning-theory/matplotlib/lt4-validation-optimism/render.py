"""Optimism of selecting the smallest validation error (chapter 4 teaching simulation).

Setting: K = 20 candidates, each with true error 0.10; each is evaluated on its own
independent validation set of m = 200 observations, so its validation error is
Binomial(200, 0.10) / 200. Repetitions: 20000, seed 20261030.
Histograms: validation error of one fixed candidate vs. the minimum over the 20.
Summary statistics are written to data.json.
"""
from pathlib import Path
import json

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
RED, RED_FILL = "#A7787D", "#F0E5E6"
INK, MUTED, LINE, GRID = "#3B4252", "#6B7280", "#4C4D4F", "#D8DCE2"
plt.rcParams.update({
    "font.family": [MATH], "font.size": 8, "axes.edgecolor": LINE,
    "axes.linewidth": 0.75, "axes.labelcolor": INK, "xtick.color": LINE, "ytick.color": LINE,
    "xtick.labelcolor": INK, "ytick.labelcolor": INK, "legend.labelcolor": INK,
    "pdf.fonttype": 3,
})

K, M, P, REPS, SEED = 20, 200, 0.10, 20000, 20261030
rng = np.random.default_rng(SEED)
errors = rng.binomial(M, P, size=(REPS, K)) / M
single = errors[:, 0]
best = errors.min(axis=1)
stats = {
    "K": K, "m": M, "true_error": P, "repetitions": REPS, "seed": SEED,
    "single_mean": round(float(single.mean()), 4),
    "single_sd": round(float(single.std()), 4),
    "min_mean": round(float(best.mean()), 4),
    "min_sd": round(float(best.std()), 4),
    "P_min_le_0.07": round(float((best <= 0.07).mean()), 4),
}
(OUT / "data.json").write_text(json.dumps(stats, indent=1, ensure_ascii=False) + "\n")
print(stats)

MM = 1 / 25.4
fig, ax = plt.subplots(figsize=(107 * MM, 60 * MM))
fig.subplots_adjust(left=0.11, right=0.97, bottom=0.2, top=0.95)
bins = (np.arange(0, 41) - 0.5) / M
ax.hist(single, bins=bins, density=True, color=BLUE_FILL, edgecolor=BLUE, lw=0.6, label="某一个候选的验证误差")
ax.hist(best, bins=bins, density=True, color=RED_FILL, edgecolor=RED, lw=0.6, label="20 个候选中的最小验证误差")
ax.axvline(P, color=LINE, lw=0.8, ls="--")
ax.text(P + 0.002, ax.get_ylim()[1] * 0.52, "真实误差 0.10", color=INK, fontproperties=CJK, ha="left")
ax.axvline(stats["min_mean"], color=RED, lw=0.8, ls=":")
ax.text(stats["min_mean"] - 0.002, ax.get_ylim()[1] * 0.92, f"平均 {stats['min_mean']:.3f}", color=RED, fontproperties=CJK, ha="right")
ax.set_xlim(0.02, 0.18)
ax.set_xlabel("验证误差", fontproperties=CJK)
ax.set_ylabel("密度", fontproperties=CJK)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(loc="upper right", bbox_to_anchor=(1.0, 1.0), frameon=False, prop=font_manager.FontProperties(fname=str(FONTS / "SourceHanSansSC-Normal.otf"), size=7.5))
for ext in ("pdf", "png"):
    fig.savefig(OUT / f"figure.{ext}", dpi=300)
