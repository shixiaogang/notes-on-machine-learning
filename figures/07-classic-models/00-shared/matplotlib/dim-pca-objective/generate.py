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
    angle = np.deg2rad(30.0)
    rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    unrotated = np.array([[u, v] for u in [-2.0, -1.0, 1.0, 2.0] for v in [-0.5, 0.5]])
    raw = unrotated @ rotation.T
    center = raw.mean(axis=0)
    x = raw - center
    _, singular_values, vh = np.linalg.svd(x, full_matrices=False)
    principal = vh[0].copy()
    if principal[0] < 0:
        principal *= -1
    directions = [np.array([1.0, 0.0]), principal]
    projections = [(x @ w)[:, None] * w for w in directions]
    losses = [float(np.mean(np.sum((x - proj) ** 2, axis=1))) for proj in projections]
    variances = [float(np.mean((x @ w) ** 2)) for w in directions]
    eigenvalues = singular_values ** 2 / len(x)
    assert np.allclose(center, 0)
    assert np.allclose(principal, rotation[:, 0])
    assert np.allclose(eigenvalues, [2.5, 0.25])
    assert np.allclose(losses, [0.8125, 0.25])
    assert np.allclose(np.array(losses) + variances, np.mean(np.sum(x ** 2, axis=1)))
    fig, axes = plt.subplots(1, 2, figsize=(WIDTH_MM / 25.4, HEIGHT_MM / 25.4))
    fig.subplots_adjust(left=0.065, right=0.985, bottom=0.31, top=0.84, wspace=0.24)
    titles = ["(a) 水平方向", "(b) 第一主方向（SVD）"]
    for ax, w, proj, title, loss in zip(axes, directions, projections, titles, losses):
        line = np.array([-2.7, 2.7])[:, None] * w
        ax.plot(line[:, 0], line[:, 1], color=style.GREEN, linewidth=1.1)
        for a, b in zip(x, proj):
            ax.plot([a[0], b[0]], [a[1], b[1]], color=style.RED, linestyle="--", linewidth=0.6)
        ax.scatter(x[:, 0], x[:, 1], s=14, color=style.BLUE, zorder=3)
        ax.scatter(proj[:, 0], proj[:, 1], s=18, facecolors="white", edgecolors=style.GREEN, linewidths=0.8, zorder=4)
        ax.set(xlim=(-2.5, 2.5), ylim=(-1.8, 1.8), xlabel=r"$x_1$", ylabel=r"$x_2$")
        ax.set_aspect("equal", adjustable="box")
        ax.set_xticks([-2, 0, 2])
        ax.set_yticks([-1, 0, 1])
        ax.set_title(title, pad=7)
        ax.text(0.5, -0.32, f"$J={loss:.4f}$", transform=ax.transAxes, ha="center", va="center")
    handles = [
        Line2D([], [], color=style.BLUE, marker="o", linestyle="None", markersize=3, label="观测"),
        Line2D([], [], color=style.GREEN, marker="o", markerfacecolor="white", linestyle="-", markersize=3, label="投影与重构"),
        Line2D([], [], color=style.RED, linestyle="--", linewidth=0.6, label="正交残差")
    ]
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.005), ncol=3, columnspacing=2.0)
    export(fig, "dim-pca-objective", {
        "unrotated_points": unrotated.tolist(), "rotation_degrees": 30.0,
        "points": raw.tolist(), "sample_mean": center.tolist(), "centered_points": x.tolist(),
        "svd_singular_values": singular_values.tolist(), "sample_covariance": (x.T @ x / len(x)).tolist(),
        "sample_eigenvalues": eigenvalues.tolist(), "directions": [w.tolist() for w in directions],
        "reconstructions": [proj.tolist() for proj in projections], "mean_squared_reconstruction_error": losses,
        "retained_variance": variances, "total_variance": float(np.mean(np.sum(x ** 2, axis=1)))
    }, {
        "sample_count": 8, "input_dimension": 2, "output_dimension": 1,
        "objective": "J(w)=mean(||x_i-(x_i^T w)w||_2^2), ||w||_2=1",
        "principal_direction": "Computed by numpy.linalg.svd, sign normalized to positive first coordinate",
        "teaching_construction": True
    }, {"mean_zero": True, "svd_direction_matches_30_degree_rotation": True,
        "eigenvalues_2_5_and_0_25": True, "errors_0_8125_and_0_25": True,
        "retained_variance_plus_error_equals_total_variance": True})

if __name__ == "__main__":
    main()
