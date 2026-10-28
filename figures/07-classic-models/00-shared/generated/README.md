# 经典模型历史插画

2026-10-12按用户提供的时间线版式和人物插画风格制作。背景由内置imagegen生成，人物与历史工作均为示意；正文仍以邻近的一手文献说明历史归因。

- `classic-models-history/`：保留无字背景，用项目字体叠加六个时段的标注。`python3 classic-models-history/typeset.py`可从保留背景复现字体层与最终PNG；需要Pillow与fontTools。图内数字与英文为Fira Math，中文标题为思源黑体Normal，说明为霞鹜文楷。
- `least-squares-observations/`：观测与共同估计场景。
- `iris-measurements/`：鸢尾花测量场景。

每个目录保留`prompt.txt`、`background.png`、`figure.png`、`generation.json`、`review.json`及参考来源。两幅场景插画不含文字，最终PNG与生成背景像素一致。参考图用于本次工作中的版式或风格指导。

旧的TikZ历史图保留在`../tikz/classic-models-history/`，正文已改为本目录中的新时间线。
