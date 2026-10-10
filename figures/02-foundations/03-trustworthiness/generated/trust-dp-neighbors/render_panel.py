from pathlib import Path
import json, numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from PIL import Image
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
D=Path(__file__).resolve().parent
DATA=json.loads((D/'panel-data.json').read_text())
EN=FontProperties(fname=str(ROOT/'fonts/FiraMath-Regular.otf'),size=8)
CN=FontProperties(fname=str(ROOT/'fonts/SourceHanSansSC-Normal.otf'),size=8)
NOTE=FontProperties(fname=str(ROOT/'fonts/LXGWWenKai-Regular.ttf'),size=8)
plt.rcParams.update({'axes.linewidth':.75,'lines.linewidth':1.1,'text.color':'#3B4252','axes.labelcolor':'#3B4252','xtick.color':'#3B4252','ytick.color':'#3B4252','font.family':'Fira Math','pdf.fonttype':42,'svg.fonttype':'path','figure.facecolor':'white','savefig.facecolor':'white'})
kind=DATA['kind'];px=DATA['size_px'];dpi=300
fig=plt.figure(figsize=(px[0]/dpi,px[1]/dpi),dpi=dpi)
if kind=='calibration':
 ax=fig.add_axes([.23,.17,.72,.72]);x=np.linspace(0,1,41)
 ax.plot(x,x,color='#7B95C6');ax.plot(x,x*x,color='#67A583',ls='--')
 ax.set(xlim=(0,1),ylim=(0,1),xticks=[0,.5,1],yticks=[0,.5,1])
 ax.set_xlabel('预测概率',fontproperties=CN,labelpad=5);ax.set_ylabel('实际正例比例',fontproperties=CN,labelpad=5)
 ax.text(.20,.82,'理想校准',fontproperties=NOTE,color='#496791',transform=ax.transAxes)
 ax.text(.52,.24,'过度自信',fontproperties=NOTE,color='#44785C',transform=ax.transAxes)
 ax.set_title('概率含义',fontproperties=CN,pad=9)
elif kind=='conformal':
 ax=fig.add_axes([.12,.25,.84,.62]);x=np.arange(1,10);y=np.array(DATA['residuals'])
 ax.scatter(x,y,s=15,color='#7B95C6',zorder=4);ax.scatter([8],[.8],s=42,facecolors='white',edgecolors='#67A583',zorder=5)
 ax.axhline(.8,color='#67A583',lw=.6,ls='--');ax.axvline(8,color='#4C4D4F',lw=.6,ls=':')
 ax.set(xlim=(.5,9.5),ylim=(0,1),xticks=[1,4,8,9],yticks=[0,.5,.8,1])
 ax.set_xlabel('排序后的秩',fontproperties=CN,labelpad=4);ax.set_ylabel('校准分数',fontproperties=CN,labelpad=4)
 ax.text(1.2,.85,'q = 0.8',fontproperties=EN,color='#44785C')
 ax.text(8.2,.11,'k = 8',fontproperties=EN,color='#3B4252')
 ax.set_title('n = 9     α = 0.2',fontproperties=EN,pad=8)
else:
 ax=fig.add_axes([.11,.38,.85,.52]);x=np.linspace(0,8,161)
 f=lambda mu:.5*np.exp(-np.abs(x-mu))
 ax.plot(x,f(3),color='#7B95C6');ax.plot(x,f(4),color='#67A583',ls='--')
 mask=(x>=5)&(x<=6);ax.fill_between(x,f(3),where=mask,color='#7B95C6',alpha=.25);ax.fill_between(x,f(4),where=mask,color='#67A583',alpha=.18)
 ax.set(xlim=(0,8),ylim=(0,.55),xticks=[0,3,4,5,6,8],yticks=[0,.5])
 ax.set_xlabel('发布值',fontproperties=CN,labelpad=3);ax.set_ylabel('概率密度',fontproperties=CN,labelpad=3)
 ax.text(5.15,.32,'E = [5, 6]',fontproperties=EN)
 ax.text(.35,.36,'3 + Z',fontproperties=EN,color='#496791');ax.text(6.35,.36,"4 + Z′",fontproperties=EN,color='#44785C')
for ax in fig.axes:
 ax.spines[['top','right']].set_visible(False)
 for l in ax.get_xticklabels()+ax.get_yticklabels():l.set_fontproperties(EN)
 ax.tick_params(width=.6,length=3)
fig.savefig(D/'panel.png',dpi=dpi);fig.savefig(D/'panel.pdf');fig.savefig(D/'panel.svg');plt.close(fig)
base=Image.open(D/'background.png').convert('RGBA');panel=Image.open(D/'panel.png').convert('RGBA')
base.alpha_composite(panel,tuple(DATA['place_xy']))
base.save(D/'composited-background.png')
