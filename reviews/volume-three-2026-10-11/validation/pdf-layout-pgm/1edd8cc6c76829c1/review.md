# PGM PDF visual QA: fixed SHA 1edd8cc6c76829c1

PDF SHA256: 1edd8cc6c76829c1bbb4b77e0bb6ab94be59915abb3cfcba45112ef5c2e558a7

Actually viewed: 5 contact sheets, 53 physical PDF pages containing 57 PGM figures, plus 26 original 140dpi detail pages. Existing root render files were only read. The first 17-detail layout-only record is preserved as review-layout-r1.md and manual-observations-layout-r1.json.

No caption separation, clipped diagram, figure/side-note overlap, or layout repair was identified in the PGM figure-page scope. Four caption/figure-label claims are inconsistent or unclear in this fixed PDF and were reported for root text repair; see PGM-PDF-F01 through F04. This PDF is therefore not declared free of all figure-caption issues.

Contact-only pages support overall placement/caption/obvious-overlap observations. Font strokes, explicit caption colours, and precise endpoints were additionally examined on the twenty-six detail pages. No new full-source technical audit, latest cross-volume alignment, or inspection of all 1050 pages is claimed. No production file, PDF, or render was changed. This record only applies to PDF SHA 1edd8cc6c76829c1bbb4b77e0bb6ab94be59915abb3cfcba45112ef5c2e558a7. Root is repairing text and will rebuild; those subsequent PDFs require their own review.

Native-detail pages: 681, 685, 692, 694, 712, 736, 737, 762, 773, 781, 790, 802, 835, 842, 870, 901, 912, 923, 930, 936, 961, 962, 972, 973, 978, 982.

## Caption and displayed-label findings

### PGM-PDF-F01 - PDF 736 (printed 720) - figure 19.1

Source address in pre-repair text: tex/06-probabilistic-graphical-models/01-representation/04-representations.tex lines 28, 32.

Claim: 对应图中的点线和$\times$；虚线及“补$H-S$”表示这条新增边；检测分离时删除红色且标有“给定”的条件节点$A$；带“补”标签的虚线表示新增的边

At book-page scale, the small cross is not clearly distinguishable. The source does contain a cross node at L24. The actual page has no clearly displayed supplement-H-S or given text labels, although the caption and following paragraph refer to them.

Minimal repair: Describe the dotted descendant/edge, dashed H-S, and red A directly; remove claims that the missing cross and text labels are present.

Status: reported to root; pending text repair/new PDF review.

### PGM-PDF-F02 - PDF 737 (printed 721) - figure 19.2

Source address in pre-repair text: tex/06-probabilistic-graphical-models/01-representation/04-representations.tex lines 48.

Claim: 上方规则说明$\operatorname{elim}(X_k)$要使剩余邻居成团。

Only the PEO step heading and elim(4/2/1/3) tags are present; no rule text appears above the figure.

Minimal repair: Say that the tags identify the eliminated node and that the remaining neighbours in each step are pairwise connected.

Status: reported to root; pending text repair/new PDF review.

### PGM-PDF-F03 - PDF 901 (printed 885) - figure 25.3

Source address in pre-repair text: tex/06-probabilistic-graphical-models/03-learning/02-structure-learning.tex lines 586.

Claim: 右侧概率框以同色箭头与结构对应。

Row backgrounds are blue/yellow/red, but the middle row's probability-box outline and outgoing arrow are green.

Minimal repair: Say that the right probability boxes and connecting arrows give each structure's prediction; omit the same-colour claim.

Status: reported to root; pending text repair/new PDF review.

### PGM-PDF-F04 - PDF 962 (printed 946) - figure 28.3

Source address in pre-repair text: tex/06-probabilistic-graphical-models/04-models/03-dynamic.tex lines 425.

Claim: 引线对应各曲线。

There is a posterior callout only; the other two curves are distinguished by the legend, not separate callout lines.

Minimal repair: Say that the legend distinguishes the three curves and the red callout marks the posterior.

Status: reported to root; pending text repair/new PDF review.

## Kalman time-label distinction

