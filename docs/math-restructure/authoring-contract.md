# 数学准备重构协作约定

本次工作已由用户授权实施。依据为 `plans/mathematical-preliminaries-reading-structure.md`，基线为 `f435c9d`。大纲中的“拟议”“暂不改正文”记录此前规划阶段，不限制本次已授权的正文实施。

## 共同要求

- 严格使用阅读结构的章、节、小节及更深标题与顺序，实施后章号由 LaTeX 连续生成。旧大纲定位号不写死在正文；正文引用使用语义标签。第20章的列表也是完整标题要求。
- 每位作者负责一个最终章节。通读该章的完整大纲、原正文与迁入材料，实际重组段落、定义、证明和例子。禁止仅改标题、把旧节整体塞进新节或压缩成概念提要。
- 大纲要求保留的定义、定理、证明、推导、算例、边界、图和语义标签必须保留或准确迁至唯一主讲位置。重复定义合并后保留兼容标签；不要把旧章标签放在节中造成章引用错误。
- 补写大纲明确指出的缺失内容。陌生概念由具体问题引入，紧接白话解释，再给正式定义、条件、计算例子和相近概念的区别。读者为已学基础分析、线性代数、概率论、组合数学的理工科本科毕业生。
- 使用 `academic-writing`，先完整读取技能及任务所需参考；遵守 `AGENTS.md`、`specs/README.md`、`specs/writings.md`、`specs/notations.md`、`specs/latex.md`、`specs/design.md`。涉及插图使用 `academic-drawing` 并读取所需参考和 `specs/figures.md`。
- 图在最终正文112 mm或跨栏169 mm尺寸设计，沿用第一卷入口的 `foundation-visual-overrides`：文楷、低饱和黄/蓝/红、深灰文字、透明标注背景；数学几何及精确关系采用项目优先的 TikZ/PGFPlots，既有 Matplotlib 图可继续使用。新图保存到 `figures/math-preparation/reading-restructure/chNN/`，图注与正文说明看什么及为何。
- 无需为每个概念机械增加图；优先补能展示对象差异、失败反例、同例比较或状态变化的图。新增图至少有源文件、正文引用、中文图注及语义标签。
- 仅写分配的最终章文件、自己图目录、`docs/math-restructure/chapters/chNN.md` 和可选的 `chNN-terms.tex` / `chNN-references.bib`。不要修改其他作者文件、共享词典、共享书目、模板或入口；不要运行全卷/全集构建，不提交 Git。
- 共享索引与引用由主代理汇总。尽量复用已登记词条及书目；新增词条或核实的新文献写入本章旁路清单，不造引文。
- 原文件在集成前保持不动（前五章原地编辑例外），跨章迁入材料从 `git show f435c9d:<路径>` 或 `build/math-restructure-baseline/` 读取，避免读取正在改动的版本。
- 每章完成后自检标题层级、全部既有标签归属、环境配对、技术条件、语言、图注及小结；交付章报告应逐项列出大纲新增内容的实质落点、迁入迁出位置、图源、证明保留情况及尚待核验项。不得把未核验项宣称通过。
- 若上下文不足，保存任务内手记并继续完成同一章；不能因为章节长就只交部分初稿。作者不得再派下级作者，以保持一章一名作者的职责。

## 最终章节与文件

所有路径均相对于工作区；前缀 `tex/01-mathematical-preliminaries/` 以下简写。

