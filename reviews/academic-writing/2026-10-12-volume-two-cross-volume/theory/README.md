# 卷二理论三章跨卷核对与实际根稿局部闭环

2026-10-12，theory_second_half，AI 自查。工作区 `.worktrees/volume-two-figures-theory`，分支 `codex/volume-two-figures-theory`，原正文基线 d2999fa6e5c4daa8fe4d59faf6a2287c40cc6da4；数学参照为卷一远端 main fbb26aecb18253a599c41e167dd27b11612d1fc8。本人曾参与04章及03章DS局部改写，不能称三章全文独立审查。本目录只保存核对证据与建议，没有在自己或根工作区编辑实际三章正文、构建或另作提交；32处建议及追加1处由root实际应用。

受审范围为二分类、多分类、一般与凸学习三章的卷一接口，以及用户指定的随机复杂度版本/常数、组合量词/学习边界、换测度与凸性前提。原稿做完整章级通读，后续P/W限定接口和明确技术单元；根终稿复读限定32处实际修改及B94、DS完整图注和相邻上下文。这里不宣称新稿三章全文逐段逐句验收，也没有本阶段PDF或原始论文全证明核验。

## 记录索引

- [identity.json](identity.json)：25份卷一tex与3份卷二原稿快照、来源提交和SHA；复制全卷一用于可恢复接口，不代表25文件均逐句审读。
- [C.md](C.md)：原稿三章完整连续通读，分别到1194、733、2151行，保留原版本的实际理解。
- [P.md](P.md)、[W.md](W.md)：候选修订依据与明确技术单元的真实局部第二、三遍，含实际意思与接受理由。
- [old-new.json](old-new.json)、[suggested.patch](suggested.patch)、[proposal-sha.json](proposal-sha.json)：32项精确候选片段及最终候选r3。补丁在原d299稿上只读应用检查成功，实际应用由root完成。
- [root-applied-r1-sha.json](root-applied-r1-sha.json)：32处实际应用后，三章与最终候选字节相同。
- [root-applied-r2-sha.json](root-applied-r2-sha.json)：B94追加修订后的实际根稿；M/G与r1相同，B只改入口末句。
- [C-root-r1.md](C-root-r1.md)、[P-root-r2.md](P-root-r2.md)、[W-root-r2.md](W-root-r2.md)：实际根稿三遍分开局部复读；最后两遍关闭B94的追加问题。
- [candidate-numbered.json](candidate-numbered.json)、[root-numbered.json](root-numbered.json)：机械句号和原句，只用于稳定定位，未由脚本生成语义判断。
- [E-gates-formulas.md](E-gates-formulas.md)：三章逐项E1—E12、七门槛、相关入口/范围转换/关键公式及其当前用途。
- [findings.md](findings.md)、[root-applied-edits.json](root-applied-edits.json)：32原发现、4候选内部问题和1根追加问题的闭环，完整old/new及原/改后行号与SHA。
- [mechanical-check.json](mechanical-check.json)、[old-anchor-call-audit-root-r2.json](old-anchor-call-audit-root-r2.json)：实际根终稿机械回归；旧机械候选结果保留为 mechanical-candidate-r2.json，不误用旧章名/哈希。
- [snapshots](snapshots/)：卷一/卷二原稿、候选r1、根实际r1/r2与旧候选句级记录的可恢复副本；proposed目录是最终候选r3。
- [delivery-manifest.json](delivery-manifest.json)：目录中交付文件的SHA与大小，供复制后机械核对。

## 当前结论与限制

32处原发现加B94入口句均已实际根修订并复读通过，声明范围内无已知未解决技术或阅读问题。单侧Rademacher、高斯、有限标签增长、普通MI/CMI学习应用的原常数保持；Natarajan/图/DS量词、有限K边界、DS六环有限类可学习的边界明确；弱凸Hessian等价已补开凸域条件。结果是局部跨卷接口通过，不能以此代三章全文三级或PDF验收。

实际根终稿SHA：

| 文件 | SHA256 |
|---|---|
| 02-binary-classification.tex | 61dcd3439abf53643d06f1f9b2031b10b2cceb8d043f7ef16302f0e6193a90e8 |
| 03-multiclass-classification.tex | 92b5d2b24e14e808612ee845953c5ff7bb648105458b7321f0dad4eba2215e20 |
| 04-convex-learning-and-stability.tex | 7688a6454626580e676761b4a3c123aa5aeb00b2b177bd74c3c793c64b4830fe |

36个Book指针目标均唯一；原label、term显示串、引文多重集合保持，各章独立本章小结1节、环境配对。10个降为位置锚点的旧label不再具有原定义/定理计数器身份；扫描实际根全部tex，其活跃宏调用为0。编号环境减少是本次去除通用重复的预期动作，不谎称编号不变。

局部记录勘误：交付前复读发现候选W.md的T-G08抄写将“T=n、η=B/(L√n)”误粘为“T=n/η=…”，且漏写风险的√n分母；正文实际1775–1777正确。本目录仅修记录为三项之和3LB/√n，旧记录冻结在 snapshots/records-candidate-r3/W.md；另将B-UC记录的误称“G”改为本地F01。未因此改正文或产生新的技术发现。

后续根PDF25图/5全书代表/4灰度复核在另外的 build/final-root-page-review 保存，以当前根PDF重新确定页码和图源指纹，不沿用本次未执行的版面结论。
