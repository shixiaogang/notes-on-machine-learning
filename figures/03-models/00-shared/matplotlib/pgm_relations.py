"""Reproducible PGM teaching charts; exact chapter values, no invented experiments."""
from pathlib import Path
import sys,json,re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
from plot_style import configure,prepare_figure,style_record,BLUE,RED,YELLOW,MUTED,STROKE,BLUE_FILL,YELLOW_FILL,RED_FILL
configure()
from plot_style import GREEN
YELLOW=GREEN # Readability adjustment for lines/points only.
OUT=Path(__file__).parent;records={}
def chart(size=(112,72)):
 f,a=plt.subplots(figsize=(size[0]/25.4,size[1]/25.4));f.subplots_adjust(left=.16,right=.97,bottom=.19,top=.91);return f,a
from export_common import save
def normal(x,m,v):return np.exp(-(x-m)**2/(2*v))/np.sqrt(2*np.pi*v)
x=np.linspace(25,95,181);y=.5*(normal(x,40,9)+normal(x,80,9));f,a=chart();a.plot(x,y,color=BLUE);a.vlines(60,0,.062,color=RED,ls='--');a.text(60,.063,'均值',ha='center');a.text(40,.068,'工况一',ha='center');a.text(80,.068,'工况二',ha='center');a.set(xlim=(25,95),ylim=(0,.08),xticks=[40,60,80],yticks=[0,.04,.08],xlabel=r'温度 $y$（$^\circ\mathrm{C}$）',ylabel=r'概率密度（$^\circ\mathrm{C}^{-1}$）');save(f,'pgm-overview-predictive-density',{'x':x.tolist(),'density':y.tolist(),'mixture':{'means':[40,80],'variance':9,'weights':[.5,.5]},'mean':60})
prior=np.array([.7885,.1615,.0415,.0085]);posterior=np.array([.0413476665,.7621919245,.1523335081,.0441269009]);f,a=chart();inds=np.arange(4);a.bar(inds-.18,prior,.34,color=BLUE_FILL,edgecolor=BLUE,label=r'先验 $p(h,s)$');a.bar(inds+.18,posterior,.34,color=YELLOW_FILL,edgecolor=STROKE,label=r'后验 $p(h,s\mid A=1)$');a.set(xlim=(-.6,3.6),ylim=(0,1.05),xticks=inds,xticklabels=['$(0,0)$','$(1,0)$','$(0,1)$','$(1,1)$'],yticks=[0,.2,.4,.6,.8,1],xlabel='$(h,s)$',ylabel='概率');a.grid(axis='y');a.set_axisbelow(True);a.legend(loc='upper right');save(f,'pgm-sampling-importance',{'prior':prior.tolist(),'posterior':posterior.tolist(),'states':[[0,0],[1,0],[0,1],[1,1]],'type':'exact finite artificial device probabilities'})
def ll(pi):return 6*np.log(.1+.7*pi)+14*np.log(.9-.7*pi)
pi=np.linspace(.02,.45,160);bound=(4460/1411)*np.log(pi)+(20-4460/1411)*np.log1p(-pi)-4.187984227219437
f,a=chart((112,78));a.plot(pi,ll(pi),color=YELLOW,label=r'$\ell(\pi)$');a.plot(pi,bound,color=BLUE,ls='--',label=r'$\mathcal{F}(q^{(0)},\pi)$');a.vlines([.1,.158043940467753],-14.5,[-13.240355146272162,-12.657186963816700],color=MUTED,ls=':',lw=.7);a.plot(.1,-13.240355146272162,'o',color=STROKE,ms=3);a.plot(.158043940467753,-12.916224328150363,'s',color=BLUE,ms=3);a.plot(2/7,ll(2/7),'o',color=YELLOW,markeredgecolor=STROKE,ms=4);a.annotate(r'$\pi^{(0)}$',(.1,-13.240355),xytext=(-4,-13),textcoords='offset points',ha='right');a.annotate(r'$\pi^{(1)}$',(.15804394,-12.916224),xytext=(4,-13),textcoords='offset points');a.annotate('$2/7$',(2/7,ll(2/7)),xytext=(0,4),textcoords='offset points',ha='center');a.set(xlim=(.02,.45),ylim=(-14.5,-12),xticks=[.1,.2,.3,.4],yticks=[-14.5,-14,-13.5,-13,-12.5,-12],xlabel=r'故障率 $\pi$',ylabel='对数值');a.grid();a.legend(loc='lower right');save(f,'pgm-parameter-learning-em-bound',{'pi':pi.tolist(),'likelihood':ll(pi).tolist(),'bound':bound.tolist(),'fixed_expected_count':4460/1411,'fixed_entropy_constant':-4.187984227219437})
points=np.array([[.1,-13.240355],[.158044,-12.657187],[.208111,-12.369507],[.241926,-12.263957],[.261921,-12.230791],[.273020,-12.221089],[.279003,-12.218343]]);pi=np.linspace(.07,.31,160);f,a=chart((112,78));a.plot(pi,ll(pi),color=STROKE);a.plot(points[:,0],points[:,1],'o',color=RED,ms=3)
for j,(p,q) in enumerate(zip(points[:3],points[1:4])):
 a.annotate('',xy=q,xytext=p,arrowprops={'arrowstyle':'->','color':RED,'lw':1})
