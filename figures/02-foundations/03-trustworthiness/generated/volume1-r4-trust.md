# 第10–14章追加机制图：R4

日期：2026-10-05。工具：内置 image_gen；具体模型、尺寸参数、seed、quality 均未暴露。中文与英文按思源黑体 Regular、Source Sans 3 Regular 的外观提示生成，并不宣称嵌入这些字库。科学事实来自本书对应正文；参考图仅迁移视觉表达。

## 10.2：三层职责

核心问题：读者如何区分可信主张的要求、证据与运行责任，而不把三者合成一个性能指标？最终宽度169mm。

对象/标签：三行“属性与规范”“证据能力”“威胁与生命周期”；同层“关键问题”与“责任主体”。三行职责依次对应任务责任方/受影响者/领域规则、技术论证/复核边界、有权主体决策/运行处置。横线为无方向的同层对应，不表示算法执行流；不跨行添加因果或授权边。

科学难点：技术证据不能自动代替授权决策；角色图标不能暗示已通过验证。候选初稿右列文档勾号被编辑为中性记录横线。保留问题、角色，删除重复解释进入图注。最终资产：https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/03-trustworthiness/generated/v1r4-trust-three-layers.png。组合源：figures/02-foundations/03-trustworthiness/tikz/trust-three-layers.tex。

## 13.4：三阶段干预 + 精确ROC

核心问题：何处改变数据、学习规则、分数到服务的映射，以及随机阈值为何能产生新的期望错误率？模型机制面板112mm；独立Matplotlib54mm；间隔3mm，总宽169mm。

对象/标签：数据记录、虚线未知标签记录（?）、补覆盖、核标签、训练网格、min_f R(f)、Δ(f)≤η、分数、随机选择、阈值1、阈值2、两条1/2分支、唯一合并输出ŷ。箭头：记录→训练→分数→随机选择→两阈值→预测决策。补覆盖箭头进入记录集合。不得增加真实标签→选择器的边。

科学难点：未知标签不能当失败；预测ŷ不是保证获选；固定一半随机化独立于真实标签；各阶段措施可以组合，但不保证单项达标便产生系统公平。初稿“获选”改为ŷ、移除大上下留白、将全图标签变为明显常规字重。最终资产：https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/03-trustworthiness/generated/v1r4-trust-fairness-intervention.png。组合源：figures/02-foundations/03-trustworthiness/tikz/trust-fairness-intervention-stages.tex。

定量面板独立：https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/03-trustworthiness/matplotlib/trust-fairness-roc.py、trust-fairness-roc-data.json、trust-fairness-roc-metadata.json；输出PDF/SVG为真实矢量，PNG仅预览。坐标均按正文示例构造，第一组阈值(0.1,0.5)/(0.3,0.9)，等权混合(0.2,0.7)，第二组点亦(0.2,0.7)。共用零原点、0–1范围、等比例坐标；线段为凸组合可达区域，不拟合确定性ROC曲线，不将构造写成实验。模型未生成或覆盖ROC数值面板。

PDF字体兼容性：仓库思源黑体OTF为CFF，Matplotlib Type42 PDF虽然可提取中文、列出嵌入字体，却在真实PDF渲染中漏掉中文字形。改为Type3矢量字形后，已检查独立PDF和LaTeX导入校样，全部中文恢复。Type3的CharProcs实际字形程序已检查有内容；通用验证器用extract_font检查时会给“possibly unembedded”误警告，不能据此认定缺失。SVG保留路径字形，源字体文件未改。

最终尺寸：三层图1922×818px，169mm宽，约288.9有效DPI；公平机制2097×750px，112mm宽，约475.6有效DPI。保留原生像素，没有上采样或改DPI标签。ROC物理54×54mm，字体8–8.5pt。两图组合宽均169mm，校样无Overfull、缺字或未定义控制序列；见build/volume1-r4-trust/figures-proof.pdf、dimensions.json、fonts.json与review.md。按物理尺寸比较，模型原生普通标签约7.5–9pt外观，阶段名略大，全部水平常规字重；该估计不是可编辑字体字号声明。

