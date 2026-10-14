# Fisher 投影目标

沿用原 `classification-lda-projection` 的精确八点教学构造，原资源保留。`data.json` 存储均值、共同偏移与比较方向；最优方向由类内散度矩阵的线性方程求得，并归一化。

运行 `python3 figures/04-classic-models/00-shared/matplotlib/classification-lda-target/generate.py`，从实际仓库字体导出 PDF、PNG 和 SVG。共享字体工具只读，不修改。

原生图为 112 × 90 mm，正文按 112 mm 引用，比例为 1，主标签为 8 pt。浅色条表示该类四个样本投影的最小至最大范围，不表示标准差。下方方差为按全部八点作分母的合并类内方差；Fisher 目标仍用散度比计算。

`checks.json` 记录精确几何与比值，`generation.json` 记录图源、数据及字体哈希，`font-and-page-check.json` 记录真实字体、物理尺寸和边界检查。全书书页排版由正文所属构建进一步验收。

`review.json` 与 `review/final-pdf-preview.png` 保存本次独立 PDF 的检查记录。首次导出及对应图源保存在 `review/first-export/`；最终图只拉开投影带与刻度的间距，点集和数值未变。
