# 修订后独立复核

工作区：`/Users/bytedance/Projects/notes_on_machine_learning/.worktrees/volume-one-readable-review`。
你未参与本章和影响本章判断的上下文改写。本次只复核，不改正文，不启动构建，
不暂存提交或集成。只写分配的 `final/chNN/` 记录。

完整读取 academic-writing 技能及 review、review-records、grammar-and-style、
content，项目 AGENTS/development/writings/latex 规范。
本目录初审与修复要求可确定任务边界；真正审读以 `repair-manifest.json`
所绑定的实际正文及 `snapshots/after/` 为准，不把初审覆盖自动算作新版本覆盖。
先独立顺读正文建立自己的判断，再读合并发现及关闭理由。

读者学过本科常见数学，按卷内顺序首次阅读当前进阶概念。重点检查语句能否读顺、
新概念在当地是否解释为何需要、解决什么问题、与此前概念的关系和区别。
必要的引用回到前文实际上下文，不借后文、聊天或代理专业常识补洞。

按章级→段级→句级完成三遍，保存有实际作用/白话复述/具体接受理由的三级覆盖、
七门槛和E1—E12校准、核心公式与难概念解释时序。
长章可拆记录，不能用宽范围覆盖、抽样或自动模板语义判断代替实际阅读。
逐项核对 `consolidated-findings.json` 中本章修复及撤销证据，
把原障碍、修订与当前上下文判断绑定同一版本。

正文涉及必要条件或错公式时指出具体缺失，不能仅写“编译通过”即关闭。
记录区分真实读者反馈与独立AI复核；你是独立AI复核。
返回 `report.md`、`paragraphs.md`、`sentences-*.md`、`closure.json` 和
`new-findings.json`，保存逐文件摘要、组成范围、连续阅读范围、
记录结论与正文结论及未核查文献/图源/程序/最终PDF的限制。

有未解决阅读或技术问题时结论为待修改；无法真正完成全部三遍时结论为证据不足，
并明确实际剩余范围。只有完整覆盖、全部适用门槛和成立发现关闭后，
才写“在声明范围内通过”。主代理随后完成工程构建与版面检查。