最后一轮局部编辑减细训练面板数学与输出ŷ的原生字重，保留正文泛指风险R(f)，未增加经验风险帽号；中文、位置、上下标、拓扑不变。

## 保留图的理由

按实际引用审阅10–14章21图。10.1集合关系简单且准确；11.3校准曲线、11.4计数与11.5完整经验风险、12.1/12.2允许集合及认证几何、12.4有限候选、13.2公平条件/人数、13.3混淆矩阵与分母、13.5有限Pareto候选、14.2代理解析曲线均已有可复现实现，此轮无科学或版式缺陷，不因工具迁移重绘。已通过R3的5张原生机制图和3张章首场景保持。14章当前实际引用只有14.1–14.3，不添加无来源14.4。

## 完整提示词与修订链

### intervention-math-weight

```text
VERY LOCAL TYPOGRAPHY EDIT, preserve all correct geometry, native Chinese labels, arrows and scientific topology. The current Chinese is now correctly Regular weight. ONLY the training-panel mathematics is still too black/bold relative to Chinese. Replace current min_f R(f) and Δ(f)≤η with the EXACT SAME mathematical content, size, baseline and position in clearly thinner NORMAL-weight scientific math, about30–40% thinner strokes: min must be upright normal roman, NOT bold; lower italic f stays BELOW min; R and both f are ordinary unbold italic; Greek Δ and η and ≤ are normal unbold symbols. Output ŷ must likewise be normal italic lowercase y with thin hat, not bold. Probability1/2 labels regular thin. Do not alter characters: objective remains min_f R(f), not empirical hat R; fairness constraint remains Δ(f)≤η. The book uses generic riskR(f). No new labels. Keep all existing correct Chinese 数据/训练/决策/补覆盖/核标签/分数/随机选择/阈值1/阈值2, question mark, plus symbol. Keep exact two1/2 probabilities and merge of the two threshold nodes into uniqueŷ output, all line endpoints and frames unchanged. Maintain current Regular Chinese and crisp darkgray substantial architecture lines. Font reference for mathematics STIX2 normal as in a textbook, not presentationbold. Pure white nodes/canvas, light flat tabs, no overall title. This is ONLY a text weight correction, not a redesign.
```

### layers-first

```text
中文机器学习教材中的三层职责科研架构，最终印刷169mm宽。用三条水平泳道组织层次—问题—责任的对应，不是计算流程；禁止画跨泳道箭头、循环或线性阶段管线。三行泳道中心严格对齐，顶端仅3个短列标“层次”“关键问题”“责任主体”，没有全图标题。第一行左模块原生标签“属性与规范”，中部两行“必须满足什么？”“对谁、在什么范围？”，右部两行“任务责任方”“受影响者·领域规则”。第二行左模块“证据能力”，中部两行“假设支持什么结论？”“还缺什么证据？”，右部两行“技术人员：论证”“复核者：边界”。第三行左模块“威胁与生命周期”，中部两行“谁能使主张失效？”“何时限制、回退？”，右部两行“有权主体：决策”“运行责任方：处置”。每行只有左侧清楚的窄角色框与简短标签，中部问题由小型文件/放大镜/时钟线条图标辅助，右部责任角色用很小的文件复核图标辅助；图标不能替代文字或占据大画面。左模块到问题、问题到角色仅用中性细水平关联线，无箭头，表示同一行对应关系，不假称数据流。不得添加任何未列文字/连接。白底，普通模块白色深灰轮廓#444444，线条最终1pt左右；只有左侧小模块可用浅米色#FDEEDA或冰蓝#D9EAEF，第二行局部结构可以用极浅蓝灰#EAEEF6；不能整行铺色，不能按输入蓝/模型紫/输出绿分配大色块。字体原生生成，中文外观参考思源黑体 Regular，英文数字参考Source Sans3 Regular，全部水平基线、常规字重，用字号而非加粗区分层次。所有标签应以最终8–10pt的可读性设计，相当于1860px宽图上36–42px em，禁止Bold/Black/Semibold、斜字、超小字。线条关系与必要文字为主体，白色留白为分组，不是卡片流水线。宽幅约2.35:1，清晰扁平矢量外观，无阴影、渐变、3D、纹理、装饰、图注、水印。
```

### layers-edit

