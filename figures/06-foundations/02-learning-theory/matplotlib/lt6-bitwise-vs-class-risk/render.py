"""逐位最优与类别最优不一致的三类概率例子（第6章 6.1.2）。

教学示例：所有邮件输入相同，类别概率 正常 0.40、广告 0.35、诈骗 0.25；
编码 正常->(0,1)，广告->(1,0)，诈骗->(1,1)，(0,0) 解码为正常。
对每个常量预测码字 c，计算
  期望位错误数 = sum_j P(c_j(y) != c_j)
  类别零一风险 = P(decode(c) != y)
逐位最优码字为 (1,1)（每位单独取多数），类别风险 0.75；
直接预测“正常”的类别风险 0.60。
"""
from pathlib import Path
import json

import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt
from matplotlib import font_manager


def project_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "tex" / "volumes.json").exists():
            return parent
    raise RuntimeError("project root not found")


ROOT = project_root()
OUT = Path(__file__).resolve().parent
for name in ("SourceHanSansSC-Normal.otf", "FiraMath-Regular.otf", "LXGWWenKai-Regular.ttf"):
    font_manager.fontManager.addfont(str(ROOT / "fonts" / name))
CJK = font_manager.FontProperties(fname=str(ROOT / "fonts" / "SourceHanSansSC-Normal.otf")).get_name()
MATH = font_manager.FontProperties(fname=str(ROOT / "fonts" / "FiraMath-Regular.otf")).get_name()
plt.rcParams.update({
    "font.family": [CJK, MATH],
    "font.size": 8,
    "mathtext.fontset": "custom",
    "mathtext.rm": MATH, "mathtext.it": MATH,
    "axes.linewidth": 0.75,
    "pdf.fonttype": 3,
})
BLUE, BLUE_FILL = "#7188A3", "#E5EAF0"
YELLOW = "#B4A16F"
INK, MUTED, GRID = "#3B4252", "#6B7280", "#D8DCE2"

probs = {"正常": 0.40, "广告": 0.35, "诈骗": 0.25}
code = {"正常": (0, 1), "广告": (1, 0), "诈骗": (1, 1)}
decode = {v: k for k, v in code.items()}
decode[(0, 0)] = "正常"
words = [(0, 1), (1, 0), (1, 1), (0, 0)]
rows = []
for c in words:
    bit_err = sum(p * sum(int(a != b) for a, b in zip(code[y], c)) for y, p in probs.items())
    cls = decode[c]
    cls_risk = 1 - probs[cls]
    rows.append({"codeword": c, "decoded": cls, "expected_bit_errors": round(bit_err, 4),
                 "class_risk": round(cls_risk, 4)})

fig, ax = plt.subplots(figsize=(4.2, 2.15))
xs = range(len(rows))
w = 0.36
b1 = ax.bar([x - w / 2 for x in xs], [r["expected_bit_errors"] for r in rows], w,
            color=BLUE_FILL, edgecolor=BLUE, linewidth=0.8, label="期望位错误数")
b2 = ax.bar([x + w / 2 for x in xs], [r["class_risk"] for r in rows], w,
            color=BLUE, edgecolor=BLUE, linewidth=0.8, label="类别零一风险")
for bars in (b1, b2):
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.025,
                f"{bar.get_height():.2f}", ha="center", va="bottom", fontsize=7, color=INK)
ax.set_xticks(list(xs))
ax.set_xticklabels([f"({r['codeword'][0]},{r['codeword'][1]})\n解码为{r['decoded']}" for r in rows],
                   color=INK)
ax.set_ylim(0, 1.55)
ax.set_ylabel("常量预测的代价", color=INK)
ax.spines[["top", "right"]].set_visible(False)
ax.yaxis.grid(True, color=GRID, linewidth=0.4)
ax.set_axisbelow(True)
ax.tick_params(colors=INK, width=0.75, labelsize=7.5)
# mark the two optima directly above the relevant bars
ax.text(2 - w / 2, rows[2]["expected_bit_errors"] + 0.12, "逐位最优", ha="center", va="bottom",
        fontsize=7.5, color=MUTED)
ax.text(0 + w / 2, rows[0]["class_risk"] + 0.12, "类别最优", ha="center", va="bottom",
        fontsize=7.5, color=MUTED)
ax.legend(frameon=False, fontsize=7.5, loc="upper left", ncol=2)
fig.tight_layout(pad=0.3)
fig.savefig(OUT / "figure.pdf")
(OUT / "data.json").write_text(json.dumps({"probabilities": probs, "rows": rows},
                                          ensure_ascii=False, indent=1))
