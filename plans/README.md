# 计划与结构索引

本目录只保存当前开发仍需要的结构、大纲、选材资料和未完成任务。状态按当前分支的正文入口确认；其他 worktree 中的草稿不等于已集成正文。全集共有六卷、19个部分，当前接入63章：第一卷17章、第二卷17章、第三卷29章，第四至六卷只有部分入口。部分号和章号由出版单元生成，详细大纲中的章次均为部分内部定位；基础三章大纲使用第二卷局部章号。

## 已接入正文的结构

| 范围 | 当前文档 | 状态与用途 |
| --- | --- | --- |
| 全书 | [六卷结构](book-structure.md) | 出版单元、内容边界与部分目录 |
| 数学准备 | [阅读结构](mathematical-preliminaries-reading-structure.md)、[章目映射](mathematical-preliminaries-chapter-map.md) | 六部分17章，使用现行编号与源文件路径 |
| 数学与后续研究 | [第17章职责](chapter17-learning-framework-outline.md) | 统一框架和六类分析关系；九节，含独立小结 |
| 机器学习基础 | [引言](introduction-outline.md)、[模型简介](machine-learning-models-outline.md)、[范式简介](machine-learning-paradigms-outline.md) | 第二卷前三章的现行安排 |
| 机器学习理论 | [部分大纲](learning-theory-outline.md) | 六章；全集21—26章，第二卷单卷4—9章 |
| 可信性 | [六卷结构](book-structure.md)中的内容边界 | 八章；具体节次以 `tex/02-foundations/03-trustworthiness/` 为准 |
| 经典模型 | [部分大纲](classic-models-outline.md) | 六章；集成学习包含 `ensemble-learning/` 中由章入口调用的节文件 |
| 神经网络模型 | [部分大纲](neural-network-models-outline.md) | 九章；模型、训练与泛化分工 |
| 概率图模型 | [部分大纲](probabilistic-graphical-models-outline.md) | 十四章；表示、推断、学习与典型模型 |

## 尚待实施的大纲

| 部分 | 大纲 | 规划章数 |
| --- | --- | --- |
| 强化学习 | [部分大纲](reinforcement-learning-outline.md) | 8 |
| 知识的获取 | [部分大纲](efficient-knowledge-use-outline.md) | 7 |
| 知识的演进与迁移 | [部分大纲](knowledge-evolution-and-transfer-outline.md) | 7 |
| 自然语言处理 | [部分大纲](natural-language-processing-outline.md) | 8 |
| 图像处理 | [部分大纲](image-processing-outline.md) | 9 |
| 推荐与搜索 | [部分大纲](recommendation-and-search-outline.md) | 10 |

系统卷尚未设置详细章纲，职责见[六卷结构](book-structure.md)。新增章节时检查实际入口，再更新本表及大纲开头的完成状态。

## 选材与未完成任务

- [自然语言处理文献地图](natural-language-processing-literature.md)、[图像处理文献地图](image-processing-literature.md)、[推荐与搜索文献地图](recommendation-and-search-literature.md)：保留检索截止日期与一手来源，供后续写作核对，不表述为持续更新的领域全貌。
- [推荐与搜索研究课题](recommendation-and-search-research-topics.md)、[应用架构](recommendation-and-search-architecture.md)：分别说明任务分类和模块关系，与部分大纲配套使用。
- [数学依赖待办](mathematical-dependencies.md)：保留尚待补充的通用接口和后卷桥接，完成后复核实际使用并移除对应条目。
- [第17章标签退役契约](chapter17-retired-labels.json)：结构审计仍使用的兼容性数据。历史基线和标签清单是检查输入，不是当前章纲；不得作为普通过程材料删除。

## 维护方式

已完成的讨论稿、阶段审读和发布记录不继续放在 `plans/` 充当当前计划，历史从 Git 查询。当前目录不重复维护旧章号与现行章号两套细纲，也不保存带失效行号的全书覆盖矩阵。仍有效的任务先收拢到待办，再移除过程文档。正文、大纲、说明和审计工具的依赖必须一起更新。