for j in range(3):a.annotate(r'$\pi^{('+str(j)+')}$',points[j],xytext=(-5,(-12 if j==0 else 6)),textcoords='offset points',ha='right')
a.plot(2/7,ll(2/7),'D',color=BLUE,ms=4);a.annotate('MLE：$2/7$',(2/7,ll(2/7)),xytext=(-4,7),textcoords='offset points',ha='right');a.text(.27,-12.31,r'$\pi^{(3)}\to\pi^{(4)}\to\cdots$',ha='center');a.set(xlim=(.07,.31),ylim=(-13.4,-12.12),xticks=[.1,.15,.2,.25,.3],yticks=[-13.2,-12.8,-12.4,-12.2],xlabel=r'故障率 $\pi$',ylabel=r'观测对数似然 $\ell(\pi)$');a.grid();save(f,'pgm-parameter-learning-em-trajectory',{'pi':pi.tolist(),'likelihood':ll(pi).tolist(),'iterations_original_rounded':points.tolist(),'mle':2/7})
truth=np.array([[0,0],[1,.5],[2,1.1],[3,1.4],[4,2.2],[5,2.6],[6,3.4],[7,3.7],[8,4.4]])
obs=np.array([[.2,-.3],[1.4,.2],[1.6,1.5],[3.5,1],[3.7,2.7],[5.4,2.2],[5.7,3.9],[7.5,3.3],[7.8,4.8]])
pred=np.array([[0,0],[.094,-.171],[.998,.085],[1.427,1.079],[2.906,1.023],[3.473,2.202],[4.848,2.201],[5.456,3.396],[6.915,3.328]])
filt=np.array([[.094,-.171],[.998,.085],[1.427,1.079],[2.906,1.023],[3.473,2.202],[4.848,2.201],[5.456,3.396],[6.915,3.328],[7.546,4.363]])
smooth=np.array([[.338,-.024],[1.261,.405],[1.935,1.176],[3.206,1.406],[3.955,2.313],[5.157,2.576],[5.926,3.467],[7.096,3.636],[7.546,4.363]])
f,a=chart((169,112));f.subplots_adjust(left=.08,right=.98,bottom=.13,top=.93)
for arr,c,ls,m,label in [(truth,STROKE,'--','o','真值'),(obs,MUTED,'-','x','观测'),(pred,BLUE,'-','o','一步预测'),(filt,RED,'-','s','滤波'),(smooth,YELLOW,'-','^','RTS 平滑')]:a.plot(arr[:,0],arr[:,1],color=c,ls=ls,marker=m,ms=4.6 if label=='一步预测' else 3,markerfacecolor='white' if label=='一步预测' else c,lw=1 if label!='滤波' else 1.3,label=label)
for center,r in [((1.427,1.079),(.566,.459)),((4.848,2.201),(.567,.459)),((7.546,4.363),(.567,.459))]:a.add_patch(Ellipse(center,2*r[0],2*r[1],facecolor=RED_FILL,edgecolor=RED,lw=.8,zorder=0))
a.annotate(r'$1\sigma$ 滤波椭圆',(4.848,2.66),xytext=(-22,8),textcoords='offset points',ha='right')
for t in [0,4,8]:a.annotate('$t='+str(t)+'$',filt[t],xytext=(4,5),textcoords='offset points')
a.set(xlim=(-.45,8.45),ylim=(-.65,5.25),xticks=[0,2,4,6,8],yticks=[0,1,2,3,4,5],xlabel='横向位置',ylabel='纵向位置',aspect='equal');a.grid();a.legend(loc='upper left');save(f,'pgm-dynamic-kalman-trajectory',{'type':'chapter reproducible teaching trajectory; preserve original three-decimal values','truth':truth.tolist(),'observations':obs.tolist(),'prediction':pred.tolist(),'filter':filt.tolist(),'smooth':smooth.tolist(),'model':{'Q_diagonal':[.8,.5],'R_diagonal':[.45,.3],'initial_covariance_diagonal':[.4,.4]},'one_sigma_ellipses':[[1.427,1.079,.566,.459],[4.848,2.201,.567,.459],[7.546,4.363,.567,.459]]})
x=np.linspace(-3,5,121);f,a=chart();a.plot(x,normal(x,.5,1.5),color=BLUE,label='预测');a.plot(x,normal(x,2,1),color=MUTED,ls='--',label='似然');a.plot(x,normal(x,1.4,.6),color=RED,lw=1.7,label='后验');a.annotate('后验 posterior',xy=(1.52,.51),xytext=(2.45,.52),ha='left',arrowprops={'arrowstyle':'->','color':RED,'lw':1});a.set(xlim=(-3,5),ylim=(0,.56),xticks=[-2,0,2,4],yticks=[0,.2,.4],xlabel=r'温度偏移 $z_2$（$^\circ\mathrm{C}$）',ylabel=r'密度（$^\circ\mathrm{C}^{-1}$）');a.legend(loc='upper left');save(f,'pgm-dynamic-gaussian-update',{'x':x.tolist(),'prediction':[.5,1.5],'likelihood':[2,1],'posterior':[1.4,.6]})
