"""Deterministic teaching figure: real epsilon-SVR solution, tube and support vectors."""
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
from scipy.optimize import minimize

style.configure()
WIDTH_MM = 105.412
HEIGHT_MM = 78.0
EPS = 0.35
C = 100.0
BOUND = C / 10  # dual box upper bound C/n, n=10

def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

xs = np.arange(0.0, 5.0, 0.5)
offs = np.array([-0.50, 0.20, -0.10, 0.55, -0.30, 0.10, 0.45, -0.20, 0.60, -0.15])
ys = 1.0 + 0.7 * xs + offs
n = len(xs)
K = np.outer(xs, xs)

def dual_obj(v):
    a, b = v[:n], v[n:]
    d = a - b
    return 0.5 * d @ K @ d + EPS * (a.sum() + b.sum()) - ys @ d

res = minimize(dual_obj, np.zeros(2 * n), bounds=[(0.0, BOUND)] * (2 * n),
               constraints=({"type": "eq", "fun": lambda v: v[:n].sum() - v[n:].sum()}),
               method="SLSQP", options={"maxiter": 1000, "ftol": 1e-12})
assert res.success, res.message
alpha, alphastar = res.x[:n], res.x[n:]
w = float((alpha - alphastar) @ xs)
f = w * xs
bs = []
for i in range(n):
    if 1e-8 < alphastar[i] < BOUND - 1e-8:
        bs.append(ys[i] - f[i] + EPS)
    if 1e-8 < alpha[i] < BOUND - 1e-8:
        bs.append(ys[i] - f[i] - EPS)
b0 = float(np.mean(bs))
pred = w * xs + b0
r = ys - pred

# KKT classification
interior = np.abs(r) < EPS - 1e-6
free = (~interior) & ((alpha > 1e-6) | (alphastar > 1e-6)) & (np.maximum(alpha, alphastar) < BOUND - 1e-6)
sat = ~(interior | free)

# KKT assertions
assert np.allclose(alpha[interior], 0.0, atol=1e-5) and np.allclose(alphastar[interior], 0.0, atol=1e-5)
assert np.allclose(np.abs(r[free]), EPS, atol=1e-4)
assert np.allclose(np.maximum(alpha[sat], alphastar[sat]), BOUND, atol=1e-3)

fig, ax = plt.subplots(figsize=(WIDTH_MM / 25.4, HEIGHT_MM / 25.4))
xx = np.linspace(-0.5, 5.0, 50)
ax.fill_between(xx, w * xx + b0 - EPS, w * xx + b0 + EPS, color=style.BLUE_FILL, zorder=1)
ax.plot(xx, w * xx + b0, color=style.BLUE, lw=1.1, label=r"拟合 $f(x)$（由对偶解恢复）")
ax.plot(xx, w * xx + b0 + EPS, color=style.MUTED, lw=0.6, ls="--")
ax.plot(xx, w * xx + b0 - EPS, color=style.MUTED, lw=0.6, ls="--")
ax.scatter(xs[interior], ys[interior], s=22, color=style.BLUE, zorder=3, label="带内样本（乘子为零）")
ax.scatter(xs[free], ys[free], s=26, color=style.RED, zorder=3, label="带边界样本（$0<\\alpha<C/n$）")
ax.scatter(xs[sat], ys[sat], s=30, facecolors="none", edgecolors=style.RED, lw=1.1, zorder=3, label="带外样本（$\\alpha=C/n$）")
ax.set_xlabel("输入 $x$"); ax.set_ylabel("响应 $y$")
ax.legend(loc="upper left", fontsize=7.5, frameon=False)
ax.set_xlim(-0.5, 5.0); ax.set_ylim(0.2, 5.6)
ax.set_xticks([0, 1, 2, 3, 4, 5]); ax.set_yticks([1, 2, 3, 4, 5])

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

data = {"epsilon": EPS, "C_in_text": C, "n": n, "box_bound_C_over_n": BOUND, "offsets": offs.tolist(),
        "w": w, "b": b0, "n_interior": int(interior.sum()),
        "n_free": int(free.sum()), "n_saturated": int(sat.sum())}
dump("data.json", data)
dump("checks.json", {"key": "regression-svr-epsilon-tube", "numeric_checks": data,
                     "kkt": "interior alpha=0; free |resid|=eps and 0<alpha<C/n; saturated alpha=C/n",
                     "renderer_text_outside_canvas": outside})
dump("generation.json", {
    "key": "regression-svr-epsilon-tube", "route": "Matplotlib + scipy SLSQP dual solve",
    "generator": str(Path(__file__).resolve().relative_to(ROOT)),
    "generator_sha256": sha(Path(__file__)),
    "style": style.style_record(),
    "parameters": {"epsilon": EPS, "C_in_text": C, "n": n, "box_bound_C_over_n": BOUND, "n_points": n, "data": "deterministic offsets"},
    "software": {"python": platform.python_version(), "numpy": np.__version__, "matplotlib": matplotlib.__version__, "scipy": __import__("scipy").__version__},
    "current_display": {"asset": str((OUT / "figure.pdf").relative_to(ROOT)), "native_width_mm": WIDTH_MM,
                        "native_height_mm": HEIGHT_MM, "body_width_mm": WIDTH_MM, "scale": 1.0,
                        "main_font_pt": 8.0, "note_font_pt": 7.5},
    "status": "KKT assertions and standalone bounds checks passed; final book page review pending"
})
dump("provenance.json", {
    "key": "regression-svr-epsilon-tube",
    "date": "2026-10-25",
    "source": "Deterministic points; fitted line recovered by solving the epsilon-SVR dual QP (SLSQP)",
    "reproduction": "python3 figures/04-classic-models/00-shared/matplotlib/regression-svr-epsilon-tube/generate.py",
    "inputs": {
        "figures/04-classic-models/00-shared/matplotlib/regression-svr-epsilon-tube/generate.py": sha(Path(__file__)),
        "figures/00-shared/academic-drawing/plot_style.py": sha(ROOT / "figures/00-shared/academic-drawing/plot_style.py")
    },
    "outputs": {
        "pdf": sha(OUT / "figure.pdf"), "svg": sha(OUT / "figure.svg"), "png": sha(OUT / "figure.png")
    },
    "randomness": "none",
    "data_and_objective": "data.json",
    "numerical_checks": "checks.json"
})
print("OK", dimensions, "interior", int(interior.sum()), "free", int(free.sum()), "sat", int(sat.sum()))
