"""Deterministic teaching figure: ridge shrinkage vs Lasso soft thresholding."""
from pathlib import Path
import hashlib, json, os, platform, sys, tempfile

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "build.sh").is_file())
OUT = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", tempfile.mkdtemp(prefix=OUT.name + "-mpl-"))
sys.path.insert(0, str(ROOT / "figures/00-shared/academic-drawing"))
import plot_style as style
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.text import Text
import numpy as np

style.configure()
WIDTH_MM = 105.412
HEIGHT_MM = 78.0
LAM = 0.5

def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

xs = np.linspace(-2, 2, 201)
ridge = xs / (1.0 + LAM)
lasso = np.sign(xs) * np.maximum(0.0, np.abs(xs) - LAM)

fig, ax = plt.subplots(figsize=(WIDTH_MM / 25.4, HEIGHT_MM / 25.4))
ax.axvspan(-LAM, LAM, color=style.BLUE_FILL, zorder=0)
ax.plot(xs, ridge, color=style.BLUE, lw=1.1, label=r"岭：$w_j=c_j/(1+\lambda)$")
ax.plot(xs, lasso, color=style.RED, lw=1.1, label=r"Lasso：$w_j=\mathcal{S}_\lambda(c_j)$")
ax.axhline(0, color=style.STROKE, lw=0.6)
ax.axvline(0, color=style.STROKE, lw=0.6)
for t in (-LAM, LAM):
    ax.plot([t, t], [-LAM, 0], color=style.MUTED, lw=0.6, ls="--")
ax.annotate(r"$\lambda=0.5$：$|c_j|\leq\lambda$ 时 Lasso 取零",
            xy=(0.0, 0.0), xytext=(0.0, 0.62), ha="center",
            fontsize=7.5, arrowprops=dict(arrowstyle="-", color=style.MUTED, lw=0.6))
ax.set_xlabel(r"正交设计下的 OLS 坐标参数 $c_j$")
ax.set_ylabel(r"惩罚收缩后的参数 $w_j$")
ax.legend(loc="lower right", fontsize=7.5, frameon=False)
ax.set_xlim(-2.1, 2.1); ax.set_ylim(-1.7, 2.0)
ax.set_xticks([-2, -1, 0, 1, 2]); ax.set_yticks([-1, 0, 1, 2])

fig.subplots_adjust(left=0.12, right=0.97, top=0.97, bottom=0.17)
style.prepare_figure(fig)
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
outside = []
for t in fig.findobj(Text):
    if not t.get_visible() or not t.get_text().strip():
        continue
    box = t.get_window_extent(renderer)
    if box.x0 < -1 or box.y0 < -1 or box.x1 > fig.bbox.width + 1 or box.y1 > fig.bbox.height + 1:
        outside.append({"text": t.get_text(), "bbox_pixels": list(box.bounds)})
assert not outside, outside
for ext in ["pdf", "svg", "png"]:
    fig.savefig(OUT / ("figure." + ext), dpi=240)
import fitz
with fitz.open(OUT / "figure.pdf") as doc:
    page = doc[0]
    dimensions = [page.rect.width * 25.4 / 72, page.rect.height * 25.4 / 72]
    assert len(doc) == 1
    assert np.allclose(dimensions, [WIDTH_MM, HEIGHT_MM], atol=0.01)

c1 = 1.0
checks = [
    {"where": "c=1", "lasso_w": float(np.sign(c1) * max(0, abs(c1) - LAM)), "expected": 0.5},
    {"where": "c=1", "ridge_w": float(c1 / (1.0 + LAM)), "expected": 2.0 / 3.0},
    {"where": "c=0.25", "lasso_w": float(np.sign(0.25) * max(0, abs(0.25) - LAM)), "expected": 0.0},
]
for chk in checks:
    key = "lasso_w" if "lasso_w" in chk else "ridge_w"
    assert abs(chk[key] - chk["expected"]) < 1e-3, chk
data = {"lambda": LAM, "design": "X^T X / n = I", "checks": checks}
dump("data.json", data)
dump("checks.json", {"key": "regression-lasso-soft-threshold", "numeric_checks": data, "renderer_text_outside_canvas": outside})
dump("generation.json", {
    "key": "regression-lasso-soft-threshold", "route": "Matplotlib",
    "generator": str(Path(__file__).resolve().relative_to(ROOT)),
    "generator_sha256": sha(Path(__file__)),
    "style": style.style_record(),
    "parameters": {"lambda": LAM, "design": "orthonormal X^TX/n=I"},
    "software": {"python": platform.python_version(), "numpy": np.__version__, "matplotlib": matplotlib.__version__},
    "current_display": {"asset": str((OUT / "figure.pdf").relative_to(ROOT)), "native_width_mm": WIDTH_MM,
                        "native_height_mm": HEIGHT_MM, "body_width_mm": WIDTH_MM, "scale": 1.0,
                        "main_font_pt": 8.0, "note_font_pt": 7.5},
    "status": "Numerical and standalone bounds checks passed; final book page review pending"
})
dump("provenance.json", {
    "key": "regression-lasso-soft-threshold",
    "date": "2026-10-25",
    "source": "Deterministic teaching construction; no external experimental data",
    "reproduction": "python3 figures/07-classic-models/00-shared/matplotlib/regression-lasso-soft-threshold/generate.py",
    "inputs": {
        "figures/07-classic-models/00-shared/matplotlib/regression-lasso-soft-threshold/generate.py": sha(Path(__file__)),
        "figures/00-shared/academic-drawing/plot_style.py": sha(ROOT / "figures/00-shared/academic-drawing/plot_style.py")
    },
    "outputs": {
        "pdf": sha(OUT / "figure.pdf"), "svg": sha(OUT / "figure.svg"), "png": sha(OUT / "figure.png")
    },
    "randomness": "none",
    "data_and_objective": "data.json",
    "numerical_checks": "checks.json"
})
print("OK", dimensions)
