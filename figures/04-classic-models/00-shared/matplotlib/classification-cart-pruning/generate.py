"""Cost-complexity pruning: candidate-subtree cost envelope and validation choice (teaching construction)."""
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
import numpy as np
import fitz

style.configure()
WIDTH_MM = 159.0
HEIGHT_MM = 66.0

def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

# Teaching construction: candidate pruned subtrees T0..T3 from one grown tree T0.
# (number of leaves L, training misclassification fraction Rhat)
TREES = [
    ("$T_0$", 4, 0.10),
    ("$T_1$", 3, 0.12),
    ("$T_2$", 2, 0.16),
    ("$T_3$", 1, 0.30),
]
# Adjacent breakpoints where J_alpha equal: R_i + L_i a = R_{i+1} + L_{i+1} a
BREAKS = []
for (n1, L1, r1), (n2, L2, r2) in zip(TREES, TREES[1:]):
    BREAKS.append((r1 - r2) / (L2 - L1))
# Validation error (teaching U-shape), sampled at the four regime midpoints.
VAL_X = np.array([0.0, 0.02, 0.04, 0.07, 0.14])
VAL_Y = np.array([0.20, 0.165, 0.155, 0.18, 0.30])
ALPHA_STAR = 0.04

def export(fig, data, parameters, checks):
    style.prepare_figure(fig)
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    from matplotlib.text import Text
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
    dump("checks.json", {"key": "classification-cart-pruning", "numeric_checks": checks,
                         "renderer_text_outside_canvas": outside})
    dump("generation.json", {
        "key": "classification-cart-pruning", "route": "Matplotlib",
        "generator": str(source.relative_to(ROOT)), "generator_sha256": sha(source),
        "style_helper": str(helper.relative_to(ROOT)), "style_helper_sha256": sha(helper),
        "style": style.style_record(), "parameters": parameters,
        "software": {"python": platform.python_version(), "numpy": np.__version__,
                     "matplotlib": matplotlib.__version__},
        "current_display": {"asset": str((OUT / "figure.pdf").relative_to(ROOT)),
                             "native_width_mm": WIDTH_MM, "native_height_mm": HEIGHT_MM,
                             "body_width_mm": WIDTH_MM, "scale": 1.0,
                             "main_font_pt": 8.0, "note_font_pt": 7.5},
        "status": "Numerical and standalone bounds checks passed; final book page review pending"})
    dump("font-and-page-check.json", {
        "key": "classification-cart-pruning", "physical_size_mm": dimensions,
        "actual_pdf_fonts": pdf_fonts, "body_width_mm": WIDTH_MM, "scale": 1.0,
        "main_font_pt_at_book_size": 8.0, "note_font_pt_at_book_size": 7.5,
        "renderer_text_outside_canvas": outside, "final_book_page_review": "pending full book build"})
    dump("provenance.json", {
        "key": "classification-cart-pruning", "date": "2026-10-25",
        "source": "Deterministic teaching construction; no external experimental data",
        "reproduction": "python3 " + str(source.relative_to(ROOT)),
        "inputs": {str(source.relative_to(ROOT)): sha(source), str(helper.relative_to(ROOT)): sha(helper)},
        "outputs": {ext: sha(OUT / ("figure." + ext)) for ext in ["pdf", "svg", "png"]},
        "randomness": "none", "data_and_objective": "data.json", "numerical_checks": "checks.json"})
    dump("review.json", {
        "key": "classification-cart-pruning",
        "science": "Adjacent-subtree cost equality solved analytically and asserted; validation curve is illustrative",
        "standalone_visual_review": "pending", "book_page_visual_review": "pending",
        "scope": "Teaching pruning sequence; no population-risk guarantee"})
    plt.close(fig)

