# 计划与结构索引

全书按[十二卷结构](book-structure.md)独立出版，不生成全集，每卷总页数不超过600页。当前正文入口接入87章：数学两卷9章与8章，基础17章，经典模型6章，神经网络10章，概率图模型15章，强化学习8章，知识学习14章。三卷应用只有分部入口与27章大纲，系统尚无章纲。当前分支的入口是完成状态依据，其他 worktree 的变更需另行集成。

## 现行结构与正文大纲

| 范围 | 文档 | 当前组织 |
| --- | --- | --- |
| 全书 | [卷目与分部](book-structure.md) | 十二卷；目录元数据为 `tex/volumes.json` |
| 数学准备（上、下） | [阅读结构](mathematical-preliminaries-reading-structure.md)、[章目映射](mathematical-preliminaries-chapter-map.md) | 各三部分，9章与8章 |
| 空间与几何 | [空间三章大纲](spaces-and-geometry-outline.md) | 卷一第5—7章 |
| 数学与机器学习 | [综合章职责](chapter17-learning-framework-outline.md) | 卷二第8章；保留标签兼容契约 |
| 基础、理论与可信性 | [引言](introduction-outline.md)、[模型简介](machine-learning-models-outline.md)、[范式简介](machine-learning-paradigms-outline.md)、[理论大纲](learning-theory-outline.md) | 卷三三部分17章 |
| 经典模型 | [卷级大纲](classic-models-outline.md) | 卷四六章，不设部分 |
| 神经网络模型 | [卷级大纲](neural-network-models-outline.md) | 卷五九章，不设部分 |
| 概率图模型 | [卷级大纲](probabilistic-graphical-models-outline.md) | 卷六表示、推断、学习、模型四部分14章 |
| 强化学习 | [卷级大纲](reinforcement-learning-outline.md) | 卷七三部分8章 |
| 知识学习 | [获取大纲](efficient-knowledge-use-outline.md)、[演进与迁移大纲](knowledge-evolution-and-transfer-outline.md) | 卷八获取、演进、迁移三部分14章 |

## 尚待起草

| 卷 | 大纲 | 部分与规划章数 |
| --- | --- | --- |
| 九：自然语言处理 | [大纲](natural-language-processing-outline.md) | 文本分析与信息组织；文本生成与交互；语音处理，共8章 |
| 十：图像和多模态处理 | [大纲](image-processing-outline.md) | 图像处理；视频处理；多模态处理，共9章 |
| 十一：推荐、搜索与广告 | [大纲](recommendation-and-search-outline.md)、[架构](recommendation-and-search-architecture.md) | 理解、选择与展示；决策与评价；搜索与广告，共10章 |
| 十二：系统 | [职责](book-structure.md) | 本轮保留现有入口，不规划内部结构 |

## 选材与待办

- [自然语言处理文献地图](natural-language-processing-literature.md)、[图像处理文献地图](image-processing-literature.md)、[推荐与搜索文献地图](recommendation-and-search-literature.md)保留检索截止日期和来源，供起草时核对。
- [推荐与搜索研究课题](recommendation-and-search-research-topics.md)与应用大纲配套。
- [数学依赖待办](mathematical-dependencies.md)保存尚待补充的通用接口和后卷桥接，完成后复核实际使用。
- [综合章标签退役契约](chapter17-retired-labels.json)保留原章17的历史基线与标签清单，当前正文位置为卷二第8章；审计仍依赖该文件。

正文变化时同步大纲、编号与入口映射。已完成的过程讨论和一次性构建记录不作为当前计划保留，历史由 Git 保存；图源、数据、生成记录和有效校验契约继续保留。
