# CH03-R1 接管者W遍：L2215--2337

人工逐句W1--W6、公式、表体、图注及MBPO图源。身份/冻结版本见resume；Dreamer正式版和MBPO论文的归因与实验数字仅检查正文证据边界，未外部核源。所有接受均指当前位置解释及可本地复算内容。

|ID、位置短引|白话意思；依据或发现|
|---|---|
|RW-L2215-S01，“奖励尺度”|跨任务rewardscale影响目标拟合，局部恢复新增表示问题，G5接受。|
|RW-L2215-S02，“正式版离散概率”|限定2025Nature版本，reward/valuehead改固定支撑概率而非标量，改变输出对象明，G3/E10接受，未核源。|
|RW-L2215-S03，2215--2217，“symexp支撑”|b_i由等距u_i经sign(u)(expabsu-1)，范围[-20,20]明确，建立输出值集合，G6接受。|
|RW-L2217-S04，2217--2219，“two-hot插值”|y落邻b间用距离分两prob、越界clip，合法非负和1且均值y；允许集合/评价对象明，G6/E9接受。|
|RW-L2219-S05，“CE与均值”|预测distribution用twohot CE训，输出sum p_i b_i为原值均值，数据→loss→output完整，G6接受。|
|RW-L2219-S06，“原域非symlog平均”|变支撑的位置不等改变均值算法，非线性反变换与求mean不交换；具体公式前给不依赖猜旧版本，G2/G7接受。|
|RW-L2221-S01，“距离不是最近点”|twohot保邻间位置相对于nearestonehot，新增任务是说明softlabel区别不是重定义，G4/E6接受。|
|RW-L2221-S02，“T与critic拟合”|T编码停止梯度G为softtarget，criticparams最小CE；目标来源/方向即时给，G6/E11接受。|
|RW-L2227-S01，“软目标CE”|sum T logp不是只单点loglikelihood，前T非onehot概率定义支持，G2接受。|
|RW-L2227-S02，“EMA正则/真实辅助.3”|EMA另作regularizer、realreplay辅助value权.3，real标签来自correspondingimaginedroot在策略return；用途/数据源明，未称真reward独立标签，G6接受，未核配置来源。|
|RW-L2227-S03，“不是统一targetnet”|EMAregularizer不等所有bootvalue替EMA，比较对象/位置具体，G2接受。|
|RW-L2227-S04，“currentcritic/sgtarget”|G回报用currentv但监督branch sg，只更新拟合方；两梯度操作不同，G6/G7接受。|
|RW-L2229-S01，“V3归一REINFORCE”|adv=G-v，discrete/continuous均likelihoodratio而非pathdynamicsgrad，版本/作用明，G3/G6接受。|
|RW-L2229-S02，2229--2230，“W/S最大目标”|W cumulativeeffectivegamma，S percent95-5EMA调scale，采样actor最大目标；本地指标/方向/量定义明，G6/E11接受。|
|RW-L2241-S01，“量固定熵鼓励”|states/W/adv在actorupdate固定，梯度只logpi和entropy，正eta增随机性；公式分工明确，G1/G6接受。|
|RW-L2241-S02，“有限片段代理非真J”|replayroots有限imaginedseq训练非无校正trueinitialJ精确梯度，sum不能假冒normalizedoccupancyexpectation；原/新distribution和归一范围明，G7/E10接受。|
|RW-L2243-S01，“5/10种子”|论文所述基准trainseed多数5、Minecraft/BSuite10，单位/分组清楚；未外部核源，不将数字当独立验证。|
|RW-L2243-S02，“abstractcommands/加速”|Minecraftinterface含抽象合成/快速破坏，任务协议影响成功指标可比性，G1/E3接受，来源未核。|
|RW-L2243-S03，“钻石非单一单位”|同成功名不同接口/预算不直接compare，要协议一起解读；具体改变条件前句给，G2/E1接受。|
|RW-L2245-S01，“train/deploy表”|当前已解析分工，现在比较计算位置/成本而非新算法保证，G2接受。|
|RW-L2245-S02，“posterior输入非充分证明”|history压缩latent用于算法，是否decisionstate充分不在此证明；明确范围保留后章而非借后章过当前位置机制，G1/G7接受。|
|RW-L2268-S01，“错state污染后续”|longimagined modelnext误差可影响future r和policyinput，直接提出短roll缺口，G5接受。|
|RW-L2268-S02，“MBPO真实根短buffer+SAC”|realreplayroot→几步modelseq→独立syntheticbuffer→混trainSAC，输出训练显式policy；数据flow完整，G6接受。|
|RW-L2268-S03，“不反导动力学”|用合成samples做SAC不是将actor梯度沿生成轨迹反传，区别Dreamerpathmethod具体，G2接受。|
|RW-L2268-S04，“Dyna/MVE不同目标”|Dyna备份Q，MBPO显式actor，MVE只合kstepvalue目标，生成转移同不代表更新对象同；前机制准确回接，G2/G7接受。|
|RW-L2270-S01，“buffer/F/B/k”|two buffers分别真/合成；F真env步拟model，B真根每轮k上限，配置时点/计量明，G6接受。|
|RW-L2270-S02，“eta_real比例”|batch真比例eta_real，其余合成，非把model数据都计入truebudget，G1/G6接受。|
|RW-L2270-S03，“旧model/policy占比”|F/k/B/mix/lifetime影响样本版本，应配置留证；承载对象参数列表具体，G1/E3接受。|
|RW-L2270-S04，“两来源图”|图追根与buffer到train不同流，符合正文目的，接受。|
|RW-L2279-S01，2279--2280，“合成一转移”|真根(3,1)、actor上、ensemble抽next(3,2)/r-.04/continue1、存version；一次操作全过程足够重建，G6接受。|
|RW-L2280-S02，“可能发生非执行”|合法基准可能next不等本次真观测，抽prob来自model，G1/G7接受。|
|RW-L2280-S03，“softtarget.41”|设targetsoftv .5则r+.9v=.41，人工criticvalue不是声称真实Q最优，G6/E12接受。|
|RW-L2280-S04，2280--2281，“actor混状态目标”|SAC actor在mixedstate对pi抽a最小alpha logpi-minQ，前SAC已建target和entropy；输入/允许param/方向明，G6/G7接受。|
|RW-L2282-S01，“真根不保真后继”|root真实性不能向modelnext继承，信息来源判据具体，G1/G7接受。|
|RW-L2284-S01，“shortroll依末值”|k小减少转移连用但prefix少需Vtail，取舍与kstep目标前建立，G2/G5接受。|
|RW-L2284-S02，“同root同pi”|量化先固定nu和pi，true/model kstepbootstrap两score，不悄换policy或初分布，G3/G6接受。|
|RW-L2284-S03，“q_j/TV与r误”|q_j^pi为真实深度sa分布，eP为kernelTV、eRmeanabsdiff，指标明确，G6/E11接受。|
|RW-L2289-S01，2289--2293，“每深度假设”|各j<k真occupancy上ePmean<=eps_m/eRmean<=eps_r，两Rbound、同V sup<=Vmax；条件与量词明确非只训练avgMSE，G1/G6接受。|
|RW-L2293-S02，“TV<=j eps_m”|samepi/root，kernel非扩张使每步加当深度真实ePmean，递推D_j<=j eps_m，G6接受。|
|RW-L2293-S03，“score差至多B”|r项真实处误差+stateD加tailstateD，B_k正控制absolute scoregap非policy improvement，G1/G6接受。|
|RW-L2301-S01，“r误两部分/末同理”|加减真实occupancy下hatR，eps_r+2RmaxTVd，再tail2VmaxTVd，推导常数依据明，G6接受。|
|RW-L2301-S02，2301--2303，“真无限多gamma^k epsV”|sameV与trueVpi uniform差epsV时额外尾error，固定pi的真正return对象需新条件，G3/G7/E10接受。|
|RW-L2303-S03，“k小非总好”|k缩小modelaccum小但gamma^k epsV衰减少，因此tradeoff非单调，指标/两误差具体，G2/E12接受。|
|RW-L2305-S01，“目标均误非行为验证”|bound需要q_j^pi，实际validation多q_j^mu，distribution不同不能借均误，G3/G7接受。|
|RW-L2305-S02，“新策略少见处”|转域需coverage/ratio约束，恢复要测哪一改变/问题，G5/E10接受。|
|RW-L2305-S03，2305--2306，“ratio<=C_j”|pointwiseqpi<=Cqmu让nonnegativee mean<=Cbehavior mean；允许域/条件/放大指标具体，G6/E9接受。|
|RW-L2306-S04，“MSE不等TV/C”|reward或predictionMSE小不直接给TVmodelbound也不给coverage ratio；指标/分布对象区别具体，G2/G7/E1接受。|
|RW-L2306-S05，2306--2308，“policyTV耦合”|改用uniformstate TVpi/mu<=epspi，同root逐步failureprob累深度，轨迹分布偏离线性；集合全s、比较norm明，G6/G7接受。|
|RW-L2308-S06，“抽象下界非SAC单调”|MBPO原分析结合behavior-modelTV和policychange，需要abstractconditions，不直接证明ensemble+SAC实际每步improve；G1/G7接受，来源未核。|
|RW-L2310-S01，“全候选/两侧误差”|B对allcandidatepolicy同时、末V目标误受控，代理新-旧超过各总误差才保真gain；data-dependentselect升级需uniform，G1/G7/E10接受。|
|RW-L2310-S02，“仅旧pi不足”|oldbehaviormean无法保证selectednewpi，同域扩大条件前句提供；具体反推限制，G1/G7接受。|
|RW-L2310-S03，“设计限制表”|分别列各作用与未证明对象，不混设计减误和全性能保证，G2接受。|
|RW-L2334-S01，“actor也可利用model误”|no-deploysearch仍modelgradient趋falsehighregion，给本地反例要核并非抽象否定节首，G5接受。|
|RW-L2334-S02，2334--2335，“一步a/r/hatR”|independenta[-1,1] realR=-a² modelR=-a²+.8a，一步任务无需继承网格，G3/G6接受。|
|RW-L2335-S03，“data0/grad.8”|data仅a0预测准、theta0确定policy，dhatR/da=.8，G6接受。|
|RW-L2335-S04，“opt.4/真-.16”|hatR concave最高合法a.4，hat=.16 true=-.16，oldtrue0，新真实更差.16，候选/方向/基准可算，G6/E9/E12接受。|
|RW-L2335-S05，“无longerror已失败”|counterexample单步说明manymodelpolicyupdates可能降低trueJ，不声称always；root fit正与域外error原因已给，G1接受。|
|RW-L2337-S01，“旧0新.4”|oldpi只a0评准确但selectnew.4未经data，恢复固定→选择域差异，G7接受。|
|RW-L2337-S02，“扩大误控或置信集合”|候选到达域需同步bound或handledata-dependentsel confidence；缺口/新增条件本地明，不默认ensemble分歧校准，G3/G7/E5/E10接受。|
|RW-L2337-S03，“统一模拟界非单点”|前节globalcandidateevent可给chosenreturn界，singlefit无；回指恢复所需命题/量词，G7接受。|
|RW-L2337-S04，“反馈图/处置表”|新pi改变visitdistribution须truevalidation，各措施位置/代价下块核，G1接受。|

