# 推荐、搜索与广告：三人分章评审

## 送审范围

本轮只评审新完成的十章，不修改正文、图表、书目、索引或构建配置，不创建提交或推送。每章由三个独立subagent审阅，共30份完整七维评审；侧重不同，但不省略其他维度。主代理负责复核、去重和逐章综合判断。

工作树：`/Users/bytedance/Projects/notes_on_machine_learning/.worktrees/latest-main-20261005-3`。

这是中文机器学习教材中的教程式综述，面向已学线性代数、概率和基本机器学习的读者。评审口径来自正文声明、相关大纲和全书分工，不把它当作PRISMA系统综述，不因没有穷尽所有论文或缺少某篇增量工作就判为关键遗漏。已批准的大纲也不自动证明分类合理；可以指出大纲自身造成的实质问题，但不能未经上下文检查就要求每章重复其他章的内容。

时间边界采用2026-10-05；检索另记录实际执行日期。送审源文件和PDF哈希见`manifest.json`。之前的写作自查和编译通过不构成本轮质量结论的证据。

## 阅读材料

- 正文：`tex/05-applications/03-recommendation-and-search/`中的十个章节；相邻章节和跨章引用按需读原文。
- 大纲：`plans/recommendation-and-search-outline.md`；同目录配套架构、研究课题、文献地图按实际路径查找。用这些确定范围，不用它们替代独立领域地图。
- 全部参考文献：`tex/references.bib`；本章图源由正文中的`\input{figures/...}`定位。
- 最终应用PDF：`build/05-applications.pdf`，323页。物理页码范围如下；它们与纸面页码相差12页。
- 已有一手资料缓存：`build/recommendation-writing/sources/`。可以读取原文缓存，但仍须独立检索领域路线、竞争观点和反面证据。不能把旧的`ch*-review.md`或写作验收报告当作自己的审阅结果。
- 原有预览：`build/recommendation-writing/final-preview/`。可以使用，但实际图表判定须观察图像；只读图源不能证明最终视觉呈现通过。

| 章 | 文件 | PDF物理页 |
| --- | --- | --- |
| 01 推荐概述 | `01-overview.tex` | 16—24 |
| 02 用户与对象理解 | `02-user-item-understanding.tex` | 25—52 |
| 03 个性化候选召回 | `03-candidate-retrieval.tex` | 53—80 |
| 04 个性化排序与响应预估 | `04-ranking-response.tex` | 81—116 |
| 05 推荐展示 | `05-presentation.tex` | 117—140 |
| 06 多目标与受约束决策 | `06-constrained-decisions.tex` | 141—156 |
| 07 长期价值与连续决策 | `07-long-term-decisions.tex` | 157—176 |
| 08 推荐评价与效果识别 | `08-evaluation.tex` | 177—198 |
| 09 搜索与相关性 | `09-search-relevance.tex` | 199—243 |
| 10 广告 | `10-advertising.tex` | 244—296 |

## 三个审阅角色

- `a`：以领域地图、覆盖与无偏性、演进与分类为重点，警惕热门新方法挤压基础路线、竞争观点和负面证据。
- `b`：以技术正确性、假设、推导、教学算例、原论文支持范围和深度为重点，核对机制而非仅核书目信息。
- `c`：以读者理解、同级职责、论证链、中文表达、跨章边界和图表为重点，独立核对分类图与比较表的依据。

每位审阅者均须按`academic-survey-review`完成三遍阅读、独立相关工作检索和七维判定；本角色只是重点，不是定向评审或抽查授权。第一遍重建实际内容，第二遍核查正确性，第三遍带着独立领域地图综合评价。分段读取须读到文件末尾；记录实际检查范围，不能用标题、摘要或作者声望替代正文证据。

## 必须先读的技能和规范

主代理已完整读取以下技能和参考。每位subagent仍需自行读取其完整内容后执行：

