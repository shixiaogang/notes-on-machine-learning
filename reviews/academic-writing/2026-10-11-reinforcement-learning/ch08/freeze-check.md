# 第8章最终冻结核对

- 2026-10-12；核对者为接管改写者，AI自查，非独立复核。
- 工作区 `.worktrees/rl-writing-20261011-ch08`；分支 `codex/rl-writing-20261011-ch08`；Git基线 `75175dea03ad6c4d9b20299835b48c087a052505`。
- 正文 `tex/04-paradigms/01-reinforcement-learning/08-trustworthy.tex` 与 `rewrite-v1.tex`字节一致，SHA-256均为 `296feb91f4aec6f55538f5d4d9251f171554e69f2ab70569583188853d065d11`。摘要文件 `rewrite-v1.sha256`；机械逐项清单 `freeze-inventory.json`。
- `base.tex` 与Git基线该章字节一致，SHA-256 `592078a5e0cfe1f8f1ed73cbd5dd40c55f360ec228c49c1e37c1f274447965ab`。
- `rewrite-pre-takeover.tex`保留旧稿，SHA-256 `6edf30730f313668f7e23e5f804b7969f7651b186ada63cb1129d4b2367cd348`。原三份自查未改，摘要见下；旧文件内的 `rewrite-v1.tex`须依旧摘要映射到此旧快照，不得误读为当前版本。
- 最后一轮仅在P037.S2明示单调性，实际连续回读P029至P043；定义/递推/压缩条件一致。全部记录和覆盖清单已重新绑定最终摘要，不以此前中间哈希作为最终对象。

## 冻结结构

| 对象 | 基线/最终 | 核对结果 |
| --- | --- | --- |
| chapter/section/subsection/subsubsection/paragraph | 19/19 | 命令、标题和顺序逐项相同；后两种本章不存在，未新增 |
| label | 74/74 | 标识及出现顺序完全相同，逐项行号与原命令列于清单 |
| 文献引用调用 | 15/15 | scite等调用及目标顺序相同，没有新增/改名一手来源 |
| 图源input | 12/12 | 路径及顺序相同，全部读取且未写；各图源SHA-256保存在清单 |
| 定义/定理/证明/例子/算法/图表环境 | 88/88个begin/end | 44对环境及名称顺序相同；5定义、7定理、6proof、2example、3算法、12图、9表 |
| 展示公式 | 42/42 | 逐项去空白后的内容与顺序完全一致，含数学、label、nonumber和句点；F01至F42人工语义见特殊记录 |
| 原交叉引用调用 | 55/67 | 全部55次原调用作为最终序列的子序列保留；新增12次解释用调用，无原目标改写 |
| 行内公式 | 558/652 | 数量因补类型/条件/比较变化，不宣称字符串全相同；9个短写合入更明确表达，下面逐项说明 |

### 标题对照

每行与基线同名同序。最终行号如下，完整基线行号见 `freeze-inventory.json`：

| 最终行 | 命令与标题 |
| --- | --- |
| 2 | chapter 可信强化学习 |
| 19 | section 行为要求与保证对象 |
| 66 | section 风险敏感决策 |
| 72 | subsection 累计结果分布上的风险决策 |
| 189 | subsection 逐阶段条件风险下的决策 |
| 273 | section 不确定环境下的鲁棒决策 |
| 286 | subsection 环境机制变化下的鲁棒决策 |
| 390 | subsection 观测信息受扰下的鲁棒决策 |
| 425 | subsection 动作执行受扰下的鲁棒决策 |
| 459 | section 安全约束下的策略学习与保护 |
| 480 | subsection 期望累计成本约束下的安全学习 |
| 636 | subsection 轨迹事件概率约束下的安全学习 |
| 754 | subsection 逐步与逐轨迹硬要求下的安全学习 |
| 859 | section 可靠性评价与保证 |
| 872 | subsection 确定验证协议并取得证据 |
| 905 | subsection 由证据估计指标与保证范围 |
| 1006 | subsection 依据要求作出判断并持续复核 |
| 1025 | section 多种要求的组合与取舍 |
| 1092 | section 本章小结 |

### 交叉引用

