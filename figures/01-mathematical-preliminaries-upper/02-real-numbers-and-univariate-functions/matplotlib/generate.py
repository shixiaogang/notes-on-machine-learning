# coding: utf-8
"""Analytic teaching charts for volume one, part 2 (real numbers and univariate functions).

Every curve is an explicit formula listed in the saved facts; no sampled data.
Run from any directory:  python3 figures/01-mathematical-preliminaries-upper/02-real-numbers-and-univariate-functions/matplotlib/generate.py [name ...]
"""
from pathlib import Path
import sys
import numpy as np

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/01-mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL

D = Path(__file__).resolve().parent


def power_sequence_nonuniform():
    fig, ax = figure(height_mm=52)
    x = np.linspace(0, 1, 1201)
    ns = [1, 2, 5, 20, 80]
    colors = [BLUE, GREEN, YELLOW, RED, PURPLE]
    for n, c in zip(ns, colors):
        ax.plot(x, x**n, color=c, label=rf'$n={n}$')
        xc = 0.5**(1/n)
        ax.plot([xc], [0.5], 'o', color=c, ms=2.6)
    ax.plot([0, 1], [0, 0], color=MUTED, lw=2.2, alpha=.45, solid_capstyle='butt')
    ax.plot([1], [1], 'o', color=INK, ms=3.4)
    ax.plot([1], [0], 'o', mfc='white', mec=INK, ms=3.4)
    ax.axhline(0.5, color=MUTED, lw=.6, ls='--')
    ax.text(0.02, 0.53, '误差 1/2', color=MUTED, fontsize=7.5)
    ax.set(xlim=(0, 1.04), ylim=(-0.04, 1.06), xlabel=r'$x$', ylabel=r'$f_n(x)=x^n$')
    ax.set_xticks([0, .25, .5, .75, 1]); ax.set_yticks([0, .5, 1])
    ax.legend(loc='upper left', ncol=2, handlelength=1.6, columnspacing=1.2)
    save(fig, D/'power-sequence-nonuniform', 'figure', {
        'curves': 'f_n(x)=x**n on [0,1]', 'n': ns,
        'crossing_points': {str(n): 0.5**(1/n) for n in ns},
        'pointwise_limit': '0 on [0,1), 1 at x=1', 'sup_error_on_[0,1)': 1})


def geometric_partial_sums():
    fig, ax = figure(height_mm=54)
    x = np.linspace(-0.995, 0.93, 1600)
    ax.plot(x, 1/(1-x), color=INK, lw=1.3, label=r'$1/(1-x)$')
    for N, c, ls in [(2, BLUE, '-'), (5, GREEN, '-'), (10, PURPLE, '-')]:
        s = (1 - x**(N+1))/(1 - x)
        ax.plot(x, s, color=c, ls=ls, label=rf'$S_{{{N}}}(x)$')
    ax.axvline(1, color=MUTED, lw=.6, ls='--'); ax.axvline(-1, color=MUTED, lw=.6, ls='--')
    ax.set(xlim=(-1.05, 1.05), ylim=(-1, 8), xlabel=r'$x$', ylabel='函数值')
    ax.set_xticks([-1, -.5, 0, .5, 1]); ax.set_yticks([0, 2, 4, 6, 8])
    ax.legend(loc='upper left', handlelength=1.6)
    save(fig, D/'geometric-partial-sums', 'figure', {
        'partial_sums': 'S_N(x)=(1-x**(N+1))/(1-x)', 'N': [2, 5, 10], 'limit': '1/(1-x) for |x|<1',
        'error': '|x|**(N+1)/|1-x|', 'x_range': [-0.995, 0.93], 'y_clip': [-1, 8]})


def convex_chord_tangent():
    fig, ax = figure(height_mm=50)
    x = np.linspace(-2.2, 1.6, 800)
    f = lambda t: np.exp(t)/2
    ax.plot(x, f(x), color=INK, lw=1.3, label=r'$f(x)=e^x/2$')
    a, b = -1.5, 1.0
    ax.plot([a, b], [f(a), f(b)], color=GREEN, lw=1.1, label='弦')
    ax.plot([a, b], [f(a), f(b)], 'o', color=GREEN, ms=3)
    ax.plot(x, 0.5 + 0.5*x, color=BLUE, lw=1.1, ls='--', label='切线')
    ax.plot([0], [0.5], 'o', color=BLUE, ms=3)
    xs = np.linspace(a, b, 200)
    ax.fill_between(xs, f(xs), f(a) + (f(b)-f(a))/(b-a)*(xs-a), color=GREEN_FILL, lw=0)
    ax.set(xlim=(-2.2, 1.6), ylim=(-0.6, 2.4), xlabel=r'$x$', ylabel=r'$y$')
    ax.set_xticks([-2, -1.5, -1, 0, 1]); ax.set_yticks([0, 1, 2])
    ax.legend(loc='upper left', handlelength=1.8)
    save(fig, D/'convex-chord-tangent', 'figure', {
        'function': 'exp(x)/2', 'chord_endpoints': [a, b], 'tangent_point': 0,
        'tangent_line': 'y=1/2+x/2', 'shaded': 'region between graph and chord on [a,b]'})


