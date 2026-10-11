# IND27-F01：r4实际修订后的独立增量复读

2026-10-11，复读者/root/transformer_audit，未参与第27章源编辑。改前source-f41d0d12.tex SHA f41d0d120284718d27e22447226ea32cf6ece4a7fe9d8b566fe0caa440b2645a；改后source-73805e8b-r4.tex SHA 73805e8bd0858cd49e2f027adf58ff77eda592cb7e9efddfe1c1b6acf7c71066。实际root生产源与after-r4.tex和本目录快照逐字相同。

全文差异只在L322/U063，原5句变7句，122文字单元/377句变122/379；36显示数学、2全表、算法、标题、标签、引用、图路径及宽度均没有变化。旧r1独立记录继续绑定f41版，不能把它的F01待修改状态覆盖成旧版通过。

## C增量及全章最终顺读

先连续读L310–331：整组激活数g(kC)→可约/不可约高阶例→factor局部msg计算→重复规则模板→MLN入口。新消息计算按receivernode的激活补齐总组count，仍只改变local计算，不把cost简化扩大成消全图环。之后顺读冻结r4全章L1–306、307–606，两段输出均完整：共同归一化→联合多属性→条件链/片段/一般图→比较与开篇回答，未出现新对象承诺、重复章节或scope改变。

## P增量

U060仍定义kC为C中所有active，U061–062反证original三变量非pairwise，U063 now先汇总otherscount，再按receiver两个状态取g，U064再grounding共享。修订不要求reader猜target值，输出msg也不是归一化概率；U063保localvsglobal环及data/model统计后句，段落中心和前后关系闭合。

## W增量（R4-U063.S01–S07）

|新句地址/短引|白话意思、运算条件和接受依据|
|---|---|
|R4-U063.S01“内部结构”|factor相同阶数也因稠密/count形式有不同localcost，与后句两构造对应。|
|R4-U063.S02“2^r…2^{r−1}”|二值r表，fixedreceiver一态求其余r−1配置；unchanged local指数说明准确。|
|R4-U063.S03“其余节点恰有k”|动态规划汇总target以外count的incomingweight；k不是全Ccount，现单独句明确后续需receiver补齐。|
|R4-U063.S04“未激活…激活…增加一”|xi=-1时total=k，xi=+1时total=k+1，势值分别e^{-g(k)}/e^{-g(k+1)}；和U060激活定义相符，两个conditionaloutput可不同。|
|R4-U063.S05“分别对k求和”|对每固定target状态把各otherscount的权重×对应势相加，得到两个msg；形成c_k convolutionO(r²)加两组O(r)sum，不改阶。|
|R4-U063.S06“只简化本地”|factoroperation变快不消别的因子环；unchanged限制没有扩大图推断保证。|
|R4-U063.S07“统计量…计数”|count/整体一致feature的learning仍empirical−model；计算msg的修订没混targetcondition与训练数据单位。|

映射：旧U063.S01/02→新S01/02；旧S03重新表述为新S03/04/05，旧S04/05→新S06/07。其余121文字单元及显示式/完整表/算法逐字不变，使用原03-W全部对应依据，不伪造重复全章句审。

代数回归：若c_k汇总其余节点incomingproduct，则m_i(-1)=Σc_ke^{-g(k)}，m_i(+1)=Σc_ke^{-g(k+1)}。三节点恰一激活λ惩罚、incoming全1例分别2+2e^{-λ}和1+3e^{-λ}，新正文可直接算出不同输出，不再漏targetcount。新两条件/G6双门槛、W5符号和G7localcost范围均满足。

IND27-F01状态：复读通过，实际r4修订关闭。最终全章顺读未新增科学条件或首次阅读缺口。范围仍不含外部来源完整认证、图源像素和最终PDF。
