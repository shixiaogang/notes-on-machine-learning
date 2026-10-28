# 卷十仍待补充的随机谱与概率估计知识

本文件只保留卷十使用、在当前数学卷仍待进一步建立的内容。卷一的确定性分析、代数、几何、信号与图算法补充已落实到现有正文；卷二已补齐成像噪声与方差稳定化、概率变换、稳健抽样、分布比较、编码与率失真等前置。相应当前提要见卷一[第一部分 数学对象、计数与极限](../01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization.md)、[第二部分 线性空间](../01-mathematical-preliminaries-upper/03-linear-spaces.md)、[第三部分 微积分](../01-mathematical-preliminaries-upper/04-calculus.md)、[第四部分 最优化](../01-mathematical-preliminaries-upper/05-optimization.md)，以及卷二[随机变量、分布与因果响应](../02-mathematical-preliminaries-lower/01-random-variables-distributions-and-causality.md)。已完成项不再列为待办。

以下仍是用户要求暂存的补充清单，不是新增章目。每项只列尚缺的具体联系；已有前置应直接回用。相机、颜色标准、辐射度量、Hough、Hu不变量、CABAC具体实现和BD-rate等领域内容继续在卷十使用处自足说明。

| 待补内容 | 尚需建立的对象、条件与论证 | 卷十用途及建议位置 |
|---|---|---|
| 平稳随机信号的功率谱与维纳估计 | 在明确周期或无限序列模型下，由平稳协方差连接功率谱/互谱与频率去相关，再推逐频率线性MMSE。卷一的循环对角化及卷二已有条件高斯/均方估计作为前置回用，不重新列缺。 | 图像复原`sec:vision-restoration-deconvolution`；卷二`chap:random-sequences-and-processes`的平稳过程，并与统计估计衔接。 |
| 平稳高斯过程的Rice结论 | 在路径光滑、非退化及所需可积条件下建立零交叉/极值密度，说明相关函数导数或滤波核能量的计算形式；不由“平稳高斯”名称自动推出。 | 特征章Canny单一响应准则；卷二`chap:random-sequences-and-processes`。 |
| AR(1)下DCT近似KLT的条件 | 明确有限块协方差、相关参数和边界假设，解释精确KLT与DCT近似之间的关系及范围。正交变换保持各向同性高斯噪声，以及软阈值的确定性最优性已经有依据，不再列缺。 | DCT变换编码的随机最优性解释；卷二随机过程与卷一信号表示之间的接口。 |
| 离散梯度的随机估计比较 | 在同一期望目标下比较得分函数估计、路径重参数、连续松弛及STE各自计算的对象、偏差与方差条件。回用已有score、采样积分和STE前后向定义，不把已有名称重复当作缺口。 | VQ与学习压缩训练；卷二随机过程/统计推断或随机优化接口。 |
