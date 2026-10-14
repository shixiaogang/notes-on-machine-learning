# regression-svr-objective

A fixed candidate line illustrates the epsilon-insensitive loss. Only the portions outside the tube are penalized. For the recorded example the full SVR objective is 0.125+1.2*C; the figure makes no claim about optimal support-vector coefficients.

Reproduce with `python3 figures/04-classic-models/00-shared/matplotlib/regression-objective-figures.py`. The generator uses the actual project fonts and shared palette. The PDF and SVG are vector exports; the PNG is a 220 dpi preview. `data.json` stores the exact example and `generation.json` stores its checks.
