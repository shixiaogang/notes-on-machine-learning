"""Reproduce the existing activation panels from their unchanged analytic samples.

The legacy PGFPlots sources document labels and displayed ranges. Numerical
input stays in feedforward-activation-curves.dat, produced by feedforward-curves.py.
"""
from pathlib import Path
import json, re, sys, hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
OUT = Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
from plot_style import configure, prepare_figure, style_record, BLUE, RED, MUTED, GREEN, ORANGE, GRID
configure()
DATA = ROOT/'figures/03-models/02-neural-network-models/tikz/feedforward-activation-curves.dat'
values = np.genfromtxt(DATA, names=True)
OLD = ROOT/'figures/03-models/02-neural-network-models/tikz'
names=['feedforward-activation-basics','feedforward-activations','feedforward-activation-rectifiers','feedforward-activation-exponential','feedforward-activation-swish','feedforward-activation-smooth','feedforward-activation-vector']
COLORS={'NNInput':BLUE,'NNHidden':GREEN,'NNOutput':RED,'NNGradient':ORANGE,'NNInk':MUTED,'ffn reference curve':MUTED}
records=[]
def option(text, key, default):
    m=re.search(r'(?:^|,)\s*'+key+r'=([^,}\]]+)',text)
    return float(m.group(1)) if m else default

def braces(text, pos):
    pos=text.index('{',pos)+1; start=pos; depth=1
    while depth:
        if text[pos]=='{': depth+=1
        elif text[pos]=='}': depth-=1
        pos+=1
    return text[start:pos-1]

for name in names:
    source=(OLD/(name+'.tex')).read_text()
    axes_spec=list(re.finditer(r'\\begin\{axis\}\[(.*?)\](.*?)\\end\{axis\}',source,re.S))
    fig,axes=plt.subplots(1,len(axes_spec),figsize=((112 if len(axes_spec)==1 else 169)/25.4,69/25.4),layout='constrained',squeeze=False)
    panel_records=[]
    for index,(ax,m) in enumerate(zip(axes[0],axes_spec)):
        options,body=m.groups()
        xlim=[option(options,'xmin',-4),option(options,'xmax',4)]
        ylim=[option(options,'ymin',-1.25),option(options,'ymax',1.2)]
        ax.set(xlim=xlim,ylim=ylim,xlabel='$z$',ylabel='$h$' if 'ylabel={$h$}' in options else '$p_k$' if 'ylabel={$p_k$}' in options else '$\sigma(z)$')
        ax.grid(color=GRID,linewidth=.4)
        ax.axhline(0,color=MUTED,lw=.6,zorder=1);ax.axvline(0,color=MUTED,lw=.6,zorder=1)
        for key in ['xtick','ytick']:
            ticks=re.search(key+r'=\{([^}]+)\}',options)
            if ticks:getattr(ax,'set_'+('xticks' if key=='xtick' else 'yticks'))([float(v) for v in ticks.group(1).split(',')])
        curves=[]
        for plot in re.finditer(r'\\addplot\[([^]]+)\]\s*table\[x=z,y=([^]]+)\]\s*\{[^}]+\};',body,re.S):
            style,column=plot.groups()
            tail=body[plot.end():]
            label=braces(tail,tail.index('\\addlegendentry'))
            color=next((v for k,v in COLORS.items() if k in style),BLUE)
            line=':' if 'dotted' in style else '-.' if ('dashdotted' in style or 'dash pattern' in style) else '--' if 'dashed' in style else '-'
            ax.plot(values['z'],values[column],color=color,ls=line,lw=1.25,label=label)
            curves.append({'column':column,'label':label,'color':color,'linestyle':line})
        if name=='feedforward-activation-basics' and index==1:
            ax.plot([-2,0],[0,0],color=BLUE,label='阶跃');ax.plot([0,2],[1,1],color=BLUE)
            ax.plot(0,0,'o',mfc='white',mec=BLUE,ms=5,zorder=5);ax.plot(0,1,'o',color=BLUE,ms=5,zorder=5)
            curves.append({'coordinates':[[-2,0],[0,0],[0,1],[2,1]],'jump_at_zero':'open zero, closed one; never connected vertically'})
        ax.legend(loc='upper left' if not(name=='feedforward-activation-basics' and index==1) else 'lower right',fontsize=8)
        if len(axes_spec)>1:ax.set_title(f'({chr(97+index)})',loc='left')
        panel_records.append({'xlim':xlim,'ylim':ylim,'curves':curves})
    from export_common import save
    save(fig,name,'02-neural-network-models',data={n:values[n] for n in values.dtype.names},params={'panels':panel_records,'source_sample_points_retained':True},inputs=[DATA,OLD/(name+'.tex')])
    records.append({'name':name,'original_specification':str((OLD/(name+'.tex')).relative_to(ROOT)),'panels':panel_records,'data_sha256':hashlib.sha256(DATA.read_bytes()).hexdigest(),'processing':'No filtering, sampling, smoothing or numerical change; only declared axis limits clip the display.'})
