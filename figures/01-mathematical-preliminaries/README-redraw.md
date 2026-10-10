# 卷一图像复现

本次归档接入111张已有图与5张补图。正文使用实际导出的PDF（数据图、简单图、组合图）或PNG（模型背景加真实字体）；原有图标签保留。

图像源、精确数据或解析定义、最终成品、生成记录和预览审查结果位于各部分的 `matplotlib/`、`tikz/`、`generated/` 子目录。跨部分的共同生成器保留一份；具体对应关系见 `00-shared/matplotlib/redraw-reproduction/registry.json`。

从项目根目录运行：

```sh
python3 figures/01-mathematical-preliminaries/00-shared/matplotlib/redraw-reproduction/replay.py v1-prelim-minimum-infimum
python3 figures/01-mathematical-preliminaries/00-shared/matplotlib/redraw-reproduction/replay.py v1-prelim-preimage-inverse
python3 figures/01-mathematical-preliminaries/06-mathematics-and-machine-learning/generated/static-learning-framework/typeset.py
```

数据与简单图可追加 `--proof-dir build/figure-replay`，将复核成品写入本工作区的临时构建目录。跨图共用一个Matplotlib生成器时，该入口会重绘该生成器覆盖的全部数据图；数值数组与解析公式保持原定义，不作重采样或平滑。两张组合图逐面板采用TikZ几何与Matplotlib数值曲线，再以PyMuPDF合成矢量PDF。

复杂图保留实际模型生成的无字背景、提示词、送入模型的外部参考图及来源、各次生成记录。`labels-source.json`与`typeset.py`确定当前文字位置、字体、字号与颜色；重放排字不会重新生成背景，也不会清除背景纹理。因果补图的五个概率面板由 `probability-data.json`与 `build_probability_panels.py`精确生成；模型不决定概率柱高。

统一样式依赖 `figures/00-shared/academic-drawing/`，字体仅使用项目根 `fonts/` 中的思源黑体Normal、霞鹜文楷、Fira Math与仅补Fira缺失数学字形的STIX2。字体许可证与共享样式由统一集成保留，不在各图重复复制。环境依赖为Python 3.9以上、Matplotlib、NumPy、Pillow、fontTools、PyMuPDF，以及TikZ复现所需XeLaTeX与xdvipdfmx。

`generation.json`给出当前相对路径、源文件与最终图像散列和可重放命令。`generation-preview.json`明确保留历史预览记录，历史机器路径只用于追踪实际生成调用，不是当前复现入口。生成模型调用具有随机性，其图案不保证重新生成时逐像素相同；保留背景之后的排字和确定数值面板可以重放。

预览审查与正文集成后验收是两个阶段。已有 `review.json`记录模型机制、文字与图案避让、原尺寸及1100px预览检查；整书版面和成品一致性由统一集成后的七版构建核验。
