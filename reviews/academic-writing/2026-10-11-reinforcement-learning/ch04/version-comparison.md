# 第4章最终版本对照

CH04-REPAIR，2026-10-13；机械比较只证明枚举与字节关系，不产生语义接受。
B=`rewrite-v1.tex`，SHA-256
`b93de38ccbd71003d1a8e88b44cb46a8dcb11912a4a2a57c58ef63aa4901e503`。
F=`final-v1.tex`及实际正文，SHA-256
`a2517965081adba83a105cc62f101a02131237234e9744df46fe4e97e27c5cfa`。
B1264行，F1270行；均基于冻结旧出版入口。

## 标题

30个标题命令逐字内容和顺序一致，无新增/删除/改名。
1章、7节、22小节；没有subsubsection/paragraph命令。
下表B→F行号为命令位置，不是PDF章号。

| 级别 | 标题 | B→F |
| --- | --- | --- |
| 章 | 信息受限下的强化学习 | 1→1 |
| 节 | 两类信息限制 | 16→16 |
| 小节 | 决策所依据的状态信息 | 20→20 |
| 小节 | 学习能够访问的经验 | 46→46 |
| 小节 | 观测完整性与数据访问权的组合 | 75→75 |
| 节 | 决策信息不完整下的强化学习 | 98→98 |
| 小节 | 从当前观测扩展为观测历史 | 102→102 |
| 小节 | 将观测历史压缩为决策状态 | 133→133 |
| 小节 | 新观测到来后的决策状态更新 | 210→210 |
| 小节 | 基于决策状态的策略求解与动作选择 | 275→281 |
| 小节 | 近似决策状态的误差与计算边界 | 331→337 |
| 节 | 固定经验下的策略评价与选择 | 373→379 |
| 小节 | 固定经验与行为策略 | 377→383 |
| 小节 | 策略价值的可识别性与覆盖条件 | 426→432 |
| 小节 | 离线策略价值的估计 | 485→491 |
| 小节 | 候选策略的比较与选择 | 636→642 |
| 节 | 固定经验下的策略学习与改进 | 675→681 |
| 小节 | 策略学习的目标与数据边界 | 679→685 |
| 小节 | 行为数据约束下的策略学习 | 703→709 |
| 小节 | 价值估计与策略更新中的外推控制 | 769→775 |
| 小节 | 学习模型上的规划与策略优化 | 887→893 |
| 小节 | 策略改进的保证与比较 | 940→946 |
| 节 | 有限新增经验下的策略修正 | 999→1005 |
| 节 | 两类信息限制叠加时的强化学习 | 1054→1060 |
| 小节 | 两类限制下的决策目标与可用信息 | 1058→1064 |
| 小节 | 策略结论的可识别程度 | 1092→1098 |
| 小节 | 完全可识别时的历史表示与决策学习 | 1156→1162 |
| 小节 | 部分可识别时的历史表示与决策学习 | 1185→1191 |
| 小节 | 不可识别时的学习边界与信息补充 | 1227→1233 |
| 节 | 本章小结 | 1257→1263 |

## 标签

97个label名称和顺序逐个一致；下列全部按原顺序给B→F命令行。