新增调用为：`chap:rl-learning`1次、`eq:rl-trustworthy-tail-gradient`1次、`alg:rl-trustworthy-static-cvar`1次、`eq:rl-trustworthy-risk-bellman`1次、`eq:rl-trustworthy-robust-bellman`2次、`eq:rl-trustworthy-cmdp`1次、`eq:rl-trustworthy-cost-gradient`1次、`alg:rl-trustworthy-primal-dual`1次、`eq:rl-trustworthy-cpo-bound`1次、`alg:rl-trustworthy-filter`1次、`eq:rl-trustworthy-offline-joint`1次。

其中本章新用的六个目标都是基线已有label；其余是增加已有目标调用次数。没有新增不存在的标签目标，原55次调用未删除或换目标。完整调用、顺序、行号清单可机器重核，引用调用字符串数量不被误称冻结未变。

### 行内公式

对基线行内数学按去空白多集比较，549个原短写可精确匹配，以下9项差异逐项人工对照。单独符号与不等式并入带域表达不是删计算内容；42个真正展示公式已逐式完全保持。

| 原短写、基线语境 | 最终表达和核对 |
| --- | --- |
| `\ell_t`，嵌套损失定义 | P033写 `\ell_t\in L^\infty(\mathcal F_{t+1})`，递归中的ell_t仍原样；新增可测有界域 |
| `u<v`，时间一致性时刻 | P033写 `0\leq u<v\leq H`，保原比较并补范围 |
| `\rho_{s,a}`，实值映射条件 | P038写 `\rho_{s,a}:\mathbb R^{|\mathcal S|}\to\mathbb R`；其他rho短写仍存在，补全算子域不改现金平移公式 |
| `\widehat\nu`，近似攻击 | P066写 `\widehat\nu\in\mathcal N`，原不等式的J(pi,widehat nu)保留；限定必须允许规则 |
| `s`，执行误差解释 | P069直接以 `E(s,a)`、`f(s,a+e,w)`说明设备界和后继，s仍在原展示式，删除独立短写没有删状态依赖 |
| `d`，占用预算解释 | P076以 `d(s,a)`、`d(s)`及原流公式说明归一化和恢复策略；原占用计算未少，只不再单独说“从d抽样” |
| `a`，执行误差解释 | 与s同一原句，P069以 `E(s,a)`及实际 `a+e`当场说明；请求a仍在原式内 |
| `b(s')`，分配预算域 | P101第一次写 `b(s')\in[0,1]`；后继携带b(s')和原概率预算式均保留 |
| `\varepsilon`，零失败阈值手算 | P138改为完整比较 `1-\delta^{1/n}\leq\varepsilon`后求n；原展示样本量式不变，阈值未删 |

新增行内式用于概率空间、映射域、正概率历史、非负/区间条件、起始标记、统计误差、干湿绝对值及下降幅度。没有为保持字符串而删必要条件，也没有以公式保留掩盖这些文字限定的实质纠正。

## 覆盖与记录

- `coverage.json`正文哈希与最终一致，171个P号。各raw逐项在最终源可恢复，最终句界包括展示末句点、嵌套aligned/nonumber后句点、scite输出句号及闭引号。
- 三份接管句级记录加特殊单元记录，机械核对覆盖666个S、50个C、47个T、24个A，共787单元，漏号0、多号0。该核对只证明编号覆盖，语义接受来自人工记录。
- 171个段级行均在接管P记录，不复用原代理旧段级接受结论。所有记录为接管者自查，独立审查数为0，后续三审由主代理组织。
- 原 `self-check-chapter.md` SHA-256：`a49aab787823873febd4048a799d7594a9ae9552d53bc6426e6be1169e05fac8`。
- 原 `self-check-paragraph.md` SHA-256：`acb5f9f1fa31d1cbfcd61d0f5095b657675409522aa8513d6226f50d51dd83f9`。
- 原 `self-check-sentence-1.md` SHA-256：`7866520245a97445178c42c1f7e437499fa1c8787c34a73f348a295eec23c808`。

## 限制与交付

`git diff --check`通过，正文/快照/覆盖摘要相符，修改和未跟踪文件仅在授权正文与ch08记录目录。没有暂存、提交、推送、构建、PDF检查、算法实验或共享写入。受影响条件已复读，但自查不是来源全核验或三方独立通过。冻结后停止写入，下一阶段由主代理按最终摘要组织独立审查。
