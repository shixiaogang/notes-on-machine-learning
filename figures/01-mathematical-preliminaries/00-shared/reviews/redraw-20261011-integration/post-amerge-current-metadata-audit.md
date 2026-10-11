# Amerge后当前136图登记的只读复核

本记录取代此前 `/private/tmp/active-drawing-metadata-and-fill.patch` 与 `/private/tmp/active-auxiliary-alpha.patch` 对「当前应修」的判断；两旧补丁**不得应用**，保留仅作合入前版本的审计历史。A合入后的科学源已有更完整的固定浅底与颜色分工，不能按旧快照回滚。

审计ROOT树`.worktrees/space-chapters-outline`，全局`integration-manifest.json`的volume1记录136条，与`redraw-reproduction/registry.json`的136条一致。下述是实际阅读当前构图调用、相邻记录代码和正文引用后的结论，没有写入ROOT树。

## 已由新源解决，当前不再修填色

- `analysis-concepts/.../plots.py:105`，`fig:analysis-metric-convergence`右面板：现在`BLUE_FILL`不透明输出邻域，已没有灰色alpha。
- 同源130–131，`fig:analysis-continuity-counterexamples`：自变量邻域为`BLUE_FILL`、函数值邻域为`YELLOW_FILL`，不透明交叠不产生新色。当前函数曲线为BLUE，完整保留δ/ε、空心边界点与严格邻域解释。保留当前科学分工，不替换成我旧建议的统一灰底。
- `geometry-cech-rips-intersection/source.tex:5–6`：全部蓝固定浅底先画，所有圆周／顶点后画，无opacity；当前顺序已经正确，不加旧patch。
- `concepts-analysis-functional/.../plots.py:78`的`simple_integral()`为`GREEN_FILL`；160的`hull_relaxation()`为`BLUE_FILL`。原数组、边界和最优面语义保持，旧固定fill字符串已消除。
- `teaching-analysis/.../plots.py:76`的`fat_square()`为`GREEN_FILL if gamma <= 1 else RED_FILL`，正／负间隔组合的颜色区分是A新版科学说明的一部分，必须保留；不能回滚成旧快照中的同一种绿色。
- 旧六个`#EDF4F0`固定定义已从active canonical源消除。analysis-geometry及analysis-concepts现在导入真正BLUE/GREEN/YELLOW/PURPLE，不再有旧GREEN-as-YELLOW假设；一阶近似GREEN、二阶近似PURPLE的当前正确`color_roles`完整保留。

## 当前透明度复核

从136条当前资源的source依赖追踪显式Artist alpha/set_alpha与TikZ opacity，仍出现的视觉属性只有：preimage图`fill opacity=1`、legend`framealpha=1`（均已不透明）；以及`teaching-linear-probability/…plots.py:52`位于不输出到正文的旧`cech_rips()`的alpha=.72。后者只列历史／非正文支路，不修；该模块实际正文路线为核可辨别性图，无此透明填充。

`concepts-dynamics:149`和`dynamics:155`的alpha=.75是CVaR参数；`concepts-probability:100`标签alpha=.2为固定步长；新增`opt-pareto-weighted-sum/source.py:16`标签alpha=1/2是标量化权重的等值线。均是科学量，保留。当前正文没有剩余需要改为不透明的显式区域alpha。字形抗锯齿的RGBA文字层不在本次区域填充范围。

## 仅剩当前生成器元数据／注释

精确新版补丁：`/private/tmp/post-amerge-current-metadata-only.patch`。9个当前源／标注源、22处元数据与注释替换。每处位置、原文、新文、当前与建议SHA256见`post-amerge-current-metadata-only.json`。Python AST／JSON语法核验通过；该事实只证明语法，没有声明重放、数学或书页验收。

1. `concepts-dynamics/concept-plots.py`保存函数仍把一系列指定YELLOW、两系列指定BLUE/RED，与当前BLUE/GREEN两系列实际调用不符；旧`scope`称按用户请求不编译／不看书页，也不适用于当前任务。改为共享五色**政策**和由每图真实artist-data／typography／绑定人工审查决定实际样式的说明；区分解析构造、外部人工验收与编译。不能把生成JSON当自动通过。当前字体角色直接取`style_record()['fonts']`。
2. `dynamics/dynamics-plots.py`同样过时系列声明；当前kalman和卷积等实际为BLUE/GREEN，保持不变。保存函数的生成器basename与总记录中不存在的`figures/00-shared/academic-drawing/dynamics/dynamics-plots.py`改成当前实际ROOT-relative源路径。已有准确`book_compilation`边界说明保持。
3. `teaching-dynamics/reader-plots.py`旧checks仍写只看单图／没有正文编译，改成导出不建立人工／书页接受；当前note导入、BLUE/GREEN/PURPLE的卷积块／交区及note字号均不改。
4. `probability-discrete/plots.py`总记录仍按系列数宣称YELLOW或BLUE/RED，实际已有BLUE/GREEN/PURPLE。换五色政策及逐图真实证据，保留所有现行Artist颜色／热图域。
5. `concepts-probability/plots.py`总记录仍把中文仅声明WenKai，遗漏主体SourceHan与显式缺字STIX；改共享真实字体角色。总记录的`plots.py`basename改当前实际ROOT-relative源路径，旧三色集合换政策说明。
6. `analysis-geometry/plots.py`与`analysis-concepts/plots.py`总记录只列三色，遗漏当前GREEN/PURPLE；改政策与逐图证据说明，字体角色取共享真实路径，8pt主体与7.5pt说明的尺度政策完整记录。保留当前颜色映射，不做任何旧YELLOW别名替换。
7. 三个现行typeset源已读：static/interactive的显式数学缺字范围已准确，不再修改；温度图typeset注释与其`labels-source.json.layout_notes`仍错误说旧script𝓔/𝓜，改为共享单字显式mathcal𝒞/ℋ/𝒦/ℰ/ℳ范围，并说明温度图实际没有这些STIX标签。只改说明，不改字体代码、标注或排字。
8. 三个动态组保存函数中固定`date`／`created=2026-10-06`继续生成 fresh记录容易被误读为本轮执行日期；保留原日期值，字段明确成`construction_origin_date`，不造当前执行日期或当前人工验收时间。

本新版补丁不含旧flat baseline `probability-discrete/sources.json`：它保留旧生成历史事实，当前canonical元数据另在回放路径导出。也不含不在正文的旧reachable_directions红底清理。它不改变任何Artist调用、真实颜色角色、公式、数组、坐标、尺寸、字体渲染、图注或正文。

root串行实施后仍需重放受影响组以更新generator SHA与当前记录，并执行最终源的构建／一致性及实际页面验证。root3最终书页独立复核保持待办，之前预审PDF不作为本轮最终PDF接受依据。