| 标签 | B→F |
| --- | --- |
| chap:rl-information | 2→2 |
| fig:rl-information-roadmap | 12→12 |
| sec:rl-information-limits | 17→17 |
| sec:rl-information-state-information | 21→21 |
| def:rl-information-history | 26→26 |
| ex:rl-information-cue | 37→37 |
| sec:rl-information-data-access | 47→47 |
| def:rl-information-access | 52→52 |
| tab:rl-information-access | 71→71 |
| sec:rl-information-two-axes | 76→76 |
| tab:rl-information-two-axes | 92→92 |
| sec:rl-information-partial-observation | 99→99 |
| sec:rl-information-history-policy | 103→103 |
| def:rl-information-pomdp | 108→108 |
| fig:rl-information-aliasing | 127→127 |
| sec:rl-information-sufficiency | 134→134 |
| def:rl-information-belief | 139→139 |
| thm:rl-information-belief-sufficient | 155→155 |
| tab:rl-information-sufficiency | 206→206 |
| sec:rl-information-filtering | 211→211 |
| eq:rl-information-bayes | 216→216 |
| eq:rl-information-predict-correct | 227→227 |
| eq:rl-information-kalman | 242→243 |
| ex:rl-information-kalman | 254→260 |
| fig:rl-information-memory | 266→272 |
| sec:rl-information-belief-control | 276→282 |
| eq:rl-information-belief-bellman | 283→289 |
| ex:rl-information-tiger | 293→299 |
| fig:rl-information-tiger | 319→325 |
| sec:rl-information-memory-errors | 332→338 |
| tab:rl-information-memory-cost | 351→357 |
| sec:rl-information-evaluation | 374→380 |
| sec:rl-information-logging | 378→384 |
| def:rl-information-behavior | 383→389 |
| tab:rl-information-fields | 414→420 |
| sec:rl-information-coverage | 427→433 |
| def:rl-information-identifiability | 432→438 |
| thm:rl-information-unseen-action | 437→443 |
| def:rl-information-support | 452→458 |
| tab:rl-information-claims | 479→485 |
| sec:rl-information-estimators | 486→492 |
| eq:rl-information-weights | 496→502 |
| eq:rl-information-is | 505→511 |
| ex:rl-information-ope-data | 515→521 |
| eq:rl-information-fqe | 545→551 |
| ex:rl-information-fqe-dr | 559→565 |
| eq:rl-information-dr | 590→596 |
| eq:rl-information-dice | 607→613 |
| tab:rl-information-estimators | 630→636 |
| sec:rl-information-selection | 637→643 |
| eq:rl-information-paired | 645→651 |
| ex:rl-information-paired | 658→664 |
| fig:rl-information-comparison | 669→675 |
| sec:rl-information-offline-learning | 676→682 |
| sec:rl-information-learning-boundary | 680→686 |
| ex:rl-information-extrapolation | 689→695 |
| fig:rl-information-offline-pipeline | 699→705 |
| sec:rl-information-behavior-constraint | 704→710 |
| eq:rl-information-td3bc | 708→714 |
| eq:rl-information-bcq | 727→733 |
| tab:rl-information-behavior-methods | 756→762 |
| ex:rl-information-return-conditioning | 762→768 |
| sec:rl-information-pessimism | 770→776 |
| eq:rl-information-cql | 775→781 |
| eq:rl-information-expectile | 794→800 |
| eq:rl-information-iql | 803→809 |
| ex:rl-information-iql | 819→825 |
| alg:rl-information-iql | 836→842 |
| tab:rl-information-extraction | 869→875 |
| fig:rl-information-extraction | 881→887 |
| sec:rl-information-model-learning | 888→894 |
| eq:rl-information-model-telescoping | 897→903 |
| tab:rl-information-model-methods | 931→937 |
| sec:rl-information-improvement | 941→947 |
| thm:rl-information-improvement | 946→952 |
| tab:rl-information-reporting | 993→999 |
| sec:rl-information-limited-interaction | 1000→1006 |
| tab:rl-information-finetuning | 1022→1028 |
| alg:rl-information-round | 1028→1034 |
| ex:rl-information-batches | 1045→1051 |
| sec:rl-information-combined | 1055→1061 |
| sec:rl-information-combined-target | 1059→1065 |
| tab:rl-information-information-sets | 1079→1085 |
| def:rl-information-decision-equivalence | 1085→1091 |
| sec:rl-information-identification-levels | 1093→1099 |
| def:rl-information-identified-set | 1100→1106 |
| fig:rl-information-confounding | 1122→1128 |
| ex:rl-information-confounding | 1126→1132 |
| sec:rl-information-full-identification | 1157→1163 |
| eq:rl-information-history-is | 1165→1171 |
| sec:rl-information-partial-identification | 1186→1192 |
| thm:rl-information-partial-order | 1195→1201 |
| ex:rl-information-partial-order | 1210→1216 |
| fig:rl-information-identification-width | 1223→1229 |
| sec:rl-information-unidentifiable | 1228→1234 |
| tab:rl-information-information-repair | 1249→1255 |
| sec:rl-information-summary | 1258→1264 |

## 展示式与引用

- F01-F43各块独立字节比较均相同，位置与逐式语义在SPECIAL表；
  没有新增/删除/修改展示数学块，不能据此说新增行内条件毫无实质变化。
- 新行内数学/条件为反馈集合、Kalman形状/e/S/cross/正规关系及跨时条件、
  DICE全部测试域/收缩唯一性/受限误差，逐项已在`repair.md`记录。
- 32个scite调用目标全序列一致，61个ref、1个eqref、9个input调用亦一致。
  没有新增/删除/替换文献目标或图输入，没有共享入口修改。
- `git diff --check`无输出；它只查已跟踪差异的空白，不检查未跟踪评审
  材料的真实覆盖，不证明数学、引用渲染或PDF版面接受。

最终可恢复快照与正文同字节，结构冻结要求满足机械对照；
语义自查见各覆盖文件，最终接受仍须独立复核。
