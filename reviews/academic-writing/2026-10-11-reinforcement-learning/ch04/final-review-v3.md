# 第4章索引映射闭环复核 v3

记录：`CH04-FR3-20261014-v3`。角色：未参与第4章正文、词典、审计脚本及
v1/v2记录修改的独立复核者。

## 受审对象与边界

- worktree：`/Users/bytedance/Projects/notes_on_machine_learning/.worktrees/docs-reinforcement-learning-content`
- branch：`docs/reinforcement-learning-content`
- HEAD：`75175dea03ad6c4d9b20299835b48c087a052505`
- 当前正文：`tex/04-paradigms/01-reinforcement-learning/04-information.tex`
- 正文 SHA-256：`48662ad427b731f34719cc9ce7706881eb869593b79409466c6601e4b8cfac7a`
- 当前词典：`tex/index-terms/04-paradigms.tex`
- 词典 SHA-256：`d9095a5a6b23417fa9986c467e7fae9cec2568ad7578961efa875898c29bf0ca`
- 当前审计脚本：`scripts/audit_index_terms.py`
- 脚本 SHA-256：`b87d4ccaeea7a303a518d7c1b7905c5ac34a3382c2a8faca232778396bc299e5`

本轮完整读取了 `specs/latex.md`、`specs/writings.md`、当前第4章正文、
当前第4卷词典、`final-review-v1.md`、`final-review-v2.md` 和
`shared-repair-requests.md`。复核问题限定为九个英文专名的正文首现、
词典归属及 `CH04-FR1-01` 闭环；不修改正文、词典、脚本或构建产物。

## 规则判定

`specs/latex.md` 要求普通双语词条集中登记，同时明确“纯英文完整名称和数学词
可以不登记”。当前审计脚本进一步将这一边界实现为：

- 含中文的普通显示词缺少映射时报 `MISSING_MAPPING`；
- 全大写形式的缩写缺少展开时报 `MISSING_ABBREVIATION_EXPANSION`；
- 不含中文且不属于上述缩写形式的完整英文、专名或数学词若有映射，反而报
  `UNEXPECTED_ENGLISH_MAPPING`，并要求保持未映射。

九项显示词均不含中文，也都不匹配脚本的全大写缩写形式。因此，它们属于必须
保持未映射的完整英文/专名，而不是缺少集中登记的中文词条或缩写。

## 正文首现复核

| 位置 | 显示词 | 首现所给英文或职责说明 | 结论 |
| --- | --- | --- | --- |
| L278 | `GTrXL` | 给出 `Gated Transformer-XL`，说明在Transformer-XL中引入门控等结构以适配强化学习优化 | 充分 |
| L610 | `DualDICE` | 给出 `Dual stationary DIstribution Correction Estimation`，说明以对偶优化求解分布校正问题 | 充分 |
| L747 | `ReBRAC` | 给出 `Revisited BRAC`，说明分别调节行动者与评论家目标中的行为惩罚 | 充分 |
| L765 | `Decision Transformer` | 专名本身完整；说明它是回报条件序列模型及其输入、训练目标和部署条件 | 充分 |
| L878 | `Diffusion-QL` | 给出 `Diffusion Q-learning`，说明扩散动作建模与Q学习的结合及价值梯度路径 | 充分 |
| L920 | `MOReL` | 给出 `Model-Based Offline Reinforcement Learning`，说明以低回报吸收状态限制不可信区域 | 充分 |
| L940 | `Trajectory Transformer` | 专名本身完整；说明它是轨迹序列预测模型及束搜索、首动作执行和重规划职责 | 充分 |
| L941 | `Diffuser` | 专名不是缩写；说明用回报引导的扩散采样生成轨迹计划并滚动重规划 | 充分 |
| L1013 | `Cal-QL` | 给出 `Calibrated Q-Learning`，说明校准Q价值尺度并排除概率校准误读 | 充分 |

这些首现不是只列方法名：每项均给出英文展开或中文机制、输入输出、限制位置或
边界说明。`shared-repair-requests.md` 对英文专名“不另造中文方法译名”的要求也
得到保留。因此，移除词典映射不影响正文首现解释，不需要重新打开
`CH04-R3-02`。

## 源级索引审计

本轮只读调用 `collect_terms`、`parse_mappings`、`parse_aliases`、`audit` 和
`audit_statistics`，不调用产物审计，结果为：

```text
SOURCE_SUMMARY calls=2526 unique=2172 mappings=2120 aliases=2 errors=0
```

九项各自的源级结果均为 `mappings=0`、`cjk=False`、
`abbreviation=False`。对全部 `tex/index-terms/*.tex` 的精确声明搜索也未找到
这九项；这正是当前规则要求的状态，不是缺口。

标准 `python3 scripts/audit_index_terms.py check` 还会读取 `build/*.idx` 与
`build/*.ind`。本轮执行时返回
`FATAL build/main.idx:952:1: unclosed index entry argument`；同时现存
`build/04-paradigms.idx`、`build/04-paradigms.ind` 仍显示九项旧双语条目。
检查期间 `build/main.idx` 的大小与修改时间继续变化，故产物集合不是稳定的当前
源快照。该结果只说明产物级暂不可判定，不能推翻零错误的源级审计。本轮未构建，
也未据此修改任何产物。

## CH04-FR1-01 闭环

v1 将“九项没有 `\DeclareBookIndexTerm`”解释为违反集中登记要求。该判断遗漏了
同一规范对完整英文/专名的豁免，也与当前审计脚本的强制分类相反。当前词典哈希
正是 v2 所恢复的改前哈希 `d9095a...f0ca`；在这个原状态上，正文首现解释充分，
源级索引审计为零错误。反证存在于原版本本身，无须制造正文或词典修改。

`CH04-FR1-01` 状态应为：**有据撤销确认**，不是仍需修复，也不是通过增加九条
映射来关闭。

## v2 失效原因

v2 绑定词典 SHA-256 `9aece507...f15621`，其关闭依据是九条后来加入的普通词典
声明。当前词典已恢复为 `d9095a5a...bf0ca`，所以 v2 的受审输入不再存在；当前
`final-input-manifest.json` 仍记录旧词典哈希和字节数，也不能绑定当前词典。

更重要的是，v2 把“九项均有且仅有一条声明”视为正确状态，而现行规范和脚本要求
这些完整英文/专名保持未映射。若在当前规则下恢复九条声明，会产生九项
`UNEXPECTED_ENGLISH_MAPPING`。因此，v2 关于 `CH04-FR1-01` 的“修改后复核关闭”
路径及其源级映射结论已经失效；其对未变正文所继承的覆盖材料不因此失效。

## 当前结论

- 记录结论：可接受；v1 的索引新发现属于规则误用，v2 的修复式闭环不再适用于当前输入。
- `CH04-FR1-01`：有据撤销确认。
- 当前正文 SHA-256 与 v1/v2 绑定的正文相同，v1 的完整 C/P/W、特殊单元和专项覆盖仍可追溯；本轮完整顺读未发现九项首现解释的新缺口。
- 正文结论：**在原声明范围内通过**。
- 产物结论：暂不可判定。未构建、未检查最终PDF或稳定索引成品，不把源级通过扩大为版面或产物级通过。
- 本轮未修改正文、词典、脚本或构建产物，未暂存、提交、推送或集成。
