"""Reproduce volume III quantitative figures from retained numerical inputs.

No model-generated chart data. Original PGF samples, coordinates and domains
are copied or evaluated at exactly the original sampling points.
"""
from pathlib import Path
import sys,json,hashlib,re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Polygon
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
from plot_style import configure,prepare_figure,style_record,BLUE,RED,YELLOW,INK,MUTED,GRID,BLUE_FILL,YELLOW_FILL,note
configure()
from plot_style import GREEN
YELLOW=GREEN # Fine quantitative marks need contrast; pale yellow regions retained.
C=ROOT/'figures/03-models/01-classic-models/tikz'
N=ROOT/'figures/03-models/02-neural-network-models/tikz'
records=[]
def load(path):return np.genfromtxt(path,names=True,delimiter=',' if path.suffix=='.csv' else None)
def fig(w=112,h=70,nrows=1,ncols=1,**kw):return plt.subplots(nrows,ncols,figsize=(w/25.4,h/25.4),layout='constrained',**kw)
def axes(ax,xlim,ylim,xlab,ylab,xt=None,yt=None,grid=False):
 ax.set(xlim=xlim,ylim=ylim,xlabel=xlab,ylabel=ylab)
 if xt is not None:ax.set_xticks(xt)
 if yt is not None:ax.set_yticks(yt)
 if grid:ax.grid()
from export_common import save

