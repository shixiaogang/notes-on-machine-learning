# 卷三图像源与复现

本目录索引正文中的 227 张图：112 张 TikZ 图、35 张数值图和 80 张复杂机制图或插图。其中 215 张为已有图替换，12 张为补图。正文引用各部分归档目录中的 `figure.pdf` 或 `figure.png`；HMC 图另使用一份解析数值图作为组合面板。

三类图片统一使用低饱和度色板：蓝色 `#7188A3` 优先，少量绿色 `#829C8B` 和黄色 `#B4A16F`，其次红色 `#A7787D` 与紫色 `#9588A5`。浅底分别为 `#E5EAF0`、`#E8EEE9`、`#F1ECDD`、`#F0E5E6`、`#ECE8F0`。TikZ 规则见 `muted-theme.tex`，数值图规则见 `matplotlib/volume3_style.py`。同一语义保持同色；具有矩阵、像素或因子语义的格子保留原形，普通模块优先圆角。

中文主体使用思源黑体 Normal，说明使用霞鹜文楷 Regular；英文、数字和数学使用 Fira Math。字体从仓库根 `fonts/` 读取，版本、哈希及许可证随资源记录追溯。仅 Fira Math 缺失的数学字符沿已批准规则使用 STIX Two Math。主体字号以书页中约 8 pt、说明约 7.5 pt 为基准。正文引用宽度受原尺寸与字号约束，不因版心空余而放大；各资源的 `display` 记录原宽、引用宽、缩放和字号上界。

数据图保存真实数据、解析式或教学构造及生成程序；简单图保存 TikZ 源和实际编译的 PDF、SVG、PNG。模型不替代精确数据曲线。三幅历史图各保留 14 个发展节点、3 个研究主题及代表文献，时间线间距不表示时间比例。

复杂图在各部分的 `generated/` 目录保存模型无字底图、提示词、实际参考与原始输出、真实字体透明层、标签坐标、排字与复现配置。`replay-config.json` 指定当前实际画布，不能默认旧 `composite-canvas.png` 仍是生产输入。`generation.json` 的 `current_refinement.production_source` 使用仓库相对路径；历史绝对路径仅追溯旧生成记录。`revisions/` 保存本轮之前的成图以及各次生成和选择记录，包含未采纳的结果。

在仓库根执行：

```sh
python3 figures/00-shared/model-generators/matplotlib/reproduce.py --route data
python3 figures/00-shared/model-generators/matplotlib/reproduce.py --route simple
python3 figures/00-shared/model-generators/generated/replay.py --check-only
```

前两条分别复现数值图与 TikZ 图。最后一条在独立的 `build/figure-replay-check` 复现复杂图，并核对最终解码 RGB 像素哈希；去掉 `--check-only` 才覆盖成图。可添加 `--key` 指定资源。排字程序叠加实际字体，不描摹、填色或清理模型图像。

高效注意力图的局部窗口面板由独立 TikZ 图源绘制，保存六行六列支持矩阵、半径和16个有效位置对；其余两面板由模型绘制。复现时重新编译精确面板，再合成到模型预留的空白位置。

SNN 图采用独立组合面板：模型生成机制底图，`plot_surrogate_panels.py` 根据真实阶跃和指定替代梯度解析式生成曲线，`analytic-function-data.csv` 和 `analytic-functions.json` 保存数值、公式、参数及字体信息。复现时重新生成两个精确面板，按 `replay-config.json` 的位置合成，不使用模型画出的近似曲线。

Python 依赖 NumPy、Matplotlib、Pillow、fontTools 与 PyMuPDF；TikZ 使用项目既有 XeLaTeX 环境。资源接入、哈希和图注由 `resource-manifest.json` 与全书 `integration-manifest.json` 记录。编译与像素复现不能代替科学审阅和最终书页视觉检查，当前审阅范围及证据保存在各图评审记录中。