## 特殊单元

|ID、位置|计算目的、对象、方向与依据|
|---|---|
|RX-L2216，2216--2219|缺跨rewardscale可训输出，b_i=sign(u_i)(eabsui-1)、u_i等距固定域，two邻prob和1/mean=y，CE最小拟label，再sum p_i b_i；不是symlogmean反变换，接受G6。|
|RX-L2223，2222--2226|缺critic对imaginedG拟合，sgG twohot label配latentx上的p_w，-sumTi logpi最小；predmodelr/c与currentv产生G，targetsg不更生成方，接受G6。|
|RX-L2232，2231--2240|缺V3actorupdate，W累存活discount权、sg((G-v)/max1S)缩adv、正熵eta鼓励explore；same sampledstate固定对logpi求梯度，max1是scale下限非candidateargmax，接受G6。|
|RT-L2252，2252|阶段/model调用/成本三个实际资源维度，接受。|
|RT-L2254，2254|realencoder/post/heads训练phi，真实samples/seqL/backpropmemory明，接受。|
|RT-L2255，2255|multipleposteriorroots先验roll与actor/r/c/v，modeltrans与update计数而非newrealbudget，须realtest，接受G1/E3。|
|RT-L2256，2256|deploymemory/post仍modelcost，采样还是确定动作须固定协议避免compareconfound，接受。|
|RT-L2257，2257|newrealbuffer交替model/actor/critic，permission/time/state重算需配置，不能默认offline可再交互，接受G1。|
|RC-L2260-S01，“位置改变非消失”|上述train/deploy部件明示计算重分配，接受。|
|RC-L2260-S02，“无搜索非无状态”|memory/posterior来自新obs仍必须保state，既有RSSM机制支持，接受G2。|
|RC-L2275-S01，“短分支”|图范围kstep合成trainingdata，接受。|
|RC-L2275-S02，“real根/model后/混SAC”|全部数据来源/输出连通，不冒合成真实，接受。|
|RC-L2275-S03，“actor不沿model反导”|SAC优化只Q/pi，phi监督只real，区别modelgradient明确，接受G2。|
|RF-mbpo-L06，“realbuffer”|存真实数据，既model监督又混SAC输入，接受。|
|RF-mbpo-L07，“ensemble/F”|F计realsteps更model，非k或SACupdatestep，接受。|
|RF-mbpo-L08，“realroot”|root distribution回放不必currentinitialrho，正文2270及2241scope已限定，接受。|
|RF-mbpo-L09，“currentpi/k”|modelroll当前policy最多k，遇terminal截断，接受。|
|RF-mbpo-L10，“syntheticbuffer”|独立recordmodel-generatedtransversion，接受。|
|RF-mbpo-L11，“SAC两模块”|mixedtrain critic与actor显式policy改，接受。|
|RF-mbpo-L12--16，“real→fit/root、root/model→roll→buffer”|真data拟phi，root和model共给syntheticseq，不拿generateddata拟真supervision，接受。|
|RF-mbpo-L17，“1-eta_real”|syntheticbatch权，与realweight互补，接受。|
|RF-mbpo-L18--19，“realbatch eta”|realdata到SAC独立流按eta计，不将modelsamples放大realbudget，接受。|
|RF-mbpo-L20--21，“更新pi回roll”|actornewpolicy改变下一批modelseq，旧buffer滞留配置2270说明，接受。|
|RF-mbpo-L22--24-S01，“model经验分别计”|root后allmodel/真合成数分计，接受G1。|
|RF-mbpo-L22--24-S02，“不用自己为真监督”|phi只real supervision，模型生成不新增environment证据，接受。|
|RX-L2281，2280--2281|缺synthetictrans如何改变actor，criticr+.9softV=.41，actor混states最小alpha logpi-minQ，行动者a~pi沿SAC既有机制，不沿生成dynamics，接受G6。|
|RX-L2286，2285--2288|缺ksteptrue/modelerror口径，eP TV rowprob、eR rewardmeanabsdiff，评价方向低好，trueq_j^pi明确；与前L1常数不同本地切换，接受G6/G7。|
|RX-L2295，2294--2300|缺samepi kstepbootstrap absolutegap，eachj prefixerror epsr+2Rmax j epsm+tail2gamma^kVmaxk epsm；从trueq均误到distributionTV递推，rewardhat sup及tailV sup用于2TV界，接受G6。|
|RX-L2302，2301--2303|kstep自举→trueinfinite目标需V/Vpi sup误epsV，尾补gamma^k epsV而非无条件视bootstrap真实，接受G6/G7。|
|RX-L2306，2305--2306|缺qpi均error从qmu转域条件，ratio domination C_j让nonnegativeavg最多C倍，允许sa同stateactiondomain，coveragezero时需qpi也0，接受G6/E9。|
|RX-L2307，2306--2308|另条件sup_s TV(pi,mu)<=epspi控同根depthtrajectory偏离，worststate非仅avg访问策略差以保每步couple；理由是newpi可能远离data，接受G6/E9。|
|RT-L2317，2317|设计/直接作用/未保条件，区分机制与证书，接受。|
|RT-L2319，2319|realroot免长synthetichistory起步，但oldpolicyroot及后继覆盖仍错，接受。|
|RT-L2320，2320|smallk减连误而tailV更重要，不能证明kopt，接受G1/E12。|
|RT-L2321，2321|增eta减syntheticweight，不能创造unvisitedrealactions，接受。|
|RT-L2322，2322|disagreement排成员不同，但sharedbias仍有，无校准TV含义；不把经验筛选当confset，接受G1/E5。|
|RT-L2323，2323|lifetime降oldmodelrecords权，不免currentsystematicbias，接受。|
|RC-L2326-S01，“控制与边界”|各control量效果可判，不超表列具体作用，接受。|
|RC-L2326-S02，“设计非全局证明”|需要验证reduceerror措施，不称safety或allperformance theorem，接受G1。|
|RX-L2335，2334--2335|缺modelgradient是否可害trueJ，合法a[-1,1] maximize-.a²+.8a选.4，true=-.16<old0，pred=.16与truegain反向，数可复算且trainingonlya0，接受G6/E9/E12。|

## 关键链

- RM-2215--2241：跨rewardscale→固定支撑distribution/twohot softlabel→imaginedlambdaG sg→critic CE/EMAregularizer区分→adv缩scale REINFORCE加正熵→replayroot有限片段代理，不声称真初分布J精确梯度。
- RM-2268--2282：长modelerror→realroot短k合成buffer→mixSAC critic和actor→一次真实root但syntheticnext数例→配置F/B/k/mix/lifetime与version，modelphi只real监督。
- RX/RS-2284--2310：同nu/pi固定比较→true深度q_j平均TV/r误→kernel非扩张累distributionTV→prefix/tail B_k→trueinfinite需epsV；qmu→qpi需ratio或uniformpolicyTV；fixedoldpi→candidatechosenpi须allcandidateevent且两侧误差小于代理gain。
- RI-2334：actor无需search仍falsemodelopt，一步合法a例给old0→new.4真正-.16，因而误控域必须随策略选择扩大。下一块反馈图及表续核。