```text
Edit this existing three-swimlane scientific diagram locally. Preserve all correct labels, objects, alignments, neutral no-arrow horizontal correspondence lines, and absolutely no cross-row connection. REQUIRED changes only: (1) Each of the three right-column document icons currently has a checkmark. Replace EVERY checkmark with three short neutral parallel horizontal record lines inside the existing folded-page outline. There must be ZERO ticks, shields, certification symbols or pass indicators. These icons designate accountable roles, not proven results. (2) All text must be clean horizontal NORMAL REGULAR weight, thinner than current bold-looking row labels: Chinese appearance Source Han Sans SC Regular, Latin Source Sans 3 Regular. Use size and spacing, never bold, for hierarchy. (3) All fills flat uniform: white canvas and question/role boxes, pale beige #FDEEDA first-row left box, near-white bluegray #EAEEF6 second-row left box, iceblue #D9EAEF third-row left box. Dark-gray substantial crisp outlines #444444. No gradients/shadows, no large overall title. Keep this exact native text:
column headers 层次 | 关键问题 | 责任主体
row1 属性与规范 | 必须满足什么？ / 对谁、在什么范围？ | 任务责任方 / 受影响者·领域规则
row2 证据能力 | 假设支持什么结论？ / 还缺什么证据？ | 技术人员：论证 / 复核者：边界
row3 威胁与生命周期 | 谁能使主张失效？ / 何时限制、回退？ | 有权主体：决策 / 运行责任方：处置
Native labels, no blank text placeholders. Final print width169mm. Text ordinary8–10pt appearance, thin Regular. Retain horizontal aspect ratio and tight reasonable margins. This is a local refinement, do not redesign the scientific relations.
```

### intervention-first

```text
科研线条架构：公平干预发生在数据、学习规则和决策三个位置。仅画机制，不画任何统计曲线/概率条/ROC坐标；右侧ROC将由数据工具作为独立面板制作，故此图不能预留空白绘图框。最终本图印刷宽112mm、高约70mm，三分区纵深清晰而紧凑。白底，全图没有标题，只有必要分区名“数据”“训练”“决策”。主体3个分区水平相邻，从左到右对应实际数据→学习→分数→决策主线，并在区内展开干预；这条数据线不是要求所有干预必须同时使用。数据分区左侧有一小组记录卡与一张虚线缺少记录，旁边新取得的记录带小加号，轻短箭头把新记录加入记录组；必要标签“补覆盖”“核标签”。禁止把未知标签画成错误标签或自动产生补充记录。记录组→训练分区。训练分区为一个白色圆角规则模块，有小型稀疏神经节点图标，原生数学标签“min_f R(f)”与“Δ(f)≤η”，模块→右侧决策分区的分数接口，原生标签“分数”。决策分区分数接口→两个平行阈值小模块（原生标签分别“阈值1”“阈值2”）；这两模块由一个独立随机选择接口控制，原生标签“随机选择”，分别以“1/2”标在两条控制支路上；两个阈值输出→同一个“获选”输出接口。随机选择不接真实标签y，不暗示按尚未观测真实资格选择阈值；不能增加群体标签或人数。必要文字仅以上标签/公式，无解释段落。数值1/2仅为随机操作参数，不画概率数据结果。图的全部文字由模型原生生成，中文外观思源黑体Regular，英文数字SourceSans3Regular，数学正常字重STIX2-like，全部水平基线，所有文字最终8–10pt（1500px宽画布em约48–58px），不能Bold/Black/Semibold，不能歪字或预留文字区。线条、框、端口和箭头为主要信息，图标只是很小辅助。普通框白底#FFFFFF，深灰#444444轮廓1pt、路径1.1pt；局部训练底板极浅蓝灰#EAEEF6，少量分区小标题带浅米色#FDEEDA与冰蓝#D9EAEF；强调蓝#4D88BD仅新增记录与绿色#61B88B仅输出接口，不铺大片蓝紫绿。按1.6:1画布，优先大字与少量清楚模块，禁止阴影、渐变、材质、3D、全图标题、图注、水印。逐分支保持连续且箭头端点不入文字；用简洁圆角连线，不无意义绕行。
```

### intervention-layout

