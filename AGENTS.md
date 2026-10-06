# 项目说明

这是一本使用 LaTeX 编写的中文机器学习笔记，基于 `tufte-book` 模板修改，并通过 Git 管理变更。

## 目录职责

- `tex/`：书籍的主内容、LaTeX 源文件及项目固定使用的 Tufte 模板文件。
- `specs/`：供 agent 遵循的开发规范。
- `plans/`：开发计划与任务拆解。
- `figures/`：书籍中使用的图像资源。
- `fonts/`：项目固定使用的字体文件、校验清单及其上游许可证。
- `build/`：LaTeX 中间产物与编译缓存，不纳入 Git。
- `target/`：全集和六个单卷的成品 PDF 及构建校验记录，随正文一起提交。

## 开发规范索引

开始编写或修改内容前，必须阅读与任务相关的开发规范：

- `specs/notations.md`：变量字形、集合、索引、迭代、切片及公式排版。
- `specs/figures.md`：TikZ 优先原则、生成式图像、配色、标注及可复现性。
- `specs/writings.md`：问题驱动的概念铺陈、逻辑衔接、自然中文、术语、引用、改写示例及交稿检查。
- `specs/latex.md`：文件组织、命名、交叉引用、宏、依赖及编译检查。
- `specs/design.md`：封面与内页、字体、颜色、数学及代码环境、边注引文和图表版式。
- `specs/commits.md`：提交消息格式、类型与范围、变更划分及历史整理；创建提交前必须阅读并遵循。

通用原则及完整说明见 `specs/README.md`。如果不同规范之间存在冲突，以更具体的规范为准。

## 写作要求

凡涉及正文、章节大纲、图表说明或示例文字，必须先阅读 `specs/writings.md`，并在交稿前完成其中的自查。以优秀技术作者和资深研发工程师的标准写作：技术准确，逻辑严密，讲解循序渐进，语言自然，体谅读者的理解负担。

- 引入新概念前，先说明当前问题或已有方法的不足；核心术语首次出现时，紧接白话解释，再逐步展开定义、机制和推导。
- 按“读者已知什么—还缺什么—新概念如何补上”组织内容。段落靠因果、条件、递进或转折衔接，不靠“首先、其次、再次、最后”串联。
- 开篇提出的问题必须在正文中得到回应，结尾收拢答案与适用边界。同一概念的名称与符号保持一致。
- 每章末尾必须设置独立的 `\section{本章小结}`；新增或重构章节时不得省略，也不得将小结并入其他小节。
- 使用具体、直接的中文，主动预判理解难点。避免空话、术语堆叠、反复总结和整齐划一的段落模板；比喻、设问与“你／我们”应服务于解释。
- 初稿完成后，分别检查逻辑、技术准确性与语言。发现概念跳步、论证缺口或读者难以跟上的句子，先修订再交稿。

## 内容结构

书籍采用“卷—部分—章—节”结构。`tex/` 下按卷设置带两位序号的英文目录，每卷以 `volume.tex` 为入口；卷内各部分再使用带两位序号的英文子目录，以 `part.tex` 为入口。目录前缀按所属层级从 01 开始，书中的部分号和章号则全书连续编号。

1. `tex/01-mathematical-preliminaries/`：第一卷“数学准备”
   - `01-mathematical-language-analysis-optimization/`：数学语言、分析与最优化
   - `02-linear-algebra-and-geometry/`：线性代数与几何
   - `03-probability-stochastic-processes-statistics/`：概率、随机过程与统计
   - `04-discrete-mathematics-and-graph-theory/`：离散数学与图论
   - `05-dynamical-systems-control-and-decision/`：动力系统、控制与决策
2. `tex/02-foundations/`：第二卷“基础、理论和可信性”
   - `01-basics/`：机器学习基础
   - `02-learning-theory/`：机器学习理论
   - `03-trustworthiness/`：机器学习可信性
3. `tex/03-models/`：第三卷“模型”
   - `01-classic-models/`：经典模型
   - `02-neural-network-models/`：神经网络模型
   - `03-probabilistic-graphical-models/`：概率图模型
4. `tex/04-paradigms/`：第四卷“范式”
   - `01-reinforcement-learning/`：强化学习
   - `02-efficient-knowledge-use/`：知识的高效利用
   - `03-knowledge-evolution-and-transfer/`：知识的演进与迁移
5. `tex/05-applications/`：第五卷“应用”
   - `01-natural-language-processing/`：自然语言处理
   - `02-image-processing/`：图像处理
   - `03-recommendation-and-search/`：推荐与搜索
6. `tex/06-systems/`：第六卷“系统”
   - `01-machine-learning-systems/`：机器学习系统；承接数据、训练与部署相关内容。

“机器学习理论”部分依次介绍统计学习框架、二分类、多分类、凸学习与算法稳定性、深度学习理论和迁移学习理论，详细规划见 `plans/learning-theory-outline.md`。全书分卷、内容边界与迁移约定见 `plans/book-structure.md`。

后续新增章节时，应放入其所属卷和部分的目录中；图像资源放入 `figures/`，并在 LaTeX 源文件中以相对路径引用。

## 提交前的成品一致性

每次提交前必须运行 `./build.sh all` 和 `./build.sh check-target`。全集为
`target/machine-learning-notes.pdf`，六个单卷为 `target/volN-<slug>.pdf`。
七份 PDF 与 `target/.build-manifest.json` 必须对应当前正文、图源、字体及构建输入，
并与正文一起暂存；不得提交过期或遗漏的成品。新克隆后运行
`git config --local core.hooksPath .githooks` 启用版本化提交检查。
索引只收录当前出版单元正文实际调用的 `\term` / `\termalias`；词典登记本身不产生条目。
全集和单卷的部首页必须使用奇数正文页码；需要补页时，空白页不显示页眉或页码，目录、书签及标签仍指向部首页。
正文第 1 页也必须位于 PDF 的实际奇数页，以同步正文页码与 PDF 页面序号的奇偶。
