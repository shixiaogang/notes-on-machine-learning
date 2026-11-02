"""SRM teaching example: empirical risk + finite-class penalty for nested spaces.

Exact formula: p_k = sqrt((log(2|H_k|) + log(k(k+1)/delta)) / (2n)),
|H_k| = 10^k, n = 1000, delta = 0.05, delta_k = delta/(k(k+1)).
Empirical risks are teaching values (marked as such in the caption).
"""
from pathlib import Path
import json, sys
import numpy as np
import matplotlib.pyplot as plt

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').exists())
D = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'figures/06-foundations/00-shared/academic-drawing'))
from plot_style import configure, prepare_figure, note, style_record, BLUE, BLUE_FILL, YELLOW, YELLOW_FILL, RED, MUTED, INK

configure()
n, delta = 1000, 0.05
emp = np.array([0.30, 0.21, 0.15, 0.12, 0.105, 0.102, 0.100, 0.099])
k = np.arange(1, len(emp) + 1)
pen = np.sqrt((np.log(2 * 10.0 ** k) + np.log(k * (k + 1) / delta)) / (2 * n))
obj = emp + pen
kh = int(np.argmin(obj)) + 1

fig, ax = plt.subplots(figsize=(107 / 25.4, 58 / 25.4), layout='constrained')
ax.bar(k, emp, width=0.62, color=BLUE_FILL, edgecolor=BLUE, linewidth=0.8, label=r'经验风险 $\hat R_S(\hat h_k)$')
ax.bar(k, pen, bottom=emp, width=0.62, color=YELLOW_FILL, edgecolor=YELLOW, linewidth=0.8, label=r'惩罚 $p_k$')
ax.plot(k, obj, color=INK, lw=0.6, ls=':', marker='o', ms=2.5, zorder=4)
ax.bar([kh], [obj[kh - 1]], width=0.62, fill=False, edgecolor=RED, linewidth=1.4, zorder=5)
note(ax.text(kh, obj[kh - 1] + 0.012, r'$\hat k=%d$' % kh, ha='center', va='bottom', fontsize=7.5, color=RED))
ax.set(xlabel=r'空间编号 $k$（$|\mathcal{H}_k|=10^k$）', ylabel='风险或上界', xticks=k,
       ylim=(0, 0.40), yticks=[0, 0.1, 0.2, 0.3, 0.4])
ax.legend(loc='upper right', fontsize=7.5)
prepare_figure(fig)
for ext in ['pdf', 'png']:
    fig.savefig(D / ('figure.' + ext), dpi=300)
plt.close(fig)

data = {'n': n, 'delta': delta, 'H_size': '10^k', 'delta_k': 'delta/(k(k+1))',
        'empirical_risk_teaching_values': emp.tolist(), 'penalty': [round(v, 4) for v in pen],
        'objective': [round(v, 4) for v in obj], 'selected_k': kh}
(D / 'data.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
gen = {'method': 'Matplotlib', 'date': '2026-10-30', 'source': 'analytic penalty formula; empirical risks are teaching values',
       'parameters': {'n': n, 'delta': delta}, 'physical_size_mm': [107, 58], 'style': style_record()}
(D / 'generation.json').write_text(json.dumps(gen, ensure_ascii=False, indent=2) + '\n')
print(data)