```text
Edit and recompose this scientific LINE ARCHITECTURE diagram into a TIGHT WIDE canvas, approximately 2.8:1 aspect ratio, with only tiny equal outer margins. Eliminate the huge unused white strips above and below; the three panels should fill the canvas height. This will print at only112mm total width, so enlarge all native labels to about8–10pt physically, NOT shrink the current diagram into an empty canvas. Regular Chinese appearance Source Han Sans SC REGULAR, Latin Source Sans 3 Regular, math normal STIX2. Every label horizontal and light NORMAL weight; specifically 数据/训练/决策 MUST lose their current bold weight. No overall title.
Preserve correct mechanism and labels with these changes:
1 Data panel: several neutral record cards, one dashed record marked ? = unknown. Small added record plus curved arrow toward records, native labels 补覆盖 and 核标签. NEVER checkmarks on unknown; no unknown→failure. Supporting icons remain small.
2 Training panel: small node-and-wire mesh within near-white bluegray #EAEEF6 local board, math min_f R(f), Δ(f)≤η, correct lower f under min. Native mathematics must read accurately and horizontally.
3 Decision panel: input 分数 → 随机选择 → two alternative branches with exact fixed 1/2 labels → upper 阈值1, lower 阈值2 → both branch outputs MERGE at ONE final white rounded output node containing the mathematical label ŷ (a lowercase italic y with hat). REQUIRED replace the existing green output label 获选 with ŷ; it represents a binary predicted decision, not a promise every applicant is chosen. The random choice has fixed half probability independent of the true qualification; do not add an arrow from true label or qualification. No extra output or loss branch.
Exact main directed edges: corrected record collection→training mesh; trained score→分数→随机选择; selector→阈值1 labelled1/2; selector→阈值2 labelled1/2; 阈值1→ŷ and 阈值2→ŷ. All arrows must clearly touch endpoint outlines and branch routes stay inside decision panel. No copied ROC graph, coordinates, plots or data bars in this asset; quantitative ROC is a separate vector panel.
Three major panel outlines are white with DARKGRAY #444444 crisp lines with substantial readable visual weight. Small shallow tab of 数据 pale beige #FDEEDA; 训练 iceblue #D9EAEF; 决策 pale beige. Small blue #4D88BD added-record accent, otherwise ordinary modules white. Flat fills, no gradient/shadow/3D. Preserve three-part conceptual sequence without implying every intervention is mandatory. No explanatory sentences within art. Large native labels, about45–55px em at~1800pxwidth, orderly spaces and mathematical scripts. Tight landscape line diagram, no humans, no poster.
```

### intervention-weight

```text
LOCAL TEXT-WEIGHT EDIT ONLY. The current scientific diagram has correct labels, topology, margins and formulas. KEEP all objects and all edges exactly, especially the two1/2 branch probabilities, min lower f, Δ(f)≤η, y-hat output, unknown ?, coverage plus and arrow. The Chinese text currently appears BOLD, especially 数据, 训练, 决策, 核标签 and 阈值. REQUIRED REDRAW ALL TEXT as clearly LIGHTER Regular-weight sans-serif. Chinese mimic Source Han Sans SC Regular: thin uniform vertical stems, ordinary book figure labeling, NOT HeiTi Bold. Latin mimic Source Sans 3 Regular. Top stage names must remain same physical size but reduce stroke thickness ~35–40%. All other Chinese should reduce stroke thickness ~25–30%. Do NOT weaken diagram frame or arrow line weight; only text gets thinner. Math min R(f), Δ(f)≤η, yhat and numeric1/2 use normal unbold scientific math, horizontal. NO overall title, no explanatory new text. One small style adjustment: final output yhat node must be WHITE fill (instead of green), same darkgray outline, keep all geometry. Header tabs flat pale beige #FDEEDA and iceblue #D9EAEF, local training board nearwhitebluegray #EAEEF6. Preserve entire diagram's tight2.8:1 layout. ALL marks native generated; no blank strips. Full exact labels 数据,训练,决策,补覆盖,核标签,分数,随机选择,阈值1,阈值2,1/2,1/2,min_f R(f),Δ(f)≤η,ŷ,?.
```
