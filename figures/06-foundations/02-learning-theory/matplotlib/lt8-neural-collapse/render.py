"""无约束特征模型中的神经坍缩：三类二维示例（图 fig:lt8-neural-collapse）。

模型：K = 3 类，每类 10 个训练样本，特征维数 d = 2（满足 d >= K - 1）。
      特征 h_i 与分类器 W（K x d）都是自由变量，不含偏置，目标函数为
      (1/N) sum_i CE(W h_i, y_i) + (lam_W / 2)||W||_F^2 + (lam_H / 2)||H||_F^2，
      N = 30，lam_W = lam_H = 5e-3。
初始化：h_i、W 各元素 ~ N(0, 0.5^2)（种子 0）；全批量梯度下降，步长 0.5，2e4 步。
度量：类内散度与类间散度之比 tr(S_W)/tr(S_B)；中心化类均值长度的变异系数（等长时为 0；
      d = 2、K = 3 时三个中心化均值之和为零，等长即等角，两两余弦为 -1/2）；
      W 的行与对应中心化类均值的方向余弦的最小值。图中低于 1e-12 的值贴在下限。
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

K, per, d, lam, eta, T = 3, 10, 2, 5e-3, 0.5, 20000
N = K * per
y = np.repeat(np.arange(K), per)
rng = np.random.default_rng(0)
H = rng.normal(0, 0.5, (N, d)); W = rng.normal(0, 0.5, (K, d))
Y = np.eye(K)[y]


def metrics(H, W):
    mu = np.stack([H[y == k].mean(0) for k in range(K)]); g = H.mean(0)
    Mc = mu - g
    sw = sum(((H[y == k] - mu[k]) ** 2).sum() for k in range(K)) / N
    sb = (Mc ** 2).sum() / K
    Mn = Mc / np.linalg.norm(Mc, axis=1, keepdims=True)
    cos = [float(Mn[i] @ Mn[j]) for i in range(K) for j in range(i + 1, K)]
    Wn = W / np.linalg.norm(W, axis=1, keepdims=True)
    align = [float(Wn[k] @ Mn[k]) for k in range(K)]
    nr = np.linalg.norm(Mc, axis=1)
    return sw / sb, cos, align, float(nr.std() / nr.mean())


snap_at = [0, 100, T]
snaps = {}; trace = {'step': [], 'ratio': [], 'cos': [], 'align': [], 'equinorm': []}
for t in range(T + 1):
    if t in snap_at:
        snaps[t] = (H.copy(), W.copy())
    if t % 50 == 0 or t < 50:
        r, c, a, e = metrics(H, W)
        trace['step'].append(t); trace['ratio'].append(r); trace['cos'].append(c); trace['align'].append(a); trace['equinorm'].append(e)
    if t == T:
        break
    Z = H @ W.T; Z -= Z.max(1, keepdims=True)
    P = np.exp(Z); P /= P.sum(1, keepdims=True)
    G = (P - Y) / N
    gW = G.T @ H + lam * W
    gH = G @ W + lam * H
    W -= eta * gW; H -= eta * gH

cols = [BLUE, GREEN, RED]
fig = plt.figure(figsize=(164 * MM, 54 * MM))
gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1, 1.25])
lims = 1.05 * max(np.abs(snaps[T][0]).max(), np.abs(snaps[0][0]).max())
for i, t in enumerate(snap_at):
    ax = fig.add_subplot(gs[0, i])
    Hs, Ws = snaps[t]
    for k in range(K):
        ax.scatter(Hs[y == k, 0], Hs[y == k, 1], s=5, color=cols[k], lw=0)
        mu = Hs[y == k].mean(0)
        ax.plot(*mu, marker='o', ms=5, mfc='white', mec=cols[k], mew=1.0)
        w = Ws[k] / np.linalg.norm(Ws[k]) * 0.8 * lims
        ax.annotate('', xy=w, xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=cols[k], lw=0.8, ls='--'))
    ax.set_aspect('equal'); ax.set_xlim(-lims, lims); ax.set_ylim(-lims, lims)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(True)
    ax.set_title(f'第 {t} 步', pad=3)
ax = fig.add_subplot(gs[0, 3])
st = np.array(trace['step']); st[0] = 1
fl = 1e-12
ax.plot(st, np.maximum(trace['ratio'], fl), color=BLUE, lw=1.1, label='类内／类间散度')
ax.plot(st, np.maximum(trace['equinorm'], fl), color=GREEN, lw=1.1, label='类均值长度的变异系数')
ax.plot(st, np.maximum([1 - min(a) for a in trace['align']], fl), color=RED, lw=1.1, ls='--', label='$1-$分类器对齐余弦')
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_ylim(5e-13, 1e2); ax.set_xlabel('梯度下降步数'); ax.grid(True)
ax.legend(loc='lower left', fontsize=7)
fig.tight_layout(pad=0.4, w_pad=0.8)
prepare_figure(fig)
for ext in ['pdf', 'png']:
    fig.savefig(OUT / f'figure.{ext}', dpi=300, facecolor='white')
final = metrics(*snaps[T])
summary = {'final_ratio': final[0], 'final_mean_cosines': final[1], 'final_alignment': final[2], 'final_equinorm_cv': final[3],
           'equinorm_cv_at_0': trace['equinorm'][0], 'ratio_at_0': trace['ratio'][0],
           'feature_norms_final': np.linalg.norm(snaps[T][0], axis=1).round(4).tolist()[:3],
           'W_row_norms_final': np.linalg.norm(snaps[T][1], axis=1).tolist()}
(OUT / 'figure-data.json').write_text(json.dumps({'summary': summary, 'trace': trace}, ensure_ascii=False) + '\n')
print(json.dumps(summary, ensure_ascii=False, indent=1))