L31 lists filt[2]=(1.427,1.079), filt[5]=(4.848,2.201), filt[8]=(7.546,4.363). L35 adds the three ellipses at exactly those centres. L37 separately annotates filt[0], filt[4], filt[8] with t=0/4/8. The time labels and covariance ellipses describe different objects; the caption ellipse times 2/5/8 are correct.

## Hand-written page observations

### PGM-PDF-01 - PDF 680 (printed 664) - figures 16.1

Observation mode: contact layout overview.

双峰预测密度图在页上部，图注紧随其下，后续说明从图注下方起排；图外右侧留白没有被旁注或其他浮动体占用。

### PGM-PDF-02 - PDF 681 (printed 665) - figures 16.2

Observation mode: contact and native detail.

图16.2三列视觉约定与图注均完整。详情中空心/填色/实点、因子方框、圆角外框、浅色共享接口及绿色轮廓、红叉各自清楚；图注的浅色填充/绿色轮廓/红色警示说明与图对应，正文不碰图块。

### PGM-PDF-03 - PDF 682 (printed 666) - figures 16.3

Observation mode: contact layout overview.

设备诊断图16.3置于正文之间；图形的四节点链与图注均在正文栏内，后续段落在图注之后续排。

### PGM-PDF-04 - PDF 685 (printed 669) - figures 16.4

Observation mode: contact and native detail.

历史图14张事件卡片、中央路径及底部三个研究问题框均完整；图16.4的三行图注在同一页底部，未拆到下一页。详情中年代、模型名和机制文字可读，圆角卡片边框未裁切。

### PGM-PDF-05 - PDF 688 (printed 672) - figures 17.1

Observation mode: contact layout overview.

第17章章首页的标题、章首说明和图17.1分开；图形下的拓扑排序文字及图注都留在页内，没有靠近页脚的裁切。

### PGM-PDF-06 - PDF 691 (printed 675) - figures 17.2

Observation mode: contact layout overview.

图17.2的Markov毯节点与图注居中，图后定义框从下一块正文区域开始，框顶没有碰到图注。

### PGM-PDF-07 - PDF 692 (printed 676) - figures 17.3

Observation mode: contact and native detail.

图17.3四种局部关系以两行安排。详情中链/分叉的状态说明在节点下方，碰撞左/右图及红色给定Z能分辨，箭头止于节点边；各图底部文字与完整图注分开。

### PGM-PDF-08 - PDF 694 (printed 678) - figures 17.4, 17.5

Observation mode: contact and native detail.

同页的图17.4与17.5各自保留完整图注，中间有解释段。详情中后代D、双圈碰撞点Z、F→H→A←S两种状态的标签与箭头分离；两幅图的底注都没有碰到下一段。

### PGM-PDF-09 - PDF 710 (printed 694) - figures 18.1

Observation mode: contact layout overview.

图18.1的两个团结构并排，图注靠近图底；页右下引用旁注与正文相邻，未覆盖图形。

### PGM-PDF-10 - PDF 712 (printed 696) - figures 18.2, 18.3

Observation mode: contact and native detail.

上部图18.2与下部图18.3均完整。详情中邻居集合标签、远端方形节点、下部两组反例标题及等式可读；图18.3图注与黄色示例框之间保有间距。

### PGM-PDF-11 - PDF 718 (printed 702) - figures 18.4

Observation mode: contact layout overview.

图18.4在正文下半页，分离节点与路径处在同一图块；图注后的小节标题没有被挤进图形内部。

### PGM-PDF-12 - PDF 723 (printed 707) - figures 18.5

Observation mode: contact layout overview.

上部黄色例子框、中部图18.5和下部数值表顺序清楚；图注与表头分开，图表均未伸入外侧空白区。

### PGM-PDF-13 - PDF 728 (printed 712) - figures 18.6

Observation mode: contact layout overview.

图18.6的四节点图和右侧支持配置表并排；其下图注完整，页面右下的文献旁注与图表块分开。

### PGM-PDF-14 - PDF 736 (printed 720) - figures 19.1

Observation mode: contact and native detail.

