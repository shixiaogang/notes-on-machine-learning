# “知识的获取”部分正文设计

## 目标

依据 `plans/efficient-knowledge-use-outline.md` 完成第三卷第八部分“知识的获取”的七章正文。交付范围包括正文、公式、31 幅 TikZ/PGFPlots 图、24 张 LaTeX 表格、文献引用、部分入口和全书编译产物。

正文必须完整落实大纲中已经确定的章节边界、讲解顺序、贯穿案例、图表职责和适用条件，不擅自增加新的同层分类，也不把大纲中的关键机制缩成方法清单。

## 文件组织

部分入口保留在 `tex/03-paradigms/02-efficient-knowledge-use/part.tex`，正式标题改为“知识的获取（Knowledge Acquisition）”，并依次引入：

- `01-knowledge-acquisition-overview.tex`
- `02-human-knowledge-acquisition.tex`
- `03-rule-based-knowledge-acquisition.tex`
- `04-model-based-knowledge-acquisition.tex`
- `05-data-derived-knowledge-acquisition.tex`
- `06-knowledge-fusion.tex`
- `07-knowledge-quality-assessment-and-correction.tex`

图形源文件统一放入 `figures/`，文件名以 `knowledge-acquisition-` 开头。表格直接放在所属章节中。参考文献最终集中合入 `tex/references.bib`。

## 写作分工

七个章节分别交给七个独立 subagent。每个章节代理只修改自己的章节文件、对应图形文件和独立的临时 BibTeX 片段，避免并行修改共享入口与主文献库。章节代理需要：

- 严格覆盖大纲中本章的全部标题和内容要求；
- 以章首问题组织正文，并在独立的“本章小结”中回应；
- 给出大纲要求的定义、公式、算法过程、教学例子、成本与失效边界；
- 完成该章规划的全部图表，图与正文相互解释；
- 只引用可核验的一手论文、权威教材或官方资料；
- 使用语义化且全书唯一的标签；
- 保留未知、不适用、弃权、候选和已核验结果之间的区别。

## 图表设计

31 幅图全部使用可编辑的 TikZ/PGFPlots 源文件，不使用占位图或生成式图片。图形采用项目已有的 `FigureInput`、`FigureModel`、`FigureOutput`、`FigureLoss`、`BookInk`、`BookTeal`、`BookBlue`、`BookAmber`、`BookMuted`、`BookPaper` 和 `BookRule` 色彩语义。颜色不是唯一编码，主路径、候选关系、反馈和未确认关系同时用线型、标记或位置区分。

图中的数值只用于可复算的教学示例，并在图注中说明，不绘制虚构实验曲线。普通图优先正文宽度，只有横向比较或高密度多面板图使用通栏环境。24 张表格均取消段首缩进，不使用竖线，并按大纲指定的比较维度组织。

## 统稿与共享资源

章节初稿合入主工作树后，由一个独立汇总 subagent 负责：

- 更新部分标题与章节入口；
- 合并并去重各章参考文献；
- 统一“知识、候选知识、标签、监督信号、来源、弃权、未知”等术语；
- 统一花卉识别与短文本实体两个贯穿案例；
- 检查章间前置知识、交叉引用、回指和后续入口；
- 检查第 6 章融合与第 7 章质量改进的反馈关系；
- 修正局部重复、概念提前使用和不一致符号；
- 完成首次全量编译并修复编译错误。

## 独立评审

统稿完成后并行启动五个只读评审 subagent，分别检查：

1. 大纲覆盖、章节边界和图表数量；
2. 技术定义、数学公式、算法条件和反例；
3. 历史事实、引用对应关系和来源可靠性；
4. 中文表达、概念依赖、章间衔接和术语一致性；
5. LaTeX 结构、标签、交叉引用、表格、图形和版面风险。

评审结果汇总为一份按严重程度排序的问题清单。一个修订 subagent 统一处理全部确认问题，避免五个评审者并发修改相同文件。修订后重新执行静态检查和全书干净编译。

## 验收

- 七章均存在，标题层级与大纲一致，并各自包含独立的 `\section{本章小结}`。
- 31 幅图和 24 张表均已实现、在正文中引用且无重复标签。
- 所有引用键均存在于 `tex/references.bib`，无未定义引用或缺失文献。
- 没有新增影响阅读的 overfull box、图形裁切、文字遮挡或表格首行缩进。
- `./build.sh clean` 与 `./build.sh` 均成功，最终 `build/main.pdf` 可读。
