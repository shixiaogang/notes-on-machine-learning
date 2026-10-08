> 历史记录：日期、图号、页码及校验值描述当时版本；当前样式见 `specs/figures.md` 与 `tex/styles/figure-style.tex`。

# 第12—15章六幅图的R7局部维护

2026-10-05。沿用已有TikZ/PGFPlots实现，只按作者点名修改布局与配色。数学定义、构造数值、对象数量、算法关系和文楷Regular保持；这不是一次图像模型重生成。

| 图号 | 可编辑源 | 修订与保持项 |
| --- | --- | --- |
| 12.3 | `../trust-adversarial-training-loops.tex` | 中央框从(67,26)—(95,53)移为(67,27)—(95,54)，`p_theta`放左上角；网络中心(81,40.5)与框中心一致。上下循环端点随框移动，固定与更新参数的两层语义保持。 |
| 13.4 | `../trust-fairness-intervention-mechanism.tex` | 未知标签的虚线记录用浅黄底；“补覆盖”移到新增记录下方，补记录连到已有记录集合的路径改水平。随机选择用一段共享干线与连续分支；阈值左右的折点各距框5mm，预测决策居中。两分支各1/2、训练目标与公平约束保持。 |
| 13.5 | `../trust-fairness-pareto.tex` | 前沿虚线由0.55pt增至1.15pt并用蓝；空心圆与支配箭头沿用蓝色。作者明确指定蓝色，因此优先于单系列默认黄；五候选坐标、200人混淆计数、B支配D与C支配E不变。 |
| 14.3 | `../trust-authorized-execution.tex` | “模型软倾向”合为一行。授权只允许A，归档A与拒绝删除B的控制关系保持。 |
| 15.1 | `../trust-global-local-explanation.tex` | 基准贡献1用黄，支付要求贡献2用蓝，附件贡献4用红，三段配色符合三种语义色规则；比例、总分7、阈值6与四种输入组合不变。 |
| 15.2 | `../trust-counterfactual-nearest.tex` | 拒绝区浅红、当前拒绝点红，批准区浅蓝、批准边界和最近反事实点蓝。投影路径用蓝；边界s+r=3、点(1,1)/(1.5,1.5)、距离1/sqrt(2)与垂直关系保持。 |

这六幅现有图注未以颜色名绑定对象，因此没有正文或图注文字需要同步修改。图13.4书内入口仍为`trust-fairness-intervention-stages.tex`，它直接载入上述169×54mm机制源。

## 校样与真实矢量导出

独立校样`build/volume1-r7-trust/proof.tex`由现有`figures/02-foundations/03-trustworthiness/tikz/trust-vector-proof.tex`复制，再追加13.5、15.1、15.2三页；用项目固定的字体、模板及颜色覆盖入口编译，成13页PDF。因为校样目录比常规build多一层，索引样式参数用`../../tex/styles/book-index.xdy`。本轮校样无Overfull、缺字、未定义控制序列或编译错误。六幅彩色细节及13.4/15.2灰度实际查看通过：标签无重叠，框内对象有边距，箭头方向和分支连续。

已有10组`figures/vectors/trust-*.pdf/.svg/.png`从同一13页校样的前10页重导出；导出算法沿用`figures/02-foundations/03-trustworthiness/tikz/trust-vector-export.py`，仅将校样路径改为R7目录，允许后面有追加检查页，并按原10个名称过滤尺寸检查。PDF/SVG均为真实矢量、0栅格对象；PDF字体含嵌入程序，SVG含真实字形路径、明确mm尺寸。PNG只作为300DPI预览。13.5、15.1、15.2以源文件直接嵌入书页，本轮未新增它们的正式独立矢量资源。

数值与导出检查分别见`build/volume1-r7-trust/six-layout-validation.json`、`validation.json`、`fonts.json`、`objects.json`、`dimensions.json`；相应源与正式导出SHA256集中保存在`trust-r7-layout.json`。上述结论是独立图验收；最终第一卷书页、图注、正文、边注与分页由全书构建后另行复查。

## R7最终书页验收

最终第一卷PDF的SHA256为`c5e59bb621d8ab6ae90f061af3cb4de001207e6eb1c68b03472e0c92a44c6dde`。本组六幅实际印刷页分别为334、355、357、378、393、401；已逐页查看完整书页，居中、配色、标签、连线、图注/正文/边注关系均PASS。另复查第4—9章33幅图，共39幅实际书页。逐图记录与页码、图像指纹见`build/volume1-r7-trust/final-book-review.md/.json`。此次验收只读，源和数学构造保持冻结。

最终第17章局部排版修复重构后，直接从最终PDF重渲染本组及第4—9章39个完整图书页，全部PNG字节SHA与已验收页一致，以上书页PASS结论保持。图源和独立导出未变化。
