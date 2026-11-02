"""模加法上的延迟泛化与嵌入的傅里叶结构（图 fig:lt8-grokking-fourier）。

本书自行运行的小型合成实验，不是 Power 等（2022）或 Nanda 等（2023）的原始设定。
任务：c = (a + b) mod p，p = 47；全部 p^2 = 2209 个输入对中随机取 40% 训练，其余检验（种子 0）。
网络：a、b 各查 32 维嵌入 E，拼接后经 128 单元 ReLU 隐藏层，再线性输出 p 个类别分数；无偏置。
初始化：E ~ N(0,1)，W1 ~ N(0, 1/64)，W2 ~ N(0, 1/128)（同一种子）。
训练：交叉熵，全批量 AdamW（lr = 3e-3，beta = (0.9, 0.98)，解耦权重衰减系数 wd），2e4 步；
      wd 取 1.0、0.3、0，三次运行使用相同数据划分与初始化。
傅里叶分析：对 wd = 1.0 的末态嵌入 E（p x 32）沿输入维作离散傅里叶变换，
      按频率 k = 1..(p-1)/2 合并 k 与 p-k 两个分量后取 Frobenius 范数；
      右图把各 a 的嵌入投影到最强频率 k* 的两个实傅里叶基向量所张成的平面。
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

p, frac, T, lr, d, h = 47, 0.4, 20000, 3e-3, 32, 128
pairs = np.array([(a, b) for a in range(p) for b in range(p)]); lab = (pairs[:, 0] + pairs[:, 1]) % p
perm = np.random.default_rng(0).permutation(len(pairs)); ntr = int(frac * len(pairs))
tr, te = perm[:ntr], perm[ntr:]


def run(wd):
    rng = np.random.default_rng(0)
    P = {'E': rng.normal(0, 1, (p, d)), 'W1': rng.normal(0, 1 / np.sqrt(2 * d), (2 * d, h)),
         'W2': rng.normal(0, 1 / np.sqrt(h), (h, p))}
    M = {k: np.zeros_like(v) for k, v in P.items()}; V = {k: np.zeros_like(v) for k, v in P.items()}

    def fwd(idx):
        a, b = pairs[idx, 0], pairs[idx, 1]
        x = np.concatenate([P['E'][a], P['E'][b]], 1); z = x @ P['W1']; r = np.maximum(z, 0)
        return a, b, x, z, r, r @ P['W2']

    def acc(idx):
        return float((fwd(idx)[-1].argmax(1) == lab[idx]).mean())
    log = {'step': [], 'train': [], 'test': [], 'wnorm': []}
    b1, b2 = 0.9, 0.98
    steps_log = set(np.unique(np.round(np.logspace(0, np.log10(T), 200)).astype(int)).tolist())
    for t in range(1, T + 1):
        a, b, x, z, r, o = fwd(tr); o = o - o.max(1, keepdims=True)
        pr = np.exp(o); pr /= pr.sum(1, keepdims=True); pr[np.arange(ntr), lab[tr]] -= 1; go = pr / ntr
        G = {'W2': r.T @ go}; gz = (go @ P['W2'].T) * (z > 0); G['W1'] = x.T @ gz; gx = gz @ P['W1'].T
        gE = np.zeros_like(P['E']); np.add.at(gE, a, gx[:, :d]); np.add.at(gE, b, gx[:, d:]); G['E'] = gE
        for k in P:
            M[k] = b1 * M[k] + (1 - b1) * G[k]; V[k] = b2 * V[k] + (1 - b2) * G[k] ** 2
            P[k] -= lr * ((M[k] / (1 - b1 ** t)) / (np.sqrt(V[k] / (1 - b2 ** t)) + 1e-8) + wd * P[k])
        if t in steps_log:
            log['step'].append(t); log['train'].append(acc(tr)); log['test'].append(acc(te))
            log['wnorm'].append(float(sum((v ** 2).sum() for v in P.values())))
    return P, log


runs = {wd: run(wd) for wd in [1.0, 0.3, 0.0]}
E = runs[1.0][0]['E']
F = np.fft.fft(E, axis=0)
ks = np.arange(1, (p - 1) // 2 + 1)
power = np.array([np.sqrt(np.linalg.norm(F[k]) ** 2 + np.linalg.norm(F[p - k]) ** 2) for k in ks])
kstar = int(ks[np.argmax(power)])
cosb = np.cos(2 * np.pi * kstar * np.arange(p) / p); sinb = np.sin(2 * np.pi * kstar * np.arange(p) / p)
# 嵌入矩阵在频率 k* 上的二维投影：先取该频率的两个实系数向量，再把每个 E[a] 投到它们张成的平面
ca = cosb @ E; sa = sinb @ E
B = np.linalg.qr(np.stack([ca, sa], 1))[0]
proj = (E - E.mean(0)) @ B

fig = plt.figure(figsize=(164 * MM, 54 * MM))
gs = fig.add_gridspec(1, 3, width_ratios=[1.35, 1, 0.85])
ax = fig.add_subplot(gs[0, 0])
sty = {1.0: (BLUE, '-'), 0.3: (GREEN, '-'), 0.0: (RED, '-')}
for wd, (P, log) in runs.items():
    c, _ = sty[wd]
    ax.plot(log['step'], log['train'], color=c, lw=0.8, ls='--')
    ax.plot(log['step'], log['test'], color=c, lw=1.1, label=rf'$\lambda_{{\mathrm{{wd}}}}={wd:g}$')
ax.set_xscale('log'); ax.set_ylim(-0.03, 1.03); ax.set_xlabel('AdamW 步数'); ax.set_ylabel('准确率')
ax.set_title('虚线训练，实线检验', pad=3); ax.legend(loc='center left', fontsize=7); ax.grid(True)
ax = fig.add_subplot(gs[0, 1])
ax.bar(ks, power, color=BLUE, width=0.7)
ax.set_xlabel('频率 $k$'); ax.set_ylabel('嵌入的傅里叶分量范数'); ax.set_title(r'$\lambda_{\mathrm{wd}}=1$ 的末态嵌入', pad=3)
ax.grid(True, axis='y')
ax = fig.add_subplot(gs[0, 2])
ax.scatter(proj[:, 0], proj[:, 1], s=6, color=BLUE, zorder=3)
for a_ in [0, 1, 2]:
    ax.scatter(*proj[a_], s=14, color=RED, zorder=4)
    ax.annotate(f'$a={a_}$', proj[a_] * 0.72, ha='center', va='center', fontsize=7, color=RED)
for a_ in [0, 1]:
    ax.annotate('', xy=proj[a_ + 1] * 0.9, xytext=proj[a_] * 0.9,
                arrowprops=dict(arrowstyle='-|>', color=RED, lw=0.7, connectionstyle='arc3,rad=0.25'))
ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
for s_ in ax.spines.values():
    s_.set_visible(True)
ax.set_title(f'频率 $k^*={kstar}$ 平面上的嵌入', pad=3)
fig.tight_layout(pad=0.4, w_pad=1.0)
prepare_figure(fig)
for ext in ['pdf', 'png']:
    fig.savefig(OUT / f'figure.{ext}', dpi=300, facecolor='white')


def first(log, key, thr):
    for s, v in zip(log['step'], log[key]):
        if v >= thr:
            return s
    return None


angles = np.mod(np.arctan2(proj[:, 1], proj[:, 0]), 2 * np.pi)
summary = {wd: {'train_ge_0.99': first(log, 'train', 0.99), 'test_ge_0.5': first(log, 'test', 0.5),
                'test_ge_0.99': first(log, 'test', 0.99), 'final_test': log['test'][-1],
                'final_wnorm2': log['wnorm'][-1]} for wd, (P, log) in runs.items()}
summary['kstar'] = kstar
summary['power_top5'] = sorted([(int(k), float(v)) for k, v in zip(ks, power)], key=lambda x: -x[1])[:5]
summary['power_share_top5'] = float(np.sort(power ** 2)[-5:].sum() / (power ** 2).sum())
summary['proj_radius_cv'] = float(np.linalg.norm(proj, axis=1).std() / np.linalg.norm(proj, axis=1).mean())
(OUT / 'figure-data.json').write_text(json.dumps({'summary': {str(k): v for k, v in summary.items()},
    'logs': {str(wd): log for wd, (P, log) in runs.items()}}, ensure_ascii=False) + '\n')
print(json.dumps({str(k): v for k, v in summary.items()}, ensure_ascii=False, indent=1))
