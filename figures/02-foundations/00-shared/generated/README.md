# 卷二模型图的实际字体排字

正文使用各部分 `generated/<key>/figure.png`。`background.png` 是模型生成的无字底图，`typesetting.json` 选择当前使用的底图；少数背景有透明白底合成或纯白外围留边，未程序清理纹理或描摹模型图元。`text-layer.png` 与 `labels.json` 保留真实字层、位置、字体和上下标。

从仓库根目录运行：

```sh
python3 figures/02-foundations/00-shared/generated/replay_labels.py figures/02-foundations/01-basics/generated/meta-learning
```

以当前 `labels.json` 为准；该命令重放已核准的当前位置。不要使用 `--publication-size` 重放最终出版版，它用于从 `preview-labels.json` 开始试排，可能覆盖后续人工避让修正。字体直接读取根目录 `fonts/` 的思源黑体 Normal、文楷和 Fira Math；没有每图字体副本。依赖为 Python、Pillow、fontTools，版本记录见卷二绘图依赖清单。

每图 `prompt.txt`、`generation.json` 保留模型提示词与真实生成历史；`references/`、`archived-references.json` 保存外部机制/对象参考。历史绝对路径只用于追溯，不是当前运行依赖。`generation.json` 的 `current_reproduction_command` 与 `current_archive_hashes` 指向当前成图；早期布局/字号记录按历史保留。复杂图的模型生成具有随机性，字层则可重复重放。

`review.json` 分开保留机制及图案限制与出版排字核验；模型图纹理等尚存备注不会因排字核验通过而删掉。正文使用全宽 164.6 mm，优先保障实际可读性；拥挤的联邦聚合公式移至原图注，其他机制连线与用户确认的图案保持。