def finite_difference_error():
    fig, ax = figure(height_mm=56)
    x0 = 1.0
    exact = np.exp(x0)
    hs = np.logspace(-15, -0.3, 300)
    fwd = np.array([abs((np.exp(x0+h)-np.exp(x0))/h - exact) for h in hs])
    cen = np.array([abs((np.exp(x0+h)-np.exp(x0-h))/(2*h) - exact) for h in hs])
    eps = np.finfo(float).eps
    ax.loglog(hs, fwd, 'o', color=BLUE, ms=1.6, label='前向差分')
    ax.loglog(hs, cen, 's', color=GREEN, ms=1.6, label='中心差分')
    ax.loglog(hs, exact*hs/2 + 2*eps*exact/hs, color=BLUE, lw=.8, ls='--')
    ax.loglog(hs, exact*hs**2/6 + eps*exact/hs, color=GREEN, lw=.8, ls='--')
    ax.set(xlim=(1e-15, 0.5), ylim=(1e-12, 10), xlabel=r'$h$', ylabel='绝对误差')
    ax.set_xticks([1e-15, 1e-12, 1e-9, 1e-6, 1e-3]); ax.set_yticks([1e-12, 1e-9, 1e-6, 1e-3, 1])
    ax.legend(loc='upper right')
    hopt_f = 2*np.sqrt(eps); hopt_c = (3*eps)**(1/3)
    save(fig, D/'finite-difference-error', 'figure', {
        'function': 'exp', 'x0': x0, 'arithmetic': 'IEEE double precision (numpy float64)',
        'h_grid': 'logspace(-15,-0.3,300)', 'machine_epsilon': eps,
        'model_forward': 'e*h/2+2*eps*e/h', 'model_central': 'e*h**2/6+eps*e/h',
        'model_optimal_h': {'forward': hopt_f, 'central': hopt_c}})


def riemann_sums():
    import matplotlib.patches as mp
    fig, axes = figure(width_mm=169, height_mm=52, ncols=2)
    x = np.linspace(0, 3, 600)
    pts = [0, 0.4, 1.0, 1.4, 2.1, 2.5, 3.0]
    tags = [0.3, 0.55, 1.3, 1.6, 2.3, 2.9]
    ax = axes[0]
    for a, b, t in zip(pts[:-1], pts[1:], tags):
        v = np.cos(t)
        c, fc = (BLUE, BLUE_FILL) if v >= 0 else (RED, '#F0E5E6')
        ax.add_patch(mp.Rectangle((a, 0), b-a, v, facecolor=fc, edgecolor=c, lw=.7))
        ax.plot([t], [v], 'o', color=INK, ms=2.6)
    ax.plot(x, np.cos(x), color=INK, lw=1.2)
    ax.axhline(0, color=MUTED, lw=.6)
    ax.set(xlim=(0, 3), ylim=(-1.1, 1.1), xlabel=r'$x$', ylabel=r'$\cos x$', title='(a) 一个黎曼和')
    ax = axes[1]
    n = 12; xs = np.linspace(0, 3, n+1)
    for a, b in zip(xs[:-1], xs[1:]):
        lo, hi = np.cos(b), np.cos(a)  # cos decreasing on [0, 3]
        ax.add_patch(mp.Rectangle((a, 0), b-a, lo, facecolor=BLUE_FILL, edgecolor=BLUE, lw=.6))
        ax.add_patch(mp.Rectangle((a, lo), b-a, hi-lo, facecolor=GREEN_FILL, edgecolor=GREEN, lw=.6))
    ax.plot(x, np.cos(x), color=INK, lw=1.2)
    ax.axhline(0, color=MUTED, lw=.6)
    ax.set(xlim=(0, 3), ylim=(-1.1, 1.1), xlabel=r'$x$', title='(b) 下和与上和')
    U = sum((xs[1]-xs[0])*np.cos(a) for a in xs[:-1]); Lw = sum((xs[1]-xs[0])*np.cos(b) for b in xs[1:])
    save(fig, D/'riemann-sums', 'figure', {
        'function': 'cos(x) on [0,3]', 'panel_a_partition': pts, 'panel_a_tags': tags,
        'panel_a_sum': float(sum((b-a)*np.cos(t) for a, b, t in zip(pts[:-1], pts[1:], tags))),
        'panel_b_equal_segments': n, 'upper_sum': float(U), 'lower_sum': float(Lw), 'U_minus_L': float(U-Lw),
        'exact_integral': float(np.sin(3))})


