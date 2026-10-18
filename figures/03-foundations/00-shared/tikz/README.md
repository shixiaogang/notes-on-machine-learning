# 卷三 TikZ 架构与机制图

本轮按用户明确要求，将48幅原位图架构、流程与机制图重新绘制为原生TikZ，统一20幅已有TikZ示意图。用户要求优先于技能默认的复杂图生成路线。保留图1.1、3.2、13.1的情境插画，以及17幅独立数据图；混合图的自然照片、手写数字和人物场景作为独立局部素材嵌入，框、箭头、文字和机制关系由TikZ绘制。旧图及其生成记录保留以供追溯。

`architecture-manifest.json`登记原资源身份、当前图源、正文位置、引用宽度和字体缩放。`architecture-style.tex`集中维护8pt主体、7.5pt说明、低饱和语义色、1.8pt圆角、线条和箭头。模块或真实分组保留框；标题和说明不额外套框，不加顶部色带。

图标取自固定版本的[Lucide](https://lucide.dev/)，原始SVG、源版本、派生说明和许可证均在`icons/`。邮件、文档等语义共用同一图标，神经网络采用统一的原生TikZ图元。极短圆端点线在PDF导出中展开为等价圆点，避免转换器丢失骰点、鸟眼或日历点。无需重新下载即可构建。

字体实际加载仓库中的思源黑体Normal、霞鹜文楷Regular和FiraMath，版本、校验值及许可证见`figures/00-shared/academic-drawing/font-manifest.json`和`fonts/`。独立导出以STIX Two补充实际使用的花体及少量缺字，不改变书籍正文字体。两个新生成的Matplotlib面板保留解析数据与独立脚本，以真实字体字形轮廓输出，避免CFF字体的Type42渲染问题。

复现时先运行图11.3、11.6所在目录的`render-panel.py`，再运行本目录的`render-architecture.py`；不带参数导出全部68幅，亦可给出一个或多个图键。工具在当前worktree的`build/volume-three-tikz-redraw/`串行编译，输出各图旁的PDF、SVG、PNG及物理尺寸记录，并检查缺字和导出期间的源文件变化。

`compare-architecture.py`读取重绘前的资源快照，输出逐图对照PDF；两列采用同一实际引用宽度，重绘侧保留矢量内容。每图的局部样本来源、自审和复读记录与图源同目录；书页验收记录放在`reviews/academic-drawing/2026-10-18-volume-three-tikz/`，不以编译通过替代视觉检查。