| 最终章 | 大纲定位号 | 章节 | 最终相对路径 |
| --- | --- | --- | --- |
| 1 | 1 | 数学对象与逻辑 | 01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex |
| 2 | 2 | 计数与计算 | 01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex |
| 3 | 3 | 测度与分析 | 01-mathematical-language-combinatorics-analysis-optimization/03-mathematical-analysis.tex |
| 4 | 4 | 最优化 | 01-mathematical-language-combinatorics-analysis-optimization/04-optimization.tex |
| 5 | 5 | 函数空间 | 01-mathematical-language-combinatorics-analysis-optimization/05-functional-analysis-and-approximation.tex |
| 6 | 6 | 线性空间 | 02-linear-algebra-and-geometry/01-linear-algebra-and-matrix-analysis.tex |
| 7 | 8 | 非线性空间与流形 | 02-linear-algebra-and-geometry/02-differential-geometry-and-symmetry.tex |
| 8 | 9 | 随机变量 | 03-random-variables-distributions-and-causality/01-random-variables.tex |
| 9 | 12 | 随机分布 | 03-random-variables-distributions-and-causality/02-information-theory-and-statistical-geometry.tex |
| 10 | 13 | 因果响应 | 03-random-variables-distributions-and-causality/03-causal-response-and-structure.tex |
| 11 | 14 | 图的表示与计算 | 04-graphs-and-signals/01-graph-structure-and-computation.tex |
| 12 | 15 | 信号的表示与计算 | 04-graphs-and-signals/02-signal-representation-and-processing.tex |
| 13 | 16 | 行动和状态 | 05-dynamical-systems-control-decision-and-games/01-action-and-state.tex |
| 14 | 17 | 策略的实现与轨迹控制 | 05-dynamical-systems-control-decision-and-games/02-policy-realization-and-control.tex |
| 15 | 18 | 策略的价值与优化 | 05-dynamical-systems-control-decision-and-games/03-policy-value-and-optimization.tex |
| 16 | 19 | 多方策略的响应与演化 | 05-dynamical-systems-control-decision-and-games/04-multi-agent-response-and-evolution.tex |
| 17 | 20 | 数学基础与后续研究 | 05-dynamical-systems-control-decision-and-games/05-mathematics-and-future-research.tex |

## 跨章迁移和共同例子

- 原线性代数、矩阵分析归最终第6章；原概率论、随机过程、统计归第8章。
- 原动力系统的 Brownian 定义及二次变差归第8章；原随机过程的随机逼近、平均 ODE、Poisson 方程与双尺度归第13章。Poisson 过程及补偿过程由第8章补写，有限活动跳跃积分与 Itô 换元由第13章补写。
- 原信息章弱收敛、紧性通用定义归第8章；第9章保留最优耦合证明并回指，不重复定义。
- 原信号章图傅里叶、环图谱与图滤波归第11章；原信号章状态核完整构造归第13章。第12章仅使用给定核。
- 原控制章 HJB、有限 LQG 成本最优性及连续有限时域 LQR 价值推导归第15章；有限 LQR 定义、Riccati 构造、无限 DARE 稳定化与滤波稳态条件归第14章。
- 最终第13—16章共用教学温度模型：离散状态为相对于环境温度的温差 `x_t`，行动为加热量 `u_t`，`x_{t+1}=0.8x_t+u_t+w_{t+1}`，观测 `y_t=x_t+v_t`。先确定性取噪声为零；需要随机时显式给噪声分布和独立性。固定目标 `r=2` 时平衡输入为 `0.4`；示例反馈 `u_t=0.4-0.3(x_t-2)` 得误差系数 `0.5`。跟踪使用 `u_t^r=r_{t+1}-0.8r_t`。默认不加输入限制，需要安全任务时明确 `0<=u_t<=1`、`0<=x_t<=3` 并检查可行性。
- 多方例在第16章明示模型扩展为两个行动的和及各方成本，不悄然沿用单行动的闭环结论；策略更新轮次使用带括号上标，区别于局内时间下标。
- 保留原路线、振子、三张牌、匹配硬币等任务专用例，不为统一而删掉已验证的算例。

## 汇总与两轮检查

章节写完后另派一名作者串联全卷，检查概念主讲、引用、共同例子和章际承接。第一轮另派3名独立 subagent 按本科理工科毕业生视角审读，逐章记录所有新概念（包括未使用 `\term` 的概念）、首次出现位置、动机、直觉、例子/图和依赖；由正文修订闭环解决问题。第二轮在第一轮修订后派1名 subagent 阅读实际 PDF，检查格式与视觉，保留页码证据并修复。最终运行结构、索引、七版构建及 `check-target`，如实记录覆盖范围。用户未要求提交，成果保留在本工作区。
