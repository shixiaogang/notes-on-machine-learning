# 卷二数据图与简单框图复现

本目录保存 53 张重绘图的数据/数学事实输入与生成程序。`archive.json` 记录各图实际归档位置，正文使用各部分 `matplotlib/<key>/figure.pdf` 或 `tikz/<key>/figure.pdf`，不用预览 PNG 代替矢量 PDF。

从仓库根目录运行：

```sh
python3 figures/02-foundations/00-shared/matplotlib/redraw/render_all.py
```

也可先重算全部 Matplotlib 图及混合图的连续面板，然后只编译选定的 TikZ 图：

```sh
python3 figures/02-foundations/00-shared/matplotlib/redraw/render_all.py --only trust-feature-attribution
```

`--only` 只筛选 TikZ 编译；数值面板仍先重算。`--skip-charts` 用于面板 PDF 已存在时。所需 Python 库见 `requirements-replay.txt`，实际环境见 `dependencies.json`；系统需要 XeLaTeX/xdvipdfmx。统一样式来自 `figures/00-shared/academic-drawing/`，实际字体与许可证来自根 `fonts/`。旧共享 matplotlib 样式保留供其他正文资源使用，此目录不依赖旧共享样式。

`facts/` 和 `baseline-source.tex` 保存可核查的原数据、公式、离散坐标，重算而非复制旧成品。`fact-source-index.json`、`adapted-function-provenance.json`、`science-notes.json` 说明示意数据和模型假设；七张混合图的连续数据由 Matplotlib 计算，节点/框/箭头由 TikZ 排列。一般不会修改正文文件。`generation.json` 的当前命令与 hash 指向实际归档，早期预览记录是历史证据。

第 7 张补图 `online-feedback-order` 为独立 TikZ 源，单独重建命令：

```sh
mkdir -p build/figure-replay/online-feedback-order
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build/figure-replay/online-feedback-order figures/02-foundations/01-basics/tikz/online-feedback-order/figure.tex
```

重新编译正文由项目 `build.sh` 完成；本目录重放不等同于全书构建校验。
