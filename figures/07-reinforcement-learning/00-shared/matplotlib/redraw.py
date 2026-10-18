#!/usr/bin/env python3
"""Volume 7 exact teaching plots, not benchmark measurements.

Formulae and constructed samples are saved alongside vector figures. The grid
uses the original rational-arithmetic model; the game coordinates are extracted
from the retained TeX recurrence, including its original rounding and tie rule.
"""
from pathlib import Path
import importlib.util
import hashlib
import json
import re
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
from matplotlib.patches import Ellipse, Rectangle

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file())
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
import plot_style as style
style.configure()
HERE=Path(__file__).resolve().parent
VOLUME=ROOT/'figures/07-reinforcement-learning'
B,G,Y,R,P=style.PALETTE
INK,MUTED,GRID=style.INK,style.MUTED,style.GRID
MM=1/25.4
DATA={}

def canvas(w=112,h=68,nrows=1,ncols=1,**kw):
    return plt.subplots(nrows,ncols,figsize=(w*MM,h*MM),layout='constrained',**kw)

def axis(ax,xlabel='',ylabel='',grid=False):
    ax.set_xlabel(xlabel);ax.set_ylabel(ylabel)
    ax.tick_params(labelsize=7.5)
    if grid:ax.grid(color=GRID,lw=.4)
    ax.set_axisbelow(True)

def text(ax,x,y,s,**kw):
    return style.note(ax.text(x,y,s,fontsize=7.5,color=INK,**kw))

def record(key,**data):
    DATA[key]={'kind':'constructed teaching data or analytic expression; not measurements',**data}

def draw_discount():
    key='rl-overview-discount';x=np.linspace(0,1,201);cross=np.sqrt(.4)
    f,a=canvas();a.plot(x,x*x,c=B);a.axhline(.4,c=G,ls='--')
    a.vlines(cross,0,.4,colors=MUTED,linestyles=':');a.plot(cross,.4,'o',c=INK,ms=3)
    a.set(xlim=(0,1),ylim=(0,1.04),xticks=np.linspace(0,1,6),yticks=np.linspace(0,1,6))
    axis(a,r'折扣因子 $\gamma$',r'起点回报 $G_0$',True)
    text(a,.8,.83,r'远路：$\gamma^2$');text(a,.04,.43,'近路：0.4')
    text(a,.65,.18,r'$\gamma_* = \sqrt{0.4}$'+'\n'+r'$\approx 0.63246$')
    record(key,domain=[0,1],expressions=['gamma**2','0.4'],intersection=float(cross));return f

def draw_threshold():
    f,a=canvas(h=56);a.step([0,1,2,3,4,5],[0,0,1,1,1,1],where='post',c=B)
    a.scatter(range(6),[0,0,1,1,1,1],c=B,s=17,zorder=3)
    a.scatter([2],[0],facecolors='white',edgecolors=B,s=17,zorder=3)
    a.set(xlim=(-.3,5.4),ylim=(-.18,1.4),xticks=range(6),yticks=[0,1])
    axis(a,r'整数队列状态 $x$',r'最优动作 $a^*_0(x)$')
    text(a,.5,.2,'保留');text(a,3.4,1.15,'清空');text(a,2.25,.6,'阈值2')
    record('rl-planning-threshold',states=list(range(6)),actions=[0,0,1,1,1,1],B=5,K=2.5,W=1,H=2);return f

