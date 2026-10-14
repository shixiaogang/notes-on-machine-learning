# CH05 final-v1 交付审计

- 日期：2026-10-13；角色：第5章汇总修订者，AI自查，不是独立复核。
- Worktree：`/Users/bytedance/Projects/notes_on_machine_learning/.worktrees/rl-writing-20261011-ch05`；分支：`codex/rl-writing-20261011-ch05`。本轮未创建新worktree，复用指定章工作区；未构建、暂存、提交、推送、spawn或集成。
- 实际正文：`tex/04-paradigms/01-reinforcement-learning/05-reward.tex`，L1-1105。
- [final-v1.tex](final-v1.tex) 与实际正文逐字节相同；SHA-256 `662ddf71163e2bc46cebc096ca0a45506d2f1a352598bb2baa73b70aa99d1557`；`shasum -a 256 -c final-v1.sha256` 实际返回 `final-v1.tex: OK`。
- 原freeze：[rewrite-v1.tex](rewrite-v1.tex)，SHA-256 `0c9b1018b03c0bfaf39abe12ad4ee9f18d9716aebce5fc8f443a86168874e8b8`。原写者及三方报告保持；原七发现全部成立，五类根因，修七条、撤销零条，全部待独立复核。

## 覆盖索引

- [repair.md](repair.md)：逐个原编号的改前/改后版本、短引、合并判断、实际动作及连续回读、新缺陷回归。
- [coverage-repair-cp.md](coverage-repair-cp.md)：分开的第一遍C1-C4及第二遍P1-P5，P001-P204。
- [coverage-repair-w01.md](coverage-repair-w01.md)：第三遍P001-P054。
- [coverage-repair-w02.md](coverage-repair-w02.md)：第三遍P055-P108。
- [coverage-repair-w03.md](coverage-repair-w03.md)：第三遍P109-P162。
- [coverage-repair-w04.md](coverage-repair-w04.md)：第三遍P163-P204。
- [coverage-repair-gates.md](coverage-repair-gates.md)：七门槛/E1-E12、全部局部入口、方法链、范围、F01-F38及行内/特殊单元。
- [sources.md](sources.md)：IQ/AIRL训练目标、六名称及DAPO会议一手证据/版本/未核边界。
- [shared-repair-requests.md](shared-repair-requests.md)：六术语词典登记、可选已有引文接入与版面请求，主代理串行处理。

## 静态核对

|对象|实际结果|
|---|---|
|全部标题|30→30，命令/文字/顺序均与rewrite-v1及base.tex相同，独立本章小结保留。|
|全部标签|86→86，文字/顺序均与rewrite-v1及base.tex相同，没有新标签或删除原标签。|
|图入口|9→9，input目标及顺序相同，未生成或修改图源。|
|文献引用|21→21，全部scite目标及顺序相同，没有新增key。|
|正文回指|48→50；新增两处对本章既有`eq:rl-reward-airl`的eqref（原0次→2次），在D分母本轮mu替换说明及对数几率信号推导；其他目标不删不改。|
|展示式|34→38，原34组逐字保留且顺序保持；只新增IQ总体/经验目标及AIRL来源似然/对数几率4组无编号展示。|
|语法静态|正文UTF-8有效，花括号平衡0且无提前闭合，begin/end栈无遗漏；`git diff --check -- <本章>`返回成功无输出。不是LaTeX构建或宏展开验证。|
|三级枚举|204源块、30纯标题定位块；P记录与W范围无缺块。W中P006/P007合并定位已人工核实，不是漏P007。|
|句与特殊枚举|614机械正文句单元（含公式前后续句），53图表注句单元，76表行含表头，38展示组。正文长句含多个实际句/动作在W中另用a/b或短引分核；数字只检漏，不作语义接受。|
|环境|5定义、4定理、3显式proof加DAgger正文论证、4示例、14表、9图、2算法均纳入。算法A含Require/Ensure、控制条件及结束命令，逐步骤检查，非只算State。|

句号枚举与W记录逐P对照，正文S编号无缺项。第一次快照比较使用UTF-8正文字符串与二进制字符串导致Ruby字符串比较为false；重新用双方`File.binread`比较为true，并独立SHA核对和checksum校验为同字节。未以该编码比较误报替换正文。静态检查的Ruby旧版本不支持`tally`，改用标准Hash计数后完成引用差异核对；没有跳过失败项。

## 写入边界

- 开始及结束，对全部已跟踪文件排除本章后按 `git ls-files -z` 次序计算逐文件SHA-256清单再取摘要，均为 `91d010755809d62491b3da68f4c658638bd2f81647f84e6d1a06dc5c824e3255`。证明其他已跟踪正文、共享输入、图源、产物未被本轮改变，不把它扩展为所有未跟踪目录的完整审计。
- 原ch05全部提供材料按路径排序的逐文件SHA清单摘要，开始和结束均为 `2f1d8df00fb4dfbaeb62d6deeb08544a0749a6ff74dcbf4178347acd067b1968`；结束计算排除本轮新增repair/coverage/sources/shared请求/final文件。原报告及coverage未覆盖。
- 结束git status仍为提供的八章M及reviews未跟踪；本轮只编辑指定05正文和新增本章修复目录文件，未暂存他人成果。
- 最后检查所用curl/hash/ruby/xargs子进程均无残留运行项。曾有一次hash命令返回异步会话，但进程已退出并用同步同命令重核，未以未完成会话结果结束。

## 实质变化与回归

- 延迟表无条件方差增大命题已收窄，加入确定性与固定随机X/折扣反证、记录到达与奖励所属时刻区分，其他三性质未删除。
- IQ原三行编码全部保留，补专家线性奖励/专家平方正则/初态项、离线经验残差和下降。单后继随机平方多条件方差、完整与受限对偶、吸收质量及温度归一化边界明确。
- AIRL原D/f/g/h式保留，补来源1/0似然、策略对数几率、mu分母/冻结/刷新、一次梯度及迁移仅g、恢复条件；没有把GAIL变换照搬。
- E/B/C/D歧义例的比较两端补清；六名称首现核一手后规范，DAPO先于表展开，其后机制保留。
- 自查发现的新增缺陷也实际处理：尺度方向/受限散度/负熵语境、AIRL一步链接条件和采样权重；末次L283收窄初态项“抵消线性增量”，避免误说任意平移不能改善平方项。最终hash下连续回读L239-329，章级接口、P052段链、S08及F11作用均重新核，其他正文未变。

## 结论与移交

- 记录结论：本轮修订、自查、原发现处理与版本/范围核对可归档。脚本只枚举核对，语义依据由实际阅读形成。
- 正文结论：汇总修订及修订者自查完成，待独立复核。没有收到未参与修订者的最终复核，不能称最终通过。
- 限制：必要前文仅局部重读；没有本轮前四章全文重新验收、全部引文一手全文、9图全部图源、研究程序/训练/实验、机械证明或最终PDF版面验收。已核一手仅`sources.md`的目标/命名及条件范围。
- 本章停止写入。请主代理以`final-v1.tex`及摘要在独立工作区交未参与修订者完整三遍复核，并串行处理共享词典/引用选择、构建及成品检查；所有原编号的最终关闭由独立复核决定。
