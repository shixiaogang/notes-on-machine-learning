# 图像资源索引

资源采用与 `tex/` 相同的卷、部分目录，再按制作方式分为 `tikz/`、`matplotlib/` 和 `generated/`。输出格式不决定分类：TikZ 的 PDF、SVG 和 PNG 预览仍随图源保存；采样数据与其生成脚本随实际使用它们的图组保存。

跨部分复用的图组、生成器及记录位于各卷 `00-shared/`；跨卷工具可放入根级 `00-shared/`。当前共用字体、五种柔和语义色、Matplotlib 与独立 TikZ 导出入口位于 `00-shared/academic-drawing/`。第一卷与第二卷按现行规范重绘；第三卷的历史成图须以其记录确认适用样式。复杂图组的子目录按内容命名，保留源文件、数据、生成参数与预览。跨部分生成器旁的 `assets.json` 指明各成图的实际归档位置，由 `figures/00-shared/resource_paths.py` 解析；各部分独用的成图不会因为共用脚本而留在共享目录。

## 现有资源

- `01-mathematical-preliminaries-upper/` 与 `02-mathematical-preliminaries-lower/`：数学两卷图源，各三部分。
  卷二于2026-10-17新增20幅解析教学图，覆盖八章的概率、因果、状态演化、控制、价值与策略比较及学习分析；各部分的`matplotlib/`子目录保存独立源码、解析参数、矢量成图与预览，使用位置登记在共用图像接入清单中。
  同日第二轮另按具体概念障碍增补15幅图，集中解释条件平均、统计推断、跳跃对齐、隐藏位置、机制复合与动态可行性等问题，不设各章数量配额；图源分别归入所属部分的`tikz/`和`matplotlib/`，保留原有推导及既有图像。
  卷一的两集合容斥示意图保留可编辑 TikZ 源、字体已嵌入的 PDF、PNG 预览及解析集合与字体记录，位于第1部分的 `tikz/inclusion-exclusion-overlap.*`。
  卷一第三章另补集合测量与积分的四幅图解：有限与可数覆盖、精确分割、内外逼近（TikZ）及取值分层积分（Matplotlib），图源、解析参数、预览和核验记录随各图保存。
  度量空间节的 `tikz/metric-ball-neighborhood/` 和 `tikz/metric-open-closed-relative/` 分别说明开球与邻域，以及开闭性随母空间改变；保留TikZ图源、字体嵌入PDF与预览。
  卷一第8章《度量空间》于2026-10-23在第2部分新增13幅TikZ概念图，统一归档于 `02-linear-algebra-and-geometry/tikz/metric-spaces/`：三角不等式、伪距离等价类与商度量、子空间弦长、相对球、内部闭包边界、稠密、有限$\varepsilon$网、连续球刻画、Lipschitz锥、双Lipschitz夹逼带、柯西尾部、完备化嵌入与压缩误差收缩；各图保留可编辑源、独立渲染入口、字体嵌入PDF及逐图生成与核验记录。
  集合测量节的 `tikz/measure-abstraction/` 另以关系图对照勒贝格测度的具体构造与一般测度空间的共同结构。
  卷一第三章于2026-10-21新增26幅概念与过程图：18幅Matplotlib解析图、8幅TikZ几何图，分别位于第1部分的`matplotlib/chapter3-concept-processes/`和`tikz/chapter3-concept-processes/`。覆盖极限与误差、局部线性近似、积分截断和换序、路径与曲面、公共边界抵消；解释放在图注，目录内保留生成器、解析参数、矢量成图、预览与逐图核验记录。
- `03-foundations/`：基础、理论与可信性三部分资源。
- `04-classic-models/` 与 `05-neural-network-models/`：不设部分，按制作方式归档。
- `06-probabilistic-graphical-models/`：表示、推断、学习与典型模型四部分。
- `07-reinforcement-learning/`：保留115张重绘图资源，其中113张接入当前正文，按部分保存原生TikZ、Matplotlib数值图与无字生成背景及真实字体排字；当前接入见卷内 `redraw-manifest.json`，复现入口见卷内 `README.md`。
- `08-knowledge-learning/`：对应正文分部的TikZ图源及记录。
- `10-image-and-multimodal-processing/`：图像、视频和多模态三部分的31份历史 TikZ 图源，分别位于对应部分的 `tikz/`；迁移保留原图的科学内容与绘制方式，样式仍沿用历史内联接口。
- `11-recommendation-search-advertising/`：理解、决策、搜索和广告十章使用的 TikZ 图源，按三个正文部分归档。
- `09-natural-language-processing/`：2026-10-18起按部分归档新图，均为TikZ图源，位于各部分的`tikz/`。`01-language-models/`收第2至8章的图（前缀`classical-`、`llm-`、`sft-`、`align-`、`infer-`、`reason-`、`eval-`）；`02-text-analysis-and-organization/`收第9至11章的图（前缀`analysis-`、`extraction-`、`classification-`）；`03-text-generation-and-interaction/`收第12至14章的图（前缀`generation-`、`dialogue-`、`execution-`）；`04-speech-processing/`收第15章的图（前缀`speech-`）。卷九较早的图仍位于`figures/`根目录的`nlp-*`文件，迁移前保持原路径。
- 卷十二尚无独立图像；新增时按实际章节建立目录。
- `00-shared/mathematical-generators/` 与 `00-shared/model-generators/`：跨卷共用生成器与图组记录。

## 使用与追溯

- 以正文实际的 `\input`、`\includegraphics` 和数据路径确认图的用途；所有路径相对项目根目录。
- `generated/` 保留大模型生成素材、提示词、模型信息及修改记录。旧文件名中的 `volume1`、`v1rN` 指旧五卷版本的基础卷，现归卷三，不是当前数学卷的编号。
- `records/` 中的阶段图号、页码、日期与哈希只描述记录时的版本。迁移后文件路径已更新，历史校验值不代表当前源文件；当前验收使用完整构建和成品清单。
- 当前图的源文件、数据、导出预览和提示词随图保留。已替换的历史素材由 Git 追溯；清理前必须检查生成器、组合图与其他正文是否仍依赖，不能只根据本轮正文调用删除；历史记录中的旧素材链接指向清理前的 Git 版本，可在那里追溯。新增资源遵循 `specs/figures.md`。
