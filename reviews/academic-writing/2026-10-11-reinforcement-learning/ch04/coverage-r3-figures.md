# CH04 R3 Figure Source Coverage

正文 hash 同主报告；9 份图源逐文件完整读过，116 资源 hash 与 manifest 全匹配。以下 G 编号用短文件名及起始行定位，逐节点、逐坐标、逐连线语义记录。未渲染 PDF，不能据源码判字号、遮挡、分页或实际尺寸通过。

## Roadmap

`figures/rl-information-roadmap.tex`：
- G-roadmap-10 “两类信息限制” / 入口问题 / 正文23-95分别观测和访问权。
- G-roadmap-11 “历史与决策状态” / 不可见状态的输入解决 / 正文105-370。
- G-roadmap-12 “叠加限制与可识别性” / 两轴组合识别 / 正文1061-1254。
- G-roadmap-13 “评价与选择” / 先定可识别再有限估计 / 429-672。
- G-roadmap-14 “学习与改进” / 从固定D形成新候选 / 682-996。
- G-roadmap-15 “有限交互修正” / 放宽权限新增真反馈 / 1002-1051。
- G-roadmap-16 limits→history / 先明观测条件再选表示 / 23-95准备。
- G-roadmap-17 history→combined / 组合节用历史条件输入 / 1061,1159。
- G-roadmap-18 limits→evaluation / 固定权限是OPE设定 / 380,488。
- G-roadmap-19 evaluation→learning / 候选最终价值证据来自评价 / 682,937。
- G-roadmap-20 learning→rounds / 旧离线组件随新增D改 / 1006。
- G-roadmap-21 rounds→combined / 组合末节信息补充用辨识/验证预算 / 1254；此为阅读依赖非算法执行，K11已限定。
- G-roadmap-22 L22-23 evaluation→combined / 史IS依已讲换测度 / 1161。
- G-roadmap-24 L24-25 learning→combined / 部分识别与信息修复涉及保守候选 / 1178,1215。

## Aliasing

`figures/rl-information-aliasing.tex`：
- G-aliasing-12 “c=L” / 第一条隐藏提示左 / 40等概率任务。
- G-aliasing-13 “保留c=L” / 环境隐藏态仍保存线索 / 非策略可见状态。
- G-aliasing-14 “到达出口” / 隐藏过程终点 / 当前画面另节点。
- G-aliasing-15 “提示L” / 初始可见提示 / 可进入完整h。
- G-aliasing-16 “相同走廊” / 中部可见输入不辨c / 强制前进。
- G-aliasing-17 “相同出口画面” / 当前位置观测混叠 / 不含动作。
- G-aliasing-18 L18-19 “历史策略…选左” / 记L后选L / 旁注与观测分开。
- G-aliasing-20 “c=R” / 第二条隐藏提示右 / 对照唯一改变c。
- G-aliasing-21 “保留c=R” / 右隐藏线索持续 / 行为记忆不是箭头环境态。
- G-aliasing-22 “到达出口” / 同可见出口 / 两隐藏处境不同。
- G-aliasing-23 “提示R” / 初始输入可分 / 与L行对照。
- G-aliasing-24 “相同走廊” / 后观测不区分 / 与16相同。
- G-aliasing-25 “相同出口画面” / 当前帧相同 / 105观测混叠例。
- G-aliasing-26 L26-27 “记住…选右” / 右历史选R / 完整h能达到1。
- G-aliasing-28 l0→lm / 左状态演化 / 实线非观测。
- G-aliasing-29 lm→lt及省略号 / 多步走廊 / 不具体声称只有一过渡。
- G-aliasing-30 r0→rm / 右状态演化 / 同结构。
- G-aliasing-31 rm→rt及省略号 / 右多步走廊 / 延迟隐藏线索保留。
- G-aliasing-32 L32-33 六虚线 / l0/ol0,lm/olm,lt/olt,r0/or0,rm/orm,rt/ort / 每条是状态生成相应观测，不是策略选择动作。
- G-aliasing-34 L34-35 “实线…虚线” / 图例线型含义 / 与K126一致。

