# 第11章独立复核闭环

审查者未参与本章起草；章/段/句三遍已完成（173源文块、742句及特殊单元），补充44纯标题块，未遗漏空行隔开的纯公式。第三遍读数按ID而非从作者自查继承接受。修前SHA为fa5f68c72f2d8b59c3ca47059c8fe0857ccf5897421522d4cfcd77a73c2fecd6，修后为cc745030cf3b8a7581cb641e9bdcb3fa8191e7bf8b253fdff67c628cb0dff9f9；不可变全文在snapshots/before和after。修改逐字存chapter-11-repairs.json。

C11-R01（P092/S03）：a=b缩放除零；补常量分支且Pinsker缩放明确a<b。复读layer-cake到下一Rényi事件段，常量差0、正宽度系数和2因子仍正确，已关闭。
C11-R02（P123/S02–03）：下确界分解∞−∞；明确族中至少一finite-KL候选及实际候选finite，非负inf必finite，非attainment仍可拆。复读Jensen两方向支持例→分解→高斯数值及蒸馏，未改变公式或输出，已关闭。
C11-R03（P089/S01–02）：点访问次数可数分组缺域；明确finiteT、finite/countable位置、standardBorel观测、P0核≪P1核，零访问∞项按0；连续域保留逐步/访问测度。复读Rényi/停止邻段、分组和Bernoulli预算完整，作用是非负累计可换序，已关闭。
C11-R04（P035/S02）：普通括号替数学环境；复读引OT/耦合定义确认不变两温差场景，已关闭。
C11-R05（P021/S02）：换元密度和finite entropy域不够本地明确；补X Lebesgue密度及logp L1，与logJac L1保证Y log密度L1。复读参考measure变化→Jac换元→差异入口，已关闭。
C11-R06（P084/S02）：tensorization范围未说finite而只证有限乘积；限定t1…T和P_t≪Q_t。复读小标题→有限乘积证明→一般条件核chain，finite负log和/非负矩积都合法，已关闭。
C11-R07（P070/S02）：相应AC方向含糊；明确jointP≪Q并推出marginal与P_A-a.e conditionalAC。复读异或例→KL链→数据处理证明，非负扩展分解不需无穷相减，已关闭。
C11-R08（P125/S02）：teacher KL与crossentropy等价需finite teacherentropy；原段类别任务限定finiteclass，补显式conditionalKL平均与固定inputlaw。复读posterior例→teacher→InfoNCE采样，有限类熵≤logM使常数可减，已关闭。
C11-R09（P137/S01）：首次0,2场景错误“仍取”回指；明确两侧位置0,2。复读Lagrange→表与dual→nextgeometry，原/对偶1及独立5/4/图注一致，已关闭。
C11-R10（P087/S02）：条件Rényi预算历史域含糊；明确Q-a.e历史及kernelAC才可在Q下tower后向积分。复读finite tensor→chain→环境/action消项→Rényi→stopping→访问式，统一条件界没有偷换成前向平均，已关闭。

七门槛：G1对象/变化/保护量明确（P024–026、P073–082、P154）；G2短码、意外、核平均、倾斜等均有白话对象（P006、P032、P098）；G3从分布到代表元、配对、参数切向、样本joint的转换各有定义条件（P031–036、P139–149、P162–164）；G4Holder→Minkowski→粘合、KL→尺度、有限局部→geometry的顺序合法；G5编码/温差/位置预算/同样本选择具体场景牵引工具；G6十发现修复并邻域闭环，积分/支持/局部及边界条件留存；G7KR对偶引用明确难方向未证明，Riesz/Prokhorov/LP/前章score引用本地均说明用途，不以指路代解释。

E1：P154同预算及P059同位置族统一比较基准通过。E2：P050方向、P051支持、P122AC双向、P159退化range均有真实后果。E3：耦合表/自然方向/风险界输出明确。E4：否定旁有正面机制（P020精度项、P134拆质量、P159unbounded）。E5：最近点检验和联合依赖桥梁（P076–082/P162–164）。E6：重用高斯/点质量每次增加尺度、表示、推断或局部边界责任，非重复占位。E7：P137错误回指已修，其余引用有本地内容。E8：入口与各节先实际场景。E9：TV全事件、测试类、目标2s和椭圆ε都定义集合/准则。E10：P142–160反复把二阶/一阶限制在local、不声称finite/global。E11：RN/conditionalkernel方向及域已修，其余新符号定义在使用前。E12：P094尾质量、P108温度只说可能波动↑、P154同预算下降量有baseline，不许无条件改进。

44标题补充：X001章对象由全章兑现；X002–006离散无条件/条件和连续精度分别对应P005–021；X007–014四尺度及无条件/条件联合关系对应P023–072；X015–021固定/序贯及两点/多点/访问预算对应P073–090；X022–025三种已知函数条件对应P091–102；X026–033三不同优化未知量与存在/离散求解对应P103–137；X034–040局部分布距离/坐标保持/更新/奇异近似对应P138–161；X041–043样本后选的平均与同时风险对应P162–169；X044小结对应P170–173。纯标题无独立公式，但按其概括承诺实际审查。

静态核验：原标签/标题/图路径/引用均保留，环境及行内/行间math边界配对。只检查源文本和数学语义，未声称检查PDF渲染、图像像素或运行构建；最终全卷构建由根任务完成。没有未关闭正文发现。


170 display-math blocks in the immutable baseline are indexed in ch11-display-formula-index.json and each is linked to its already-read manual P/S record. This is a location supplement only; it introduces no automatic semantic judgment and does not alter the source hash.
