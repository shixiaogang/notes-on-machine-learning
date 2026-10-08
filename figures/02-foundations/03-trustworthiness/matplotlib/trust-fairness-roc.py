"""Exact ROC panel for the teaching example ex:fairness-random-threshold.

Run from any directory with Matplotlib/NumPy available. Inputs are the explicit
constructed validation rates in the book, not measured experimental evidence.
The mixing coin is independent of the true label; thus both class-conditional
rates are convex combinations. No smoothing, estimation or fitted ROC curve.
"""
from pathlib import Path
import json
import sys

import matplotlib
matplotlib.use("Agg")
from matplotlib import font_manager
import matplotlib.pyplot as plt
import numpy as np

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
OUT = Path(__file__).resolve().parent
DATA = OUT / "trust-fairness-roc-data.json"
for filename in ("SourceSans3-Regular.otf", "LXGWWenKai-Regular.ttf", "STIXTwoText-Regular.otf"):
    font_manager.fontManager.addfont(ROOT / "fonts" / filename)
plt.rcParams.update({
    "font.family": ["Source Sans 3", "LXGW WenKai"],
    "font.size": 8.5, "font.weight": "normal", "axes.labelweight": "normal",
    # Source Han's repository OTF uses CFF; Type42 produced invisible CJK glyphs
    # in the rendered PDF despite an apparently embedded font. Type3 retains
    # actual vector glyph outlines and is verified after PDF import into TeX.
    "mathtext.fontset": "stix", "pdf.fonttype": 3, "ps.fonttype": 3,
    "svg.fonttype": "path", "axes.linewidth": .9,
    "text.color": "#222222", "axes.edgecolor": "#444444",
    "axes.labelcolor": "#222222", "xtick.color": "#444444", "ytick.color": "#444444",
    "xtick.labelsize": 8, "ytick.labelsize": 8,
    "xtick.major.width": .6, "ytick.major.width": .6,
})
spec = json.loads(DATA.read_text())
points = np.array(spec["first_group_thresholds"])
weights = np.array(spec["mixture_weights"])
mixed = weights @ points
assert np.isclose(weights.sum(), 1) and np.all(weights >= 0)
assert np.allclose(mixed, spec["mixture_point"]) and np.allclose(mixed, spec["second_group_point"])

fig = plt.figure(figsize=(54 / 25.4, 54 / 25.4), facecolor="white")
ax = fig.add_axes([.19, .18, .74, .74])
ax.spines[["top", "right"]].set_visible(False)
ax.set(xlim=(0, 1), ylim=(0, 1), xticks=[0, .5, 1], yticks=[0, .5, 1])
ax.set_aspect("equal", adjustable="box")
ax.tick_params(length=2.5, pad=2)
ax.set_xlabel("FPR", labelpad=2)
ax.set_ylabel("TPR", labelpad=2)
blue, coral = "#7998AD", "#D57B70"
ax.plot(points[:, 0], points[:, 1], color=blue, lw=1.1, zorder=2)
ax.plot(points[:, 0], points[:, 1], "o", ms=4.5, mfc="white", mec=blue, mew=1, zorder=3)
ax.plot(*mixed, "s", ms=4.8, mfc=coral, mec=coral, mew=.8, zorder=4)
for point, title, coord, color in [
    (points[0], "阈值1", "(0.1, 0.5)", blue),
    (mixed, "等权混合", "(0.2, 0.7)", coral),
    (points[1], "阈值2", "(0.3, 0.9)", blue),
]:
    ax.annotate(title, point, xytext=(8, -1), textcoords="offset points",
                fontsize=8.5, va="center", color=color)
    ax.annotate(coord, point, xytext=(8, -11), textcoords="offset points",
                fontsize=8, va="center", color=color)
fig.canvas.draw()
for extension in ("pdf", "svg", "png"):
    fig.savefig(OUT / f"trust-fairness-roc.{extension}", dpi=350, facecolor="white")
plt.close(fig)
metadata = {
    "python": sys.version.split()[0], "matplotlib": matplotlib.__version__,
    "numpy": np.__version__, "size_mm": [54, 54], "axes_limits": [[0, 1], [0, 1]],
    "aspect": "equal", "origin": [0, 0], "input": DATA.name,
    "fonts": ["SourceSans3-Regular.otf", "LXGWWenKai-Regular.ttf"],
    "mathtext": "stix", "pdf_fonttype": 3, "svg_fonttype": "path",
    "pdf_font_reason": "CFF OpenType Source Han glyphs were invisible under Type42; Type3 vector glyph outlines validated in source and imported PDFs",
    "palette": {"thresholds": blue, "mixture": coral, "outline": "#444444"},
    "processing": "Exact two-point convex combination; no filtering, fitting, sampling or randomness",
    "vector_outputs": ["trust-fairness-roc.pdf", "trust-fairness-roc.svg"],
}
(OUT / "trust-fairness-roc-metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
print("Saved the exact 54mm ROC vector panel and native-size preview.")
