"""Compare Fisher's exact optimal direction with one unit direction.

Run from any directory. All numbers come from data.json; no random sampling.
The original TikZ asset is preserved and is not modified by this generator.
"""
from pathlib import Path
import os
import tempfile
import sys
import json
import hashlib
import warnings

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "build.sh").is_file())
os.environ.setdefault("MPLCONFIGDIR", tempfile.mkdtemp(prefix="notes-ml-lda-"))
sys.path.insert(0, str(ROOT / "figures/00-shared/academic-drawing"))
import plot_style as style
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.text import Text
import numpy as np
import fitz

style.configure()
DATA = json.loads((HERE / "data.json").read_text())
means = np.asarray(DATA["class_means"])
offsets = np.asarray(DATA["common_offsets"])
classes = [mu + offsets for mu in means]
n = sum(len(x) for x in classes)
total_mean = sum(x.sum(axis=0) for x in classes) / n
sw = sum((x - x.mean(axis=0)).T @ (x - x.mean(axis=0)) for x in classes)
sb = sum(len(x) * np.outer(x.mean(axis=0) - total_mean,
                           x.mean(axis=0) - total_mean) for x in classes)
optimal = np.linalg.solve(sw, means[1] - means[0])
optimal /= np.linalg.norm(optimal)
other = np.asarray(DATA["comparison_unit_direction"])
directions = [optimal, other]
records = []
for w in directions:
    projections = [x @ w for x in classes]
    records.append({"unit_direction": w.tolist(),
                    "projected_samples": [z.tolist() for z in projections],
                    "projected_means": [float(z.mean()) for z in projections],
                    "sample_ranges": [[float(z.min()), float(z.max())] for z in projections],
                    "sample_range_width": [float(np.ptp(z)) for z in projections],
                    "pooled_within_variance": float(w @ sw @ w / n),
                    "Fisher_ratio": float(w @ sb @ w / (w @ sw @ w))})
assert np.allclose(sw, np.diag([0.4, 8]))
assert np.allclose(sb, np.diag([8, 0]))
assert np.allclose(optimal, [1, 0])
assert np.isclose(records[0]["Fisher_ratio"], 20)
assert np.isclose(records[1]["Fisher_ratio"], 180 / 329)
assert records[0]["Fisher_ratio"] > records[1]["Fisher_ratio"]
assert np.allclose([r["sample_range_width"][0] for r in records], [0.6, 1.84])
assert np.allclose([r["pooled_within_variance"] for r in records], [0.05, 0.658])

WIDTH_MM, HEIGHT_MM = 112, 90
fig = plt.figure(figsize=(WIDTH_MM / 25.4, HEIGHT_MM / 25.4), dpi=300)
legend = [Line2D([], [], marker="o", linestyle="none", color=style.BLUE, markersize=4,
                 label="类1"),
          Line2D([], [], marker="s", linestyle="none", color=style.RED, markersize=4,
                 label="类2")]
fig.legend(handles=legend, loc="upper center", bbox_to_anchor=(0.52, 0.995),
           ncol=2, handletextpad=0.4, columnspacing=1.8)
