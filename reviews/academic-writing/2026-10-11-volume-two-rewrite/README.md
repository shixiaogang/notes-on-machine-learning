# 卷二改写与 academic-writing 审查记录

## 范围与版本

本任务以 `17b2ded1e4e336e1c9751e980ff47f30c6190458` 为基线，按现有大纲改写卷二的 17 章与三份部分导读。章节、小节、图源和组成入口保持原有组织；每章仍保留独立的“本章小结”。正文改写包括概念引入、方法讲解、示例说明、图注、承接和小结，审查后修正含混条件、比较口径、指标方向和压缩表达。

最终交付正文以 [composition.json](composition.json) 列出的 24 个实际输入为准；其中 17 个章文件、三个导读文件及四个组成入口均保存在 [final/](final/) 下，并逐文件记录 SHA-256。各分项记录保留审查时的冻结稿与修改稿，不能把早期稿的 SHA 当作最终正文 SHA。

任务工作区：`.worktrees/volume-two-adjustments`；分支：`codex/volume-two-adjustments`。本轮改写、审查和构建均在该工作区执行。提交与集成状态以阶段交付记录为准。

## 审查方法与覆盖

各章按 C（连续读完整章、检查 C1–C4）、P（逐段检查 P1–P5）和 W（逐句落地句义、检查 W1–W6）的顺序审读。记录同时覆盖七项门槛、E1–E12 校准、关键入口、方法链和核心公式的解释。发现条目保留修改前后文本、版本和复读范围；撤销的问题保留撤销依据，不计作已修复发现。

语义判断记录由AI审读者完成，保存在各章的 C/P/W 文件中。编号、提取和哈希脚本只辅助整理，不代替句义解释或语义审查。记录中的 S 单位有些包括标题、图注或公式提示，不能把全部 S 数量称作自然语言句数。

参与改写者的检查称为自查；公平性和可解释性的冻结稿由未参与该稿改写的审读者分别复核，其修订部分仍称改后自查。记录抽核仅验证记录的一致性和抽样依据，不等于重新独立审读全部正文。

| 部分 | 章 | 审查与修复记录 |
| --- | --- | --- |
| 基础 | 引言 | [终稿审查](basics/introduction-final-review.md)、[C](basics/introduction-C.json)、[P](basics/introduction-P.json)、[W 第一批](basics/introduction-W-part1.json)、[第二批](basics/introduction-W-part2.json)、[第三批](basics/introduction-W-part3.json) |
| 基础 | 模型简介 | [终稿审查与发现闭环](basics/models-final-review.md)、[C](basics/models-C.md)、[P](basics/models-P.json)、[W 第一批](basics/models-W-part1.json)、[第二批](basics/models-W-part2.json)、[第三批](basics/models-W-part3.json)、[改后复读](basics/models-W-r3.json) |
| 基础 | 范式简介 | [终稿审查与发现闭环](basics/paradigms-final-review.md)、[C](basics/paradigms-C.md)、[P](basics/paradigms-P.json)、[W 第一批](basics/paradigms-W-part1.json)、[第二批](basics/paradigms-W-part2.json)、[第三批](basics/paradigms-W-part3.json)、[改后复读](basics/paradigms-W-r4.json) |
| 理论 | 机器学习理论基础 | [C/P 与校准](theory-a/01-review.md)、[W](theory-a/01-sentence-review.md) |
| 理论 | 二分类学习的可学习性 | [C/P 与校准](theory-a/02-review.md)、[W](theory-a/02-sentence-review.md) |
| 理论 | 多分类学习的可学习性 | [C/P 与校准](theory-a/03-review.md)、[W](theory-a/03-sentence-review.md)、[集成修订](integration/findings.json) |
| 理论 | 一般学习的可学习性 | [C/P/W、关键链与改后复读索引](theory-b/README.md) |
| 理论 | 深度学习的可学习性 | [C/P/W、关键链与改后复读索引](theory-b/README.md) |
| 理论 | 迁移学习的可学习性 | [C/P/W、关键链与改后复读索引](theory-b/README.md) |
| 可信性 | 可信机器学习基础 | [C](trust/01-pass1-chapter.md)、[P](trust/01-pass2-paragraph.md)、[W](trust/01-pass3-sentence.md)、[关键链与校准](trust/01-key-units-and-calibration.md)、[发现闭环](trust/01-findings-and-closure.md) |
| 可信性 | 可靠性 | [C](trust/02-pass1-chapter.md)、[P](trust/02-pass2-paragraph.md)、[W](trust/02-pass3-sentence.md)、[关键链与校准](trust/02-key-units-and-calibration.md)、[发现闭环](trust/02-findings-and-closure.md) |
| 可信性 | 鲁棒性 | [C](trust/03-pass1-chapter.md)、[P](trust/03-pass2-paragraph.md)、[W](trust/03-pass3-sentence.md)、[关键链与校准](trust/03-key-units-and-calibration.md)、[发现闭环](trust/03-findings-and-closure.md) |
| 可信性 | 公平性 | [冻结稿复核、修订与复读索引](trust-04-independent/README.md) |
| 可信性 | 目标对齐与行为约束 | [C](trust/05-pass1-chapter.md)、[P](trust/05-pass2-paragraph.md)、[W](trust/05-pass3-sentence.md)、[关键链与校准](trust/05-key-units-and-calibration.md)、[发现闭环](trust/05-findings-and-closure.md) |
| 可信性 | 可解释性 | [冻结稿复核、修订与复读索引](theory-b/interpretability-06/README.md) |
| 可信性 | 隐私保护 | [C/P 与校准](theory-a/07-privacy-review.md)、[W](theory-a/07-privacy-sentence-review.md) |
| 可信性 | 对抗安全 | [C/P/W、关键链与改后复读索引](theory-b/security-08/README.md) |

