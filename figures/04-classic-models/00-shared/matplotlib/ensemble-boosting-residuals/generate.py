"""Reproduce a deterministic teaching figure from exact numerical inputs."""
from pathlib import Path
import hashlib
import json
import os
import platform
import sys
import tempfile

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "build.sh").is_file())
OUT = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", tempfile.mkdtemp(prefix=OUT.name + "-mpl-"))
sys.path.insert(0, str(ROOT / "figures/00-shared/academic-drawing"))
import plot_style as style
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.text import Text
import numpy as np
import fitz

style.configure()
WIDTH_MM = 159.0
HEIGHT_MM = 72.0

def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def export(fig, key, data, parameters, checks):
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
    with fitz.open(OUT / "figure.pdf") as doc:
        page = doc[0]
        dimensions = [page.rect.width * 25.4 / 72, page.rect.height * 25.4 / 72]
        pdf_fonts = sorted({f[3] for f in page.get_fonts(full=True)})
        assert len(doc) == 1
        assert np.allclose(dimensions, [WIDTH_MM, HEIGHT_MM], atol=0.01)
    source = Path(__file__).resolve()
    helper = Path(style.__file__).resolve()
    dump("data.json", data)
    dump("checks.json", {"key": key, "numeric_checks": checks, "renderer_text_outside_canvas": outside})
    dump("generation.json", {
        "key": key, "route": "Matplotlib",
        "generator": str(source.relative_to(ROOT)),
        "generator_sha256": sha(source),
        "style_helper": str(helper.relative_to(ROOT)),
        "style_helper_sha256": sha(helper),
        "style": style.style_record(), "parameters": parameters,
        "software": {"python": platform.python_version(), "numpy": np.__version__, "matplotlib": matplotlib.__version__},
        "current_display": {
            "asset": str((OUT / "figure.pdf").relative_to(ROOT)),
            "native_width_mm": WIDTH_MM, "native_height_mm": HEIGHT_MM,
            "body_width_mm": WIDTH_MM, "scale": 1.0,
            "main_font_pt": 8.0, "note_font_pt": 7.5
        },
        "status": "Numerical and standalone bounds checks passed; final book page review pending"
    })
    dump("font-and-page-check.json", {
        "key": key, "physical_size_mm": dimensions, "actual_pdf_fonts": pdf_fonts,
        "body_width_mm": WIDTH_MM, "scale": 1.0, "main_font_pt_at_book_size": 8.0,
        "note_font_pt_at_book_size": 7.5, "renderer_text_outside_canvas": outside,
        "final_book_page_review": "pending full book build"
    })
    dump("provenance.json", {
        "key": key, "date": "2026-10-12",
        "source": "Deterministic teaching construction; no external experimental data",
        "reproduction": "python3 " + str(source.relative_to(ROOT)),
        "inputs": {str(source.relative_to(ROOT)): sha(source), str(helper.relative_to(ROOT)): sha(helper)},
        "outputs": {ext: sha(OUT / ("figure." + ext)) for ext in ["pdf", "svg", "png"]},
        "randomness": "none", "data_and_objective": "data.json", "numerical_checks": "checks.json"
    })
    dump("review.json", {
        "key": key, "science": "Exact input, projections or update, and objective independently asserted in source",
        "standalone_visual_review": "pending", "book_page_visual_review": "pending",
        "scope": "Teaching calculation; no population-risk or arbitrary-loss guarantee"
    })
    plt.close(fig)