## Memory

`figures/rl-information-memory.tex`：
- G-memory-10 “递推记忆” / 面板a增量计算 / 258公式。
- G-memory-11 “历史注意力” / 面板b重新读h / 非同一计算成本。
- G-memory-12 “z_t” / 旧记忆输入 / 258已定义潜表示。
- G-memory-13 “f_theta” / 参数化更新器 / 用旧态和当前反馈。
- G-memory-14 “z_t+1” / 新表示 / 下一动作输入。
- G-memory-15 “a_t,r_t,o_t+1” / 已执行动作及新反馈 / 未使用未来奖励。
- G-memory-16 “策略” / 按新z决策 / 不直接读隐藏s。
- G-memory-17 old→update / 旧态参与更新 / 递推依赖。
- G-memory-18 update→new / 更新输出 / 数学z_{t+1}。
- G-memory-19 feedback→update / 反馈进入递推 / h追加内容一致。
- G-memory-20 new→policy / 新记忆给执行规则 / 非训练评价分数。
- G-memory-21 “h_t+1” / 全部记录史 / 不只是当前帧。
- G-memory-22 “注意力” / 从历史提取表示 / 有输入机制非只有名称。
- G-memory-23 “z_t+1” / 注意力输出 / 对照递推表示。
- G-memory-24 “追加动作与反馈” / 从h_t更新原历史 / 记录顺序不混。
- G-memory-25 “策略” / 用编码动作 / 同部署信息。
- G-memory-26 h→attention / 完整史进入 / 非只循环旧z。
- G-memory-27 attention→encoding / 重新计算z / 时间索引一致。
- G-memory-28 append→history / 反馈维护历史 / 不清空过去记录。
- G-memory-29 encoding→apolicy / z用于行动 / 两面板部署接口相同。
- G-memory-30/31 预热及后缀虚框 / 两个训练职责区域 / 非回合重置标记。
- G-memory-32 “预热前缀：重建记忆” / 前缀不计算损失 / K265有解释。
- G-memory-33 “训练后缀：计算损失” / 后缀才训练目标 / 与32顺序有依据。
- G-memory-34/35 两边界竖线 / 回合开始与损失起点 / 第二条不是回合重置。
- G-memory-36 “真实回合开始：重置” / 此图真回合开头 / 不扩大任意片段。
- G-memory-37 “不盲目清零” / 片段损失起点保历史 / 否定对象明确。
- G-memory-38 预热至feedback导线 / 序列反馈用于恢复 / 非梯度线。
- G-memory-39 预热至append导线 / 同序列可追加h / 模型类型不同不改数据时间。

## Tiger

`figures/rl-information-tiger.tex`：
- G-tiger-9 “b0(L)=.5” / 初始危险概率 / 294先验。
- G-tiger-10 L10-11 “直接开门…-45” / .5*10+.5*(-100) / 根动作单步真期望。
- G-tiger-12 L12-13 “成本-1…3.05” / 倾听再最优开门值 / 包含gamma .9。
- G-tiger-14 L14-15 “听见左侧… .95” / 贝叶斯后危险左 / 不是安全概率。
- G-tiger-16 L16-17 “听见右侧… .05” / 后验危险左 .05 / 与.95对称。
- G-tiger-18 L18-19 “开右门…4.5” / 左危险高开右 / .95*10-.05*100。
- G-tiger-20 L20-21 “开左门…4.5” / 右危险高开左 / 同条件值。
- G-tiger-22 prior→open / 直接根动作 / 无先验更新。
- G-tiger-23 prior→listen / 根选择信息动作 / 有成本。
- G-tiger-24 listen→left及1/2 / 听左概率(.95+.05)/2 / 非后验概率。
- G-tiger-25 listen→right及1/2 / 听右同半 / 初始对称条件。
- G-tiger-26 left→openright / 按反馈适应 / 有限末步4.5>-1。
- G-tiger-27 right→openleft / 相反反馈相反动作 / 非固定计划序列。

