# 嵌入层接入前馈网络示意图

正文入口：`tex/05-neural-network-models/02-feedforward-networks.tex`，标签 `fig:ffn-embedding-architecture`。实际书页宽169mm，原图1859×846像素，约279.4ppi。

`background.png`与`raw-0.png`为模型第二次生成的无字底图；结构全部由模型生成，未用脚本重画或修补。`revisions/r1/`保留未采用的第一版、实际提示词和退回理由。`prompt-r2.txt`是第二次实际修订指令，实际提供的两张参考图及校验值见`reference-assets.json`。模型具体版本未由工具暴露。

在仓库环境运行`python3 figures/05-neural-network-models/00-shared/generated/ffn-embedding-architecture/replay.py`，按`labels-source.json`坐标用真实字体重放文字层，生成`labels.json`、`text-layer.png`与`figure.png`。依赖Python、Pillow、fontTools以及共享`typeset_common.py`，当前实测版本见`print-size-check.json`；字体文件、版本、许可证与哈希见`font-provenance.json`。

此图是教学结构示意，不含实验测量。K=6、d_e=4、r=2、m=4、c=3；先嵌入后数值拼接。图内6个输入圆只是同一拼接向量的坐标展开。横排小格不改变正文的列向量约定；偏置未单独画出。

独立图、真实字体及最终PDF页面的验收结论见`review.json`与`typography-review.json`。模型色板近似和轻微明暗偏差如实记录于`palette-observations.json`；文字层使用项目准确中性色。
