"""Gradient descent on separable logistic regression: norm diverges, direction -> max margin.

Data: positive points P = [(1,.25),(2.5,2),(.4,1.6),(3,.6),(1.8,1.1)], negatives -P
(so the homogeneous hard-margin direction is found by maximising the minimum
margin over unit directions on a grid of 200001 angles; no QP solver needed).
Loss: mean logistic loss; w0 = 0; eta = 0.9 n / ||X||_2^2 (< n/||X||_2^2).
Recorded at log-spaced t up to 1e6.
"""
from pathlib import Path
import json, sys
import numpy as np
import matplotlib.pyplot as plt

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').exists())
D_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'figures/06-foundations/00-shared/academic-drawing'))
from plot_style import configure, prepare_figure, note, style_record, BLUE, GREEN, RED, PURPLE, YELLOW, MUTED, INK, BLUE_FILL, RED_FILL

configure()
np.seterr(all="ignore")  # spurious BLAS matmul flags on this platform; values checked finite below
P = np.array([[1.0, 0.25], [2.5, 2.0], [0.4, 1.6], [3.0, 0.6], [1.8, 1.1]])
X = np.vstack([P, -P]); y = np.r_[np.ones(5), -np.ones(5)]; n = len(y)
A = y[:, None] * X
ang = np.linspace(0, 2 * np.pi, 200001)
mins = np.min(np.cos(ang)[None, :] * A[:, :1] + np.sin(ang)[None, :] * A[:, 1:], axis=0)
k = int(np.argmax(mins)); u_svm = np.array([np.cos(ang[k]), np.sin(ang[k])]); gamma_svm = float(mins[k])
eta = 0.9 * n / np.linalg.norm(X, 2) ** 2
marks = sorted(set(np.unique(np.logspace(0, 6, 121).astype(int)).tolist()))
mk = set(marks)
w = np.zeros(2); rec = {}
for t in range(1, 10 ** 6 + 1):
    s = A @ w
    w = w + eta * (A / (1 + np.exp(s))[:, None]).mean(0)
    if t in mk:
        rec[t] = w.copy()
ts = np.array(marks)
W = np.array([rec[t] for t in marks])
nrm = np.linalg.norm(W, axis=1)
U = W / nrm[:, None]
angle = np.degrees(np.arccos(np.clip(U @ u_svm, -1, 1)))
mmin = (A @ U.T).min(0)
assert np.all(np.isfinite(mmin)) and np.all(np.isfinite(W))

fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(165 / 25.4, 56 / 25.4), layout='constrained',
                                 gridspec_kw={'width_ratios': [1.05, 1, 1]})
a1.scatter(P[:, 0], P[:, 1], s=12, color=BLUE, marker='o', zorder=3, )
a1.scatter(-P[:, 0], -P[:, 1], s=12, facecolor='white', edgecolor=RED, marker='s', zorder=3)
xs = np.linspace(-3.5, 3.5, 2)
for t, c, ls in [(10, MUTED, ':'), (1000, PURPLE, '--')]:
    u = rec[t] / np.linalg.norm(rec[t])
    a1.plot(xs * (-u[1]), xs * u[0], color=c, ls=ls, lw=0.9, label=r'边界，$t=10^{%d}$' % round(np.log10(t)))
a1.plot(xs * (-u_svm[1]), xs * u_svm[0], color=GREEN, lw=1.1, label='最大间隔边界')
sv = np.where(np.isclose(A @ u_svm, gamma_svm, atol=1e-3))[0]
a1.scatter(X[sv, 0], X[sv, 1], s=42, facecolor='none', edgecolor=GREEN, lw=0.8, zorder=4)
a1.set(xlim=(-3.4, 3.4), ylim=(-2.4, 2.4), aspect='equal', xlabel='$x_1$', ylabel='$x_2$')
a1.legend(loc='lower center', bbox_to_anchor=(0.5, 1.0), fontsize=6.5, handlelength=1.6, borderaxespad=0.2)
a2.semilogx(ts, nrm, color=BLUE)
a2.semilogx(ts, np.log(ts) / gamma_svm, color=MUTED, lw=0.6, ls='--')
note(a2.text(1.5, 0.92 * np.log(1e6) / gamma_svm, '虚线：斜率参照\n' + r'$\log t/\gamma_{\mathrm{svm}}$', fontsize=7, color=MUTED, va='top'))
a2.set(xlabel=r'迭代次数 $t$', ylabel=r'$\|\mathbf{w}^{(t)}\|_2$', ylim=(0, 1.15 * max(nrm.max(), np.log(1e6) / gamma_svm)))
a3.semilogx(ts, angle, color=RED, label='与最大间隔方向的夹角（度）')
a3.set(xlabel=r'迭代次数 $t$', ylabel='夹角（度）', ylim=(0, 16))
b3 = a3.twinx()
b3.semilogx(ts, mmin, color=GREEN, ls='--', label='最小归一化间隔')
b3.axhline(gamma_svm, color=GREEN, lw=0.6, ls=':')
b3.set_ylim(0.90, 1.03)
b3.set_ylabel('最小归一化间隔', color=GREEN)
b3.spines['right'].set_visible(True)
note(b3.text(1.5, gamma_svm + 0.004, r'$\gamma_{\mathrm{svm}}=%.3f$' % gamma_svm, fontsize=7, color=GREEN))
h1, l1 = a3.get_legend_handles_labels(); h2, l2 = b3.get_legend_handles_labels()
a3.legend(h1 + h2, ['夹角', '最小间隔'], loc='lower left', fontsize=7)
prepare_figure(fig)
for ext in ['pdf', 'png']:
    fig.savefig(D_DIR / ('figure.' + ext), dpi=300)
plt.close(fig)

sel = [1, 10, 100, 1000, 10000, 100000, 1000000]
table = {t: {'norm': round(float(np.linalg.norm(rec[t])), 3),
             'angle_deg': round(float(np.degrees(np.arccos(np.clip(rec[t] @ u_svm / np.linalg.norm(rec[t]), -1, 1)))), 3),
             'min_margin': round(float((A @ (rec[t] / np.linalg.norm(rec[t]))).min()), 4)} for t in sel}
data = {'positives': P.tolist(), 'eta': eta, 'u_svm': u_svm.tolist(), 'gamma_svm': gamma_svm,
        'support_vectors_index': sv.tolist(), 'table': table}
(D_DIR / 'data.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
gen = {'method': 'Matplotlib', 'date': '2026-10-30', 'source': 'exact full-batch gradient descent on logistic loss; SVM direction by angular grid search',
       'parameters': {'eta': eta, 'T': 10 ** 6, 'w0': [0, 0]}, 'physical_size_mm': [165, 56], 'style': style_record()}
(D_DIR / 'generation.json').write_text(json.dumps(gen, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(data, indent=1))
