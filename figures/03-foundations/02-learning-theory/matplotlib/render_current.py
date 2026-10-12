"""Render theory teaching constructions using coordinated shared functions.

Only local final-size and visual corrections are applied here. Analytic values,
sampling and experimental recurrence remain in the recorded shared sources.
"""
from pathlib import Path
import runpy, json, hashlib
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
SOURCE = ROOT/'figures/03-foundations/00-shared/matplotlib/redraw/charts.py'
loaded = runpy.run_path(str(SOURCE))
g = loaded['export'].__globals__
g['load_math_functions']()
original_export = g['export']
def export_local(fig, part, name, data, panel=False):
    from matplotlib.ticker import PercentFormatter
    if fig.get_size_inches()[0]*25.4 > 165:
        fig.set_size_inches(164.6/25.4, fig.get_size_inches()[1])
    if name == 'double-descent':
        # The exact zero tail must remain visible above the separate axis.
        fig.axes[0].spines['bottom'].set_position(('outward',2))
        fig.axes[0].set_yticks([0],['0'])
        for line in fig.axes[0].lines:
            if line.get_linestyle() == '--': line.set_zorder(4)
    if name == 'learning-theory-uniform-convergence':
        ax=fig.axes[0]
        ax.set_ylabel('分类错误率（%）')
        ax.yaxis.set_major_formatter(PercentFormatter(100, decimals=0))
        ax.set_xticks(data['hypothesis_positions'],[rf'$h_{i}$' for i in range(1,7)])
        for patch in ax.patches:
            patch.set_facecolor(g['GREEN_FILL']);patch.set_alpha(1);patch.set_zorder(0)
    if name == 'learning-theory-support-coverage':
        for ax in fig.axes:
            for patch in ax.patches:
                patch.set_facecolor(g['RED_FILL']);patch.set_edgecolor(g['RED'])
                patch.set_linewidth(.6);patch.set_alpha(1)
    if name == 'learning-theory-ntk-linearization':
        for text in fig.axes[0].texts:
            if text.get_text() in [r'$\theta^{(0)}$',r'$\theta^{(6)}$']:
                text.set_text(text.get_text().replace(r'\theta',r'\mathbf{\theta}'))
    if name in ['learning-theory-model-selection','learning-theory-ntk-linearization']:
        # Data markers at the declared axis endpoints must be complete.
        for ax in fig.axes:
            for line in ax.lines:
                line.set_clip_on(False)
    data['local_visual_corrections']='native physical size; fixed fill; explicit percentage scale; visible exact-zero tail as applicable'
    original_export(fig,part,name,data,panel)
g['export']=export_local
for function in ['selection','ntk','support','importance','error_decomposition','double_descent','distribution_shift','uniform_panel']:
    g[function]()
    print(function,'rendered',flush=True)
sources=[SOURCE]+[SOURCE.with_name(n) for n in ['analytic-redraw-functions.py','risk-shift-functions.py','quantitative-redraw-functions.py']]+[Path(__file__)]
record={'tool_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},'records':g['RECORDS'],'review':'generation metadata only; each current output requires visual and scientific review'}
(ROOT/'reviews/academic-drawing/2026-10-11-volume-two-figures/theory/chart-generation.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
