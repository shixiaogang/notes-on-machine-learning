# neural-generative-gan-architecture

Native size: [150, 90] mm; include at width=150mm (figure*), scale 1, main labels 8 pt.

GAN的一种全连接实现。生成器把随机输入逐层映射为观测；真实与生成观测进入同一个判别器，隐藏层之后的单一得分经sigmoid变成来源概率。蓝色虚线区域是采样时保留的路径。来源标签用于训练判别器，不是其输入；更新生成器时固定判别器参数，并沿生成路径回传输入梯度。

Reproduce independently: `python3 figures/05-neural-network-models/00-shared/tikz/neural-generative-gan-architecture/generate.py`. Source, scientific edges, source papers and actual style references are recorded in source.tex/data.json; font versions, SHA-256, licenses and canvas checks in generation.json. Standalone figure QA only; book-page review belongs to parent integration. Original neural-generative-gan-flow is preserved.

## 生产退役（2026-10-13）

用户要求本章的架构示意全部由大模型生成。此目录的原生图源和三格式成品完整保留，仅用于拓扑核对与历史复现；新的生产资源位于 `figures/05-neural-network-models/00-shared/generated/neural-generative-architectures/gan`。不再将本目录成品接入正文。
