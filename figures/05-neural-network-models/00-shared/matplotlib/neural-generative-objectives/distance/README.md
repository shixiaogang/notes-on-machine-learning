# neural-generative-distance

比较位于 0 与 a 的两个点质量分布。Wasserstein-1 距离随位移连续变化，JS 散度在任何非零位移处都是 log 2。空心点排除 a=0 时的 log 2，实心点表示该处的实际值 0；虚线的两侧分别绘制，没有连接上下跳变。示例对应 WGAN 原论文的分离支持集现象。

这是作者构造的解析教学示例，不是模型训练实验。`data.json` 保存定义与参数，`curves.csv` 保存逐点计算结果，`generation.json` 记录代码、输入、字体和成品校验值。

在项目根目录运行 `python3 figures/05-neural-network-models/00-shared/matplotlib/neural-generative-objectives/generate.py`。使用共享绘图工具加载仓库中的真实字体：中文思源黑体 Normal，英文与数学 Fira Math；仅 Fira 缺字时使用 STIX Two Math。字体许可证见 `fonts/licenses/`。PDF 与 SVG 为矢量导出，PNG 为 220 dpi 预览。原生尺寸 112 × 55 mm，按原生宽度引用时主体文字保持 8 pt。
