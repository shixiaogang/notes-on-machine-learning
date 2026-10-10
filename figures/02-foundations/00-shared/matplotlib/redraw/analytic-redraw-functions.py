def flat():
 s=np.linspace(-1,1,70);fig,axs=plt.subplots(1,2,figsize=(112*MM,71*MM),layout='constrained',sharex=True,sharey=True)
 for ax,factor,title,c in zip(axs,[.45,.08],['窄谷','宽谷'],[RED,BLUE]):
  risk=.1+factor*s*s;ax.plot(s,risk,color=c);ax.plot([.6,.6],[0,.1+factor*.36],color=MUTED,ls='--',lw=.6)
  ax.plot([0],[.1],marker='o',color=c);ax.plot([.6],[.1+factor*.36],marker='o',color=c,mfc='white')
  ax.set(title=title,xlim=(-1.1,1.1),ylim=(0,.62),xlabel=r'参数位移 $s$',xticks=[-1,0,1],yticks=[.1,.3,.5])
 axs[0].set_ylabel(r'$\hat R_S$')
 export(fig,'02-learning-theory','learning-theory-flat-sharp',{'formula':['.1+.45*s^2','.1+.08*s^2'],'domain':[-1,1],'samples':70,'common_displacement':.6,'risk_at_displacement':[.262,.1288],'teaching_same_parameterization':True})

def selection():
 x=np.linspace(1,9,80);ints=np.arange(1,10);train=lambda t:.3*np.exp(-.4*(t-1))+.02;val=lambda t:.13+.015*(t-5)**2
 fig,ax=plt.subplots(figsize=(112*MM,74*MM),layout='constrained')
 ax.plot(x,train(x),color=BLUE,label='训练误差');ax.plot(ints,train(ints),ls='none',marker='o',ms=3,color=BLUE)
 ax.plot(x,val(x),ls='--',color=RED,label='验证误差');ax.plot(ints,val(ints),ls='none',marker='s',ms=3,color=RED,mfc='white')
 ax.plot([5,5],[0,.13],color=MUTED,ls=':',lw=.7);ax.plot([5],[.13],ls='none',marker='o',ms=8,color=RED,mfc='none')
 ax.scatter([5],[.17],color=STROKE,marker='^',s=22,zorder=5)
 ax.annotate('测试误差',xy=(5,.17),xytext=(7,.30),ha='center',arrowprops={'arrowstyle':'-','color':MUTED,'lw':.7})
 ax.set(xlim=(1,9),ylim=(0,.48),yticks=[0,.1,.2,.3,.4],xlabel='模型复杂度',ylabel='经验误差',xticks=[1,3,5,7,9]);ax.legend(loc='upper center',ncols=2);ax.set_xticklabels(['1','3',r'$\hat k=5$','7','9'])
 export(fig,'02-learning-theory','learning-theory-model-selection',{'train_formula':'.3 exp(-.4(t-1))+.02','validation_formula':'.13+.015(t-5)^2','domain':[1,9],'samples':80,'integer_points':ints.tolist(),'validation_minimizer':5,'selected_test_error':.17,'no_test_error_curve':True,'constructed_teaching_example':True})

def ntk():
 path=FACTS/'figures/02-foundations/02-learning-theory/tikz/learning-theory-ntk-linearization.tex';txt=path.read_text()
 rows=re.findall(r'(\d)/([\d.]+)/([\d.]+)/([\d.]+)/([\d.]+)/([\d.]+)',txt)
 d=np.array(rows,dtype=float);assert d.shape==(7,6)
 a,b=1.,1.;exact=[]
 for t in range(7):
  f=a*np.tanh(b);lin=np.tanh(1)+np.tanh(1)*(a-1)+(1/np.cosh(1)**2)*(b-1)
  exact.append([t,a,b,f,lin,abs(f-lin)])
  residual=f-.9; grad_a=residual*np.tanh(b);grad_b=residual*a/np.cosh(b)**2
  a-=.3*grad_a;b-=.3*grad_b
 np.testing.assert_allclose(d,exact,atol=1e-12,rtol=0)
 fig,axs=plt.subplots(1,3,figsize=(169*MM,73*MM),layout='constrained')
 axs[0].plot(d[:,1],d[:,2],color=YELLOW,marker='o',ms=3);axs[0].plot(d[:1,1],d[:1,2],ls='none',marker='o',ms=5,color=YELLOW,mfc='white')
 axs[0].annotate(r'$\theta^{(0)}$',d[0,1:3],xytext=(5,5),textcoords='offset points');axs[0].annotate(r'$\theta^{(6)}$',d[-1,1:3],xytext=(-32,4),textcoords='offset points')
 axs[0].set(xlim=(1,1.13),ylim=(1,1.08),xlabel=r'$a$',ylabel=r'$b$',xticks=[1,1.05,1.1],yticks=[1,1.03,1.06])
 axs[1].plot(d[:,0],d[:,3],color=BLUE,marker='o',ms=3,label='真实');axs[1].plot(d[:,0],d[:,4],color=RED,ls='--',marker='s',mfc='white',ms=3,label='一阶');axs[1].legend(loc='upper left')
 axs[1].set(xlim=(0,6),ylim=(.75,.90),xlabel=r'更新次数 $t$',ylabel=r'$f(x_*)$',xticks=[0,2,4,6],yticks=[.75,.80,.85,.90])
 axs[2].plot(d[:,0],d[:,5],color=YELLOW,marker='o',ms=3);axs[2].set(xlim=(0,6),ylim=(0,.002),xlabel=r'更新次数 $t$',ylabel=r'$|f-f^{\mathrm{lin}}|$',xticks=[0,2,4,6],yticks=[0,.001,.002])
 export(fig,'02-learning-theory','learning-theory-ntk-linearization',{'formula':'a*tanh(b*x)','x_star':1,'target':.9,'loss':'half squared error','eta':.3,'initial':[1,1],'source_values':d.tolist(),'validation':'independent gradient recurrence agrees with source rounded values atol=1e-12','linearization':'tanh(1)+tanh(1)*(a-1)+sech(1)^2*(b-1)'})

