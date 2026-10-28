"""Exact teaching data panel, with fonts sized at final physical inclusion width."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
D=Path(__file__).resolve().parent
ROOT=next(p for p in D.parents if (p/'build.sh').exists())
data=json.loads((D/'panel-data.json').read_text())
A=D/'assets';A.mkdir(exist_ok=True)
cn=FontProperties(fname=ROOT/'fonts/SourceHanSansSC-Normal.otf',size=8)
en=FontProperties(fname=ROOT/'fonts/FiraMath-Regular.otf',size=8)
note=FontProperties(fname=ROOT/'fonts/LXGWWenKai-Regular.ttf',size=7.5)
blue='#7188A3';green='#829C8B';ink='#3B4252';stroke='#4C4D4F'
plt.rcParams.update({'figure.facecolor':'white','savefig.facecolor':'white','axes.linewidth':.75,'text.color':ink,'axes.labelcolor':ink,'xtick.color':ink,'ytick.color':ink,'pdf.fonttype':3,'svg.fonttype':'path'})
w,h=data['physical_mm'];fig=plt.figure(figsize=(w/25.4,h/25.4),dpi=300)
if data['kind']=='calibration':
 ax=fig.add_axes([.24,.17,.71,.72]);x=np.linspace(0,1,41)
 ax.plot(x,x,color=blue,lw=1.1)
 ax.plot(x,x*x,color=green,lw=1.1,ls='--')
 ax.set(xlim=(0,1),ylim=(0,1),xticks=[0,.5,1],yticks=[0,.5,1])
 ax.set_xlabel('预测概率',fontproperties=cn,labelpad=4)
 ax.set_ylabel('实际正例比例',fontproperties=cn,labelpad=4)
 ax.set_title('概率含义',fontproperties=cn,pad=8)
 ax.text(.17,.82,'理想校准',fontproperties=note,color=blue,transform=ax.transAxes)
 ax.text(.57,.18,'过度自信',fontproperties=note,color=green,transform=ax.transAxes)
else:
 ax=fig.add_axes([.12,.33,.85,.53]);r=np.arange(1,10);s=np.array(data['residuals'])
 ax.scatter(r,s,s=15,color=blue,zorder=3)
 ax.scatter([8],[.8],s=42,facecolors='white',edgecolors=green,zorder=4)
 ax.axhline(.8,color=green,lw=.6,ls='--');ax.axvline(8,color=stroke,lw=.6,ls=':')
 ax.set(xlim=(.5,9.5),ylim=(0,1),xticks=[1,4,8,9],yticks=[0,.5,.8,1])
 ax.set_xlabel('排序后的秩',fontproperties=cn,labelpad=4)
 ax.set_ylabel('校准分数',fontproperties=cn,labelpad=4)
 ax.text(1.2,.85,'q = 0.8',fontproperties=en,color=green)
 ax.text(8.2,.11,'k = 8',fontproperties=en,color=ink)
ax.spines[['top','right']].set_visible(False)
for side in ['left','bottom']:ax.spines[side].set_color(stroke)
for label in ax.get_xticklabels()+ax.get_yticklabels():label.set_fontproperties(en)
ax.tick_params(width=.6,length=3)
# Type3 retains real CFF glyph outlines; Type42 loses SourceHan axes in PDF renderers.
fig.savefig(A/'panel.pdf');fig.savefig(A/'panel.svg');fig.savefig(A/'panel.png',dpi=300);plt.close(fig)
