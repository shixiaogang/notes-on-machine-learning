"""Exact calibration order-statistic panel for fig:trust-conformal-construction.

Input is the book's explicit teaching construction, not experimental evidence.
Run with Matplotlib and NumPy available; outputs are generated at final 106x40mm.
"""
from pathlib import Path
import json, math, sys
import matplotlib
matplotlib.use("Agg")
from matplotlib import font_manager
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent
ROOT = OUT.parent
spec = json.loads((OUT / "trust-conformal-residuals-data.json").read_text())
values = np.sort(np.asarray(spec["residuals"], dtype=float))
n, alpha = len(values), spec["alpha"]
k = math.ceil((n + 1) * (1 - alpha))
q = float(values[k - 1])
assert (n, k, q) == (spec["n"], spec["k"], spec["q"])
for filename in ("SourceSans3-Regular.otf", "LXGWWenKai-Regular.ttf", "STIXTwoText-Regular.otf"):
    font_manager.fontManager.addfont(ROOT / "fonts" / filename)
plt.rcParams.update({
    "font.family": ["Source Sans 3", "LXGW WenKai"], "font.size": 9,
    "font.weight": "normal", "axes.labelweight": "normal",
    "mathtext.fontset": "stix", "pdf.fonttype": 3, "svg.fonttype": "path",
    "axes.linewidth": .85, "text.color": "#4C4D4F", "axes.edgecolor": "#4C4D4F",
    "axes.labelcolor": "#4C4D4F", "xtick.color": "#4C4D4F", "ytick.color": "#4C4D4F",
    "xtick.major.width": .65, "ytick.major.width": .65,
})
fig = plt.figure(figsize=(106 / 25.4, 40 / 25.4), facecolor="white")
ax = fig.add_axes([.10, .26, .88, .58])
ax.spines[["top", "right"]].set_visible(False)
ax.set(xlim=(.45, 9.55), ylim=(0, 1.10), xticks=np.arange(1, n+1), yticks=[0, .4, .8, 1.0])
ax.set_xlabel("$i$", labelpad=0)
ax.set_ylabel("$s_{(i)}$", labelpad=3)
ax.tick_params(length=2, pad=2)
blue, coral = "#7998AD", "#D57B70"
colors = [coral if i == k - 1 else blue for i in range(n)]
ax.bar(np.arange(1, n+1), values, width=.65, color=colors, edgecolor="none", zorder=2)
ax.axhline(q, color=coral, lw=.85, linestyle=(0,(4,3)), zorder=3)
for i, value in enumerate(values, 1):
    ax.text(i, value+.035, f"{value:.1f}", ha="center", va="bottom", fontsize=8.5)
fig.text(.52, .965, r"$n=9,\ \alpha=0.2,\ k=8,\ q=0.8$", ha="center", va="top", fontsize=9)
for ext in ("pdf", "svg", "png"):
    fig.savefig(OUT / f"trust-conformal-residuals.{ext}", dpi=350, facecolor="white")
plt.close(fig)
metadata = {
    "source": "Explicit teaching construction from the book; not measurements",
    "input": "trust-conformal-residuals-data.json", "n": n, "alpha": alpha, "k": k, "q": q,
    "formula": "ceil((n+1)*(1-alpha)), then the k-th sorted residual",
    "size_mm": [106,40], "font_size_pt": 9, "value_label_size_pt": 8.5,
    "python": sys.version.split()[0], "matplotlib": matplotlib.__version__, "numpy": np.__version__,
    "fonts": ["SourceSans3-Regular.otf", "LXGWWenKai-Regular.ttf"], "mathtext": "stix",
    "pdf_fonttype": 3, "svg_fonttype": "path", "palette": {"residual":blue, "eighth":coral},
    "processing": "Full list sorted ascending; no random sampling, smoothing, fitting or filtering",
}
(OUT / "trust-conformal-residuals-metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2)+"\n")
print(f"Saved precise residual panel; n={n}, k={k}, q={q}")
