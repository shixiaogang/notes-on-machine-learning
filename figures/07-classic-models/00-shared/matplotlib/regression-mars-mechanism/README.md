# regression-mars-mechanism

MARS 机制教学图（确定性一维构造，无随机种子）。生成脚本：`python3 figures/07-classic-models/00-shared/matplotlib/regression-mars-mechanism/generate.py`。

- (a) 两条铰链 $(x-t)_+$、$(t-x)_+$ 与折点 $t$；
- (b) 前向两步：Friedman 成对规则（候选折点 $t$ 同时加入两条铰链并重估全部系数），按真实最小二乘 RSS 下降最大者挑选；图例给出各步 RSS；
- (c) 后向删基：RSS/n 与 GCV 对比，GCV 为 $\mathrm{RSS}/n/(1-C/n)^2$，Friedman 有效参数 $C=M+dM$（$M$ 为非常数基函数数、每基函数惩罚 $d=2$，本一维加性示例；$n=41$，序列中最大 $C=12<n/2$）；
- (d) 两铰链乘积 $(x_1-3)_+(7-x_2)_+$ 只在矩形 $x_1>3,\ x_2<7$ 内非零。

数据为解析式教学构造（折点 $x=4$ 的分段线性目标加固定 $0.04\sin(2.5x)$ 波纹，$x=0..10$ 步长 0.25 共 41 点），非真实实验。全部 RSS/GCV 由生成器内最小二乘算出，见 `data.json`、`generation.json`、`checks.json`。