基础与理论导读见 [C 与门槛审查](guides/chapter-gates-review.md) 和 [P/W](guides/paragraph-sentence-review.json)；可信性导读见 [C](trust/guide-pass1-chapter.md)、[P](trust/guide-pass2-paragraph.md)、[W](trust/guide-pass3-sentence.md)、[关键链与校准](trust/guide-key-units-and-calibration.md) 和 [发现闭环](trust/guide-findings-and-closure.md)。

## 终稿补充与记录抽核

基础三章的原导航恢复及局部复读见 [navigation-restoration.json](basics/navigation-restoration.json)。理论 01、02、04–06 与可信性 01–04 共九个文件的导航及两项术语恢复，见 [补充审查](theory-a/navigation-terms/review.md)、[逐项修改](theory-a/navigation-terms/changes.json) 和 [终稿版本](theory-a/navigation-terms/manifest.json)。该补充覆盖相应分项报告之后的修改，最终版本仍以总 composition 为准。多分类章“计费口径”改为“计分口径”的局部修订与连续复读见 [integration/findings.json](integration/findings.json)。

可信性目录中保留的公平性、可解释性早期稿是过程证据；它们的最终审查覆盖分别由上表的 `trust-04-independent/` 和 `theory-b/interpretability-06/` 提供。

范式图前强制换页造成的留白在 [分页修订记录](integration/pagination-fix.json) 中补充修复，仅改变浮动指令；保留修改前后完整章快照和最终版面复查。

[记录抽核报告](theory-a/records-audit.md) 检查其声明范围内的编号覆盖、版本、发现闭环与人工依据样本，不扩大为整卷独立审查。[目标对齐与可信导读的记录抽核](trust/final-records-audit.md) 补充核对其终稿版本与记录勘误；勘误已修复并闭环。[总索引与最终组成核对](theory-b/final-integration-audit.md) 验证相对链接、24 个输入的哈希、章节小结和角色表述，并逐项保存机械差异。

## 验证与边界

工程检查、七份成品一致性及 PDF 版面抽检的实际结果统一记录在 [engineering-verification.json](integration/engineering-verification.json)。七份PDF构建、成品校验、完整测试及版本结构检查均通过。指定范围的真实PDF版面抽检已完成，持续学习图的分页缺陷已修复并补查。抽样页、哈希与边界见 [终稿抽样记录](integration/final-pdf-sampling.json)，人工观察见 [主审报告](integration/pdf-visual-root.md)、[七份成品及索引补查](theory-a/pdf-visual-review.md) 和 [可信性版面报告](trust/pdf-visual-review.md)。机械结构比较只记录标题、标签、引用和公式文本等差异，不据此自动判定文字质量或数学正确性。

本次进行了与改写相关的概念、公式讲解、条件和比较口径核对，并运行引言示例、核查部分研究比较的原始来源。没有对全部参考文献、外部证明或实验协议进行逐项独立复现；PDF 版面检查为按章和成品组成抽检，不能称作逐页审阅全书。

## 后续版本

本目录冻结的是整卷改写阶段正文。卷二图像修订及卷一 fbb26ae 整合后发生的局部正文变化，以 [跨卷修订与审查](../2026-10-12-volume-two-cross-volume/README.md) 和其最终组成快照为准，不能用本目录旧 SHA 代替当前正文验收。
