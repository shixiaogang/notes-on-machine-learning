# 根跨卷17片段复核交付

日期2026-10-12，审查者 theory_first_half。范围为根 `root-changes.json` 实际17单位：ROOT-01–13、F01–F04，以及恢复其本地含义所必需的段落和公式。五章不是全文复核。框架01/02/F04为自查；其余原片段未参与改写，为限定范围独立代理复核；自己提出的五个候选及实际改后复读为自查闭环。

卷一依赖实际为 `fbb26aecb18253a599c41e167dd27b11612d1fc8`。按照结论先行、括号“可参考”精确指针在后核查；本轮没有新增或重复编号通用定义/定理，保留卷二实例、风险公式和计算。根只读，本工作区只写build报告，无源编辑、构建、另提交。

正文结论：17单位及声明上下文在本轮范围内通过；发现5项全部实际修改后复读关闭，已知未解决项0。完整五章未读部分、所有证明/原论文事实/图源/最终PDF均不在该结论内。

证据顺序：

1. `C-context.md`：章节C1–C4的限定定位与真正读取的卷一数学内容范围，全章证据不足项保留。
2. `P-logic.md`：17单位所在完整自然段作用、承接、入口、细节、范围及方法/公式链。
3. `W-sentences.md`：实际根r1新句、完整F所在段和关键显示式/相邻句的逐句白话含义与接受依据。
4. `findings-candidates.json`：R01核截面、R02 P/Q/Q下矩、R03允许初态、R04完备可分中文条件、R05独立先验语序的精确old/new。
5. `final-r3-closure.md`：实际根应用五候选后再次C/P/W读取，完整受影响单位逐句记录与关闭理由。
6. `gates-and-E-final.md`：按五章各自本轮对象核对全部七门槛及E1–E12，未以统一模板代判断。

版本证据：`source-manifest.json`与 `../snapshots/root-fragments/` 保存首次r1五章；`root-changes-actual.json` 保存当时17单位。`final-r3-manifest.json`与 `../snapshots/root-fragments-final-r3/` 保存当前实际最终五章及每单位哈希；`root-changes-final-r3.json` 保存根当前r3元数据。`r1-r3-integrity.json`证明仅五个候选发生变化；`final-source-readonly-check.json`交付前再核实际根等于快照。机械比对只负责版本，不替C/P/W语义。

| 最终根文件 | SHA256 |
|---|---|
| 02-learning-theory/01-statistical-learning-framework.tex | d191e61b73b768af8130c809f69f1f7a4a8da9862d85478857e73d470a46f9ee |
| 02-learning-theory/05-deep-learning-theory.tex | e6caa114454d49a468b97621e029bd8c0b01d361d07746a9bf5194e1c069a24e |
| 02-learning-theory/06-transfer-learning-theory.tex | f57c9b76d11020492d31c6c64431e465952c4f581d2d3918eb9f2ea883a1ba49 |
| 03-trustworthiness/07-privacy.tex | 73709f4534f59c9f7bf61cd92e589d879fa2f07e3c6d1f52a51f143e4d8b4305 |
| 03-trustworthiness/08-adversarial-security.tex | db3f1f9e91605e2f415533e1c5494e647a86f2b520803344e8455588da183ba5 |

基础原12处根实际闭环另见上级 `root-applied-basics-closure.md` 与 `root-applied-basics-manifest.json`。其前一轮整章C与局部P/W仍各保留实际范围，不扩称独立全文。
