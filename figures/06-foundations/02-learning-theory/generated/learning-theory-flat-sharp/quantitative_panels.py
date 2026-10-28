"""Native-size analytic panels; no model-background manipulation or compositing."""
from pathlib import Path
import json,sys,hashlib
import numpy as np
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/06-foundations/00-shared/academic-drawing'))
from plot_style import configure,prepare_figure,style_record,BLUE,GREEN,note
import matplotlib.pyplot as plt

def render(folder):
    folder=Path(folder);configure()
    x=np.linspace(-1,1,401);epsilon=.6
    fig,axs=plt.subplots(1,2,figsize=(164.6/25.4,53/25.4),sharex=True,sharey=True)
    fig.subplots_adjust(left=.09,right=.985,bottom=.25,top=.85,wspace=.20)
    for ax,c,coef,title,increase in zip(axs,[BLUE,GREEN],[.45,.08],['窄谷','宽谷'],[.162,.0288]):
        y=.1+coef*x*x;perturbed=.1+coef*epsilon**2
        assert abs(perturbed-.1-increase)<1e-14
        ax.plot(x,y,color=c,lw=1.1)
        ax.scatter([0],[.1],color=c,zorder=4,s=14)
        ax.scatter([epsilon],[perturbed],edgecolors=c,facecolors='white',zorder=4,s=20,linewidth=.9)
        ax.vlines(epsilon,0,perturbed,colors=c,ls=':',lw=.6)
        ax.hlines([.1,perturbed],0,epsilon,colors=c,ls=':',lw=.6)
        note(ax.annotate(r'$\Delta\hat R_S='+str(increase)+'$',xy=(epsilon,perturbed),xytext=(-.35,.46),fontsize=7.5,color=c,arrowprops={'arrowstyle':'->','color':c,'lw':.6}))
        ax.set(xlim=(-1,1),ylim=(0,.62),xticks=[-1,0,.6,1],yticks=[0,.1,.3,.6],xlabel='同方向参数位移 $s$',title=title+'：$0.1+'+str(coef)+'s^2$')
    axs[0].set_ylabel('经验风险截面')
    prepare_figure(fig)
    for ext in ['png','pdf','svg']:fig.savefig(folder/('quantitative-panels.'+ext),dpi=300,facecolor='white')
    plt.close(fig)
    data={'construction':'exact analytic teaching example, not experimental data','x':x.tolist(),'narrow':(.1+.45*x*x).tolist(),'wide':(.1+.08*x*x).tolist(),'formulas':['0.1+0.45*s^2','0.1+0.08*s^2'],'common_displacement':epsilon,'minimum':[.1,.1],'perturbed_values':[.262,.1288],'increases':[.162,.0288],'direction_norm':1,'same_axes':{'x':[-1,1],'y':[0,.62]},'generated_basins_are_qualitative':True,'generated_background_unchanged':True,'publication_width_mm':164.6,'publication_height_mm':53,'main_label_pt':8,'auxiliary_label_pt':7.5,'vector_output':'quantitative-panels.pdf','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'style':style_record()}
    (folder/'quantitative-data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':render(Path(__file__).resolve().parent)
