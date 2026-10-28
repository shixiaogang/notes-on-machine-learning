# DCGAN architecture

Include `figure.png` at `width=150mm` in a `figure*`; the corresponding raster PDF is also provided. Native raster is 1619 × 971 px, displayed at 150 × 89.96 mm (about 274 ppi). Main labels are approximately 8 pt; normalization/activation notes are approximately 7.5 pt, with exact effective sizes recorded in `generation.json` and `labels.json`.

Generator: latent 100 → projection 4×4×512 → transpose-convolution stages 8×8×256 → 16×16×128 → 32×32×64 → 64×64×3. Hidden generator outputs use BN+ReLU, final output tanh.

One discriminator receives real or generated samples separately: 64×64×3 → 32×32×64 → 16×16×128 → 8×8×256 → 4×4×512 → scalar sigmoid. First convolution uses Leaky ReLU without BN; later hidden stages use BN+Leaky ReLU. These channel counts are teaching choices rather than a universal DCGAN specification. Drawn sheet counts are schematic, not actual channels.

Caption draft: DCGAN的生成器逐级扩大空间尺寸，判别器通过带步幅卷积逐级缩小空间尺寸。图中通道数是一组教学配置；叠片只表示多通道，不对应实际片数。判别器的真实与生成图像是分别输入的两种来源，不作通道拼接。生成器末层使用tanh，判别器末层输出单一来源概率；隐藏层的归一化与激活配置分别标在尺寸链下方。

Source: Radford, Metz and Chintala, arXiv:1511.06434, submitted 2015, ICLR 2016. https://arxiv.org/abs/1511.06434

The built-in image generator was given the three actually inspected CNN/Transformer references; `prompt.txt` and the targeted `prompt-revision-1.txt` preserve the prompts. `background-v1.png` is the original output; `background.png` is the selected corrected output. Tool model/parameters were not exposed and are not invented. `text-layer.png` is a transparent true-font overlay. Reproduce typesetting: `python3 figures/08-neural-network-models/00-shared/generated/neural-generative-dcgan-architecture/render.py`. Background is never recolored or redrawn by this script.

Standalone figure review is in `review.json`; actual book-page review belongs to parent integration.
