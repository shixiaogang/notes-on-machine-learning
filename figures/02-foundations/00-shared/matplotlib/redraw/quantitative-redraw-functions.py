def single(height=75):
    fig, ax = plt.subplots(figsize=(112*MM,height*MM), layout='constrained')
    return fig, ax

def training():
    path = FACTS/'figures/02-foundations/01-basics/tikz/introduction-training-loss.csv'
    d = np.genfromtxt(path, delimiter=',', names=True)
    assert len(d)==61 and np.array_equal(d['step'], np.arange(61))
    assert all(np.isfinite(d[name]).all() for name in d.dtype.names)
    fig,ax=single(68)
    ax.plot(d['step'],d['train_loss'],color=BLUE,label='训练集')
    ax.plot(d['step'],d['validation_loss'],color=RED,ls='--',label='验证集')
    ax.axvline(20,color=YELLOW,ls=':',lw=1)
    ax.text(21,.277,'选定检查点',color=MUTED,va='bottom')
    ax.set(xlim=(0,60),ylim=(.25,.72),yticks=[.3,.4,.5,.6,.7],xlabel=r'迭代次数 $t$',ylabel='平均交叉熵损失')
    ax.grid(True);ax.legend(loc='upper right')
    export(fig,'01-basics','introduction-training-loss',{'file':str(path.relative_to(ROOT)), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),'rows':61,'fields':list(d.dtype.names),'checkpoint':20})

def point_distribution():
    x=np.linspace(16,28,601)
    density=np.exp(-.5*((x-22)/2)**2)/(2*np.sqrt(2*np.pi))
    fig,axs=plt.subplots(1,2,figsize=(112*MM,68*MM),layout='constrained',gridspec_kw={'width_ratios':[.85,1.15]})
    a,b=axs
    a.set(title='一个预测值',xlim=(16,28),ylim=(-.025,.225),xlabel='温度（°C）')
    a.spines['left'].set_visible(False);a.spines['bottom'].set_position(('data',0));a.set_yticks([])
    a.set_xticks([16,20,22,24,28]);a.scatter([22],[0],s=35,facecolors=YELLOW,edgecolors=STROKE,zorder=4)
    a.annotate(r'$\hat y=22$',xy=(22,0),xytext=(22,.09),ha='center',arrowprops={'arrowstyle':'-','color':MUTED,'linestyle':'--'})
    b.set(title='一个预测分布',xlim=(16,28),ylim=(0,.225),xlabel='温度（°C）',ylabel=r'密度（$(^{\circ}\mathrm{C})^{-1}$）')
    b.set_xticks([16,20,24,28]);b.set_yticks([0,.1,.2]);b.plot(x,density,color=YELLOW)
    b.fill_between(x,0,density,where=(x>=20)&(x<=24),color=YELLOW_FILL)
    export(fig,'01-basics','models-point-distribution',{'formula':'Normal(mean=22 Celsius, std=2 Celsius)','domain':[16,28],'samples':601,'shade_interval':[20,24],'x':x.tolist(),'density':density.tolist(),'note':'Original TikZ used rounded millimetre coordinate transformation; evaluate stated exact normal density.'})

def coverage():
    orders=[list(range(1,11)),[9,10,3,4,5,6,7,8,1,2]]
    risks=[]
    for order in orders:
        risks.append(np.cumsum(np.isin(order,[9,10]))/np.arange(1,11)*100)
    assert risks[0][7]==0 and risks[1][7]==25 and risks[0][-1]==risks[1][-1]==20
    x=np.arange(1,11)*10; fig,ax=single(76)
    ax.plot(x,risks[0],color=BLUE,marker='o',mfc='white',ms=4)
    ax.plot(x,risks[1],color=RED,ls='--',marker='^',mfc='white',ms=4)
    ax.plot([80,80],[0,25],color=MUTED,ls=':',lw=.6)
    ax.text(81,29,r'乙：$2/8$');ax.text(77,3,r'甲：$0/8$',ha='right')
    ax.text(23,96,'分数乙');ax.text(20,9,'分数甲')
    ax.set(xlim=(0,100),ylim=(0,105),xlabel=r'处理比例 $\hat c(t)$（%）',ylabel=r'接受部分风险 $\hat R_{\mathrm{sel}}(t)$（%）',xticks=np.arange(0,101,20),yticks=np.arange(0,101,25))
    export(fig,'03-trustworthiness','trust-risk-coverage-curve',{'n':10,'error_ids':[9,10],'orders':orders,'coverage_percent':x.tolist(),'risk_percent':[r.tolist() for r in risks],'undefined_at_zero_coverage':True,'source_rounding':'source TikZ displayed risk to 6 decimals; retain exact rational counts'})

