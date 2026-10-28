# neural-generative-progressive-architecture

Native size: 112×106 mm; include at width=112mm (figure), scale 1, main labels 8 pt, auxiliary 7.5 pt.

渐进式增长GAN增添分辨率层时的局部结构。生成器混合上采样后的旧输出与新输出；判别器先把两种入口转换成相同分辨率的特征，再混合后送入旧主体。权重α在训练过渡阶段从0增至1，完成后去掉旧入口和旧输出支路；旧主体仍继续训练，并非保留两个独立模型作集成。toRGB与fromRGB是图像通道与特征通道之间的1×1卷积映射。

Reproduce independently with the Python: `python3 figures/08-neural-network-models/00-shared/tikz/neural-generative-progressive-architecture/generate.py`. Only standalone XeLaTeX is run; generation.json binds source/font hashes, versions, licenses, and actual canvas checks. The bibliography and shared manifest are owned by the parent.

## 生产退役（2026-10-13）

用户要求本章的架构示意全部由大模型生成。此目录的原生图源和三格式成品完整保留，仅用于拓扑核对与历史复现；新的生产资源位于 `figures/08-neural-network-models/00-shared/generated/neural-generative-architectures/progressive`。不再将本目录成品接入正文。
