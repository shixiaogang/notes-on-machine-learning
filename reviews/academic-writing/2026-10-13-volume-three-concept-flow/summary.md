# 卷三第二轮审读汇总：概念理解与段落串联

审读时间：2026-10-13。范围：卷三《基础、理论与可信性》全部 17 章正文。
审读口径：面向本科理工科读者，检查每个概念是否讲清"为何提出、与之前概念的关系、有无直观理解"，段落与章节之间是否合理串联；不调整章节结构与主要内容，仅增补必要的过渡、直觉、类比与消歧。
第一轮（句子粒度润色，70 处）见 `reviews/academic-writing/2026-10-13-volume-three-prose-polish/`，提交为 `c88637b0`。本轮为其后的第二轮。

## 总体结论

卷三正文的概念链整体完整：各章章首均从具体任务情境提出问题并交代与前后章的分工，术语在引入处均有自足定义，难点概念普遍配有数值例子、对照构造或图示。本轮共 6 处增补（编号按各章记录内的 G 编号），集中在学习理论部分；可信性部分 8 章均无需修改。宁缺毋滥：概念链已完整的章不做为改而改。

## 各章修改一览

| 章 | 文件 | 本轮修改 | 要点 |
| --- | --- | --- | --- |
| 1 引言 | `01-basics/01-introduction.tex` | 4 处 | 哲学→心理学过渡句；归纳偏置呼应休谟；过拟合／欠拟合补容量—数据直觉；期望风险呼应泛化 |
| 2 模型简介 | `01-basics/02-machine-learning-models.tex` | 1 处 | 激活函数例子补规范名"整流线性单元（ReLU）" |
| 3 范式简介 | `01-basics/03-learning-paradigms.tex` | 0 处 | 概念链完整 |
| 4 统计学习框架 | `02-learning-theory/01-statistical-learning-framework.tex` | 2 处 | PAC 名称拆解（"近似正确"=ε、"概率"=1−δ）；NFL 名称含义 |
| 5 二分类 | `02-learning-theory/02-binary-classification.tex` | 2 处 | VC 维本卷自足表述；Rademacher 随机符号≈随机标签直觉 |
| 6 多分类 | `02-learning-theory/03-multiclass-classification.tex` | 1 处 | 图打散定义处消歧"图指函数图像，非节点边图" |
| 7 凸学习与稳定性 | `02-learning-theory/04-convex-learning-and-stability.tex` | 0 处 | 概念链完整 |
| 8 深度学习理论 | `02-learning-theory/05-deep-learning-theory.tex` | 0 处 | 四个分析入口的动机、分工与边界齐备；"切线"已有切空间锚点 |
| 9 迁移学习理论 | `02-learning-theory/06-transfer-learning-theory.tex` | 1 处 | $\mathcal H\triangle\mathcal H$ 散度补记号来源（对称差） |
| 10 可信性基础 | `03-trustworthiness/01-foundations.tex` | 0 处 | 部分间转折与三层次结构清晰 |
| 11 可靠性 | `03-trustworthiness/02-reliability.tex` | 0 处 | "估计—检验—保证"链条完整 |
| 12 鲁棒性 | `03-trustworthiness/03-robustness.tex` | 0 处 | 与第 9 章理论、第 17 章安全的分工明确 |
| 13 公平性 | `03-trustworthiness/04-fairness.tex` | 0 处 | 五类判定分支的对象、准则、证据与边界齐备 |
| 14 对齐 | `03-trustworthiness/05-alignment.tex` | 0 处 | 代理偏离动机与监督边界明确 |
| 15 可解释性 | `03-trustworthiness/06-interpretability.tex` | 0 处 | 目的—方法—质量—补救四层完整 |
| 16 隐私 | `03-trustworthiness/07-privacy.tex` | 0 处 | 秘密—单位—渠道—承诺—验证—实现—撤回链条完整 |
| 17 对抗安全 | `03-trustworthiness/08-adversarial-security.tex` | 0 处 | 攻击—评估—防御均按"位置—条件—证据"组织 |

各章详细评估与未动项理由见同目录 `v3-c01-concept.md` 至 `v3-c17-concept.md`。

## 修改原则回顾

- 术语 `\term{}` 只在正式定义处使用；跨卷引用不加 `\term`（如 VC 维定义在卷一，整流线性单元在卷五）。
- 增补均为表述层面：一句过渡、半句直觉或一处消歧，不动章节结构、定理内容与证明。
- 每处修改均经 `git diff` 复核；构建与提交检查见交付说明。
