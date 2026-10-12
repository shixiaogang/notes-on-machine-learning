# 卷二已完成部分审查记录一致性抽核

记录 AW-V2-RECORD-AUDIT-A1；2026-10-11。审查者 `/root/theory_first_half`，角色为记录一致性抽核者。本代理曾参与理论 01–03、隐私 07 的改写，并实施本报告下述九文件局部导航/词条修复，因此这些文件只作记录检查与局部改后自查，不能称全文独立审查；其余文件此次也只抽核记录，未实施新的独立全文正文审查。

受审记录来自 `/Users/robbieshi/Library/Mobile Documents/com~apple~CloudDocs/writings/Notes/Machine Learning/.worktrees/volume-two-adjustments/reviews/academic-writing/2026-10-11-volume-two-rewrite`；对 root 正文和报告只读。九文件修复先在本代理自己的 `volume-two-rewrite-theory-a` worktree 完成，由 root 校 SHA 后串行集成，本代理没有写 root。冻结正文的机械版本表见下；以下各记录路径相对受审记录根目录。

本次范围是 basics 三章、basics/theory 两份导读、theory-a 的理论 01–03 与隐私 07、theory-b 的理论 04–06 与安全 08、trust 01–03、trust-04-independent 公平章，共 15 章与 2 份导读。可信 05/06、可信导读和全卷总索引不在原抽核范围；其审查/索引当时尚在整理，未当作缺项。本次不核外部论文、证明正确性、程序、现实规范、图源或 PDF。读者与前置知识按各主报告的声明核对。

抽核动作：实际读取各组 C/P/W 主记录、版本与闭环报告；机械核对 P/S 编号及可恢复快照；在不同位置人工读取句义、段落职责、公式特殊单元及修后记录，判断是否有具体意义和依据。编号/摘要/计数由脚本完成，下面的记录判断由人工阅读形成。能证明的是记录内容、位置和版本是否相互支持，不能从记录反推或独立证实历史阅读行为。

## 当前正文与可恢复版本

核对发生在 root 已集成导航和词条恢复、正文冻结后。下表每个 SHA 与右侧文件逐字节相同，不仅是文件名对应。后续正文若改变，本表和相关接受项需重新核对。

| 正文（相对 tex/03-foundations） | SHA256 | 对应最终快照（相对记录根） |
|---|---|---|
| `01-basics/01-introduction.tex` | `5cdd1533edc3d5e40f137b42099622f65b9969248d64947a28dc22ec9791d387` | `basics/r2/01-introduction.tex` |
| `01-basics/02-machine-learning-models.tex` | `8f44de71bed9d61a2ade3f9c04efb8c54a2778ccc1d2a45ced07cf890ffb9346` | `basics/r4/02-machine-learning-models.tex` |
| `01-basics/03-machine-learning-paradigms.tex` | `50573999c4377ec39b30ccf18dc25790163de8ecf7f41c2c3525def75a8a76c4` | `basics/r5/03-machine-learning-paradigms.tex` |
| `01-basics/reading-guide.tex` | `54fff268f1afbf88d6544d787b80278a0e3cce37a84691035e947bb069b3ff2e` | `guides/basics-final.tex` |
| `02-learning-theory/reading-guide.tex` | `7ede43a2e5a5231b055a4579b80655f21659b535d95ee3d264c11da030baa5f7` | `guides/theory-final.tex` |
| `02-learning-theory/01-statistical-learning-framework.tex` | `2a1457f20194678c710d38fc93e07cc5be0a01157fcc693459f1a54a0732b1f7` | `theory-a/navigation-terms/theory-01-statistical-learning-framework.tex.after.tex` |
| `02-learning-theory/02-binary-classification.tex` | `9d8003c64b9152fb5752cfdda6ec864230be41026cb86f53a759b326aa50af88` | `theory-a/navigation-terms/theory-02-binary-classification.tex.after.tex` |
| `02-learning-theory/03-multiclass-classification.tex` | `041f337067a38c9367e4a7561648b07033d11222758278df2f9bd3581a8ecb97` | `integration/multiclass-after.tex` |
| `02-learning-theory/04-convex-learning-and-stability.tex` | `da48f293d62dd20d5312cb5303f8ac354b364daa918c83cf51d56009adff0f44` | `theory-a/navigation-terms/theory-04-convex-learning-and-stability.tex.after.tex` |
| `02-learning-theory/05-deep-learning-theory.tex` | `3104d764f06b3eb1788539437be9aa65071d01312ab9751fcea0e762790eefc8` | `theory-a/navigation-terms/theory-05-deep-learning-theory.tex.after.tex` |
| `02-learning-theory/06-transfer-learning-theory.tex` | `31e5fba72ee612b2a6eea676e03e0615f23ed545f9af86532233281ed7156c2a` | `theory-a/navigation-terms/theory-06-transfer-learning-theory.tex.after.tex` |
| `03-trustworthiness/01-foundations.tex` | `b7bf083a10b29404fe14a7945aa82e67b0264bfbe6f4c5b008b3cbbe338aaa80` | `theory-a/navigation-terms/trust-01-foundations.tex.after.tex` |
| `03-trustworthiness/02-reliability.tex` | `edc6039971eacbfec2b49754b33c44d496f4a4da9e0d70c0446e1c6250031805` | `theory-a/navigation-terms/trust-02-reliability.tex.after.tex` |
| `03-trustworthiness/03-robustness.tex` | `b3bd84002c252fa2974324e91f60d5fa83fca75f63d7afc3c995d68c4f40469f` | `theory-a/navigation-terms/trust-03-robustness.tex.after.tex` |
| `03-trustworthiness/04-fairness.tex` | `9b531220919ae32084ac32ed6c136b95357fd5b14a7a5cfe99de896b5c9daea4` | `theory-a/navigation-terms/trust-04-fairness.tex.after.tex` |
| `03-trustworthiness/07-privacy.tex` | `2c87d62592909f9a93b37a8d5fe957439c8349df84dc289f972696b6cdf0506b` | `theory-a/07-privacy-v2.tex` |
| `03-trustworthiness/08-adversarial-security.tex` | `0b3a44c2555bc03e368aa5df0fa814a40c1b41f33ebfe73cabfd4662bc94d215` | `theory-b/security-08/snapshots/v2/08-adversarial-security.tex` |