## Comparison

`figures/rl-information-comparison.tex`：
- G-comparison-5/6 上组刻度 / x0..8,pi2于y1/pi1于y2 / y为策略类别非回报值。
- G-comparison-7 “价值估计（回报）” / 横轴量纲 / 与659单值估计同指标。
- G-comparison-14 L14-17 pi1点5误差1.96 / 区间3.04..6.96 / 正态SE1条件。
- G-comparison-18 L18-21 pi2点4误差1.96 / 区间2.04..5.96 / 同95%。
- G-comparison-25/26 下组刻度 / -.2..1.6，Delta单行 / 不和上横轴假相同比例。
- G-comparison-27 “性能差估计（回报）” / 横轴为J1-J2 / 正数pi1好。
- G-comparison-34 L34-35 虚零线 / 检差是否含0 / 不与边际重叠等价。
- G-comparison-36 L36-39 点1误差.392 / 差区间.608..1.392 / SE.2乘1.96。

## Offline Pipeline

`figures/rl-information-offline-pipeline.tex`：
- G-pipeline-11 “固定数据D” / 仅原日志 / 所有拟合来源。
- G-pipeline-12 “Q,V” / 价值模型 / 和行为、环境分别。
- G-pipeline-13 “行为模型mu_hat” / 拟收集动作分布 / 非真实已知机制保证。
- G-pipeline-14 “P_hat,R_hat” / 环境预测 / 不新增真查询。
- G-pipeline-15 “动作提取…pi” / 从模型接口形成可执行策略 / 不输出价值作为策略。
- G-pipeline-16 “保留日志或授权测试” / 独立证据来源 / 固定协议不能自行授权真实测试。
- G-pipeline-17 “奖励目标与限制” / 学习目标输入 / 不是观察数据。
- G-pipeline-18 “定义损失” / 目标约束Q训练 / 价值学习目的。
- G-pipeline-19 data→q“拟合” / 用日志训练价值 / 实线数据依赖。
- G-pipeline-20 data→behavior“拟合” / 行为拟合 / 无奖励也可。
- G-pipeline-21 data→model“拟合” / 用真实转移训练P/R / 模拟样本不当新模型证据。
- G-pipeline-22 L22-23 “价值引导” / Q接口提动作 / 非自行取全动作可信。
- G-pipeline-24 “生成动作” / 行为模型供候选 / 样本非真实覆盖证明。
- G-pipeline-25 L25-26 “预测与规划” / 模型轨迹供计划 / 首动作输出。
- G-pipeline-27 “评价” / 固定pi送证据环节 / 选择误差另控制。
- G-pipeline-28 L28-29 “未覆盖动作” / 价值查询外推入口 / 对应反例a1。
- G-pipeline-30 L30-31 “未覆盖轨迹” / 模型滚动外推入口 / 图中两虚线是查询类型，正文693另说明动作生成位置，不以两线数量否定三语义入口。

## Extraction

`figures/rl-information-extraction.tex`：
- G-extraction-10 “价值驱动生成器训练” / 面板a是训练 / 非候选后筛选。
- G-extraction-11 “条件生成器” / 由s条件生成动作 / 872机制。
- G-extraction-12 “生成动作a” / 当前生成候选 / 不是真实执行反馈。
- G-extraction-13 “Q(s,a)” / 给生成动作价值 / 与数据a不同可能外推。
- G-extraction-14 generator→candidate / 正向生成 / 计算路径。
- G-extraction-15 candidate→value / 动作价值评分 / 为训练目标。
- G-extraction-16 L16-17 “价值梯度…回传” / Q梯度穿生成过程改参数 / 与Diffusion-QL描述一致。
- G-extraction-18 “生成后的价值筛选” / 面板b为部署接口 / 不更新行为生成器。
- G-extraction-19 “行为生成器” / 拟合行为后提样本 / 非价值梯度驱动训练。
- G-extraction-20 “a1…am” / m个样本集合 / 候选来源明确。
- G-extraction-21 “重采样或取最大” / 按权重随机或贪心 / 两变体不混同概率目标。
- G-extraction-22 “价值评分” / Q给候选权重或次序 / 不是模型新反馈。
- G-extraction-23 “最终动作” / 被选单动作 / 与872部署输出一致。
- G-extraction-24 behavior→candidates / 从行为模型采样 / 生成误差仍有。
- G-extraction-25 candidates→selection / 候选集进入筛选 / max只在m内。
- G-extraction-26 candidates→critic / 候选估Q / 范围不等全A。
- G-extraction-27 critic→selection / 评分作用选择 / 明确价值接口。
- G-extraction-28 selection→action / 输出选择结果 / 非行为模型作为动作。

