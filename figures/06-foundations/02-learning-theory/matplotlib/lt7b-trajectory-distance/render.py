"""Distance between SGD trajectories on neighbouring samples (shared indices).

Sample S: z_i = linspace(-0.5, 0.5, 20); neighbour S' replaces z_1 = -0.5 by 0.5.
Step eta = 0.1, T = 300, R = 4000 shared index sequences (seed 1); plotted is
the Monte Carlo mean of |w_t - w'_t| and the corresponding theorem bound.
  convex:          l(w,z) = -z w            (L = 0.5, M = 0), w0 = 0
                   bound 2 L eta t / n
  strongly convex: l(w,z) = (w-z)^2/2 on W = [-1, 1], projected
                   (mu = M = 1, L = 1.5 on W), w0 = 0
                   bound 2L/(mu n) (1 - (1-mu eta)^t)
  non-convex:      l(w,z) = 1 - cos(w-z)     (L = M = 1), w0 = pi
                   bound (2L/(M n)) ((1+M eta)^t - 1)
"""
from pathlib import Path
import json, sys
import numpy as np
import matplotlib.pyplot as plt

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').exists())
D_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'figures/06-foundations/00-shared/academic-drawing'))
from plot_style import configure, prepare_figure, note, style_record, BLUE, GREEN, RED, MUTED, INK

configure()
rng = np.random.default_rng(1)
n, eta, T, R = 20, 0.1, 300, 4000
z = np.linspace(-0.5, 0.5, n)
z2 = z.copy(); z2[0] = 0.5
idx = rng.integers(0, n, size=(R, T))
t = np.arange(T + 1)
cases = [
    ('凸且光滑：$\\ell=-zw$', lambda w, z: -z, 0.0, None, 2 * 0.5 * eta * t / n, BLUE),
    ('逐观测强凸：$\\ell=(w-z)^2/2$', lambda w, z: (w - z), 0.0, 1.0, 2 * 1.5 / n * (1 - (1 - eta) ** t), GREEN),
    ('仅光滑：$\\ell=1-\\cos(w-z)$', lambda w, z: np.sin(w - z), np.pi, None, 2 / n * ((1 + eta) ** t - 1), RED),
]
fig, axes = plt.subplots(1, 3, figsize=(165 / 25.4, 52 / 25.4), layout='constrained', sharex=True)
rec = {}
for ax, (title, g, w0, B, bound, c) in zip(axes, cases):
    w = np.full(R, w0); v = np.full(R, w0); D = [0.0]
    for s in range(T):
        i = idx[:, s]
        w = w - eta * g(w, z[i]); v = v - eta * g(v, z2[i])
        if B is not None:
            w = np.clip(w, -B, B); v = np.clip(v, -B, B)
        D.append(float(np.mean(np.abs(w - v))))
    D = np.array(D)
    ax.plot(t, D, color=c, label='平均距离 $\\mathbb{E}_U|w_t-w\'_t|$')
    ax.plot(t, bound, color=INK, lw=0.7, ls='--', label='定理上界')
    top = 1.15 * max(D.max(), bound.max()) if bound.max() < 10 else 2.5 * D.max()
    ax.set(title=title, xlabel=r'迭代次数 $t$', ylim=(0, top), xlim=(0, T))
    rec[title] = {'mean_distance_at': {int(k): round(float(D[k]), 4) for k in [5, 20, 50, 100, 300]},
                  'bound_at': {int(k): float(f'{bound[k]:.4g}') for k in [5, 20, 50, 100, 300]}}
    if B is None and w0 == np.pi:
        frac = float(np.mean(np.abs(w - v) > 3))
        rec[title]['fraction_pairs_in_different_basins'] = frac
        note(ax.text(190, 0.88 * top, '上界在 $t=50$ 已达 %.1f' % bound[50], fontsize=7, color=MUTED, ha='center'))
        note(ax.text(190, 0.76 * top, '%.0f%% 的轨迹对最终相距约 $2\\pi$' % (100 * frac), fontsize=7, color=MUTED, ha='center'))
axes[0].set_ylabel('参数距离')
axes[0].legend(loc='upper left', fontsize=7)
prepare_figure(fig)
for ext in ['pdf', 'png']:
    fig.savefig(D_DIR / ('figure.' + ext), dpi=300)
plt.close(fig)
(D_DIR / 'data.json').write_text(json.dumps({'n': n, 'eta': eta, 'T': T, 'R': R, 'seed': 1, 'results': rec}, ensure_ascii=False, indent=2) + '\n')
gen = {'method': 'Matplotlib', 'date': '2026-10-30', 'source': 'Monte Carlo SGD simulation with shared index sequences (numpy seed 1)',
       'parameters': {'n': n, 'eta': eta, 'T': T, 'R': R}, 'physical_size_mm': [165, 52], 'style': style_record()}
(D_DIR / 'generation.json').write_text(json.dumps(gen, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(rec, ensure_ascii=False, indent=1))
