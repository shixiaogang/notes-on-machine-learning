# 卷一分章修复与润色要求

日期：2026-10-12。适用于用户授权的“每章一名独立代理”修复阶段。

## 工作区与版本

- 工作区：`/Users/bytedance/Projects/notes_on_machine_learning/.worktrees/volume-one-readable-review`。只在这里读写。
- 分支：`codex/volume-one-readable-review`，已快进到 `main` 的 `ba0d3fce`（十二卷出版结构）。
- 初审基线：`a5514b22`，即重组前“卷一·数学准备”的17章。重组后第1—9章位于
  `tex/01-mathematical-preliminaries-upper/`（新卷1《数学准备：计算、分析与几何》），
  第10—17章位于 `tex/02-mathematical-preliminaries-lower/`（新卷2《数学准备：概率、因果与决策》，
  卷内章号从1重新开始）。逐章路径见本目录 `repair-path-map.json`。
- 与基线相比，正文只改了文件路径、图像路径和跨卷引用宏，行数基本不变：
  第12章基线L1378之后的行号加3，第13章基线L882之后的行号加4，其余章节行号不变。
  初审记录的行号与 `units/chNN.md` 的 P/S 锚点可继续用于定位，但一律以当前文件实际内容为准。
- 修复前快照：`snapshots/before/`（含 `SHA256SUMS`）。

## 角色与边界

你是本章的独立汇总修复代理，没有参加初审。用户授权你依据三位初审者的报告核实问题、修复本章，
并按 academic-writing 要求润色相关内容。你自己完成判断，不使用 Agent 工具派生代理。

- 只修改分配给你的一个章节源文件。不改其他章节、`part.tex`、`volume.tex`、共享宏与样式、
  文献库、索引词典、图源、构建脚本、计划与规范。
- 不运行 `build.sh`、`latexmk`、`xelatex`、`make`，不执行 `git add/commit/stash/checkout/reset/restore`
  等改变仓库状态的命令。可以运行只读命令，如 `git diff -- <你的文件>`、`git show`、`grep`。
  不要运行 `git status`：沙箱中它会触发 LFS 过滤器报错。
- 同一工作区有其他章节代理同时修改各自文件。不要触碰、格式化或回退他人文件。
- 主代理统一负责词典登记、部分指引、构建、成品检查和提交。

## 必读材料

1. `AGENTS.md`、`specs/development.md`、`specs/writings.md`、`specs/latex.md`；涉及语义环境时读 `specs/design.md`。
2. academic-writing 技能：`/Users/bytedance/.trae-cn/skills/academic-writing/SKILL.md`，以及
   `references/grammar-and-style.md`、`references/chinese-examples.md`、`references/content.md`、
   `references/review.md`、`references/review-records.md`；遇到结构疑点再读 `references/structure.md`。
3. 本目录 `REVIEW-INSTRUCTIONS.md`（审查准则）和 `REPAIR-INSTRUCTIONS.md`（修复准则）。
   后者中的旧路径按新路径理解；“新词条登记在词典”一项改为写入记录、由主代理登记；
   “不启动构建、不暂存提交、不改共享宏和其他卷”继续有效。
4. `initial/chNN/reviewer-a|b|c/` 的 `findings.json` 和 `report.md`，尤其是报告中的难概念解释时序表；
   判断需要时再读 `paragraphs.md`、`sentences-*.md`。第1—4章可参考 `pending-fixes.md` 的中期合并，
   但它不是最终结论，每项仍须回到正文重核。
5. `plans/mathematical-preliminaries-reading-structure.md` 中本章的职责、所属 `part.tex` 的指引，
   以及本章回指的前文实际上下文。

## 读者与目标

读者是理工科本科生，学过本科常见的分析、线性代数、概率与组合数学，按卷内顺序第一次接触本章的进阶主题。
只把当前位置以前已经解释的内容当作已知，不用后文、专业常识或聊天内容替当前位置补洞。

目标是读得顺、难概念讲得清。对本科常见数学之外的概念，在首次需要的地方说明：

- 当前遇到了什么数学问题，原有对象或做法缺什么；
- 新概念怎样回应这个问题，名称出现后立即用白话说明它是什么、起什么作用；
- 它与前面已知对象在对象、条件、用途上相同和不同在哪里；
- 必要时给出可以复算的最小例子、推理桥梁或反例，并交代不成立的条件与代价。

