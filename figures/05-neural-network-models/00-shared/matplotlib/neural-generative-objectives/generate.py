"""Exact teaching distributions and distances; no sampled data or fitted model.

Run with Python, NumPy, Matplotlib and PyMuPDF. Locate the owning project root
from build.sh so reproduction never depends on a machine-specific path.
"""
from pathlib import Path
import csv
import hashlib
import importlib.util
import json
import math
import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "build.sh").exists())
BASE = Path(__file__).resolve().parent
STYLE_PATH = ROOT / "figures/00-shared/academic-drawing/plot_style.py"
spec = importlib.util.spec_from_file_location("neural_generative_plot_style", STYLE_PATH)
style = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = style
spec.loader.exec_module(style)
style.configure()

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.text import Text
import numpy as np
import fitz
from fontTools.ttLib import TTFont


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def export(fig, key, size, data, arrays, checks, meaning):
    out = BASE / key
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "data.json", data)
    with (out / "curves.csv").open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(list(arrays))
        writer.writerows(zip(*arrays.values()))
    style.prepare_figure(fig)
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    outside = []
    for artist in fig.findobj(Text):
        if artist.get_visible() and artist.get_text():
            box = artist.get_window_extent(renderer)
            if box.x0 < -1 or box.y0 < -1 or box.x1 > fig.bbox.x1 + 1 or box.y1 > fig.bbox.y1 + 1:
                outside.append(artist.get_text())
    assert not outside, outside
    for suffix in ["pdf", "svg", "png"]:
        kwargs = {"metadata": {"Creator": "Neural generative exact teaching figure"}} if suffix == "pdf" else {}
        fig.savefig(out / ("figure." + suffix), dpi=220, **kwargs)
    with fitz.open(out / "figure.pdf") as doc:
        assert len(doc) == 1
        page = doc[0]
        measured = [page.rect.width * 25.4 / 72, page.rect.height * 25.4 / 72]
        assert np.allclose(measured, size, atol=.001), measured
        fonts = sorted({entry[3] for entry in page.get_fonts()})
        assert len(page.get_images()) == 0
    font_record = style.style_record()
    font_record["font_versions"] = {path.name: TTFont(path)["name"].getDebugName(5)
                                    for path in [style.CN_FILE, style.NOTE_FILE, style.EN_FILE, style.STIX_FILE]}
    font_record["license_records"] = ["fonts/licenses/SourceHanSans-OFL.txt", "fonts/licenses/LXGWWenKai-OFL.txt",
                                     "fonts/licenses/FiraMath-font-license.txt", "fonts/licenses/STIX-OFL.txt"]
    write_json(out / "generation.json", {
        "key": "neural-generative-" + key, "route": "Matplotlib", "date": "2026-10-13",
        "generator": str(Path(__file__).relative_to(ROOT)), "generator_sha256": sha(Path(__file__)),
        "style": font_record, "style_sha256": sha(STYLE_PATH),
        "input_sha256": {str((out / name).relative_to(ROOT)): sha(out / name) for name in ["data.json", "curves.csv"]},
        "asset_sha256": sha(out / "figure.pdf"),
        "native_size_mm": size, "body_width_mm": size[0], "scale_at_requested_width": 1.0,
        "example_type": "Author-constructed exact dimensionless teaching example",
        "scientific_checks": checks,
        "render_checks": {"visible_text_outside_canvas": outside, "actual_size_mm": measured,
                          "main_font_pt": 8, "actual_pdf_fonts": fonts, "raster_images_embedded": 0,
                          "png_dpi": 220, "final_book_page_review": "Parent integration task"},
    })
    (out / "README.md").write_text(
        "# neural-generative-" + key + "\n\n" + meaning + "\n\n"
        "这是作者构造的解析教学示例，不是模型训练实验。`data.json` 保存定义与参数，"
        "`curves.csv` 保存逐点计算结果，`generation.json` 记录代码、输入、字体和成品校验值。\n\n"
        "在项目根目录运行 `python3 figures/05-neural-network-models/00-shared/matplotlib/"
        "neural-generative-objectives/generate.py`。使用共享绘图工具加载仓库中的真实字体："
        "中文思源黑体 Normal，英文与数学 Fira Math；仅 Fira 缺字时使用 STIX Two Math。"
        "字体许可证见 `fonts/licenses/`。PDF 与 SVG 为矢量导出，PNG 为 220 dpi 预览。"
        f"原生尺寸 {size[0]} × {size[1]} mm，按原生宽度引用时主体文字保持 8 pt。\n")
    plt.close(fig)


