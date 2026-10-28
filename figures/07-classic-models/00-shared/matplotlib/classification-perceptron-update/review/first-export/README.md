# 感知机的一次更新

`data.json` 保存六个教学点、更新前的权重与偏置、当前错分正类点和学习率。生成脚本按正文的增广更新同时计算权重与偏置，用计算得到的参数画边界，不手工决定线的位置。

运行 `python3 figures/03-models/01-classic-models/matplotlib/classification-perceptron-update/generate.py`。两面板使用相同坐标范围和物理比例，蓝圆为正类，红方为负类，浅蓝区域为正类预测区域，虚线为旧边界，绿色实线为更新后边界。黑色空心圆标出触发更新的点。

图为 112 × 77 mm，正文按 112 mm 引用，主标签为真实字体 8 pt。`checks.json` 核验增广更新、得分增加与边界交点；`generation.json` 记录图源、数据和字体哈希；`font-and-page-check.json` 记录物理尺寸、PDF 字体和裁切检查。独立图通过后，仍需由全书构建检查图注与书页布局。
