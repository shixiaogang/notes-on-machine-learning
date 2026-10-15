"""Render one exact augmented perceptron update in the same input plane."""
from pathlib import Path
import os
import tempfile
import sys
import json
import hashlib
import warnings

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "build.sh").is_file())
os.environ.setdefault("MPLCONFIGDIR", tempfile.mkdtemp(prefix="notes-ml-perceptron-"))
sys.path.insert(0, str(ROOT / "figures/00-shared/academic-drawing"))
import plot_style as style
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle, Polygon
from matplotlib.text import Text
import numpy as np
import fitz

style.configure()
data = json.loads((HERE / "data.json").read_text())
positive = np.asarray(data["positive_samples"])
negative = np.asarray(data["negative_samples"])
x = np.asarray(data["trigger_sample"])
y = data["trigger_label"]
eta = data["learning_rate"]
w0 = np.asarray(data["weight_before"])
b0 = data["bias_before"]
w1 = w0 + eta * y * x
b1 = b0 + eta * y
score0, score1 = float(w0 @ x + b0), float(w1 @ x + b1)
assert np.allclose(w1, [1.25, 0.5])
assert np.isclose(b1, -0.5)
assert np.isclose(score0, -0.5) and np.isclose(score1, 0.625)
assert y * score0 < 0 < y * score1
increase = float(eta * (x @ x + 1))
assert np.isclose(score1 - score0, increase)

WIDTH_MM, HEIGHT_MM = 112, 77
fig = plt.figure(figsize=(WIDTH_MM / 25.4, HEIGHT_MM / 25.4), dpi=300)
legend = [Line2D([], [], marker="o", linestyle="none", color=style.BLUE,
                 markersize=4, label=r"正类 $y=+1$"),
          Line2D([], [], marker="s", linestyle="none", color=style.RED,
                 markersize=4, label=r"负类 $y=-1$")]
fig.legend(handles=legend, loc="upper center", bbox_to_anchor=(0.52, 0.995),
           ncol=2, handletextpad=0.4, columnspacing=1.3)
for k in [0, 1]:
    ax = fig.add_axes([0.09 + 0.48 * k, 0.25, 0.365, 0.585])
    ax.set_xlim(-1, 2)
    ax.set_ylim(-1.5, 2)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks([-1, 0, 1, 2])
    ax.set_yticks([-1, 0, 1, 2])
    ax.tick_params(pad=2, length=2)
    ax.grid(True)
    ax.set_xlabel(r"$x_1$", labelpad=1)
    ax.set_ylabel(r"$x_2$", labelpad=1)
    if k == 0:
        ax.add_patch(Rectangle((1, -1.5), 1, 3.5, facecolor=style.BLUE_FILL,
                               edgecolor="none", zorder=0))
    else:
        # Exact intersections of 1.25*x1 + .5*x2 = .5 with the plot rectangle.
        x_at_bottom = (-b1 - w1[1] * -1.5) / w1[0]
        x_at_top = (-b1 - w1[1] * 2) / w1[0]
        ax.add_patch(Polygon([(x_at_bottom, -1.5), (2, -1.5),
                              (2, 2), (x_at_top, 2)], facecolor=style.BLUE_FILL,
                             edgecolor="none", zorder=0))
        xx = np.array([x_at_top, x_at_bottom])
        yy = (-b1 - w1[0] * xx) / w1[1]
        assert np.allclose(w1[0] * xx + w1[1] * yy + b1, 0)
        ax.plot(xx, yy, color=style.GREEN, linewidth=1.1, zorder=2)
    ax.axvline(1, color=style.STROKE, linewidth=0.85,
               linestyle=(0, (4, 3)), zorder=2)
    ax.scatter(positive[:, 0], positive[:, 1], s=18, color=style.BLUE,
               marker="o", zorder=3)
    ax.scatter(negative[:, 0], negative[:, 1], s=18, color=style.RED,
               marker="s", zorder=3)
    ax.scatter([x[0]], [x[1]], s=65, marker="o", facecolors="none",
               edgecolors=style.INK, linewidths=0.8, zorder=4)
    ax.annotate("当前正类点", xy=x, xytext=(-0.9, 1.64) if k == 0 else (0.70, 1.75), fontsize=8,
                arrowprops={"arrowstyle": "->", "linewidth": 0.6,
                            "color": style.STROKE},
                color=style.INK, ha="left", va="center")
    ax.set_title("更新前" if k == 0 else "一次更新后", pad=5)
    fig.text(0.09 + 0.48 * k, 0.12,
             r"$g(\mathbf{x}_i)=-0.5$" if k == 0 else r"$g(\mathbf{x}_i)=0.625$",
             fontsize=8)
    fig.text(0.09 + 0.48 * k, 0.065,
             "触发更新" if k == 0 else "当前点已分对", fontsize=8)

