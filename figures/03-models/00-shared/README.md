# 卷三图像源与复现

本目录记录已接入正文的 224 张图：157 张数据图、简单图或混合图，59 张已有复杂图，以及 8 张补图。正文只引用各部分归档下的 figure.pdf 或 figure.png。

数据图和简单图在各部分的 matplotlib 或 tikz 目录归档。data.json 保存真实数值或解析关系；data-definition.json 标识精确几何或有限构造，并指向 source.tex。公共数值程序位于本目录 matplotlib，沿用原始数值、解析式和离散节点，没有用模型替代数据曲线。

复杂图和补图在各部分的 generated 目录归档。保留模型背景、完整提示词、参考记录、实际无字合成画布、真实字体文字层与标签。composite-canvas.png 是最终文字层实际叠加的无字底图；replay-config.json 与 labels.json 是当前排字输入。历史 generation 中的工作区路径只追溯旧生成记录，不作为复现入口。当前 production_source 和 production_recipe 使用仓库相对路径。

所有字体从仓库根 fonts 读取，不逐图复制。思源黑体 Normal 用于中文主标注，文楷用于注释，Fira Math 用于英文、数字和数学；只有 Fira Math 缺失的数学字符按已批准规则使用 STIX Two Math。共同配色和数学字体规则来自 figures/00-shared/academic-drawing。

在仓库根执行以下命令：

    python3 figures/03-models/00-shared/matplotlib/reproduce.py --route data
    python3 figures/03-models/00-shared/matplotlib/reproduce.py --route simple
    python3 figures/03-models/00-shared/generated/replay.py --check-only

前两条分别复现数值图与 TikZ 图。最后一条将复杂图排字复现到独立 build/figure-replay-check，并核对最终 RGB 像素哈希；去掉 --check-only 才会覆盖归档成图。可添加 --key 指定一张复杂图。排字程序仅叠加真实字体，不描摹、填色或清理模型图像。

Python 运行依赖：NumPy、Matplotlib、Pillow、fontTools、PyMuPDF；TikZ 依赖 XeLaTeX、Poppler 和项目既有 TeX 环境。具体字体哈希与绘图输入见 resource-manifest.json、各图 generation.json 和 data.json。仓库根 build.sh 用于定位项目根及正文构建。

SNN 补图中的真实阶跃与替代梯度曲线由 plot_surrogate_panels.py 和 analytic-data.json 保留。模型负责机制图案，函数曲线是解析式的 Matplotlib 输出，panel-placement.json 保留准确嵌入位置。

所有复杂图优先使用全宽 figure*，保持已确认图案和排字。书页缩印的最终视觉检查由串行集成构建完成；print-size-check.json 提供筛选信息，不把编译成功或名义字号当作视觉通过。
