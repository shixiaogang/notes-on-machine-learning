from pathlib import Path
import json, difflib, hashlib

# 人工写出的建议文本；程序只定位旧行、保存old/new、产生diff，不作语义判断。
OUT=Path(__file__).resolve().parent
SRC=OUT/'snapshots/tex/03-foundations/03-trustworthiness'
PROPOSED=OUT/'proposed-sources/tex/03-foundations/03-trustworthiness'
changes=[]
def change(f,a,b,new,ids):
    old='\n'.join((SRC/f).read_text().splitlines()[a-1:b])
    changes.append(dict(file=f,lines=[a,b],old=old,new=new,findings=ids))

change('01-foundations.tex',76,76,r'''知道不同错误的成本后，我们可以从损失推导处置阈值。这里比较邮件隔离和放行，按各行动在当前输入下的期望损失选择。设$p$为给定输入下邮件属于垃圾邮件的真实概率，误拦成本为$c_{\mathrm{fp}}>0$，漏放成本为$c_{\mathrm{fn}}>0$，正确处理暂不计成本。隔离只有遇到正常邮件才产生损失，其条件期望为$(1-p)c_{\mathrm{fp}}$；放行的条件期望为$pc_{\mathrm{fn}}$。选择损失较小的行动，隔离条件便是''',['CVT10'])
change('01-foundations.tex',81,81,r'''两项损失相等时，当前模型下的行动等价。误拦成本越高，隔离所需的概率越高，阈值因此不必是0.5（可参考\BookDefinitionRef{def:decision-conditional-risk-bayes-rule}{第一卷“策略的价值与优化”章的“条件风险与Bayes决策”定义}）。实践中代入的是估计概率，决策质量便依赖估计质量。若干概率区间的平均预测与事件频率吻合，只给出分组证据，不能证明每个输入上的概率准确；第~\ref{chap:trust-reliability}章将展开这些区别和检验。''',['CVT10'])
change('02-reliability.tex',53,53,r'''贝叶斯方法用参数后验给候选规律分配权重。以下采用给定协变量$\bm x$的条件模型，假设给定参数后未来目标与训练资料$\mathcal D$条件独立，并使用相应的概率质量函数或密度。记参数为$\bm{\theta}$、后验密度为$p(\bm{\theta}\mid\mathcal D)$，对每个参数的条件预测取后验平均，得到''',['CVT04'])
change('02-reliability.tex',71,71,r'''第一项平均每个模型的条件方差，第二项计算模型预测均值的后验分歧，分别对应所建模型的偶然波动和参数知识不足。分解成立于这套概率模型，尚未证明现实因素全部被涵盖；候选模型如果共同遗漏因素，均值分歧很小仍可能系统性出错（可参考\BookSectionRef{sec:statistics-scoring-calibration}{第一卷“随机变量”章的“预测分布的计算与评价”小节}及其中的后验预测计算）。''',['CVT04'])
change('02-reliability.tex',75,75,r'''一种近似是选择易抽样的分布族$q_{\bm{\phi}}(\bm{\theta})$，让参数$\bm{\phi}$调节它与后验的差异。设$p(\mathcal D\mid\bm{\theta})$为似然、$p(\bm{\theta})$为先验，并假设证据$0<p(\mathcal D)<\infty$。以下候选$q_{\bm\phi}$对后验绝对连续，后验KL有限；为将目标拆成两项，还要求$\mathbb E_{q_{\bm\phi}}|\log p(\mathcal D\mid\bm\theta)|<\infty$与先验KL有限。在这些条件下，以KL散度比较近似和后验，可等价最小化目标''',['CVT03'])
change('02-reliability.tex',83,83,r'''记此目标为$\mathcal J(\bm{\phi})$，因为$\operatorname{KL}(q_{\bm{\phi}}(\bm{\theta})\|p(\bm{\theta}\mid\mathcal D))=\mathcal J(\bm{\phi})+\log p(\mathcal D)$，与$\bm{\phi}$无关的证据项不影响优化（可参考\BookSectionRef{sec:information-elbo-approximation}{第一卷“概率分布”章的“表示约束下的分布逼近”一节}）。似然项要求候选解释数据，KL项约束偏离先验。优化替代了直接积分，却无法突破近似族本身的限制，例如独立单峰分布未必容纳相距很远的多种解释；收敛也不消除这一限制。''',['CVT03'])
change('02-reliability.tex',148,148,r'''邮件的0.9需要对照哪些结果？二分类中记$y\in\{0,1\}$，$p(\bm{x})$报告$y=1$的概率，我们检查同一分数下的事件均值：''',['CVT10'])
change('02-reliability.tex',154,154,r'''\term{校准}（calibration）于是要求，相同概率报告在总体中有相符的事件频率。条件期望形式也适用于连续分数，避免对概率为零的精确分数集合直接计算普通频率（可参考\BookDefinitionRef{def:statistics-probability-calibration}{第一卷“随机变量”章的“二元概率校准”定义}）。''',['CVT10'])
change('02-reliability.tex',312,312,r'''先固定训练得到的评分$s(\bm{x},y)$，大值表示候选与模型较不相符，训练与校准资料分开。假设给定训练资料及训练所用随机性后，$n$个校准样本与一个未来样本可交换，且同一固定评分用于它们。对校准样本计算$s_i=s(\bm{x}_i,y_i)$，目标错误水平$\alpha\in(0,1)$确定接受秩和集合：''',['CVT01'])
change('02-reliability.tex',320,320,r'''在上述条件下，未来分数的可交换秩使这一构造满足''',['CVT01','CVT10'])
change('02-reliability.tex',325,325,r'''给定训练资料及训练随机性后，这一概率仍同时平均校准和未来样本；解除训练条件后，不等式同样成立。使用$\leq q$纳入边界并列分数只增加覆盖（可参考\BookTheoremRef{thm:probability-split-conformal-coverage}{第一卷“随机变量”章的“拆分共形的有限样本覆盖”定理}）。覆盖目标固定以后，还需比较评分造成的范围大小与后续行动代价。''',['CVT01','CVT10'])
change('03-robustness.tex',241,241,r'''允许分布族$\mathfrak Q$需先按任务规定，例如容许已声明环境的比例改变，或容许参考分布附近预设距离内的变化。\term{分布鲁棒优化}（distributionally robust optimization, DRO）比较族内最高风险，并从模型候选$\mathcal F$中寻找降低这一风险的模型。此处监督学习目标为''',['CVT10'])
change('03-robustness.tex',247,247,r'''它将每个候选模型在允许分布族内的最高期望损失作为比较依据（可参考\BookSectionRef{sec:decision-risk-criteria-robustness}{第一卷“策略的价值与优化”章的“策略的轨迹价值与风险”一节}中的“概率约束与模型不确定性”小节）。采用这一训练或压力目标所得的模型仍需独立测试，目标值本身没有给部署程序提供证书。若要概率上界，则需从抽样来源明确的$S=\{(\bm{x}_i,y_i)\}_{i=1}^n$构造$\widehat{\mathfrak Q}(S)$，用独立资料或预设统计规则选距离、矩约束、半径或组，并证明真实分布以声明概率在其中；经验推广与内层近似误差也需控制。过小漏变化，过大包含无意义压力，可积性、上确界取得或近似方式均影响保证。''',['CVT10'])
change('04-fairness.tex',203,203,r'''关注禁止因素怎样传递影响时，需要因果模型。反事实公平（counterfactual fairness）固定同一个体的外生背景，再比较不同群体属性干预下的预测，而非直接配对现实中的两人；Kusner等据此给出定义\scite{kusner2017counterfactual}。''',['CVT10'])
change('04-fairness.tex',205,205,r'''令$\bm U,\bm X,A$为外生背景、观测和属性，取值为$\bm u,\bm x,a_0$；此处$\hat Y\in\{0,1\}$表示是否给予机会的二元决策。$\hat Y_{A\leftarrow v}(\bm U)$表示属性设为允许值$v$后的决策。要求对事实分布$P_{\bm X,A}$几乎处处的$(\bm{x},a_0)$，全部$b\in\{0,1\}$与允许的$v$满足''',['CVT05'])
change('04-fairness.tex',215,215,r'''事实观测先推断外生背景，同一机制再生成干预世界。只改一列却固定其后果，没有完成这种反事实传播（可参考\BookDefinitionRef{def:causal-counterfactual-fairness}{第一卷“因果响应”章的“反事实公平”定义}）。''',['CVT10'])
change('04-fairness.tex',451,451,r'''为避免把后续收益混入资格，记培训结果$z$，获得机会$r=1$，潜在结果$z(1)$，选择概率$e(\bm{x},a)=\mathbb P(r=1\mid\bm{x},a)$。假设所考察群体具有正概率，$z(1)$在该群体内可积；给定特征和属性时$r$独立于$z(1)$，$e>0$在该群体的特征分布下几乎处处成立，且获选者$z=z(1)$。逆概率加权于是给出''',['CVT08'])
change('04-fairness.tex',457,457,r'''$r=0$时乘积定义零，无需观察其$z$。先条件化再用独立性消去选择概率，最后组内平均便得右侧（可参考\BookSectionRef{sec:causal-point-identification}{第一卷“因果响应”章的“响应目标的点识别”小节}中的逆概率表示）。审核者使用未记录的信息，可能破坏这一条件独立性，小概率放大方差，做加权之前需检查这些条件。''',['CVT08'])
change('05-alignment.tex',36,36,r'''仅以清空收件箱打分，无法区分删除与归档的后果。为分析实际目标与训练信号的差别，设任务轨迹为$\tau$，在授权、规范与后果聚合方式固定后，以$U(\tau)\in\mathbb R$评价实际后果，较大值表示更符合给定目标。这个标量是分析模型中的对象；其数值未必可观测，也不存在适用于所有主体的唯一取值。不可补偿的约束仍须另行表达。固定环境模型，从历史$h$实施当前动作$a$，再按后续策略$\pi$生成轨迹。若$U$在该轨迹规律下可积，动作的期望效用为''',['CVT07'])
change('05-alignment.tex',38,38,r''' Q_U^\pi(h,a)=\mathbb E_{h,a}^{\pi}[U(\tau)]\text{。}''',['CVT07'])
change('05-alignment.tex',40,40,r'''$\mathbb E_{h,a}^{\pi}$表示按环境转移与策略从给定历史、动作继续生成的轨迹规律取平均，未要求历史行为曾以正概率选取这个动作。静态候选排序也可以把后续过程纳入这个期望。实际系统通常只能取得评分、点击、比较标签或完成标记，再由这些观察构造奖励$r(h,a)$。奖励与效用在原数据中相关，只支持相应分布上的代理关系；加强优化后是否仍一致，需要继续检验。''',['CVT07'])
change('05-alignment.tex',74,74,r'''邮件整理既希望提高效率，也需要限制误删等风险成本，因而只最大化效率奖励还不足以表达全部要求。设策略$\pi$按历史$h_t$选择动作$a_t$，$r_t$为奖励，$c_t\geq0$为风险成本，$T$为时域，$b$为预算。一种常见表述为''',['CVT10'])
change('05-alignment.tex',81,81,r'''它限制平均累计成本，因而不能保证每条轨迹都满足要求（可参考\BookSectionRef{sec:policy-trajectory-return}{第一卷“策略的价值与优化”章的“轨迹收益与策略价值”小节}和\BookSectionRef{sec:decision-risk-criteria-robustness}{同章的“策略的轨迹价值与风险”一节}）。明确禁止的动作需要在动作集合或执行权限中排除；失败概率要求则需先定义失败事件，再建立相应概率约束。''',['CVT10'])
change('05-alignment.tex',129,129,r'''这里观察的是比较结果，奖励函数是用来解释这些结果的模型。若不同奖励函数给出相同比较概率，数据便不能区分它们；在未覆盖的候选上也不能仅凭拟合结果确定排序（可参考\BookSectionRef{sec:future-analysis-identification}{第一卷“数学基础与后续研究”章的“训练样本生成规律下的统计目标可识别性”小节}）。''',['CVT10'])
change('05-alignment.tex',238,238,r'''行为约束中，有些规则可以由独立于模型措辞的授权记录与执行检查实现。此时需要验证状态转移保持边界，而不是要求模型每次都正确复述规则。''',['CVT10'])
change('05-alignment.tex',246,246,r'''若初始状态安全，每步都有可执行安全动作，执行器只实施该集合中的动作，且真实转移被$\mathcal T$覆盖，便可逐步归纳：安全状态经过允许动作仍到达安全状态。因此这一结论依赖状态、转移覆盖和执行权限三方面的前提（可参考\BookSectionRef{sec:control-safety-cbf}{第一卷“策略的实现与轨迹控制”章的“策略的约束与安全”一节}中的离散状态保持条件）。''',['CVT10'])
change('06-interpretability.tex',112,112,r'''\term{累积局部效应}（accumulated local effects, ALE）在现有取值附近估计小幅变化，再沿特征累积，以减少远离数据支持的替换。这里限定连续特征的一个有界区间$I$，并将参考总体限制在其中：$P_{\mathrm{ref}}(X_j\in I)=1$，$X_j$的Lebesgue密度在$I$上几乎处处为正。假设模型对第$j$项可微，相应导数在条件分布下可积，条件导数均值在$I$上绝对可积。对$t_0,t\in I$，一阶表达为''',['CVT02'])
change('06-interpretability.tex',121,121,r'''$t_0$是积分起点，$C_j$使结果在同一$P_{\mathrm{ref}}$下中心化。正密度条件使条件均值的版本差异只落在Lebesgue零测集上，不改变这里的积分；绝对可积条件也保证累积值与中心化常数有限（可参考\BookDefinitionRef{def:probability-regular-conditional-distribution}{第一卷“随机变量”章的“正则条件分布”定义}及其版本边界）。实际可将取值分箱，在每箱已有样本上查询边界差并累加平均差，不必计算导数\scite{apley2020ale}。离散特征或无数据区间需要另行声明差分或外推约定，不能由上述积分自动确定。''',['CVT02'])
change('06-interpretability.tex',296,296,r'''预测解释还可以比较特征组合的输出增量，再平均每项在所有加入次序中的增量，以形成贡献分配。设$N=\{1,\ldots,d\}$，$\mu(S)$为按规定的缺失特征填充方式保留当前特征子集$S$时的平均输出。将背景输出$b=\mu(\varnothing)$单列，并令$v(S)=\mu(S)-b$，于是$v(\varnothing)=0$。第$j$项贡献为''',['CVT06','CVT10'])
change('06-interpretability.tex',303,303,r'''SHAP（Shapley additive explanations）利用这种分配形成加性贡献；完整输入的贡献之和为$f(\bm x)-b$，背景输出$b$另作截距。缺失特征怎样补充、使用何种分布，决定$\mu(S)$、基准与所解释问题\scite{lundberg2017shap}（可参考\BookDefinitionRef{def:game-shapley-value}{第一卷“多方策略的响应与演化”章的“Shapley值”定义}）。''',['CVT06','CVT10'])
change('06-interpretability.tex',305,305,r'''边缘背景采样给出$\mu(S)=\mathbb E[f(\bm x_S,\bm X_{-S})]$，主要比较人工组合上的响应；$v(S)=\mu(S)-b$只扣除同一个背景常数，不改变各项加入时的增量。按已知特征条件采样则保留关联，也可能给未被模型直接读取但预测其他特征的变量分配贡献，仍须按同一背景输出中心化。二者依定义回答不同问题。精确枚举有指数规模，结构方法或采样近似应报告背景与计算误差。''',['CVT06'])
change('06-interpretability.tex',497,497,r'''误拦解释之后，使用者还需要可执行恢复路径。\hyperref[sec:interpretability-local-counterfactual]{“不同结果的反事实比较”段}找到了改变判断的输入，尚未说明如何实现。\term{行动补救}（algorithmic recourse）寻找在权限与现实后果约束下能够达到目标的行动；这里进一步考察权限、流程负担、公平与现实验证（可参考\BookSectionRef{sec:causal-action-recourse}{第一卷“因果响应”章的“目标约束下的行动补救”小节}）。''',['CVT10'])
change('06-interpretability.tex',557,557,r'''模型内可算还不同于证据可识别。多套结构模型可能符合相同观察甚至边缘干预资料，却预测不同个体后果。应先声明证据与领域假设允许的模型类，再报告方案、成本与成功概率对模型的敏感性，必要时施加类上的稳健约束。缺失识别依据不能仅当参数误差处理（可参考\BookSectionRef{sec:causal-factual-counterfactual}{第一卷“因果响应”章的“事实条件下的反事实计算”小节}及其中的跨世界识别边界）。''',['CVT10'])

patch=[]; hashes=[]
for f in sorted({c['file'] for c in changes}):
    old=(SRC/f).read_text(); new=old
    for c in [c for c in changes if c['file']==f]:
        assert new.count(c['old'])==1,(f,c['lines'])
        new=new.replace(c['old'],c['new'],1)
    dest=PROPOSED/f;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(new)
    repo='tex/03-foundations/03-trustworthiness/'+f
    patch+=list(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='a/'+repo,tofile='b/'+repo))
    hashes.append(dict(file=f,old_sha256=hashlib.sha256(old.encode()).hexdigest(),proposal_sha256=hashlib.sha256(new.encode()).hexdigest()))
(OUT/'old-new-proposals.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
(OUT/'proposal-manifest.json').write_text(json.dumps(hashes,ensure_ascii=False,indent=2)+'\n')
(OUT/'proposed.patch').write_text(''.join(patch))
print(len(changes),'人工替换建议；仅写ignored build中的提案与diff，未修改正文。')
