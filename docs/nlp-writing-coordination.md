# 自然语言处理八章协作约定

## 交付与边界

按 `plans/natural-language-processing-outline.md` 与 `plans/natural-language-processing-literature.md` 编写整部正文。每位作者负责一章，主 agent 汇总串联、整合文献、构建与验收。本文件属于工作约定，不进入书稿正文。

工作区为当前 `latest-main-20261005-2` worktree。沿用工作区现有五卷路径，不迁移其他工作区的目录和内容，不提交、不推送。已有第1章需要补足大纲要求和修正，不视为已最终验收。

| 章 | 正文文件（位于 `tex/04-applications/01-natural-language-processing/`） | 章标签 | 新图源前缀 | 临时文献 |
| --- | --- | --- | --- | --- |
| 1 | `01-introduction.tex` | `chap:nlp-introduction` | 现有两图或 `nlp-intro-` | `build/nlp-writing/ch01.bib` |
| 2 | `02-text-analysis.tex` | `chap:nlp-text-analysis` | `nlp-analysis-` | `build/nlp-writing/ch02.bib` |
| 3 | `03-information-extraction.tex` | `chap:nlp-information-extraction` | `nlp-extraction-` | `build/nlp-writing/ch03.bib` |
| 4 | `04-classification-matching-organization.tex` | `chap:nlp-classification-matching-organization` | `nlp-classification-` | `build/nlp-writing/ch04.bib` |
| 5 | `05-text-generation.tex` | `chap:nlp-text-generation` | `nlp-generation-` | `build/nlp-writing/ch05.bib` |
| 6 | `06-question-answering-dialogue.tex` | `chap:nlp-question-answering-dialogue` | `nlp-dialogue-` | `build/nlp-writing/ch06.bib` |
| 7 | `07-solving-and-execution.tex` | `chap:nlp-solving-and-execution` | `nlp-execution-` | `build/nlp-writing/ch07.bib` |
| 8 | `08-speech-tasks.tex` | `chap:nlp-speech-tasks` | `nlp-speech-` | `build/nlp-writing/ch08.bib` |

## 共同案例

- 所有数值、通知、轨迹和声音例子均明确为教学构造，不声称实测。
- 活动名称为“机器学习读书会”，活动编号 `ML-0418`。
- 为使星期可核验，通知中的年份统一为 **2025年**，与研究检索截止时间无关。通知发布于2025年4月15日（北京时间）。
- 通知全文：“机器学习读书会原定于4月17日举行，现改至4月18日（周五）14:00，地点为海棠楼201。校内师生可直接参加，校外来宾须在4月16日18:00前提交报名信息。”
- “4月16日18:00前”是精确截止条件，不简写为“4月16日前”。“我明天下午到可以吗”的咨询时点为4月17日，校外咨询者还需核验是否已报名。
- 不在未说明的情况下新增主讲人、费用、剩余名额、时长或预约状态；需要时明确引入本节补充资料或业务状态。
- 允许各章根据算法需要使用其他简短例子，不强行把所有技术都塞进同一个业务。

## 写作深度

- 作者必须完整阅读 `academic-writing/SKILL.md` 及其本任务必需参考、工作区 `AGENTS.md`、相关 `specs/`，绘图时阅读 `academic-drawing`。用户已明确授权写作和分工，不再次索要执行许可。
- 保留大纲全部章、节、小节和方法小小节的结构与职责；重要算法用 `\subsubsection` 编号。每个叶节点有实质讲解，不能只把大纲换成短句。
- 完整代表实现走通输入、监督/参数来源、目标、计算、解码/恢复、核验和边界。大纲指定的手算（CKY、Viterbi、EM、CTC、搜索等）给出可复核输入、中间结果和结论，重要数值用小脚本复算。
- 各章保留独立 `\section{本章小结}`，章首与结尾衔接相邻章已解决的问题，不重复抄目录。
- 保留所有规划图表，按解释需要增加紧凑数值表。图源放在 `figures/`，沿用项目字体、调色板；正文宽112mm、跨栏宽169mm，不用缩小字号来掩盖拥挤。
- 共同概念可以简短回顾并引用已存在章节；不能凭空引用尚无正文的范式章。前卷入口包括 `chap:machine-learning-paradigms`、`sec:self-supervised-learning`、`sec:weakly-supervised-learning`、`sec:transfer-learning`、`chap:classification`、`chap:transformer`、`sec:pgm-dynamic-discrete`、`sec:pgm-energy-models-crf-definition`。

## 并行文件所有权

- 只编辑自己的章节文件、对应前缀图源以及 `build/nlp-writing/chNN*` 工作文件。第1章作者还拥有现有 `figures/nlp-one-text-many-tasks.tex` 和 `figures/nlp-task-history.tex`。
- 不修改 `part.tex`、`tex/references.bib`、`tex/preamble.tex`、共享样式、构建脚本或其他章；需要修改时发送具体建议，由主 agent 整合。
- 先复用文献库已有键；新增经核验条目写到自己的临时 `.bib`，主 agent 按 DOI/标题去重后并入唯一正式文献库。
- 论文专有细节需核查一手方法正文，不能只据摘要猜计算步骤。不确定项须查证或准确收窄，不留下伪造事实。
- `\scite{key}` **已自动输出中文句号**，后面不要再接句号、逗号或分号。句中引用使用 `\sidecite`。全文作者名不能用 `others` 省略。
- 一页集中多条完整引文会越界，尤其50名作者的论文。长条目可以在本章末、小结前的非编号“文献说明”中用非浮动 `fullwidth` 和 `\fullcite` 完整呈现，正文用 `\citeauthor`/`\citeyear`/`\citetitle` 等不生成边注的命令引用并明确回指。常规短引文仍用边注。
- 全书 `build/main.*` 只允许主 agent 构建。局部预览若需要，须使用自己唯一的 jobname 与 `build/nlp-writing/chNN/` 目录，不能并行写主构建缓存。正式交付由主 agent 通过 `./build.sh`。
- 本机 TeX 在 `/Library/TeX/texbin`；如遇 Biber 通用二进制错误，已有 `/tmp/biber-arm64` 可用，使用临时 PATH 适配，不改系统和仓库构建配置。局部 LaTeX 必须继承 `.latexmkrc` 中 `TEXINPUTS` 等路径，不能误用系统 Tufte 类。

## 作者交付记录

每位作者将简短记录放入 `build/nlp-writing/chNN-review.md`，包括：

- 大纲全部叶节点到正文标题/标签的对应，以及图表对应；
- 可复算例子和核验结果；
- 新增文献、一手来源及实际支持范围；
- 暴露给其他章使用的标签、需统稿者处理的接口；
- 实际完成的文字、技术、局部编译和版面检查；未检查的不写成通过。

交稿后主 agent 统一术语和例子，查缺补漏，完成分部和全书构建，核验新增各页及图表、边注、公式。文件存在或编译退出码为零都不能代替内容和版面验收。