def grid_module():
    p=next(VOLUME.rglob('rl-grid-reference.py'))
    spec=importlib.util.spec_from_file_location('rl_grid_reference',p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def grid_axes(ax):
    ax.set(xlim=(.5,4.5),ylim=(.5,3.5),xticks=[1,2,3,4],yticks=[1,2,3])
    ax.set_aspect('equal');ax.tick_params(length=0)
    for x in np.arange(.5,5):ax.axvline(x,c=GRID,lw=.5)
    for y in np.arange(.5,4):ax.axhline(y,c=GRID,lw=.5)
    ax.add_patch(Rectangle((1.5,1.5),1,1,fc=GRID,ec=MUTED,hatch='///',lw=.5))

def draw_occupancy():
    m=grid_module();data=m.figure_occupancy();f=plt.figure(figsize=(157.4*MM,82*MM))
    aa=[f.add_axes([.05,.28,.41,.57]),f.add_axes([.55,.28,.41,.57])]
    cm=LinearSegmentedColormap.from_list('occupancy',['white',style.BLUE_FILL,B])
    for a,name,title in zip(aa,['upper','lower'],['A  上路策略','B  下路策略']):
        z=np.full((3,4),np.nan)
        for key,d in data[name]['occupancy'].items():
            x,y=map(int,key.split(','));z[y-1,x-1]=d['decimal']
        im=a.imshow(z,extent=(.5,4.5,.5,3.5),origin='lower',vmin=0,vmax=.51,cmap=cm)
        grid_axes(a);a.set_title(title,loc='left')
        for (x,y),d in zip(m.STATES,[data[name]['occupancy'][f'{x},{y}']['decimal'] for x,y in m.STATES]):
            a.text(x,y+.16,f'{d:.3f}',ha='center',va='center',fontsize=8,color=INK)
            action=data[name]['actions'][f'{x},{y}']
            if action=='stop':a.text(x,y-.2,'G',ha='center',fontsize=8,color=INK)
            else:
                dx,dy=dict(up=(0,.3),down=(0,-.3),left=(-.3,0),right=(.3,0))[action]
                a.annotate('',xy=(x+dx/2,y-.23+dy/2),xytext=(x-dx/2,y-.23-dy/2),
                           arrowprops=dict(arrowstyle='->',lw=.7,color=INK))
        a.text(.8,.6,'S',ha='center',fontsize=7.5)
    f.colorbar(im,cax=f.add_axes([.30,.13,.40,.04]),orientation='horizontal',label=r'折扣占用量 $d^\pi(s)$',ticks=[0,.255,.51])
    record('rl-overview-occupancy',gamma=.9,probabilities=data,shared_color_range=[0,.51],absorbing_goal_included=True);return f

def draw_grid_values():
    m=grid_module();v=[m.F(0) for _ in m.STATES];snap={}
    for k in range(1,11):
        v=[max(m.qvalue(s,a,v) for a in m.actions(s)) for s in m.STATES]
        if k in [1,3,10]:snap[k]=[float(q) for q in v]
    f,aa=canvas(157.4,66,ncols=3)
    cm=LinearSegmentedColormap.from_list('values',[Y,'white',B]);norm=TwoSlopeNorm(0,-1,1)
    for a,(k,vv) in zip(aa,snap.items()):
        z=np.full((3,4),np.nan)
        for (x,y),val in zip(m.STATES,vv):z[y-1,x-1]=val
        im=a.imshow(z,extent=(.5,4.5,.5,3.5),origin='lower',cmap=cm,norm=norm)
        grid_axes(a);a.set_title(f'$k={k}$')
        for (x,y),val in zip(m.STATES,vv):a.text(x,y,f'{val:.4f}',ha='center',va='center',fontsize=7.5,color=INK)
        a.text(4.4,3.38,'g',ha='right',va='top',fontsize=7.5)
    f.colorbar(im,ax=aa,orientation='horizontal',fraction=.07,pad=.08,ticks=[-1,-.5,0,.5,1],label='共同价值色阶')
    record('rl-planning-grid-values',gamma=.9,initial_value=0,synchronous=True,states=m.STATES,iterations=snap,goal_value=0);return f

def draw_bandit():
    f,aa=canvas(157.4,67,ncols=2);a,b=aa
    means=np.array([.55,.48,.30]);half=np.array([.05,.20,.12])
    a.errorbar([1,2,3],means,yerr=half,fmt='o',c=B,ms=4,capsize=3,lw=1)
    a.plot(2,.68,'o',mfc='none',mec=Y,ms=8);a.set(xlim=(.5,3.5),ylim=(0,.78),xticks=[1,2,3])
    axis(a,'臂','均值');a.set_title('A  三臂区间快照',loc='left');text(a,1.7,.72,'上界最大：臂2')
    b.add_patch(Ellipse((2.5,1.7),3.8,1.3,fc=style.BLUE_FILL,ec=B,lw=1))
    b.plot(2.5,1.7,'o',c=INK,ms=3);b.annotate('',xy=(4.8,2.8),xytext=(2.5,1.7),arrowprops=dict(arrowstyle='->',color=G))
    text(b,3.25,2.9,r'动作方向 $\mathbf{x}$');text(b,2.5,1.4,r'$\widehat{\boldsymbol{\theta}}$',ha='center')
    b.set(xlim=(0,5.5),ylim=(0,3.4),xticks=[],yticks=[]);axis(b,r'$\theta_1$',r'$\theta_2$')
    b.set_aspect('equal');b.set_title('B  参数置信椭球示意',loc='left')
    record('rl-learning-bandit-geometry',means=means.tolist(),halfwidths=half.tolist(),ellipse_center=[2.5,1.7],ellipse_semiaxes=[1.9,.65]);return f

def draw_returns():
    f,aa=canvas(112,62,ncols=2,sharey=True)
    for a,x,p,title,col in [(aa[0],[.5],[1],'A  固定回报',B),(aa[1],[-.5,1.5],[.5,.5],'B  随机回报',G)]:
        a.vlines(x,0,p,colors=col,lw=1.1);a.scatter(x,p,c=col,s=18)
        a.axvline(.5,c=MUTED,ls=':',lw=.6);a.set(xlim=(-.8,1.8),ylim=(0,1.12),xticks=[-.5,.5,1.5],yticks=[0,.5,1])
        axis(a,'回报 $G$','概率质量');a.set_title(title,loc='left')
    record('rl-learning-return-distributions',A=dict(support=[.5],probabilities=[1]),B=dict(support=[-.5,1.5],probabilities=[.5,.5]),means=[.5,.5]);return f

def draw_linear():
    f,a=canvas(112,85);rx,ry=1/np.sqrt(101),1/np.sqrt(2)
    a.add_patch(Ellipse((0,0),2*rx,2*ry,fc=style.GREEN_FILL,ec=G,lw=1.1))
    a.axhline(0,c=MUTED,lw=.6);a.axvline(0,c=MUTED,lw=.6)
    a.set(xlim=(-.42,.72),ylim=(-.85,.85),xticks=[0],xticklabels=['0'],yticks=[-ry,0,ry],yticklabels=['−0.7071','0','0.7071'])
    a.annotate('0.0995',xy=(rx,0),xytext=(.23,-.17),fontsize=7.5,
               arrowprops=dict(arrowstyle='-',color=MUTED,lw=.6),color=INK)
    a.set_aspect('equal');axis(a,r'$\Delta w_1$',r'$\Delta w_2$')
    text(a,.2,.5,r'$\Lambda=\mathrm{diag}(101,2)$'+'\n第一方向样本100次\n第二方向样本1次\n正则化1')
    text(a,.2,-.4,r'$\Delta\mathbf{w}^{\mathsf{T}}\Lambda\Delta\mathbf{w}\leq1$')
    record('rl-learning-linear-design',precision=[101,2],semiaxes=[rx,ry],counts=[100,1],regularization=1);return f

def draw_double_curve():
    f,a=canvas(74,65);x=np.linspace(0,3,181)
    a.plot(x,(1-.5*x)**2,c=B,label='平均残差平方');a.plot(x,.5*(1-x)**2+.5,c=G,ls='--',label='样本残差平方')
    a.scatter([2,1],[0,.5],c=[B,G],s=14);a.set(xlim=(0,3),ylim=(0,2.6),xticks=[0,1,2,3],yticks=[0,1,2])
    axis(a,r'$\theta$','损失');a.legend(fontsize=7.5,loc='upper left')
    record('rl-learning-double-sampling-curve',domain=[0,3],expressions=['(1-.5*theta)**2','.5*(1-theta)**2+.5'],minimizers=[2,1],difference='theta**2/4');return f

def draw_ppo_curve():
    f,a=canvas(78,72);q=np.linspace(0,1.65,201)
    a.plot(q,np.minimum(q,1.2),c=B,label=r'$\widehat A=+1$')
    a.plot(q,-np.maximum(q,.8),c=G,ls='--',label=r'$\widehat A=-1$')
    for u in [.8,1.2]:a.axvline(u,c=GRID,ls=':',lw=.7)
    a.set(xlim=(0,1.7),ylim=(-1.85,1.7),xticks=[0,.8,1.2,1.6],yticks=[-1.6,-.8,0,.8,1.6])
    axis(a,'概率比率 $q$','单样本代理贡献');a.legend(fontsize=7.5,loc='upper left')
    record('rl-learning-policy-geometry-curve',epsilon=.2,domain=[0,1.65],expressions=['min(q,1.2)','-max(q,.8)']);return f

def draw_comparison():
    f,aa=canvas(112,94,nrows=2);a,b=aa;z=1.96;sed=np.sqrt(2-2*.98)
    for mean,y,col,mark in [(5,2,G,'o'),(4,1,B,'s')]:a.errorbar(mean,y,xerr=z,fmt=mark,c=col,ms=4,capsize=3,lw=1)
    a.set(xlim=(0,8),ylim=(.5,2.5),xticks=[0,2,4,6,8],yticks=[1,2],yticklabels=['$\pi_2$','$\pi_1$']);axis(a,'价值估计（回报）')
    b.axvline(0,c=MUTED,ls='--',lw=.7);b.errorbar(1,1,xerr=z*sed,fmt='D',c=Y,ms=4,capsize=3,lw=1)
    b.set(xlim=(-.2,1.6),ylim=(.5,1.5),xticks=[0,.4,.8,1.2,1.6],yticks=[1],yticklabels=['$\Delta$']);axis(b,'性能差估计（回报）')
    record('rl-information-comparison',means=[5,4],variances=[1,1],covariance=.98,z=z,delta_interval=[1-z*sed,1+z*sed]);return f

def draw_width():
    f,a=canvas();n=np.geomspace(4,256,256);rad=2/np.sqrt(n)
    a.axhspan(1,3,fc=style.GREEN_FILL);a.hlines([1,3],4,256,colors=G,linestyles='--',lw=.8)
    a.plot(n,1-rad,c=B);a.plot(n,3+rad,c=B);a.set_xscale('log',base=2)
    a.set(xlim=(4,256),ylim=(0,4.35),xticks=[4,16,64,256],xticklabels=['4','16','64','256'],yticks=range(5));axis(a,'样本量 $n$','价值（回报）')
    text(a,30,2,'不可消除的识别宽度',ha='center',va='center');text(a,10,4,'统计误差示意')
    a.annotate('',xy=(8,3.66),xytext=(8,3.04),arrowprops=dict(arrowstyle='<->',color=Y,lw=.8))
    record('rl-information-identification-width',n_range=[4,256],identified_interval=[1,3],statistical_radius='2/sqrt(n)');return f

def draw_pareto():
    f,a=canvas(h=73);x=[2,4,6];y=[4,7,8];a.plot(x,y,'o--',c=G,ms=4,lw=.9)
    a.plot(5,5,'s',mfc='none',mec=MUTED,ms=5);a.set(xlim=(0,7),ylim=(0,10),xticks=[0,2,4,6],yticks=range(0,11,2));axis(a,'能耗（任意单位，越小越好）','收益（任意单位）',True)
    for xx,yy,s in [(1.8,4,'甲'),(3.8,7.2,'乙'),(6,8.4,'丙'),(5.15,5,'丁：被支配')]:text(a,xx,yy,s)
    a.annotate('',xy=(4.15,6.7),xytext=(4.9,5.2),arrowprops=dict(arrowstyle='->',color=MUTED,lw=.7))
    record('rl-reward-pareto',policies=dict(A=[2,4],B=[4,7],C=[6,8],D=[5,5]),lines='visual guide only; no continuous feasible policies asserted');return f

def draw_overopt():
    f,aa=canvas(157.4,67,ncols=2,sharex=True,sharey=True);x=np.linspace(0,1,81)
    for a,yy,col,ls,title in zip(aa,[.2+.7*x,.2+1.2*x-x*x],[B,G],['-','--'],['A  代理奖励','B  独立任务表现']):
        a.plot(x,yy,c=col,ls=ls);a.set(xlim=(0,1),ylim=(0,1),xticks=[0,.5,1],yticks=[0,.5,1]);a.set_title(title,loc='left');axis(a,'优化强度 $x$','分数（任意单位）',True)
    aa[1].tick_params(labelleft=True);text(aa[1],.6,.63,'先升后降',ha='center')
    record('rl-reward-overoptimization',domain=[0,1],expressions=['.2+.7*x','.2+1.2*x-x**2']);return f

def draw_task_plane():
    f,a=canvas(h=73)
    for x,h in [(1,.4),(2,.4),(3,.2)]:a.add_patch(Rectangle((x-.12,0),.24,h,fc=style.GREEN_FILL,ec='none'))
    a.scatter([1,1,2,2,3],[.1,.3,.1,.3,.1],c=INK,s=15)
    for x,y,mark,col in [(1,.15,'o',B),(2,.2,'s',G),(3,.3,'^',Y),(4,.45,'x',INK)]:
        a.plot(x,y,marker=mark,mfc='none',mec=col,ms=6,ls='')
    for x,y,s in [(1.15,.15,'同分布'),(2.15,.2,'插值'),(2.8,.33,'未见组合'),(3.2,.48,'新因素范围')]:text(a,x,y,s)
    a.set(xlim=(.6,4.4),ylim=(0,.53),xticks=[1,2,3,4],yticks=np.arange(0,.51,.1));axis(a,r'目标 $(x,3)$ 的横坐标 $x$',r'总滑移概率 $\eta$')
    record('rl-transfer-task-plane',population_support={'1':[0,.4],'2':[0,.4],'3':[0,.2]},training_points=[[1,.1],[1,.3],[2,.1],[2,.3],[3,.1]],evaluation_points=[[1,.15],[2,.2],[3,.3],[4,.45]],goal_coordinate_discrete=True);return f

def draw_identification():
    f,aa=canvas(112,94,nrows=2,sharex=True);b=np.arange(81);e=.5*np.exp(-b/8);j=.2+.8*(1-np.exp(-np.maximum(b-20,0)/16))
    for a,y,col,label in zip(aa,[e,j],[B,G],['辨识误差 $e(B)$','策略回报 $J(B)$']):
        a.axvspan(0,20,fc=style.BLUE_FILL);a.axvline(20,c=MUTED,ls=':',lw=.7);a.plot(b,y,c=col);a.set(xlim=(0,80),xticks=[0,20,40,60,80]);axis(a,'',label)
    aa[0].set_ylim(0,.55);aa[1].set_ylim(0,1.05);aa[1].set_xlabel('累计目标交互 $B$（步）')
    record('rl-transfer-identification-curves',B=list(map(int,b)),expressions=['.5*exp(-B/8)','.2+.8*(1-exp(-max(B-20,0)/16))'],boundary=20);return f

def draw_tracking():
    f,a=canvas(h=78);x=[0,20,20,25,30,35,40,50,60];y=[.9,.9,.3,.3,.55,.75,.85,.9,.9]
    a.plot(x,y,c=B);a.fill([20,40,40,35,30,25,20],[.9,.9,.85,.75,.55,.3,.3],c=style.YELLOW_FILL)
    a.axhline(.85,c=MUTED,ls=':',lw=.7)
    for xx,col,txt,yy in [(20,Y,'变化',1.06),(25,INK,'检测',.98),(40,G,'恢复',1.06)]:
        a.axvline(xx,c=col,ls='--',lw=.7);text(a,xx,yy,txt,ha='center')
    text(a,32,.32,'检测延迟：5回合\n检测后恢复：15回合');text(a,1,.76,'恢复阈值0.85')
    a.set(xlim=(0,60),ylim=(0,1.16),xticks=[0,20,25,40,60],yticks=[0,.3,.6,.9]);axis(a,'部署回合 $k$','假设回报')
    record('rl-transfer-tracking',vertices=list(zip(x,y)),change=20,detection=25,recovery=40,recovery_threshold=.85,prechange_return=.9);return f

def draw_evaluation():
    f,a=canvas();b=np.array([0,10,20,30,40,50,60,80,100,120]);u=np.array([-.16,-.08,0,.08,.16]);v=np.array([-.02,0,.02])
    yy=.2+.7*(1-np.exp(-b[:,None,None]/30))+u[None,:,None]*np.exp(-b[:,None,None]/60)+v[None,None,:]
    taskmeans=yy.mean(2);mean=taskmeans.mean(1);sd=taskmeans.std(1,ddof=1)
    a.fill_between(b,mean-sd,mean+sd,fc=style.BLUE_FILL);a.plot(b,mean,'o-',c=B,ms=2.5,lw=1.1)
    a.set(xlim=(0,120),ylim=(0,1.04),xticks=[0,30,60,90,120],yticks=np.linspace(0,1,6));axis(a,'目标适应交互 $B$（步）','假设回报')
    text(a,5,.92,'5项假设任务，每项3个训练种子');text(a,42,.22,'任务均值 ±1 任务间标准差\n不是均值置信区间')
    record('rl-transfer-evaluation-curves',B=b.tolist(),task_offsets=u.tolist(),seed_offsets=v.tolist(),raw_values=yy.tolist(),mean=mean.tolist(),sample_sd=sd.tolist(),aggregation='average seeds within task, then sample SD across five task means');return f

def game_data():
    path=HERE/'matching-pennies-data.json'
    if not path.is_file():raise FileNotFoundError('Extract retained TeX recurrence first: '+str(path))
    return json.loads(path.read_text())

def draw_trajectories():
    d=game_data();f,aa=canvas(157.4,66,ncols=3)
    for a,key,title,col in zip(aa,['Sim','Alt','Hist'],['同时更新','交替更新','历史最佳响应'],[B,G,INK]):
        z=np.array(d[key]);a.plot(z[:,0],z[:,1],c=col,lw=.8)
        a.plot(.7,.5,'o',c=INK,ms=3);a.plot(.5,.5,'+',c=INK,ms=6)
        a.set(xlim=(0,1),ylim=(0,1),xticks=[0,.5,1],yticks=[0,.5,1]);a.set_aspect('equal');a.set_title(title)
        axis(a,'平均 $p$' if key=='Hist' else '$p$','平均 $q$' if key=='Hist' else '$q$')
    record('rl-multi-agent-trajectories',source='matching-pennies-data.json',eta=.1,points=121);return f

def draw_stability():
    d=game_data();f,a=canvas(112,81)
    for key,col,ls,label in [('CurrentGap',B,'-','当前策略总偏离间隙'),('AverageGap',G,'--','平均策略总偏离间隙'),('Regret',INK,':','两人平均外部遗憾正部的较大者')]:
        z=np.array(d[key]);a.plot(z[:,0],z[:,1],c=col,ls=ls,lw=1,label=label)
    a.set(xlim=(1,121),ylim=(0,.75));axis(a,'累计轮次 $n$','精确收益单位',True);a.legend(loc='upper center',bbox_to_anchor=(.5,-.19),fontsize=7.2)
    record('rl-multi-agent-stability',source='matching-pennies-data.json',points=121);return f

def draw_scaling():
    f,a=canvas();m=np.arange(2,41);full=.05*m+.01*m*(m-1);local=.05*m+.01*m*np.minimum(4,m-1)
    a.plot(m,full,c=B,label=r'全连接：$m(m-1)$ 条有向边');a.plot(m,local,c=G,ls='--',label='局部：每人最多4个出邻居')
    a.set(xlim=(2,40),ylim=(0,18));axis(a,'参与者数量 $m$','假设串行时延（毫秒）',True);a.legend(loc='upper left',fontsize=7.5)
    record('rl-multi-agent-scaling',domain=list(map(int,m)),expressions=['.05*m+.01*m*(m-1)','.05*m+.01*m*min(4,m-1)'],units='ms');return f

def draw_loss():
    f,aa=canvas(112,99,nrows=2,sharex=True)
    for a,x,p,title in zip(aa,[[1],[0,20]],[[1],[.95,.05]],['A  确定损失','B  偶发严重损失']):
        a.vlines(x,0,p,colors=B,lw=1.1);a.scatter(x,p,c=B,s=17);a.axvline(1,c=MUTED,ls=':',lw=.6)
        a.set(xlim=(-1,22),ylim=(0,1.13),xticks=[0,1,10,20],yticks=[0,.5,1]);axis(a,'损失 $L$','概率质量');a.set_title(title,loc='left')
    text(aa[0],5,.75,'均值1，0.95分位点1\n取原子中0.05质量，尾部均值1')
    text(aa[1],4,.7,'均值1，0.95分位点0');text(aa[1],9,.3,'20处的0.05质量\n全部进入尾部，尾部均值20')
    record('rl-trustworthy-loss',distributions=[dict(support=[1],mass=[1]),dict(support=[0,20],mass=[.95,.05])],means=[1,1],quantile95=[1,0],cvar95=[1,20]);return f

def draw_intervals():
    f,aa=canvas(157.4,110,nrows=2);a,b=aa;n=np.array([100,299]);upper=100*(1-.05**(1/n))
    for yy,uu,col in zip([2,1],upper,[B,G]):
        a.hlines(yy,0,uu,colors=col,lw=1.2);a.plot(uu,yy,'|',c=col,ms=8);a.plot(0,yy,'o',c=INK,ms=3)
        text(a,uu+.04,yy+.1,f'{uu:.4f}%',va='bottom')
    a.axvline(1,c=MUTED,ls='--',lw=.7);a.set(xlim=(0,3.65),ylim=(.5,2.6),yticks=[1,2],yticklabels=['$n=299$','$n=100$'],xticks=[0,1,2,3]);axis(a,'95%单侧失败概率上界（%）')
    a.set_title('A  零失败试验：上界需要不超过1%',loc='left');text(a,1.55,.64,'0.9969% < 1%；2.9513% > 1%')
    for yy,lo,hi,col in [(2,4,8,B),(1,5.5,6.5,G)]:b.errorbar(6,yy,xerr=[[6-lo],[hi-6]],fmt='o',c=col,capsize=4,lw=1.1,ms=3)
    b.axvline(5,c=MUTED,ls='--',lw=.7);b.set(xlim=(0,9),ylim=(.5,2.6),yticks=[1,2],yticklabels=['支持达标','尚不能判定'],xticks=[0,4,5,6,8]);axis(b,'回报（给定区间示意）');b.set_title('B  回报下界需要不低于5',loc='left')
    record('rl-trustworthy-intervals',zero_failure_n=n.tolist(),confidence=.95,upper_percent=upper.tolist(),probability_threshold_percent=1,schematic_return_intervals=[[4,8],[5.5,6.5]],return_estimate=6,return_threshold=5);return f

DRAWERS={
 'rl-overview-occupancy':draw_occupancy,'rl-overview-discount':draw_discount,
 'rl-planning-grid-values':draw_grid_values,'rl-planning-threshold':draw_threshold,
 'rl-learning-bandit-geometry':draw_bandit,'rl-learning-return-distributions':draw_returns,
 'rl-learning-linear-design':draw_linear,'rl-learning-double-sampling-curve':draw_double_curve,
 'rl-learning-policy-geometry-curve':draw_ppo_curve,'rl-information-comparison':draw_comparison,
 'rl-information-identification-width':draw_width,'rl-reward-pareto':draw_pareto,
 'rl-reward-overoptimization':draw_overopt,'rl-transfer-task-plane':draw_task_plane,
 'rl-transfer-identification-curves':draw_identification,'rl-transfer-tracking':draw_tracking,
 'rl-transfer-evaluation-curves':draw_evaluation,'rl-multi-agent-trajectories':draw_trajectories,
 'rl-multi-agent-stability':draw_stability,'rl-multi-agent-scaling':draw_scaling,
 'rl-trustworthy-loss':draw_loss,'rl-trustworthy-intervals':draw_intervals}

def main(keys):
    for key in keys:
        if key.startswith(('rl-overview','rl-planning','rl-learning')):part='01-problems-and-solving'
        elif key.startswith(('rl-information','rl-reward')):part='02-information-and-reward'
        else:part='03-task-expansion-and-trustworthiness'
        out=VOLUME/part/'matplotlib';out.mkdir(exist_ok=True)
        fig=DRAWERS[key]();style.prepare_figure(fig)
        fig.savefig(out/(key+'.pdf'));fig.savefig(out/(key+'.png'),dpi=300)
        (out/(key+'.data.json')).write_text(json.dumps(DATA[key],ensure_ascii=False,indent=2)+'\n')
        rec={'source':str(Path(__file__).relative_to(ROOT)),
             'data':str((out/(key+'.data.json')).relative_to(ROOT)),
             'physical_size_mm':[round(v*25.4,3) for v in fig.get_size_inches()],
             'main_font_pt':8,'note_font_pt':7.5,'style':style.style_record(),
             'review':'Rendering only; scientific and book-page review in redraw-manifest.json'}
        (out/(key+'.render.json')).write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
        plt.close(fig);print(key,flush=True)

if __name__=='__main__':main(sys.argv[1:] or list(DRAWERS))
