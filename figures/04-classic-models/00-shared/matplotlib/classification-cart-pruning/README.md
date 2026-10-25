# classification-cart-pruning

代价复杂度剪枝的教学序列。(a) 四棵候选子树代价 $J_\alpha(T)=\widehat R(T)+\alpha|L(T)|$ 的下包络在切点切换最优子树；(b) 最优子树随 $\alpha$ 分段常值，训练误差随剪枝上升，教学验证误差在 $T_2$ 段最小，取代表值 $\alpha^*=0.04$。

教学构造（非真实实验）：四棵嵌套子树 $T_0$（4 叶，$\widehat R=0.10$）、$T_1$（3 叶，$\widehat R=0.12$）、$T_2$（2 叶，$\widehat R=0.16$）、$T_3$（1 叶，$\widehat R=0.30$）；相邻代价相等切点 $\alpha_k=(\widehat R(T_{k+1})-\widehat R(T_k))/(|L(T_k)|-|L(T_{k+1})|)$ 代入得 $\alpha=0.02,0.04,0.14$，最优子树在 $[0,0.02),[0.02,0.04),[0.04,0.14),[0.14,\alpha_{\max})$ 上依次为 $T_0,T_1,T_2,T_3$；教学验证误差在四段依次为 $0.22,0.19,0.18,0.33$，每段高于同段训练误差，$T_2$ 段最小。

在项目根目录运行 `python3 figures/04-classic-models/00-shared/matplotlib/classification-cart-pruning/generate.py` 复现图像、数值数据和检查记录。图像原生尺寸与正文引用均为 159 × 66 mm，主体字号为 8 pt；沿用项目公共色板与真实字体，不改共享绘图工具。

输入与计算结果见 `data.json`（含每棵子树叶数、训练误差、regime 边界、最优子树 per regime、教学验证误差、切点公式），数值断言见 `checks.json`（切点值、相邻代价相等、验证最小在 $T_2$ 段、训练误差非降），生成环境与字体见 `generation.json`，来源与校验值见 `provenance.json`。独立图已目视检查，最终书页检查由完整构建完成后补充。
