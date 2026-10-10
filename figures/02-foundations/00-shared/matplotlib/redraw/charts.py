"""Re-evaluate explicit source formulas, counts and CSVs; render current fonts.

All arrays are complete teaching constructions or the existing training CSV.
No random examples, resampling, fitted statistics or old images are used.
"""
from pathlib import Path
import sys,json,hashlib,re,math,csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
from matplotlib.ticker import PercentFormatter
from matplotlib.transforms import offset_copy
from matplotlib.text import Text
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
OUT=Path(__file__).resolve().parent
ARCHIVE=json.loads((OUT/'archive.json').read_text())
def destination(key):return ROOT/ARCHIVE[key]['folder']
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
from plot_style import *
configure()
FACTS=OUT/'facts'
MM=1/25.4
YELLOW=GREEN # This class of fine quantitative curve requires a visible Lancet hue.
YELLOW_FILL=SAGE
GRAY=MUTED
SCOPE=json.loads((OUT/'scope.json').read_text())['figures']
LOOKUP={Path(f['source'][0]).stem:f for f in SCOPE}
RECORDS=[]
NAME_MAP={'risk-decomposition':'learning-theory-error-decomposition','double-descent':'learning-theory-double-descent','distribution-shift':'learning-theory-distribution-shift'}

def export(fig,part,name,data,panel=False):
    key=NAME_MAP.get(name,name);dest=destination(key);dest.mkdir(exist_ok=True)
    stem=name if panel else 'figure'
    prepare_figure(fig);fig.canvas.draw()
    labels=[];outside=[]
    for t in fig.findobj(Text):
        if not t.get_visible() or not t.get_text():continue
        box=t.get_window_extent(fig.canvas.get_renderer())
        labels.append({'text':t.get_text(),'bounds_pixels':list(box.bounds),'size_pt':t.get_fontsize(),'role':getattr(t,'academic_role','body')})
        if box.width and box.height and (box.x0<-.5 or box.y0<-.5 or box.x1>fig.bbox.width+.5 or box.y1>fig.bbox.height+.5):outside.append(t.get_text())
    for ext in ['pdf','svg','png']:fig.savefig(dest/f'{stem}.{ext}',dpi=300,facecolor='white')
    record={'key':key,'source':LOOKUP[key]['source'],'source_sha256':[hashlib.sha256((FACTS/p).read_bytes()).hexdigest() for p in LOOKUP[key]['source']],
      'data':data,'style':style_record(),'size_mm':(fig.get_size_inches()/MM).tolist(),
      'processing':{'filtering':'none','missing_values':'none; nonfinite rejected','sampling':'complete finite points or declared analytic grid','random_generation':'none'},
      'origin':'explicit book teaching construction; training CSV retains declared experiment inputs','files':[str((dest/f'{stem}.{e}').relative_to(ROOT)) for e in ['pdf','svg','png']],
      'outside_canvas_texts':outside,'renderer':'Matplotlib; freshly generated'}
    (dest/f'{stem}-data.json').write_text(json.dumps(record,ensure_ascii=False,indent=2))
    (dest/f'{stem}-labels.json').write_text(json.dumps(labels,ensure_ascii=False,indent=2))
    RECORDS.append(record);plt.close(fig)

def save(fig,name,spec,data=None):
    if data is not None:
        d=destination(NAME_MAP.get(name,name))/'input.csv'
        with d.open('w',newline='') as stream:csv.writer(stream).writerows([data[0]]+list(data[1]))
        spec['sampled_csv']='input.csv'
    export(fig,'02-learning-theory',name,spec)

def load_math_functions():
    namespace=globals()
    for filename in ['quantitative-redraw-functions.py','analytic-redraw-functions.py','risk-shift-functions.py']:
        text=(OUT/filename).read_text().replace("color='#D8DCE2'","color=GRID").replace('color="#EDF2F5"','color=BLUE')
        exec(compile(text,str(OUT/filename),'exec'),namespace)

def linear_panel():
    x=np.linspace(2,30,60)
    fig,axs=plt.subplots(1,2,figsize=(112*MM,50*MM),layout='constrained',sharex=True,sharey=True)
    for ax,title,y in zip(axs,['线性预测','非线性预测'],[4+.75*(x-2),4+.027*(x-2)**2]):
        ax.plot(x,y,color=GREEN);ax.set(title=title,xlabel='$x$',xlim=(0,32),ylim=(0,30),xticks=[],yticks=[])
    axs[0].set_ylabel(r'$\hat y$')
    export(fig,'01-basics','models-linear-nonlinear',{'functions':['4+.75*(x-2)','4+.027*(x-2)^2'],'domain':[2,30],'samples':60,'teaching_not_fitted':True},panel=True)

