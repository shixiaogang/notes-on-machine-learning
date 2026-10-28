# 第3章模型图标修订记录

- 日期：2026-10-05。
- 工具：Codex 内置 `image_gen`；具体模型标识未公开。
- 用途：概念插画中的模型图标，非解剖图、精确网络拓扑或实验结果。
- 输入：现有半监督和持续学习插画，仅要求改变图标内部纹路。
- 后处理：未修改图像内容，原始输出直接复制到项目；旧素材保留。
- 最终文件：`paradigms-semi-supervised-signals.png`、`paradigms-continual-memory.png`。
- 核验：半监督的两路信号汇入同一分类器；持续学习保留相同图标分区，填充逐阶段积累。其他场景、对象与路径保持原有分工。两图最终以112mm宽排入书中，内部纹路同时用形状、位置与填充区分。

## semi

```text
Use case: precise-object-edit. Image 1 is the edit target. Change ONLY the interior pattern inside the small brain icon in the center of the navy learning device. Keep the brain's outer silhouette and central fissure, its size and position, the two surrounding gears, the device, all input cards, arrows, output card, paper texture, colors and every other object exactly as they are. This brain is a conceptual learning-model glyph, not biological anatomy. Replace generic gyri with a legible two-channel motif: one pale blue interior branch with small FILLED circular nodes on the left and one warm cream interior branch with OPEN ring nodes on the right, visibly converging toward one central node. This signifies labeled and unlabeled learning signals jointly entering the SAME classifier; do not imply two classifiers. Use few broad clean strokes readable at 112 mm total-image print width. No text, formulas, extra icons or new objects. Preserve landscape 3:2 composition and sharp edges.
```

## continual

```text
Use case: precise-object-edit. Image 1 is the edit target. Change ONLY the internal patterns of the three little brain icons inside the three teal devices. Keep their brain outer silhouettes, size, central fissures, positions and ALL other objects, cards, arrows, device contours, colors, background texture and composition unchanged. The three devices depict the SAME learner evolving across time, so use one consistent internal architecture in all three brains. Replace generic spokes with a few broad connected memory-cell chambers, using a clear dark-teal contour and cream strokes: at stage one one cell has a warm amber center; at stage two keep that amber cell and light up a SECOND chamber in pale blue; at stage three retain both and light up a THIRD chamber in muted coral. Visually show accumulation of retained knowledge, not deletion, unrelated different architectures or exact neuron counts. Make strokes legible at 112 mm total-image print width. Concept glyph, not biological anatomy or measured network. No text, formulas, extra icons or new objects. Preserve landscape 3:2 composition and sharp edges.
```
