"""集合标签类上读标签规则的两种情形（第6章 6.3.4）。

目标为 h_A，p = P_X(A) 为输入落在目标集合 A 中的概率，样本量 n。
读标签规则：样本中出现 A 内的输入即恢复目标（风险 0）；否则输出处处为 * 的
默认规则 h_empty，风险恰为 p。因此
  P{风险 > eps} = 0                 (p <= eps)
               = (1 - p)^n          (p >  eps)
参数：eps = 0.1，n = 30，delta = 0.05；右侧最大值 (1-eps)^n = 0.9^30 ≈ 0.0424 <= delta。
虚线为 P{样本未见 A} = (1-p)^n，对所有 p 画出。
"""
from pathlib import Path
import json

import numpy as np
import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt
from matplotlib import font_manager


def project_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "tex" / "volumes.json").exists():
            return parent
    raise RuntimeError("project root not found")


ROOT = project_root()
OUT = Path(__file__).resolve().parent
for name in ("SourceHanSansSC-Normal.otf", "FiraMath-Regular.otf", "LXGWWenKai-Regular.ttf"):
    font_manager.fontManager.addfont(str(ROOT / "fonts" / name))
CJK = font_manager.FontProperties(fname=str(ROOT / "fonts" / "SourceHanSansSC-Normal.otf")).get_name()
MATH = font_manager.FontProperties(fname=str(ROOT / "fonts" / "FiraMath-Regular.otf")).get_name()
plt.rcParams.update({
    "font.family": [CJK, MATH],
    "font.size": 8,
    "mathtext.fontset": "custom",
    "mathtext.rm": MATH, "mathtext.it": MATH,
    "axes.linewidth": 0.75,
    "pdf.fonttype": 3,
})
BLUE = "#7188A3"
GREEN, GREEN_FILL = "#829C8B", "#E8EEE9"
RED = "#A7787D"
INK, MUTED, GRID = "#3B4252", "#6B7280", "#D8DCE2"

EPS, N, DELTA = 0.1, 30, 0.05
p = np.linspace(0, 1, 1001)
miss = (1 - p) ** N
fail = np.where(p > EPS, miss, 0.0)

fig, ax = plt.subplots(figsize=(4.2, 2.3))
ax.axvspan(0, EPS, color=GREEN_FILL, lw=0)
ax.plot(p, miss, color=MUTED, lw=0.9, ls=(0, (3, 2)), label=r"未见到 $A$ 的概率 $(1-p)^n$")
ax.plot(p[p <= EPS], fail[p <= EPS], color=BLUE, lw=1.4)
ax.plot(p[p > EPS], fail[p > EPS], color=BLUE, lw=1.4, label=r"风险超过 $\varepsilon$ 的概率")
ax.plot([EPS, EPS], [0, (1 - EPS) ** N], color=BLUE, lw=0.6, ls=":")
ax.axhline(DELTA, color=RED, lw=0.6, ls="--")
ax.text(0.98, DELTA + 0.012, r"$\delta=0.05$", color=RED, ha="right", va="bottom", fontsize=7.5)
ax.annotate("$p\\leq\\varepsilon$：默认规则风险已不超过 $\\varepsilon$", xy=(EPS * 0.6, 0.45),
            xytext=(0.2, 0.55), fontsize=7.5, color=INK, va="center",
            arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6))
ax.annotate(r"$(1-\varepsilon)^n\approx0.042$", xy=(EPS, (1 - EPS) ** N), xytext=(0.3, 0.25),
            fontsize=7.5, color=INK,
            arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.02)
ax.set_xlabel(r"目标集合的概率 $p=\mathcal{P}_X(A)$", color=INK)
ax.set_ylabel("概率", color=INK)
ax.spines[["top", "right"]].set_visible(False)
ax.yaxis.grid(True, color=GRID, linewidth=0.4)
ax.set_axisbelow(True)
ax.tick_params(colors=INK, width=0.75, labelsize=7.5)
ax.legend(frameon=False, fontsize=7.5, loc="upper right")
fig.tight_layout(pad=0.3)
fig.savefig(OUT / "figure.pdf")
(OUT / "data.json").write_text(json.dumps({
    "epsilon": EPS, "n": N, "delta": DELTA,
    "max_failure_prob": round((1 - EPS) ** N, 6),
    "formula": "P{R>eps} = 1{p>eps} (1-p)^n",
}, ensure_ascii=False, indent=1))
