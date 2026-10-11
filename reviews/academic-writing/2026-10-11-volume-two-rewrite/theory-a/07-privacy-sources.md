# AW-THEORY-A-07：关键来源实际核读

2026-10-11，theory_first_half，AI作者自查。正文v1/v2引文键保持原样；此文件只说明以下三项实际访问的原始论文，不宣称17组引文的全部外部论证已复核。未重跑论文实验，不核最新进展或法律义务。

- [Guo等，Certified Data Removal from Machine Learning Models，PMLR论文](https://proceedings.mlr.press/v119/guo20c/guo20c.pdf)：实际读方法、Theorem 3以及Algorithms 1–2相关上下文。核对对象为正则化线性模型；Newton删除更新依赖目标的优化条件，认证还利用训练目标的随机线性扰动，并累计梯度残差，超过预算则重训。支持正文P158–160区分优化误差与输出分布保证；没有把完整外部证明当本章已证明内容。
- [Zhang等，Negative Preference Optimization: From Catastrophic Collapse to Effective Unlearning，作者论文](https://arxiv.org/html/2404.05868v2)：实际读引言、Figure 1解释、方法中当前与参考序列概率的权重，以及保留集损失说明。目标序列概率已经压低后，更新权重趋小；保留损失用于控制效用下降。支持P162的机制与经验定位，未把有限实验升级任意语言模型与重训同分布证书；完整理论推导未复核。
- [Mironov，Rényi Differential Privacy，作者论文](https://arxiv.org/pdf/1702.07476)：实际读定义、后处理段、Proposition 1及相邻证明上下文、Proposition 3转换、Proposition 7高斯机制。核到每个历史下统一同阶界才可自适应相加、转换项为log(1/delta)/(alpha−1)、未抽样高斯按均值位移平方与噪声方差之比计。对应P126–127；正文抽样机制另有条件，并未由此论文片段证明所有抽样放大公式。

DP定义、群体界、随机响应、Laplace密度比、先验例、线性梯度、均值扣贡献及强凸残差界在本章实际公式与前提下作数学核算。Shokri、LiRA、提取、DLG、PATE、安全聚合、可求和遗忘和SISA保留既有技术范围及引用，在本次按正文所声明对象/步骤/条件核查，未独立重审其论文完整证明或协议实现。五张本章图注以及外部联邦图导航已读文字与参数，图像像素、图源程序、系统实验与最终PDF由集成阶段另验，不在本记录结论中冒充通过。