图19.1四面板的红色A与图注颜色一致，图注/正文衔接没有版面重叠；详情中×在本书页尺度不能清楚辨认（源码L24确有小×），‘补H–S’及‘给定’文本标签未清楚显示，图注与紧接正文却以这些标注引导读者。作为PGM-PDF-F01报告；不宣称源码不存在×。

### PGM-PDF-15 - PDF 737 (printed 721) - figures 19.2

Observation mode: contact and native detail.

图19.2的红色双圈、灰色已删轮廓、虚线填充边与图注对应；各elim标签与步骤图分开，版面完整。详情发现图注宣称上方有‘剩余邻居成团’规则文本，但实际上方只有步骤标题，下面只有elim(4/2/1/3)；作为PGM-PDF-F02报告。

### PGM-PDF-16 - PDF 743 (printed 727) - figures 19.3

Observation mode: contact layout overview.

图19.3三节点抵消例子的图和图注在页中，低位算法框与图块分开；外侧多条引文没有覆盖图底或算法框。

### PGM-PDF-17 - PDF 754 (printed 738) - figures 19.4

Observation mode: contact layout overview.

图19.4两种报警因子图并排，概率因子文本在图底，图注紧随；19.4.3标题另起下方正文块。

### PGM-PDF-18 - PDF 755 (printed 739) - figures 19.5

Observation mode: contact layout overview.

图19.5的分组前后两种因子图位于页上部；图注之后有公式和连续正文，图内连线没有延伸到图注区域。

### PGM-PDF-19 - PDF 762 (printed 746) - figures 20.1

Observation mode: contact and native detail.

图20.1上部F→H→A←S链和三行消元框在正文栏内。详情中每行箭头都从蓝框边连到绿框边，‘消去S/H、归一化F’分别位于对应箭头上方；公式标签未压线，图注后20.2.2标题与正文起排清楚。

### PGM-PDF-20 - PDF 773 (printed 757) - figures 20.2

Observation mode: contact and native detail.

图20.2两组消元图用相同节点尺度，左A及右C用红色强调待消变量，右侧六条补边为红色；对应图注颜色正确。详情中桶作用域/表项数文字没有压线，完整图注与正文分开。

### PGM-PDF-21 - PDF 777 (printed 761) - figures 20.3

Observation mode: contact layout overview.

图20.3星形约束与补边图占页上部，面板之间的转换箭头明确；图注下方的20.4.3标题与正文分开。

### PGM-PDF-22 - PDF 781 (printed 765) - figures 21.1

Observation mode: contact and native detail.

图21.1与上部表21.1均完整。详情中F、H、S、证据A=1与方形因子不重叠；切割虚线、双向消息箭头及u(h)/v(h)标签有各自空间，图注和下方解释段连续。

### PGM-PDF-23 - PDF 786 (printed 770) - figures 21.2

Observation mode: contact layout overview.

图21.2四个阶段用浅色面板分组，面板标题、团框和分隔集位置能分辨；完整图注在统一图块之后，下面的21.2.3标题不碰图注。

### PGM-PDF-24 - PDF 787 (printed 771) - figures 21.3

Observation mode: contact layout overview.

图21.3位于running-intersection定义框之后，两条团链和面板说明分开；图注、正文与后续公式都留在本页。

### PGM-PDF-25 - PDF 790 (printed 774) - figures 21.4

Observation mode: contact and native detail.

图21.4详情中两条蓝色入站箭头与标签、两条绿色双向消息均清楚；分隔集引线不压住消息文字，外层团框与右侧校准框完整。颜色说明和图注对应，下面消息公式有独立正文空间。

### PGM-PDF-26 - PDF 795 (printed 779) - figures 21.5

Observation mode: contact layout overview.

图21.5证据更新团树在页上部，实线/虚线图例在图内下方，图注完整；下方21.5小节及引理框起排整齐。

### PGM-PDF-27 - PDF 802 (printed 786) - figures 22.1

Observation mode: contact and native detail.

图22.1使用页上部全宽，两条查询分支及外层分组边界完整。详情中各列箭头在框间留白中连接，分支边界与蓝/红/绿框文字分开；三行图注同页，正文22.1起排在其后。

