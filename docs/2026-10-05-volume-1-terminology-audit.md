# 第一卷术语审计

本表记录第一卷中需要跨章保持一致的专业术语。首次出现位置按当前章节标题和节标题描述；普通中文词语、只在单一局部推导中使用的符号名称不纳入本表。

| 中文术语 | 英文名称 | 缩写 | 首次出现位置 | 状态 |
| --- | --- | --- | --- | --- |
| 机器学习 | machine learning | ML | 第1章“从学习到机器学习” | 已核对，首次定义完整 |
| 模型 | model | - | 第1章“对问题进行建模” | 已核对，后文与“学习算法”分开使用 |
| 模型参数 | model parameters | - | 第1章“对问题进行建模” | 已核对 |
| 假设空间 | hypothesis space / hypothesis class | - | 第1章“对问题进行建模” | 中文统一；建模部分使用 hypothesis space，学习理论使用 hypothesis class |
| 归纳偏置 | inductive bias | - | 第1章“对问题进行建模” | 已核对 |
| 经验风险最小化 | empirical risk minimization | ERM | 第1章“对问题进行建模” | 已核对 |
| 泛化 | generalization | - | 第1章“模型的评估” | 已核对 |
| 独立同分布 | independent and identically distributed | i.i.d. | 第1章“经验” | 已核对 |
| 监督学习 | supervised learning | - | 第3章“监督学习” | 已核对 |
| 无监督学习 | unsupervised learning | - | 第3章“无监督学习” | 已核对 |
| 强化学习 | reinforcement learning | RL | 第3章“强化学习” | 已核对；正文首次出现未强制使用缩写 |
| 间隔 | margin | - | 第2章“样本到分类边界的间隔” | 已补英文；后文按对象使用“分类间隔”或“几何间隔” |
| PAC学习 | probably approximately correct learning | PAC | 第4章“PAC学习” | 已核对 |
| VC维 | Vapnik--Chervonenkis dimension | VC | 第5章“打散和VC维” | 已核对 |
| Rademacher复杂度 | Rademacher complexity | - | 第5章“Rademacher复杂度” | 已核对 |
| Natarajan维 | Natarajan dimension | - | 第6章“从二分类到多分类” | 已补英文 |
| 图维 | graph dimension | - | 第6章章首 | 已补英文 |
| DS维 | Daniely--Shalev-Shwartz dimension | DS | 第6章章首 | 已补英文 |
| 算法稳定性 | algorithmic stability | - | 第7章章首 | 已补英文 |
| 迁移学习 | transfer learning | - | 第3章“迁移学习” | 已核对 |
| 源域 | source domain | - | 第3章“迁移学习” | 已核对 |
| 目标域 | target domain | - | 第3章“迁移学习” | 已核对 |
| 领域自适应 | domain adaptation | DA | 第3章“迁移学习” | 主称已统一为“领域自适应”；首次出现保留“领域适应”别名 |
| 领域泛化 | domain generalization | DG | 第3章“迁移学习” | 已核对 |
| 可信机器学习 | trustworthy machine learning | - | 第10章章首 | 已核对 |
| 可靠性 | reliability | - | 第11章章首 | 已补英文 |
| 鲁棒性 | robustness | - | 第12章章首 | 已核对 |
| 公平性 | fairness | - | 第13章“公平性的含义” | 已核对 |
| 目标对齐 | alignment | - | 第14章“目标对齐与行为约束的含义” | 已核对 |
| 行为约束 | behavioral constraint | - | 第14章“目标对齐与行为约束的含义” | 已补英文 |
| 可解释性 | interpretability | - | 第15章章首 | 已核对 |
| 隐私保护 | privacy protection | - | 第16章“保护对象与保护范围” | 已补英文 |
| 对抗安全 | adversarial security | - | 第17章章首 | 已补英文 |
| 对抗攻击 | adversarial attack | - | 第17章“对抗攻击及其典型表现” | 已核对 |
| 数据投毒 | data poisoning | - | 第17章“对抗攻击及其典型表现” | 已核对 |
| 后门 | backdoor | - | 第17章“对抗攻击及其典型表现” | 已补英文，并与数据投毒的操作过程区分 |

审计结论：

- 第一卷关键术语的中文名称、英文名称与常用缩写已经核对。
- “假设空间”对应两种常见英文表达，正文按建模与学习理论语境保留差异，中文名称不变。
- “领域自适应”已作为全卷主称，“领域适应”只在首次出现时作为别名保留。
- “间隔”和“后门”的首次双语对照已经补齐。