def classic():
 # Retained OLS data and deterministic fitted line.
 d=load(C/'regression-ols.csv');f,a=fig();axes(a,(-.3,6.4),(0,5.2),'输入 $x$（无量纲）','响应 $y$（无量纲）',range(7),range(6),True)
 a.vlines(d['x'],1+.5*d['x'],d['y'],color=RED,ls='--',lw=.9,label='残差 $r_i$');a.plot([-.3,6.4],[.85,4.2],color=YELLOW,label='拟合 $1+0.5x$');a.scatter(d['x'],d['y'],s=15,color=BLUE,label='观测样本',zorder=4);a.legend(loc='upper left');a.text(3.16,3.07,'$r_i$')
 save(f,'regression-ols','01-classic-models',dict(x=d['x'],y=d['y']),{'line':'1+0.5*x'},[C/'regression-ols.csv'])
 # Exact unit-ball and quadratic contours.
 t=np.linspace(0,2*np.pi,121);f,aa=fig(169,83,ncols=2)
 for i,a in enumerate(aa):
  axes(a,(-1.35,3.15),(-1.5,3),'$w_1$','$w_2$',[-1,1,2,3],[-1,1,2]);a.set_aspect('equal');a.set_title('（a）岭：圆形约束' if i==0 else '（b）Lasso：菱形约束')
  if i==0:a.fill(np.cos(t),np.sin(t),fc=YELLOW_FILL,ec=YELLOW,lw=1);radii=[.8973665961,1.2473665961,1.5973665961];point=(.9486832981,.316227766)
  else:a.add_patch(Polygon([(1,0),(0,1),(-1,0),(0,-1)],fc=YELLOW_FILL,ec=YELLOW,lw=1));radii=[1,1.35,1.7];point=(1,0)
  for rad in radii:a.plot(1.8+rad*np.cos(t),.6+rad*np.sin(t),ls='--',c=RED,lw=.8)
  a.scatter([1.8],[.6],facecolors='white',edgecolors=INK,s=20);a.text(1.8,.72,'OLS 解');a.scatter(*point,c=INK,s=20);a.annotate('$\\widehat{w}$',point,xytext=(-18,-15),textcoords='offset points');a.text(.45,2.55,'$w_1^2+w_2^2\\leq1$' if i==0 else '$|w_1|+|w_2|\\leq1$')
 save(f,'regression-regularization','01-classic-models',{'theta_radians':t,'ridge_point':[.9486832981,.316227766],'lasso_point':[1,0]},{'J':'||w-(1.8,.6)||^2/2','unit_constraints':True,'ridge_radii':[.8973665961,1.2473665961,1.5973665961],'lasso_radii':[1,1.35,1.7]})
 d=load(C/'regression-neighborhood.csv');sel=load(C/'regression-neighborhood-selected.csv');f,aa=fig(169,76,ncols=2)
 for i,a in enumerate(aa):
  axes(a,(-.2,6.2),(-.35,4.5),'输入 $x$（无量纲）','响应 $y$（无量纲）',[0,2,4,6],[0,2,4]);a.set_title('（a）$k$-NN：邻域平均' if i==0 else '（b）LOESS：局部直线');lr=(1.8,3.8) if i==0 else (1.6,4)
  a.axvspan(*lr,color=YELLOW_FILL,zorder=0);a.scatter(d['x'],d['y'],facecolors='white',edgecolors=MUTED,s=16);a.scatter(sel['x'],sel['y'],color=BLUE,s=19);a.axvline(2.8,color=MUTED,ls='--',lw=.8)
  pred=1.2379 if i==0 else 1.170625706;xx=np.asarray(lr);a.plot(xx,np.full(2,pred) if i==0 else pred+.7259369997*(xx-2.8),c=YELLOW);a.scatter([2.8],[pred],marker='D',s=30,c=RED,zorder=5);a.text(.05,.95,'$k=4$' if i==0 else '$h=1.2$',transform=a.transAxes,va='top');a.text(2.9,4.12,'$x_0=2.8$')
 save(f,'regression-neighborhood','01-classic-models',{'x':d['x'],'y':d['y'],'selected_x':sel['x'],'selected_y':sel['y']},{'query':2.8,'knn_pred':1.2379,'loess_intercept':1.170625706,'loess_slope':.7259369997},[C/'regression-neighborhood.csv',C/'regression-neighborhood-selected.csv',C/'regression-neighborhood-values.tex'])
 d=load(C/'regression-gp-posterior.csv');o=load(C/'regression-gp-observations.csv');f,a=fig(112,82);axes(a,(-4,4),(-2.3,2.3),'输入 $x$（无量纲）','响应或函数值（无量纲）',[-4,-2,0,2,4],[-2,-1,0,1,2],True);a.fill_between(d['x'],d['lower'],d['upper'],color=YELLOW_FILL);a.plot(d['x'],d['mean'],c=YELLOW,label='后验均值');a.scatter(o['x'],o['y'],s=16,c=BLUE,label='带噪观测',zorder=4)
 for v in ['lower','upper']:a.plot(d['x'],d[v],c=YELLOW,ls='--',lw=.6)
 a.legend(loc='upper center',bbox_to_anchor=(.5,1.17),ncols=2)
 save(f,'regression-gp-posterior','01-classic-models',{n:d[n] for n in d.dtype.names},{'kernel':'squared exponential','mean':0,'ell':.9,'sigma_f':1,'observation_sigma':.18,'interval':'latent mean +/-1.96 posterior sd'},[C/'regression-gp-posterior.csv',C/'regression-gp-observations.csv'])
 d=load(C/'clustering-optics.dat');f,aa=fig(112,112,nrows=2,gridspec_kw={'height_ratios':[1,2]});a=aa[0];axes(a,(-.4,12.5),(-.5,.5),'原始特征值 $x$','',[0,4,8,12],[]);a.scatter(d['x'],np.zeros(len(d)),s=14,c=INK);a.spines['left'].set_visible(False)
 a=aa[1];axes(a,(.4,23.6),(0,1.15),'OPTICS 访问次序','距离',[1,8,14,23],[0,.4,.8]);a.axvspan(.5,7.5,color=BLUE_FILL);a.axvspan(13.5,22.5,color=YELLOW_FILL);a.vlines(d['order'],0,d['reach'],color=RED,lw=1);a.plot(d['order'],d['reach'],'o',c=RED,ms=3,label='可达距离');a.plot(d['order'],d['core'],'--',c=BLUE,label='核心距离');a.scatter(d['order'],d['restart'],marker='^',s=22,c=INK,label='可达距离 $+\\infty$');a.axhline(.35,color=INK,ls='-.',lw=.8);a.text(16,.41,"$\\varepsilon'=0.35$");a.legend(loc='upper center',bbox_to_anchor=(.5,-.24),ncols=2)
 save(f,'clustering-optics-reachability','01-classic-models',{n:d[n] for n in d.dtype.names},{'min_points':3,'includes_self':True,'eps_max':1.1,'infinity_display':'restart marker at1.05; missing reach values remain unconnected'},[C/'clustering-optics.dat'])
 d=load(C/'clustering-kde.dat');p=load(C/'clustering-mean-shift-path.dat');f,a=fig(112,79);axes(a,(-4,4),(0,.34),'位置 $y$','$\\widehat f(y)$',[-4,-2,0,2,4],[0,.1,.2,.3]);a.plot(d['x'],d['narrow'],c=INK,label='$h=0.6$');a.plot(d['x'],d['broad'],c=MUTED,ls='--',label='$h=2.4$')
 for side,c,m in [('left',YELLOW,'o'),('right',BLUE,'s')]:a.plot(p[side],p['f'+side],c=c,marker=m,ms=3);a.annotate('',(p[side][1],p['f'+side][1]),(p[side][0],p['f'+side][0]),arrowprops={'arrowstyle':'->','color':INK});a.text(p[side][0]+(-1.6 if side=='left' else .1),.06,'$y^{(0)}='+str(p[side][0])+'$')
 a.legend();save(f,'clustering-mean-shift-modes','01-classic-models',{'curves':{n:d[n] for n in d.dtype.names},'paths':{n:p[n] for n in p.dtype.names}},{'samples':[-2.5,-2,-1.5,1.5,2,2.5],'bandwidths':[.6,2.4]},[C/'clustering-kde.dat',C/'clustering-mean-shift-path.dat'])
 d=load(C/'clustering-gmm.dat');f,aa=fig(112,111,nrows=2,sharex=True);a=aa[0];axes(a,(-4,4),(0,.3),'','概率密度',[-4,-2,0,2,4],[0,.1,.2]);a.plot(d['x'],d['first'],c=YELLOW,label='$\\pi_1p_1(x)$');a.plot(d['x'],d['second'],c=BLUE,ls='--',label='$\\pi_2p_2(x)$');a.plot(d['x'],d['mixture'],c=INK,label='$p(x)$');a.axvline(0,c=MUTED,ls=':');a.legend(loc='upper center',bbox_to_anchor=(.5,1.25),ncols=3)
 a=aa[1];axes(a,(-4,4),(0,1.05),'观测值 $x$','成分后验',[-4,-2,0,2,4],[0,.5,1]);a.plot(d['x'],d['gammaone'],c=YELLOW);a.plot(d['x'],d['gammatwo'],c=BLUE,ls='--');a.axvline(0,c=MUTED,ls=':');a.scatter([0],[.5],s=17,c=INK);a.annotate('$\\gamma_1=\\gamma_2=0.5$',(0,.5),xytext=(.85,.5),arrowprops={'arrowstyle':'-','color':MUTED});a.text(-2,.7,'$\\gamma_1(x)$');a.text(2,.85,'$\\gamma_2(x)$')
 save(f,'clustering-gmm-responsibilities','01-classic-models',{n:d[n] for n in d.dtype.names},{'weights':[.5,.5],'means':[-1,1],'sigmas':[1,1]},[C/'clustering-gmm.dat'])
 x=np.linspace(0,4,150);f,a=fig(112,69);axes(a,(0,4),(0,1.05),'距离 $r$','核权重',range(5),[0,.25,.5,.75,1],True);a.plot(x,np.exp(-x*x),c=BLUE,label='$\\exp(-r^2)$');a.plot(x,1/(1+x*x),c=YELLOW,ls='--',label='$(1+r^2)^{-1}$');a.legend();save(f,'dim-neighbor-tails','01-classic-models',{'r':x,'gaussian':np.exp(-x*x),'student':1/(1+x*x)},{'samples':150,'normalization':'unnormalized affinities'})
 f,a=fig(112,77);axes(a,(-2.2,3.8),(-1.8,2.7),'$\\beta_1$','$\\beta_2$',[-2,-1,0,1,2,3],[-1,0,1,2]);a.set_aspect('equal')
 for rad in [.6,1.2,1.8]:a.plot(rad*np.cos(t),rad*np.sin(t),c=RED,ls='--',lw=.7)
 for rad in [.55,1.05,1.55]:a.plot(2+rad*np.cos(t),1+.55*rad*np.sin(t),c=BLUE,lw=.8)
 a.scatter([2],[1],facecolors='white',edgecolors=BLUE,s=26);a.text(2.04,1.04,'MLE');a.scatter([1.256],[.848],c=YELLOW,edgecolors=INK,s=24);a.text(.92,.63,'MAP');a.scatter([0],[0],c=RED,s=20);a.text(-.06,-.1,'先验中心',ha='right',va='top');a.annotate('',(1.38,.87),(1.9,.98),arrowprops={'arrowstyle':'->','color':INK})
 save(f,'regression-mle-map-geometry','01-classic-models',{'theta_radians':t,'MLE':[2,1],'MAP_display_rounded':[1.256,.848]},{'likelihood_mean':[2,1],'likelihood_scales':[1,.55],'prior_scale':1.3,'MAP_exact':[2/(1+1/1.3**2),1/(1+.55**2/1.3**2)]})