### PGM-PDF-28 - PDF 806 (printed 790) - figures 22.2

Observation mode: contact layout overview.

图22.2三个三角结构在页顶并排；各面板底部概率式没有与图注相撞，下面变分式和解释段占独立正文区域。

### PGM-PDF-29 - PDF 816 (printed 800) - figures 22.3

Observation mode: contact layout overview.

图22.3九节点区域图与右侧图例占页上部，图注位于整个图块之后；下面的区域计数与自由能公式未被图遮住。

### PGM-PDF-30 - PDF 828 (printed 812) - figures 22.4

Observation mode: contact layout overview.

图22.4割图位于引文旁注以下，阴影背景、端点和容量标注组成一个紧凑图块；图注之后的小节标题与论述有独立间距。

### PGM-PDF-31 - PDF 835 (printed 819) - figures 23.1

Observation mode: contact and native detail.

图23.1与表23.1都在正文栏内。详情中浅蓝/浅黄两组柱、刻度、图例和横轴状态均可读且分离；图注不碰数值表，页右下引文旁注未压住公式与正文。

### PGM-PDF-32 - PDF 842 (printed 826) - figures 23.2

Observation mode: contact and native detail.

HMC图23.2独占一个完整图页，上部四步流程、回路、接受率框，下部真实曲线与三框流程均在本页。详情中曲线刻度和数值注释可读；实线箭头抵达框边，返回回路避开接受率框，图注三行完整，没有延续到下一页。

### PGM-PDF-33 - PDF 848 (printed 832) - figures 23.3

Observation mode: contact layout overview.

图23.3重采样两列表格的连接线止于各行边界；图注下方23.4.3标题与其余正文未与图块重叠。

### PGM-PDF-34 - PDF 870 (printed 854) - figures 24.1, 24.2

Observation mode: contact and native detail.

图24.1、24.2上下排列，均有完整图注。详情中上图绿实线/蓝虚线、两轮参数点和图例可辨；下图红迭代点/箭头与蓝MLE菱形可辨，末端注释留在曲线上方/下方，没有与图注相撞。

### PGM-PDF-35 - PDF 873 (printed 857) - figures 24.3

Observation mode: contact layout overview.

图24.3三类缺失机制浅色面板并排，虚线和观测指示框处在各自面板中；图注在下方，下一小节标题没有靠进背景色块。

### PGM-PDF-36 - PDF 884 (printed 868) - figures 25.1

Observation mode: contact layout overview.

图25.1三种DAG及底部CPDAG垂直排放，各结构标题单独成行；图注和正文说明留在同页，页侧引文与图块分开。

### PGM-PDF-37 - PDF 895 (printed 879) - figures 25.2

Observation mode: contact layout overview.

图25.2的三节点树和边权、候选边位于页顶，图底解释与图注分开；下面高斯图模型小节没有遮住图注。

### PGM-PDF-38 - PDF 901 (printed 885) - figures 25.3

Observation mode: contact and native detail.

图25.3蓝/黄/红三条背景均完整且与结构顺序一致，图注与正文无重叠。详情中上/中/下概率箭头及框边为蓝/绿/红，故图注‘同色箭头’不能覆盖黄色中行；作为PGM-PDF-F03报告。

### PGM-PDF-39 - PDF 909 (printed 893) - figures 26.1

Observation mode: contact layout overview.

图26.1的朴素贝叶斯与TAN两组分类器在例子/推导之后并排；图注之后的参数式继续留在本页，图和公式没有交叠。

### PGM-PDF-40 - PDF 912 (printed 896) - figures 26.2

Observation mode: contact and native detail.

图26.2处在MADE掩码正文与文献旁注之间。详情中h1/h2圆角框、允许的依赖箭头、q1偏置标签、下方矩阵与右侧禁止箭头都清楚；旁注与图右边留有空隙，图注不碰后面的PixelCNN段。

### PGM-PDF-41 - PDF 923 (printed 907) - figures 26.3

Observation mode: contact and native detail.

