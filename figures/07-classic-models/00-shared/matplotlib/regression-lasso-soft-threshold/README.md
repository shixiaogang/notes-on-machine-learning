# regression-lasso-soft-threshold

正交设计（$X^{\top}X/n=I$）下岭回归与Lasso的单坐标收缩曲线：岭 $w_j=c_j/(1+\lambda)$，Lasso 软阈值 $w_j=\mathcal S_\lambda(c_j)$，$\lambda=0.5$。阈值带内 Lasso 精确取零，岭连续缩小全部坐标。

在项目根目录运行 `python3 figures/07-classic-models/00-shared/matplotlib/regression-lasso-soft-threshold/generate.py` 复现图像、数值数据和检查记录。图像原生尺寸与正文引用均为 105.412 × 78 mm，主体字号为 8 pt；沿用项目公共色板与真实字体，不改共享绘图工具。

输入与计算结果见 `data.json`，数值断言见 `checks.json`，生成环境与字体见 `generation.json`，来源与校验值见 `provenance.json`。独立图已目视检查，最终书页检查由完整构建完成后补充。
