# 第3章R2特殊单元：正式陈述、证明、例子与算法

CH03-R2-SF，2026-10-12，修订1；独立R2；正文hash `927887345166301fb9aaa47eb6a53ec8389f7abfe6353bc87e5b27b5049f353e`。三级顺读见C、P1-P6、W1-W11及句界文件。以下从亲自第三遍所读正文形成正式单元记录，补定义/量词/完整证明/算法全步骤，不由枚举脚本生成语义。图表、全部展示式及关键行内式另续文件。

## 定义D01-D09

| ID、位置短引 | 对象、白话、边界与具体依据 |
|---|---|
| D01 L71-74「探索的几种评价对象」 | 累积回报损失、最终推荐臂均值差、需要比较行为的样本覆盖、最终策略起点平均损失四对象。分别指定评价时刻、参照及初始分布，共享特征方向明确非导航方向；正式块未声称四指标互斥或一个代另。W-L73-a/b/c/d逐句。 |
| D02 L86-96「有界随机老虎机」 | K固定臂、历史条件下固定独立[0,1]奖励；定义均值/最优/差距/访问数。伪遗憾是均值的差非偶然轨迹差，按臂访问分组等式准确。参数/量词/奖励界和自适应条件齐；最大取所有K臂高均值，E只均算法访次，W-L88/L95。 |
| D03 L1654-1659「学习模型的预测对象」 | 确定模型输出状态，随机模型输出后继分布；贝叶斯参数后验积分与多拟合集成属另层。动力学、奖励均值、继续概率分别职责，联合(s',r,c)可保相关。前局部非格点条件均值揭正确输出为何重要，非定义罗列代机制。 |
| D04 L2154-2157「想象轨迹」 | 真历史后验为根，后动作策略、后状态模型、奖/继续预测头。离根无新obs用先验，不偷未来obs编码；来源/时间条件清。紧接RSSM只提供当前算法所需最小计算，不借后信息章补定义。 |
| D05 L2421-2429「半马尔可夫与Markov Option」 | SMDP每调用有终点/累计奖/随机K；ω=(I,pi,beta)，I启动集/内动作/抵达终止概率。先至少一步后检测、仅(s,ω)依赖、zeta限I合法者；K0/历史依赖额外状态不暗混。W-B句界单列完整三元定义。 |
| D06 L2595-2606「互信息与赋能」 | 固s0和时域，I技能/后果是posterior/prior log均或后果熵减少。赋能max允许原子动作序列分布的I(Actionseq;S_K|s0)，候选域/高辨识方向明，闭环技能改变控制类要另定义；不是MI高=任务可解，前后反例明确。 |
| D07 L2848-2863「线性MDP与混合MDP」 | 前者已知phi(s,a)、未知R系数/后继向量测度对所有B；概率非负全空间1。后者已知base kernels、未知simplex权；一般系数也需合法核。known/unknown位置与下一V依赖不同，不能交换理论保证。 |
| D08 L2949-2963「实现性与完备性」 | 时刻F类/终F_H={0}，实现仅Q*成员，完备对任意nextf真实最优T备份都在本类；若另G则T F⊂G。域/量词/两类区别齐，单候选两步反例及匹配闭合反向归纳明确。 |
| D09 L2970-2984「Bellman因子分解」 | roll-in pi_g至t，再t/t+1按pi_f，平均候选残差E_t(f,g)。每t存在统一M维ν(g)/ξ(f)内积与norm product ζ界；rank作用环境/F/访问分布，不是网络权矩阵rank。白话指出到哪和候选哪错，算法不需知道因子。 |

## 定理T01-T14与证明PR01-PR11

| ID、位置、短引 | 完整陈述或证明的人工核对 |
|---|---|
| T01 L377-392「固定参数前后向更新等价」 | 有限终止可微V固定theta、e_-1=0，回合后一次总更新；lambda目标残差梯度和=delta迹和。不扩大到每步变参任网络。 |
| PR01 L393-418「望远镜…系数…交换有限和」 | n步V相消得折扣delta，几何混权给(gamma lambda)^j；lambda0/1由定义核，有限三角和交换得迹递推展开。全部等式和端点已人工核，未省在线变参关键条件。 |
| T02 L458-473「轨迹与逐决策IS」 | 有限H、固pi/mu、同起点/环境、目标绝对连续、每奖目标绝对可积；完整权与每奖前缀权均恢复目标E G。每步rho/pi-mu及区段W定义齐。 |
| PR02 L474-495「消共同核…前缀…绝对可积」 | full密度比动作积，同环境/起点消；prefix边缘密度比W0:t，先对|r|换测度核可积再signed r，有限奖和得逐决策。不在pi0行为历史错误假设未来ratio条件均1。 |
| T03 L655-665「条件方差分解」 | x=s或(s,a)二阶可积delta，E(delta²|x)=E(delta|x)²+Var；Var可依theta，两argmin一般不同非必异。 |
| PR03 L666-672「中心化展开」 | 定m=E delta|x，展开平方，条件cross均0、首项Var，三项全核。无可积缺口或无故交换无限和。 |
| T04 L957-965「Q误差到贪心性能」 | 有限折扣、全合法pair q对Q* sup误差eps，逐state合法q最大策略，损失sup≤2eps/(1-gamma)。不是训练MSE替sup或Qpi替Q*。 |
| PR04 L966-982「两误差…Bellman…展开n消尾」 | 真optimala与q chosena通过q greedy删非正差，误差两端≤2eps；同chosen Bellman递归gap，有限n几何累和尾因有界gamma^n消，逐s取sup。所有候选/方向/倍数由步骤支持。 |
| T05 L1034-1044「有限似然比梯度」 | 有限状态动作/H、邻域可微合法a正、核起点独theta/奖界沿入口；z logpi导，gradient E sum gamma^t z Gtail。 |
| PR05 L1045-1071「trajectory因子…score零均…删过去奖」 | 只pi随theta求p导，有限和/奖界支持交换；抽a前h score条件0使过去r项消，future sum=gamma^t G_t。没有漏timeweight或假设环境可微。 |
| T06 L1113-1121「动作前基线零均」 | b历史动作前可测，乘积可积，E(score b)=0，完整G减b不改期望gradient。准确V不是必要前提，停止导和同批依赖在正文另限。 |
| PR06 L1122-1131「b出条件均…归一导0」 | 固h时b常数，sum pi gradlogpi=grad1=0，塔性质/有限time和。核得是均值不变非一定方差下降。 |
| T07 L1233-1242「性能差恒等式」 | finite discount两平稳pi/pi'、奖有界同rho0，Jnew-Jold=(1-gamma)^-1 E_newdpi,newpi Aold。均值域为新占用非旧数据。 |
| PR07 L1243-1256「旧V的望远镜」 | 新trajectory条件Aold=r+gamma oldVnext-oldVnow，乘gamma^t有限sum，tail旧V有界消；sameinitial旧V均=Jold，归一新占用定义得系数。L1247正文延续已专门列句ID。 |
| T08 L1447-1456「熵正则变分」 | finite legal action任意有限q、alpha>0，simplex max averageq+alphaH=alpha logsumexp，unique positive softmax。连续无界不直接继承。 |
| PR08 L1457-1467「目标=logZ-alphaKL」 | logp*=q/alpha-logZ代目标得constant−alphaKL；KL非负唯一0，finiteq保证正支撑，无0分母。正常数缩放/候选约束明。 |
| T09 L1993-2010「固定策略模型误差界」 | 同finite合法SA/gamma<1两MDP奖励均绝≤Rmax，逐pair奖励差epsR/转移L1epsP；任固定平稳pi value sup及同rho0 J差≤B。不是单行为平均误差条件。 |
| PR09 L2012-2030「三个差项与移项」 | pi平均保R/P界，hatV≤Rmax/(1-gamma)；Bellman相减加减P hatV，随机矩阵不扩sup及L1乘sup，移gamma值差得双折扣分母；sameinitial平均保sup。全部三项和常数规范核，TV要另倍数。 |
| T10 L2464-2469「Option压缩」 | rewardbound/gamma<1、每可用K≥1且a.s.有限、内部/beta固定，有界tail V/W，固定高平均与可启动Option max备份≤gamma sup差。W-B补独立固规则前提句。 |
| PR10 L2471-2481「累计奖消…E gamma^K…max不扩」 | 同规则奖消，只tailgamma^K(V-W)，K≥1使E gamma^K≤gamma；prob平均及max差≤max逐ω差，再sup_s。L2480完整中文尾读，不跳到Option永不终事件。 |
| T11 L2803-2816「UCBVI-BF遗憾界」 | onlinefinite已知det[0,1]R/timehomogeneousP/H/V_H0，T=KH、Llog、原BFalgo+bonus，highprob显三项。归一/时齐/原algorithm不可省。 |
| T12 L2908-2926「LSVI-UCB代表保证」 | onlineH/finitea/det[0,1]R、knownphi≤1、theta≤sqrt d、所有boundedv向量measure界、lambda1/beta足够；highprob d³H³T尺度，无oracle但maxa/phi需可算。 |
| T13 L2988-2998「OLIVE有限类PAC」 | fixedresetH、finitea、nonnegative总episode奖≤1、finiteF N/[0,1]/终0/Q*实现、M factor ζ≥1；原阈值batch样本回合bound并乘H才真feedback。 |
| T14 L3053-3062「一步辨识下界」 | 两environment同state两a/H1，Bernoulli action1 .5±Delta/action2 .5，Delta≤.25；adaptive n、any stochasticoutput，两环境PAC eps=Delta/4、δ<.25，n≥(16Delta²)^-1 log1/(4δ)。W-B把环境规模和奖差独立句列清。 |
| PR11 L3063-3081「gap要求→检验→KL」 | outputp在plus≥.75/minus≤.25，threshold>.5两err≤2δ；history同alg的KL链仅action1 E N1 timeskl，kl=2Delta log ratio≤16Delta²；two-lawerr≥.5 exp−KL联立移项。内部代数/时序完整核，所用外部检验不等式本章未重新证明，一手未外查。 |

T11-T13正文并未给完整原论文证明：L2818-2840与L2930-2942及L3002-3033是明确标注的证明支点/算法机制说明。已亲自全文读并逐句判断，不能把这些说明冒称完成外部全部证明验收。其余PR01-PR11正文完整证明皆纳入本记录；不构建或数值程序执行。

## 例子EX01-EX10

| ID、位置短引 | 输入、过程、结果、教学范围 |
|---|---|
| EX01 L98-101「噪声锁贪心」 | 两Bernoulli .7/.4各试一次(0,1)prob .12；首估0未再访，另首次1使有限mean永>0，永久错选有充分机制，不依平局或近均值。 |
| EX02 L308-322「同终轨迹不同目标」 | 6网格转移第一次墙滑原地，五-.04+终1，G0 .426686/G1 .51854/everymean .472613；冻V .2/.3给TD .14/.23，lr.5分别TD .17/MC .313343。都是同初值独立比较非串行/真V解。 |
| EX03 L578-581「三个一步目标」 | 真record右到4,1，tailup.8/left.2，behavior .75/.25 nextleft；SARSA .14/Expected .545/Qlearn .68，from .3 lr.5 new .22/.4225/.49，目标不同非同真值矛盾。 |
| EX04 L674-682「两后继改最优参数」 | s奖1/gamma.5 nextu/v各半，V(s)=theta/u0/v2theta；样本delta1-theta/1，平方均值min2 vs平方均min1，差theta²/4。独立task/range仅s residual，真预测随机性带参数var机制齐。 |
| EX05 L1348-1357「同经验AC两更新」 | grid初合法right/up，V .2/.5/theta0，真right到2,1 reward-.04 delta .21；critic lr.1到.221，actor lr.2 score.5 theta.021 p~.50525，两参数估值/概率不同输出。 |
| EX06 L1742-1753「Dyna不返上游」 | old上游right记录allQ0，new末up成功lr1 Q1；model采oldrecord目标.86 lr.5 Q.43，同replay可算。真P备份若otherQ0仅.68，未recordslips不因多plan解决，范围单样本非随机精解。 |
| EX07 L1977-1982「乐观错误」 | 安全真/hat .6，rare捷径真succ .1吸收失败0/modelsucc .9；test99%safe MAE.008但chosenloss .5。search更多可稳定选假最大，教学real/hat/data权完整。 |
| EX08 L2115-2125「两步model gradient」 | detscalar xnext=ax+bu、uθx/x0=1/terminalC x2²/2，q=a+bθ，Dx2=2bq/Cθ=2bq³；a=b1θ-.5 gives .25/lr.1 θ'-.525。漏第二次pi读x缺一半仅该例，不泛化。 |
| EX09 L2485-2495「持续时间不能忽略」 | room4,2→6,2 A2/B4步，allr-.04不触最终目标/tail.8；正确.572/.38732，wronggammaonce .644/.58244高估；randomK jointE不换gamma^EK EV。 |
| EX10 L3200-3207「最好checkpoint偏差」 | trueboth .6 independent±.1，fixedlastE .6，maxmeasurement .5 prob.25/.7 .75 →.65；truechosen .6，报告+.05仅selectionnoise。不是本文实训练结果。 |

另有未用example环境的教学反例/手算（UCB快照、noisy-TV、Double-Q、Baird、回报分布、模型预测非法均值、PPO裁剪、SAC、MVE/MPC、MuZero、模型梯度单步偏差、房间层级、技能区域、组合锁、归一化）均在W各定位记录，公式和图special再索引，不能以这十正式例的数量宣告全部算例仅十个。

## 算法全步骤A01-A04

步骤ID按源命令行稳定编号；`For/If/End`是控制流，不伪装自然句，但其条件/闭合也检查。`Require/Ensure`纳输入输出。算法标题语义在相邻正文已解释，没有冻结标题修订要求。

| ID、源行短引 | 白话、依赖与判断 |
|---|---|
| A01-IN L819「网络/空回放/B/C/更新频率/合法动作」 | 输入涵模型变量、批/同步/调度及动作接口；预热数量在更新条件实际使用，应按实现配置固定。算法为机制循环不是无需配置的可运行程序，正文L838特别要求C单位。 |
| A01-01 L820「bar theta=theta…起s」 | 初始目标网复制在线，取得真实起点，避免未定义目标分支。 |
| A01-02 L821「每个真环境步t」 | 外循环计真实交互，更新可0或多，不混gradientstep。 |
| A01-03 L822「epsilon贪心合法A(s)」 | 当前Q动作源，合法集合限制，探索取样未假转移model。 |
| A01-04 L823「执行…r,s',真z…入D」 | 真实后继/奖励/终止存buffer，模型样本不列为真实。 |
| A01-05 L824「预热数量且更新时刻」 | 条件允许buffer足量再抽B，调度在Require给频率。 |
| A01-06 L825「均匀B…停止导y」 | replayuniform empirical目标，延迟Q算tail max与真z遮，y冻结。 |
| A01-07 L826「批均Huber规定次梯度」 | 在线theta降loss，数据批平均除B，目标网不从loss导。 |
| A01-08 L827「EndIf」 | 学习块结束后同步计数独立运行，不将目标copy藏在预热条件。 |
| A01-09 L828「同步计数到C」 | C实际单位须正文固定，机制可按env/grad但不是未知混计。 |
| A01-10 L829「copy/restart count」 | 目标更新为显式复制非反向gradient路径。 |
| A01-11 L830「EndIf」 | copy条件闭合，非每真step自动都copy。 |
| A01-12 L831「真终或上限reset…否则s=s'」 | 数据记录和下一起点更新分开，time reset不改其任务终语义。 |
| A01-13 L832「仅截断z0…保reset前s'」 | 防误尾0及跨episode错s'，真终z1不重置为0。 |
| A01-14 L833「EndFor」 | 外环境循环控制流完整，非直到loss收敛的停止定理。 |
| A01-OUT L834「在线网及区分探索的评估策略」 | 交付网络和约定evalpolicy，epsilon训练不自动当贪心部署。 |
| A02-01 L1314「保存old/freeze旧pi和critic」 | 此轮采样/ratio与A目标绑定同版本，训练不会回改old。 |
| A02-02 L1315「旧pi片段…r/真终/截断/旧logp」 | 数据含判断bootstrap和ratio所需字段，batch时旧policy明确。 |
| A02-03 L1316「真终V0/非终边界旧V」 | 片段尾按任务真实终止，不将所有batch尾置0。 |
| A02-04 L1317「逆GAE…固定A/R=A+Vold」 | target固旧评价器，R用于value fit，明确生成过程不当前critic变后重算。 |
| A02-05 L1318「预定E轮小批优化」 | 计算重用固定旧data，不称新同policygradient；停止次数可复现。 |
| A02-06 L1319「声明batch权ratio/Clip」 | 权应按目标protocol已声明，q current/old同record动作。 |
| A02-07 L1320「actor上升/critic平方下降」 | 两目标/参数梯度方向不同，criticR停止求导，不串改A。 |
| A02-08 L1321「测KL…可选超阈提前停」 | 停是附加设计而非Clip硬约束，条件“若采用”保不同实现。 |
| A02-09 L1322「EndFor」 | 一轮优化结束或按规则stop，控制流闭合。 |
| A02-10 L1323「弃本轮旧依据…新pi真采」 | 重用仅本轮近端数据，下一轮old更新，非永久same旧batch无校。 |
| A03-01 L1528「策略/双Q/targetQ/温度/真D初始化」 | 双评论家及其bar、alpha变量均定义，真buffer不先装合成。 |
| A03-02 L1529「每真交互步」 | 外预算trueenvstep，内U重算不新增data。 |
| A03-03 L1530「当前pi采执行record…预热随机」 | executionpolicy明，预热另指定random；记录s/a/r/s'/z真结果。 |
| A03-04 L1531「入D/reset或转s'」 | 先留data后按resetcondition续state，time reset允许不同真终语义。 |
| A03-05 L1532「截断z0/reset前s'」 | 与DQN同正确bootstrap边界，不能跨episode取nextroot。 |
| A03-06 L1533「U次gradient」 | 训练复用次数显计，非1env=1update。 |
| A03-07 L1534「replaybatch…当前pi尾a'…sgy」 | tail当前actor采而barQ评价，整个softy冻结，真recorda用于critic。 |
| A03-08 L1535「两Q各降…不向target/a'反导」 | critic只w_j更新，actor/target分支不从LQ同时改。 |
| A03-09 L1536「同s重采a…固定Q参降Lpi」 | actor对生成动作密度/grad_aQ求导，非recorda imitation。 |
| A03-10 L1537「auto temp固定输出降Lalpha」 | 此step策略样本/logp不导，alpha expξ变化方向同正文熵条件。 |
| A03-11 L1538「barQ=(1-tau)bar+tauQ」 | 缓跟目标参数不同于DQN周期全copy，tau此同步步率需实际配置0..1，不混分位/轨迹tau。 |
| A03-12 L1539「内EndFor」 | U次更新后再一个真实步，时间单位不混。 |
| A03-13 L1540「外EndFor」 | 持续循环到设预算结束，机制循环非全algorithmconvergence证明。 |
| A04-01 L1730「探索Q在s_t真执行record」 | 真实经验五量(s,a,r,s',c)，c继续非z真终，字段符号与前model定义一致。 |
| A04-02 L1731「真实访Q用同式」 | 真样本先备份，免模型更新覆盖已得反馈。 |
| A04-03 L1732「后继/奖/c计数联合model」 | 随机网格保存joint outcomes而非lastsuccess deterministic，以保相关。 |
| A04-04 L1733「nplan次」 | 内循环为modelcompute预算，非真environmentsteps。 |
| A04-05 L1734「已见(s,a)指定规划分布」 | 当前表格model仅已有pair可采，不能隐查未record动作真P。 |
| A04-06 L1735「从当前经验model采joint」 | 模型版本/经验计数形成样本，不保证真P精确；joint reward/continuation/state依赖保。 |
| A04-07 L1736「同Q更新假pair」 | 同r+gamma c max target，但证据来源假；计算形式不改变样本信息独立性。 |
| A04-08 L1737「EndFor」 | nplan完整结束后再真环境推进，不并行改共享Q未知次序。 |
| A04-09 L1738「真终/time reset…截c1/真后继」 | 真终c0，采限reset仍c1保尾，状态续/重启与记录语义分开。 |

## 该文件范围结论

- 正式陈述9定义、14定理、10例子共33；正文完整proof 11，合计44正式单元。每单元含本地对象/条件/用途/边界并回连逐句依据。额外算法4个，共48个输入/操作/控制/输出步骤单元（A01 16、A02 10、A03 13、A04 9）；已按实际记录行机械核对，不由脚本生成语义判断。
- 此处算法只核正文伪代码输入输出/公式/控制流一致，不执行程序。原论文完整证明、数值运行与PDF未核；本角色未修正文、未构建、未暂存提交。
- 图31个已在SG补齐全部图内元素的63个功能部件记录；表40个、40表头与159表行见ST1-ST3；展示式147个与重要行内式见M1-M3。普通W涵盖相邻解释及图表注，特殊单元记录不以普通W代替。
- CH03-R2-01（有限Huber不保证精确分位）仍待修改。此文件完成正式单元记录不等正文通过。
