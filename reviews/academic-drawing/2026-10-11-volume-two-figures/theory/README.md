# 卷二学习理论图像修订验收索引

范围：理论六章24幅现有图的实质修订，以及一幅新增DS六顶点邻接图，共25图。新增图用交替单坐标无向边说明DS邻接与固定两标签笛卡尔四组合的差别，连接正文六个显式向量；不重复已有Natarajan两点模式图，也不把有限类误说成不可学习。制作方式为8幅数据图、8幅TikZ图、8幅纯模型图及1幅模型背景／真实数据面板混合图。模型图背景必须无字，真实文字层独立；简单关系图不由模型替代，定量数值不由模型决定。

这是本组AI的图像与局部文字自查记录。章级、逐段、逐句记录只覆盖新DS局部正文和随图修改的文字及必要上下文，不称六章全文独立审查。根协调者对two-randomness和DS有单独限定范围复核；其反馈按实际问题闭环保留。

最终证据入口如下。

- [基线逐图问题](initial-review.md)：24幅旧图的实际观察与修订计划。
- [25图原生验收](native-review.md)：逐图科学关系、对象数量、条件、样式与字体观察及闭环。
- [最终书页验收](book-page-review.md)：卷二25图、全集5张代表页、4张灰度页的真实观察；r3四张变化图页已复看。
- [最终资产清单](asset-manifest.json)：正文和成图SHA、实际物理引用宽度、8／7.5pt字号、PDF及页图SHA、物理页与印刷页、r2到r3相同性证据。
- [选定模型版本](selected-model-versions.json)及[完整26次调用](model-calls-complete.json)：真实模型prompt、输入参考、原始输出及候选归档。`model-calls.json`是早期11次调用快照；`asset-manifest-provisional.json`和每图旧generation/review文件是历史记录，不代表本轮最终验收。
- [最终09-muted实际调用](model-call-09-muted.json)：正确平坦性拓扑不变，仅模型重新收敛描边颜色；没有背景填色清理。
- [数据重绘与采样](chart-generation.json)：函数、输入、共享依赖及最终SHA；精确双下降控制点和插值后训练风险严格为0断言保留在数据生成记录中。
- [正文接口与字体审计](source-and-font-audit.json)：六章小结、引用保留、九模型真实字体层、八当前TikZ与共享输入一致性。未引用的六个旧TikZ记录单列，不混入当前数量。
- [默认文件检查](file-validation.json)、[当前Matplotlib矢量字形](matplotlib-vector-font-audit.json)、[最终验证说明](validation-summary.md)与[机器可读验证结果](validation-summary.json)：原样保留默认300DPI警告及Type3提示，实际物理尺寸和字体验收适用边界明确。
- [r3实际书页问题闭环](layout-r3-closure.md)：轴端标记裁切、辅助字偏淡、模型框线偏亮均已修复，并真实复看原生与最终页；[r2问题页与快照](layout-r2-evidence/asset-manifest-r2.json)保留修订前证据。
- 局部写作审查：[C章级](local-writing/C.md)、[P逐段](local-writing/P.md)、[W逐句及E1–E12](local-writing/W.md)、[修复与复读闭环](local-writing/closure-r2.md)。[before](local-writing/snapshots/before/sha256.json)、[after-r1](local-writing/snapshots/after-r1/sha256.json)、[after-r2终稿](local-writing/snapshots/after-r2/sha256.json)记录稳定句段与正文SHA。r3只改绘图和字层，正文仍为after-r2。
- [精确修改文件清单](source-files.txt)：提交内源、图源、候选及审查文件，排除target成品。共同绘图依赖按根协调原样暂存；不含其他组图像成果。

任务工作区`.worktrees/volume-two-figures-theory`，分支`codex/volume-two-figures-theory`，依赖已提交改写`b0ffa7ff`。全部生成、修改、构建与提交均在此工作区，build和target不与其他任务共写。成品构建与提交记录由Git及target构建清单保存；最终集成方须按最终合并输入重新构建。