- `/Users/bytedance/.trae-cn/skills/academic-survey-review/SKILL.md`及其`references/`下六个文件：`review-workbook.md`、`report.md`、`presentation.md`、`correctness.md`、`coverage-and-bias.md`、`synthesis.md`。
- `/Users/bytedance/.trae-cn/skills/academic-writing/SKILL.md`，以及其`references/review.md`、`structure.md`、`grammar-and-style.md`。
- 工作树`AGENTS.md`、`specs/README.md`、`specs/writings.md`；数学、图表与版式判断再读`specs/notations.md`、`figures.md`、`design.md`、`latex.md`。

研究检索可使用WebSearch/WebFetch；已有原文可用缓存。记录检索式、数据源、日期、范围、纳入排除标准、实际访问层级和停止依据。摘要只能支持摘要明确陈述，不支持方法细节。检索受阻时保留具体限制，不静默略过或把无法核验写成错误。

结构判为通过前必须有同级职责矩阵、主要论证链、适用图表行列依据检查。不要把定义、共同基础、流程阶段和小结一概视为非法并列；判断正文是否解释了它们的职责和关系。严重问题必须有可定位的原句、公式、表格或已核验的一手来源。

## 独立性与写入范围

- 不读取其他审阅者的报告，不给其他审阅者发意见，不再派生subagent。
- 只能写入自己被分配的目录，例如`docs/reviews/recommendation-search-advertising/ch01-a/`。
- 本地数值核验、图像预览或新下载资料使用独立临时目录，例如`build/survey-review/ch01-a/`。
- 不运行共享`build.sh`，不改送审材料。需要PDF图像时用`python3`和PyMuPDF（`fitz`）渲染已有PDF。
- 报告使用中文。结论必须区分已核实错误、证据缺口、可选增强和无法核验，不为凑数报告问题。

## 每位审阅者的交付

在自己的目录创建以下三个文件后再结束：

1. `workbook.md`：按技能工作底稿填完全部适用字段。用结构化事实、证据位置和简短观察，避免长篇思维过程。缺失字段说明不适用或无法核验的具体原因。保存三遍阅读记录、同级职责矩阵、论证链、关键论断台账、检索和领域地图、覆盖与偏差记录。
2. `report.md`：范围、主要发现、七维结论表、关键遗漏与建议、修改顺序、核验限制。每条发现包含严重程度、维度、原文位置与短引文、证据、影响、最小修订方向。结论仅用“通过、部分通过、不通过、无法核验”，置信度仅用“高、中、低”；“无法核验”固定为低。
3. `findings.json`：供主代理合并的结构化摘要，使用下列结构。`findings`可为空，不设问题数量配额；重要问题不可因篇幅压缩而漏报。

```json
{
  "chapter": "01",
  "reviewer": "a",
  "reading_complete": true,
  "search_performed": true,
  "dimensions": [
    {"dimension": "结构与文字表述", "verdict": "通过", "confidence": "中", "evidence": "位置或底稿条目", "limitations": "实际限制"}
  ],
  "findings": [
    {
      "id": "CH01-A-R1",
      "severity": "主要",
      "dimensions": ["分类整理"],
      "location": {"file": "tex/05-applications/03-recommendation-and-search/01-overview.tex", "lines": "20-30", "anchor": "sec:..."},
      "quote": "可定位的原句或公式",
      "issue": "可核验的具体问题",
      "evidence": ["文内依据或外部来源URL及实际读取位置"],
      "impact": "怎样影响理解或结论",
      "recommendation": "最小修订方向",
      "status": "已核实问题"
    }
  ],
  "sources": [
    {"url": "来源URL", "access": "全文/摘要/元数据", "use": "核验什么"}
  ],
  "limitations": ["未核验范围或访问限制"]
}
```

`dimensions`须恰好覆盖七个维度。严重程度仅用“阻断性、主要、次要”；发现状态可用“已核实问题、证据缺口、建议增强”。没有证据的怀疑写入限制或待核验台账，不包装为确定错误。

最终回复主代理：三个交付路径、最重要的发现、七维简表与尚待核验项。主代理将根据原文和证据解决分歧，最终判断不按简单多数投票决定。
