# regression-svr-epsilon-tube

用真实 ε-SVR 对偶 QP（SLSQP，$\epsilon=0.35$，原问题$C=100$，对偶盒上界$C/n=10$）求出的拟合线与容忍带。10 个确定性点按求解后的乘子标注三类：带内样本乘子为零（蓝点）、带边界样本 $0<\alpha<C/n$（红点）、带外饱和样本 $\alpha=C/n$（红圈）；断言通过 KKT 互补松弛条件。

在项目根目录运行 `python3 figures/04-classic-models/00-shared/matplotlib/regression-svr-epsilon-tube/generate.py` 复现图像、数值数据和检查记录。图像原生尺寸与正文引用均为 105.412 × 78 mm，主体字号为 8 pt；沿用项目公共色板与真实字体，不改共享绘图工具。复现需用户环境已安装 `scipy`。

输入与计算结果见 `data.json`，数值断言见 `checks.json`，生成环境与字体见 `generation.json`，来源与校验值见 `provenance.json`。独立图已目视检查，最终书页检查由完整构建完成后补充。