def support():
 fig,axs=plt.subplots(1,3,figsize=(169*MM,68*MM),layout='constrained',sharex=True,sharey=True)
 for ax,(lo,hi),lab,mass in zip(axs,[(1.5,3.5),(3,5),(3.9,5.9)],'abc',[0,.5,.95]):
  ax.fill_between([1,4],[1/3]*2,color=BLUE_FILL);ax.plot([1,1,4,4],[0,1/3,1/3,0],color=BLUE)
  ax.fill_between([lo,hi],[.5]*2,color=RED_FILL);ax.plot([lo,lo,hi,hi],[0,.5,.5,0],color=RED,ls='--')
  if hi>4:ax.add_patch(Rectangle((4,0),hi-4,.5,facecolor=RED,alpha=.3,edgecolor='none'))
  ax.set(title=f'({lab})',xlim=(0,6),ylim=(0,.6),xlabel=r'$x$',xticks=[0,2,4,6],yticks=[0,1/3,.5],yticklabels=['0',r'$1/3$',r'$1/2$'])
  ax.text(3,.56,rf'$u_T={mass}$',ha='center')
 axs[0].set_ylabel(r'密度 $p$');axs[0].text(1.5,.22,r'$p_S$');axs[2].text(4.9,.40,r'$p_T$')
 export(fig,'02-learning-theory','learning-theory-support-coverage',{'source_uniform':[1,4],'source_density':1/3,'targets':[[1.5,3.5],[3,5],[3.9,5.9]],'target_density':.5,'uncovered_target_mass':[0,.5,.95]})

def importance():
 x=np.linspace(0,1,101); points=np.array([.1,.3,.5,.7,.9]);weights=2*points
 fig,ax=plt.subplots(figsize=(112*MM,74*MM),layout='constrained')
 ax.fill_between(x,0,2*x,color=RED_FILL);ax.plot(x,2*x,color=RED);ax.axhline(1,color=MUTED,ls='--',lw=.8)
 ax.scatter(points,2*points,s=45*weights,facecolor=BLUE_FILL,edgecolor=BLUE,zorder=5)
 ax.text(.07,1.11,'源域');ax.text(.83,2.04,'目标域')
 ax.set(xlim=(0,1.05),ylim=(0,2.22),xlabel=r'$x$',ylabel=r'密度 $p(x)$',xticks=[0,.1,.3,.5,.7,.9,1],yticks=[0,1,2])
 for px,w in zip(points,weights):ax.annotate(rf'$w={w:g}$',(px,2*px),xytext=(0,8 if w<.3 else -18),textcoords='offset points',ha='center')
 export(fig,'02-learning-theory','learning-theory-importance-weighting',{'source_density':'1 on [0,1]','target_density':'2x on [0,1]','weight_ratio':'2x','specified_source_points':points.tolist(),'weights':weights.tolist(),'point_areas_proportional_to_weights':True,'constructed_not_random':True})

def radar():
 counts=np.array([[4,2,1],[2,4,3]]);data=counts/4;angles=np.array([np.pi/2,7*np.pi/6,11*np.pi/6]);xy=np.column_stack((np.cos(angles),np.sin(angles)))
 fig,ax=plt.subplots(figsize=(112*MM,82*MM),layout='constrained');ax.set_aspect('equal');ax.set_axis_off()
 for q in [.25,.5,.75,1]:ax.plot(*np.vstack((q*xy,q*xy[0])).T,color='#D8DCE2',lw=.5)
 for v in xy:ax.plot([0,v[0]],[0,v[1]],color=STROKE,lw=.6)
 for label,v in zip(['保真度','覆盖范围','稳定性'],xy):ax.text(*(1.15*v),label,ha='center',va='center')
 for values,c,m,ls,lab in zip(data,[BLUE,RED],['o','s'],['-','--'],['甲','乙']):
  vertices=xy*values[:,None];closed=np.vstack((vertices,vertices[0]));ax.plot(*closed.T,color=c,marker=m,mfc='white' if lab=='乙' else c,ms=4,ls=ls,label=lab)
 ax.text(.12,1,'1');ax.text(.12,.5,'0.5');ax.legend(loc='lower center',bbox_to_anchor=(.5,-.05),ncols=2);ax.set(xlim=(-1.25,1.25),ylim=(-.9,1.23))
 export(fig,'03-trustworthiness','trust-explanation-quality-radar',{'checks_per_axis':4,'counts':counts.tolist(),'scores':data.tolist(),'axes':['保真度','覆盖范围','稳定性'],'constructed_coverage_scores_not_model_quality':True,'no_aggregation':True})