def gaussian(x, mean, sigma):
    return np.exp(-.5 * ((x - mean) / sigma) ** 2) / (sigma * math.sqrt(2 * math.pi))


def modes():
    size = [159, 66]
    fig, axes = plt.subplots(1, 2, figsize=tuple(v / 25.4 for v in size))
    fig.subplots_adjust(left=.068, right=.984, bottom=.255, top=.82, wspace=.27)
    x = np.linspace(-4, 4, 801)
    sigma = .35
    target = .5 * gaussian(x, -2, sigma) + .5 * gaussian(x, 2, sigma)
    middle, one_peak = gaussian(x, 0, sigma), gaussian(x, 2, sigma)
    for ax, candidate, title in zip(axes, [middle, one_peak], ["均值附近的单峰候选", "只覆盖右峰的单峰候选"]):
        ax.plot(x, target, color=style.BLUE, linestyle=(0, (4, 2)), zorder=3)
        ax.plot(x, candidate, color=style.GREEN, zorder=2)
        ax.set_xlim(-4.1, 4.1)
        ax.set_ylim(0, 1.22)
        ax.set_xticks([-4, -2, 0, 2, 4])
        ax.set_yticks([0, .5, 1])
        ax.set_xlabel(r"样本值 $x$（无量纲）", labelpad=3)
        ax.set_ylabel("概率密度", labelpad=3)
        ax.set_title(title, pad=7)
        ax.tick_params(length=2.5, pad=2)
    fig.legend(handles=[Line2D([0], [0], color=style.BLUE, linestyle=(0, (4, 2))),
                        Line2D([0], [0], color=style.GREEN)],
               labels=[r"目标分布 $P$", r"生成分布 $Q$"],
               loc="lower center", bbox_to_anchor=(.5, .025), ncol=2,
               handlelength=2.5, columnspacing=2.2)
    inside = lambda mu: .5 * (math.erf((4 - mu) / (sigma * math.sqrt(2))) - math.erf((-4 - mu) / (sigma * math.sqrt(2))))
    checks = {"mixture_weights_sum_to_one": True,
              "all_density_values_nonnegative": bool(np.all(target >= 0) and np.all(middle >= 0) and np.all(one_peak >= 0)),
              "target_identical_in_both_panels": True,
              "normalization": "Each component is an exact normalized normal density; weighted mixture integrates to one",
              "displayed_probability_mass": {"P": .5 * inside(-2) + .5 * inside(2), "Q_left": inside(0), "Q_right": inside(2)}}
    assert min(checks["displayed_probability_mass"].values()) > .999999
    export(fig, "modes", size,
           {"P": "0.5 N(-2,0.35^2) + 0.5 N(2,0.35^2)", "Q_left": "N(0,0.35^2)",
            "Q_right": "N(2,0.35^2)", "sigma": sigma, "mixture_means": [-2, 2], "mixture_weights": [.5, .5],
            "source": "Author-constructed analytic example specified for this chapter; no external dataset",
            "display_range": [-4, 4], "display_grid_points": len(x), "density_formula": "exp(-(x-mu)^2/(2 sigma^2))/(sigma sqrt(2 pi))"},
           {"x": x, "P_density": target, "Q_left_density": middle, "Q_right_density": one_peak}, checks,
           "两个面板使用同一个双峰目标分布。左图候选集中在两个峰之间，右图候选只覆盖右侧峰。"
           "目标密度用蓝色虚线，候选密度用绿色实线，二者的样本空间与坐标尺度相同。")


