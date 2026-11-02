"""深层线性分解中各奇异值随时间的增长（第8章，图 fig:lt8-deep-linear-spectrum）。

设定：目标矩阵 W* = diag(3, 1, 0.3)，完全观测的平方损失
L(W) = ||W - W*||_F^2 / 2，各层平衡且与 W* 的奇异方向对齐，初值 sigma_k(0) = 1e-3。
此时定理 thm:balanced-deep-linear-flow 的奇异值方程化为
    d sigma_k / dt = L * sigma_k^(2 - 2/L) * (s_k - sigma_k).
以 u = log t 为自变量用四阶 Runge--Kutta 积分（du = 1e-3），无随机数。
L = 2 时可与解析解 s / (1 + (s/sigma0 - 1) exp(-2 s t)) 对照（脚本末尾核对）。
"""
from pathlib import Path
import sys, json
import numpy as np
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').exists())
sys.path.insert(0, str(ROOT / 'figures/06-foundations/00-shared/academic-drawing'))
from plot_style import *  # noqa: F401,F403
import matplotlib.pyplot as plt
configure()
OUT = Path(__file__).resolve().parent
MM = 1 / 25.4

S = np.array([3.0, 1.0, 0.3])
SIGMA0 = 1e-3
DEPTHS = [1, 2, 3]
T0, T1 = 1e-3, 1e3


def rhs(sigma, t, L):
    return t * L * sigma ** (2 - 2 / L) * (S - sigma)  # d sigma / d(log t)


def integrate(L, du=1e-3):
    u = np.arange(np.log(T0), np.log(T1) + du, du)
    sig = np.empty((u.size, S.size)); sig[0] = SIGMA0
    for i in range(u.size - 1):
        t = np.exp(u[i]); h = du; y = sig[i]
        k1 = rhs(y, t, L)
        k2 = rhs(y + h / 2 * k1, t * np.exp(h / 2), L)
        k3 = rhs(y + h / 2 * k2, t * np.exp(h / 2), L)
        k4 = rhs(y + h * k3, t * np.exp(h), L)
        sig[i + 1] = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return np.exp(u), sig


fig, axes = plt.subplots(1, 3, figsize=(160 * MM, 50 * MM), sharey=True)
colors = [BLUE, GREEN, RED]
record = {'targets': S.tolist(), 'sigma0': SIGMA0, 'half_times': {}}
for ax, L in zip(axes, DEPTHS):
    t, sig = integrate(L)
    halves = []
    for k in range(S.size):
        ax.plot(t, sig[:, k], color=colors[k], lw=1.1, label=rf'$s_{k+1}={S[k]:g}$')
        ax.axhline(S[k], color=colors[k], lw=0.6, ls=':')
        idx = np.argmax(sig[:, k] >= S[k] / 2)
        halves.append(float(t[idx]))
        ax.plot(t[idx], sig[idx, k], 'o', ms=3, color=colors[k])
    record['half_times'][f'L={L}'] = halves
    ax.set_xscale('log'); ax.set_xlim(1e-2, T1); ax.set_ylim(0, 3.3)
    ax.set_xlabel('训练时间 $t$（对数刻度）')
    ax.set_title(f'深度 $L={L}$', pad=3)
    ax.grid(True, which='major', axis='both')
axes[0].set_ylabel(r'端到端奇异值 $\sigma_k(t)$')
axes[0].legend(loc='center right', bbox_to_anchor=(1.0, 0.6), handlelength=1.6)
fig.tight_layout(pad=0.4, w_pad=1.0)
prepare_figure(fig)
for ext in ['pdf', 'png']:
    fig.savefig(OUT / f'figure.{ext}', dpi=300, facecolor='white')

# 核对 L=2 的解析解
t, sig = integrate(2)
exact = S / (1 + (S / SIGMA0 - 1) * np.exp(-2 * np.outer(t, S)))
record['max_abs_error_L2_vs_analytic'] = float(np.max(np.abs(sig - exact)))
(OUT / 'figure-data.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(record, ensure_ascii=False, indent=2))
