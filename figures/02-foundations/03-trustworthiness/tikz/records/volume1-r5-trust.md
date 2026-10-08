> 历史记录：日期、图号、页码及校验值描述当时版本；当前样式见 `specs/figures.md` 与 `tex/styles/figure-style.tex`。

# 第10—14章真矢量重建与配色维护记录

日期：2026-10-05。R5依据作者“真实矢量”和文楷Regular要求，重建七幅先前由内置模型设计并核验的架构图，同时维护12.2认证几何和13.2公平对照。它是**依据已确认模型设计的矢量重建**，并非image_gen直接输出SVG，也没有将PNG嵌进SVG/PDF冒充矢量。原R3/R4原生图片和完整提示词记录保留在`figures/scenes/`，纯章首场景11.1、13.1、14.1仍使用原生图片。下文保留R5重建过程；当前配色与新增验收见R6维护段。

## 源与书内尺寸

| 图号 | 相对figures的可编辑源 | 书内布局尺寸 | 科学结构与本轮修改 |
|---|---|---|---|
| 10.2 | `trust-three-layers.tex` | 169×66 mm | 三层、三个问题和责任对应；横线不是算法箭头。 |
| 10.3 | `trust-decision-consequences.tex` | 110×56 mm | 固定同一预测，隔离与删除两分支，收件人后果不同。 |
| 11.2 | `trust-uncertainty-sources.tex` | 169×61 mm | 固定模型的结果分布对照三个候选模型；概率.2/.5/.8及条长准确。 |
| 11.6 | `trust-conformal-construction.tex` | 169×85 mm | 独立训练固定f、s，再用校准残差排序；n9、α.2、k8、q.8；区间端点f±q。 |
| 12.2 | `trust-certified-region.tex` | 110×73 mm | 填充在轴下；轴连续；负例点离开轴；去图内底部证明式，条件仍在正文/图注。 |
| 12.3 | `trust-adversarial-training-loops.tex` | 169×84 mm | 内层固定θ增大KL；外层CE+βKL更新θ；分布条仅示意，无实测数值。 |
| 13.2 | `trust-fairness-incompatibility.tex` | 168×45 mm | 三项比例的分母和精确计数保留；全长同为40mm；去重复基准/独立式/结论行。 |
| 13.4 | `trust-fairness-intervention-stages.tex` | 169×54 mm | 三阶段机制独占全宽；两支独立等概率阈值；泛指R(f)，不是未经说明的经验风险。 |
| 14.3 | `trust-authorized-execution.tex` | 110×66 mm | 模型提案与执行外硬边界；A可归档，B删除被拒；没有B通向执行结果的边。 |

当前13.4直接引用`trust-fairness-intervention-mechanism.tex`，三阶段机制为169×54mm，整图不再附右侧ROC。精确ROC源与PDF/SVG继续保留为独立资源，构造及随机阈值例子仍在正文。R5历史布局曾采用112mm机制与54mm ROC并列；R6按作者反馈扩宽机制。13.2从强制专题页改为可与正文衔接的全宽浮动图`[htbp]`，图内高度由96mm收拢为45mm；准则的冲突条件与边界保留在图注。

## 实现与字体

- 书内直接引用TikZ源，文字、对象边界、小图标路径和连线同次布局；不存在事后遮住模型文字的白底文字贴片。
- 七幅模型重建的中文采用仓库`LXGWWenKai-Regular.ttf`，通过第一卷`foundation-visual-overrides.tex`选择文楷Regular；英文与数字随既有Source Sans 3体系，数学随TeX的STIX2体系。模块名、阶段名和普通标签均不使用粗体；显式标签字号9 TeX pt，数学下标按常规数学排版缩小。
- 11.6的九残差面板用Matplotlib独立生成`trust-conformal-residuals.pdf/.svg/.png`，保存输入JSON、解析规则、代码和元数据。它使用全部九个构造残差，无抽样、平滑、拟合或过滤；参数与横纵位置由数值计算。主文字9pt，柱顶数字8.5pt；数学采用Matplotlib的STIX字形。
- 三阶段机制、邮件、文件、文件夹、时钟、垃圾桶、模型内部网格都为真实路径；复用小图标源为`trust-vector-icons.tex`。
- 当前默认单强调色为黄`#D6B35D`，两种为蓝`#7998AD`与红`#D57B70`，三种为蓝、红、黄；分别配近白填充`#FFF1CF`、`#EDF2F5`与`#F8E8E5`。灰、白承担轮廓、连接和中性底板，不计语义强调色。颜色来自项目共享命名色，第一卷覆盖样式维护兼容别名；普通模型框保持白色或近白底。

## 输出与复现

