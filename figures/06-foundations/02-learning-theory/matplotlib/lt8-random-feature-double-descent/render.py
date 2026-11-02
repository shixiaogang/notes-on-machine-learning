"""随机特征回归的模型规模双重下降（图 fig:lt8-random-feature-double-descent）。

数据：输入 x ~ N(0, I_d / d)，d = 20；标签 y = beta^T x + xi，beta ~ N(0, I_d)（每次重抽后归一化为 ||beta||_2 = sqrt(d)），
      xi ~ N(0, sigma^2)，sigma = 0.5。训练样本 n = 100，测试样本 5000。
特征：phi_j(x) = relu(v_j^T x)，v_j ~ N(0, I_d)，特征数 N 从 5 到 2000。
拟合：最小二乘；N < n 时为普通最小二乘，N >= n 时取最小欧氏范数插值解（伪逆）；
      对照为岭回归，经验目标 (1/n)||Phi c - y||^2 + lam ||c||^2，lam = 1e-3 与 1e-1。
指标：测试均方误差，40 次独立重复（种子 0..39）的中位数，阴影为四分位区间（N 接近 n 时均值受个别病态设计矩阵支配，另存于 figure-data.json）。
训练误差在 N >= n 时为数值零，图中贴在纵轴下限。
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

d, n, n_test, sigma, reps = 20, 100, 5000, 0.5, 40
Ns = np.unique(np.concatenate([np.round(np.logspace(np.log10(5), np.log10(2000), 40)).astype(int), [90, 95, 100, 105, 110]]))
lams = [1e-3, 1e-1]
test = {'min-norm': np.zeros((reps, Ns.size)), 'train': np.zeros((reps, Ns.size))}
for lam in lams:
    test[lam] = np.zeros((reps, Ns.size))
for r in range(reps):
    rng = np.random.default_rng(r)
    beta = rng.normal(size=d); beta *= np.sqrt(d) / np.linalg.norm(beta)
    X = rng.normal(size=(n, d)) / np.sqrt(d); Xt = rng.normal(size=(n_test, d)) / np.sqrt(d)
    y = X @ beta + sigma * rng.normal(size=n); yt = Xt @ beta + sigma * rng.normal(size=n_test)
    V = rng.normal(size=(Ns.max(), d))
    for k, N in enumerate(Ns):
        P = np.maximum(X @ V[:N].T, 0); Pt = np.maximum(Xt @ V[:N].T, 0)
        c = np.linalg.pinv(P, rcond=1e-12) @ y
        test['min-norm'][r, k] = np.mean((Pt @ c - yt) ** 2)
        test['train'][r, k] = np.mean((P @ c - y) ** 2)
        for lam in lams:
            if N <= n:
                cl = np.linalg.solve(P.T @ P / n + lam * np.eye(N), P.T @ y / n)
            else:
                cl = P.T @ np.linalg.solve(P @ P.T / n + lam * np.eye(n), y / n)
            test[lam][r, k] = np.mean((Pt @ cl - yt) ** 2)

fig, ax = plt.subplots(figsize=(110 * MM, 62 * MM))
styles = [('min-norm', '最小范数解（无正则）', BLUE, '-'), (1e-3, r'岭回归 $\lambda=10^{-3}$', GREEN, '-'),
          (1e-1, r'岭回归 $\lambda=10^{-1}$', PURPLE, '-.'), ('train', '训练误差（最小范数解）', MUTED, '--')]
summary = {}
for key, lab, col, ls in styles:
    med = np.median(test[key], 0)
    q1, q3 = np.percentile(test[key], [25, 75], axis=0)
    ax.plot(Ns, np.maximum(med, 1.01e-2), color=col, ls=ls, lw=1.1, label=lab)
    if key != 'train':
        ax.fill_between(Ns, q1, q3, color=col, alpha=0.25, lw=0)
    summary[str(key)] = {'median': {str(N): float(v) for N, v in zip(Ns, med)},
                         'mean': {str(N): float(v) for N, v in zip(Ns, test[key].mean(0))}}
ax.axvline(n, color=MUTED, lw=0.6, ls=':')
ax.text(n * 1.06, 0.02, '$N=n=100$', color=MUTED, fontsize=7.5)
ax.axhline(sigma ** 2, color=RED, lw=0.6, ls=':')
ax.text(6, sigma ** 2 * 1.1, r'噪声方差 $\sigma^2$', color=RED, fontsize=7.5)
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_ylim(1e-2, 2e2)
ax.set_xlabel('随机特征数 $N$'); ax.set_ylabel('均方误差')
ax.legend(loc='upper right', fontsize=7); ax.grid(True)
fig.tight_layout(pad=0.4)
prepare_figure(fig)
for ext in ['pdf', 'png']:
    fig.savefig(OUT / f'figure.{ext}', dpi=300, facecolor='white')
(OUT / 'figure-data.json').write_text(json.dumps({'Ns': Ns.tolist(), 'mean_mse': summary}, ensure_ascii=False, indent=1) + '\n')
mn = test['min-norm'].mean(0)
print({int(N): round(float(v), 3) for N, v in zip(Ns, np.median(test['min-norm'],0))})
print('ridge1e-1', {int(N): round(float(v), 3) for N, v in zip(Ns, test[1e-1].mean(0))})
