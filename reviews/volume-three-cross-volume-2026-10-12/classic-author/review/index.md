# 经典部分真实跨卷协调：作者自查索引

最终候选：candidate-r4（22个经典接入文件，12改动、10不变），基线actual rebase HEAD 33a06c0706bd8242083eb8d5d1abad367fe50117；目标actual main a9cebd3ad6820d90e3f033822cdecd5a3002f547。before/after逐SHA见candidate-r4-manifest.json。补丁classic-cross-volume-final.patch SHA **54b45316d56b3f17d7bf8c256fcb5d6f8a6d79d8ddfc3f019bdcd409742675db**。

审查顺序真实分别执行：先冻结r1，再C-r1→P-r1→W-r1-01/02；修订冻结r2，再C-r2→P-r2→W-r2；新发现冻结r3，再C-r3→P-r3→W-r3；隐含预告修订冻结r4，再C-r4→P-r4→W-r4。固定版本之间未并行修改正文；全部是作者自查，不冒称未参与写作的独立审查。不同版本相同SHA的未动单元继承其已有逐句证据。

覆盖范围：r1行政划段U01–U37全部实际读完，37个变动段/特殊块的每个正文句与显示式有人工短引/白话意思/依据；r2重新覆盖实际返修句及邻段；r3加入第6章L8及6/12段；r4加入回归L788及前表图注、后转场与KRR/GP目标段。SVM含偏置theorem/proof、PCA模型theorem、EM theorem/proof、Dirichlet更新、JL维数式与扩散平稳分布、TSVM独立测试界均在实际阅读范围。无算法新增/编辑；分类集成表L1–22实际阅读，回归比较表相邻图注实际阅读，图路径/宽度未改。未宣称本轮重新通读六章全部或重新验收所有图/PDF。

|发现|候选关闭证据|
|---|---|
|CV-F001 GP目标节误指|r1 U14；改sec:rv-paths→actual sec:rv-gaussian-generation，有限相容高斯与路径版本边界均本地。|
|CV-F002 PCA谱隙归属|r1 U24；“该定理谱隙”改本地严格谱隙决定主子空间/投影，模型PCA theorem保留。|
|CV-F003 JL自适应范围过宽|r1 U25/26；映射后固定集内选择仍覆盖，集外新查询需另析。|
|CV-F004 KRR整目标有限读取误说|r1 U15；限数据拟合项而非范数项，存在/有限条件保留。|
|ACV-C001 全可实现分布弱优势|r2 C/P/W；概述L101条件完整，绑定actual a9全分布定理。|
|ACV-C002 回归引用二分类范围|r2 C/P/W；回归L1445及分类集成24限定二分类AdaBoost。|
|ACV-C003 完整概率向量校准图|r2 C/P/W；分类L76区分逐类/最高概率与完整向量条件频率。|
|ACV-P001 机制/理论长段|r2 C/P/W；概述99/101分段但不增标题。|
|ACV-P002 Dirichlet参考呈现|r2 C/P/W；概率245本地合法先验后括号，不让外卷当句子主语。|
|ACV-W001 KRR驻点最优机制|r2 C/P/W；回归1398补系数目标凸性，与函数严格凸唯一性分工。|
|ACV-W002 零分母计数指标|r2 C/P/W；分类76先声明零分母记号规则再宏/微汇总。|
|ACV-W003 集成章泛指投票上界|r3 C/P/W；集成8限定二分类AdaBoost/正优势/训练上界。|
|ACV-I001 隐含“完整证明”预告|r4 C/P/W；回归788改由同核线性系统说明，节身份保留且后文兑现。|

七门槛/E1–E12见calibration-and-gates.md，actual目标读取/38引用对照见../target-reading-record.md；341.tex/.md的入站身份及四thm退役见../inbound-and-deduplication-decision.md；仅行政校验见../administrative-boundaries.json与patch-application-check-r4.json。

局部文字/技术自查无已知未关闭项。补丁在ignored scratch的actual基线副本已应用并逐字还原12个候选文件；正式源码尚未写入，未构建/提交。root实际应用后的源绑定、独立复核反馈、全书构建/测试/书页QA及最终推送仍在主任务阶段，不以本报告替代。