for row, (w, record) in enumerate(zip(directions, records)):
    y = 0.565 if row == 0 else 0.105
    title = "最优方向" if row == 0 else "对比方向"
    ratio = "20" if row == 0 else "0.55"
    fig.text(0.06, y + 0.345, title + r"  $J=" + ratio + "$", fontsize=8)
    xy = fig.add_axes([0.09, y + 0.06, 0.325, 0.255])
    xy.set_xlim(-1.65, 1.65)
    xy.set_ylim(-1.35, 1.35)
    xy.set_aspect("equal", adjustable="box")
    xy.set_xticks([-1, 0, 1])
    xy.set_yticks([-1, 0, 1])
    xy.tick_params(pad=2, length=2)
    xy.grid(True)
    xy.set_xlabel(r"$x_1$", labelpad=0)
    xy.set_ylabel(r"$x_2$", labelpad=0)
    for x, color, marker in zip(classes, [style.BLUE, style.RED], ["o", "s"]):
        xy.scatter(x[:, 0], x[:, 1], s=16, color=color, marker=marker, zorder=4)
        mu = x.mean(axis=0)
        xy.plot(mu[0], mu[1], marker="+", color=color, markersize=7,
                markeredgewidth=1.1, zorder=4)
    xy.annotate("", xy=0.85 * w, xytext=(0, 0),
                arrowprops={"arrowstyle": "->", "color": style.GREEN,
                            "linewidth": 1.1}, zorder=5)
    xy.text(0.42 if row == 0 else 0.0, 0.24 if row == 0 else 0.95,
            r"$\mathbf{w}^{\ast}$" if row == 0 else r"$\mathbf{w}_{\mathrm{B}}$",
            color=style.GREEN, fontsize=8)

    zax = fig.add_axes([0.535, y + 0.055, 0.42, 0.26])
    zax.set_xlim(-1.85, 1.85)
    zax.set_ylim(-0.75, 1.15)
    zax.set_xticks([-1, 0, 1])
    zax.set_yticks([])
    zax.spines["left"].set_visible(False)
    zax.spines["bottom"].set_position(("data", 0))
    zax.tick_params(axis="x", pad=2, length=2)
    zax.text(1.93, 0.02, r"$z$", va="center", fontsize=8)
    for c, (color, fill, marker, yy) in enumerate(
            [(style.BLUE, style.BLUE_FILL, "o", 0.27),
             (style.RED, style.RED_FILL, "s", -0.30)]):
        zs = np.asarray(record["projected_samples"][c])
        lo, hi = record["sample_ranges"][c]
        zax.add_patch(Rectangle((lo, yy - 0.065), hi - lo, 0.13,
                               facecolor=fill, edgecolor=color, linewidth=0.6,
                               zorder=1))
        zax.scatter(zs, np.full(4, yy), color=color, marker=marker, s=13, zorder=3)
        zax.plot([zs.mean(), zs.mean()], [yy - 0.14, yy + 0.14],
                 color=color, linewidth=1.1, zorder=4)
    m1, m2 = record["projected_means"]
    zax.annotate("", xy=(m2, 0.73), xytext=(m1, 0.73),
                arrowprops={"arrowstyle": "<->", "linewidth": 0.75,
                            "color": style.STROKE})
    zax.text((m1 + m2) / 2, 0.9,
             "均值间距 " + ("2" if row == 0 else "1.2"),
             ha="center", fontsize=8)
    variance = "0.05" if row == 0 else "0.658"
    fig.text(0.55, y + 0.005, "类内方差 " + variance, fontsize=8)

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
check = {"key": "classification-lda-target", "physical_size_mm": native,
         "body_width_mm": WIDTH_MM, "scale": 1, "main_font_pt": 8,
         "actual_pdf_fonts": fonts, "page_count": len(pdf),
         "raster_images": len(page.get_images()), "actual_text_clipped": clipped,
         "missing_glyphs": missing, "visual_review": "pending"}
(HERE / "font-and-page-check.json").write_text(json.dumps(check, ensure_ascii=False, indent=2) + "\n")
(HERE / "checks.json").write_text(json.dumps({"S_W": sw.tolist(), "S_B": sb.tolist(),
    "directions": records, "optimality_check": "PASS: exact generalized eigen direction and J comparison",
    "range_vs_variance": "Intervals are sample ranges; displayed variance is w.T S_W w / n"},
    ensure_ascii=False, indent=2) + "\n")
generation = {"key": "classification-lda-target", "route": "Matplotlib exact finite projection data",
    "generator": str(Path(__file__).relative_to(ROOT)),
    "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "data": str((HERE / "data.json").relative_to(ROOT)),
    "data_sha256": hashlib.sha256((HERE / "data.json").read_bytes()).hexdigest(),
    "label": "fig:classification-lda-projection", "is_addition": False,
    "replaces": DATA["original_asset"], "original_preserved": True,
    "physical_size_mm": [WIDTH_MM, HEIGHT_MM], "body_width_mm": WIDTH_MM,
    "style": style.style_record(), "exports": ["figure.pdf", "figure.png", "figure.svg"]}
(HERE / "generation.json").write_text(json.dumps(generation, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"native_mm": native, "Fisher_ratio": [r["Fisher_ratio"] for r in records],
                  "fonts": fonts, "checks": "PASS"}, ensure_ascii=False))
