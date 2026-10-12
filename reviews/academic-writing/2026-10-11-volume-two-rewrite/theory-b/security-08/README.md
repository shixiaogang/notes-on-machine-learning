# 对抗安全章重写与三遍自查

记录身份：SEC-C1/P1/W1/W2/K1/R2，2026-10-11，theory_second_half，AI作者自查。完整正文tex/03-foundations/03-trustworthiness/08-adversarial-security.tex；工作区为volume-two-rewrite-theory-b，分支codex/volume-two-rewrite-theory-b，基线17b2ded。该章由根代理追加分配，编辑范围只在本章及本审查目录；没有构建或提交。

受审版本及恢复：snapshots/v0原稿，v1整章重写初稿，v2最终修复；全部SHA256在snapshot-manifest.json。最终SHA256为`0b3a44c2555bc03e368aa5df0fa814a40c1b41f33ebfe73cabfd4662bc94d215`。三个版本稳定180个P；v1/v2为531个中文句/标题片段，其中34标题只作结构元数据核查。所有图注、程序、例子及公式段均覆盖，未把排版命令伪装成语义判断。

目标读者掌握基础分类、经验平均、梯度和基础统计，依赖可信性基础三层框架、鲁棒认证、隐私与执行干预的章内复述接口；未独立重审这些完整前置章节。实际组成范围是本章一份正文，无递归嵌入文本。现行章边界依据plans/README.md和book-structure.md，节次以正文为准，保留所有标题与独立本章小结。academic-writing、规定表达/示例/内容/结构/审查/记录资料以及项目写作和LaTeX规范作为审查依据。

三遍按顺序分开实际执行：

1. [章级SEC-C1](pass1-chapter.md)：完整连续通读后核实际问题、节职责、承诺及答案。
2. [段级SEC-P1](pass2-paragraphs.md)与[180段详细记录](pass2-paragraphs.tsv)：中心、承接、首次依赖、转换和细节作用。
3. [初稿句级SEC-W1](pass3-sentences-v1.md)及[最终SEC-W2](pass3-sentences-v2.md)：每句短引、白话意思和具体接受/发现依据。语义判断手写于sentence-meanings.tsv；标题职责手写于metadata-review.tsv；最终影响项手写于final-overrides.tsv。assemble_records.py只复制这些已有判断、检查编号和哈希，不推断语义。
4. [关键单元SEC-K1](key-units-and-calibration.md)：13组方法入口、依赖、范围/核心公式双门槛以及E1—E12逐项校准。
5. [修复闭环SEC-R2](revision-reread.md)：3项真实问题，22个受影响单元的重新检查与最终连续复读。[静态保全](verification.md)：146/180单元改写，8组展示公式逐字保留，34标题/36标签/20引文逐序一致，原行内数学表达保留。

记录结论可接受；正文在声明范围通过。无已知未解决文本或章内运算问题。未核外部论文证明/引用真实性、图源程序及版权、图片像素、PDF版面；根代理统一集成构建七版，不以源码自查代替这些验证。
