"""Exact teaching examples for candidate approximation and regression losses.

Run from any directory with Python, NumPy and Matplotlib. No sampled observations
or numerical optimization enter these figures; data.json records every example.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').exists())
BASE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('book_plot_style', ROOT / 'figures/00-shared/academic-drawing/plot_style.py')
style = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = style
spec.loader.exec_module(style)
style.configure()

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.text import Text
import numpy as np

WIDTH, HEIGHT = 159, 76

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def canvas():
    fig, axes = plt.subplots(1, 2, figsize=(WIDTH / 25.4, HEIGHT / 25.4))
    fig.subplots_adjust(left=.078, right=.982, bottom=.29, top=.84, wspace=.28)
    return fig, axes

def axes_style(ax, xlabel, ylabel):
    ax.set_xlabel(xlabel, labelpad=3)
    ax.set_ylabel(ylabel, labelpad=3)
    ax.tick_params(length=2.5, pad=2)

def export(fig, key, data, checks, explanation):
    folder = BASE / key
    folder.mkdir(exist_ok=True)
    data_file = folder / 'data.json'
    data_file.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    style.prepare_figure(fig)
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    outside = []
    for artist in fig.findobj(Text):
        if not artist.get_visible() or not artist.get_text():
            continue
        box = artist.get_window_extent(renderer)
        if box.x0 < -1 or box.y0 < -1 or box.x1 > fig.bbox.x1 + 1 or box.y1 > fig.bbox.y1 + 1:
            outside.append(artist.get_text())
    assert not outside, outside
    for suffix in ['pdf', 'svg', 'png']:
        fig.savefig(folder / ('figure.' + suffix), dpi=220, metadata={'Creator': 'Book objective figure generator'} if suffix == 'pdf' else None)
    record = {
        'key': key, 'route': 'Matplotlib', 'date': '2026-10-12',
        'generator': str(Path(__file__).relative_to(ROOT)),
        'generator_sha256': sha(Path(__file__)),
        'style': style.style_record(),
        'input_sha256': {str(data_file.relative_to(ROOT)): sha(data_file)},
        'native_size_mm': [WIDTH, HEIGHT], 'body_width_mm': WIDTH,
        'example_type': 'Author constructed exact, dimensionless teaching example',
        'scientific_checks': checks,
        'render_checks': {'visible_text_outside_canvas': outside, 'main_font_pt': 8, 'png_dpi': 220},
    }
    (folder / 'generation.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    (folder / 'README.md').write_text(
        '# ' + key + '\n\n' + explanation + '\n\n'
        'Reproduce with `python3 figures/07-classic-models/00-shared/matplotlib/regression-objective-figures.py`. '
        'The generator uses the actual project fonts and shared palette. The PDF and SVG are vector exports; '
        'the PNG is a 220 dpi preview. `data.json` stores the exact example and `generation.json` stores its checks.\n')
    plt.close(fig)

def approximation():
    fig, axes = canvas()
    x = np.linspace(-1, 1, 401)
    target = x ** 2
    best = np.full_like(x, 1/3)
    for ax in axes:
        ax.plot(x, target, color=style.INK, label=r'目标 $x^2$', zorder=3)
        ax.set_xlim(-1.04, 1.04)
        ax.set_ylim(-.06, 1.08)
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([0, 1/3, 1], ['0', r'$1/3$', '1'])
        axes_style(ax, r'输入 $x$（无量纲）', '函数值（无量纲）')
    axes[0].fill_between(x, target, best, color=style.BLUE_FILL, zorder=0)
    axes[0].plot(x, best, '--', color=style.BLUE, label=r'最佳仿射候选 $1/3$')
    axes[1].plot(x, target, '--', color=style.GREEN, linewidth=1.6, label=r'最佳二次候选 $x^2$', zorder=4)
    axes[0].set_title(r'仿射候选：$a+bx$', pad=8)
    axes[1].set_title(r'二次候选：$a+bx+cx^2$', pad=8)
    for ax, center in zip(axes, [.276, .786]):
        ax.legend(loc='lower center', bbox_to_anchor=(center, .02), bbox_transform=fig.transFigure, ncol=1, handlelength=2, borderaxespad=0, labelspacing=.25)
    axes[0].text(.5, .94, r'$\frac{1}{2}\inf\|f-m\|_{L^2}^2=2/45$', ha='center', va='top', transform=axes[0].transAxes)
    axes[1].text(.5, .94, r'$\inf\|f-m\|_{L^2}=0$', ha='center', va='top', transform=axes[1].transAxes)
    error = .5 * (1/5 - 1/9)
    assert np.isclose(error, 2/45)
    export(fig, 'regression-feature-approximation',
           {'input_distribution': 'Uniform[-1,1]', 'target': 'x**2', 'best_affine': '1/3', 'best_quadratic': 'x**2',
            'half_integrated_squared_error': {'affine': error, 'quadratic': 0}, 'display_grid_points': len(x)},
           {'exact_uniform_moments': {'E[X]': 0, 'E[X**2]': 1/3, 'E[X**3]': 0, 'E[X**4]': 1/5}, 'affine_projection_error_equals_2_over_45': True},
           'Compare the entire affine and quadratic candidate spaces with the fixed target x² under Uniform[-1,1]. '
           'The affine optimum follows from exact orthogonal projection; neither curve is a fitted sample result.')

def quantile():
    fig, axes = canvas()
    taus = [.25, .5, .75]
    colors = [style.BLUE, style.GREEN, style.RED]
    dashes = ['-', '--', ':']
    responses = np.array([0., 1., 2., 4., 8.])
    residual = np.linspace(-4, 4, 321)
    a = np.unique(np.r_[np.linspace(-.5, 8.5, 401), responses])
    minima = []
    for tau, color, line in zip(taus, colors, dashes):
        loss = np.maximum(tau * residual, (tau - 1) * residual)
        axes[0].plot(residual, loss, linestyle=line, color=color, label=rf'$\tau={tau:g}$')
        r = responses[:, None] - a
        objective = np.maximum(tau*r, (tau-1)*r).mean(axis=0)
        optimum = responses[int(np.ceil(len(responses)*tau)) - 1]
        exact_min = np.maximum(tau*(responses-optimum), (tau-1)*(responses-optimum)).mean()
        assert np.isclose(objective.min(), exact_min)
        assert a[np.argmin(objective)] == optimum
        axes[1].plot(a, objective, linestyle=line, color=color)
        axes[1].scatter([optimum], [exact_min], marker='o', s=20, color=color, zorder=4)
        minima.append({'tau': tau, 'minimizing_prediction': optimum, 'mean_pinball_loss': exact_min})
    axes[0].axvline(0, color=style.GRID, linewidth=.6, zorder=0)
    axes[0].set_xlim(-4.2, 4.2)
    axes[0].set_ylim(-.05, 3.6)
    axes[0].set_xticks([-4, -2, 0, 2, 4])
    axes[0].set_yticks([0, 1, 2, 3])
    axes[0].set_title('非对称地计入两侧残差', pad=8)
    axes_style(axes[0], r'残差 $r=y-a$（无量纲）', r'分位数损失 $\rho_\tau(r)$')
    axes[0].text(.2, .92, '高估', transform=axes[0].transAxes, ha='center')
    axes[0].text(.8, .92, '低估', transform=axes[0].transAxes, ha='center')
    axes[0].legend(loc='lower center', bbox_to_anchor=(.276, .04), bbox_transform=fig.transFigure, ncol=3, handlelength=1.6, columnspacing=.8, borderaxespad=0)
    axes[1].set_title('同一组响应，不同的最优阈值', pad=8)
    axes[1].set_xlim(-.5, 8.5)
    axes[1].set_ylim(.3, 5.8)
    axes[1].set_xticks([0, 1, 2, 4, 8])
    axes[1].set_yticks([1, 3, 5])
    axes_style(axes[1], r'常数预测 $a$（无量纲）', r'平均损失 $\frac{1}{5}\sum_i\rho_\tau(y_i-a)$')
    axes[1].text(.5, .95, '响应：0，1，2，4，8', ha='center', va='top', transform=axes[1].transAxes)
    fig.text(.786, .065, '圆点为各目标的最小值', ha='center', va='center')
    export(fig, 'regression-quantile-objective', {'responses': responses.tolist(), 'taus': taus, 'minima': minima, 'definition': 'rho_tau(r)=max(tau*r,(tau-1)*r)'},
           {'unique_minimum_order_statistic': 'ceil(n*tau); n*tau is noninteger for each example', 'grid_minima_checked_against_exact_values': True},
           'The first panel shows asymmetric pinball losses. The second minimizes the average loss for five fixed dimensionless responses. '
           'Each minimum is the exact empirical quantile; the intercept-only example isolates the learning objective.')

def svr():
    fig, axes = canvas()
    x = np.array([-2., -1.25, -.5, 0., .6, 1.2, 2.])
    residual = np.array([-.2, .8, -.3, -1., .1, .5, .9])
    prediction = 1 + .5*x
    y = prediction + residual
    epsilon = .5
    excess = np.maximum(np.abs(residual)-epsilon, 0)
    grid = np.linspace(-2.2, 2.2, 201)
    curve = 1+.5*grid
    axes[0].fill_between(grid, curve-epsilon, curve+epsilon, color=style.BLUE_FILL, zorder=0)
    axes[0].plot(grid, curve, color=style.INK, label=r'候选 $f(x)=1+x/2$')
    axes[0].plot(grid, curve-epsilon, '--', color=style.BLUE, linewidth=.75)
    axes[0].plot(grid, curve+epsilon, '--', color=style.BLUE, linewidth=.75)
    outside = np.abs(residual)>epsilon
    axes[0].scatter(x[~outside], y[~outside], marker='o', s=19, facecolors='white', edgecolors=style.BLUE, zorder=4)
    axes[0].scatter(x[outside], y[outside], marker='s', s=19, color=style.RED, zorder=4)
    for xi, yi, fi, ri in zip(x[outside], y[outside], prediction[outside], residual[outside]):
        edge = fi + np.sign(ri)*epsilon
        axes[0].plot([xi, xi], [edge, yi], color=style.RED, linewidth=1.7, zorder=3)
    axes[0].set_xlim(-2.2, 2.2)
    axes[0].set_ylim(-.45, 3.35)
    axes[0].set_xticks([-2, -1, 0, 1, 2])
    axes[0].set_yticks([0, 1, 2, 3])
    axes[0].set_title(r'只计入超出 $\epsilon=0.5$ 的部分', pad=8)
    axes_style(axes[0], r'输入 $x$（无量纲）', r'响应 $y$（无量纲）')
    handles = [Line2D([0],[0], color=style.INK), Line2D([0],[0], marker='o', markersize=4, markerfacecolor='white', markeredgecolor=style.BLUE, linestyle=''), Line2D([0],[0], marker='s', markersize=4, color=style.RED, linestyle='')]
    axes[0].legend(handles, ['候选直线', '带内及边界', '带外残差'], loc='lower center', bbox_to_anchor=(.276, .04), bbox_transform=fig.transFigure, ncol=3, handlelength=1.25, columnspacing=.7, borderaxespad=0)
    r = np.linspace(-1.6, 1.6, 321)
    axes[1].axvspan(-epsilon, epsilon, color=style.BLUE_FILL, zorder=0)
    axes[1].plot(r, np.maximum(np.abs(r)-epsilon,0), color=style.BLUE)
    axes[1].set_xlim(-1.65, 1.65)
    axes[1].set_ylim(-.08, 1.35)
    axes[1].set_xticks([-1.5, -.5, .5, 1.5])
    axes[1].set_yticks([0, .5, 1])
    axes[1].set_title(r'容忍带对应一段零损失', pad=8)
    axes_style(axes[1], r'残差 $r=y-f(x)$（无量纲）', r'$L_\epsilon(r)=(|r|-\epsilon)_+$')
    axes[1].text(0, .52, '不计损失', ha='center')
    fig.text(.786, .065, r'完整目标还计入斜率惩罚 $w^2/2$', ha='center', va='center')
    assert np.isclose(excess.sum(), 1.2)
    assert np.isclose(.5*(.5**2), .125)
    export(fig, 'regression-svr-objective', {'x': x.tolist(), 'y': y.tolist(), 'candidate': '1+x/2', 'epsilon': epsilon, 'residuals': residual.tolist(), 'outside_excess': excess.tolist(), 'sum_loss': float(excess.sum()), 'half_slope_norm_squared': .125},
           {'drawn_excess_segments_equal_losses': True, 'sum_loss_equals_1_point_2': True, 'candidate_is_not_claimed_to_be_fitted_optimum': True},
           'A fixed candidate line illustrates the epsilon-insensitive loss. Only the portions outside the tube are penalized. '
           'For the recorded example the full SVR objective is 0.125+1.2*C; the figure makes no claim about optimal support-vector coefficients.')

if __name__ == '__main__':
    approximation()
    quantile()
    svr()
    print('Generated three exact regression objective figures.')