def distance():
    size = [112, 55]
    fig, ax = plt.subplots(figsize=tuple(v / 25.4 for v in size))
    fig.subplots_adjust(left=.13, right=.97, bottom=.255, top=.79)
    a = np.linspace(-2, 2, 401)
    w1 = np.abs(a)
    js = np.where(a == 0, 0., math.log(2))
    ax.plot(a, w1, color=style.BLUE, label=r"$W_1(P,Q_a)=|a|$", zorder=2)
    ax.plot([-2, 0], [math.log(2), math.log(2)], color=style.GREEN, linestyle=(0, (4, 2)), zorder=3)
    ax.plot([0, 2], [math.log(2), math.log(2)], color=style.GREEN, linestyle=(0, (4, 2)), zorder=3)
    ax.plot([0], [math.log(2)], marker="o", markersize=4.8, markeredgewidth=1.1,
            markeredgecolor=style.GREEN, markerfacecolor="white", linestyle="none", zorder=5)
    ax.plot([0], [0], marker="o", markersize=4.8, markeredgewidth=1.1,
            markeredgecolor=style.GREEN, markerfacecolor=style.GREEN, linestyle="none", zorder=5)
    ax.set_xlim(-2.05, 2.05)
    ax.set_ylim(-.08, 2.12)
    ax.set_xticks([-2, -1, 0, 1, 2])
    ax.set_yticks([0, math.log(2), 1, 2], ["0", r"$\log 2$", "1", "2"])
    ax.set_xlabel(r"位移 $a$（无量纲）", labelpad=3)
    ax.set_ylabel("分布距离（无量纲）", labelpad=3)
    ax.tick_params(length=2.5, pad=2)
    fig.legend(handles=[Line2D([0], [0], color=style.BLUE),
                        Line2D([0], [0], color=style.GREEN, linestyle=(0, (4, 2)))],
               labels=[r"$W_1(P,Q_a)$", r"$\operatorname{JS}(P,Q_a)$"],
               loc="upper center", bbox_to_anchor=(.54, .965), ncol=2,
               handlelength=2.3, columnspacing=2)
    export(fig, "distance", size,
           {"P": "Dirac(0)", "Q_a": "Dirac(a)", "W1": "abs(a)",
            "source": "Author-drawn one-dimensional point-mass instance of the separated-support phenomenon",
            "background_reference": "https://proceedings.mlr.press/v70/arjovsky17a.html",
            "JS": "0 if a == 0 else log(2)", "logarithm": "natural",
            "display_range": [-2, 2], "display_grid_points": len(a),
            "discontinuity_markers": {"open_point": [0, math.log(2)], "closed_point": [0, 0]}},
           {"a": a, "W1": w1, "JS": js},
           {"zero_displacement_both_distances_zero": bool(w1[a == 0][0] == 0 and js[a == 0][0] == 0),
            "JS_nonzero_displacement_equals_log2": bool(np.all(js[a != 0] == math.log(2))),
            "W1_equals_absolute_displacement": bool(np.array_equal(w1, np.abs(a))),
            "JS_discontinuity_not_interpolated": True},
           "比较位于 0 与 a 的两个点质量分布。Wasserstein-1 距离随位移连续变化，"
           "JS 散度在任何非零位移处都是 log 2。空心点排除 a=0 时的 log 2，实心点表示该处的实际值 0；"
           "虚线的两侧分别绘制，没有连接上下跳变。示例对应 WGAN 原论文的分离支持集现象。")


if __name__ == "__main__":
    modes()
    distance()
    print("modes 159 × 66 mm; distance 112 × 55 mm; exact-data and canvas checks passed")
