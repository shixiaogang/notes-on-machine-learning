# 四处通用理论去重与真实入站身份维护

实际基线 33a06c0706bd8242083eb8d5d1abad367fe50117。git archive 的tex/plans全文件快照是678份，包含图、历史JSON、TSV等；**正式入站证明扫描范围是341份追踪的.tex/.md：223 tex、118 md**，包括计划中历史正文快照，见inbound-rebased-tex-md-scope.json的全路径名单。之前通信中678是归档数量，不是声称678份正文均通读。

341份范围内按完整key搜索，四个标签各只有唯一\label定义，未见ref、BookTheoremRef、eqref等入站调用，无跨卷调用。另按实际完整名称及Rayleigh--Ritz/Rayleigh–Ritz等拼法检索，人工读取inbound-name-occurrences-rebased.json的17处命中：8处为卷三四个候选theorem标题/标签，2处卷一自身Rayleigh–Ritz原理/应用、1处卷一大纲、6处卷一历史审查快照；后9处均不是调用卷三模型结论。较宽的“分位数损失/渐近分布/核岭回归”等检索命中也实际阅读，含模型用途与本地无宏预告，见inbound-and-implicit-search-rebased.json；没有把所有同名主题自动当入站调用。

|退役标签|修前唯一定义|保留的本地身份与后置参考|隐含调用/预告处理|
|---|---|---|---|
|thm:clustering-rayleigh|04-clustering L740|eq:clustering-spectral-relaxation；actual卷一thm:matrix-analysis-trace-minimum|旧L691“下节给出证明”改“说明连续最优值/唯一性条件”；局部Lsym、1≤K≤n、最小λ和/严格隙列空间保留，NJW和Cheeger保持。|
|thm:regression-quantile|02-regression L437|eq:regression-pinball、sec:regression-quantiles；actual卷一sec:statistics-nonparametric-missing|“下面证明”改直接给本地完整CDF最优集；上下左右和E|Y|条件保留，条件/经验分布转换及LP不动。ensemble-learning/03-boosting L169引用的是节key，L176叶内分位更新仍有基础，未退役该节。|
|thm:regression-glm-asymptotic|02-regression L712|模型GLM的structure/learning/theory等节标签；actual卷一sec:statistics-bias-efficiency|“条件与证明”“上述定理”改充分条件/这项分布结论；保固定维iid/内点/得分矩/局部统一Hessian/有限一致内部MLE，以及GLM信息式和logistic分离反例。|
|thm:regression-krr|02-regression L1433|sec:regression-gpr-theory、eq:regression-gp-posterior；actual卷一thm:functional-representer-theorem+sec:functional-finite-parameter-solvers|原L827无宏“完整证明”在r4改同核线性系统说明；后“该解”仍指本地fhat/alpha0。SVR L603、NW L1078是方法区别/截距条件，未引用退役key且结论保持。|

这些通用theorem/proof不保留裸thm标签；candidate-r4行政比较仅删上述4个label，无新增本地label。其它chapter/section/paragraph标题、input、scite键、图路径宽度均相同。PCA最优正交重构、SVM含偏置间隔界、GMM/EM模型单调性等模型专有theorem/proof保留。

数学保留与去重边界：谱trace-min目标/达到解/间隙列空间保留；pinball与CDF集合保留，仅通用单侧导数证明移到卷一参考；GLM矩/极限/模型信息保留，仅通用积分得分与CLT证明展开去重；KRR函数目标1/(2n)+λ/2、K+nλI、函数读出/驻点/凸性/系数不唯一保留，通用系数目标proof展开去重。不是删去模型推导所需条件。基线/候选快照与逐句依据可恢复。

当前是实际rebase后、尚未应用的精确候选决定；root应用后需再次校验源SHA、入口、构建与PDF。没有声称正式标签已在root退役。
