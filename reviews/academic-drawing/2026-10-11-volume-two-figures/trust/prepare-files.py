"""Make a complete exact file list only after enforcing this task's scope."""
from pathlib import Path
import subprocess
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
OUT=Path(__file__).resolve().parent
shared={'figures/03-foundations/00-shared/academic-drawing/'+n for n in ['plot_style.py','preamble.tex','palette.tex','render_tikz.py','README.md']}
shared|={'figures/03-foundations/00-shared/matplotlib/redraw/'+n for n in ['charts.py','analytic-redraw-functions.py','risk-shift-functions.py','quantitative-redraw-functions.py']}
chapters={'tex/03-foundations/03-trustworthiness/'+n for n in ['01-foundations.tex','02-reliability.tex','03-robustness.tex','04-fairness.tex','05-alignment.tex','06-interpretability.tex']}
target={'target/'+n for n in ['.build-manifest.json','machine-learning-notes.pdf','vol1-mathematical-preliminaries.pdf','vol2-foundations.pdf','vol3-models.pdf','vol4-paradigms.pdf','vol5-applications.pdf','vol6-systems.pdf']}
fig='figures/03-foundations/03-trustworthiness/'
generated=['activation-patching','adversarial-training','fairness-interventions','fairness-opportunity','rlhf-dpo-feedback','uncertainty-sources','decision-consequences','trustworthiness-map','references-20261011']
tikz=['trust-actionable-recourse','trust-calibration-discrimination','trust-certified-region','trust-conformal-construction','trust-counterfactual-nearest','trust-fairness-denominators','trust-feature-attribution','trust-global-local-explanation','trust-robust-neighborhood','trust-selective-risk-coverage','trust-technical-scope','trust-three-layers','alignment-mail-goal','authorized-execution','decision-consequences','reliability-review','trustworthiness-map']
charts=['trust-explanation-quality-radar','trust-fairness-incompatibility','trust-fairness-pareto','trust-proxy-overoptimization','trust-risk-coverage-curve','trust-robust-accuracy-tradeoff']
prefixes=[fig+'generated/'+n+'/' for n in generated]+[fig+'tikz/'+n+'/' for n in tikz]+[fig+'matplotlib/'+n+'/' for n in charts]+[str(OUT.relative_to(ROOT))+'/']
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT).decode().split('\0')
files=set(git('diff','HEAD','--name-only','-z'))|set(git('ls-files','--others','--exclude-standard','-z'))
files.discard('');files.add(str((OUT/'files-changed.txt').relative_to(ROOT)))
for p in files:assert p in shared|chapters|target|{fig+'generated/typeset_20261011.py'} or any(p.startswith(s) for s in prefixes),p
(OUT/'files-changed.txt').write_text('\n'.join(sorted(files))+'\n')
print('Scoped file list:',len(files),'files')