## C/P/W 覆盖核对

下列数目按各作者已经冻结的编号系统核对，不能将含标题/命题/图注的数量和仅正文数量直接比较。S 数是初次 W 所绑定版本的句/特殊单元数；后续改变必须结合修后记录，不拿旧句号冒充终稿句号。

| 对象 | P/W 段单元 | 初次 W 句/特殊单元 | 本次核对 |
|---|---:|---:|---|
| basics 引论 | 117 | 468 | P 的 unit 与 W 三分卷的 paragraph 集合相同，句号无重复 |
| basics 模型 | 145 | 532 | P/W 全部段号相同，r3 变化另有 W-r3，r4 导航另有闭环 |
| basics 范式 | 189 | 554 | P/W 全部段号相同，r4 变化另有 W-r4，r5 导航另有闭环 |
| basics 导读 | 3 | 9 | 每段都有实际职责及逐句意思 |
| theory 导读 | 4 | 15 | 每段都有实际职责及逐句意思 |
| theory-a 理论 01 | 195 带句块 | 644 | v1 编号清单的每个 S 均在句审中；v2 与词条修后分版本复读 |
| theory-a 理论 02 | 159 带句块 | 551 | v1 每个 S 均有句审；v3/v4 与词条修后另有实际变化句义 |
| theory-a 理论 03 | 118 带句块 | 354（含非正文注释） | v1 每个编号均有记录；v2/v3、集成“计分”另有闭环 |
| theory-b 理论 04–06 | 224+214+141=579 | 818+691+449=1958 | v2 单元表每个 S 均出现在 W2；P 表 579 行，未发现缺号或多号 |
| trust 01 | 135 带句块 | 448 | coverage 清单全部 P/S 在原 P/W 表中，修后四轮变化另记录 |
| trust 02 | 108 带句块 | 343 | coverage 清单全部 P/S 在原 P/W 表中，修后变化另记录 |
| trust 03 | 88 带句块 | 262 | coverage 清单全部 P/S 在原 P/W 表中；P030 注释三句补审有说明 |
| 公平 04 | 125 带文字块 | 343 | 两份 P 与三份 W 段号一致、句号无重复；32 改动块有 fixed-v3 W，主报告说明 108 新单元 |
| 隐私 07 | 153 带句块 | 530 | v1 每个 S 均有句审；v2 的变化块/新句另有复读记录 |
| 安全 08 | 180（含结构） | 531 | P TSV 180 行；v2 单元表的每个 S 均在 W2，未发现缺号或多号 |

