# CH07 最终独立复核：递归图源

## 范围

正文直接引用14个TikZ/PGFPlots图源；`rl-multi-agent-trajectories.tex`和
`rl-multi-agent-stability.tex`递归读取共享数据源
`rl-multi-agent-dynamics-data.tex`。以下15个文件均按图内文字、箭头、数值、
公式、图注和正文引用关系读取。

| 图源 | 科学语义核验 |
|---|---|
| `figures/rl-multi-agent-map.tex` | 收益与信息约束行为标准和数据，联合经验进入估计、价值进入更新，新策略回到经验来源，适配与评价另接；箭头与章首解释一致。 |
| `figures/rl-multi-agent-timing.tex` | 同轮送达在行动前，延迟消息只进入下一轮历史；顺序行动权限另行声明，没有由程序调用次序偷加信息。 |
| `figures/rl-multi-agent-card-tree.tex` | 机会高低牌各半，1和2的行动节点、下注/过牌/弃牌/跟注叶收益与正文规则一致；2面对下注和过牌的两个信息集分别跨牌面连接。 |
| `figures/rl-multi-agent-ctde.tex` | 局部历史只进各自行动者，训练信息和联合动作只进评论家；动作输入标“仅Q”，训练梯度虚线可在部署删除。 |
| `figures/rl-multi-agent-exploration.tex` | 独立噪声、公共信号、角色条件和通信四条路径区分相关行动依据；箭头只表示执行者实际得到的信息。 |
| `figures/rl-multi-agent-data-loop.tex` | 支持充分进入经验构造；不足后先查权限，再分别继续采集、批间重定或限制结论，循环方向与正文一致。 |
| `figures/rl-multi-agent-mixers.tex` | VDN求和、QMIX状态条件单调混合；状态只进训练混合器，局部`argmax q_i`用于执行，虚线为训练反传。 |
| `figures/rl-multi-agent-trajectories.tex` | 三面板分别使用同时更新、交替更新和历史最佳响应；轴为`p,q`或累计平均，初值与均衡标记一致。 |
| `figures/rl-multi-agent-dynamics-data.tex` | 共享递推以`eta=0.1`、初值`(0.7,0.5)`生成同时与交替序列；交替的`q`使用已更新`p`。历史响应对截至当前累计平均生成下一轮响应，平局用容差回退`1/2`。当前间隙、平均间隙和两方平均外部遗憾正部公式与正文一致。图展示的首末点间有120次可见更新；文件尾额外算出的下一状态未被绘制，不改变图示。 |
| `figures/rl-multi-agent-cfr-reach.tex` | 真实到达含机会、1过牌和2下注三因子；CFR反事实权重删去1的前序因子；平均策略权重恰使用该自身因子。 |
| `figures/rl-multi-agent-psro.tex` | 策略库经对局估计收益表，元策略规定响应对象，近似响应训练后冻结加入库并补测；库索引与环境动作明确分开。 |
| `figures/rl-multi-agent-stability.tex` | 复用同一交替梯度序列画当前总间隙、平均策略总间隙和两人累计平均遗憾正部较大者；纵轴为精确矩阵收益单位，图注未宣称实验成绩。 |
| `figures/rl-multi-agent-graph.tex` | 右图只重排同一物理三节点图，通行者角色和对应输出随节点重排；邻域消息经同一集合聚合器，符合等变定义。 |
| `figures/rl-multi-agent-cross-play.tex` | A、B均用L，C用R；同约定格为10、异约定为0，对角深框只标同来源。九格和为50，与正文均值`50/9`一致。 |
| `figures/rl-multi-agent-scaling.tex` | 全连接使用`m(m-1)`条有向边，局部曲线使用`m min(4,m-1)`的满额出邻居数；节点和边串行成本与正文两式一致。 |

## 图源结论与限制

- 图内术语、颜色语义、箭头方向、数值和正文图注一致。
- 共享递推未把当前策略、平均策略和遗憾曲线混成同一输出。
- 本次只核验TeX图源的科学语义，未运行图源程序、未构建、未查看最终PDF，
  因而不对字体、裁切、溢出、浮动位置或实际书页排版作通过结论。
