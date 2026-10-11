# 七旧包装的实际全书入站

扫描对象：真实rebase HEAD33a06c0706bd8242083eb8d5d1abad367fe50117的341个tracked tex/md（tex与plans）；源字节来自Git show，无生产修改。结果seven-inbound-rebased.json：7个定义处+4真实调用+1proof自引；旧label字符串没有任何plans/reviews归档命中，也无非PGM入站。唯一隐含“前两定理”在04:383。将candidate放入同一实际全书label/ref图后，全部525PGM引用有目标，旧7label无悬空调用。

|旧结果|before精确删除范围|普通段/真实迁移位置|
|---|---|---|
|D01 def:pgm-directed-faithfulness|02:238–248|candidate02:238先Markov再忠实→集合相等；04:88改BookDefinitionRef{def:causal-faithfulness}，I/D方向本地恢复。236参数动机保留。|
|D02 lem:pgm-undirected-intersection|03:268–284|candidate03:268有限/非空/全乘积正和两独立前提合并普通化；引用类型BookLemmaRef。无旧显式入站；270以后逐变量归纳与Markov等价证明保留。|
|D03 thm:pgm-representations-ancestral-moralization|04:106–117|candidate04:106完整查询条件+两结构判据；115自引proof随引用式proof取消；before183→candidate172 BookTheoremRef{thm:graph-theory-ancestral-moralization}，g/h/k归一化不删。|
|D04 thm:pgm-representations-chordal-perfect|04:356–367|candidate04:345同节点等分离iff弦+PEO反序构造；before516→candidate483 BookTheoremRef{thm:graph-theory-chordal-perfect}，空因子/Z/q_k算法保留。|
|D05 thm:pgm-representations-perfect-undirected|04:370–381|candidate04:348父集成团iff可完美无向表示、骨架弦；before383→candidate350“这两种转换”，保留与固定p忠实性区别。无显式入站。|
|D06 thm:pgm-junction-tree-maximum-weight|06:251–259|candidate06:251完全极大团图含0边与最大权iff运行交集；before619→candidate611 BookTheoremRef{thm:graph-theory-clique-tree-maximum-weight}。局部消息依赖+后续合并步骤保留，不冒称每个消元步等一个团消息。|
|D07 thm:pgm-variational-cut|07:874–888|candidate07:874–881有限二元成对逐边次模→w≥0/D′/C普通应用；无旧显式入站。源0汇1、割E−C、885算例、897–903LP阈值完整承接保留。|

档案边界：未修改任何旧review快照或旧labels记录。上述精确range以rebased-binding逐字相同before源为准，patch同时消除Needspace仅为旧盒预留的命令，不改变章节层级、input或图资源。数学符号桥新增是应用摘要，不重建第二个格式化定理或卷一完整证明。

四真实迁移与隐含序数实际重读：04:85–91、169–197、342–353、448–487，06:608–614；D02额外读03:252–310；D07读07:852–920并逐源Graph1613–1688核对。
