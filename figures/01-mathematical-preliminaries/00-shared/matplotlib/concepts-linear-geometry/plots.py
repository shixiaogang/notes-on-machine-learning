"""Analytic teaching figures for dual norms, spectral gaps and strip geometry.

Run with Python, NumPy and Matplotlib. Fonts are loaded from the repository;
no TeX, numerical optimization, random sampling or external dataset is used.
"""
from pathlib import Path
import json
import hashlib
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT / 'figures/00-shared'))
from resource_paths import asset_path
sys.path.insert(0, str(ROOT / 'figures/01-mathematical-preliminaries/00-shared/matplotlib'))
from plot_style import (BLUE, RED, YELLOW, INK, MUTED, BLUE_FILL,
                        configure, prepare_figure, style_record)

GRAY = MUTED
configure()
RECORDS = []


def prepare_axes(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(width=.6, length=3, labelsize=8)


def save(fig, name, facts):
    prepare_figure(fig)
    exports = []
    for extension in ("pdf", "svg", "png"):
        output = asset_path(OUT, f"{name}.{extension}")
        fig.savefig(output, dpi=360)
        exports.append({"path": output.name,
                        "sha256": hashlib.sha256(output.read_bytes()).hexdigest()})
    RECORDS.append({"name": name, "teaching_construction": True,
        "source": "Exact expressions and finite-dimensional examples in chapters 6–8.",
        "width_mm": float(fig.get_size_inches()[0] * 25.4),
        "height_mm": float(fig.get_size_inches()[1] * 25.4),
        "exports": exports, **facts})
    plt.close(fig)


def dual_balls():
    fig, axs = plt.subplots(1, 3, figsize=(169 / 25.4, 65 / 25.4),
                            layout="constrained")
    angle = np.linspace(0, 2 * np.pi, 721)
    curves = [np.array([[1, 0, -1, 0, 1], [0, 1, 0, -1, 0]]),
              np.array([np.cos(angle), np.sin(angle)]),
              np.array([[-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1]])]
    maxima = [2., np.sqrt(5), 3.]
    witnesses = [np.array([1., 0.]), np.array([2., -1.]) / np.sqrt(5),
                 np.array([1., -1.])]
    for ax, curve, maximum, witness, color, name, value in zip(
            axs, curves, maxima, witnesses, (BLUE, RED, YELLOW),
            (r"(a) $\|r\|_1\leq1$", r"(b) $\|r\|_2\leq1$",
             r"(c) $\|r\|_\infty\leq1$"), ("2", r"\sqrt{5}", "3")):
        prepare_axes(ax)
        ax.fill(*curve, color=color, alpha=.12)
        ax.plot(*curve, color=color)
        x = np.linspace(-1.3, 1.3, 301)
        ax.plot(x, 2*x - maximum, ls="--", color=GRAY, lw=.6)
        ax.scatter(*witness, s=24, color=INK, zorder=3)
        ax.annotate(r"$r_* $", xy=witness, xytext=(-23, 10),
                    textcoords="offset points", fontsize=9)
        ax.set(title=name, xlabel=r"$r_1$", ylabel=r"$r_2$",
               xlim=(-1.35, 1.35), ylim=(-1.35, 1.35), aspect="equal",
               xticks=[-1, 0, 1], yticks=[-1, 0, 1])
        ax.text(.02, .96, rf"$h={value}$", transform=ax.transAxes,
                va="top", fontsize=9)
    save(fig, "linear-dual-unit-balls", {
        "question": "How does the same linear functional change under different perturbation budgets?",
        "formula": "max(2*r1-r2) over each unit ball; support line 2*r1-r2=h",
        "parameters": {"z": [2, -1], "p": [1, 2, "infinity"],
            "positive_maxima": maxima,
            "maximizers": [r.tolist() for r in witnesses]},
        "sampling": "721 uniform circle angles, exact polygon vertices; common equal axes.",
        "design": "Three equally scaled unit balls; only boundary, supporting line and maximizer are shown.",
    })


def gap_direction():
    epsilon = .02
    gamma = np.logspace(-3, 0, 501)
    shift = np.sqrt((gamma/2)**2 + epsilon**2) - gamma/2
    degrees = np.rad2deg(.5 * np.arctan2(2*epsilon, gamma))
    assert np.all(shift <= epsilon)
    fig, axs = plt.subplots(2, 1, figsize=(112/25.4, 91/25.4),
                            sharex=True, layout="constrained")
    for ax in axs:
        prepare_axes(ax)
        ax.set_xscale("log")
        ax.set_xlim(1.e-3, 1.)
    axs[0].plot(gamma, shift, color=YELLOW)
    axs[0].axhline(epsilon, color=GRAY, ls="--", lw=.6)
    axs[0].set(ylabel=r"特征值增量 $\Delta\lambda_{\max}$",
               ylim=(0, .023), yticks=[0, .01, .02])
    axs[0].text(.64, .82, r"$\|E\|_2=0.02$", transform=axs[0].transAxes,
                va="top", fontsize=9)
    axs[1].plot(gamma, degrees, color=YELLOW)
    axs[1].set(xlabel=r"原始谱隙 $\gamma$", ylabel=r"方向转角 $\theta$（度）",
               ylim=(0, 47), yticks=[0, 15, 30, 45])
    save(fig, "matrix-gap-direction", {
        "question": "Can small eigenvalue changes coexist with large changes in the corresponding direction?",
        "formulas": ["A=diag(1+gamma,1); E=[[0,epsilon],[epsilon,0]]",
            "delta_lambda_max=sqrt((gamma/2)^2+epsilon^2)-gamma/2",
            "theta=0.5*atan2(2*epsilon,gamma)"],
        "parameters": {"epsilon": epsilon, "gamma_range": [.001, 1.]},
        "sampling": "501 logarithmically spaced gamma; exact analytic expressions; angles displayed in degrees.",
        "design": "Stacked panels share the spectral-gap axis; different outputs retain separate units.",
    })


def strip_geometry():
    radius, width = 2., .3
    theta = np.pi/2 + np.linspace(-.6, .6, 401)
    fig, axs = plt.subplots(2, 1, figsize=(112/25.4, 104/25.4),
                            layout="constrained")
    # The strip is open. Dashed curves mark its excluded radial boundaries.
    for ax in axs:
        prepare_axes(ax)
        polygon = np.vstack((np.column_stack(((radius-width)*np.cos(theta),
                        (radius-width)*np.sin(theta))),
                        np.column_stack(((radius+width)*np.cos(theta[::-1]),
                        (radius+width)*np.sin(theta[::-1])))))
        ax.fill(*polygon.T, color=BLUE_FILL)
        for r in (radius-width, radius+width):
            ax.plot(r*np.cos(theta), r*np.sin(theta), color=GRAY, ls="--", lw=.6)
        ax.set(xlabel="环境第一坐标", ylabel="环境第二坐标",
               xlim=(-1.48, 1.48), ylim=(1.2, 2.6), aspect="equal",
               xticks=[-1, 0, 1], yticks=[1.5, 2, 2.5])
    axs[0].plot(radius*np.cos(theta), radius*np.sin(theta), color=YELLOW)
    p = np.array([0., radius])
    axs[0].scatter(*p, s=23, color=INK, zorder=5)
    for endpoint, text, color in [([-.65, 2.], r"$\partial_s\Phi$", BLUE),
                                ([0., 2.55], r"$\partial_u\Phi$", RED)]:
        axs[0].annotate("", xy=endpoint, xytext=p,
            arrowprops={"arrowstyle": "->", "color": color, "linewidth": 1.1})
        offset = (4, -6) if color == RED else (-8, 5)
        axs[0].annotate(text, xy=endpoint, xytext=offset,
                       textcoords="offset points", fontsize=9)
    axs[0].annotate(r"$p$", xy=p, xytext=(-15, -14), textcoords="offset points")
    axs[0].text(.02, .95, "(a) 中心线与二维带", transform=axs[0].transAxes, va="top")
    arc = np.pi/2 + np.linspace(-.2, .2, 181)
    for u, color, style, label in [(-.25, BLUE, "-", "内侧：0.7"),
                                 (.25, RED, "-", "外侧：0.9")]:
        r = radius + u
        axs[1].plot(r*np.cos(arc), r*np.sin(arc), color=color, ls=style)
        axs[1].scatter(r*np.cos(arc[[0,-1]]), r*np.sin(arc[[0,-1]]),
                       s=18, color=color)
        xy = np.array([r*np.cos(np.pi/2-.2), r*np.sin(np.pi/2-.2)])
        axs[1].annotate(label, xy=xy, xytext=(10, 1),
                       textcoords="offset points", fontsize=9)
    for t in (np.pi/2-.2, np.pi/2+.2):
        axs[1].plot(np.array([radius-width, radius+width])*np.cos(t),
                    np.array([radius-width, radius+width])*np.sin(t),
                    color=GRAY, lw=.6)
    axs[1].text(.02, .95, r"(b) 同一 $\Delta s=0.8$", transform=axs[1].transAxes, va="top")
    save(fig, "geometry-strip-tangent-coordinates", {
        "question": "Which directions belong to the modeled object, and how do coordinate increments become geometric lengths?",
        "formula": "Phi(s,u)=((R+u)*cos(s/R),(R+u)*sin(s/R)); arc length=(1+u/R)*delta_s",
        "parameters": {"R": radius, "w": width, "u": [-.25, .25],
                       "delta_s": .8, "arc_lengths": [.7, .9],
                       "angle_domain": [float(np.pi/2-.6), float(np.pi/2+.6)]},
        "sampling": "401 background angles,181 arc points; exact equal-aspect coordinates; no noise.",
        "design": "Two stacked equal-scale geometry panels avoid compressing the tangent labels; dashed boundaries are excluded.",
    })


if __name__ == "__main__":
    for build in (dual_balls, gap_direction, strip_geometry):
        build()
    (asset_path(OUT, "sources.json")).write_text(json.dumps({
        "created": "2026-10-06", "software": {"matplotlib": matplotlib.__version__,
        "numpy": np.__version__}, "fonts": {"Chinese": "LXGWWenKai-Regular.ttf",
        "Latin": "SourceSans3-Regular.otf", "mathtext": "STIX",
        "PDF_embedding": "Type 3 vector glyphs; CFF text fonts are not exported as Type 42",
        "SVG_embedding": "Paths"},
        "palette": {"blue": BLUE, "red": RED, "yellow": YELLOW},
        "shared_style": style_record(),
        "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "shared_style_sha256": hashlib.sha256((ROOT / 'figures/01-mathematical-preliminaries/00-shared/matplotlib/plot_style.py').read_bytes()).hexdigest(),
        "figures": RECORDS}, ensure_ascii=False, indent=2), encoding="utf-8")
