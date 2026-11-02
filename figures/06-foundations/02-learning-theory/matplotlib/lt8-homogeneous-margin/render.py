"""齐次两层 ReLU 网络在可分数据上训练时的原始间隔与归一化间隔（图 fig:lt8-homogeneous-margin）。

模型：f(x) = sum_j a_j * relu(w_j^T x)，无偏置，对参数 theta=(a,W) 为 2 次正齐次。
数据：n = 24 个二维单位向量，角度 theta_i = 2*pi*i/24 + 0.13（避开边界），
      标签 y_i = sign(cos(2*theta_i))（四个象限交替，线性不可分）。
初始化：m = 30，a_j, w_j 各分量 ~ N(0, 0.3^2)，随机种子 0。
训练：平均逻辑损失的全批量梯度下降，步长 eta = 0.2，共 3e5 步。
记录：||theta||^2、最小原始间隔 min_i y_i f(x_i)、归一化间隔 min_i y_i f(x_i)/||theta||^2。
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

n, m, eta, T = 24, 30, 0.2, 300_000
ang = 2 * np.pi * np.arange(n) / n + 0.13
X = np.stack([np.cos(ang), np.sin(ang)], 1)
y = np.sign(np.cos(2 * ang))
rng = np.random.default_rng(0)
a = rng.normal(0, 0.3, m)
W = rng.normal(0, 0.3, (m, 2))

log_steps = np.unique(np.round(np.logspace(0, np.log10(T), 400)).astype(int))
rec = {'step': [], 'norm2': [], 'min_margin': [], 'norm_margin': [], 'loss': []}
first_sep = None
log_steps_set = set(log_steps.tolist())
for t in range(1, T + 1):
    H = X @ W.T                  # n x m
    R = np.maximum(H, 0)
    f = R @ a
    z = y * f
    g = -y / (1 + np.exp(np.clip(z, -50, 50))) / n   # dloss/df
    ga = R.T @ g
    gW = ((g[:, None] * (H > 0)) * a[None, :]).T @ X
    a -= eta * ga; W -= eta * gW
    if first_sep is None and np.all(z > 0):
        first_sep = t
    if t in log_steps_set:
        n2 = float(np.sum(a ** 2) + np.sum(W ** 2))
        rec['step'].append(t); rec['norm2'].append(n2)
        rec['min_margin'].append(float(z.min())); rec['norm_margin'].append(float(z.min() / n2))
        rec['loss'].append(float(np.mean(np.log1p(np.exp(-z)))))

steps = np.array(rec['step'])
fig, axes = plt.subplots(1, 2, figsize=(150 * MM, 52 * MM))
ax = axes[0]
pos = np.array(rec['min_margin']) > 0
ax.plot(steps, rec['norm2'], color=BLUE, lw=1.1, label=r'$\|\theta\|_2^2$')
ax.plot(steps[pos], np.array(rec['min_margin'])[pos], color=RED, lw=1.1,
        label='最小原始间隔 $q_{\min}$')
ax.set_xscale('log'); ax.set_yscale('log')
ax.set_xlabel('梯度下降步数'); ax.set_title('原始量：范数与间隔一同增长', pad=3)
ax.legend(loc='upper left'); ax.grid(True)
ax = axes[1]
nm = np.array(rec['norm_margin'])
ax.plot(steps[pos], nm[pos], color=GREEN, lw=1.1)
ax.set_xscale('log'); ax.set_xlabel('梯度下降步数'); ax.set_xlim(axes[0].get_xlim())
ax.set_ylabel(r'$q_{\min}/\|\theta\|_2^2$')
ax.set_title('归一化间隔趋于稳定', pad=3); ax.grid(True)
for ax in axes:
    ax.axvline(first_sep, color=MUTED, lw=0.6, ls='--')
axes[1].text(first_sep * 1.3, nm[pos].min() + 0.05 * (nm[pos].max() - nm[pos].min()),
             '全部分对', color=MUTED, fontsize=7.5)
fig.tight_layout(pad=0.4, w_pad=1.5)
prepare_figure(fig)
for ext in ['pdf', 'png']:
    fig.savefig(OUT / f'figure.{ext}', dpi=300, facecolor='white')
summary = {'first_all_correct_step': first_sep,
           'final': {k: rec[k][-1] for k in rec},
           'norm_margin_at_steps': {str(s): v for s, v in zip(rec['step'], rec['norm_margin']) if s in (1000, 10000, 100000, 300000) or s == rec['step'][-1]}}
(OUT / 'figure-data.json').write_text(json.dumps({'summary': summary, 'trace': rec}, ensure_ascii=False) + '\n')
print(json.dumps(summary, ensure_ascii=False, indent=1))
