# CH03-R1 接管者W遍：L1583--1706

同一接管者人工W1--W6；新节、定义、公式、表体、图内标签全列。源图`rl-learning-regularized-search.tex`、`rl-learning-model-anatomy.tex`完整亲读，数值只作正文与源公式手算一致性核验，不称核实原论文/图版/算法执行。

|ID、位置短引|白话意思；专项依据或发现|
|---|---|
|RW-L1583-S01，“熵与参考KL”|entropy鼓多动作、KL限离参考pi，比较两正则约束哪项行为；1479/1277已有机制此处新共同局部目标，G2/G4接受。|
|RW-L1583-S02，“固定q合法分布”|给s固定动作q，在合法a概率simplex最大平均q减参考KL，把两者统一同优化对象；集合/方向/计算理由先于式，G3/G6/E9接受。|
|RW-L1583-S03，“给定q/pref/alpha”|评分、参考分布、正惩罚权参数本地设定；不与critic预测或已学policy误混，G6接受。|
|RW-L1588-S01，1588--1590，“支撑乘子求导”|只能在pref正支撑求p，归一sum p=1用lambda乘子，导一阶条件给指数更新；lambda是乘子非lambda-return混用角色即时述，G6接受。|
|RW-L1597-S01，“均匀/旧policy”|均匀ref时KL=logK-H回entropy，ref旧pi则一步镜像升；同目标两参考用途非所有算法等价，G2/G7接受。|
|RW-L1597-S02，“零支持不能重发现”|pref_a0而p_a>0产生无限KL，最优仍0无法新探该a；明确允许候选支撑/边界，不用低temp补信息，G1/G6接受。|
|RW-L1597-S03，“非数值温度问题”|支撑限制来自概率测度，不是减少alpha能解的浮点障碍；前无限KL机制支撑正向结论，G4接受。|
|RW-L1599-S01，“图上局部更新”|上排是fixeds动作分布正则改进，不是参数空间sample，G2接受。|
|RW-L1599-S02，“控制即推断”|用高奖励轨迹更大最优性事件概率再条件化行为，解释指数权视角；名称伴操作/概率对象，G3/G4接受。|
|RW-L1599-S03，“有限时域指数”|离散finiteH，opt变量条件概率∝exp(r/alpha)，给actionprior和真实kernel得轨迹后验指数回报重权；条件模型构造非历史事实已核，G1/G6接受。|
|RW-L1599-S04，“幸运转移”|精确posterior也偏好不可控好运后果，policy无法选随机核结果；概率后验与可执行控制对象区别具体，G2接受。|
|RW-L1599-S05，“固定核变分policy”|可执行近似需轨迹族保真实核只调pi并限推断范围；说明允许集合从执行能力来，G3/G6/E5/E9接受。|
|RW-L1599-S06，“不是全部精确后验”|构造可解释部分entropy/KL，不证所有policyalg同精确posterior解；范围限定有前幸运转移反例，不笼统排除算法，G1/G7接受，原来源未核。|
|RW-L1601-S01，“需评分或grad”|前动作正则需q或参数方向，承接黑盒搜索缺口；本地恢复所需信息而非机械另痛点，G5接受。|
|RW-L1601-S02，“不可微/整回报”|policy含不可微程序或仅整回合return可查询时，改试多组theta；从actiondistribution→parametercandidates的理由/输入能力明确，G3/E10接受。|
|RW-L1601-S03，“CEM精英拟合”|维护theta搜索分布，选高return部分候选精英，拟它们以改下轮范围；术语+预测/筛选对象+操作及时，G4接受。|
|RW-L1601-S04，1601--1602，“Gaussian第k轮”|theta_i从当前m/C高斯抽，按估return选非空E，未平滑更新样本MLE均值/协方差；允许候选从搜索分布来，elite方向是高回报，G6接受。|
|RW-L1612-S01，“最小协方差/平滑”|样本elite少可能Cov塌，mincov或平滑限制过早收缩；具体失效量与措施对象明，G1/G2接受。|
|RW-L1612-S02，1612--1613首句，“一维F候选”|人工F=-(theta-1)²，theta(-1,0,1,2)score(-4,-1,0,-1)，取top2并列小theta取(0,1)，MLE均.5 var.25；参数/排名/平局/估法都给，G1/G6接受。|
|RW-L1613-S03，“人工非实测”|candidate/score不是真实训练，数例只解释CEM动作，G1/W5接受，来源未核。|
|RW-L1622-S01，“ES扰动关系”|CEM筛选拟elite，ES可用theta扰动与return相关来估方向；两方法不同机制不混同高斯sample，G2/G4接受。|
|RW-L1622-S02，1622--1625，“Gaussian邻域平均”|先定义F_sigma为原J在Gaussian参数邻域的期望，要算其grad，不称原J同grad；新目标来源/为何可估不可微方向明，G3/G6/E11接受。|
|RW-L1630-S01，1630--1633，“成对扰动估量”|同epsilon方向正负theta score差/(2N sigma)乘epsilon平均，反对称降低常数成分；样本/方向/尺度/候选Gaussian前给，G6接受。|
|RW-L1635-S01，“平滑偏差”|ESgrad对应F_sigma，sigma改搜索距离及原J平滑偏，非随便改步长不影响目标；评价对象与范围明确，G2/G7接受。|
|RW-L1638-S01，“CMA-ES演化路径”|利用selection和跨轮路径改Cov/全局步长适方向scale，非CEM sampleCov同名；概览新记忆对象/更新职责具体，不冒完整推导，G2/G4接受。|
|RW-L1640-S01，“整段参数/每步动作”|theta扰动在整轨迹保持可能形成跨时一致，actionnoise每步改localaction；比较采样单位/相关方式具体，G2/E2接受。|
|RW-L1640-S02，“不免费长程”|每theta仍需足回合辨return，d维全Cov O(d²)存估、noise改排名；收益/代价具体且无免费保证，G1/G6接受。|
|RW-L1640-S03，“比较交互并行可微维度”|选择方法需总真实步、并行能力、policy导、paramdim等条件，不看式长度；可检验要求是算法资源/访问条件多轴，G1/E3接受。|
|RW-L1646-S01，“回放不答未记录后果”|重复旧经验不直接给未见a的后果，model使用需求就地；“直接”保value泛化/外推不被全否定，G5接受。|
|RW-L1646-S02，“拟可查询predictor”|经验拟后继/奖预测，可补valueupdate或当前a比较；从replay→预测model数据用途明确，G3/G4接受。|
|RW-L1646-S03，“Dyna/MPC两用”|Dyna模拟经验改Q，MPC预测candidate回报选计划只首a；不是用model必trainV，分类按执行比较接口，G2接受。|
|RW-L1646-S04，“MPC无独立V仍比较”|MPC不一定另学value，但动作由预计return比较，说明冻结节名职责不强加模型类；G1/G4接受。|
|RW-L1646-S05，“下节跨态策略”|model train sharedparampi下节，部署直接pi区别当前每步plan；仅预告不用后结论撑当下，G2/G7接受。|
|RW-L1652-S01，“3,2右的落点”|基准向右.8到4,2、上下滑各.1到3,3/3,1，三个合法state与概率和1；例输入明确，G1/G5接受。|
|RW-L1652-S02，“均值3.8,2不存在”|coordinate平方loss最佳条件mean=(3.8,2)，不是离散格合法s；目标统计值/控制状态域冲突可手算，G2/G6接受。|
|RW-L1652-S03，“不能代合法V”|mean位置不保滑移多个结果且V只格点无此输入，无法直接planningexpectedV；具体后果由原域给，不仅称预测不好，G2/E2接受。|
|RW-L1652-S04，“统计正确控制不适”|loss估对conditionalmean仍非所需控制对象，强调model目标选型而非算法失效普断，G1/E6接受。|
|RW-L1656-S01，“det/random输出”|det给后继s_hat，random给条件核P_hat，比较保单结果还是分布；动机mean非法已1652本地，G4接受。|
|RW-L1656-S02，“Bayes/ensemble”|Bayes在parameter/function上后验再积分预测，ensemble保重采/初始化多拟合predictors；对象层次与形成多个model理由明确，G2/G3/E5接受。|
|RW-L1658-S01，“动力/奖/继续”|P预测落点、R即时奖均值、c_hat预测转移可继续概率，是三output职责；新标记在definition明确类型不等discount，G4接受。|
|RW-L1658-S02，“联合(s',r,c)”|可learnjoint保奖/后继/continuation相关，不仅三独立头；允许对象扩大/原因明，G3/G7/E10接受。|
|RW-L1661-S01，“从记录非直接return”|model预测loss拟真实observed后果，不等policy控制return目标；统一训练/使用目标不同，G2接受。|
|RW-L1661-S02，“c0真终/c1继续”|继续label相对先前z终止翻转，在本地明确新记号角色/范围；G4接受。|
|RW-L1661-S03，“三NLL真实D/候选phi”|随机后继/条件奖/继续model从真实记录最小三项NLL，数据expectation/paramvariable先给；family输出前1656形成，G6/E11接受。|
|RW-L1669-S01，“训练三监督”|每真实记录s'/r/c进对应NLL更新phi，经验数据到参数动作具体；不只“用MLE”名词，G4/G6接受。|
|RW-L1669-S02，“使用抽后继奖继续”|planninggive sa先抽preds'再r/c，continue则从s'再展开否则停；可查询input→output→rollout步骤明确，G2接受。|
|RW-L1669-S03，“预计候选return”|predictedtrajectory供candidatea回报比较，是model用于control的接口；不等实际真实return证明，G1接受。|
|RW-L1669-S04，“predictionloss/strategygoal”|modelloss评价record预测，policy评价用预测选行动后的回报，两评价对象不可互代；G2/E2接受。|
|RW-L1671-S01，“joint依赖需明”|生成joint后果须指定各预测条件关系，承接1669采样的数据依赖缺口；G5接受。|
|RW-L1671-S02，“条件独立或联合”|三项分布乘隐含r/c给sa/s'独立，不成立需joint或c再条件r；损失作为compositefit可用但joint模拟假设就地先于使用保证补足，G1/G6接受。|
|RW-L1671-S03，“期望奖足/风险要joint”|只expectedBellman rewardmean足，风险/联合事件要full distribution相关；原期望target→风险newtarget新增信息需求明确，G3/G7/E10接受。|
|RW-L1671-S04，“tasklabel别采集截止”|采集时限c不能标0，否则学虚假termination；模型output/数据label/控制后果有因果具体链，G1/E3接受。|
|RW-L1673-S01，“图像潜态”|观测图像可先编码z再预测latentnext，明确从explicitstate到internalrep路线；G3/G4接受。|
|RW-L1673-S02，“图表部件”|图分编码/转移/任务头/重建，表比较explicit/worldmodels/planet实际接口；接受。|
|RW-L1673-S03，“同训用换表示”|latent仍记录预测/模型rollout，只把stateinput换rep且可加reconstructiontrainencoder；可继承目标/新增部件具体，G7/E10接受。|
|RW-L1675-S01，“保控制信息”|换rep需保判断a后果所需状态，非训练pixelloss低自动充分；承载encoder/criteria1661输出、前918反例具体，G1/E3接受。|
|RW-L1675-S02，“单帧看不出速度”|oneframe不能观speed需history，重建再准不创造未观运动信息；新obs条件/具体反例先给，G5/E8接受。|
|RW-L1675-S03，“RSSM历史后章”|recursive模型历史infer暂预告，不能借后章满足当前latentstate充分；当前只model使用givenrep，G7接受。|
|RW-L1675-S04，“给定表示/另析充分”|明确本节研究givenrep预测用法，history充分非此处已证明；声明范围清楚不据目录断言已完，G1/G7接受。|
|RW-L1701-S01，“World Models组合”|视觉压缩/递归预测/小controller组合，前1692表机制支撑概览名；历史来源未外核。|
|RW-L1702-S01，“PlaNet在线plan”|latentmodel直接onlineplanning，与WorldModelscontrollertrain部署成本/目标不同；表1692/1693给实际接口差非泛“更先进”，G2接受。|
|RW-L1704-S01，“评价三件事”|要分modeltest各评价对象，非所有loss同质，后句具体列，G2接受。|
|RW-L1704-S02，“一步/闭环/校准”|one-step在testD局部预测，multisteppolicy随predstate行动偏离，confidencecoverage校准；数据域/操作/指标目标分别明确，G2/E1/E2接受。|
|RW-L1704-S03，“门口错可低avg”|稍错非关键坐标可能无碍，avg更低但门前预测跨墙改变greedya；条件反例说明平均coordinate误差不保controlquality，G2/E6/E12接受。|
|RW-L1704-S04，“连续房间边界”|改continuous房间，小distance跨collisionboundary后果不同，不能按pixelavg；扩grid→continuouscollision本地声明/用途是边界敏感，G3/G7/E10接受。|
|RW-L1706-S01，“ensemble一致错”|disagreementlocate候选未一致区域，但共有data/feature/inductivebias可全错仍一致；多个candidate形成来自1656，反例内容具体，G1/E5接受。|
|RW-L1706-S02，“需统计校准”|ensemblevar要额外假设和coverage过程才置信radius，不因allagree就真核；概率输出/参数候选不确定不同且接受依据明，G1/G4/E3接受。|

## 特殊单元

|ID、位置|白话与判断依据|
|---|---|
|RX-L1584，1584--1587|缺fixeds同时用q/参考行为约束的局部pi，allowp合法simplex、pref给、alpha正，平均q减KL求大；prefzeros限定positive support1588/1597，不虚构可探索零候选，接受G6。|
|RX-L1589，1589|在pref>0支撑对sum p=1 Lagrangian导，q-alpha(logratio+1)-lambda=0，解logratio线性q；乘子lambda区别returnlambda本地，接受。|
|RX-L1591，1591--1596|pref*exp(q/alpha)再归一是局部正则精解，uniformref回softmax，oldpi为mirrorstep；不是任意futureJ单调保证，1597zero支持边界明，接受。|
|RX-L1603，1603--1611|缺CEM改paramsearchdistribution，Gaussian候选score最高E，非空elite均值和MLEcov除|E|，新mean用于cov而非旧mean；平局与正cov退化例后补实现选择，接受G6。|
|RX-L1613，1613，教学F/精英|F=-(theta-1)²在-1/0/1/2分-4/-1/0/-1，top2tie按小theta是0/1，mean.5/cov.25；非unbiased样本variance除n-1，明确MLE，接受。|
|RX-L1623，1623--1625|缺不可微policy参数优化方向，F_sigma=Gaussian邻域EJ(theta+sigmaepsilon)，新目标平滑而非原J；sigma作为搜索尺度、对theta参数neighbor分布清楚，接受G6/E11。|
|RX-L1626，1626--1629|Gaussian平移分布对均值导为epsilon/sigma，积分Jgrad density得F_sigma grad，满足相应可积导条件；不要求J自身可微，前1601黑盒任务解释为何选scoregradient，接受。|
|RX-L1631，1631--1633|N对对称noise，正负Jhat差除2N sigma乘epsilon，期望给平滑grad；噪回报需评估充分1640明，不声称finite exact，接受。|
|RX-L1662，1662--1668|缺s'/r/c预测模型拟合量，真实D记录、phi候选前给，三条件NLL最小；sum作为各条件fit，若当jointprob乘需r/c给sa/s'独立1671，不能自动保相关风险事件；接受G6。|
|RT-L1689，“表示/拟合/接口”|比较explicit及latent实例保哪种变量/部署怎样用，不是“有model即每步plan”，接受。|
|RT-L1691，“显式”|位置速度state已定义，fitnextdist/reward可知另学，next合法送V，coordloss需scale/后果解释；1652非法mean例支持，接受。|
|RT-L1692，“World Models”|VAE观测压缩+mixture密度递归预测latent，controller读rep/记忆、可EStrain；组件名为概览各作用白话同给，不拿隐藏历史机制作本节充分性前提，接受。|
|RT-L1693，“PlaNet”|RSSM deterministicrecursive+randomlatent，fitobs/r/multistep，latent动作序列plan执行首；stateinference/rolloutquality条件明，详细历史推断另章非声称已证，接受。|
|RC-L1680-S01，“预测职责”|modeloutputs分辨不同下游所需，不只图有训练网络就classification，接受。|
|RC-L1680-S02，“explicit/latent”|上直接state、下rep，reconstruct/reward/continue不同头，需要按用途选；正文1658/1673先建对象，接受。|
|RC-L1680-S03，“虚重建非经验”|虚线编码→decode可选辅助重建，不是虚拟转移写replay，图关系类型明，接受。|
|RC-L1696-S01，“显式潜在区别”|输入/内部状态类型与任务控制接口不同，接受。|
|RC-L1696-S02，“三层不确定”|randomlatent是结果/隐state随机，parameterposterior是未知dynamics，ensemble是多fit，不直接互换置信；1656/1693对象具体，G2/E2接受。|
|RC-L1618-S01，“两搜索分布”|统一主题但actionspacevsparameterspace不同随机变量，接受。|
|RC-L1618-S02，“上下职责/不混概率”|upperfixeds行动作reg，lowerparamelitefit，动作prob和theta samplingprob不同集合；源图各明确，G3接受。|
|RF-search-L05，“fixeds动作改进”|上主题只有该s的a概率，不是训练全paramdistribution，接受。|
|RF-search-L06，“pref(a|s)”|参考动作分布给KLbaseline，与oldpi可选定义一致，接受。|
|RF-search-L08，“Eq-alpha KL”|局部score平均减参考KL，优化方向升1583，接受。|
|RF-search-L10，“new ∝pref exp”|归一解1593，zero support不造新a，接受。|
|RF-search-L11--12，“ref→objective→new”|参考集合与q确定局部目标，再求新动作分布，非真实环境交互箭头，接受。|
|RF-search-L13，“paramCEM人工”|lower是theta参数候选且指定教学数，接受。|
|RF-search-L15-S01，“-1/0/1/2候选”|人工candidate参数而非四合法环境动作，接受。|
|RF-search-L15-S02，“-4/-1/0/-1分”|一维F评分对应四theta，G6接受。|
|RF-search-L17-S01，“两elite/0,1”|top2按回报大且tie小theta，E此处列参数值而算法式E列候选索引，例明确“精英(0,1)”可对成员，非把index0强引算法数组，接受。|
|RF-search-L17-S02，“并列小参数”|tie -1对应theta0/2选0，使例可复算，接受。|
|RF-search-L19，“nextsearchm.5C.25”|GaussianMLE两elite均与variance，非targetpolicy a概率，接受。|
|RF-search-L20--21，“candidate到elite到fit”|筛选后拟searchdistribution，不宣称随机environment model拟合，接受。|
|RF-search-L22--23，“下轮param重采整return”|newdistribution再取theta评整个轨迹，明确真实交互代价而非单步reward，接受。|
|RF-anatomy-L05，“explicitstate”|上输入是state可见，接受。|
|RF-anatomy-L06，“state/a s_t a_t”|modelconditionalinput来自真实可见状态动作，接受。|
|RF-anatomy-L07，“conditional P_hatphi”|randomdynamics输出conditionalnextlaw，非真实knownkernel，接受。|
|RF-anatomy-L08，“nextdistribution/s_hat”|节点标题说后继分布，s_hat为其预测/抽出的后继记号；1656 P分布与1669抽后继机制明确，不能将node仅s_hat误读detmean替完整law，接受，PDF视读未核。|
|RF-anatomy-L09，“r_hat/c_hat”|rewardmean/continuationprob不同输出职责，1658明确类型，接受。|
|RF-anatomy-L10--11，“sa→P→next”|预测后继先conditiongiven sa，不表示真实环境被控制，接受。|
|RF-anatomy-L12，“sa到reward/c”|图为taskhead职责简化输入，也可jointconditiononnext正文1671明确；不用于声明r/c与s'独立，接受。|
|RF-anatomy-L13，“latent可historyinfer”|下是给定latentstate先来源于obs/history，notassertsingleimagealwaysMarkov，接受。|
|RF-anatomy-L14，“obs或history/a past”|o≤t/a<t是inferstate信息，而当前a_t另供转移，时间索引对，接受。|
|RF-anatomy-L15，“encode/infer z_t”|形成内部state，缺velocity需history1675说明，接受。|
|RF-anatomy-L16，“z_t/a_t→z_t+1”|latentmodel按当前action预测后latent，控制条件信息不丢，接受。|
|RF-anatomy-L17，“reward/c taskhead”|latentfuture/taskprediction不同于decodeobs，接受。|
|RF-anatomy-L18，“decode o_hat_t”|从currentlatent重建currentobs，不冒forecastnextpixel，接受。|
|RF-anatomy-L19，“obs→infer”|编码或历史推断，给模型latentinput，接受。|
|RF-anatomy-L20，“infer→transition a_t”|currentstate与新action为预测输入，a_tlabel不是historya<t，接受。|
|RF-anatomy-L21，“transition→taskheads”|潜在演化供r/c预测，任务头不等value/actor，接受。|
|RF-anatomy-L22，“虚decode支路”|optionalreconstructtrainrep而非强制规划时pixeldecode，接受。|
|RF-anatomy-L24-S01，“重建保信息”|重建loss约束表示留obs信息，不保证控制充分，后半立即补，接受。|
|RF-anatomy-L24-S02，“动作预测/充分”|control还需state包含动作后果所需变量及actionconditionaldynamics，1675速度反例具体支持，G1/E3接受。|

## 局部入口、方法链与范围

- RI-1583：已有entropy/参考KL→fixeds合法概率选择→平均q减KL目标→归一乘子求解→指数参考重权→zero support限制；运算从可行动作simplex来，非任意模型最坏集合。
- RI-1599：指数权与opt事件条件化→有限轨迹posterior→随机核幸运偏好不可控→执行轨迹族固定真实kernel仅optimizepi，限定近似范围。未借专业推断称全部algorithm等精后验。
- RI/RM-1601/1622：需要q/grad但policy不可微或整return→参数候选Gaussiansearch→elite高score筛→MLEmean/cov→noise/高维交互代价；ES另定义Gaussian邻域J平滑目标→paramscoregradient→成对估计→sigma平滑偏差。无需模型predict/residual监督目标，非适用链说明而非硬添risk。
- RI/RM-1646/1652/1661：未记录a后果→model可查询预测→Dyna模拟改Q/MPC当前plan两接口→平均格点不存在反例→det/random/parameterposterior/ensemble对象分→真实record三NLLfit→给sa抽next/r/c→continue或停形成rollout→candidate预计return。模型predictionloss非policyJ，jointsample依赖1671单列。
- RS-1671：只期望return需rewardmean→risk/joint事件需full相关；真tasktermination→collectioncut不可标c0。RS-1673/1675：explicitstate→latentobs/history，速度单帧不可知不能继承完整Markovstate，模型给定rep使用与history充分性分工明。
- RD-1704/1706：localpredictionloss、closedloop偏离、confidencecoverage三对象不同；ensembleagreement只成员意见，不等校准置信。E1/E2/E3/E5/E6/E9/E10/E11/E12有本地对象/例/条件依据。无本块新必改发现。