各组都有实际 C 记录：basics 的 C 文件给经验任务与章职责；guides 的 chapter-gates-review 说明完整片段职责；theory-a 主报告分开 C/P/W 并指出章首承诺的实际落点；theory-b 的 pass1-chapters 与安全 pass1-chapter 重建一般学习、深度、迁移、对抗链的核心问题和条件；trust 三章 C 报告重建要求/证据/持续使用、估计/校验/程序、邻域/环境/运行关系；公平 C.json 的对象为未参与改写的冻结输入，后续作者修订自查在 README 中另行说明。没有把列出目录本身当作核心问题的唯一证据。

## 句义与特殊单元人工抽样

- basics 引论 B003、B029、B054：分别逐句记录经验与训练差别、阈值比较数值和评价对象，句义有各自内容；模型 B060、B088、B120 分别解释参数/概率/尺度、仿射与激活、零一/替代损失；范式 B142、B175、B211 分别说明比较指标与基准、表格内四种角色、阅读路线。P 表也写具体承接与转向。若同段数句共享判断依据，其实际意思仍逐句区分，不是同一句接受模板重复粘贴。表格 B175 按共同分类动作合并，并解释四行内容及非互斥范围。
- 两导读的全部七段：对完整片段给 C/P/W，句义分别说明当前问题、各章职责、前置和阅读顺序；没有用统一“概括本章”替代每句。
- theory-a：只检查本代理已有记录的版本/编号/内容对应，不提供新的独立语义背书。01 的 P008–019 逐句解释观测单位、比较/输出空间和随机来源；02 的 v4 导航附录列实际变化句义与连续范围；03 F03-10 列恢复位置并绑定 v2/v3，集成修词另有前后快照；07 的 P019–026 逐句区分访问许可、精确计数泄露、相邻概率保证与检验量，非统一句义。四章的初次 W 和后续 delta 并存，未把修后文本冒充原审版本。
- theory-b 04-P024：每句分别说明衰减函数、阈值模式、2γ 间隔和有限尺度；04-P044 分开参数距离、损失变化、普通与条件互信息；05-P056/057 说明容量条件与数据选解；06-P126 分开块内相关、跨块 IID 与新块损失期望。06-P082 的定理/证明虽合并记录，但显式列 S01–S08，并说明共同核/覆盖、κβ、优化残差、风险分解及 Markov 转换这一共同推导动作。符合连续句共同完成同一动作时可合并的规则。
- trust 01 P002–016、P056、P095：逐句区分统计推广、行动授权、三层职责、联合/条件覆盖及限期教学授权。trust 02 P060、P082、P127：记录分母、选择风险、概率量词和三类检验；原审发现仍标 F02-04 待修，关闭在新版本附录，未提前消除原发现。trust 03 P039/P071 与 P035–046 的 P 表：区分单样本全称反例、总体容限、认证上界、训练与证书；原 W 指出不足，修后另列条件与新句义。
- 公平 F060、F081、F108、F109、F131、F155：分别记录审计状态/距离/全称界、合成结论边界、训练修改对象、候选和经验目标、独立阈值混合、因果与动态来源。F108 原 W 留下压缩表达发现，fixed-v3 给新句义；固定稿的 F009、F108、F152 也读了实际改后意思。图注按完整读图动作合并，主报告已说明覆盖范围。句义和判断依据含当地指标/量词，非统一模板。
- 安全 P087、P179/180：分别解释内部梯度/访问与查询黑盒、评估及梯度遮蔽来源、外部内容/接口/交互证据；P TSV 的开篇各行实际说明主动操作、损害与接口职责。W 可辨对象和限制。

本抽样未发现“只给段落摘要、没有列句号和实际句意”的覆盖冒充；也没有把统一状态字串当作全部语义依据。部分同行共用校准依据、形式命题合并和图注整体记录均有具体共同动作与覆盖句号/范围，不能仅因采用紧凑格式判为模板化。

## E1–E12、七门槛与关键单元

