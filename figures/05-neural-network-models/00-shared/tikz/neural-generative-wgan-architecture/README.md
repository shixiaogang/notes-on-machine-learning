# neural-generative-wgan-architecture

Native size: [150, 93] mm; include at width=150mm (figure*), scale 1, main labels 8 pt.

WGAN保留生成器与共享评价器的双网络结构，将来源概率改为不经过sigmoid的实数评分。下方显示两种不同的评价器训练约束：原WGAN裁剪评价器参数；WGAN-GP在真实与生成观测之间抽取插值点，再惩罚同一评价器对这些点的输入梯度范数偏离1。下方约束只用于训练评价器，未增加生成器层，也不是生成样本的输出后处理。

Reproduce independently: `python3 figures/05-neural-network-models/00-shared/tikz/neural-generative-wgan-architecture/generate.py`. Source, scientific edges, source papers and actual style references are recorded in source.tex/data.json; font versions, SHA-256, licenses and canvas checks in generation.json. Standalone figure QA only; book-page review belongs to parent integration. Original neural-generative-gan-flow is preserved.

## 生产退役（2026-10-13）

用户要求本章的架构示意全部由大模型生成。此目录的原生图源和三格式成品完整保留，仅用于拓扑核对与历史复现；新的生产资源位于 `figures/05-neural-network-models/00-shared/generated/neural-generative-architectures/wgan`。不再将本目录成品接入正文。
