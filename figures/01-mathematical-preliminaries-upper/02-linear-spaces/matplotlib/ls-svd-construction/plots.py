"""教学图：SVD 构造三部曲 A^T A -> 特征值 -> 奇异向量。

固定 A=[[2,0.5],[0.5,1]]。A^T A = [[4.25,2.5],[2.5,3.25]]，
对称谱引理给出正交对角化，特征值 λ1≈6.30, λ2≈1.20，
奇异值 σ_i = sqrt(λ_i) ≈ 2.51, 1.09；右奇异向量 v_i 即特征向量，
左奇异向量 u_i = A v_i / σ_i。无随机数，不调用 LaTeX。
运行：python3 plots.py
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

HERE = Path(__file__).resolve().parent
NAME = HERE.name
ROOT = next(p for p in Path(__file__).resolve().parents
            if (p / "build.sh").is_file() and (p / "tex/book.tex").is_file())
for fname in ["SourceHanSansSC-Normal.otf", "LXGWWenKai-Regular.ttf"]:
    font_manager.fontManager.addfont(ROOT / "fonts" / fname)

BLUE, GREEN, YELLOW = "#7188A3", "#829C8B", "#B4A16F"
INK, STROKE = "#3B4252", "#4C4D4F"
BLUE_FILL, GREEN_FILL = "#E5EAF0", "#E8EEE9"
CN, EN = "Source Han Sans SC", "LXGW WenKai"
matplotlib.rcParams.update({
    "font.family": [EN, CN], "font.size": 8, "axes.unicode_minus": False,
    "text.color": INK, "axes.edgecolor": STROKE, "pdf.fonttype": 3,
    "figure.facecolor": "white",
})

A = np.array([[2.0, 0.5], [0.5, 1.0]])
AtA = A.T @ A
lam, V = np.linalg.eigh(AtA)
order = np.argsort(lam)[::-1]
lam = lam[order]; V = V[:, order]
sig = np.sqrt(lam)
U = A @ V / sig

fig, axes = plt.subplots(1, 3, figsize=(13, 3.6))

# 第一步：A^T A
ax = axes[0]
ax.set_title("第一步：形成对称 Gram 矩阵", fontsize=9)
ax.text(.5, .72, "A = [[2, 0.5], [0.5, 1]]",
        ha="center", fontsize=10, transform=ax.transAxes)
ax.text(.5, .40,
        "AᵀA = [[4.25, 1.5], [1.5, 1.25]]",
        ha="center", fontsize=10, transform=ax.transAxes, color=BLUE)
ax.text(.5, .16, "对称方阵，可正交对角化", ha="center", fontsize=8.5,
        transform=ax.transAxes)
ax.axis("off")

# 第二步：正交对角化
ax = axes[1]
ax.set_title("第二步：对称谱引理对角化", fontsize=9)
ax.text(.5, .66, r"$A^\top A = V\,\mathrm{diag}(\lambda_1,\lambda_2)\,V^\top$",
        ha="center", fontsize=9.5, transform=ax.transAxes) if False else \
ax.text(.5, .66, "AᵀA = V · diag(λ₁, λ₂) · Vᵀ",
        ha="center", fontsize=9.5, transform=ax.transAxes)
ax.text(.5, .40, rf"$\lambda_1\approx{lam[0]:.2f},\ \lambda_2\approx{lam[1]:.2f}$",
        ha="center", fontsize=10, transform=ax.transAxes, color=GREEN)
ax.text(.5, .18, r"$v_1,v_2$ 为正交特征方向", ha="center",
        fontsize=8.5, transform=ax.transAxes)
ax.axis("off")

# 第三步：奇异值与左右奇异向量
ax = axes[2]
ax.set_title("第三步：σ_i=√λ_i，u_i=Av_i/σ_i", fontsize=9)
ax.text(.5, .70, rf"$\sigma_1\approx{sig[0]:.2f},\ \sigma_2\approx{sig[1]:.2f}$",
        ha="center", fontsize=10, transform=ax.transAxes, color=YELLOW)
ax.text(.5, .46, r"$v_i$：右奇异向量（= 特征向量）", ha="center",
        fontsize=8.5, transform=ax.transAxes)
ax.text(.5, .26, r"$u_i=Av_i/\sigma_i$：左奇异向量", ha="center",
        fontsize=8.5, transform=ax.transAxes)
ax.text(.5, .08, "A = U · diag(σᵢ) · Vᵀ",
        ha="center", fontsize=9.5, transform=ax.transAxes, color=INK)
ax.axis("off")

fig.tight_layout()
out = HERE / f"{NAME}.pdf"
fig.savefig(out); fig.savefig(HERE / f"{NAME}.png", dpi=160)
record = {"A": A.tolist(), "AtA": AtA.tolist(), "lambda": lam.tolist(),
          "sigma": sig.tolist(), "V": V.tolist(), "U": U.tolist()}
(HERE / "sources.json").write_text(json.dumps(record, ensure_ascii=False, indent=2))
print("wrote", out); print(json.dumps(record, ensure_ascii=False))
