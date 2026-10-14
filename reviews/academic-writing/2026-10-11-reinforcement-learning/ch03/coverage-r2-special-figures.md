# 第3章R2特殊单元：全部图内与图注

CH03-R2-SG，2026-10-12，修订1；独立R2；hash `927887345166301fb9aaa47eb6a53ec8389f7abfe6353bc87e5b27b5049f353e`。C遍已全文读31图，本次在三遍完成后再次完整读取所有直接`figures/rl-learning-*.tex`源。以下ID以文件名、TikZ node名或显式几何/文本单元绑定；foreach展开的每个成员列清。图注全部句子另见W原caption行，本文件逐图索引。科学对象/数值/连接关系已核，未渲染或检查书页字体、裁切和版面；不能凭源说视觉通过。图源均属冻结116项清单，末核SHA一致。

## 图01-图10

| 稳定ID、位置短引 | 白话与逐部件依据 |
|---|---|
| SG01 `map:data,time`「覆盖/间隔」 | 经验和时间条件共同接入组合框，不以时间抽象为modelbased第五类；两标签分别已在正文L30预告。 |
| SG01 `v,p,mv,mp`「四接口」 | 四框每个都读：不模型value、不模型π、modelvalue、modelπ，横竖分割只是两维分类，无框间执行箭头。 |
| SG01 `theory,eval,四种组合框,边` | 下两框样本边界/实验预算，data-time连线→四组合、组合虚线分叉→theory/eval，虚线分析口径非真实data传递。C L35两句支撑，全部8node与框/分割/边核。 |
| SG02 `bandit-geometry:a轴/刻度1,2,3` | 横臂纵均值，纵1/2/3对应.2/.4/.6比例；臂1mean.55区间.5-.6、臂2mean.48区间.28-.68、臂3mean.3区间.18-.42，foreach三成员与端帽/点全核。 |
| SG02 `上界最大标记,b椭球/轴/估计/x/长轴文字` | 圈臂2上端.68准确；θ1/θ2轴、centerhatθ、长横轴低信息、x特征方向箭头，不导航方向/不是欧氏球。非diag例比例正文已限，C L174三句。 |
| SG03 `exploration-chain:s0,s1,s2,s3,reset` | 起点→门前→门后→奖励三边正确/单向/正确，s2错误虚线回s0为代表错误重置，标题/低到达率文字不称所有算法指数下界；链从独立教学抽出。 |
| SG03 `pos,door,tv/两边/误差1文本` | 位置往门的长程行动与往ξ±1显示器的误差奖励不同，已知随机律仍squareerror1；图无用预测error证明epistemicuncertainty。C L252三句说明独立任务。 |
| SG04 `traces:时间轴/s_k-3,s_k-2,s_k-1,s_k/err` | 四原子时刻、当前δ_k，箭头δ→本次1/前次.72/前两.5184/前三.373248，foreach四点及箭头值均γλ=.72幂。 |
| SG04 `e公式/衰减说明/虚线` | e_k=sum_{t≤k}(γλ)^{k−t}∇V(s_t)，远访贡献小；前三虚线表示更远同机制不是targetcopy。C L425三句前/后视图职责不混。 |
| SG05 `is-sampling:s0,s1,s2/权重` | two-stepπ/μ ratios.8/.5=1.6、.6/.25=2.4；第一reward权1.6/第二3.84，图没加γ因单列概率权，正文另有γr_1。 |
| SG05 `r0,r1,r2/rare说明` | 起/中/奖励1，两μ.1 pathprob.01 weight100，E1 Var99正文核；环境核不进入ratio。C L504三句分上下不同task/支持与方差。 |
| SG06 `double-sampling:x,a,b,p/边` | samex分别采ξ用于δ、tildeξ用于∇δ，两branch→乘积；给定x条件独立/不是same样本复用解释，所有4node/4edge准确。 |
| SG06 `θ轴0,1,2,3/loss轴/两曲线/极小点/图例` | blue(1−θ/2)²极小2、amber .5(1−θ)²+.5极小1，θ横缩1.5不变参数，δVarθ²/4说明；60samples解析生成非实验。C L700两句，未运行绘图。 |
| SG07 `dqn:env,buf,online,target,loss,y` | 六node每个text：true(s,a,r,s',z)→buffer→online(s,a)/target(s')、target→sgy→loss、online→loss。Huber onlyθupdate，r+γ(1−z)legalmax同F800。 |
| SG07 `全部边/periodcopy/gradient/actionfeedback` | online虚线copybar不是targetgradient；loss橙边只回online；onlineεgreedy→env控制下一batch。C L812两句与图全部数据标签核，max域邻正文明确。 |
| SG08 `return-distributions:A/B轴与刻度` | 每panel横G(-.5,.5,1.5)纵prob(.5,1)，A.5 atomprob1，B−.5/1.5各.5；所有foreach六x标签/四y标签读。 |
| SG08 `均值虚线/说明` | 两虚线都G.5，均值same但B有波动，非parameterCI。C L894两句人工指定distribution，node/atoms全核。 |
| SG09 `error-flow:start,fork,left,right/边` | 起点必到低dataweightfork，left真实1估0/right真实0估1，orangechosenright、虚线未选left，MSE1e−3/loss1与本地task吻合。 |
| SG09 `data,q,policy,class/feedback` | 样本cover→q、representation/optimization→q→动作访问→分布改变→data，所有4边加return链准确；非errors无条件linear sum。C L1008两句。 |
| SG10 `gae:a,b,c,aw,bw,cw` | 时刻t/t+1/t+2 delta.2/−.1/.5，weights1/.72/.5184，各contrib.2/−.072/.2592，六node文字全核。 |
| SG10 `sum/边/γλ说明` | 三contributions汇A=.3872，γλ=.72，均人工数例，不learningcurve。C L1173两句、F1163支持。 |

