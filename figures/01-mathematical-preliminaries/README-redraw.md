# 卷一图像复现

2026-10-11 修订。卷一原有 129 幅编号图按当前规范重绘，其中包括函数空间章的 8 幅非浮动图；本轮另补充 7 幅图、2 张表，并扩展第十七章已有的对象对照表。当前共 136 幅编号图。资源索引中的 `is_addition` 保留历史分类，不能据此推算本轮新增数量。

正文使用数据图、简单图和组合图的 PDF，或无字模型背景与真实字体合成的 PNG。图源、精确数据、导出文件和生成记录位于各部分的 `matplotlib/`、`tikz/`、`generated/` 子目录。跨部分生成器只保留一份；当前对象、源文件和正文资产对应关系见 `00-shared/resource-manifest.json`，执行路由见 `00-shared/matplotlib/redraw-reproduction/registry.json`。

在所属 worktree 根目录运行，例如：

```sh
python3 figures/01-mathematical-preliminaries/00-shared/matplotlib/redraw-reproduction/replay.py v1-prelim-minimum-infimum --proof-dir build/figure-replay
python3 figures/01-mathematical-preliminaries/00-shared/matplotlib/redraw-reproduction/replay.py v1-functional-query-tree --proof-dir build/figure-replay
python3 figures/01-mathematical-preliminaries/06-mathematics-and-machine-learning/generated/static-learning-process/typeset.py
```

数据图与简单图的 `--proof-dir` 将复核输出写入本 worktree 的临时目录。共用 Matplotlib 源文件的图按源文件组执行，保留当前导出的科学数组；有随机过程的示例读取已冻结的数据，不重新抽样。简单图按真实源文件名导出并安装正文实际引用的文件，查询树的 `query-tree.pdf` 也纳入路由。两张组合图分别使用 TikZ 几何和 Matplotlib 数值面板，再以 PyMuPDF 合成 PDF。

复杂图保留实际模型生成的无字背景、提示词、参考图和各轮来源。每图的 `labels-source.json` 与 `typeset.py` 决定真实字体、位置和字号。排字重放使用已保留的背景，不再次调用模型；全局入口目前不支持复杂图的 `--proof-dir`，默认执行会改写该图的派生输出。隔离复核应复制背景和标签定义后使用同一排字模块。模型生成本身不保证像素一致。

表示定理图与因果推前图已分别改用 TikZ 和精确 Matplotlib 源，不再执行旧生成式目录。因果图的两点先验、后验与推前概率由 `04-random-variables-distributions-and-causality/matplotlib/causal-two-point-pushforwards/` 中的有理数输入决定。卷积变换机制图以及温度、静态学习和交互学习图使用保留的模型背景。

共享样式位于 `figures/00-shared/academic-drawing/`。字体仅使用项目 `fonts/` 的思源黑体 Normal、霞鹜文楷 Regular、Fira Math，以及仅补缺失数学字形的 STIX Two Math。当前五色与固定浅底按 `specs/figures.md`；模型背景的近似偏差另行记录。复现环境见 `00-shared/matplotlib/redraw-reproduction/dependencies.json`，需要 Matplotlib、NumPy、Pillow、fontTools、PyMuPDF，以及 TikZ 所需的 XeLaTeX、xdvipdfmx。缓存只写各 worktree 的 `build/figure-proofs/`。

原生输出、实际书页和文字审查分开记录。`00-shared/reviews/`、`00-shared/matplotlib/redraw-ch01-09/` 与 `00-shared/matplotlib/redraw-ch10-16/review-20261011/` 保存作者检查、独立意见及修订闭环；最终集成记录绑定当前源文件、正文资产和 PDF。`scripts/render_volume_one_figure_pages.py` 仅收集实际图页、字号与哈希，不自动判断科学含义或视觉质量。旧日期记录描述当时版本，不作为当前验收结论。
