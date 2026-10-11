# 29 发现与七门槛、E1–E12

C→P→W 三遍均对原固定稿 `5cee06782bf5cd1ccde8531eeae1785656045e2250a23c954af55da4430597e4` 执行。最终增量稿 `084acd6b2eab33f0c4685d149f6af93769b850d77260fe47af5378036a3302b1` 的关闭证据另见 06-final-closure.md；此文件保留原发现绑定关系，不将原稿改标为新稿。

## 稳定发现

| ID | 原位置/短引 | 根因与最小动作 | 当前证据状态 |
|---|---|---|---|
| IND29-F01 | L773 / P112.S02「还需提供自身的可逆性和密度追踪机制」 | 给少步学生评价密度写了过强必要条件。可逆映射是可计算密度的一条路线；多对一映射也可以累加逆像贡献，随机模型亦可有密度。P111没有将学生限为双射。应先要求自己的密度构造和求值机制，再将可逆体积追踪写成条件路线。 | 原 W 遍发现并即时报告；root 已实际修新 L787；06 的独立增量和终稿整章顺读关闭。 |
| IND29-R01 | L543、561 / P082.S04→P083.S03，状态相关但参数固定方差后，wt/Ct从期望外取出 | 原式在开头 time-only σt 下成立，但旁支未显式回到仅随 t 变的方差，首读可能把状态依赖继承到外取系数。可在相减后段首补「回到仅随噪声步变化的固定逆转移方差设定」。 | 阅读澄清，未判原核心式错误；新 L575 已补，06 复读关闭。 |
| IND29-R02 | L767 / P109.S01「若积分只到δ>0」 | P105刚说明密度评价是数据→终点，未说明截断的是观测端点，可能把δ读作终端积分上限。改「若把观测端点截断到δ>0」。 | 阅读澄清，意图可由P098恢复但不靠后文倒算；新L781已改，06复读关闭。 |

另有 root 发现的两处行宽布局增量：将 P029 的观测 log density 和 P079 的同一路径反向分解从行内移为显示式。它们不是本代理宣称的独立版面发现；本代理只核新增式语义和上下文，不能代 root 的 PDF 复核。

## 七门槛（原全文检查后以终稿差异关闭）

- G1 可检验命题：P013的归一化以前后分布积分1判；P037 decoder独立时后验等先验以Bayes判；P045 density公式以diffeomorphism判；P070 terminal KL写出数值对象。P112的可逆“必要”未能成立，开F01并用actualfinal限定关闭。能力/约束的承载对象可落到 p/q/f/核/算法，而非模型“效果”标签。
- G2 压缩表达：P021拆φ共享与mean/scale输出变化；P031–032区分模型族误差、后验族误差和当前encoder gap；P081–084精度/条件方差/逆转移方差/标准差不互称。P110质量比较固定 network/budget/criterion，P070“充分接近”已有具体 KL 和 scale/dimension依据，不靠“接近”口号通过。
- G3 新对象转换：P007完整x评价→顺序sample信息条件；P062–064観测p→固定x下latentq；P069单步ε→整条path明确不是同一联合抽法；P074真实逆混合→已知x0解析条件；P101递减t→递增u改符号；P105 truefield→learnedfield定义新ODEdensity。R01限定从state-dependent旁支回time-only，R02限定observationendpoint，均须explicit修。
- G4 解释时序：P012先latent因素再VAE；P020先marginalintegral难题再ELBO；P044先多对一积分再Flow双射；P078先固定x0/pathlatent再ratio；P088先unknownscore与knownkernel再identity；P097先Brownian/time-isotropic设定再reverse。跨章结果本地已有当前结论，未拿聊天背景/后文补释替代。
- G5 局部入口：每节/主要小节入口 P005、P012、P020、P034、P044、P051、P062、P068、P078、P097、P115、P125、P130 都有本地具体对象。P034以dim/noise、P062以变换放在p还是q、P130以noise+程序承接，非只有抽象判断。
- G6 公式双门槛：56显示式逐项见W-special；NLL是已给iid完整x经验目标，ELBO回答marginal难算问题，sup_Q来自fixedθ的候选qfamily，KL各平均measure在本地指定；diffusionwt为middleKL换noise得到，timeonly条件不移旁注。无最坏集合优化，故无需编造adversarial允许集。本章一般连续逆式的反演proof借外部理论，已明确正则边界，未把本站局部代数当完整反演证明。
- G7 回指与范围：P035 conditionalmean先含finiteL2结论后Bookref；P045变换条件与公式先给；P078本地pathELBO；P068人工t/动态真实time本地说；P121–123三理论问题本地展开后引用NN。只核当前位置的可读性；被引NN/28内容本代理参与改写，关联披露，不称这些跨章判断完全独立。

