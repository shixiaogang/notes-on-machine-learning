# CH08 最终独立复核：图源

正文直接引用12个TikZ/PGFPlots图源，均完整读取；这些图源没有递归`\input`。

| 图源 | 科学语义核验 |
|---|---|
| `figures/rl-trustworthy-map.tex` | 共同对象分到风险、鲁棒和安全三条并行支路，汇入共同验证、组合取舍和综合结论；连接线不表示算法先后。 |
| `figures/rl-trustworthy-loss.tex` | 两分布分别为`δ_1`与`0.95δ_0+0.05δ_20`，均值均1；0.95分位点分别1和0，最差5%质量分别取1处原子部分和20处全部质量。 |
| `figures/rl-trustworthy-risk-tree.tex` | 静态面板按叶节点联合概率得到11，嵌套面板先在A得到20、B得到10，再在根得到20；对应同一risky物理树。 |
| `figures/rl-trustworthy-channels.tex` | 真实状态、观测通道、策略请求、执行通道和环境转移分开；观测例不改变真实位置，执行例显示旧队列动作本拍生效。 |
| `figures/rl-trustworthy-rectangular.tex` | 真实耦合集为`p1+p2=1`斜线，矩形外包为单位方形；左下`(0,0)`只属于外包，不属于共享参数模型。 |
| `figures/rl-trustworthy-primal-dual.tex` | 奖励/成本评论家给策略优势，累计成本与预算差给乘子，乘子再进入惩罚后策略更新；图注明训练轨迹不会自动安全。 |
| `figures/rl-trustworthy-events.tex` | 首次失败树用存活条件概率`q_t`，整回合概率为乘积补集；训练期另对可能变化的多个策略回合取并集。 |
| `figures/rl-trustworthy-filter.tex` | 候选请求经状态估计、模型/误差集和备份/证书共同检查后成为实际动作；日志区分实际动作、后继和干预并反馈学习器。 |
| `figures/rl-trustworthy-validation.tex` | 预设协议→取证→指标/误差界→判断；条件或方案变化回到协议，补证/收窄/保护回到取证。流程未冒充统计保证。 |
| `figures/rl-trustworthy-intervals.tex` | 100次零失败上界2.9513%高于1%，299次上界0.9969%低于1%；回报示意以区间下界相对阈值判断，方向正确。 |
| `figures/rl-trustworthy-intersection.tex` | 三个阈值允许集合与策略类的交集仅作概念示意；图注明确不表示数值嵌入或凸性。 |
| `figures/rl-trustworthy-protected-path.tex` | 无保护路径5步穿危险格；有保护先走到`(2,1)`、拒绝向右、返回起点并走上路，共7步。虚线请求与实际备份路径分开。 |

## 图源结论与限制

- 图内标签、箭头、概率、数值、路线步数及正文图注一致。
- 未发现把机制扰动、观测扰动、执行扰动或候选策略、保护系统混写的图示。
- 本次只核验源文件科学语义，未构建或查看最终PDF，不对裁切、溢出、字体、
  浮动位置或颜色成品作结论。