def discriminative_panel():
    x=np.linspace(-4,4,101);p=1/(1+np.exp(-2*x+np.log(4)));j0=.8*np.exp(-.5*(x+1)**2)/np.sqrt(2*np.pi);j1=.2*np.exp(-.5*(x-1)**2)/np.sqrt(2*np.pi)
    fig,axs=plt.subplots(2,1,figsize=(65*MM,99*MM),layout='constrained')
    axs[0].plot(x,p,color=GREEN);axs[0].set(xlim=(-4,4),ylim=(0,1),ylabel=r'$p_\theta(y=1\mid x)$',xlabel='$x$',xticks=[-4,0,4],yticks=[0,.5,1])
    axs[1].plot(x,j0,color=BLUE,label='$p(x,y=0)$');axs[1].plot(x,j1,color=RED,ls='--',label='$p(x,y=1)$');axs[1].set(xlim=(-4,4),ylim=(0,.36),ylabel='联合密度',xlabel='$x$',xticks=[-4,0,4],yticks=[0,.2]);axs[1].legend(loc='upper right',fontsize=7)
    export(fig,'01-basics','models-discriminative-generative',{'conditional':'sigmoid(2x-ln4)','joint_densities':['.8*N(-1,1)','.2*N(1,1)'],'domain':[-4,4],'samples':101,'discrete_mail_values_separate_from_continuous_example':True},panel=True)

def calibration_panel():
    x=np.linspace(0,1,41);fig,ax=plt.subplots(figsize=(78*MM,66*MM),layout='constrained')
    ax.plot(x,x,color=BLUE);ax.plot(x,x*x,color=RED,ls='--');ax.set(xlim=(0,1),ylim=(0,1),xlabel='预测概率 $p$',ylabel='事件频率',xticks=[0,.5,1],yticks=[0,.5,1]);ax.text(.1,.85,'理想校准');ax.text(.42,.1,'过度自信')
    export(fig,'03-trustworthiness','trust-calibration-discrimination',{'ideal':'p','overconfident':'p^2','domain':[0,1],'samples':41,'equal_size_group_rates':[.2,.8],'constant_scores':[.5,.5],'group_scores':[.2,.8]},panel=True)

def fairness_rate_panel():
    groups=['u','v'];values=[[24/100,52/100],[16/20,48/60],[16/24,48/52]];denoms=[['24/100','52/100'],['16/20','48/60'],['16/24','48/52']]
    fig,axs=plt.subplots(1,3,figsize=(169*MM,72*MM),layout='constrained',sharex=True)
    for ax,title,vs,ss in zip(axs,['人口统计均等','均等化赔率','正预测值均等'],values,denoms):
        ax.barh([1,0],vs,color=[BLUE,RED],height=.3);ax.set(xlim=(0,1.05),ylim=(-.45,1.7),yticks=[0,1],yticklabels=['$v$','$u$'],title=title,xticks=[0,.5,1]);ax.xaxis.set_major_formatter(PercentFormatter(1,decimals=0))
        for y,v,s in zip([1,0],vs,ss):ax.text(v+.02,y,s,va='center',fontsize=7.6)
    note(axs[1].text(.52,1.45,'两组假正例率也相同：8/80 = 4/40',ha='center',fontsize=7.4))
    export(fig,'03-trustworthiness','trust-fairness-incompatibility',{'n_each_group':100,'counts':{'u':{'TP':16,'FP':8,'positives':20,'negatives':80},'v':{'TP':48,'FP':4,'positives':60,'negatives':40}},'selection_rates':values[0],'true_positive_rates':values[1],'false_positive_rates':[.1,.1],'positive_predictive_values':values[2],'bars_from_zero':True})

def dp_panel():
    x=np.linspace(0,8,161);f=lambda m:.5*np.exp(-abs(x-m));p,q=f(3),f(4)
    fig,ax=plt.subplots(figsize=(109*MM,52*MM),layout='constrained')
    ax.plot(x,p,color=BLUE);ax.plot(x,q,color=RED,ls='--');ax.fill_between(x,0,p,where=(x>=5)&(x<=6),color=BLUE,alpha=.2);ax.fill_between(x,0,q,where=(x>=5)&(x<=6),color=RED,alpha=.15)
    ax.axvspan(5,6,color=GRID,alpha=.15,zorder=0);ax.set(xlim=(0,8),ylim=(0,.58),xlabel='输出 $u$',ylabel='概率密度',xticks=[0,3,4,5,6,8],yticks=[0,.25,.5]);ax.text(2.2,.43,'$D$');ax.text(4.3,.43,"$D'$ ");note(ax.text(5.5,.56,'E = [5,6]',ha='center',fontsize=7.7))
    export(fig,'03-trustworthiness','trust-dp-neighbors',{'Laplace_means':[3,4],'scale':1,'domain':[0,8],'samples':161,'event':[5,6],'adjacency':'one record added; counts3 and4'},panel=True)

