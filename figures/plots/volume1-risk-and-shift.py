"""Rebuild four teaching figures at their final book dimensions.

Run from any directory: python figures/plots/volume1-risk-and-shift.py
Dependencies: Python 3.11+, NumPy, Matplotlib (versions saved in metadata).
All inputs are explicit teaching constructions, not experimental observations.
The two qualitative trajectories preserve the original cubic Bezier paths.
PDF/SVG contain vector paths and embedded/subset font outlines; PNG is a preview.
"""
from pathlib import Path
import csv
import json
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import PercentFormatter
from matplotlib.transforms import offset_copy
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
for name in ("SourceSans3-Regular.otf", "LXGWWenKai-Regular.ttf", "STIXTwoText-Regular.otf"):
    font_manager.fontManager.addfont(ROOT / "fonts" / name)
plt.rcParams.update({
    "font.family": ["Source Sans 3", "LXGW WenKai"],
    "font.size": 8.5, "font.weight": "normal", "axes.labelweight": "normal",
    "mathtext.fontset": "stix", "pdf.fonttype": 3, "ps.fonttype": 3,
    "svg.fonttype": "path", "axes.linewidth": .9,
    "text.color": "#222222", "axes.edgecolor": "#444444",
    "axes.labelcolor": "#222222", "xtick.color": "#444444", "ytick.color": "#444444",
    "xtick.labelsize": 8, "ytick.labelsize": 8,
    "xtick.major.width": .6, "ytick.major.width": .6,
})
BLUE, RED, YELLOW, GRAY = "#7998AD", "#D57B70", "#D6B35D", "#747A80"
META = {"python": sys.version.split()[0], "matplotlib": matplotlib.__version__,
        "numpy": np.__version__, "fonts": ["SourceSans3-Regular.otf", "LXGWWenKai-Regular.ttf"],
        "mathtext": "stix", "pdf_font_encoding": "Type3 vector glyph programs: avoids CFF OpenType blank-glyph rendering in Type42; original fonts unchanged", "origin": "Explicit teaching constructions; no empirical data",
        "sources": ["tex/02-foundations/02-learning-theory/01-statistical-learning-framework.tex",
                    "tex/02-foundations/02-learning-theory/05-deep-learning-theory.tex",
                    "tex/02-foundations/02-learning-theory/06-transfer-learning-theory.tex"],
        "processing": "No filtering, missing values, random generation, aggregation or inference",
        "palette": {"blue": BLUE, "red": RED, "yellow": YELLOW, "neutral": GRAY},
        "figures": {}}


def canvas(width=112, height=64):
    return plt.figure(figsize=(width/25.4, height/25.4), facecolor="white")


def clean_axes(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(length=2.5, pad=2)


def save(fig, name, spec, data=None):
    fig.canvas.draw()
    for ext in ("pdf", "svg", "png"):
        fig.savefig(OUT / f"{name}.{ext}", dpi=350, facecolor="white")
    if data is not None:
        with (OUT / f"{name}.csv").open("w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(data[0])
            writer.writerows(data[1])
    META["figures"][name] = spec
    plt.close(fig)


def bezier_path(segments, scale=(1, 1)):
    """Sample each cubic at 201 fixed t values, removing duplicate joins only."""
    ts = np.linspace(0, 1, 201)
    chunks = []
    for i, segment in enumerate(segments):
        p = np.asarray(segment, dtype=float)
        t = ts[:, None]
        points = (1-t)**3*p[0] + 3*(1-t)**2*t*p[1] + 3*(1-t)*t*t*p[2] + t**3*p[3]
        chunks.append(points if i == 0 else points[1:])
    return np.vstack(chunks) / np.asarray(scale)


def error_decomposition():
    fig = canvas(height=70)
    ax = fig.add_axes([.13, .15, .79, .78])
    clean_axes(ax)
    ax.spines["bottom"].set_visible(False)
    ax.set(xlim=(0, 1), ylim=(0, .18), xticks=[], yticks=[0, .05, .12, .15])
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=1, decimals=0))
    ax.set_ylabel("期望风险", labelpad=5)
    levels = [(0.05, YELLOW, "-", "贝叶斯风险", r"$R^\star_{\mathcal{P}}$"),
              (0.12, RED, "-", "类内最低风险", r"$\inf_{h\in\mathcal{H}} R_{\mathcal{P}}(h)$"),
              (0.15, BLUE, "--", "输出假设风险", r"$R_{\mathcal{P}}(\hat h)$")]
    for value, color, style, text, formula in levels:
        ax.plot([.05, .64], [value, value], color=color, lw=1.15, ls=style)
        ax.text(.06, value+.0045, text, va="bottom", fontsize=8.3)
        ax.text(.06, value+.0045, formula, va="bottom", fontsize=8.3,
                transform=offset_copy(ax.transData, fig=fig, x=len(text)*8.3+5, y=0, units="points"))
    for lo, hi, color, text, style in [(.05, .12, RED, "近似误差\n7个百分点", "-"),
                                       (.12, .15, BLUE, "估计误差\n3个百分点", "--")]:
        ax.annotate("", (.7, hi), (.7, lo), arrowprops={"arrowstyle":"<->", "color":color,
                    "lw":1.1, "linestyle":style, "shrinkA":1, "shrinkB":1})
        ax.text(.75, (lo+hi)/2, text, va="center", fontsize=8.3, color=color)
    save(fig, "risk-decomposition", {"size_mm":[112,70], "values":[.05,.12,.15],
         "gaps":[.07,.03], "axis":"True proportional risk scale, zero baseline"},
         (["risk_level","risk"], [["bayes",.05],["class_optimum",.12],["learned",.15]]))


