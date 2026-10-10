"""Exact analytic cut panels, appended without transforming the model's artwork."""
from pathlib import Path
import json,sys,hashlib
import numpy as np
from PIL import Image
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
from plot_style import configure,prepare_figure,BLUE,GREEN
import matplotlib.pyplot as plt

def compose(folder):
 folder=Path(folder);diagram=Image.open(folder/'figure.png').convert('RGB');diagram.save(folder/'diagram.png');configure();w=diagram.width;h=560
 x=np.linspace(-1,1,401);narrow=.1+.45*x*x;wide=.1+.08*x*x;epsilon=.6
 assert abs((.1+.45*epsilon**2)-.1-.162)<1e-14
 assert abs((.1+.08*epsilon**2)-.1-.0288)<1e-14
 fig,axs=plt.subplots(1,2,figsize=(w/300,h/300),layout='constrained',sharex=True,sharey=True)
 for ax,ys,c,coef,name,inc in zip(axs,[narrow,wide],[BLUE,GREEN],[.45,.08],['窄谷','宽谷'],[.162,.0288]):
  y=.1+coef*epsilon**2;ax.plot(x,ys,color=c);ax.scatter([0],[.1],color=c,zorder=4,s=14)
  ax.scatter([epsilon],[y],edgecolors=c,facecolors='white',zorder=4,s=20,linewidth=1)
  ax.vlines(epsilon,0,y,colors=c,ls=':',lw=.8);ax.hlines([.1,y],0,epsilon,colors=c,ls=':',lw=.6)
  ax.annotate(r'$\Delta\hat R_S='+str(inc)+'$',xy=(epsilon,y),xytext=(-.85,.44),fontsize=8.5,color=c,arrowprops={'arrowstyle':'->','color':c,'lw':.7})
  ax.set(xlim=(-1,1),ylim=(0,.62),xticks=[-1,0,.6,1],yticks=[0,.1,.3,.6],xlabel='同方向参数位移 $s$',title=name+'：$0.1+'+str(coef)+'s^2$')
 axs[0].set_ylabel('经验风险截面');prepare_figure(fig);fig.savefig(folder/'quantitative-panels.png',dpi=300,facecolor='white');fig.savefig(folder/'quantitative-panels.pdf',facecolor='white');plt.close(fig)
 chart=Image.open(folder/'quantitative-panels.png').convert('RGB');gap=25;final=Image.new('RGB',(w,diagram.height+gap+chart.height),'white');final.paste(diagram,(0,0));final.paste(chart,(0,diagram.height+gap));final.save(folder/'figure.png',dpi=(300,300))
 data={'x':x.tolist(),'narrow':narrow.tolist(),'wide':wide.tolist(),'formulas':['0.1+0.45*s^2','0.1+0.08*s^2'],'common_displacement':epsilon,'minimum':[.1,.1],'perturbed_values':[.262,.1288],'increases':[.162,.0288],'direction_norm':1,'same_axes':{'x':[-1,1],'y':[0,.62]},'generated_basins_are_qualitative':True,'generated_background_unchanged':True,'component_rects':{'diagram':[0,0,diagram.width,diagram.height],'exact_chart':[0,diagram.height+gap,chart.width,chart.height]},'output_pixels':final.size}
 (folder/'quantitative-data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':compose(Path(__file__).resolve().parent)
