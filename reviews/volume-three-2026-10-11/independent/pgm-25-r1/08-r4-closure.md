# I25-R1 r4独立增量复核（C→P→W）

实际固定源source-after-r4.tex SHA256 ce90502cc9be582178dcd2c9c36e37ac5c24dd87e2b57e471fe642161ce36cdc，与根after-r4相等。受审者未参与修订。先读source实际连续L204–236、450–489、490–566并看r3→r4完整diff，后才核作者07-closure-r4.md/repairs实际变化。未把增量审读称全章新478句；未变语义依原完整r2 C/P/W及逐字diff保留。

C：GES前有单DAG局部最优与BICmove，后有smallnode精确DP/IP；其保证明确为fixed d/sample→∞的真实MEC恢复，确与finite score认证分开。discrete从Gaussian精度转finitefeatures、positiveexp、全部参数稀疏pen，再existence/no-pen边界→gradient/modelexpectationcost→pseudo/Ising，目标转换成立。latentGaussian从Schur具体例子到S/L估计，existence与split-identifiability分开，之后统计图转externalsetting因果；新增条件没有承诺恢复truehiddenphysics。只剩GES首次新‘局部一致性’解释仍遥后550，见F03持续首读点。

P：r4 L215前3句（same-score representatives→CPDAGforwardbackward→multiendpoint合法性）未变，新增第4句给asymptoticMEC，第5句列score模型条件；完美映射前19章L70/88已有定义、scoreequiv和decomposable本节Dir/localLL有对象，唯localconsistency新词在550才解释，需要就地白话。r4 L464明确λ>0/全部params罚，L470独立existence/no-pen两句，后一段回gradientcost，中心顺序完整。r4 L512正pen，L525 norm/gamma→existence→λ0PD/margKunique/splitnonunique，L527只讲nuclearnorm/恢复conditions，L529交集移项承接，避免优化存在偷作统计identification。L541删共同‘直接’，与Markov parents、faithfulCI及MAGlatentcontexts相容。

W新增/受影响逐句（地址以r4行与文字定位，未覆盖排版命令）：
I25-R4-GES-W04 L215短引“在固定节点数”：意为fixed d且n→∞时recovertrueMEC；输出/渐近明确，非finite global-score，F03此子缺口关闭。
I25-R4-GES-W05 L215短引“该保证还依赖”：scoreequiv/decomposable/localconsistent+perfectmap限定上述恢复；scoreequiv与分解前文有解释，perfectmap前19定义可依赖；localconsistent仍首次术语无本地意思，F03该条件首读点待补。
I25-R4-DIS-W01 L464短引“取λ>0并惩罚全部参数”：finite positiveexp averageNLL+allthetaL1，pen范围无未罚方向；满足coercivity所需，非只非diag罚。
I25-R4-DIS-W02 L470短引“正惩罚使参数”：finite-state平均−logp≥0，因此λ||theta||1使||theta||→∞时objective→∞，continuous finite-dparam minimum存在；不额外声称唯一，正确。
I25-R4-DIS-W03 L470短引“取λ=0时”：需查unpenalized finiteMLE，某零cell逼boundary onlyinf；singlebinaryall1 logistic反例满足该描述，不宣称所有zero都无MLE。F04关闭。
I25-R4-LR-W01 L512短引“取λ>0”：以positivepen默认拟S/L；γ>0随后norm说明，与formula先后相连，λ0另说明。
I25-R4-LR-W02 L525短引“逐元素…包含对角”：normSallentries/γpositive调relativepen；保证Sdiag受罚不同glasso，pen角色明确。
I25-R4-LR-W03 L525短引“正惩罚控制”：finiteKPD optimumexists，K=S−L与LPSD下S=K+L；normS≥trS=trK+trL及trsampleK≥0，lambdaγtrK+lambda(γ+1)trL控制growth，−logdet控制zeroeigs。PD指实际precisionK，不将LPSD误读为所有矩阵都PD。
I25-R4-LR-W04 L525短引“取λ=0时”：sampleSobs PD下margKopt inverse且unique，S/L可能nonunique；L0/SK可给finite实现，sum未罚可移，描述准确。F02lowrank子范围关闭，r3glasso子范围已关，因此F02整体关闭。
I25-R4-LR-W05 L527短引“半正定矩阵”：PSD核norm=trace，罚鼓励lowrank；没有ranktrue保证。
I25-R4-LR-W06 L527短引“恢复保证还需”：需要sparse/lowrankdistinguish/diffuselatent，后交集移项给反例；同源统计恢复与finiteopt分开。
I25-R4-SUF-W02 L541短引“共同原因都已观测”：要求所选变量的commoncauses被观测，含经潜中介path的共同起点；删direct阻止共同父节点不足反例，未要求所有世界变量都观测。F05关闭；前Markov parents的‘直接原因’仍正确不应联动删除。

实际特殊formula M35/M40与45显示式仍原式：finiteexp positiveλallpen/coercive和lowrankpositiveλγ存在推导独立成立；核心条件与表/图没有变。GES恢复primarysource渐近条件对象已支持；localconsistent术语本身的白话L550原句为‘样本足够多时，评分奖励补上遗漏依赖，惩罚多余依赖’，可以在首次L215直接前置这一意思，无需新事实。

r4门槛回看：G1明确finiteopt/trueMEC，G2充分性commoncause关系正确，G6正pen与min选择边界具体，G7无罚→有罚/precision→split范围已交代；G3/G4在GES新增condition的首次解释仍待补。E3保证对象/E10范围/E11newcomputeconditions/E12min/evidence方向没有新增风险。无本轮新科学错误，存在性新增话未偷作generality/selection正确性。

作者07记录：SHA恢复与实际变化吻合，独立身份没有冒称；coerciveproof针对Sdiag全部罚/PSDtrace正确，λ0仅margprecisionunique与source相同；finitebinaryNLL反例正确。作者称F03全关尚缺首见localconsistent的解释时序，需最后补充再独立复读。

状态：I25-F01/F02/F04/F05全部实际改后独立复读通过；F03保证范围子点已过，localconsistency首读释义待修改。不得把本页看过局部又称r4整章重新三遍。
