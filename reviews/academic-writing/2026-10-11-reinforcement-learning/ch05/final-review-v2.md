# 第5章最终独立复核 v2

## 身份与受审对象

- 日期：2026-10-14；角色：未参与第5章正文、图源、词典及本轮修订的最终独立复核者。
- Worktree：`/Users/bytedance/Projects/notes_on_machine_learning/.worktrees/rl-review-20261011-ch05-r1`
- 分支：`codex/rl-review-20261011-ch05-r1`；基线HEAD：`75175dea03ad6c4d9b20299835b48c087a052505`
- manifest SHA-256：`b854336c0668359a4279ba2cb68fd8ed7263fdb5266587dca6053c80bf37d300`
- 正文：`tex/04-paradigms/01-reinforcement-learning/05-reward.tex`
- 冻结快照：`ch05/integrated-final-v2.tex`
- 正文与快照 SHA-256：`12250894a8a5ecd359bbb4a68e040c0ed77f44d6600c524103f7a0581030a681`，逐字节一致。
- 旧v1快照：`integrated-final-v1.tex`，SHA-256 `dec8f755107429df29f8b99fd374f2ed201bf5c4733c88ee25cbfc9fe2232d3c`。

精确diff只有L314、L322、L552三处首现术语修订；其余正文、公式、图表、引文和结构不变。本轮仍重新执行章级、段级和句级三遍复读，并重查特殊单元与专项门槛。

## 覆盖索引

- `final-coverage-v2-c.md`：C1--C4全文重核。
- `final-coverage-v2-p.md`：全部自然段P1--P5复读及三处受影响段。
- `final-coverage-v2-w.md`：W001--W667复读及三处受影响句群。
- `final-coverage-v2-special-gates.md`：特殊单元、方法链、范围转换、七门槛和E1--E12。
- `final-coverage-v2-closure.md`：原7编号、`CH05-FR1-01`及v2回归闭环。

## 发现与关闭

- v2新发现：0。
- `CH05-FR1-01`：复核通过并关闭。
  - L314“学徒学习”已使用术语宏并登记 `apprenticeship learning`。
  - L322“最大熵逆强化学习”已使用术语宏、补英文名称并登记映射。
  - L552“基于可验证奖励的强化学习”已使用术语宏并登记RLVR英文映射。
- 当前39个术语宏调用全部可在最终共享词典解析。
- v1已关闭的原三审7个编号在v2无回归。

## 结论

- 记录结论：v2最终复核记录可接受。
- 正文结论：在声明范围内通过。`CH05-FR1-01` 已关闭，三遍复读、专项复核和回归检查均未发现新问题。
- 旧 `final-review-v1.md` 的正文“待修改”结论只适用于旧哈希，已由本报告取代。

## 核验限制

- 一手来源：沿用v1对IQ-Learn和AIRL原论文及作者代码的独立核验；本轮术语修订未改变来源主张，未逐篇重读其余引文全文。
- 证明：本轮复读全部正式证明和关键推导；未用证明助理，也未认证引用论文完整附录证明。
- 程序：未运行算法、模型训练、统计实验或绘图程序。
- 版面：遵照任务要求未构建、未查看最终PDF；字体、断行、表宽、浮动体、边注、溢出和页数未验收。
- 图像：9份图源科学语义结论无回归；这不等于最终书页版面通过。
- Git：未暂存、提交、推送、集成或启动其他代理。