def main():
    x = np.arange(6, dtype=float)
    y = np.array([0., 0., 1., 3., 4., 4.])
    f0 = np.full(len(x), y.mean())
    residual = y - f0
    thresholds = (x[:-1] + x[1:]) / 2
    fits, sse = [], []
    for threshold in thresholds:
        left = x <= threshold
        fitted = np.where(left, residual[left].mean(), residual[~left].mean())
        fits.append(fitted)
        sse.append(float(np.sum((residual - fitted) ** 2)))
    selected = int(np.argmin(sse))
    threshold, h1 = thresholds[selected], fits[selected]
    eta = 0.6
    f1 = f0 + eta * h1
    j0, j1 = [float(np.mean((y - f) ** 2) / 2) for f in [f0, f1]]
    assert threshold == 2.5
    assert np.allclose(h1, [-5/3] * 3 + [5/3] * 3)
    assert np.allclose(f1, [1] * 3 + [3] * 3)
    assert np.allclose([j0, j1], [1.5, 1/3])
    assert j1 < j0
    fig, axes = plt.subplots(1, 3, figsize=(WIDTH_MM / 25.4, HEIGHT_MM / 25.4))
    fig.subplots_adjust(left=0.055, right=0.988, bottom=0.31, top=0.84, wspace=0.39)
    targets = [y, residual, y]
    fitted = [f0, h1, f1]
    titles = ["(a) 现有预测", "(b) 拟合普通残差", "(c) 加法更新"]
    bottom = [r"$J_0=1.5$", r"$\eta=0.6$", r"$J_1=1/3$"]
    for i, (ax, target, fit, title, text) in enumerate(zip(axes, targets, fitted, titles, bottom)):
        ax.scatter(x, target, s=14, color=style.BLUE, zorder=3)
        for xx, yy, ff in zip(x, target, fit):
            ax.plot([xx, xx], [yy, ff], color=style.RED, linestyle="--", linewidth=0.6)
        if i == 0:
            ax.plot([-0.35, 5.35], [2, 2], color=style.GREEN)
        else:
            ax.plot([-0.35, threshold, threshold, 5.35], [fit[0], fit[0], fit[-1], fit[-1]], color=style.GREEN)
            ax.axvline(threshold, color=style.MUTED, linestyle=":", linewidth=0.6)
        ax.set(xlim=(-0.35, 5.35), ylim=(-2.5, 2.5) if i == 1 else (-0.5, 4.5), xlabel=r"$x$")
        ax.set_ylabel(r"$r^{(1)},h_1$" if i == 1 else r"$y,F$")
        ax.set_xticks([0, 2, 4])
        ax.set_yticks([-2, 0, 2] if i == 1 else [0, 2, 4])
        ax.set_title(title, pad=7)
        ax.text(0.5, -0.31, text, transform=ax.transAxes, ha="center", va="center")
    handles = [
        Line2D([], [], color=style.BLUE, marker="o", linestyle="None", markersize=3, label="本面板的拟合目标"),
        Line2D([], [], color=style.GREEN, linestyle="-", label="本面板的拟合函数"),
        Line2D([], [], color=style.RED, linestyle="--", linewidth=0.6, label="两者的差")
    ]
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.005), ncol=3, columnspacing=1.5)
    export(fig, "ensemble-boosting-residuals", {
        "x": x.tolist(), "y": y.tolist(), "F0": f0.tolist(), "ordinary_residual": residual.tolist(),
        "candidate_thresholds": thresholds.tolist(), "candidate_residual_SSE": sse,
        "selected_threshold": float(threshold), "h1": h1.tolist(), "learning_rate": eta,
        "F1": f1.tolist(), "J0": j0, "J1": j1
    }, {
        "loss": "ell(y,F)=0.5*(y-F)^2", "objective": "J=mean(ell)",
        "initialization": "Empirical mean response", "member": "Least-squares regression stump over all consecutive-x midpoints",
        "update": "F1=F0+eta*h1, eta=0.6; whole-tree line-search coefficient is 1",
        "teaching_construction": True, "scope": "One exact squared-loss teaching update; not an arbitrary-loss or new-sample guarantee"
    }, {"best_threshold_is_2_5": True, "leaves_are_minus_and_plus_5_over_3": True,
        "updated_predictions_are_1_and_3": True, "losses_are_1_5_and_1_over_3": True,
        "squared_loss_decreases_in_this_update": True})

if __name__ == "__main__":
    main()
