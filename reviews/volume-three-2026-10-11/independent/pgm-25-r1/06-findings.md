# I25-R1 独立发现及实际返修核验

原受审固定源source-snapshot.tex SHA256 2467d92611a028072c1121bc94275473ebd18bc0047f65e752e0c999cb2fcbdd。全部I25-U/M地址绑定此稿；r3新增source-after-r3.tex SHA256 9bfa251dd2be0f818caa2dea06703a57baebfc93f58a7d54dc3d10a6b82d7dc5。本人只读审查未参与修订生产稿。每条以实际源文字而非聊天承诺关闭。

## I25-F01：MDL数据码长范围
改前：r2 U032-W02 L136，“编码未被模型预测的数据”。缺口：MDL给定模型后编码整份D，而不是只编码误预测的记录；把条件码长缩为失败子集会破坏模型比较口径。最小动作：明确“在给定模型后编码整份数据”。
实际改后：r3 L136恰为该表述。独立连续复读r3 L125–151，C：BIC与编码作为复杂度准则接同表数例/先验积分，主线未改；P：码长对象现在model及conditional fullD，主导罚的部分近似和图码长仍保留；W：码长句明确对象，其他三句的近似范围/方向无扩张，LL/BIC教学值未变。G2/G6通过，未新增比较单位冲突。状态：复读通过，关闭。

## I25-F02：Gaussian有限解边界（两处）
改前：r2 U091-W03/M31 L414–423，“λ≥0…估计正定精度矩阵”，随后“目标凸使优化误差可控”。缺口：可行K正定不保证有限minimum；样本S奇异且λ=0，沿nullspace增K使目标无界；S有零对角时offdiag罚不能压对应t→∞，即使λ>0仍无界。S=0,K=tI原目标=−dlogt为直接反例。最小动作：给正惩罚与正样本方差条件，无罚需S PD，零方差另处理。
实际改后：r3 L414先diagS>0且λ>0，L423写唯一有限PD解/λ0需S PD并为inverse/零样本方差先移除或另建；L425解释罚而将优化类别与统计条件分开。独立连续复读r3 L404–452，C：GaussianCI→smalln缺口→pen构造→existence→neighbor/兼容原任务，未变statcapacity；P：新增existence段独立承担finite/zero边界，罚项说明不抢定义；W：各variance严格正不是S整体PD，两者明确不同；λ0inverse正确；双计数/不罚diag/预测coeff/OR-AND未动。Gaussian子范围状态：复读通过。
充分条件独立推导：sampleS≽0,diagS>0,λ>0，D=diag(S)，W=(1−ε)S+εD PD，ε>0可小到offdiag|Wij−Sij|<λ。罚支撑给f(K)≥tr(WK)−logdetK；其W最小eigenvalue正，约束sublevel的所有K eigenvalues在远离0且有界区间，故finiteopt存在。−logdetstrictconvex→uniqueK。λ0仅S PD时−logdet+trSK有minimumS⁻¹。本论证专门本章offdiag版本，未引用论文all-entry版本作替换。
扩充改前：r2 U109-W01/M40 L508–521同样允许λ≥0，稀疏低秩程序写min而非argmin（已更正早期消息措辞）。λ0且observed sampleS奇异仍无finite optimum，取L=0、S=K即可继承反例；正文“可以拟合”需边界。r3 L510–525尚未改这部分。最小动作：说明正惩罚为默认；λ0需observed sampleS PD且只边缘K最优，S/L识别另需区分条件。λ>0且γ>0因罚含S对角、PSD L trace可控制大K及L，存在边界不同于offdiag版本，不能盲复制zero样本方差要求。整体状态：Gaussian子范围已关，lowrank子范围待修改，因此F02整体未关闭。

## I25-F03：GES首次保证缺对象与时序
改前：r2 U049-W04 L215，“其理论保证依赖…条件，适用的是这套搜索与假设”。读者缺口：尚未说保证为固定维大样本恢复真实MEC/CPDAG，可能读为finite global score optimum。544因果节才定义局部一致与CPDAG恢复，不能以远后文补首次介绍。最小动作：215就说明“大样本一致性，即恢复真实等价类”以及scoreequiv/decomposable/localconsistent/perfect-map条件；后因果含义部分仍可扩展。
来源核实：[Chickering原论文](https://www.jmlr.org/papers/v3/chickering02b.html)明确两阶段渐近恢复完美映射，非一般greedy finiteglobal结论。本文独立入口缺口为G1/G4而不否定GES算法内容。r3未改此句。状态：待修改。

## I25-F04：有限正指数族的无罚MLE可不取得
改前：r2 U099-W01/M35 L454–467，“取λ≥0，完整似然的稀疏估计为minθ…”。缺口：finite positiveexpmodel无罚MLE可只逼zero-prob boundary；单binary全x=1,f(x)=x时平均NLL=log(1+exp(−θ))仅θ→∞达下确界0，finiteθ无min。λ>0且全部θ受L1罚时finite状态NLL≥0使objectivecoercive，有限解存在；λ0则需无罚MLE实际存在或处理boundary。最小动作：默认positivepen/另注明zero-pen存在条件，不改核心formula。r3未改。状态：待修改。

## I25-F05：充分性共同原因/共同直接父节点
改前：r2 U114-W02 L535，“共同直接原因都已观测，即当前模型没有遗漏潜在混杂”。缺口：普通“直接原因”按fullcausalgraph父节点理解时，仅观测共同父节点不足nohiddenconfounding，例如隐Z→A→X1且Z→X2（仅X1/X2观测），Z是共同原因而非两者共同直接父节点。旧before还明说“相对于当前节点集合”，新句省去该相对口径；后“只针对所选节点集合”限定集合但未定义路径缩约的direct含义。
核查一手：[Tetrad原作者说明](https://www.phil.cmu.edu/projects/tetrad/old/tet3/chp5.htm)用两条只在共同起点交会的有向路径定义commoncause，sufficiency要求这些共同原因观测。最小动作：删除“直接”，写所选变量共同原因已观测；如果要相对节点集的direct定义则需先解释，新增负担更大。此条不仅文风偏好而是W5/G2两定义不等价。r3未改。状态：待修改。

本轮r3只对实际MDL与glasso返修上下文增量审读，不把它称全章重新478句阅读；r3未变源与r2差异已逐字核对，因此其他已审语义沿r2保留，未审修订恢复待审。待F02lowrank/F03/F04/F05返修快照后按影响范围重新C/P/W。
