# 正文大纲索引

本目录按 `tex/volumes.json` 的十二卷登记组织。每个设有部分的卷按部分保存一份大纲；卷四与卷五不设部分，各保存一份卷级大纲。卷目录名称与 `tex/` 对应目录一致。

大纲以 `volume.tex → part.tex → 章节及章内输入` 的实际接入顺序为准：章号在卷内连续，保留正文层级，每节及下级小节均说明主要内容、论证依据和表述逻辑。正文与旧规划不一致时采用正文；未接入的拟设章节不作为现有内容。当前共147章；卷九接入15章，卷十接入15章，卷十一接入10章，卷十二仅有部分入口，尚无章节正文。

| 卷 | 卷名 | 正文章数 | 部分与大纲 |
| --- | --- | --- | --- |
| 1 | 数学准备：计算、分析与几何 | 27 | [数学对象、计数与极限](01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization.md)；[线性空间](01-mathematical-preliminaries-upper/03-linear-spaces.md)；[微积分](01-mathematical-preliminaries-upper/04-calculus.md)；[最优化](01-mathematical-preliminaries-upper/05-optimization.md)；[空间与几何](01-mathematical-preliminaries-upper/06-space-and-geometry.md)；[信号](01-mathematical-preliminaries-upper/07-signals.md)；[图](01-mathematical-preliminaries-upper/08-graphs.md) |
| 2 | 数学准备：概率、因果与决策 | 10 | [随机变量、分布与因果响应](02-mathematical-preliminaries-lower/01-random-variables-distributions-and-causality.md)；[演化、控制、决策与博弈](02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games.md)；[数学与机器学习](02-mathematical-preliminaries-lower/03-mathematics-and-machine-learning.md) |
| 3 | 基础、理论与可信性 | 17 | [机器学习基础](03-foundations/01-basics.md)；[机器学习理论](03-foundations/02-learning-theory.md)；[机器学习可信性](03-foundations/03-trustworthiness.md) |
| 4 | 模型：经典模型 | 6 | [模型：经典模型](04-classic-models/outline.md) |
| 5 | 模型：神经网络模型 | 10 | [模型：神经网络模型](05-neural-network-models/outline.md) |
| 6 | 模型：概率图模型 | 15 | [表示](06-probabilistic-graphical-models/01-representation.md)；[推断](06-probabilistic-graphical-models/02-inference.md)；[学习](06-probabilistic-graphical-models/03-learning.md)；[模型](06-probabilistic-graphical-models/04-models.md) |
| 7 | 学习范式：强化学习 | 8 | [基本问题与求解](07-reinforcement-learning/01-problems-and-solving.md)；[信息与奖励受限的学习](07-reinforcement-learning/02-information-and-reward.md)；[任务扩展与可信决策](07-reinforcement-learning/03-task-expansion-and-trustworthiness.md) |
| 8 | 学习范式：知识的获取、演进与迁移 | 15 | [知识的获取](08-knowledge-learning/01-knowledge-acquisition.md)；[知识的演进](08-knowledge-learning/02-knowledge-evolution.md)；[知识的迁移与共享](08-knowledge-learning/03-knowledge-transfer.md) |
| 9 | 应用：自然语言处理 | 15 | [语言模型](09-natural-language-processing/01-language-models.md)；[文本分析与信息组织](09-natural-language-processing/02-text-analysis-and-organization.md)；[文本生成与交互](09-natural-language-processing/03-text-generation-and-interaction.md)；[语音处理](09-natural-language-processing/04-speech-processing.md) |
| 10 | 应用：图像和多模态处理 | 15 | [图像和多模态基础（6章）](10-image-and-multimodal-processing/01-image-and-multimodal-foundations.md)；[图像和多模态模型（2章）](10-image-and-multimodal-processing/02-image-and-multimodal-models.md)；[图像处理（3章）](10-image-and-multimodal-processing/03-image-processing.md)；[视频处理（2章）](10-image-and-multimodal-processing/04-video-processing.md)；[多模态处理（2章）](10-image-and-multimodal-processing/05-multimodal-processing.md) |
| 11 | 应用：推荐、搜索与广告 | 10 | [理解、选择与展示](11-recommendation-search-advertising/01-understanding-selection-and-display.md)；[决策与评价](11-recommendation-search-advertising/02-decision-and-evaluation.md)；[搜索与广告](11-recommendation-search-advertising/03-search-and-advertising.md) |
| 12 | 系统 | 0（仅部分入口） | [机器学习系统](12-systems/01-machine-learning-systems.md) |

卷十共15章、5部分。图像和多模态基础部分接入概述、图像的形成与表示、图像的变换与滤波、图像的特征与分割、视频的表示与运动、多模态数据的对齐与融合六章；图像和多模态模型部分接入图像与视频模型、多模态模型两章；图像处理部分接入图像识别与检索、图像复原增强压缩及图像生成编辑三章；视频处理接入视频感知跟踪检索及视频复原增强压缩两章；多模态处理接入多模态理解及多模态生成两章。各部分的不编号阅读指引不计入章数。

正文位置均通过相对链接给出。旧卷级规划、选材资料、研究课题、过程记录及重复映射已从本目录移除，历史可由 Git 查阅。仍被数学审计使用的历史章目映射和标签退役契约迁至 `tests/fixtures/math-reading-structure/`；它们用于校验，不承担正文规划职责。

目录与维护要求见[正文大纲与计划目录规范](../specs/plans.md)。每次修改正文都须核对相应部分或卷的大纲，保持标题、顺序和主要段落提要一致；内容、条件或结论变化时，即使标题未变也须同步提要。涉及卷、部分或章数变化时同步本索引，正文与相应大纲作为同一项变更交付与提交。各卷独立出版，不生成全集。
