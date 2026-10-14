# CH05 共享修复请求

- 日期：2026-10-13；正文对应修订摘要见`repair.md`。本代理未修改任何共享文件；下列由主代理串行决定并验证。

## 词典

- `tex/index-terms.tex` 搜索六个名称及其对应中文均无登记。本章先用普通中英文字写足首现，未发明未知词典宏。请登记或与全书既有别名统一后接入。

|中文显示|英文/专名|首现位置|建议|
|---|---|---|---|
|基于搜索的结构化预测|search-based structured prediction；SEARN|`sec:rl-reward-bc-dagger`，L233|保SEARN方法专名，不编造逐字母全称。|
|聚合价值模仿|Aggregate Values to Imitate；AggreVaTe|同上|大小写与作者命名相同。|
|通过评价强化手动训练智能体|Training an Agent Manually via Evaluative Reinforcement；TAMER|`sec:rl-reward-preference`，L354|本章已保人工评分对象。|
|条件风险价值|conditional value-at-risk；CVaR|`sec:rl-reward-shaping`，L673|与可信章统一中文；本章以损失上尾解释回报较差方向。|
|事后经验回放|hindsight experience replay；HER|`sec:rl-reward-auxiliary`，L715|本章只作迁移章入口；主代理避免重复登记别名。|
|解耦剪裁与动态采样策略优化|Decoupled Clip and Dynamic sAmpling Policy Optimization；DAPO|`sec:rl-reward-joint-update`，L955|明确区别同缩写的Direct Advantage-Based Policy Optimization。|

## 引文

- 本轮没有新增 `scite` key、没有改既有引用目标。IQ/AIRL/SEARN/AggreVaTe/TAMER/DAPO现有key可用；精确一手位置与版本见`sources.md`。
- CVaR首现本次只补名称和损失方向，没有新增其完整定义；如主代理要求就地补出处，请使用已核的Rockafellar与Uryasev `Optimization of Conditional Value-at-Risk`，先检查共享库是否已有对应key，禁止未经检查新造key。本代理未修改库。
- HER作者论文 `1707.01495`，已有 `rl6-andrychowicz2017-her` 在后章使用；本章保原未来入口，未加入新引文。主代理可按全书引用规范决定是否在此补已有key。

## 验证

- 本章新增4组无编号展示式（IQ总体/经验目标，AIRL来源似然/对数几率信号）。需要主代理集成后检查公式断行、长英文首现、表格列宽和页数；本代理按禁令没有构建/PDF验证。
- 9图的本轮图注已读，图源没有重核也没有修改；旧R1/R3图源记录保留，但不冒称本代理新稿复核已包含图源。请最终独立复核明确图源及版面范围。
