# 第4章最终复核补充

记录：`CH04-FR2-20261014-v2`。角色：未参与正文、词典修改及既有审查记录写作的最终复核补充者。

## 复核范围与版本

- worktree：`/Users/bytedance/Projects/notes_on_machine_learning/.worktrees/rl-review-20261011-ch04-r1`
- branch：`codex/rl-review-20261011-ch04-r1`
- 基线/HEAD：`75175dea03ad6c4d9b20299835b48c087a052505`
- 当前 manifest SHA-256：`b854336c0668359a4279ba2cb68fd8ed7263fdb5266587dca6053c80bf37d300`
- 最终正文：`tex/04-paradigms/01-reinforcement-learning/04-information.tex`
- 正文 SHA-256：`48662ad427b731f34719cc9ce7706881eb869593b79409466c6601e4b8cfac7a`
- 正文快照：`ch04/integrated-final-v1.tex`，与最终正文逐字节相同
- 最终词典：`tex/index-terms/04-paradigms.tex`
- 词典 SHA-256：`9aece507873dbac7cb8cfda413b80db0a312ffed124da346917daaf4f5f15621`

本轮完整读取了 `final-review-v1.md`、其五份 `final-coverage-v1-*` 覆盖记录、
九项术语的最终正文首现句、最终词典、`shared-repair-requests.md`、
`source-checks.md` 和 `final-review-instructions.md`。复核只针对
`CH04-FR1-01` 所涉共享映射及其对第4章最终结论的影响。

## 继承 v1 正文覆盖

v1 的 C、P、W、特殊单元和专项记录均绑定正文 SHA-256
`48662ad427b731f34719cc9ce7706881eb869593b79409466c6601e4b8cfac7a`。
当前正文及 `integrated-final-v1.tex` 的字节和哈希均未变化，因此继承以下结论：

- `final-coverage-v1-c.md` 的 C1--C4 章级覆盖；
- `final-coverage-v1-p.md` 的 P1--P5 段级覆盖；
- `final-coverage-v1-w.md` 的 W1--W6 句级覆盖；
- `final-coverage-v1-special.md` 的定义、定理、证明、公式、例子、表格、图源和算法覆盖；
- `final-coverage-v1-gates.md` 的七项门槛、E1--E12、局部入口、方法链、范围转换和公式双门槛结论。

本补充报告不把哈希继承冒充一次新的全文三遍审读；它确认 v1 的正文三级覆盖仍适用于
未变正文，并对唯一开放的共享映射问题作独立复核。

## 共享映射变化范围

v1 报告绑定 manifest SHA-256
`538995d26e714c05a2623ce1bee35f689770a98a184b06bd110047dd788e4023`。
从当前词典只读虚拟移除本轮九条声明，可恢复改前词典：

- 改前词典：SHA-256 `d9095a5a6b23417fa9986c467e7fae9cec2568ad7578961efa875898c29bf0ca`，11821字节；
- 改后词典：SHA-256 `9aece507873dbac7cb8cfda413b80db0a312ffed124da346917daaf4f5f15621`，12364字节。

将恢复出的改前词典哈希和字节数写回当前 manifest 的对应内存数据后，所得 SHA-256
精确等于 v1 的 `538995...4023`；当前 manifest 则为 `b854...d300`。因此，相对 v1，
共享变化只包含以下九条普通词典声明及 manifest 中该词典条目的哈希和字节数，正文未变。

| 正文首现 | 显示键 | 英文映射 | 词典位置 | 结果 |
|---|---|---|---|---|
| L278 | `GTrXL` | `Gated Transformer-XL` | L82 | 匹配 |
| L610 | `DualDICE` | `Dual stationary DIstribution Correction Estimation` | L89 | 匹配 |
| L747 | `ReBRAC` | `Revisited BRAC` | L93 | 匹配 |
| L765 | `Decision Transformer` | `Decision Transformer` | L94 | 匹配 |
| L878 | `Diffusion-QL` | `Diffusion Q-learning` | L98 | 匹配 |
| L920 | `MOReL` | `Model-Based Offline Reinforcement Learning` | L102 | 匹配 |
| L940 | `Trajectory Transformer` | `Trajectory Transformer` | L104 | 匹配 |
| L941 | `Diffuser` | `Diffuser` | L105 | 匹配 |
| L1013 | `Cal-QL` | `Calibrated Q-Learning` | L108 | 匹配 |

九项显示键与正文 `\term{...}` 参数逐字一致，英文映射与正文首现、
共享修复请求及已保存的一手命名核验一致；正文顺序和词典顺序一致。

## CH04-FR1-01 关闭复核

- 改前：九项正文调用没有集中双语映射，v1 将 `CH04-FR1-01` 记为开放。
- 改后：九项均有且仅有一条 `\DeclareBookIndexTerm`，没有同名 alias、重复声明或冲突映射。
- manifest：当前记录的正文与词典哈希均和实际文件一致。
- 状态：**CH04-FR1-01 复核通过，关闭**。

## 只读源级审计

未构建，未写入正文、词典或构建产物。只读审计结果：

- 全部词典的普通显示键无重复或冲突，alias 身份无重复或冲突；
- 第4章全部41个唯一 `\term` 调用均有集中声明；
- 第4章归入 `04-paradigms` 词典的词条顺序与本章首次出现顺序一致；
- 九项的显示键、英文映射、唯一声明、唯一首现调用及相对顺序全部匹配；
- 最终正文、正文快照、词典及 manifest 中对应哈希相互一致。

未发现需要编号的 `CH04-FR2-NN` 新问题。

## 限制

- 本轮继承 v1 对未变正文的三级覆盖，没有重新执行另一轮全文 C/P/W 审读。
- 未重新联网打开九项原论文；英文映射以正文首现、共享请求和 `source-checks.md`
  已记录的一手命名核验交叉检查。
- 未重证外部完整理论，未运行训练、实验、绘图或算法程序。
- 按要求未构建、未运行项目测试、未检查最终 PDF 或索引成品；源级映射通过不等于
  字体、换行、索引渲染、超链接、裁切和溢出版面通过。
- 未重新核验 manifest 中与第4章正文和最终词典无关的其他章节及资源。
- 未修改正文或词典，未暂存、提交、推送或集成。

## 最终结论

- 记录结论：可接受。
- v1 正文三级覆盖：对未变正文继续有效。
- `CH04-FR1-01`：复核通过并关闭。
- 开放原问题：0。
- FR2 新问题：0。
- 正文结论：**在声明范围内通过**。