图26.3的LDA板结构在正文栏中完整。详情中βk板、文档板、词板及k/g/j重复索引各有位置，外部α/η的箭头准确止于对应节点边；图注在板底下，没有遮住后面的坐标更新公式。

### PGM-PDF-42 - PDF 930 (printed 914) - figures 27.1

Observation mode: contact and native detail.

图27.1详情中三节点联合结构、给定输入的灰底圆角框、虚线特征读入及下方图例分层清楚；图注的灰底框/虚线含义与图对应，图注及下方小节/公式无重叠。

### PGM-PDF-43 - PDF 934 (printed 918) - figures 27.2

Observation mode: contact layout overview.

图27.2的RBM二部图与右侧条件分布示意并排，面板标题及条件式都在图块内；图注与下方的概率计算说明分开。

### PGM-PDF-44 - PDF 936 (printed 920) - figures 27.3

Observation mode: contact and native detail.

图27.3在页上部全宽。详情中条件概率、抽样值、正/负相统计及更新W四层关系可读；链路箭头止于各块边，两个统计分支汇入梯度差的两侧；小字号辅助注释未压住连线，完整三行图注与正文分开。

### PGM-PDF-45 - PDF 944 (printed 928) - figures 27.4

Observation mode: contact layout overview.

图27.4一阶/二阶作用域示意与底部两个Markov框分层排放；图注之后27.3.4标题和条件概率公式留有间距，右侧引文未盖住图底。

### PGM-PDF-46 - PDF 949 (printed 933) - figures 28.1

Observation mode: contact layout overview.

图28.1动态模板在正文下部，时间切片标题和各节点在同一图块；图注仍在本页，底部无裁切。

### PGM-PDF-47 - PDF 961 (printed 945) - figures 28.2

Observation mode: contact and native detail.

图28.2使用页中全宽。详情中五类轨迹的颜色/线型/标记、滤波椭圆、t=0/4/8和图例可辨；标签有白底避免与线重叠，图注与下面状态矩公式分开。 Read-only generator verification confirms labels at filter times 0/4/8 and ellipses at times 2/5/8 are separate objects; caption times are correct.

### PGM-PDF-48 - PDF 962 (printed 946) - figures 28.3

Observation mode: contact and native detail.

图28.3详情中蓝色预测实线、灰色似然虚线和红色后验粗线均可读且与图注一致；完整图注/正文/旁注分开。实际只有红色后验引线，图注‘引线对应各曲线’为未更新宣称；作为PGM-PDF-F04报告。

### PGM-PDF-49 - PDF 964 (printed 948) - figures 28.4

Observation mode: contact layout overview.

图28.4切换状态的三层节点在页中，跨切片虚线控制边处在框图自身范围内；图注后正文继续，无与页脚或旁注重叠。

### PGM-PDF-50 - PDF 972 (printed 956) - figures 29.1

Observation mode: contact and native detail.

图29.1两条VAE流程和底部ELBO框均在正文栏宽内。详情中上部生成方向和下部推断方向分别用实线/虚线，箭头止于框边，ELBO文字未出框；图注与后续高斯/KL公式之间有空隙。

### PGM-PDF-51 - PDF 973 (printed 957) - figures 29.2

Observation mode: contact and native detail.

图29.2在页顶全宽。详情中观测到编码器、均值/尺度、噪声、重参数化、解码器、条件似然及训练目标连线可辨；红虚线参数梯度与前向实线分开，下方独立生成路径完整；图注三行同页且不碰正文。

### PGM-PDF-52 - PDF 978 (printed 962) - figures 29.3

Observation mode: contact and native detail.

图29.3的耦合层在正文栏内。详情中zA直达xA及分支进入子网络、zB到仿射操作再到xB的箭头止于对应框边；子网络虚线抵达操作框上边，Jacobian框文字可读且不出框，图注之后例子与正文继续。

### PGM-PDF-53 - PDF 982 (printed 966) - figures 29.4, 29.5

Observation mode: contact and native detail.

图29.4与29.5同页。详情中上图两排噪声状态字号一致、箭头方向分别向右/向左；下图两行花朵/噪声样本及下标完整，中央方向说明与样本框分开，两幅图注各自完整且未触及页脚。