## Confounding

`figures/rl-information-confounding.tex`：
- G-confounding-10 “普通隐藏状态” / 左隐藏不额外进动作 / 条件h后的随机数独立。
- G-confounding-11 “隐藏混杂” / 右多未记录动作原因 / 不是所有POMDP都该图。
- G-confounding-12 “U” / 左潜变量 / 虚框表示未记录。
- G-confounding-13 “h_t” / 左可记录历史 / 执行行为可见。
- G-confounding-14 “a_t” / 左动作 / 只根据h选择。
- G-confounding-15 “Y” / 左未来反馈 / K1121已释。
- G-confounding-16 U→h / 隐状态影响历史观测 / h可作条件。
- G-confounding-17 U→Y / 隐状态影响后果 / 不自动混杂。
- G-confounding-18 h→a / 行为依记录历史 / 独立策略随机数另假。
- G-confounding-19 a→Y / 动作影响反馈 / 因果假设不是日志证明。
- G-confounding-20 “U” / 右未记类型 / 观察字段未变。
- G-confounding-21 “h_t” / 右同记录历史 / 给定仍有隐藏路径。
- G-confounding-22 “a_t” / 右动作 / 另取U信息。
- G-confounding-23 “Y” / 右后果 / 潜在共因影响。
- G-confounding-24 U→h / 同普通图观测关系 / 不是新增字段。
- G-confounding-25 U→Y / 类型影响后果 / 与动作共因。
- G-confounding-26 h→a / 行为也用记录信息 / 并非只看U。
- G-confounding-27 a→Y / 动作后果关系 / 同模型任务。
- G-confounding-28 U→a / 新隐藏动作依据 / 给定h仍后门U。
- G-confounding-29 L29-30 “随机数独立于U” / 左无额外混杂 / 正文1159条件对应。
- G-confounding-31 L31-32 “U仍影响动作” / 右专家隐藏信息 / 与1127专家可见U反例。

## Identification Width

`figures/rl-information-identification-width.tex`：
- G-width-5/6 x对数及刻度4,16,64,256 / 样本量非时间或训练轮 / 刻度按log2且标实际n。
- G-width-7 y刻度0,1,2,3,4 / 回报数值 / 原识别范围1..3。
- G-width-8 “样本量n”“价值（回报）” / 两轴单位 / 横n与解析半径对应。
- G-width-14 填色1..3 / 总体识别包络 / 固定随n不变。
- G-width-15 虚线y1 / 总体下端 / 不是采样下界。
- G-width-16 虚线y3 / 总体上端 / 与上端识别同层。
- G-width-17 L17-18 1-2/sqrt x / 示意统计下端 / n4为0,n256为.875，趋1。
- G-width-19 L19-20 3+2/sqrt x / 示意统计上端 / n4为4,n256为3.125，趋3。
- G-width-21 L21-22 “不可消除的识别宽度” / 固定日志机制下总体宽2 / 正文1217限定同类样本，非对新增信息永久不可消。
- G-width-23 L23-25 双向箭头 / 示意上侧统计额外宽度 / 非精确标尺数值声明，不从像素推置信保证。
- G-width-26 L26-27 “统计误差示意” / 外层半径教学 / 正文明确不是推导置信曲线。