def uniform_panel():
    positions=np.array([10,25,40,55,70,85]);population=np.array([31,22,27,18,24,20]);empirical=np.array([29,19,23,12,20,17])
    fig,ax=plt.subplots(figsize=(112*MM,68*MM),layout='constrained')
    for x,p,e in zip(positions,population,empirical):ax.plot([x,x],[e,p],color=MUTED,lw=.6);ax.plot([x-3,x+3],[p,p],color=RED,lw=1.5)
    ax.scatter(positions,empirical,color=BLUE,s=25);ax.axvspan(49,61,color=GREEN,alpha=.08);note(ax.text(55,7,'ERM输出',ha='center',fontsize=8));ax.set(xlim=(0,94),ylim=(0,45),xlabel='假设',ylabel='分类错误率（教学尺度）',xticks=[],yticks=[0,10,25,40]);ax.text(3,43,r'横线：期望风险 $R_{\mathcal{P}}(h)$',color=RED,fontsize=8);ax.text(48,43,r'圆点：经验风险 $\hat R_S(h)$',color=BLUE,fontsize=8)
    export(fig,'02-learning-theory','learning-theory-uniform-convergence',{'hypothesis_positions':positions.tolist(),'population':population.tolist(),'empirical':empirical.tolist(),'ERM_position':55,'teaching_not_empirical':True})

def local_panel():
    fig,ax=plt.subplots(figsize=(57*MM,50*MM),layout='constrained');left=0
    for value,color,label in [(1,GREEN,'基准'),(2,BLUE,'支付'),(4,RED,'附件')]:ax.barh([0],[value],left=left,color=color,height=.35);ax.text(left+value/2,.23,str(value),ha='center');ax.text(left+value/2,-.35,label,ha='center',fontsize=7.5);left+=value
    ax.axvline(6,color=STROKE,ls='--',lw=.75);ax.set(xlim=(0,8),ylim=(-.6,.7),yticks=[],xticks=[0,3,6],xlabel='评分');note(ax.text(6.15,.53,'阈值 6',fontsize=7.5));ax.spines['left'].set_visible(False)
    export(fig,'03-trustworthiness','trust-global-local-explanation',{'rule':'f=1+2*x1+4*x2','sample':[1,1],'components':[1,2,4],'threshold':6,'bars_proportional':True},panel=True)

def attribution_panel():
    fig,ax=plt.subplots(figsize=(57*MM,47*MM),layout='constrained');ax.barh([1,0],[2,4],color=[BLUE,RED],height=.32);ax.set(xlim=(0,5.6),ylim=(-.55,1.55),xticks=[0,2,4],yticks=[],xlabel='特征贡献');ax.text(2.1,1,'$a_1=2$',va='center');ax.text(4.1,0,'$a_2=4$',va='center')
    export(fig,'03-trustworthiness','trust-feature-attribution',{'input':[1,1],'baseline':[0,0],'rule':'f=1+2*x1+4*x2','gradient':[2,4],'integrated_gradients':[2,4],'contributions_not_probabilities':True},panel=True)

def conformal_panel():
    source=FACTS/'figures/02-foundations/03-trustworthiness/matplotlib/trust-conformal-residuals-data.json';spec=json.loads(source.read_text());v=np.sort(spec['residuals']);k=math.ceil((len(v)+1)*(1-spec['alpha']));assert k==8 and v[k-1]==.8
    fig,ax=plt.subplots(figsize=(106*MM,42*MM),layout='constrained');ax.bar(np.arange(1,10),v,color=[RED if i==7 else BLUE for i in range(9)],width=.65);ax.axhline(.8,color=RED,ls='--');ax.set(xlim=(.45,9.55),ylim=(0,1.05),xticks=np.arange(1,10),yticks=[0,.4,.8],xlabel='$i$',ylabel='$s_{(i)}$')
    for i,z in enumerate(v,1):ax.text(i,z+.015,f'{z:.1f}',ha='center',fontsize=7)
    export(fig,'03-trustworthiness','trust-conformal-construction',{**spec,'source_file':str(source.relative_to(ROOT)),'full_sort':True},panel=True)

if __name__=='__main__':
    load_math_functions()
    failures=[]
    for fn in [training,point_distribution,coverage,robustness,fairness,proxy,flat,selection,ntk,support,importance,radar,error_decomposition,double_descent,distribution_shift,linear_panel,discriminative_panel,calibration_panel,fairness_rate_panel,dp_panel,uniform_panel,local_panel,attribution_panel,conformal_panel]:
        try:fn();print(fn.__name__,'rendered',flush=True)
        except Exception as exc:failures.append({'function':fn.__name__,'error':str(exc)});plt.close('all');print(fn.__name__,'FAILED',str(exc),flush=True)
    (OUT/'charts-records.json').write_text(json.dumps(RECORDS,ensure_ascii=False,indent=2))
    (OUT/'chart-failures.json').write_text(json.dumps(failures,ensure_ascii=False,indent=2))
    print('Fresh chart-containing figures:',len(RECORDS))