style.prepare_figure(fig)
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
clipped = []
for artist in fig.findobj(Text):
    if artist.get_visible() and artist.get_text().strip():
        bb = artist.get_window_extent(renderer)
        if bb.x0 < -1 or bb.y0 < -1 or bb.x1 > fig.bbox.width + 1 or bb.y1 > fig.bbox.height + 1:
            clipped.append(artist.get_text())
assert not clipped, clipped
with warnings.catch_warnings(record=True) as captured:
    warnings.simplefilter("always")
    for suffix in ["pdf", "png", "svg"]:
        fig.savefig(HERE / ("figure." + suffix), dpi=300)
missing = [str(w.message) for w in captured if "Glyph" in str(w.message)]
assert not missing, missing
pdf = fitz.open(HERE / "figure.pdf")
page = pdf[0]
native = [page.rect.width * 25.4 / 72, page.rect.height * 25.4 / 72]
assert np.allclose(native, [WIDTH_MM, HEIGHT_MM], atol=0.002)
fonts = sorted({font[3] for font in page.get_fonts(full=True)})
(HERE / "font-and-page-check.json").write_text(json.dumps({
    "key": "classification-perceptron-update", "physical_size_mm": native,
    "body_width_mm": WIDTH_MM, "scale": 1, "main_font_pt": 8,
    "actual_pdf_fonts": fonts, "page_count": len(pdf),
    "raster_images": len(page.get_images()), "actual_text_clipped": clipped,
    "missing_glyphs": missing, "visual_review": "pending"}, ensure_ascii=False, indent=2) + "\n")
(HERE / "checks.json").write_text(json.dumps({
    "weight_before": w0.tolist(), "bias_before": b0,
    "weight_after": w1.tolist(), "bias_after": b1,
    "trigger_score_before": score0, "trigger_score_after": score1,
    "signed_score_increase": increase,
    "boundary_before": "x1=1", "boundary_after": "1.25*x1+0.5*x2=0.5",
    "checks": "PASS: augmented update, trigger signs, score increase, boundary intersections"},
    ensure_ascii=False, indent=2) + "\n")
(HERE / "generation.json").write_text(json.dumps({
    "key": "classification-perceptron-update", "route": "Matplotlib exact 2D update",
    "generator": str(Path(__file__).relative_to(ROOT)),
    "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "data": str((HERE / "data.json").relative_to(ROOT)),
    "data_sha256": hashlib.sha256((HERE / "data.json").read_bytes()).hexdigest(),
    "label": "fig:classification-perceptron-update", "is_addition": True,
    "physical_size_mm": [WIDTH_MM, HEIGHT_MM], "body_width_mm": WIDTH_MM,
    "style": style.style_record(), "exports": ["figure.pdf", "figure.png", "figure.svg"]},
    ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"native_mm": native, "scores": [score0, score1],
                  "fonts": fonts, "checks": "PASS"}, ensure_ascii=False))