def main():
    # Assert breakpoints.
    assert np.allclose(BREAKS, [0.02, 0.04, 0.14]), BREAKS
    # At a breakpoint, adjacent costs are equal.
    for a, (n1, L1, r1), (n2, L2, r2) in zip(BREAKS, TREES, TREES[1:]):
        assert abs((r1 + L1 * a) - (r2 + L2 * a)) < 1e-12
    assert abs(ALPHA_STAR - BREAKS[1]) < 1e-12

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(WIDTH_MM / 25.4, HEIGHT_MM / 25.4))
    fig.subplots_adjust(left=0.085, right=0.985, bottom=0.20, top=0.86, wspace=0.30)
    a = np.linspace(0, 0.18, 400)
    # Panel (a): J_alpha lines and lower envelope.
    costs = []
    for (name, L, r), c in zip(TREES, [style.MUTED] * 4):
        J = r + L * a
        costs.append(J)
        ax1.plot(a, J, color=c, linewidth=0.8, linestyle="--")
    costs = np.array(costs)
    envelope = costs.min(axis=0)
    ax1.plot(a, envelope, color=style.BLUE, linewidth=1.6)
    for bx in BREAKS:
        ax1.axvline(bx, color=style.MUTED, linewidth=0.6, linestyle=":")
    bbox = dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85)
    ax1.text(0.02, 0.10, "α=0.02", fontsize=7.5, ha="center", va="bottom", color=style.MUTED, bbox=bbox)
    ax1.text(0.04, 0.60, "α=0.04", fontsize=7.5, ha="center", va="bottom", color=style.MUTED, bbox=bbox)
    ax1.text(0.14, 0.60, "α=0.14", fontsize=7.5, ha="center", va="bottom", color=style.MUTED, bbox=bbox)
    ax1.set(xlim=(0, 0.18), ylim=(0.08, 0.62), xlabel=r"剪枝参数 α", ylabel=r"代价 $J_\alpha(T)$")
    ax1.set_yticks([0.1, 0.3, 0.5])
    ax1.set_xticks([0, 0.05, 0.10, 0.15])
    ax1.set_title("(a) 各候选子树代价与下包络", fontsize=8, pad=6)
    from matplotlib.lines import Line2D
    handles = [Line2D([], [], color=style.MUTED, linestyle="--", linewidth=0.8,
                      label="候选子树 $J_\\alpha(T)$"),
               Line2D([], [], color=style.BLUE, linewidth=1.6, label="最优子树下包络")]
    ax1.legend(handles=handles, fontsize=7.0, loc="lower right", frameon=False)

    # Panel (b): optimal subtree is piecewise-constant on each regime.
    # Regime edges: [0,0.02)->T0, [0.02,0.04)->T1, [0.04,0.14)->T2, [0.14,0.18]->T3.
    edges = [0.0, 0.02, 0.04, 0.14, 0.18]
    train_err = [t[2] for t in TREES]                      # Rhat(T_k)
    val_err = [0.22, 0.19, 0.18, 0.33]                    # teaching validation per subtree
    chosen_regime = 2                                      # T2 has minimum validation error
    # Shade the chosen regime.
    ax2.axvspan(edges[chosen_regime], edges[chosen_regime + 1], color=style.GREEN, alpha=0.08)
    for k in range(4):
        ax2.hlines(train_err[k], edges[k], edges[k + 1], color=style.MUTED, linewidth=1.2)
        ax2.hlines(val_err[k], edges[k], edges[k + 1], color=style.RED, linewidth=1.2)
        xmid = (edges[k] + edges[k + 1]) / 2
        ax2.plot(xmid, train_err[k], color=style.MUTED, marker="o", markersize=3)
        ax2.plot(xmid, val_err[k], color=style.RED, marker="s", markersize=3)
    ax2.text((edges[chosen_regime] + edges[chosen_regime + 1]) / 2, 0.35,
             r"验证最小，选 $\alpha^*$", fontsize=7.5, ha="center", color=style.GREEN)
    ax2.set(xlim=(0, 0.18), ylim=(0.05, 0.37), xlabel=r"剪枝参数 α（每段对应一棵最优子树）",
            ylabel="误分类率")
    ax2.set_yticks([0.1, 0.2, 0.3])
    ax2.set_xticks([0, 0.05, 0.10, 0.15])
    ax2.set_title("(b) 分段常值：训练误差上升，验证误差取最小", fontsize=8, pad=6)
    h2 = [Line2D([], [], color=style.MUTED, marker="o", markersize=3, linewidth=1.2,
                 label=r"训练误差 $\hat R(T_k)$"),
          Line2D([], [], color=style.RED, marker="s", markersize=3, linewidth=1.2,
                 label=r"验证误差（教学）")]
    ax2.legend(handles=h2, fontsize=7.0, loc="lower right", frameon=False)

    export(fig, {
        "candidate_subtrees": [{"name": n, "leaves": L, "training_error": r} for n, L, r in TREES],
        "regime_edges_alpha": edges,
        "optimal_subtree_per_regime": ["T0", "T1", "T2", "T3"],
        "training_error_per_regime": train_err,
        "validation_error_per_regime_teaching": val_err,
        "breakpoint_formula": "alpha_k = (Rhat(T_{k+1}) - Rhat(T_k)) / (|L(T_k)| - |L(T_{k+1})|)",
        "chosen_regime": 2, "chosen_subtree": "T2"},
        {"cost": "J_alpha(T)=Rhat(T)+alpha*|L(T)|",
         "breakpoints": "adjacent-subtree cost equality alpha_k=(Rhat(T_{k+1})-Rhat(T_k))/(|L(T_k)|-|L(T_{k+1})|)",
         "plot_style": "piecewise-constant: each regime [edges[k],edges[k+1]) is optimal subtree T_k",
         "validation": "teaching constant per subtree; minimum on T2 regime",
         "teaching_construction": True},
        {"breakpoints_are_0_02_0_04_0_14": True,
         "adjacent_costs_equal_at_each_breakpoint": True,
         "validation_error_minimum_is_on_T2_regime": val_err.index(min(val_err)) == 2,
         "training_errors_are_nondecreasing": all(train_err[k] <= train_err[k + 1] for k in range(3))})

if __name__ == "__main__":
    main()
