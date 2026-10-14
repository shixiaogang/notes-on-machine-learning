# 第7章共享串行修复请求

## CH07-SR-01：集成稿词典复核

- 类型：词典；不请求新增文献。
- 原因：当前任务禁止修改共享`tex/index-terms/`。本工作区的`tex/index-terms/04-paradigms.tex`为空，而第7章冻结稿已经调用多项尚未在本工作区词典登记的`\term`。主代理的`SH02`称集成词典已登记基线首现词，集成时仍须对最终第7章重新审计。
- 请核对并按集成稿首次出现位置登记以下现有正文词条：
  - `完全合作` / `fully cooperative`
  - `两人零和` / `two-player zero-sum`
  - `一般和` / `general-sum`；注意现有词典只有`一般和博弈` / `general-sum game`，显示词不一致。
  - `部分可观测随机博弈` / `partially observable stochastic game`
  - `分散部分可观测马尔可夫决策过程` / `decentralized POMDP`
  - `集中训练、分散执行` / `centralized training with decentralized execution`
  - `差分奖励` / `difference reward`
  - `个体与整体最大化一致性` / `individual-global-max`
  - `策略空间响应预言机` / `policy-space response oracles`
  - `零样本协调` / `zero-shot coordination`
  - `临时团队协作` / `ad hoc teamwork`
- 本轮新增的`\term{混合策略}`已有`mixed strategy`映射，无需新增。
- `随机博弈`、`自我对弈`、`平均场多智能体强化学习`等中英首现已在正文统一，但当前未新增`\term`调用；是否纳入主题词索引由主代理按全书首次出现和词典策略串行决定。
- CommNet、QMIX、QTRAN、QPLEX、LOLA、Other-Play、SMAC、MPE等为英文专名或缩写，本轮未强造中文索引词。

## 引用

- 本轮没有新增引用键或新增文献需求。
- FACMAC、MPE、CommNet及其余方法名称继续使用冻结稿已有的一手文献键；最终集成只需按既定来源审计复核，无需本章代理修改`tex/references.bib`。
