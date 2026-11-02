"""NTK 线性化：核谱控制残差收缩，宽度增加时核漂移变小（图 fig:lt8-ntk-residual）。

数据：n = 20 个输入 x_i = (cos t_i, sin t_i, 1)/sqrt(2)，t_i = 2*pi*i/20 + 0.1，
      第三个坐标为常数，相当于偏置；标签 y_i = sin(2 t_i) + 0.5 cos(5 t_i)。
网络：f(x) = m^{-1/2} sum_j a_j relu(w_j^T x)，a_j ~ N(0,1)，w_j ~ N(0, I_3)，两层都训练。
损失：(1/2n) ||f - y||^2，全批量梯度下降，步长 eta = n / (2 lambda_max(K_0))，T = 3000 步。
核：K(x,x') = <grad_theta f(x), grad_theta f(x')>，K_0 为初始化处的 n x n 核矩阵。
固定核预测：r(t) = (I - eta K_0 / n)^t r(0)，r = f - y。
宽度 m in {100, 1000, 10000}（随机种子 1,2,3）；中图另取 m = 100000（种子 4）；
核漂移另取 m in {30,...,100000}，种子 0。
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

n = 20
t_in = 2 * np.pi * np.arange(n) / n + 0.1
X = np.stack([np.cos(t_in), np.sin(t_in), np.ones(n)], 1) / np.sqrt(2)
y = np.sin(2 * t_in) + 0.5 * np.cos(5 * t_in)
T = 3000


def kernel(a, W, m):
    H = X @ W.T
    R = np.maximum(H, 0); D = (H > 0).astype(float)
    return (R @ R.T + ((D * a ** 2) @ D.T) * (X @ X.T)) / m


def run(m, seed, T=T, keep=False):
    rng = np.random.default_rng(seed)
    a = rng.normal(0, 1, m); W = rng.normal(0, 1, (m, 3))
    K0 = kernel(a, W, m)
    lam, U = np.linalg.eigh(K0)
    eta = 0.5 * n / lam[-1]
    res = []
    for t in range(T + 1):
        H = X @ W.T; R = np.maximum(H, 0); D = (H > 0)
        f = R @ a / np.sqrt(m); r = f - y
        res.append(r.copy())
        if t == T:
            break
        g = r / n
        ga = R.T @ g / np.sqrt(m)
        gW = ((g[:, None] * D) * a[None, :]).T @ X / np.sqrt(m)
        a = a - eta * ga; W = W - eta * gW
    KT = kernel(a, W, m)
    res = np.array(res)
    M = np.eye(n) - eta * K0 / n
    pred = [res[0]]
    for t in range(T):
        pred.append(M @ pred[-1])
    drift = np.linalg.norm(KT - K0) / np.linalg.norm(K0)
    return dict(res=res, pred=np.array(pred), lam=lam, U=U, eta=eta, drift=drift)


widths = [100, 1000, 10000]
runs = {m: run(m, s) for m, s in zip(widths, [1, 2, 3])}
big = run(100000, 4)
drift_m = [30, 100, 300, 1000, 3000, 10000, 30000, 100000]
drifts = [run(m, 0, T=T)['drift'] for m in drift_m]

fig, axes = plt.subplots(1, 3, figsize=(164 * MM, 50 * MM))
steps = np.arange(T + 1)
cols = {100: RED, 1000: GREEN, 10000: BLUE}
ax = axes[0]
for m in widths:
    rr = runs[m]
    ax.plot(steps, np.linalg.norm(rr['res'], axis=1), color=cols[m], lw=1.1, label=f'$m={m}$')
    ax.plot(steps, np.linalg.norm(rr['pred'], axis=1), color=cols[m], lw=0.8, ls='--')
ax.set_yscale('log'); ax.set_xlabel('梯度下降步数'); ax.set_ylabel(r'$\|f-y\|_2$（训练点）')
ax.set_title('实线为网络，虚线为固定核', pad=3); ax.legend(loc='lower left'); ax.grid(True)

ax = axes[1]
rr = big
idx = [n - 2, n // 2, 0]
names = ['第二大', '居中', '最小']
for k, name, c in zip(idx, names, [BLUE, GREEN, RED]):
    comp = np.abs(rr['res'] @ rr['U'][:, k]); comp0 = comp[0]
    ax.plot(steps, comp / comp0, color=c, lw=1.1, label=f'{name}：$\\lambda={rr["lam"][k]:.2g}$')
    ax.plot(steps, (1 - rr['eta'] * rr['lam'][k] / n) ** steps, color=c, lw=0.8, ls='--')
ax.set_yscale('log'); ax.set_ylim(1e-3, 2); ax.set_xlabel('梯度下降步数')
ax.set_ylabel('残差分量 / 初值'); ax.set_title('按 $K_0$ 特征方向（$m=10^5$）', pad=3)
ax.legend(loc='lower left', fontsize=7); ax.grid(True)

ax = axes[2]
ax.loglog(drift_m, drifts, 'o-', color=BLUE, lw=1.1, ms=3)
ax.set_xlabel('隐藏宽度 $m$'); ax.set_ylabel(r'$\|K_T-K_0\|_F/\|K_0\|_F$')
ax.set_title('训练结束时的核漂移', pad=3); ax.grid(True)
fig.tight_layout(pad=0.4, w_pad=1.0)
prepare_figure(fig)
for ext in ['pdf', 'png']:
    fig.savefig(OUT / f'figure.{ext}', dpi=300, facecolor='white')
summary = {'eigs_m100000': big['lam'].tolist(), 'eta_m100000': big['eta'],
           'components_final_ratio_m100000': {str(k): float(abs(big['res'][-1] @ big['U'][:, k]) / abs(big['res'][0] @ big['U'][:, k])) for k in idx},
           'components_pred_ratio_m100000': {str(k): float((1 - big['eta'] * big['lam'][k] / n) ** T) for k in idx},
           'final_residual_norm': {m: float(np.linalg.norm(runs[m]['res'][-1])) for m in widths},
           'final_pred_norm': {m: float(np.linalg.norm(runs[m]['pred'][-1])) for m in widths},
           'drift': dict(zip(map(str, drift_m), drifts))}
(OUT / 'figure-data.json').write_text(json.dumps(summary, ensure_ascii=False, indent=1) + '\n')
print(json.dumps(summary, ensure_ascii=False, indent=1))