basics 三份 final-review 均有逐项 E 表、七门槛和模型/训练/评价/规则等具体方法或公式记录；导读 chapter-gates-review 对 E 项逐项给触发/不适用原因，完整片段没有数学方法，未要求虚构公式。theory-a 四主报告有 E1–E12、入口/方法链/范围/关键公式的具体位置；01–03 的七门槛有分项或跨关键单元记录，07 有显式七门槛节。theory-b key-units-and-calibration 对三章分别给 E1–E12 及方法与核心公式，W2 说明 G1–G7 的实际含义；安全另有自己的 key-units-and-calibration。trust 01–03 的 key-units 各给 E1–E12、全部主要方法入口和显示公式，并有七门槛结论。公平 README 现在已成稿，七门槛、20 个主要方法/公式链及 E1–E12 表均存在，和 C/P/W/发现索引有明确分工。

人工抽看的是当地关系：一般学习损失空间与风险估计、迁移风险恒等式与标签/覆盖条件、可靠性分母和概率对象、鲁棒半径与证书对象、公平全族/个体对/因果/潜在结果、隐私单位与邻接、安全允许操作与损害。它们给出了问题→对象/符号→运算/范围→回答，不只有“公式已查”的统一确认。没有新的缺项需由正文修补。

## 版本与问题闭环

basics 的 r1→r2 与各章后续修订保存快照；模型 r3→r4 和范式 r4→r5 的导航恢复有完整改前/改后段及意义、条件、承接不变的复读记录。引论 I-P01 有据撤销保留反证，其他实际修订绑定新版本，不为撤销制造假改动。

theory-a 01–03 初次 W 绑定 v1，技术/句义修复绑定后续快照与连续复读。理论 02 F02-12 恢复 10 块 11 导航，记录 P001–018/P029–037/P054–060/P119–123；理论 03 F03-10 恢复 13 块 15 导航并连续全文复读。当前正文与 v0 按 ref/eqref/BookChapterRef/BookSectionRef 多重集比对相同：01 为 39，02 为 49，03 为 27；不以次数相同替代引用对象相同。多分类集成时“计费”→“计分”有 integration/findings 的单独前后快照及连续范围，当前正文 SHA 正是 after。隐私 v1→v2 的八发现及额外改句有对应新句义和全段复读。

theory-b revision-reread 和安全 revision-reread 保存不同版本与发现状态；有限宽度、低秩边界、迁移条件以及像素缩放等实际修改有前后短引和最终连续复读，未只记“已改”。trust 01 的 R2/R3/R4、02 的 R2、03 的 R2/R3 在 findings-and-closure 保留改前/改后、新句义和局部连续范围；各最终 SHA 与快照一致。公平 27 发现与 32 改动块有完整前后段、fixed-v3 版本、continuous_scope 和 W-fixed-v3 实际新句义；主报告还说明全稿两段顺读与二次复读中的新增修改。

集成者的全卷机械对照另发现理论 04–06、可信 01–04 共 20 处原导航被改写省掉，由 parent 授权扩成本代理的小项修复；理论 01 的登记字串与理论 02 的限制类词条也恢复。全部在自己 worktree 写回、留前后快照并复读 22 个段及紧前/紧后块；关键引用目标另读，详见 theory-a/navigation-terms/review.md、changes.json、manifest.json、mechanical-checks.json。root 已按 SHA 集成，上述 9 个当前正文与 .after.tex 一致。此部分只能称局部改后自查，不因此前未改写过其中七章而宣称全文独立复核。root 告知索引检查恢复为 calls 2284、unique 1981、errors 0；这是集成者验证，本代理未重跑全卷工程测试。

## 本次发现与关闭

AUD-01（记录统计）：03-review.md 原句把“7 组引文与 34 处导航”并列，实际 34 是 27 处交叉导航加 7 组引文。正文引用多重集无缺失。已报告 parent；root 改后实际读到“27 处交叉导航与 7 组引文保留”，与 v0/current 机械统计相符，关闭。修订发生在记录，未改变正文；原值和问题在本审计记录保存。

AUD-02（导航/登记词条）：遗漏导航及两处索引接口均按 NAV-01–22 实际修订并关闭；详见上节。无未关闭的记录缺项。公平主报告现已存在；总索引仍待 root 生成，不把尚未生成的汇总索引当成各章 C/P/W 不存在。可信 05/06 与可信导读不在本次结论中。

记录结论：在所列冻结版本和抽核范围内，可接受。正文结论：本次没有做新的全文独立验收；原作者自查结论及声明限制保持，22 处恢复在局部复读范围通过。记录完整不等于来源、技术证明、现实规范和版面已独立核实。最终构建和 PDF QA 由 root 的后续验收记录负责。