## 图11-图20

| 稳定ID、位置短引 | 白话与全部部件核对 |
|---|---|
| SG11 `policy-geometry:start,theta,phi/箭头` | sameBernoulli参数两坐标，startp.5 θφ0，θ+.1→p.5250、φ+.1→θ+.01→p.5025；两不同路径same起点，Fisher文字不等坐标step。 |
| SG11 `q轴/贡献轴/.8,1.2界/两解析线/图例` | ε.2/±A1，正blue q到1.2flat、负amber−.8flat到q.8后−q；axisy标签1.2/−.8与曲线准确，内min两贡献非hardqconstraint。C L1301两句。 |
| SG12 `actor-critic:actor,env,sample,critic,delta` | 五node currentπ→realenv→sharedrecord→V，r/z→δ与V→δ，critic非P；图record四tuple省z但旁边明确终止输入，不偷timecap为终。 |
| SG12 `所有反馈边/更新文本/旁说明` | blue采估路径、orange虚δ∇V→critic/δ∇logπ→actor，newstate回actor，两个目标/下一data互相反馈；图符号省γt作机制略记，正文F1336明确目标权。C L1364两句。 |
| SG13 `sac:data,q,lq,y,actor,lp,target` | 七node trueDrecorda→双Q→LQ、sgy→LQ；Dstate→currentactor重采a→Lpi、targetbarQ/currenta'→y，r/z与s'分别data输入。 |
| SG13 `Q到Lpi/grad/LQgrad/温度同步文本` | critic参数fixed仍∇aQ路径到actor，Lpi重paramgradient回actor、LQ只w_j；bar缓跟/temperature另调，目标支路不导，所有路由/标签核。C L1516三句。 |
| SG14 `regularized-search:old,obj,new` | fixedstate p_ref→avgq−αKL→pnew∝prefexp(q/α)，向高q但不离zerosupport，动作分布不参数分布。 |
| SG14 `draw,elite,fit/return边` | candidate−1,0,1,2/score−4,−1,0,−1，tie小θ elite{0,1}，MLEmean.5/var.25，下一重新paramsampling/整轨迹eval。C L1618两句区分两个空间。 |
| SG15 `model-anatomy:s,p,sp,r` | explicit(s,a)→conditionalP→preds'，另一(s,a)→reward/continueheads；是职责示意，输出不把非法conditionalmean作legalgridstate。joint相关需求L1671已有说明，非此箭头声称独立。 |
| SG15 `o,e,d,pred,rec/所有边/尾说明` | historyobs/actions→encoder/inference z→latentdyn(z,a)→R/c，z虚→optionalrec_o；重建保信息仍需actionconditional/充分性，不以latent当充分state证明。C L1680三句。 |
| SG16 `dyna:env,data,q,model,sample` | 真一步→record五量，record实→Q/modelcounts，model虚sample nplan→模拟五量→Q；Q→探索下真a的完整return。 |
| SG16 `统一Q文字/来源说明` | r+γcmaxQ目标减当前在正文F1713全式，图是target简称非update全式；replay可同recordupdate/model新后果需承担误差。C L1723三句真预算明确。 |
| SG17 `mpc:obs,fit,opt,act` | realobs复规划root/按日程stateinfermodelupdate→候选sampling/scoring/update→仅first真实execute，closedloop反馈只有该step新obs。 |
| SG17 `particles/opt双边/不可逆说明` | Nseq*Mparticles*Lsteps/optionalV/I轮，opt和simulation双向evaluationloop，剩余不trueD/irreversiblealreadyexecuted；C L1793三句不声称闭环取消风险。 |
| SG18 `muzero:history,root,up,right,leaf` | history经representation→latentroot，up/right展开g各预测r/z，leaf fprior/value；图nodee_phi与正文h_phi属表示函数别名，职责一致无额unknownmodule。 |
| SG18 `backup/real,rv,pi/searchπ/尾训练说明` | leaf r+γv备份→root N/Q；真实后续r/value targets、rootsearchvisits π∝N^(1/τ)→policyloss；沿recorda展开fit三targets、每执行重search、prior不是soleactor。C L1870三句。 |
| SG19 `tdmpc:root,a1,a2,b1,b2,c1,c2,q,act` | 真encoderroot分三候选两步latentroll→R累计+末Q→最高scoreseqfirsta，三path所有node/edge显列，点是状态非CNN层。 |
| SG19 `prior,data,loss/实虚/文字` | πprior提出部分candidate、其他trajectorynoise，truefivefieldseq虚→latent/R/TDloss→训练dyn，prior另Qscore训练；不是πonlydeployment。C L1920三句。 |
| SG20 `model-exploitation:s,safe,shortcut/边` | fork safehat/true.6/test99% vsrare.9/.1/test1%，chosenorange捷径；avgabs.01*.8=.008，trueloss.6−.1=.5。 |
| SG20 `额外planning说明/C L1987` | morecompute可能更稳定错选notpredict误差变少；C三句明确人工概率/测试权，不实验曲线。 |