def double_descent():
    population = [((3,40),(13,11),(22,6),(30,15)),
                  ((30,15),(39,25),(43,44),(47,44)),
                  ((47,44),(51,44),(51,20),(62,12)),
                  ((62,12),(70,6),(82,5),(94,4))]
    training = [((3,31),(20,14),(36,4),(47,.7))]
    p = bezier_path(population, (96,49))
    tr = bezier_path(training, (96,49))
    tr = np.vstack([tr, (94/96, .7/49)])
    assert np.all(np.diff(tr[:, 0])>0) and np.all(np.diff(tr[:, 1])<=1e-12)
    fig = canvas(height=64)
    ax = fig.add_axes([.12,.24,.82,.69]); clean_axes(ax)
    ax.set(xlim=(0,1), ylim=(0,1), xticks=[], yticks=[])
    ax.set_xlabel("模型复杂度", labelpad=14); ax.set_ylabel("平均损失", labelpad=5)
    ax.plot(p[:,0],p[:,1],lw=1.3,color=RED)
    ax.plot(tr[:,0],tr[:,1],lw=1.2,color=BLUE,ls="--")
    threshold=47/96
    ax.axvline(threshold,0,.93,color=GRAY,lw=.8,ls=":")
    ax.text(threshold,-.035,"插值阈值",ha="center",va="top",fontsize=8)
    ax.text(.66,.50,"期望风险",color=RED)
    ax.text(.11,.10,"经验风险",color=BLUE)
    save(fig,"double-descent",{"size_mm":[112,64], "kind":"Qualitative Bezier teaching path",
         "normalization":[96,49], "population_control_points":population,
         "training_control_points":training, "sampling":"201 t values per cubic; no empirical ticks"},
         (["series","complexity_position","loss_position"],
          [["population",*r] for r in p]+[["training",*r] for r in tr]))


def grokking():
    training = [((2,36),(10,31),(12,4),(19,2)), ((19,2),(36,1),(70,1),(96,1))]
    testing = [((2,37),(23,36),(50,36),(60,34)), ((60,34),(68,30),(69,6),(79,3)),
               ((79,3),(85,2),(91,2),(96,2))]
    tr = bezier_path(training, (99,46)); te = bezier_path(testing, (99,46))
    assert np.all(np.diff(tr[:,1])<=1e-12) and np.all(np.diff(te[:,1])<=1e-12)
    fig = canvas(height=64)
    ax = fig.add_axes([.12,.24,.82,.69]); clean_axes(ax)
    ax.set(xlim=(0,1), ylim=(0,1), xticks=[], yticks=[])
    ax.set_xlabel("训练进程",labelpad=15); ax.set_ylabel("错误比例",labelpad=5)
    ax.axvspan(19/99,65/99,color="#EDF2F5",zorder=0)
    ax.plot(tr[:,0],tr[:,1],color=BLUE,ls="--",lw=1.2)
    ax.plot(te[:,0],te[:,1],color=RED,lw=1.3)
    for x, text in [(19/99,r"$t_{\mathrm{fit}}$"),(65/99,r"$t_{\mathrm{gen}}$")]:
        ax.axvline(x,0,.86,color=GRAY,lw=.8,ls=":")
        ax.text(x,-.035,text,ha="center",va="top")
    ax.text(.30,.85,"测试错误率",color=RED)
    ax.text(.30,.10,"经验零一风险",color=BLUE)
    save(fig,"grokking",{"size_mm":[112,64], "kind":"Qualitative Bezier teaching path",
         "training_control_points":training,"test_control_points":testing,
         "normalization":[99,46], "markers":[19/99,65/99],
         "sampling":"201 t values per cubic; horizontal coordinate is schematic training progress"},
         (["series","training_progress_position","error_position"],
          [["training",*r] for r in tr]+[["test",*r] for r in te]))