独立成图为`figures/vectors/trust-*.pdf/.svg/.png`。PDF包含矢量路径与嵌入字体，SVG含从实际嵌入字体导出的真实字形路径，PNG仅是300DPI预览。独立导出采用内容紧裁加4pt安全边，尺寸可与书内布局框略不同；书内直接使用源布局，**不缩放这些紧裁预览来实现9pt标签**。

独立校样源：`figures/02-foundations/03-trustworthiness/tikz/trust-vector-proof.tex`。在项目根目录编译到`build/volume1-r5-trust/figures-proof.pdf`后运行`figures/02-foundations/03-trustworthiness/tikz/trust-vector-export.py`。导出程序保存`fonts.json`、`objects.json`、`dimensions.json`和`validation.json`，SVG不含`<image>`、PDF不含栅格XObject；当前10个校样面板共0个栅格对象，全部书内宽度适合112或169mm。10个面板包含9幅书图，以及13.4机制源的一页独立校样。

11.6残差可运行`figures/02-foundations/03-trustworthiness/matplotlib/trust-conformal-residuals.py`再生；参数文件为`trust-conformal-residuals-data.json`，版本和字体记录见`trust-conformal-residuals-metadata.json`。LaTeX编译不执行绘图脚本，直接使用已保存的矢量面板。

## R5历史自检

逐图查看真实PDF渲染。修正了初稿中横轴i的下边界裁切、13.4下路1/2与分叉线相碰、多个子路径仅最后一段显示箭头、TeX末尾空白增加布局宽度等问题。R5当时的10页独立校样无Overfull、缺字或未定义控制序列；所有必要对象、方向、计数、公式和条件已核对，PASS。

通用验证器对Matplotlib Type3字体报告“possibly unembedded”：这是不能通过extract_font返回字节直接识别Type3造成的非阻断提示。另按CharProcs字形程序流核查，均有实际嵌入内容；PDF实际渲染与TeX导入后的残差/ROC字符可见，且不存在栅格字形替代。本轮不将空字节误认作未嵌入，也不忽略真实渲染验收。

独立图校样通过不替代全书浮动体验收；根代理统一重建后仍需复查实际书页、图注、正文穿插与边注。

## R6配色维护与独立校样

2026-10-05，按作者新增规则维护已有矢量源。双色对照统一蓝、红；单强调的输出区间使用黄；三职责和三干预阶段按蓝、红、黄排列。简略神经网络每层使用同一实色填充，输入、中间、输出三层依次蓝、红、黄，填充不再混成近白；内部连接保持灰线。这套层颜色由`trust-vector-icons.tex`统一实现，图11.2的固定模型和三个候选模型也逐层填色。网络内部的层编码与全图比较对象的颜色分开理解。

图13.2中两群体始终为u蓝、v红；共同的TPR/FPR条用中性灰，避免把群体颜色再用于资格类别。图13.3两组混淆矩阵分别用近白蓝、近白红，预测与真值仍由行列标签确定。图11.6的精确残差面板保留普通残差蓝、选中残差红，区间面板用黄；训练和校准卡片保持白底。这一早期配色维护阶段保持所有比例、样本计数、函数值、坐标、布局尺寸和连接方向。后续局部布局调整见下一段，科学数值与连接关系仍保持。

本组10对正式PDF/SVG已重导出，与第16—17章的7对合计17对。10页校样无溢出、缺字或编译错误；17个PDF均无栅格对象，所有字体具有嵌入程序，SVG不含image元素且宽高明确以mm标注。联合检查记录为`build/volume1-r6-trust/export-validation.json`，源检查记录为`build/volume1-r6-trust/source-review.json`。这些是独立图验收，最终书页的正文、图注与边注关系另行检查。


## R6局部布局修订

根据作者补充反馈，根代理完成以下四项局部布局调整。修改沿用文楷Regular、真实矢量对象和蓝红黄层序，没有增加科学关系或示例数值。

| 图号 | 当前调整 |
| --- | --- |
| 10.2 | 每层的层次、问题、责任三个框使用同一近白底色，三层依次蓝、红、黄，使横向对应更明确。 |
| 11.2 | 三个候选模型f_i标注放到框内左上角；右侧输出条及其数值向右移5mm，条长与概率0.2、0.5、0.8保持。 |
| 12.3 | 中央模型框高度由35mm缩为27mm，p_theta与内部网络靠近；输入、输出、内外循环端点随框边移动，连接语义不变。 |
| 13.4 | 移除图中的右侧ROC，将三阶段机制从112mm扩为169mm，增加阶段内和阶段间距离；ROC构造保留在正文例子与独立资源。 |

上述源已重新编译十页独立校样并重导出十对正式PDF/SVG。当前图13.4与其单独机制校样同为169×54mm。根代理的最终全书构建和书页检查另行记录，独立校样不代替正文、图注与边注的版面验收。
