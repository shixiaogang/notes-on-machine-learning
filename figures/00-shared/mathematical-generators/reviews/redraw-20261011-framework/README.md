# 第五、六部分六图重绘

2026-10-11。当前正文引用新目录，旧目录完整保留历史。`semantic-and-visual-review.md` 为本轮作者三遍科学/文字自查；独立复核由其他审者执行，不能把作者检查或旧日期记录当独立验收。机器脚本不输出语义通过结论。

| 对象 | 当前方法与目录 | 图内主体尺度 |
|---|---|---|
| 温度状态、加热与观测 | `05-dynamical-systems-control-decision-and-games/generated/temperature-state-observation/` | 169mm引用宽，8pt |
| 估计状态输出反馈 | `05-dynamical-systems-control-decision-and-games/tikz/observer-output-feedback/` | 矢量169mm引用宽，7.934pt |
| 固定策略与最优Bellman递推 | `05-dynamical-systems-control-decision-and-games/tikz/bellman-policy-and-optimality/` | 矢量169mm引用宽，7.934pt |
| 静态学习 | `06-mathematics-and-machine-learning/generated/static-learning-process/` | 169mm引用宽，8pt |
| 同一环境下交互学习 | `06-mathematics-and-machine-learning/generated/interactive-learning-process/` | 169mm引用宽，8pt |
| 任务→数学问题→条件与工具 | `06-mathematics-and-machine-learning/tikz/learning-task-analysis-tools/` | 矢量169mm引用宽，7.934pt |

表中目录相对 `figures/01-mathematical-preliminaries/`。辅助说明7.5pt，科学上下标按层级缩小。共享 Source Han Sans Normal / WenKai Regular / Fira Math；仅 Fira 缺失的𝒞/ℋ/𝒦/ℰ/ℳ由真实STIX Two Math补充。

在项目根目录运行三个 `generated/*/typeset.py`，重新生成透明真实字体层与合成PNG；各脚本自动寻找根目录。三个TikZ源使用 `python3 figures/00-shared/academic-drawing/render_tikz.py <source.tex...>` 导出PDF、路径SVG与300dpiPNG。Python需Pillow/FreeType、fontTools，TikZ导出另需PyMuPDF以及书籍既有XeLaTeX。字体及许可位于项目 `fonts/`，不读取系统中文替代字体。共享依赖只读，缓存/编译产物留本worktree的build/figure-proofs。

模型背景不能靠脚本从提示词逐像素重现；每图保留真实参考、提示词各轮、模型工具实际返回的原始输出路径及hash、选中背景、排字坐标与分角色字号。原图均未清理填色或重绘；模型未暴露model identifier，记录明示未知。当前静态v3按native精确色板回模型修色，色板来源和可编辑代码均保存；这不是对模型PNG做代码调色。

`collect-mechanical-evidence.py` 仅读取原背景统计RGB、真实字体cmap、标注bbox和文件hash。RGB采样包含抗锯齿，不是要求所有像素只有五种颜色，也不证明无视觉纹理。背景是目标色近似，排字/TikZ代码用精确色值。实际图页和文字条件的接受理由见人工记录。最终整合PDF页码/图像hash由全卷集成后重新绑定。
