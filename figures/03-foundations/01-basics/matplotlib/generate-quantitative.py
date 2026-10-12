"""Only regenerate the four explicitly owned quantitative assets; shared tools stay unchanged."""
from pathlib import Path
import runpy,json
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
script=ROOT/'figures/03-foundations/00-shared/matplotlib/redraw/charts.py'
scope=runpy.run_path(str(script),run_name='basics_chart_import')
scope['load_math_functions']()
# Functions added through load_math_functions live in the original function globals.
ns=scope['load_math_functions'].__globals__
original_destination=ns['destination']
ns['destination']=lambda key: ROOT/'figures/03-foundations/01-basics/matplotlib'/key if key in ['models-linear-nonlinear','models-discriminative-generative'] else original_destination(key)
for name in ['training','point_distribution','linear_panel','discriminative_panel']:
 ns[name]()
 print(name,'rendered',flush=True)
report=ROOT/'reviews/academic-drawing/2026-10-11-volume-two-figures/basics/quantitative-generation.json'
report.write_text(json.dumps(ns['RECORDS'],ensure_ascii=False,indent=2)+'\n')
