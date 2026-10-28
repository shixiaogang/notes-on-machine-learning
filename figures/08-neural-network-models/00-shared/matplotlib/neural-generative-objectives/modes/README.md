# neural-generative-modes

两个面板使用同一个双峰目标分布。左图候选集中在两个峰之间，右图候选只覆盖右侧峰。目标密度用蓝色虚线，候选密度用绿色实线，二者的样本空间与坐标尺度相同。

这是作者构造的解析教学示例，不是模型训练实验。`data.json` 保存定义与参数，`curves.csv` 保存逐点计算结果，`generation.json` 记录代码、输入、字体和成品校验值。

在项目根目录运行 `python3 figures/08-neural-network-models/00-shared/matplotlib/neural-generative-objectives/generate.py`。使用共享绘图工具加载仓库中的真实字体：中文思源黑体 Normal，英文与数学 Fira Math；仅 Fira 缺字时使用 STIX Two Math。字体许可证见 `fonts/licenses/`。PDF 与 SVG 为矢量导出，PNG 为 220 dpi 预览。原生尺寸 159 × 66 mm，按原生宽度引用时主体文字保持 8 pt。
