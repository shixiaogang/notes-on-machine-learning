# 最终经典跨卷协调补丁交接

工作区：prose-classic，分支codex/volume-three-prose-classic；本轮仅写自己的ignored build，未触碰该工作区或root的正式tex，未构建/提交。

真实卷三基线33a06c0706bd8242083eb8d5d1abad367fe50117，上游main a9cebd3ad6820d90e3f033822cdecd5a3002f547。最终candidate-r4-manifest.json绑定22个经典文件，12改动，10不变；实际上游目标10文件及SHA/git blob冻结于target-source-a9/和对应manifest。

应用入口：classic-cross-volume-final.patch（SHA 54b45316d56b3f17d7bf8c256fcb5d6f8a6d79d8ddfc3f019bdcd409742675db）。candidate-r4-manifest.json SHA de7fd2a50d6a2ed2d93c4ed8cf70b4366dd41bb353fb57bae617a9f27fe8da4b。review/index.md SHA 8fb7732b5e794cae6a2a73fb2b2c6a07c1a1fdc15cc48e75656105cfd2d01c05。modified-source-sha.tsv给12实际改动源的完整before/after SHA。

18处准备建议已采纳并结合actual a9闭环；四个基础theorem/proof在真实341.tex/.md无入站后改为带完整条件的模型应用说明与后置参考，不裸留thm标签；模型特殊PCA/SVM/EM结果保留。全部原15卷二引用核实际内容，补一个有限多分类入口；最终38引用=22卷一+16卷二，全部actual目标唯一定义。文字另收紧共形训练/校准条件、AdaBoost二分类/上界范围、概率向量校准对象、指标零分母和KRR凸性。

作者C→P→W分别执行、实际新稿固定，r1发现→r2修复→r3集成范围→r4隐含预告，所有成立项已闭环；逐句地址、短引、白话意思、条件/边界依据与G/E校准在review/。局部范围明示，不把变动单元自查当六章再次全文接受。figure_audit按root分派进行独立复核，其反馈不在这份作者结论内。

行政检查：标题/顺序/input/scite/图路径宽度不变，恰4授权thm标签退役，无新label，begin/end成对；补丁实际应用到ignored scratch并逐字还原12候选。没有用这些机械检查替代语义审查。根正式应用后的SHA绑定、全书构建/测试/书页验证、最终提交推送仍需root执行。

可复制文件集见handoff-manifest.json，含真实before/candidate各版快照、目标源、补丁与所有记录。678仅是tex/plans归档全部文件数；正式入站扫描范围是223.tex+118.md=341，详见inbound-rebased-tex-md-scope.json，不误记为678份正文。