def robustness():
    natural=np.array([80,88,94,90]);robust=np.array([70,60,45,74]);assert np.all(robust<=natural)
    fig,ax=single(79)
    ax.plot(natural[:3],robust[:3],color=BLUE,ls='--',marker='o',mfc='white',ms=5)
    ax.plot([90],[74],color=RED,marker='D',mfc='white',ms=5,ls='none')
    for lab,x,y,dx,dy in [('A',80,70,-.7,1),('B',88,60,-1,-3),('C',94,45,.5,-2),('D',90,74,.5,1)]:ax.text(x+dx,y+dy,lab)
    ax.annotate('',xy=(89.7,72),xytext=(88.3,62),arrowprops={'arrowstyle':'-|>','color':RED,'lw':.9})
    ax.set(xlim=(74,100),ylim=(35,85),xlabel='原输入准确率（%）',ylabel='鲁棒准确率（%）',xticks=np.arange(75,101,5),yticks=np.arange(40,81,10))
    export(fig,'03-trustworthiness','trust-robust-accuracy-tradeoff',{'n':100,'constructed_teaching_example':True,'natural_correct':natural.tolist(),'robust_correct':robust.tolist(),'candidate_labels':list('ABCD')})

def fairness():
    counts=np.array([[38,40,36,36],[40,45,40,41],[40,50,45,45],[38,46,38,38],[38,50,42,42]])
    gap=np.abs(counts[:,0]-counts[:,1])/50*100;acc=counts.sum(axis=1)/200*100
    assert np.allclose(gap,[4,10,20,16,24]) and np.allclose(acc,[75,83,90,80,86])
    fig,ax=single(79)
    ax.plot(gap[:3],acc[:3],color=BLUE,ls='--',marker='o',mfc='white',ms=5)
    ax.plot(gap[3:],acc[3:],color=MUTED,ls='none',marker='x',ms=6)
    for i,lab in enumerate('ABCDE'):ax.annotate(lab,(gap[i],acc[i]),xytext=(-8,5) if i<3 else (4,-12),textcoords='offset points')
    for start,end in [((15,80.5),(11,82.5)),((23.5,87),(21,89))]:ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'-|>','color':BLUE,'lw':1})
    ax.set(xlim=(0,30),ylim=(70,100),xlabel=r'真正例率差 $\Delta(f)$（百分点，越小越好）',ylabel='准确率（%，越高越好）',xticks=np.arange(0,31,5),yticks=np.arange(70,101,5))
    export(fig,'03-trustworthiness','trust-fairness-pareto',{'n':200,'group_size':100,'positives_per_group':50,'negatives_per_group':50,'columns':['TP_u','TP_v','TN_u','TN_v'],'counts':counts.tolist(),'gap_percentage_points':gap.tolist(),'accuracy_percent':acc.tolist(),'constructed_teaching_example':True})

def proxy():
    sr=np.linspace(0,1,41);su=np.linspace(0,1,61);r=.2+.8*sr;u=.2+2.8*su*(1-su)
    assert np.isclose(u.max(),.9) and np.isclose(su[u.argmax()],.5)
    fig,ax=single(77);ax.plot(sr,r,color=BLUE,ls='--');ax.plot(su,u,color=RED)
    ax.plot([.5,.5],[0,.9],ls=':',lw=.6,color=MUTED)
    ax.text(.96,1.03,r'$r(s)$',ha='right',va='bottom');ax.text(.28,.82,r'$U(s)$',va='bottom')
    ax.set(xlim=(0,1),ylim=(0,1.12),xlabel=r'代理优化强度 $s$（教学归一量）',ylabel='归一评分',xticks=[0,.5,1],yticks=[0,.2,.6,1])
    export(fig,'03-trustworthiness','trust-proxy-overoptimization',{'r_formula':'.2+.8*s','U_formula':'.2+2.8*s*(1-s)','domain':[0,1],'r_samples':41,'U_samples':61,'constructed_teaching_example':True,'not_empirical_research_data':True,'r_values':r.tolist(),'U_values':u.tolist()})