## E1–E12 实际校准

| 项 | 触发位置及动作 | 判断 |
|---|---|---|
| E1 比较口径 | P002两costquery、P071 terminal KL两值、P110 same network/budget/criterion、P120 same representation/measure/preprocess。核比较对象、scale、方向、参照。 | 未拿“效果接近”当命题；toy数值均固定同target或明确不同barα，KL下降有数值可查。 |
| E2 关系后果 | P030 oneposterior sample/encoder-decoder cost，P055–056 query方向，P095 randomstep vsTgeneration，P128 compression/latentfit/decodeerror。拆关系两端与具体后果。 | 输入已知性改变并行方向，samples改变decode次数，latent小空间节省重复denoise；不是空泛“与使用有关”。 |
| E3 要求承担对象 | P045 f双射/C1，P069 βrange，P098 qt与reverse解条件，P117 sum/product图scope。逐项定位“谁满足何条件”。 | 承载对象清楚；F01原studentdensity能力把一种mechanism写必要，已修。 |
| E4 多重否定 | P045 a.e.diff+bijective不足；P065 positivebase不能exactdisconnected支持；P131 nod-dimensionaldensity。翻为正命题核范围。 | 可读为需extra changevarconditions、positive transformeddensity、pushforwardsingular；必要限制皆有条件，无nestedexception训导框架。 |
| E5 候选集合桥梁 | P017 nonlinear残差→approx posterior；P031 fixedθ Qsup；P062 posterior Flow扩q；P125包含原family→bestELBO不降。 | 每个新family由计算缺口/已有对象推出，包含关系在最大值结论前说明，不要求凭专业背景猜集合。 |
| E6 重复例新增用途 | P018后验非点、P029ELBOtightness、P047uniqueinverse、P071endpointmismatch、P084weightcheck、P106ODEsign。沿N05贯穿例检查new任务。 | 同target复用有六种独立新增计算，不把迟到定义当“新例”；每次都有本地equation/object。 |
| E7 三问题本地化 | P121–123与P136逐句读 expression/convergence/generalization。 | candidatefamilylimits、actualobjective/cost、newdata/factors三项都展开；NN只供后续分析，当前段足以懂问题。 |
| E8 入口抽象判定 | 逐检查新方法入口：latent共同变化、multi-inverse integral、forwardnoise、pathlatent、timecoefficients、samplerpushforward。 | 方法各有具体构造/待求对象先于一般labels；未以“不是…”的抽象句占局部入口。 |
| E9 最不利集合 | 全文无max-min、worstperturbation/robust允许集；核sup_Q为最好q而非worstcase。 | 最坏集项不适用的对象理由明确。仍核NLL minimize/ELBO maximize/KL方向/逆时间符号，无方向漏查。 |
| E10 局部到一般范围 | P060 fixedA trace无偏→fullnumericaldensity，P074 knownx0Gaussian→true reverse混合，P104 sameqtime→differentpath，P107 approximationODE/SDE。 | 每次范围扩张/停止继承的部分写明，旧exact结论不套approxprogram。 |
| E11 新记号为何需要 | P031 Q/sup为误差源分解，P069 barα为任意stepdirectdraw，P088 qt/score为unknowndensitygradient，P101 u为numericalpositiveclock，P105 pODE为真实求值对象。 | 新量之前都有problem/calc need；φ对应ω在本地解释不是裸跨章符号。 |
| E12 绝对量与变化 | P029 pθ不动qchange影响ELBO；P070 conditionalKL平均vsmarginalKL；P071两个endpointvariance；P125 theoreticalsupvsactualtraining。 | 量是密度/界或KL，各数据对象、方向和基准可指出，未只称“更好”。 |

本文件给出的接受依据均针对具体正文位置。没有外部论文全文查证、模拟实验、完整随机反演证明或新PDF认证；终稿文字通过的范围结论须联同06关闭证据，不以计数或构建通过代替。
