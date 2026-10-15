# PROGRESSIVE architecture

本图生产底图全部由 `image_gen.imagegen` 绘制，包含所有节点、模块边界及箭头；根据用户“生成模型的架构图都用大模型生成”的要求选择此路径。原生 TikZ 图只作为科学拓扑参考，不转换为生产底图。

`prompt.txt` 与 `prompt-revision-1.txt` 保留实际提示词；`background-v1.png` 为首版，`background.png` 为修订底图，`tool-output.json` 保留原工具结果路径。`render.py` 仅用仓库真实字体生成透明 `text-layer.png` 并复合成 `figure.png`。`figure.pdf` 是同一 PNG 的物理尺寸封装，不能视为矢量图。

最终插入宽度 112 mm；实际高度 112.000000 mm。主标注请求8 pt，采用4倍文字层采样向下取整，实际范围 [7.974983988245488, 7.974983988245488] pt；小注请求7.5 pt，下标请求6 pt。字体、版本、许可证与源文件哈希见 `generation.json`。

重现：在本任务 worktree 运行 `python3 figures/05-neural-network-models/00-shared/generated/neural-generative-architectures/progressive/render.py`。底图是保留的工具原始图；重放只验证真实字体排字及复合，不宣称能用不可见的生成种子重放 imagegen。

`data.json` 描述科学节点、边与第一手来源。`review.json` 为作者自查；独立评审记录与成书页面检查另由整合代理保存。
