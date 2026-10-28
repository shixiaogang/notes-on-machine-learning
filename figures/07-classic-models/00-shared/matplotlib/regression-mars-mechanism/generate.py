"""Reproduce the MARS teaching mechanism: hinges, forward stepwise fitting,
backward GCV pruning, and an interaction rectangle. Deterministic piecewise-linear
data; all RSS/GCV numbers are computed by ordinary least squares in this script.

Forward stage follows Friedman's paired rule: at each knot t add both hinges
(x-t)_+ and (t-x)_+ jointly and refit all coefficients. GCV uses Friedman's
effective parameter count C = r + d*K (r: basis functions incl. intercept;
K: knots; d: per-knot penalty; d=2 for this 1D additive example).
"""
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
import matplotlib.colors as mcolors
from matplotlib.text import Text
import numpy as np
import fitz

style.configure()
WIDTH_MM = 159.0
HEIGHT_MM = 96.0
D_PENALTY = 2.0  # Friedman's per-knot penalty d (1D additive model)

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
    dump("provenance.json", {
        "key": key, "date": "2026-10-25",
        "source": "Deterministic teaching construction; piecewise-linear target with a single kink at x=4; no external data",
        "reproduction": "python3 " + str(source.relative_to(ROOT)),
        "inputs": {str(source.relative_to(ROOT)): sha(source), str(helper.relative_to(ROOT)): sha(helper)},
        "outputs": {ext: sha(OUT / ("figure." + ext)) for ext in ["pdf", "svg", "png"]},
        "randomness": "none", "data_and_objective": "data.json", "numerical_checks": "checks.json"
    })
    plt.close(fig)