写法遵循 academic-writing 的写作风格：从对象与问题进入，把机制与推导讲透，用完整句子推进关系，
自然使用“我们”带领推演，过渡承接实际认识，得到结论后检查边界。删除空话、重复预告和模板化过渡；
不用“显然”“不难看出”掩盖推导；不给段落加“背景”“机制”之类的标签；不逐节套用同一模板。

## 工作步骤

1. **顺读全章。** 先完整读完本章当前正文（长章可分段读，但必须读完），建立自己的章级理解。
2. **汇总核实。** 读三位审读者的全部发现，逐条回到当前正文核实。同一位置、同一根因的发现合并为
   `CHNN-M-01` 起编号，保留全部原编号。成立的修改；不成立的有据撤销，写明当前正文为何已经足够。
   初审已撤销的项也复核一次。顺读中发现的新问题编号为 `CHNN-N-01` 起，同样修复并记录。
3. **修改正文。** 先技术问题，再理解障碍，最后局部费力。优先补桥、局部前移、合并重复和改句；
   为读顺可以重写一个段落，但必须遵守：
   - 不改 `\chapter`、`\section`、`\subsection`、`\subsubsection`、`\paragraph` 的标题文字、层级与顺序；
     结构审计会逐条比对标题。保留全部 `\label`，不改名；保留 `\section{本章小结}`。
   - 不改变数学条件、量词、符号和证据强度。确认原文有数学错误时可以修正，并在记录中明确说明。
   - 不编造历史、来源或数据，不新增文献引用。
   - 不改图像环境中的 `\includegraphics` 与 `\label`；只有发现针对图注时才改图注。
   - 同卷引用使用 `第~\ref{...}章`、`第~\ref{...}节`、`式~\eqref{...}`。跨卷引用（新卷2的章节引用新卷1，
     或反之）使用 `\BookChapterRef`、`\BookSectionRef`、`\BookEquationRef` 等宏，并先在当地写清所用结论、
     成立条件和用途，再写“可参考……”。不手写章号。新卷2的章号从1开始，正文中不能再出现
     “第10章”这类旧编号；“本卷”“前十六章”“前五个部分”等与现结构不符的表述按现结构改写。
   - 尽量不新增或删除 `\term`；改写含 `\term` 的句子时保留该调用。确需新增术语时，先在
     `tex/index-terms/*.tex` 查找已有译名；不要编辑词典，把中文、英文和位置写进记录，由主代理登记。
   - 不新增宏包或宏，只使用项目已有宏与语义环境。尽量不新增 `\label`；确需新增时保证唯一并沿用本章前缀。
   - 篇幅以讲清楚为准，不以加长为目标。本章净增长尽量不超过约10%（每卷总页数上限600页）；
     能替换的不叠加新段落，重复解释应合并。
4. **复读。** 每处修改后核对技术含义，并连同前后文复读。全部修改完成后，从头到尾再顺读整章一遍，
   检查新引入的问题、术语和符号一致性、回指与衔接。这是 AI 自查，不是独立复核。
5. **检查 LaTeX。** 核对括号、环境、`$` 配对，中文全角标点，句末 `\scite` 位于句号之前，
   没有因删改换行或 `%` 造成文字粘连。运行
   `python3 scripts/audit_math_reading_structure.py --chapter <全书章号1—17>`（只读），确认 issues=0。

## 分批推进与中断续作

已有章节代理因模型流超过6分钟无输出而中断。为使成果不因中断丢失：

- 按节或每批3—5项发现推进：核实一批、修改一批、复读一批，随即更新 `repair/chNN/` 的两份记录，
  再进入下一批。不要一次规划或写出整章改动，也不要构造过长的单次编辑。
- 开始前先检查 `git diff -- <本章文件>` 和 `repair/chNN/`。若有前一次中断留下的改动或记录，
  先核对它们与当前正文是否一致，再从未完成处继续，不重复修改，也不回退已有改动。

## 记录

只写 `repair/chNN/`：

- `consolidated-findings.json`：数组，每项含 `merged_id`、`original_ids`、`severity`、
  `decision`（修改、有据撤销或新增发现）、`location_before`（基线行号与短引）、
  `location_after`（当前行号与短引）、`action`、`reread_range`、`closure_reason`。
- `repair-notes.md`：修复摘要；重点补充了哪些难概念及怎样补；撤销项的理由；自查的连续复读范围；
  修改前后的行数；需要主代理处理的事项（词条、跨章依赖、构建疑点）；仍需独立复核的项目。

## 返回

返回本章的原始发现数、合并后数、修改数、撤销数、新增发现数、修改前后行数、未解决项、
需要主代理处理的事项，以及记录路径。
