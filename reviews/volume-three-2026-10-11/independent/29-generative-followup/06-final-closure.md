# 29 终稿增量 C/P/W 与关闭

受审前稿：source-5cee0678.tex，SHA `5cee06782bf5cd1ccde8531eeae1785656045e2250a23c954af55da4430597e4`，旧全文 C→P→W、特殊单元已全部先完成。

实际终稿：source-084acd6b.tex，从根TASK最终源只读复制，SHA `084acd6b2eab33f0c4685d149f6af93769b850d77260fe47af5378036a3302b1`，903行。旧快照与原记录均保留，未覆盖。根源冻结，本代理没有编辑、构建或提交。

对两稿先看全文差异，确认实际只有五处相关语义/布局增量，再独立读取两旁连续上下文 L140–226、468–612、736–802。此时未阅读root的局部review.md来代替判断。随后将终稿按 L1–310、311–620、621–903顺序连续读完整903行，正文、全部公式、表格、算法和图注均在输出中，没有截断。最后阅读完整章首→三机制→比较→小结的关系，未新建未关闭发现。

## 增量 C 遍

- VAE数例显示 log N(2;0,5) 保持同一个观测密度对象；后面q=prior与θ固定的差距比较没有被插图式打断，仍回答q匹配程度影响下界。
- DDPM路径反向分解新增左端 q(x1:T|x0)，把“同一路径密度”从口头回指落实为等式；仍是fixed forward q的因子分解，不把learned pθ逆chain当同一条truepath。
- 方差从time-only presetσ、可学/状态相关两旁支回到time-only，weight外取期望的论证保持；simpleloss/importance抽步/DSM后续职责没有变。
- δ明确为观测端点，与奇异data positive-noise区间/PDE/flow端点需要相接；终端priorTc保持原对象，不误解成Tc改δ。
- 蒸馏学生density先要求自己densityconstruction/evaluation，再给可逆volume route；后文implicitmany-inverse/pushforward论述兼容，生成程序与可算density的章首问题得到一致回答。

## 增量 P 遍

- 旧P029→新L161–175，与前P027/028 Gaussian/Bernoulli observationloss和后P030 trainingcost连读：显示式只是数值检查的观测目标，ELBO exacttight与qpriorlower结果相同，没有新增需要解释的model。
- 旧P079→新L482–514，与前pathELBO及后三项解释连读：qpath左端、qT边界、t2:T条件reverse乘积正确；下一句“再对”简化原“再先对”的语序，conditionexpectation角色一致。
- 旧P082–083→新L544–588，连到P084–087：state-related旁支不再悬在wt/Ct公式上，“回到”明示原输入模型；mean抵消仍对任意σ成立，但其expectedKL式明确限timeonly。
- 旧P109→新L781，与前ODEnumericalerror、后samplingNFE连读：δ是zero-observation endpoint截断，得到noisedspace modeldensity，仍需decode/approx得到obsprob；两种measure的区别未删。
- 旧P111/112→新L785–787，与前采样cost、后四queries连读：teachersteps→studentcompute省/extra training，density需model自己的机制；新条件半句提供一种具体可逆选择，并未强加所有学生architecture。

## 增量 W 遍与特殊公式

- P029.S01b-v2「等于观测对数密度」→下接display log N(2;0,5)=−.5log10π−.4。公式 EQ12a 的variance5 normalizer、x²/(2variance)=.4重算正确；-2.12366由 Elogcond−KL 得，不是logdensity尺度改变。后S02、S03原样复读，qprior -4.91894与fixedθ仍准确。
- P079.S01b-v2「同一路径密度的反向分解」→新 EQ31a 左端 q(x1:T|x0)=qT|x0Πt2:T qprev|xt,x0。将原Bayesratio连乘时q1|x0与分母消去，留qT，t1boundary不漏；是sameforwardconditionaljoint。P079.S02-v2「再对每个…条件期望」后fullJdiff三terms不变，E_qt与decodeboundary没有混换。
- P083.S02b-v2「回到仅随噪声步变化…」→固定σt只是t函数，故wt/Ct相对于data/noise expectation为常量。两均值xt抵消系数 β/(√α√noise) 不变；ℓt=wtEεloss+Ct t2:T正确。IND29-R01关闭，不需要声称原timeonly核心公式错误。
- P109.S01-v2「观测端点截断到δ」→density是pδ而非p0，terminalTc保持同一prior与终段flow。先前L690正噪声interval条件当地可回接，不再靠猜积分上下限。P109.S02 unitmass/dequantization判断原样复读。IND29-R02关闭。
- P112.S01-v2「转移到额外训练…近似」→studentcost/approximation代价不被删除。
- P112.S02-v2「密度构造与求值机制；采用可逆映射时…」→先说任何需likelihood的student须自己的probmodel/evaluationroute，后conditional可逆route用volume追踪；不再把bijectivity当所有density存在/可求的必要条件。与P131多inverse累加兼容。IND29-F01关闭。
- P112.S03-v2「真实时间与噪声尺度…不同」→videoentiresequence可noise，但动态time仍单独轴，未把Tc说成predictionhorizon；本人写过被引28，保持关联披露。

终稿58显示式：旧56式均逐字原序保存，新增EQ12a和EQ31a就是旧行内关系改显示，加了qpath明确左端；两新增式已单独上述核验。行内片段289→287为两关系移出，非删数学含义。20标题命令（19纯标题单位+扩展阅读paragraph）、66labels、5paths/widths、15scite/32terms、全部算法原序相等，行政差异见final-boundaries.json，不把行政相等当语义通过。

## 最终整章顺读结果与限制

最终903行连续顺读后：共同measure/iid/query问题在VAE latent积分、Flow changevars、diffusion随机path中逐次兑现；ELBO/weightednoise/simpletarget不等值、knownx0posterior/modelreverse/trueunknownreverse不同、true-score同边缘只在matchingboundary与正则下成立，各条件都还在。模型比较本地分别讲expression、convergence、generalization，小结回收这些计算结论。五增量未引入newscope或本地推导断点，未发现新的技术或首次阅读硬问题。

范围结论：技术表述与首次阅读复核通过。未参与29改写/作者record，但参与了被引NN训练、泛化及PGM28，故不是跨章完全独立认证；仅就29当地内容支持判断，不把个人所知补进正文。外部论文全文事实、完整概率过程反演proof、执行实验、当前最终PDF版式不在本轮认证范围。root负责七PDF整卷构建与版面。本代理无productionwrite、编译、render或commit。