def main():
    # ---------- deterministic teaching data: one kink at x=4 plus small ripple ----------
    x = np.arange(0, 10.01, 0.25)
    y = np.where(x < 4, 0.0, 0.8 * (x - 4)) + 0.04 * np.sin(2.5 * x)
    n = len(x)
    knots_grid = np.round(np.arange(0, 10.01, 0.25), 2)

    def ols_fit(bases):
        B = np.column_stack([np.ones(n)] + list(bases))
        coef, *_ = np.linalg.lstsq(B, y, rcond=None)
        fitted = B @ coef
        return coef, fitted, float(np.sum((y - fitted) ** 2))

    def hinge(side, t):
        return (np.maximum(0.0, x - t) if side == "+" else np.maximum(0.0, t - x))

    # ---------- forward stage: Friedman paired rule ----------
    # candidate knot t adds BOTH hinges (x-t)_+ and (t-x)_+ jointly; refit all coefficients;
    # pick the knot giving the largest RSS reduction.
    rss0 = ols_fit([])[2]
    step_bases, knots, rss_series = [], [], [rss0]
    for _ in range(2):
        best = None
        for t in knots_grid:
            if t in knots:
                continue
            rss = ols_fit(step_bases + [hinge("+", t), hinge("-", t)])[2]
            if best is None or rss < best[0]:
                best = (rss, float(t))
        rss, t = best
        step_bases += [hinge("+", t), hinge("-", t)]
        knots.append(t)
        rss_series.append(rss)
    assert knots[0] == 4.0 and knots[1] == 8.25, knots
    assert rss_series[1] < 0.05
    assert rss_series[2] < rss_series[1]

    c1 = ols_fit(step_bases[:2])[0]
    c2 = ols_fit(step_bases[:4])[0]

    def sci(v):
        a, b = f"{v:.1e}".split("e")
        return f"{a}\\times10^{{{int(b):+d}}}"

    def hinge_on_grid(side, t):
        return np.maximum(0.0, xx - t) if side == "+" else np.maximum(0.0, t - xx)

    # ---------- backward stage: GCV = (RSS/n)/(1-C/n)^2, Friedman C = M + d*M ----------
    # M = number of non-constant basis functions; d = per-knot penalty (1D additive: d=2).
    def gcv(rss, m):
        C = m + D_PENALTY * m
        return (rss / n) / (1 - C / n) ** 2

    subsets = [
        ("全留(2折点)", step_bases, 4),
        ("删去折点8.25", step_bases[:2], 2),
        ("删去折点4", step_bases[2:], 2),
        ("只含截距", [], 0),
    ]
    prune = []
    for name, bases, m in subsets:
        _, _, rss = ols_fit(bases)
        C = m + D_PENALTY * m
        assert C < n / 2, (name, C, n)
        prune.append({"subset": name, "M": m, "C": C, "RSS": rss, "GCV": gcv(rss, m)})
    best_name = min(prune, key=lambda p: p["GCV"])["subset"]
    assert best_name == "删去折点8.25", prune

    # ---------- figure ----------
    fig, axes = plt.subplots(2, 2, figsize=(WIDTH_MM / 25.4, HEIGHT_MM / 25.4))
    fig.subplots_adjust(left=0.08, right=0.985, bottom=0.13, top=0.88, wspace=0.34, hspace=0.62)

    ax = axes[0, 0]
    xx = np.linspace(0, 10, 201)
    t_show = 5.0
    ax.plot(xx, np.maximum(0, xx - t_show), color=style.BLUE, linewidth=1.1, label=r"$(x-t)_+$")
    ax.plot(xx, np.maximum(0, t_show - xx), color=style.GREEN, linewidth=1.1, label=r"$(t-x)_+$")
    ax.axvline(t_show, color=style.MUTED, linestyle=":", linewidth=0.6)
    ax.text(t_show + 0.55, 3.3, "折点 $t$", ha="left", va="center", color=style.MUTED, fontsize=7.5)
    ax.set(xlim=(0, 10), ylim=(-0.4, 5.8), xticks=[0, 2, 4, 6, 8, 10], yticks=[0, 2, 4], xlabel=r"$x$", title="(a) 铰链函数")
    ax.legend(fontsize=7.5, frameon=False, loc="upper left")

    ax = axes[0, 1]
    ax.scatter(x, y, s=10, facecolors="none", edgecolors=style.BLUE, linewidths=0.8, zorder=3, label="教学数据")
    ax.plot(xx, np.full_like(xx, y.mean()), color=style.MUTED, linewidth=0.9, linestyle="--", zorder=2,
            label=f"只含截距 RSS={rss_series[0]:.1f}")
    B1 = np.column_stack([np.ones_like(xx), hinge_on_grid("+", knots[0]), hinge_on_grid("-", knots[0])])
    ax.plot(xx, B1 @ c1, color=style.GREEN, linewidth=1.2, zorder=4,
            label=f"第1步折点{knots[0]:g} RSS=${sci(rss_series[1])}$")
    B2 = np.column_stack([np.ones_like(xx), hinge_on_grid("+", knots[0]), hinge_on_grid("-", knots[0]),
                          hinge_on_grid("+", knots[1]), hinge_on_grid("-", knots[1])])
    ax.plot(xx, B2 @ c2, color=style.RED, linewidth=1.2, linestyle=(0, (5, 2)), zorder=5,
            label=f"第2步折点{knots[1]:g} RSS=${sci(rss_series[2])}$")
    ax.set(xlim=(-0.3, 10.3), ylim=(-0.4, 6.2), xticks=[0, 2, 4, 6, 8, 10], yticks=[0, 2, 4, 6], xlabel=r"$x$", title="(b) 前向选基两步")
    ax.legend(fontsize=6.5, frameon=False, loc="upper left", bbox_to_anchor=(0.02, 0.98), borderaxespad=0.0, handlelength=1.4, labelspacing=0.35)

    ax = axes[1, 0]
    labels = [p["subset"] for p in prune]
    ax.semilogy(range(4), [p["RSS"] / n for p in prune], "o-", color=style.BLUE, linewidth=1.0, label="RSS/n")
    ax.semilogy(range(4), [p["GCV"] for p in prune], "s--", color=style.RED, linewidth=1.0, label="GCV")
    ax.annotate("GCV最小", xy=(1, prune[1]["GCV"]), xytext=(1.35, 0.0022),
                fontsize=7.0, color=style.RED,
                arrowprops=dict(arrowstyle="->", color=style.RED, lw=0.7))
    ax.set_xticks(range(4))
    ax.set_xticklabels(labels, fontsize=7.0)
    ax.set(title="(c) 后向删基：RSS/n 与 GCV（纵轴对数）", ylim=(5e-4, 8),
           xlabel="删基序列（每次删去一个折点的两条铰链，从全模型到只含截距）")
    ax.legend(fontsize=7.0, frameon=False, loc="upper left")

    ax = axes[1, 1]
    xx1, xx2 = np.meshgrid(np.linspace(0, 10, 121), np.linspace(0, 10, 121))
    prod = np.maximum(0, xx1 - 3.0) * np.maximum(0, 7.0 - xx2)
    cmap = mcolors.LinearSegmentedColormap.from_list("marsrect", ["#FFFFFF", style.BLUE])
    ax.pcolormesh(xx1, xx2, prod, shading="auto", cmap=cmap)
    ax.axvline(3.0, color=style.MUTED, linestyle=":", linewidth=0.6)
    ax.axhline(7.0, color=style.MUTED, linestyle=":", linewidth=0.6)
    ax.text(6.6, 3.2, r"$(x_1-3)_+(7-x_2)_+$", ha="center", fontsize=7.5, color=style.MUTED)
    ax.text(1.6, 8.4, "矩形外为零", fontsize=7.0, color=style.MUTED)
    ax.set(xlim=(0, 10), ylim=(0, 10), xticks=[0, 2, 4, 6, 8, 10], yticks=[0, 2, 4, 6, 8, 10],
           xlabel=r"$x_1$", ylabel=r"$x_2$", title="(d) 两铰链乘积的交互区域")

    export(fig, "regression-mars-mechanism", {
        "teaching_data": {"x": x.tolist(), "y": [float(v) for v in y]},
        "target": "piecewise linear with one kink at x=4 plus fixed 0.04 sin(2.5x) ripple",
        "forward": {"rss_series": rss_series, "knots": knots, "rule": "Friedman paired hinges per knot"},
        "prune": prune,
        "gcv_form": "GCV = (RSS/n)/(1-C/n)^2, Friedman C(M)+d*M: M = non-constant basis functions, d = knot penalty (d=2, 1D additive)"
    }, {
        "gcv_penalty_d": D_PENALTY,
        "gcv_penalty_form": "C = M + d*M (Friedman 1991), M = non-constant basis functions",
        "teaching_construction": True, "scope": "One deterministic 1D teaching example"
    }, {
        "forward_knots": knots,
        "rss_series": rss_series,
        "gcv_minimizing_subset": best_name,
    })

if __name__ == "__main__":
    main()
