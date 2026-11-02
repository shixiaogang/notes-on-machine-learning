"""AdaBoost on a 10-point 1D teaching sample with exact weighted threshold stumps.

Inputs x_i = i (i = 1..10), labels y = (+,+,+,-,+,+,-,-,+,-).
Weak learner: exact minimiser of weighted error over thresholds
{0.5, 1.5, ..., 10.5} and both orientations (ties: first found).
Left panel: weights D^(t)(i) for t = 1..30 (heat map).
Right panel: training 0-1 error of H_T, prod_t Z^(t), exp(-2 sum gamma_t^2).
"""
from pathlib import Path
import json, sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').exists())
D_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'figures/06-foundations/00-shared/academic-drawing'))
from plot_style import configure, prepare_figure, note, style_record, BLUE, BLUE_FILL, GREEN, RED, INK, MUTED

configure()
x = np.arange(1, 11).astype(float)
y = np.array([1, 1, 1, -1, 1, 1, -1, -1, 1, -1])
n = len(x)
thr = np.concatenate([[0.5], x + 0.5])


def stump(D):
    best = None
    for t in thr:
        for s in [1, -1]:
            h = np.where(x > t, s, -s)
            e = D[h != y].sum()
            if best is None or e < best[0] - 1e-12:
                best = (e, t, s, h)
    return best


T_MAX = 30
D = np.ones(n) / n
F = np.zeros(n)
weights = [D.copy()]
err, prodz, expb, rounds = [], [], [], []
P, G = 1.0, 0.0
for T in range(1, T_MAX + 1):
    e, t, s, h = stump(D)
    a = 0.5 * np.log((1 - e) / e)
    P *= 2 * np.sqrt(e * (1 - e))
    G += (0.5 - e) ** 2
    F += a * h
    D = D * np.exp(-a * y * h)
    D /= D.sum()
    weights.append(D.copy())
    err.append(float(np.mean(np.where(F >= 0, 1, -1) != y)))
    prodz.append(P)
    expb.append(float(np.exp(-2 * G)))
    rounds.append({'t': T, 'e': round(float(e), 4), 'threshold': float(t), 'orientation': int(s), 'alpha': round(float(a), 4)})
W = np.array(weights[:T_MAX])  # D^(1..T_MAX)

cmap = LinearSegmentedColormap.from_list('blue', ['#FFFFFF', BLUE_FILL, BLUE, '#3B4E66'])
fig, (a1, a2) = plt.subplots(1, 2, figsize=(165 / 25.4, 58 / 25.4), layout='constrained',
                             gridspec_kw={'width_ratios': [1.15, 1]})
im = a1.imshow(W.T, aspect='auto', cmap=cmap, origin='lower', extent=(0.5, T_MAX + 0.5, 0.5, n + 0.5), vmin=0, vmax=0.35)
a1.set(xlabel=r'轮次 $t$', ylabel=r'样本 $i$（$x_i=i$）', yticks=range(1, 11))
lab = ['+' if v > 0 else '−' for v in y]
a1.set_yticklabels([f'{i} ({l})' for i, l in zip(range(1, 11), lab)], fontsize=7)
cb = fig.colorbar(im, ax=a1, fraction=0.05, pad=0.02)
cb.set_label(r'权重 $D^{(t)}(i)$', fontsize=7.5)
cb.ax.tick_params(labelsize=7)
tt = np.arange(1, T_MAX + 1)
a2.semilogy(tt, prodz, color=BLUE, label=r'$\prod_{s\leq t}Z^{(s)}$')
a2.semilogy(tt, expb, color=GREEN, ls='--', label=r'$\exp(-2\sum_{s\leq t}(\gamma^{(s)})^2)$')
er = np.array(err)
a2.plot(tt[er > 0], er[er > 0], ls='none', marker='o', ms=2.5, color=RED, label=r'训练错误率 $\hat R_S(H_t)>0$')
z0 = int(np.argmax(er == 0)) + 1
zlast = int(np.max(np.nonzero(er > 0)[0])) + 1
note(a2.text(zlast + 1.5, 0.06, r'$t=%d$ 及 $t\geq%d$ 时训练错误为0' % (z0, zlast + 1), fontsize=7, color=RED))
a2.set(xlabel=r'轮次 $t$', ylabel='训练错误或上界', ylim=(0.004, 1.2), xlim=(1, T_MAX))
a2.legend(loc='lower left', fontsize=7)
prepare_figure(fig)
for ext in ['pdf', 'png']:
    fig.savefig(D_DIR / ('figure.' + ext), dpi=300)
plt.close(fig)

data = {'x': x.tolist(), 'y': y.tolist(), 'rounds': rounds, 'train_error': err,
        'prod_Z': [round(v, 5) for v in prodz], 'exp_bound': [round(v, 5) for v in expb],
        'weights_round1_to_4': [np.round(w, 4).tolist() for w in weights[:5]], 'first_zero_error_round': z0, 'last_nonzero_round': zlast}
(D_DIR / 'data.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
gen = {'method': 'Matplotlib', 'date': '2026-10-30', 'source': 'exact AdaBoost run on a constructed 10-point teaching sample',
       'parameters': {'T': T_MAX, 'weak_learner': 'exact weighted threshold stumps, both orientations'},
       'physical_size_mm': [165, 58], 'style': style_record()}
(D_DIR / 'generation.json').write_text(json.dumps(gen, ensure_ascii=False, indent=2) + '\n')
print(rounds[:6], z0, prodz[9], expb[9], prodz[29])
