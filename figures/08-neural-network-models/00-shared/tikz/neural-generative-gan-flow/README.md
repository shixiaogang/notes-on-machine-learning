# GAN 的前向计算

噪声经生成器变为生成样本。生成样本与真实样本分别进入同一个判别器，由判别器输出真假评分。图中来源标签 0 和 1 是训练判别器时使用的监督标注，不是网络输入。所有箭头只表示前向计算，参数更新与梯度反馈由正文解释。

在项目根目录运行 `python3 figures/08-neural-network-models/00-shared/tikz/neural-generative-gan-flow/generate.py`，只编译本图，不启动书籍构建。`source.tex` 保存五个计算节点和连线，`wrapper.tex` 独立加载仓库中的思源黑体 Normal 与 Fira Math，不改变书籍数学字体；字体许可证见 `fonts/licenses/`。

`data.json` 保存节点、边和标签的语义，`generation.json` 保存源文件、字体及成品校验值。PDF 与 SVG 为矢量导出，PNG 为 220 dpi 预览。原生尺寸 112 × 55 mm，按原生宽度引用时主体字号保持 8 pt。书页中的最终引用和排布由章节整合任务验证。
