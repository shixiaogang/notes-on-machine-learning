"""Append exact analytical panels; never change pixels in the model artwork."""
from pathlib import Path
import sys,json,hashlib
import numpy as np
from PIL import Image
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
from plot_style import configure,prepare_figure,BLUE,GREEN
import matplotlib.pyplot as plt

def compose(folder):
    folder=Path(folder);diagram=Image.open(folder/'figure.png').convert('RGB')
    diagram.save(folder/'diagram.png')
    configure();w=diagram.width;h=440
    x=np.linspace(-4,4,401)
    posterior=1/(1+np.exp(-2*x+np.log(4)))
    joint0=.8*np.exp(-.5*(x+1)**2)/np.sqrt(2*np.pi)
    joint1=.2*np.exp(-.5*(x-1)**2)/np.sqrt(2*np.pi)
    fig,axs=plt.subplots(1,2,figsize=(w/300,h/300),layout='constrained')
    axs[0].plot(x,posterior,color=GREEN)
    axs[0].set(xlim=(-4,4),ylim=(0,1),ylabel=r'$p(y=1\mid x)$',xlabel='$x$',xticks=[-4,0,4],yticks=[0,.5,1],title='条件类别概率')
    axs[1].plot(x,joint0,color=BLUE,label='$p(x,y=0)$')
    axs[1].plot(x,joint1,color=GREEN,ls='--',label='$p(x,y=1)$')
    axs[1].set(xlim=(-4,4),ylim=(0,.36),ylabel='联合密度',xlabel='$x$',xticks=[-4,0,4],yticks=[0,.2],title='先验加权的联合密度')
    axs[1].legend(loc='upper right',fontsize=8.5)
    prepare_figure(fig)
    fig.savefig(folder/'quantitative-panels.png',dpi=300,facecolor='white')
    fig.savefig(folder/'quantitative-panels.pdf',facecolor='white')
    plt.close(fig)
    chart=Image.open(folder/'quantitative-panels.png').convert('RGB');gap=25
    final=Image.new('RGB',(diagram.width,diagram.height+gap+chart.height),'white')
    final.paste(diagram,(0,0));final.paste(chart,(0,diagram.height+gap));final.save(folder/'figure.png',dpi=(300,300))
    (folder/'quantitative-data.json').write_text(json.dumps({'x':x.tolist(),'posterior':posterior.tolist(),'joint_y0':joint0.tolist(),'joint_y1':joint1.tolist(),'formulas':['sigmoid(2x-ln4)','0.8*N(-1,1)','0.2*N(1,1)'],'posterior_at_zero':float(posterior[200]),'discrete_values':[.8*.01,.2*.12,.032],'generated_background_unchanged':True,'component_rects':{'diagram':[0,0,diagram.width,diagram.height],'exact_chart':[0,diagram.height+gap,chart.width,chart.height]},'output_pixels':final.size},ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':compose(Path(__file__).resolve().parent)