def extra_classic():
 f,a=fig(112,83);k=np.arange(1,8);b=np.array([4.5,3.5,2.5,1.7,1,.6,.4]);v=np.array([.3,.5,.8,1.2,1.9,2.8,4]);noise=np.full(7,.8)
 a.bar(k,b,width=.56,color=BLUE,label='偏差平方');a.bar(k,v,bottom=b,width=.56,color=RED,label='方差');a.bar(k,noise,bottom=b+v,width=.56,color=YELLOW,ec=INK,lw=.5,label='不可约噪声');a.axhline(.8,color=INK,ls='--',lw=.8);axes(a,(.4,7.6),(0,6.4),'模型复杂度','期望预测误差',[1,7],[]);a.set_xticklabels(['低','高']);a.legend(loc='upper right')
 save(f,'regression-bias-variance-noise','01-classic-models',{'complexity':k,'bias_squared':b,'variance':v,'irreducible_noise':noise},{'teaching_construction':True,'not_experimental':True})
 x=np.linspace(-4,4,121);sig=1/(1+np.exp(-x));f,a=fig(112,83);axes(a,(-4,4),(0,1.1),'得分 $z$','$p$',[-4,0,np.log(4),4],[0,.5,.8,1]);a.set_xticklabels(['−4','0','$\\log4$','4']);a.plot(x,sig,c=BLUE);a.axhline(1,color=GRID)
 for xx,yy,c,m in [(0,.5,RED,'o'),(np.log(4),.8,YELLOW,'s')]:
  a.plot([-4,xx,xx],[yy,yy,0],ls='--' if yy==.5 else '-.',c=c);a.scatter([xx],[yy],c=c,ec=INK if c==YELLOW else c,s=22,marker=m,zorder=3);a.text(xx+.25,yy-.07,'$\\tau='+str(yy)+'$')
 a.set_title('$z=w^\\top x+b\\;\\mapsto\\;p=\\sigma(z)$');a.text(.5,-.25,'预测正类：$p\\geq\\tau \\Leftrightarrow z\\geq\\log[\\tau/(1-\\tau)]$',transform=a.transAxes,ha='center')
 save(f,'classification-logistic-probability','01-classic-models',{'z':x,'p':sig,'thresholds':[0,np.log(4)]},{'sigma':'1/(1+exp(-z))','threshold_probs':[.5,.8]})
 f,aa=fig(169,93,ncols=2);t=np.linspace(0,2*np.pi,121);yy=np.linspace(-2.5,2.5,101)
 for i,a in enumerate(aa):
  axes(a,(-2.5,2.7),(-2.5,2.65),'$x_1$','$x_2$',[-2,0,2],[-2,0,2]);a.set_aspect('equal');a.plot(-1+np.cos(t),np.sin(t),c=BLUE);a.plot(1+np.cos(t),(1 if i==0 else 2)*np.sin(t),c=YELLOW,ls='--');a.scatter([-1],[0],c=BLUE,s=20);a.scatter([1],[0],c=YELLOW,ec=INK,s=20,marker='s');a.text(-1,-.5,'$\\mu_1$');a.text(1,-.5,'$\\mu_2$');a.plot(np.zeros(101) if i==0 else np.log(2)/2-3*yy**2/16,yy,c=RED);a.set_title('LDA：共享协方差' if i==0 else 'QDA：类特有协方差');a.text(.5,-.26,'$x_1=0$' if i==0 else '$x_1=\\log2/2-3x_2^2/16$',transform=a.transAxes,ha='center')
 save(f,'classification-gaussian-boundaries','01-classic-models',{'circle_t':t,'boundary_y':yy,'qda_boundary_x':np.log(2)/2-3*yy**2/16},{'priors':[.5,.5],'means':[[-1,0],[1,0]],'LDA_covariances':[[1,1],[1,1]],'QDA_covariances':[[1,1],[1,4]],'contours':'Delta_c=1, not equal density values'})

