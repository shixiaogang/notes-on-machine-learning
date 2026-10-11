# 卷二学习理论后三章重写与自查

2026-10-11；审查者 theory_second_half，AI 作者自查，非独立复核。任务工作区 `.worktrees/volume-two-rewrite-theory-b`，分支 `codex/volume-two-rewrite-theory-b`，基线17b2ded。对象为一般学习、深度学习、迁移学习三个完整章节；只改这三章和本审查目录，未提交、未构建。根代理负责集成和七版构建。

## 正文与快照身份

|章|最终文件|最终SHA256|段/特殊单元|中文句/元数据段片|
|---|---|---|---|---|
|04|04-convex-learning-and-stability.tex|1cde4106ae35e487b8c0432c8572d841638afe9d78951fd9f886d20e3875618e|224|818|
|05|05-deep-learning-theory.tex|3659af49d971a98994c3c6e198031742b1b1170fb2f85640064132bab7658118|214|691|
|06|06-transfer-learning-theory.tex|5e011ba19f4892de298be692ee8050cf067db1a6783b16862aa6ce32e48eb881|141|449|

`v0-units.json` 为基线段编号；`v1-units.json` 和 `v2-units.json` 为受审初稿与最终稿的完整段文、源行号和句号。P按空行划分，包括标题、命题、证明、图表文字和闭合单元；S对含中文的句末片段编号，少数标题/元数据没有语言句末仍入索引，仅作职责检查。总计579个P、最终1958个S片段，不能把这个索引计数当作1958个普通语言句。v0/v1/v2原稿保存在 `snapshots/`，全部摘要在 `snapshot-manifest.json`；修订后以v2为准。

## 三遍实际审查与修复

1. [第1遍：整章论证](pass1-chapters.md)，TB-C1，先核章节职责、问题到答案、入口、论述顺序与允许范围。
2. [第2遍：逐段](pass2-paragraphs.md)，TB-P1，覆盖579个P，核中心、前后关系、条件、证据和特殊单元。
3. [第3遍：逐句初稿](pass3-sentences-v1.md)，TB-W1；[最终句级记录](pass3-sentences-v2.md)，TB-W2。普通句实际意思与依据手写于 `sentence-meanings.tsv`，特殊单元为 `special-review.tsv`；修订后新增/改变意思手写于 `final-overrides.tsv` 与 `final-special-overrides.tsv`。排版脚本只复制这些判断、核编号和摘要，不生成语义结论。
4. [关键公式入口与E1—E12](key-units-and-calibration.md)，TB-K1，21组局部方法链、范围转换与每章12项实际判断；[问题闭环与连续复读](revision-reread.md)，TB-R2，9项台账（含1项有依据撤回），列修订与复核，不将旧版判断自动挪给新版。
5. [静态保全核验](verification.md)：391/579单元有改动；原383组展示公式数学表达、标签、引文、章节目序保持；关键行内数学内容已恢复。重写不仅涉及开篇、结尾或词语替换，普通论述覆盖各节。

目标读者为具概率、线性代数与基础优化知识的研究生；假定已读学习理论前两章，复核接口时恢复章内依赖。依据为academic-writing的grammar-and-style、chinese-examples、content、structure、review、review-records及项目写作/LaTeX规范与现行learning-theory-outline；未独立重审前置完整章节。

最终结论：当前三章的本次文本与章内推导自查已完成并关闭发现的问题；保留各章独立“本章小结”。未核外部原论文证明、图源程序及版权，未作图片视觉验收或PDF排版验收。该限制由根代理在集成验证报告中一并说明。
