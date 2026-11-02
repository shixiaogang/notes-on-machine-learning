"""平均场缩放与 NTK 缩放下隐藏神经元参数的移动（图 fig:lt8-mean-field-particles）。

数据：n = 60 个输入 x_i ~ N(0, I_2)（种子 0）；教师函数 y = relu(u_1^T x) + relu(u_2^T x)，
      u_1 = (1.5, 0.5)，u_2 = (-0.5, 1.5)，无噪声。
学生：f(x) = c_m sum_j a_j relu(w_j^T x)，m = 400 个单元，w_j ~ N(0, 0.5^2 I_2)，a_j ~ N(0, 1)（种子 1）。
  NTK 缩放：c_m = m^{-1/2}，步长 eta = 0.2；
  平均场缩放：c_m = m^{-1}，步长 eta = 0.2 * m（使单个单元的更新为常数量级，见正文）。
损失：(1/2n) sum_i (f(x_i) - y_i)^2，全批量梯度下降 4000 步，两层都训练。
图中每个点是一个单元的 w_j，颜色区分 a_j 末值的符号，灰点为初值，细线连接 w_j 的初值与末值。
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

n, m, T = 60, 400, 4000
X = np.random.default_rng(0).normal(size=(n, 2))
U = np.array([[1.5, 0.5], [-0.5, 1.5]])
y = np.maximum(X @ U.T, 0).sum(1)


def train(scale, eta):
    rng = np.random.default_rng(1)
    W = rng.normal(0, 0.5, (m, 2)); a = rng.normal(0, 1, m)
    path = [W.copy()]; losses = []
    for t in range(T):
        H = X @ W.T; R = np.maximum(H, 0); D = H > 0
        r = scale * R @ a - y
        losses.append(float(np.mean(r ** 2) / 2))
        g = r / n
        ga = scale * R.T @ g
        gW = scale * ((g[:, None] * D) * a[None, :]).T @ X
        a -= eta * ga; W -= eta * gW
        if t % 20 == 19:
            path.append(W.copy())
    return np.array(path), a, losses


res = {'NTK 缩放 $1/\\sqrt{m}$': train(m ** -0.5, 0.2),
       '平均场缩放 $1/m$': train(1 / m, 0.2 * m)}
fig, axes = plt.subplots(1, 2, figsize=(130 * MM, 62 * MM), sharex=True, sharey=True)
summary = {}
for ax, (name, (path, a, losses)) in zip(axes, res.items()):
    for j in range(m):
        ax.plot([path[0, j, 0], path[-1, j, 0]], [path[0, j, 1], path[-1, j, 1]], color=GRID, lw=0.5, zorder=1)
    ax.scatter(path[0, :, 0], path[0, :, 1], s=2, color=MUTED, lw=0, zorder=2, label='初值')
    pos = a > 0
    ax.scatter(path[-1, pos, 0], path[-1, pos, 1], s=4, color=BLUE, zorder=3, label='$a_j>0$')
    ax.scatter(path[-1, ~pos, 0], path[-1, ~pos, 1], s=4, color=RED, zorder=3, label='$a_j<0$')
    for u in U:
        ax.annotate('', xy=u, xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.1))
    move = np.linalg.norm(path[-1] - path[0], axis=1)
    summary[name] = {'final_loss': losses[-1], 'mean_move': float(move.mean()), 'max_move': float(move.max())}
    ax.set_title(name + f'\n平均移动 {move.mean():.2f}，末端损失 {losses[-1]:.1e}', pad=3)
    ax.set_aspect('equal'); ax.set_xlim(-2.2, 2.2); ax.set_ylim(-2.2, 2.2)
    ax.set_xlabel('$w_{j,1}$'); ax.grid(True)
axes[0].set_ylabel('$w_{j,2}$')
axes[1].legend(loc='lower right', handletextpad=0.2, borderaxespad=0.2)
fig.tight_layout(pad=0.4, w_pad=1.0)
prepare_figure(fig)
for ext in ['pdf', 'png']:
    fig.savefig(OUT / f'figure.{ext}', dpi=300, facecolor='white')
(OUT / 'figure-data.json').write_text(json.dumps(summary, ensure_ascii=False, indent=1) + '\n')
print(json.dumps(summary, ensure_ascii=False, indent=1))