def hierarchical_and_diffusion():
 f,a=fig(112,79);axes(a,(-.6,6.35),(0,4.4),'样本','合并相异度',range(6),[0,1,2,3,4]);a.set_xticklabels(list('abcdef'))
 segments=[[(0,0),(0,1),(1,1),(1,0)],[(2,0),(2,1.4),(3,1.4),(3,0)],[(4,0),(4,.8),(5,.8),(5,0)],[(.5,1),(.5,2.7),(2.5,2.7),(2.5,1.4)],[(1.5,2.7),(1.5,3.8),(4.5,3.8),(4.5,.8)]]
 for points in segments:p=np.array(points);a.plot(p[:,0],p[:,1],color=INK,lw=.9)
 for yy,c,ls,label in [(1.9,YELLOW,'--','三个簇'),(3.2,BLUE,'-.','两个簇')]:a.plot([-.2,5.5],[yy,yy],c=c,ls=ls);a.text(5.65,yy,label,va='center')
 save(f,'clustering-dendrogram','01-classic-models',{'segments':segments,'cut_levels':[1.9,3.2]},{'merge_heights':'teaching construction, not measured','leaf_spacing':'arbitrary'})
 import importlib.util
 spec=importlib.util.spec_from_file_location('original_diffusion',C/'dim-diffusion-walk.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);snapshots,stationary=module.compute()
 # Preserve the original six-decimal displayed probabilities; exact fractions stay in source.
 arrays={str(t):np.array([[float(module.decimal(snapshots[t][row][j])) for j in range(6)] for row in [0,5]]) for t in [1,4,64]}
 from matplotlib.colors import LinearSegmentedColormap
 cmap=LinearSegmentedColormap.from_list('lancet_blue',['white',BLUE]);f=plt.figure(figsize=(112/25.4,133/25.4),layout='constrained');gs=f.add_gridspec(5,1,height_ratios=[3,1,1,1,.16]);g=f.add_subplot(gs[0]);g.set(xlim=(-.6,5.8),ylim=(-.8,2.0));g.axis('off');positions=np.array([[0,1.2],[0,-.2],[1.7,.5],[2.9,.5],[4.6,1.2],[4.6,-.2]])
 for i,j in [(0,1),(0,2),(1,2),(3,4),(3,5),(4,5)]:g.plot(positions[[i,j],0],positions[[i,j],1],c=BLUE if i<3 else RED,lw=.8,zorder=1)
 g.plot(positions[[2,3],0],positions[[2,3],1],c=RED,ls='--',lw=.6);g.text(2.3,.25,'0.15',ha='center');g.text(.7,1.7,'左团',ha='center');g.text(3.9,1.7,'右团',ha='center')
 for j,(xx,yy) in enumerate(positions):
  g.scatter([xx],[yy],s=185,marker='o' if j<3 else 's',fc='white',ec=BLUE if j<3 else RED,zorder=3);g.text(xx,yy,('左' if j<3 else '右')+str(j%3+1),ha='center',va='center');g.add_patch(Circle((xx,yy+(.19 if j not in [1,5] else -.19)),.16,fill=False,ec=MUTED,lw=.55,zorder=0))
 labels=['左1','左2','左3','右1','右2','右3']
 for i,t in enumerate([1,4,64]):
  a=f.add_subplot(gs[i+1]);v=arrays[str(t)];im=a.imshow(v,cmap=cmap,vmin=0,vmax=1/3,aspect='auto');a.set_yticks([0,1],['左1出发','右3出发']);a.set_xticks(range(6),labels if i==0 else []);a.xaxis.tick_top();a.tick_params(length=0);a.set_title('$t='+str(t)+'$',loc='left');a.axvline(2.5,c=MUTED,ls='--',lw=.6)
  for row in range(2):
   for col in range(6):a.text(col,row,f'{v[row,col]:.3f}',ha='center',va='center',color='white' if v[row,col]>.22 else INK)
 cbar=f.colorbar(im,cax=f.add_subplot(gs[4]),orientation='horizontal',ticks=[0,1/6,1/3]);cbar.set_label('概率',labelpad=2)
 save(f,'dim-diffusion-walk','01-classic-models',arrays,{'alpha':0,'kernel_within_group':1,'bridge_weight':.15,'row_stochastic':True,'stationary':[float(q) for q in stationary],'color_range':[0,1/3],'normalization':'same for all panels','exact_data_source':'dim-diffusion-walk.py Fraction matrix powers'},[C/'dim-diffusion-walk.py',C/'dim-diffusion-walk.tex'])

def neural():
 f,aa=fig(169,62,ncols=3)
 for i,a in enumerate(aa):
  xx=np.arange(2**(i+1)+1)/2**(i+1);yy=np.arange(len(xx))%2;axes(a,(0,1),(0,1.1),'$x$','',[0,.5,1],[0,1],True);a.plot(xx,yy,c=[BLUE,YELLOW,RED][i]);a.set_title('$T_'+str(i+1)+'(x)$ · '+str(2**(i+1))+' 个线性区间')
 save(f,'feedforward-depth-composition','02-neural-network-models',{f'T{i+1}':{'x':(np.arange(2**(i+1)+1)/2**(i+1)),'y':np.arange(2**(i+1)+1)%2} for i in range(3)},{'composition':'T(x)=2*x for x<=.5 else2*(1-x)'})
 x=np.linspace(0,80,161);tr=.05+.7*np.exp(-x/15);va=.16+.5*np.exp(-x/12)+.002*x;f,a=fig(112,78);axes(a,(0,80),(0,.8),'训练轮次 $t$','损失',[0,20,40,60,80],[0,.2,.4,.6,.8]);a.plot(x,tr,c=BLUE,label='训练损失');a.plot(x,va,c=YELLOW,ls='--',label='验证损失');a.axvline(36.43865,c=MUTED,ls='--');a.scatter([36.43865],[.2568773],c=RED,s=20,zorder=3);a.legend();save(f,'generalization-early-stopping','02-neural-network-models',{'t':x,'train':tr,'validation':va},{'train':'.05+.7exp(-t/15)','validation':'.16+.5exp(-t/12)+.002t','original_marked_min':[36.43865,.2568773]})
 t=np.linspace(0,2*np.pi,121);f,a=fig(112,83);axes(a,(-.45,1.75),(-.15,1.5),'$w_1$','$w_2$',[0,.5,1,1.5],[0,.5,1,1.5]);a.set_aspect('equal')
 for lev in [.15,.4,.8,1.6,3.2,4.8]:a.plot(np.sqrt(2*lev/4)*np.cos(t),np.sqrt(2*lev)*np.sin(t),c=GRID,lw=.5)
 a.plot(.8+.45*np.cos(t),.8+.45*np.sin(t),c=RED,ls='--');pts=np.array([[.8,.8],[1.237,.909],[.206,.691]])
 for pt,c,l,off in zip(pts,[BLUE,RED,YELLOW],['当前参数 $w$','$w+\\epsilon^\\star$','下一步 $w^+$'],[(-50,10),(4,7),(-45,-16)]):a.scatter(*pt,c=c,edgecolors=INK if c==YELLOW else c,s=20);a.annotate(l,pt,xytext=off,textcoords='offset points')
 a.annotate('',(1.19,.90),(.84,.81),arrowprops={'arrowstyle':'->','color':RED});a.annotate('',(.26,.70),(.75,.79),arrowprops={'arrowstyle':'->','color':INK});a.text(1.02,1.03,'内层上升');a.text(.22,.49,'$-\\eta\\nabla L(w+\\epsilon^\\star)$')
 save(f,'generalization-sam','02-neural-network-models',{'display_points':pts},{'loss':'(4*w1^2+w2^2)/2','rho':.45,'eta':.12,'display':'original rounded coordinates retained'})
 f,aa=fig(112,106,nrows=2,sharex=True,gridspec_kw={'height_ratios':[1,2]});x=np.arange(1,5);aa[0].bar(x,[.6,.6,0,.6],width=.3,color=BLUE_FILL,ec=BLUE);axes(aa[0],(.5,4.5),(0,.75),'','$a^{(t)}$',x,[0,.6]);a=aa[1];axes(a,(.5,4.5),(0,1.22),'时间区间 $t$','电位',x,[0,.5,1]);a.plot(x,[.6,1.08,.064,.6512],'-o',c=YELLOW,ms=4,label='$v^{(t)}$');a.scatter(x,[.6,.08,.064,.6512],facecolors='white',edgecolors=RED,s=22,label='$u^{(t)}$',zorder=4);a.axhline(1,c=MUTED,ls='--',lw=.8);a.annotate('',(2,.11),(2,1.08),arrowprops={'arrowstyle':'->','color':INK});a.legend(ncols=2,loc='upper center',bbox_to_anchor=(.5,1.23))
 save(f,'snn-lif','02-neural-network-models',{'t':x,'a':[.6,.6,0,.6],'v':[.6,1.08,.064,.6512],'u':[.6,.08,.064,.6512]},{'leak':.8,'threshold':1,'reset':'subtract spike threshold'})
 f,aa=fig(169,75,ncols=3);t=np.linspace(0,2*np.pi,121)
 for i,a in enumerate(aa):
  axes(a,(-3.2,3.2),(-3.2,3.2),'$x_1$','$x_2$',[-2,2],[-2,2]);a.set_aspect('equal');a.axhline(0,c=MUTED,lw=.7);a.axvline(0,c=MUTED,lw=.7);a.set_title(['原始尺度','逐坐标标准化','完整白化'][i]);a.plot((2 if i==0 else 1)*np.cos(t),.8*np.cos(t)+.6*np.sin(t) if i<2 else np.sin(t),c=[BLUE,YELLOW,RED][i])
 save(f,'training-whitening','02-neural-network-models',{'t_radians':t},{'curves':[['2cos(t)','.8cos(t)+.6sin(t)'],['cos(t)','.8cos(t)+.6sin(t)'],['cos(t)','sin(t)']]})
 f,aa=fig(112,110,nrows=2,sharex=True);x=np.linspace(1,64,801)
 for i,a in enumerate(aa):
  w=10000**(-2*i/8);axes(a,(1,64),(-1.15,1.15),'输入位置 $i$','幅值',[1,16,32,48,64],[-1,0,1],True);a.plot(x,np.sin(x*w),c=[BLUE,YELLOW][i],label='$\\sin(i\\omega_k)$');a.plot(x,np.cos(x*w),c=[BLUE,YELLOW][i],ls='--',label='$\\cos(i\\omega_k)$');a.set_title(('高频：坐标1、2' if i==0 else '低频：坐标3、4')+f' · $\\omega_{i}={w:g}$')
 aa[1].legend(loc='upper center',bbox_to_anchor=(.5,-.24),ncols=2)
 save(f,'transformer-position-waves','02-neural-network-models',{'position':x,'sin0':np.sin(x),'cos0':np.cos(x),'sin1':np.sin(.1*x),'cos1':np.cos(.1*x)},{'dimension':8,'omega':'10000^(-2k/8)','samples':801})
 # Preserve the stored rounded optimizer paths exactly, rather than rederive rounded trajectories.
 src=(N/'training-optimizer-trajectories.tex').read_text();blocks=re.findall(r'coordinates\s*\{(.*?)\};',src,re.S)[:3];paths=[np.array([[float(x),float(y)] for x,y in re.findall(r'\(([-.\d]+),([-.\d]+)\)',b)]) for b in blocks]
 assert all(len(p)==21 for p in paths)
 f,a=fig(112,108);axes(a,(-1.08,1.08),(-.27,1.08),'$\\theta_1$（陡方向）','$\\theta_2$（缓方向）',[-1,-.5,0,.5,1],[0,.5,1]);
 for lev in [.02,.08,.32,1.28,5.12,13]:a.plot(np.sqrt(2*lev/25)*np.cos(t),np.sqrt(2*lev)*np.sin(t),c=GRID,lw=.5)
 labels=['SGD：$\\eta=0.06$','Momentum：$\\eta=0.025,\\beta=0.75$','Adam：$\\eta=0.12,\\beta_1=0.8,\\beta_2=0.9$']
 for pa,c,m,lab in zip(paths,[BLUE,RED,YELLOW],['o','s','^'],labels):a.plot(pa[:,0],pa[:,1],c=c,marker=m,ms=2.6,markevery=2,label=lab)
 a.scatter([1],[1],c=INK,s=19);a.scatter([0],[0],c=YELLOW,ec=INK,s=20);a.text(.03,-.03,'极小点',va='top');a.text(-1.02,.03,'$q=(25\\theta_1^2+\\theta_2^2)/2$');a.legend(loc='upper center',bbox_to_anchor=(.5,1.32),ncols=1)
 save(f,'training-optimizer-trajectories','02-neural-network-models',dict(zip(['SGD','Momentum','Adam'],paths)),{'loss':'(25*theta1^2+theta2^2)/2','kappa':25,'initial':[1,1],'rounded_original_coordinates_preserved':True},[N/'training-optimizer-trajectories.tex'])
 # Curvature figure retains the exact same mesh and recursive trajectory values.
 f=plt.figure(figsize=(169/25.4,103/25.4),layout='constrained');a=f.add_subplot(121,projection='3d');b=f.add_subplot(122);xx=np.linspace(-.4,.4,17);yy=np.linspace(-1.2,1.2,17);X,Y=np.meshgrid(xx,yy);Z=50*X*X+.5*Y*Y;a.plot_wireframe(X,Y,Z,color=GRID,lw=.5);k=np.arange(81);px=.35*(-.5)**k;py=.985**k;pz=50*px*px+.5*py*py;a.plot(px,py,pz,c=BLUE,lw=1.2);a.scatter(px[:9],py[:9],pz[:9],c=BLUE,s=9);a.scatter([0],[0],[0],c=RED,s=17);a.set(xlim=(-.4,.4),ylim=(-1.2,1.2),zlim=(0,9),xlabel='$\\theta_1$',ylabel='$\\theta_2$',zlabel='$q$',title='（a）稳定步长 · $\\kappa=100$');a.view_init(elev=28,azim=55);a.text(px[0],py[0],pz[0],'0');a.text(px[-1],py[-1],pz[-1],'80');a.set_zlabel('');a.text2D(.02,.88,'$q$',transform=a.transAxes);axes(b,(-.45,.45),(-.06,1.08),'$\\theta_1$','$\\theta_2$',[-.35,0,.35],[0,.5,1]);b.set_title('（b）临界步长 · $\\kappa=100$')
 for lev in [.125,.5,2,6.125]:b.plot(np.sqrt(2*lev/100)*np.cos(t),np.sqrt(2*lev)*np.sin(t),c=GRID,lw=.5)
 kk=np.arange(21);qx=.35*(-1.)**kk;qy=.98**kk;b.plot(qx,qy,c=RED);b.scatter(qx[:7],qy[:7],s=9,c=RED);b.scatter([-.35,.35],[0,0],s=20,marker='s',c=RED);b.scatter([0],[0],s=20,c=YELLOW,ec=INK);b.text(.35,1,'0',ha='right');b.text(.35,.6676079718,'20',ha='right',va='top');b.annotate('',(.12,.928553136),(-.12,.935007024),arrowprops={'arrowstyle':'->','color':RED});b.annotate('',(-.12,.7435216068),(.12,.7486894373),arrowprops={'arrowstyle':'->','color':RED})
 save(f,'training-curvature','02-neural-network-models',{'mesh_x':xx,'mesh_y':yy,'stable_k':k,'stable_x':px,'stable_y':py,'critical_k':kk,'critical_x':qx,'critical_y':qy},{'loss':'(100*theta1^2+theta2^2)/2','eta_stable':.015,'eta_critical':.02,'mesh17x17':True,'view_degrees':[55,28]})
 f=plt.figure(figsize=(169/25.4,137/25.4),layout='constrained');a=f.add_subplot(221);x=np.linspace(-1.5,1.5,121);fx=1+(x*x-1)**2+.8*(x**3/3-x);axes(a,(-1.5,1.5),(0,3.4),'$x$','$F(x,0)$',[-1,0,1],[0,1,2,3]);a.plot(x,fx,c=BLUE);a.scatter([-1,1],[1.5333333333,.4666666667],c=YELLOW,ec=INK,s=20);a.scatter([-.2],[2.0794666667],c=RED,s=20,marker='s');a.text(-1,1.32,'局部极小',ha='center',va='top');a.text(.55,.58,'全局极小');a.set_title('（a）局部与全局极小');u=np.linspace(-1,1,13);X,Y=np.meshgrid(u,u);cut=np.linspace(-1,1,41)
 for pos,label,z,zlims in [(222,'（b）极小点：各方向上升',X*X+Y*Y,(0,2)),(223,'（c）极大点：各方向下降',-X*X-Y*Y,(-2,0)),(224,'（d）鞍点：上升与下降并存',X*X-Y*Y,(-1,1))]:
  a=f.add_subplot(pos,projection='3d');a.plot_wireframe(X,Y,z,color=GRID,lw=.5);a.plot(cut,np.zeros_like(cut),cut*cut if pos!=223 else -cut*cut,c=BLUE if pos!=223 else RED);a.scatter([0],[0],[0],s=19,c=YELLOW,edgecolors=INK)
  if pos==224:a.plot(np.zeros_like(cut),cut,-cut*cut,c=RED,ls='--')
  a.set(xlim=(-1,1),ylim=(-1,1),zlim=zlims,xlabel='$x$',ylabel='$y$',zlabel='$f$',title=label);a.view_init(elev=25,azim=45)
 save(f,'training-stationary-points','02-neural-network-models',{'x':x,'F_x_0':fx,'surface_mesh_axis':u,'cross_section':cut},{'F':'1+(x^2-1)^2+.8*(x^3/3-x)+y^2','stationary_points':[[-1,0],[-.2,0],[1,0]],'mesh_samples':13,'curve_samples':41})
