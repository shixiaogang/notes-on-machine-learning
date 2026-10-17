# 图像资源索引

资源采用与 `tex/` 相同的卷、部分目录，再按制作方式分为 `tikz/`、`matplotlib/` 和 `generated/`。输出格式不决定分类：TikZ 的 PDF、SVG 和 PNG 预览仍随图源保存；采样数据与其生成脚本随实际使用它们的图组保存。

跨部分复用的图组、生成器及记录位于各卷 `00-shared/`；跨卷工具可放入根级 `00-shared/`。当前共用字体、五种柔和语义色、Matplotlib 与独立 TikZ 导出入口位于 `00-shared/academic-drawing/`。第一卷与第二卷按现行规范重绘；第三卷的历史成图须以其记录确认适用样式。复杂图组的子目录按内容命名，保留源文件、数据、生成参数与预览。跨部分生成器旁的 `assets.json` 指明各成图的实际归档位置，由 `figures/00-shared/resource_paths.py` 解析；各部分独用的成图不会因为共用脚本而留在共享目录。

## 现有资源

- `01-mathematical-preliminaries-upper/` 与 `02-mathematical-preliminaries-lower/`：数学两卷图源，各三部分。
  卷二于2026-10-17新增20幅解析教学图，覆盖八章的概率、因果、状态演化、控制、价值与策略比较及学习分析；各部分的`matplotlib/`子目录保存独立源码、解析参数、矢量成图与预览，使用位置登记在共用图像接入清单中。
  同日第二轮另按具体概念障碍增补15幅图，集中解释条件平均、统计推断、跳跃对齐、隐藏位置、机制复合与动态可行性等问题，不设各章数量配额；图源分别归入所属部分的`tikz/`和`matplotlib/`，保留原有推导及既有图像。
- `03-foundations/`：基础、理论与可信性三部分资源。
- `04-classic-models/` 与 `05-neural-network-models/`：不设部分，按制作方式归档。
- `06-probabilistic-graphical-models/`：表示、推断、学习与典型模型四部分。
- `07-reinforcement-learning/` 与 `08-knowledge-learning/`：对应正文分部的 TikZ 图源及记录。
- `10-image-and-multimodal-processing/`：图像、视频和多模态三部分的31份历史 TikZ 图源，分别位于对应部分的 `tikz/`；迁移保留原图的科学内容与绘制方式，样式仍沿用历史内联接口。
- 卷九、卷十一和卷十二尚无独立图像；新增时按实际章节建立目录。
- `00-shared/mathematical-generators/` 与 `00-shared/model-generators/`：跨卷共用生成器与图组记录。

## 使用与追溯

- 以正文实际的 `\input`、`\includegraphics` 和数据路径确认图的用途；所有路径相对项目根目录。
- `generated/` 保留大模型生成素材、提示词、模型信息及修改记录。旧文件名中的 `volume1`、`v1rN` 指旧五卷版本的基础卷，现归卷三，不是当前数学卷的编号。
- `records/` 中的阶段图号、页码、日期与哈希只描述记录时的版本。迁移后文件路径已更新，历史校验值不代表当前源文件；当前验收使用完整构建和成品清单。
- 当前图的源文件、数据、导出预览和提示词随图保留。已替换的历史素材由 Git 追溯；清理前必须检查生成器、组合图与其他正文是否仍依赖，不能只根据本轮正文调用删除；历史记录中的旧素材链接指向清理前的 Git 版本，可在那里追溯。新增资源遵循 `specs/figures.md`。