def distribution_shift():
    fig=canvas(height=65)
    axes=[fig.add_axes([.065+i*.325,.275,.255,.48]) for i in range(3)]
    x=np.linspace(-3,3,601)
    normal=lambda mu:np.exp(-.5*((x-mu)/.65)**2)/(.65*np.sqrt(2*np.pi))
    source,target=normal(-.9),normal(.9)
    ax=axes[0];clean_axes(ax)
    ax.plot(x,source,color=BLUE,lw=1.15)
    ax.plot(x,target,color=RED,lw=1.15,ls="--")
    ax.set(xlim=(-3,3),ylim=(0,.68),xticks=[-2,0,2],yticks=[0,.6],xlabel=r"$x$")
    ax.text(0,1.09,r"$p(x)$",transform=ax.transAxes,ha="left")
    ax=axes[1];clean_axes(ax)
    ax.bar([-.12,.88],[.65,.35],width=.22,color="#EDF2F5",edgecolor=BLUE,linewidth=1)
    ax.bar([.12,1.12],[.35,.65],width=.22,facecolor="white",edgecolor=RED,linewidth=1,linestyle="--")
    ax.set(xlim=(-.5,1.5),ylim=(0,1),xticks=[0,1],yticks=[0,1],xlabel=r"$y$")
    ax.text(0,1.09,r"$p(y)$",transform=ax.transAxes,ha="left")
    ax=axes[2];clean_axes(ax)
    eta_s=1/(1+np.exp(-2*x));eta_t=1/(1+np.exp(2*x))
    ax.plot(x,eta_s,color=BLUE,lw=1.15);ax.plot(x,eta_t,color=RED,lw=1.15,ls="--")
    ax.set(xlim=(-3,3),ylim=(0,1),xticks=[-2,0,2],yticks=[0,1],xlabel=r"$x$")
    ax.text(0,1.09,r"$\eta(x)$",transform=ax.transAxes,ha="left")
    for ax,title in zip(axes,["协变量偏移","标签偏移","概念偏移"]):
        ax.text(.5,1.31,title,ha="center",transform=ax.transAxes,fontsize=8.5)
    handles=[plt.Line2D([0],[0],color=BLUE,lw=1.15),plt.Line2D([0],[0],color=RED,lw=1.15,ls="--")]
    fig.legend(handles,["源域","目标域"],loc="lower center",bbox_to_anchor=(.5,.005),
               ncols=2,frameon=False,handlelength=2,columnspacing=2,fontsize=8.5)
    assert abs(.65+.35-1)<1e-12 and np.all((eta_s>=0)&(eta_s<=1))
    save(fig,"distribution-shift",{"size_mm":[112,65], "origin":"Normalized teaching distributions",
         "covariate":"Normal(-0.9,0.65^2) vs Normal(0.9,0.65^2), full domain R, visible [-3,3]",
         "labels":{"source":[.65,.35],"target":[.35,.65]},
         "concept":"eta_s(x)=sigmoid(2x), eta_t(x)=sigmoid(-2x)",
         "sampling":"601 equally spaced points on [-3,3]; no extrapolation or empirical inference"},
         (["x","source_density","target_density","source_eta","target_eta"],
          np.column_stack([x,source,target,eta_s,eta_t])))


if __name__=="__main__":
    OUT.mkdir(exist_ok=True)
    error_decomposition();double_descent();grokking();distribution_shift()
    (OUT/"volume1-risk-and-shift.json").write_text(json.dumps(META,ensure_ascii=False,indent=2))
    print("Saved four vector PDF/SVG figures, PNG previews, sampled CSVs and metadata.")