def narrow_spikes():
    fig, ax = figure(height_mm=50)
    for n, c in [(2, BLUE), (4, GREEN), (8, PURPLE)]:
        xs = [0, 1/n, 2/n, 1]; ys = [0, n, 0, 0]
        ax.plot(xs, ys, color=c, label=rf'$f_{{{n}}}$')
    ax.set(xlim=(0, 1), ylim=(0, 8.6), xlabel=r'$x$', ylabel=r'$f_n(x)$')
    ax.set_xticks([0, .25, .5, 1]); ax.set_yticks([0, 2, 4, 8])
    ax.legend(loc='upper right')
    save(fig, D/'narrow-spikes', 'figure', {
        'definition': 'triangle on [0,2/n] with apex (1/n,n), zero elsewhere', 'n': [2, 4, 8],
        'integral_each': 1, 'pointwise_limit': 0, 'sup_norm': 'n'})


def quadrature_rules():
    fig, axes = figure(width_mm=169, height_mm=54, ncols=2)
    ax = axes[0]
    f = lambda t: np.exp(2*t)/3
    x = np.linspace(0, 1, 400)
    ax.fill_between([0, 1], [f(.5), f(.5)], color=YELLOW_FILL, lw=0)
    ax.plot([0, 1], [f(.5), f(.5)], color=YELLOW, lw=1.1, label='中点矩形')
    ax.plot([0, 1], [f(0), f(1)], color=GREEN, lw=1.1, ls='--', label='梯形直线')
    # quadratic through the three nodes 0, 1/2, 1
    A = f(.5); C = (f(0)+f(1)-2*f(.5))/(2*.25); B = (f(1)-f(0))/1.0
    ax.plot(x, A + B*(x-.5) + C*(x-.5)**2, color=PURPLE, lw=1.1, ls='-.', label='Simpson抛物线')
    ax.plot(x, f(x), color=INK, lw=1.3, label=r'$f(x)$')
    ax.plot([0, .5, 1], [f(0), f(.5), f(1)], 'o', color=INK, ms=3)
    ax.set(xlim=(-0.02, 1.02), ylim=(0, 2.6), xlabel=r'$x$', title='(a) 一段上的近似')
    ax.set_xticks([0, .5, 1]); ax.legend(loc='upper left', fontsize=7)
    ax = axes[1]
    exact = np.e - 1
    ns = np.array([2, 4, 8, 16, 32, 64, 128, 256])
    def left(n): h = 1/n; return h*np.exp(np.arange(n)*h).sum()
    def mid(n): h = 1/n; return h*np.exp(np.arange(n)*h + h/2).sum()
    def trap(n): h = 1/n; y = np.exp(np.arange(n+1)*h); return h*(y.sum() - (y[0]+y[-1])/2)
    def simp(n): h = 1/n; y = np.exp(np.arange(n+1)*h); return h/3*(y[0]+y[-1]+4*y[1:-1:2].sum()+2*y[2:-1:2].sum())
    data = {}
    for name, rule, c, m in [('左矩形', left, BLUE, 'o'), ('中点', mid, YELLOW, 's'), ('梯形', trap, GREEN, '^'), ('Simpson', simp, PURPLE, 'D')]:
        err = np.array([abs(rule(n) - exact) for n in ns])
        ax.loglog(ns, err, marker=m, color=c, ms=3, lw=1, label=name)
        data[name] = err.tolist()
    ax.set(xlabel='段数 n', ylabel='绝对误差', title='(b) 积分误差随段数的变化')
    ax.set_xticks([2, 8, 32, 128]); ax.set_xticklabels(['2', '8', '32', '128'])
    ax.legend(loc='lower left', fontsize=7)
    save(fig, D/'quadrature-rules', 'figure', {
        'panel_a_function': 'exp(2x)/3 on [0,1]', 'panel_b_integrand': 'exp(x) on [0,1]', 'exact': exact,
        'n': ns.tolist(), 'errors': data, 'arithmetic': 'IEEE double precision'})


DRAWERS = {f.__name__.replace('_', '-'): f for f in [power_sequence_nonuniform, geometric_partial_sums, convex_chord_tangent, finite_difference_error, riemann_sums, narrow_spikes, quadrature_rules]}

if __name__ == '__main__':
    names = sys.argv[1:] or list(DRAWERS)
    for name in names:
        DRAWERS[name]()
        print('generated', name)