## 图21-图31

| 稳定ID、位置短引 | 白话与全部部件核对 |
|---|---|
| SG21 `model-gradient:s0,s1,s2,p0,p1,p2,f0,f1,cost` | 三state各调用sameθπ，前两u0/u1经fixedφ动力学到下state，末state→terminalcost；p2只是同参数策略在末状态的表示，当前两步成本无后续u2边、不计额动作。 |
| SG21 `全部forward/reverse/说明` | 实state→π/state→f、πaction→f、f→next，虚cost回两model及两π有效action；图略反馈导路径本地D式保π_xD，fixedφ只策略求导/trueD另fit。C L2100三句。 |
| SG22 `dreamer:data,post,fit,actor,prior,heads,returns,critic` | 八node真seq→RSSMposteriorroot/modelprediction+KLfit，actor→prior→R/c→return、critic→return/rootpost→prior，再priorstate→actor。 |
| SG22 `所有虚线/legend/root边` | returns→criticfit和actorfit虚为损失依据而非一概pathderivative，post→fit真监督；V1/V2/V3梯度区别正文已给。root后无真obs，C L2190三句部署需posterior。 |
| SG23 `mbpo:real,model,root,roll,buffer,sac` | sixnodesDreal→φfit everyF、Dreal→root→currentπ k-roll、φ→roll→Dmodel，realη和model1−η两个batch→SAC。 |
| SG23 `updatedπ/数据声明` | SAC虚更新后π回roll，φ不以合成当true监督；true/synthetic分别count，根之后非真实。C L2275三句。 |
| SG24 `model-feedback:model,policy,env,fit` | model→πchange→trueexecute/calibrate→newregionfit→model，闭反馈清；oldπ误差小不保newπ，offline无right真实交互edge。 |
| SG24 `penalty,short,cal/虚线` | 三制约分别改modelscore/propagationdepth/newdata，u惩罚不是统计半径、short不免tailerror。C L2342三句连一步a0→.4例。 |
| SG25 `options-rooms:grid/wall/doors/routes/dots/S,D,G` | 8x5cell、x4.5墙y2/4开口、start2,2、D4,2、G7,2；straight5atoms/two高calls、upper强制(4,4)detour9atoms四额step，foreach六圆点准确。 |
| SG25 `左右房间/实虚图例/高层时刻说明` | 框S/D是两highdecision、Gterminal，不误框G第三highcall；实line5/上path9和门coords标签明确。C L2391四句独立task不baseline。 |
| SG26 `hierarchy:task,high,low,env,end,reward` | sixmodule任务到G→ζ选door/ω→lowπ原子→env→original/optionalauxR；newstate供low与β、β交还high，不每stepζ。 |
| SG26 `reward虚反馈/全部edges/尾说明` | originalR高层/auxlow可分别更新，Option-Critic无需auxR；learninglow改highactiontransition旧经验要处理，随机highinterval不减trueatomicsteps。C L2506三句。 |
| SG27 `skill-regions:三个填充z1,z2,z3/S/G/墙门/三箭头` | z1左下/z2左中/z3左上三个终点region、S3,2/G7,2，三policy全stayleft，门存在却无skill穿，所有fill/label/route端点读。 |
| SG27 `说明/C L2665` | 可完全区分→MIlog3在均匀detsetting，但无taskreach/相容启动保证；填充是人工region非heatmap。C三句。 |
| SG28 `optimistic-grid:11计数/障碍/状态公式` | 所有合法cell人工N(s)：(1,1)40,(2,1)24,(3,1)12,(4,1)4,(1,2)7,(3,2)2,(4,2)0,(1,3)5,(2,3)3,(3,3)1,(4,3)0；(2,2)障碍不写N，terminal0只是人工展示。 |
| SG28 `next,root/backup数值/图例文字` | V+(4,1).9/(3,2).4/(3,1).2，(3,1)right真实P.8/.1/.1，-.04+.9(.72+.04+.02)+.1=.762核。countstatevsstateaction明，教学discountbackup非UCBVI无γ实验。C L2750三句。 |
| SG29 `linear-design:ellipse/两轴/.0995/.7071/Λ/sampletexts` | Λdiag101,2=I+100e1e1'+1e2e2'，Δw'ΛΔw≤1，xradius.099504/yradius.707107，labels数值四舍五入、firstnarrow/secondbroad；featuredirection非新state熟悉度。 |
| SG29 `末说明/C L2901` | analyticconfidencegeometry非algorithmexperiment；caption三句人工matrix，未核渲染scale。 |
| SG30 `combination-lock:v0,v1,v2,v3,v4/fail/所有上边` | s0/s1/s2/ellipsis/sH，correcta0*,a1*,a2*,aH−1*向前，错误边示例前两到observablefail，文字其余也fail，rootreset仅episode。 |
| SG30 `h0,h1,h2,h3,h4/下链/说明` | hiddenprogress onlytime0/1/2/ellipsis/endfeedback，无progresssignal；upper可复prefix、lower失败排one完整串，改变obs/oracle改变hardness。C L3043两句明确not全obs表格协议。 |
| SG31 `evaluation-protocol:record/左右坐标/两个说明框` | 每seedcheckpoint保存Nenv/wall/testmean/rawG，leftxtrue转移/rightxwall两y测试expectedreturn估计；samecheckpointdata投两轴，不绘future/no数据曲线。 |
| SG31 `record双箭头/共享图例框/C L3149` | samealgo名/style/color/target/seeds，两图问sampleutilization vs同hardwaretimecost，不预设胜者、不把manualtrend当measure。C三句。 |

## 覆盖与限制

- 31个直接图源全部全文复读；上述63个功能部件记录显列所有节点、foreach成员、图内文字/坐标/刻度/数组、曲线/原子/填充、图例和连接端点。部件数是记录分组数，不是TikZ节点总数；未把颜色样式和排版命令伪装成自然句。
- 31图注全部在W逐句形成白话/具体依据，本文件以C原行逐图绑定。不把“图源已读”当图注已读或PDF已看。
- 数值图仅解析公式/人工输入与正文相对照；未执行绘图脚本、实验、数值证明程序，也未验收实际尺寸字体/书页对比度。冻结图源样式迁移和目录规范属共享资源治理，本角色不能改图，不将此局部写作审核扩为全书迁移。
- 图内没有新增成立技术发现；正文CH03-R2-01仍未修，图专项记录不使正文通过。
