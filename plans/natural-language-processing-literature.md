# 自然语言处理研究文献地图（2017—2026）

## 检索范围与材料用途

检索截止日期为2026年10月5日，主要考察2017—2026年这十个发表年度的研究。材料包括ACL、NAACL、EMNLP、TACL、COLING、LREC、SemEval及相关共享任务，以及直接涉及语言任务的AAAI、ICLR、NeurIPS、ICML、CVPR、Interspeech工作。原始论文、正式出版页、作者预印本和官方基准优先；不采用排行榜或二手介绍替代任务定义。

检索先用会议研究主题检查领域边界，再按任务族查找提出任务、改变输入输出条件、建立基准、分析评价或提供有代表性实现的论文。早期、中期和近期工作都保留，避免仅用最近的语言模型论文反推全部NLP内容。模型或方法论文只在帮助说明任务实现时入选，章节仍由任务目标决定。

本次核验题名、年份、发布状态、一手链接，以及摘要和公开任务说明所支持的研究问题。表中“大纲用途”是本书的组织判断。这里不报告性能排名、数值优势或一般有效性；正式写作时，针对所选实现继续核读论文方法、实验和评价设置。此地图是教材规划的代表性样本，不是穷尽检索或发表数量统计；2026年预印本按其公开状态标明。

配套的[部分大纲](natural-language-processing-outline.md)据此按“文本分析—文本处理与应用”组织8章，相近子任务在章内比较。第3章主讲抽取，第4章主讲分类、匹配与组织，第8章只保留语音任务；视觉、页面、视频及音画联合证据转交后续图像部分。文献地图保留较细的研究问题供选材，不把每条任务线都安排为独立章节。论文数量不决定篇幅，一个任务也不会因使用生成模型而改变其正确性要求。

## 会议主题对覆盖范围的约束

| 一手入口 | 可用于本次规划的依据 | 组织时的取舍 |
| --- | --- | --- |
| [ACL 2017研究主题](https://acl2017.org/calls/papers/) | 语言结构、篇章、分类与文档组织、抽取、生成、翻译、对话、语音及多语等方向已有明确入口。 | 保留这些任务的输出和实现，不能将整个领域压缩为语言模型及问答。 |
| [ACL 2026主会研究主题](https://2026.aclweb.org/calls/main_conference_papers/) | 除持续存在的语言任务外，还列出代码、语言智能体、人机协作、检索增强、推理和多模态等议题。 | 将可执行程序、环境任务与人机交互纳入本部分，视觉与音画联合证据转交图像部分；架构、效率和通用学习方法回指前卷。 |
| [ARR研究领域与关键词](https://aclrollingreview.org/areas) | 同一工作可以同时涉及任务、语言条件、方法与评价，领域关键词并非互斥目录。 | 以任务确定主讲位置，多语、低资源、领域和长上下文作为交叉条件，相关章节只补新增约束。 |

认知建模、语言理论、通用训练和模型解释属于NLP研究范围，但本部分是机器学习书籍的应用部分。语言现象保留到能帮助定义任务和理解错误的深度；通用模型分析、可信性与系统研究交由全书相应部分承担。医疗、法律、金融、教育和社会分析主要在任务中呈现领域约束，避免另设重复全部任务的应用杂项章。

## 从研究样本提炼的问题地图

下表归纳代表研究暴露的任务问题，并不声称所有研究沿同一时间线演进。不同任务持续存在，输入条件、输出范围、实现方法和证据要求可以分别变化。

| 任务线 | 需要在正文回答的研究问题 | 代表材料 | 对应章节 |
| --- | --- | --- | --- |
| 局部语言分析与实体提及 | 语言单位差异、标签结构和稀有或未见实体怎样影响位置与类别预测？ | UD v2、Few-NERD | 第2章讲词法与句法，第3章讲实体识别 |
| 句法与语义结构 | 怎样预测合法树、谓词论元和语义图；输出结构何时能支持后续计算？ | 成分解析、SRL、SPRING | 第2章 |
| 语义解析与数据库接口 | 怎样关联模式、理解未见数据库并处理复杂查询和工作流程？ | Spider、SParC、CoSQL、Spider 2.0 | 第2章，并连接第6、7章 |
| 篇章与指代 | 怎样连接跨句提及、分割篇章单元并判断显式或隐式关系？ | 端到端共指、DISRPT | 第2章 |
| 事实与事件抽取 | 怎样从局部触发词走向文档级论元、证据及事件间关系；生成记录怎样保持原文依据？ | DocRED、MAVEN、WikiEvents、MAVEN-ERE、EventRelBench | 第3章 |
| 分类、情感与立场 | 怎样区分文本类别、评价对象、情绪和目标立场；未见目标与混合编辑怎样改变标签？ | SemEval情感、Bi-STANCE、CLUE、Creator-Editor检测 | 第4章 |
| 语义关系 | 词汇相似时怎样识别语序、否定和角色差异；关系判定能否跨体裁、语言和困难实例？ | STS、MultiNLI、PAWS、ANLI、XNLI | 第4章 |
| 生成与编辑 | 怎样在改写、纠错、简化和结构化数据表达中规定允许变化？ | JFLEG、ASSET、WebNLG | 第5章 |
| 摘要与信息综合 | 高压缩、长文本和多来源条件下怎样选择内容、保持事实并检查来源？ | XSum、SummEval、FActScore | 第5章 |
| 翻译 | 怎样处理低资源方向、篇章连贯、专业术语及实时输出；评价怎样反映实际错误？ | NLLB、WMT24、MQM评价、STACL、DiscoX | 第5章 |
| 问答与核验 | 怎样找到多处证据、识别无答案、判断主张及核对长回答中的事实？ | SQuAD 2.0、HotpotQA、FEVER、RAG、FActScore | 第6章 |
| 多轮对话 | 怎样保持需求状态、接入未见服务、结合知识并与用户协作？ | MultiWOZ、SGD、Persona-Chat、Wizard of Wikipedia、τ系列 | 第6章 |
| 程序与行动 | 怎样从短函数生成扩展到代码库修改和网页任务；答案、测试与环境结果各证明什么？ | HumanEval、SWE-bench、GSM8K、ToT、ReAct、WebArena | 第7章 |
| 语音与实时交互 | 怎样追踪识别、理解、翻译和合成的误差；轮次、打断和延迟怎样进入评价？ | Tacotron 2、CoVoST 2、Whisper、SeamlessM4T、Moshi、τ-Voice | 第8章 |
| 图文、文档与视频 | 怎样使用真实的视觉、版面和时序证据；如何发现问题或字幕捷径？ | VQA v2、TextVQA、DocVQA、OmniDocBench、Video-MME-v2 | 图像大纲“多模态理解”章 |
| 跨任务评价 | 自动指标、行为测试、人工偏好和模型评审怎样对应任务；多语和文化条件怎样控制？ | BERTScore、CheckList、Dynabench、HELM、MT-Bench、XTREME、Belebele、Global MMLU | 第1章及各任务章 |

2017—2019年的入选样本提供句对关系、共指、文档抽取、摘要、问答和对话等任务入口；2020—2022年的样本补充细粒度、文档级、多语言、数据构造和评价问题；2023—2026年的样本进一步检查事实归因、程序与环境执行、用户协作和实时交流，视觉多模态材料转交图像部分。这些分段只描述本次选材的解释职责，不表示新阶段使既有任务失去价值。

## 代表文献

表中编号供选材追溯，正式书稿使用统一BibTeX。正式发表年与预印本首发年不同时分列；未核实正式发表信息的条目标为预印本。研究问题与纳入理由限于规划所需范围。

### 语言分析、文本理解与抽取

| 编号 | 任务／问题 | 论文、年份与出处 | 大纲用途与边界 |
| --- | --- | --- | --- |
| N001 | 中文文本分类与句对理解 | Xu等，2020，COLING：[CLUE: A Chinese Language Understanding Evaluation Benchmark](https://aclanthology.org/2020.coling-main.419/) | 为中文分类、句对任务和阅读理解提供共同入口。大纲应保留单文本／句对、文本长度和中文语言现象的区别；不能用一个综合分数代替任务定义和逐任务评价。 |
| N002 | 情感分析的目标与输出粒度 | Rosenthal等，2017，SemEval：[SemEval-2017 Task 4: Sentiment Analysis in Twitter](https://aclanthology.org/S17-2088/) | 区分整条文本的情感、针对某个目标的情感，以及语料级情感分布估计。适合说明二分类、序数等级与总体估计是不同输出；应另补方面／观点目标与意见持有者。 |
| N003 | 立场判断与中英文条件 | Zhao与Caragea，2025，ACL：[Bilingual Zero-Shot Stance Detection](https://aclanthology.org/2025.acl-long.1446/) | 支持立场作为独立任务：文本对某个目标或主张赞成、反对或中立。研究使用Bi-STANCE，区分单语、跨语言、双语、未见目标和跨领域条件；文本情感正负不能自动推出立场。 |
| N004 | 从语料发现主题 | Bianchi等，2021，ACL-IJCNLP：[Pre-training is a Hot Topic: Contextualized Document Embeddings Improve Topic Coherence](https://aclanthology.org/2021.acl-short.96/) | 用主题连贯性和主题多样性说明发现主题的目标与解释问题；简述上下文表示如何支持主题发现，通用模型推导回指模型卷。2020年预印本，正式发表为2021年。 |
| N005 | 语义相似度 | Cer等，2017，SemEval：[SemEval-2017 Task 1: Semantic Textual Similarity Multilingual and Crosslingual Focused Evaluation](https://aclanthology.org/S17-2001/) | 支持相似度为连续判断、多语言／跨语言可为评价条件。用于区别语义相似、同义复述、主题相关和证据支持，避免统一当成“文本匹配”。 |
| N006 | 自然语言推断及跨体裁评价 | Williams等，2018，NAACL：[A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference](https://aclanthology.org/N18-1101/) | MultiNLI支持前提—假设及蕴含／矛盾／中立三种语义关系；比较体裁匹配和不匹配测试。2017年预印本，正式发表为2018年；NLI不是证明任意真实世界命题。 |
| N007 | 高词汇重叠下的复述判断 | Zhang等，2019，NAACL：[PAWS: Paraphrase Adversaries from Word Scrambling](https://aclanthology.org/N19-1131/) | 展示词汇几乎相同仍可能因语序和角色变化而不等义，适合用“纽约到佛罗里达／佛罗里达到纽约”类例子连接句法与句对理解。不把相似词袋视为语义等价。 |
| N008 | NLI中的困难实例与评价捷径 | Nie等，2020，ACL：[Adversarial NLI: A New Benchmark for Natural Language Understanding](https://aclanthology.org/2020.acl-main.441/) | 人与模型迭代构建ANLI，适合说明训练捷径、对抗收集与静态基准局限。这里解释任务证据；标注采集方法的一般机制可回指知识获取。 |
| N009 | 少样本与细粒度实体识别 | Ding等，2021，ACL-IJCNLP：[Few-NERD: A Few-shot Named Entity Recognition Dataset](https://aclanthology.org/2021.acl-long.248/) | 用层级实体类型和未见细类说明NER既要确定边界也要确定类型；少样本是数据条件。应同时保留平面／嵌套／不连续实体、领域实体与新类型识别，不把BIO标注当成全部NER问题。 |
| N010 | 词法与依存句法的跨语言标注 | Nivre等，2020，LREC：[Universal Dependencies v2: An Evergrowing Multilingual Treebank Collection](https://aclanthology.org/2020.lrec-1.497/) | UD包含语言单位划分、词性、词形与依存关系，可支撑词法—句法的连续解释和多语言边界。依存分析与成分分析需分别定义；共享标注不意味着各语言结构相同。 |
| N011 | 语义角色标注 | He等，2018，ACL：[Jointly Predicting Predicates and Arguments in Neural Semantic Role Labeling](https://aclanthology.org/P18-2058/) | 区分已给定谓词的角色标注与同时预测谓词、论元跨度和角色。用“谁对谁做什么、在何时何地”建立直觉，再说明SRL的词汇／框架角色与事件抽取的任务本体并不相同。 |
| N012 | 跨数据库的语义解析 | Yu等，2018，EMNLP：[Spider: A Large-Scale Human-Labeled Dataset for Complex and Cross-Domain Semantic Parsing and Text-to-SQL Task](https://aclanthology.org/D18-1425/) | 支持自然语言—结构化查询的映射、schema linking、未见数据库与组合查询泛化。查询文本匹配、执行结果和数据库条件要分开；Text-to-SQL只是一类语义解析。 |
| N013 | 从单条查询到实际数据库工作流程 | Lei等，2025，ICLR：[Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows](https://proceedings.iclr.cc/paper_files/paper/2025/hash/46c10f6c8ea5aa6f267bcdabcb123f97-Abstract-Conference.html) | 2024年预印本，正式发表为2025年。支持复杂数据库元信息、方言、多步查询、文档和代码环境的语义理解；基础映射讲在语义解析，执行闭环及环境交互连接对话／工具应用，系统实现回指系统卷。 |
| N014 | 文档级关系抽取 | Yao等，2019，ACL：[DocRED: A Large-Scale Document-Level Relation Extraction Dataset](https://aclanthology.org/P19-1074/) | 跨句综合实体、共指与证据判断关系，支持从句内到文档级抽取。区别实体边界、实体身份、实体对关系、证据定位；人工数据与远程监督数据不可混为同一评价依据。 |
| N015 | 事件检测 | Wang等，2020，EMNLP：[MAVEN: A Massive General Domain Event Detection Dataset](https://aclanthology.org/2020.emnlp-main.129/) | 支持触发词和事件类型、一般领域的类型覆盖与数据不均衡问题。事件检测先确定提及何种事件，完整事件抽取还需论元及角色，不能只列“事件分类”便称为覆盖整个事件任务。 |
| N016 | 文档级事件论元抽取 | Li等，2021，NAACL：[Document-Level Event Argument Extraction by Conditional Generation](https://aclanthology.org/2021.naacl-main.69/) | 原论文提出WikiEvents，展示跨句、隐含共指和信息充分的论元表达；条件生成可作为抽取方法简述。任务仍受原文证据与事件模式约束，不能因为使用生成就改归自由文本生成。 |
| N017 | 事件之间的关系 | Wang等，2022，EMNLP：[MAVEN-ERE: A Unified Large-scale Dataset for Event Coreference, Temporal, Causal, and Subevent Relation Extraction](https://aclanthology.org/2022.emnlp-main.60/) | 为事件共指、时间、因果和子事件关系提供统一任务依据。建议将时间表达识别／归一化、事件排序和不同事件关系分层安排；时间先后并不自动等于因果。 |
| N018 | 事件关系理解在生成模型时代的评价 | Gong等，2025，Findings EMNLP：[EventRelBench: A Comprehensive Benchmark for Evaluating Event Relation Understanding in Large Language Models](https://aclanthology.org/2025.findings-emnlp.482/) | 句级／文档级问题覆盖事件共指、时间、因果、子事件组成关系，支持把模型适配放回既有任务框架。多项选择式关系判断与端到端定位全部事件关系需要分别评价，不能用前者替代后者。 |
| N019 | 实体共指消解 | Lee等，2017，EMNLP：[End-to-end Neural Coreference Resolution](https://aclanthology.org/D17-1018/) | 以文档候选跨度和先行词关系说明提及检测与实体聚类怎样相连，方法只概述任务接口。需要区别指代消解、共指聚类、实体链接；中文应补零指代，篇章应补桥接与话语指示。 |
| N020 | 篇章单元及篇章关系 | Braud等，2023，DISRPT：[The DISRPT 2023 Shared Task on Elementary Discourse Unit Segmentation, Connective Detection, and Relation Classification](https://aclanthology.org/2023.disrpt-1.1/) | 明确篇章分析至少包含单元分割、连接词检测和关系判断；比较不同语言、体裁和标注体系。显式连接词与隐式关系需要分别处理，不把篇章关系归约成句子相似度。 |

### 文本转换、证据回答与交互

| 编号 | 论文及一手来源 | 年份与类型 | 任务问题 | 大纲用途 |
| --- | --- | --- | --- | --- |
| N021 | Napoles、Sakaguchi与Tetreault：[JFLEG: A Fluency Corpus and Benchmark for Grammatical Error Correction](https://aclanthology.org/E17-2037/) | 2017，任务/基准 | 语法纠错能否同时改善整体流畅度，而不只作最小局部修改；提供原句与多个人工修订。 | 在“文本生成与转换”中保留纠错、流畅性改写和语义保持，区分最小修改与整体重写；英文数据不能直接代表中文纠错。 |
| N022 | Narayan、Cohen与Lapata：[Don’t Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization](https://aclanthology.org/D18-1206/) | 2018，混合 | 通过单句新闻摘要任务与XSum数据，要求系统概括文章中心，而非主要复制原文句子。 | 用于区分抽取式、生成式与极短摘要，并解释压缩率、信息选择和忠实性；卷积方法只作代表路线简述。 |
| N023 | Alva-Manchego等：[ASSET: A Dataset for Tuning and Evaluation of Sentence Simplification Models with Multiple Rewriting Transformations](https://aclanthology.org/2020.acl-main.424/) | 2020，任务/基准 | 简化往往同时涉及词语替换、拆句、重排与删减，单一变换的数据不能充分检验真实简化。 | 将文本简化列为独立子任务，说明多参考答案、简洁性、可读性与原意保留之间的关系。 |
| N024 | Fabbri等：[SummEval: Re-evaluating Summarization Evaluation](https://aclanthology.org/2021.tacl-1.24/) | 2021，评价；预印本2020 | 摘要评价缺少一致流程，需要在共同系统输出上比较自动指标与专家、众包判断。 | 摘要章保留多维质量与人工评价；第1章说明指标相关性、评价者与实验口径，不能把ROUGE当作质量的全部。 |
| N025 | Min等：[FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://aclanthology.org/2023.emnlp-main.741/) | 2023，评价 | 一段长文本可能混合有依据与无依据的陈述；将文本拆成原子事实，计算可靠知识源支持的比例。 | 长文本生成与问答均需讨论事实核验、证据支持与细粒度错误；明确它度量事实精确性，不能单独评价完整性、信息量或总体回答质量。 |
| N026 | Freitag等：[Experts, Errors, and Context: A Large-Scale Study of Human Evaluation for Machine Translation](https://aclanthology.org/2021.tacl-1.87/) | 2021，评价 | 高质量译文的人工评价需要明确错误分类、专业评价者与完整文档上下文；比较MQM式错误分析和既有评价结果。 | “翻译质量与错误分析”保留语义准确性、流畅度、术语和上下文；不能只讲句级BLEU，评价者和上下文是实质条件。 |
| N027 | NLLB Team等：[No Language Left Behind: Scaling Human-Centered Machine Translation](https://arxiv.org/abs/2207.04672) | 2022，方法及数据/评价混合 | 大量低资源语言缺少平行数据和高质量翻译支持；通过数据挖掘、多语方法与FLORES-200等评价资源处理语言覆盖问题。 | 低资源、多语、直接翻译与语言覆盖在第5章5.5节明确展开；模型结构简述后回指模型卷，不把NLLB单列成章节，也不把其报告结果写成所有低资源条件下的保证。 |
| N028 | Kocmi等：[Findings of the WMT24 General Machine Translation Shared Task: The LLM Era Is Here but MT Is Not Solved Yet](https://aclanthology.org/2024.wmt-1.1/) | 2024，任务/基准与评价 | 在多个语言对和领域中，比较参赛系统、语言模型及在线服务，并使用专业人工错误标注。 | 近年语言模型仍应在共同翻译任务中与专用系统比较；大纲需覆盖跨域、文体、复杂语言现象和错误类型，不按模型版本排章节。 |
| N029 | Rajpurkar、Jia与Liang：[Know What You Don’t Know: Unanswerable Questions for SQuAD](https://aclanthology.org/P18-2124/) | 2018，任务/基准 | 阅读理解系统不能只定位答案，还必须识别段落不支持回答的情况；引入人工对抗构造的不可回答问题。 | “可回答性与澄清/拒答”必须保留；明确无答案是相对于给定证据而言，不能直接等同于模型不知道或世界上没有答案。 |
| N030 | Yang等：[HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering](https://aclanthology.org/D18-1259/) | 2018，任务/基准 | 需要综合多个支持文档并给出句级支持事实，也包括事实比较问题。 | 阅读理解之外保留多文档、多跳问答与证据定位；答案正确率和支持事实质量分别评价，不把生成推理文字等同于正确证据链。 |
| N031 | Thorne等：[FEVER: a Large-scale Dataset for Fact Extraction and VERification](https://aclanthology.org/N18-1074/) | 2018，任务/基准 | 依据文本证据判断陈述受到支持、被反驳或信息不足，并检索相应证据。 | 事实核验不是一般情感/主题分类，应放在证据驱动的理解任务中；区分证据不足与陈述为假，并讨论来源可靠性和证据时效。 |
| N032 | Lewis等：[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | 2020，方法 | 仅依靠参数知识难以灵活访问、更新知识并说明来源；将检索到的外部文本与生成结合。 | 在第6章“资料集合中的检索与阅读”小节完整展开检索—阅读—生成与证据归因；通用检索理论回指“推荐与搜索”，检索索引与服务实现回指系统卷。不能据此宣称RAG自动保证真实。 |
| N033 | Budzianowski等：[MultiWOZ - A Large-Scale Multi-Domain Wizard-of-Oz Dataset for Task-Oriented Dialogue Modelling](https://aclanthology.org/D18-1547/) | 2018，任务/基准 | 多领域任务型对话需要同时处理用户约束、状态追踪、对话行为和响应生成。 | 任务型对话应沿意图/槽位—状态—策略—响应展开，明确多轮任务完成与单轮回复生成的区别；数据版本与标注修正不能混用。 |
| N034 | Rastogi等：[Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset](https://ojs.aaai.org/index.php/AAAI/article/view/6394) | 2020，混合；预印本2019 | 服务和API不断增加、接口不同且部分缺少训练数据，静态单一领域本体不能充分表示这些条件；使用服务模式描述来定义意图、槽位和状态。 | 保留多领域、服务模式和未见接口的对话任务；语言理解与工具接口应连接，但通用迁移原理回指范式卷。 |
| N035 | Cobbe等：[Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168) | 2021，混合 | 引入GSM8K以研究多步数学应用题，并比较候选解生成与正确性验证。 | 保留自然语言数学/逻辑问题求解、最终答案与过程检查；验证器作为简述方法，不把自然语言推理链直接认作证明。 |
| N036 | Chen等：[Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374) | 2021，混合 | 从自然语言文档字符串生成程序，并用HumanEval执行测试评价功能正确性。 | 语言到程序与可执行输出可作独立节；解释执行与测试证据、重复采样和pass@k。它同时是模型论文，本书只简述模型路线。 |
| N037 | Yao等：[ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | ICLR 2023，方法；预印本2022 | 将推理文字、行动和环境反馈交替组织，使系统获取外部信息、更新计划并处理异常。 | 用于简述语言Agent的一条代表流程；章节仍以指令理解、工具任务、规划执行、反馈与成功评价组织，不按ReAct等框架名分类。 |
| N038 | Zhou等：[WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) | ICLR 2024，任务/基准；预印本2023 | 在可复现的完整网页环境中完成长程自然语言任务，以结果功能正确性而非单一路径匹配评价。 | 保留信息搜集、导航、内容/配置操作及长程任务；解释状态、观察、行动与目标验证，区分轨迹看似合理与任务确实完成。 |
| N039 | Jimenez等：[SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) | ICLR 2024，任务/基准；预印本2023 | 根据真实问题描述理解既有代码库并修改多个关联位置，解决真实软件问题。 | 程序任务不能只包括短函数生成，还应保留代码理解、定位与修改；作为扩展任务简述，避免把NLP部分变成软件工程教材。 |
| N040 | Barres等：[τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment](https://arxiv.org/abs/2506.07982) | 2025预印本，任务/基准 | 客服/技术支持中用户也会修改共同环境；Agent必须既作推理与操作，又清楚指导用户行动。 | 对话与Agent的连接点应包含用户配合、信息澄清、共享状态和行动协调；最终成功与交流/协调错误分别分析。 |

### 多语、语音与共性评价（含视觉任务移交索引）

| 编号 | 论文与年份 | 任务问题 | 大纲用途 |
| --- | --- | --- | --- |
| N041 | [Making the v in VQA Matter: Elevating the Role of Image Understanding in Visual Question Answering](https://openaccess.thecvf.com/content_cvpr_2017/html/Goyal_Making_the_v_CVPR_2017_paper.html)，CVPR 2017 | 视觉问答怎样避免仅凭问题中的语言先验猜答案；用互补图片改变同一问题的答案来减轻偏差。 | **转交图像大纲“多模态理解”章**；本表保留移交索引。图文问答：图像证据的作用；评价：反事实输入、语言捷径和证据依赖检查。 |
| N042 | [XNLI: Evaluating Cross-lingual Sentence Representations](https://aclanthology.org/D18-1269/)，EMNLP 2018 | 只有一种语言的任务训练数据时，怎样在其他语言完成句子理解；构造多语自然语言推断评价。 | 文本关系判断：跨语言自然语言推断；多语实现比较：翻译测试数据、平行语料对齐、共享表示。 |
| N043 | [Natural TTS Synthesis by Conditioning WaveNet on Mel Spectrogram Predictions](https://arxiv.org/abs/1712.05884)，ICASSP 2018；预印本 2017 | 怎样从文本生成可听懂且自然的语音；先预测梅尔频谱，再以声码器生成波形。 | 语音合成：文本规范化、发音和声学输出；方法只讲文本到声学序列与波形的任务分工，网络结构回指模型卷。 |
| N044 | [Towards VQA Models That Can Read](https://openaccess.thecvf.com/content_CVPR_2019/html/Singh_Towards_VQA_Models_That_Can_Read_CVPR_2019_paper.html)，CVPR 2019 | 图片问题的答案可能来自图片中的文字；怎样结合识字、视觉内容和语言问题读出、推断或复制答案。 | **转交图像大纲“多模态理解”章**；本表保留移交索引。图文理解：场景文字问答；文档理解：OCR 结果与视觉输入如何组成证据。 |
| N045 | [Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://aclanthology.org/2020.acl-main.442/)，ACL 2020 | 留出集准确率怎样补充为按语言能力组织的行为测试；利用最小功能测试、不变性和方向变化等测试方式发现错误。 | 共同评价（第1章）：否定、实体替换、语序和共指等诊断；每个任务章可配置少量针对本任务的测试案例。 |
| N046 | [DocVQA: A Dataset for VQA on Document Images](https://openaccess.thecvf.com/content/WACV2021/html/Mathew_DocVQA_A_Dataset_for_VQA_on_Document_Images_WACV_2021_paper.html)，WACV 2021 | 文档问答怎样利用版面、栏目和内容关系；纯文字阅读理解基线与视觉问答基线各有什么缺口。 | **转交图像大纲“多模态理解”章**；本表保留移交索引。文档理解：页面问答、位置和结构线索；抽取式问答与生成式问答的文档条件。 |
| N047 | [CoVoST 2 and Massively Multilingual Speech Translation](https://www.isca-archive.org/interspeech_2021/wang21s_interspeech.html)，Interspeech 2021；预印本 2020 | 怎样研究多语、低资源语音翻译；以多语言语音—译文语料比较识别、文本翻译及语音翻译。 | 语音翻译：级联与直接路径、跨语监督和错误传递；正文引用正式标题，避免与预印本标题末尾的 “Speech-to-Text Translation” 混写。 |
| N048 | [Robust Speech Recognition via Large-Scale Weak Supervision](https://proceedings.mlr.press/v202/radford23a.html)，ICML 2023；预印本 2022 | 怎样利用大量网络音频及转录监督研究跨数据集、多语言的语音识别泛化。 | 语音识别：训练证据与真实输入差异，跨口音和背景噪声的评价；弱监督一般机制回指知识获取。 |
| N049 | [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110)，TMLR 2023；预印本 2022 | 怎样在统一条件下比较多种语言应用场景，记录准确性及校准、鲁棒性等不同要求，公开提示和输出供复查。 | 共同评价（第1章）：任务集合、统一实验条件、多指标与可复核记录；一般可信性方法回指前文。 |
| N050 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://papers.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html)，NeurIPS 2023 | 开放式多轮回答怎样评价；模型评审怎样与人工偏好对照，又会受到位置、冗长和自我偏好影响。 | 对话：多轮评价；共同评价（第1章）：人工偏好与事实正确分开、评审偏差、交换顺序与人工抽查。 |
| N051 | [SeamlessM4T: Massively Multilingual & Multimodal Machine Translation](https://arxiv.org/abs/2308.11596)，2023，预印本 | 语音和文本输入、语音和文本输出的翻译任务怎样统一；比较直接实现与级联实现，并研究噪声、说话人变化及翻译附加风险。 | 语音翻译：跨模态语言转换、识别—翻译—合成的分工；多语综合：同一模型支持多任务仍要分别验收。 |
| N052 | [The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants](https://aclanthology.org/2024.acl-long.44/)，ACL 2024；预印本 2023 | 怎样用平行篇章和问题比较不同语言变体的阅读理解能力，覆盖高、中、低资源条件。 | 阅读理解与问答：多语言段落问答；评价：相同内容跨语言对照，并说明平行翻译评价的边界。 |
| N053 | [Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation](https://aclanthology.org/2025.acl-long.919/)，ACL 2025；预印本 2024 | 把英文题目翻译成多语后，怎样识别翻译偏差与原题的文化地域假设；以改进翻译和标注区分文化条件。 | 多语综合：语言理解与文化知识分开；评价：目标用户、原生语言题目和翻译题目的适用性。 |
| N054 | [OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations](https://openaccess.thecvf.com/content/CVPR2025/html/Ouyang_OmniDocBench_Benchmarking_Diverse_PDF_Document_Parsing_with_Comprehensive_Annotations_CVPR_2025_paper.html)，CVPR 2025；预印本 2024 | 多种真实 PDF 如何完整解析；用层级和属性标注分别评价流水线与端到端视觉语言方法，避免只看简单页面上的文字。 | **转交图像大纲“多模态理解”章**；本表保留移交索引。文档理解：阅读顺序、表格、公式、版面及结构化内容；评价：解析模块表现和下游问答表现同时检查。 |
| N055 | [Video-MME-v2: Towards the Next Stage in Benchmarks for Comprehensive Video Understanding](https://arxiv.org/abs/2604.05015v1)，2026-04-06，预印本 | 视频理解怎样覆盖多处视觉信息汇集、时序变化和多模态推理；用关联问题的成组评价检查一致性，并分析字幕线索依赖。 | **转交图像大纲“多模态理解”章**；本表保留移交索引。视频语言任务：时间证据定位、跨片段问答；评价：单题答对与一组相关回答一致的差别。仅标记为近期研究问题，不把来源对自身权威性的宣称写成教材判断。 |
| N056 | [XTREME: A Massively Multilingual Multi-task Benchmark for Evaluating Cross-lingual Generalisation](https://proceedings.mlr.press/v119/hu20b.html)，ICML 2020 | 将分类、结构标注和句子检索置于跨语言多任务评价中，比较跨语言泛化。 | 第1至4章：语言条件横跨不同输出任务，保留逐语言和逐任务结果。 |
| N057 | [Moshi: a speech-text foundation model for real-time dialogue](https://arxiv.org/abs/2410.00037)，2024，预印本 | 将实时双向口语对话作为任务入口，涉及声音与文本以及交流时间条件。 | 第8章：全双工、交叠发言和响应时延；架构只回顾语言任务所需接口。 |

### 近期任务细化与补充实现

| 编号 | 论文与年份 | 任务问题 | 大纲用途 |
| --- | --- | --- | --- |
| N058 | Shi等：[τ-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge](https://arxiv.org/abs/2603.04370)，2026，预印本 | 将非结构化知识使用纳入客服智能体评价，连接证据获取、多轮交流与行动。 | 第6、7章：分别检验知识使用和环境任务，不把检索与执行完全割裂。 |
| N059 | Ray等：[τ-Voice: Benchmarking Full-Duplex Voice Agents on Real-World Domains](https://arxiv.org/abs/2603.13686)，2026，预印本 | 把实时双向语音交互放到领域任务中，检查交流与任务完成。 | 第6、7、8章：声音、轮次、打断与行动结果应分别进入完整交互评价。 |
| N060 | Kitaev与Klein：[Constituency Parsing with a Self-Attentive Encoder](https://aclanthology.org/P18-1249/)，ACL 2018 | 为成分句法解析研究句子编码和表示对结构预测的作用。 | 第2章：以成分树和解析过程为任务入口，编码器变化只作实现比较，不重写注意力。 |
| N061 | Bevilacqua等：[One SPRING to Rule Them Both: Symmetric AMR Semantic Parsing and Generation without a Complex Pipeline](https://ojs.aaai.org/index.php/AAAI/article/view/17489)，AAAI 2021 | 将文本到AMR语义图与语义图到文本作为两个相对应的转换任务。 | 第2、5章：解释图线性化、生成与图恢复的接口；语义图与句法树分别定义。 |
| N062 | Kiela等：[Dynabench: Rethinking Benchmarking in NLP](https://aclanthology.org/2021.naacl-main.324/)，NAACL 2021 | 利用人与模型参与的数据构造形成动态挑战测试，研究静态基准之外的错误。 | 第1章：动态评测与行为测试相互补充，数据采集的通用机制回指知识获取。 |
| N063 | Zhang等：[BERTScore: Evaluating Text Generation with BERT](https://arxiv.org/abs/1904.09675)，ICLR 2020；预印本2019 | 用上下文表示比较生成文本和参考文本中的词元，以补充表面重合指标。 | 第1、5章：语义相似是评价证据之一，不能据此替代事实、覆盖和任务约束核验。 |
| N064 | Li等：[Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection](https://aclanthology.org/2026.acl-long.235/)，ACL 2026 | 把纯人写、纯模型生成以及两种人机编辑来源细分，研究创作者与编辑者的区别。 | 第4章：生成文本识别的标签随混合创作条件改变；不将检测结果当作作者身份的确定证明。 |

### 补足生成、开放对话与翻译子任务

| 编号 | 论文及一手来源 | 年份与贡献类型 | 任务问题 | 大纲用途与边界 |
| --- | --- | --- | --- | --- |
| N065 | Gardent、Shimorina、Narayan与Perez-Beltrachini：[The WebNLG Challenge: Generating Text from RDF Data](https://aclanthology.org/W17-3518/) | INLG 2017，任务/共享基准 | 将给定RDF三元组集合表达为自然语言；涉及词语选择、信息聚合、指代表达、句子切分和表层实现等相互关联的选择。 | 第5章5.2节保留数据到文本任务，区分结构化事实输入与文本改写。WebNLG主要给定待表达内容，不能据此把宏观内容选择、报告规划等所有问题都视为已覆盖。任务和约束是主线，规则、统计与神经路线只简述。 |
| N066 | Zhang等：[Personalizing Dialogue Agents: I have a dog, do you have pets too?](https://aclanthology.org/P18-1205/) | ACL 2018，任务/数据与方法混合 | 开放域闲聊容易缺少具体内容和稳定的人设；通过Persona-Chat及说话者资料条件研究有个性、较一致的对话。 | 第6章“问答与对话”明确保留开放域对话、人设条件和跨轮一致性。该文涉及对话中的人物资料，不足以代表所有长期记忆或个性化机制，更不能将人设一致等同于事实真实。 |
| N067 | Dinan等：[Wizard of Wikipedia: Knowledge-Powered Conversational Agents](https://arxiv.org/abs/1811.01241)，[官方项目及会议引用](https://parl.ai/projects/wizard_of_wikipedia/) | ICLR 2019，任务/数据与方法混合；预印本2018 | 开放域对话需要从外部知识中找出相关内容并结合交流上下文作出回复；数据标注将对话回复与维基百科知识依据连接。 | 第6章“知识支持的交流”小节保留知识对话，复用“证据问答”节的资料获取流程。评价知识选择与回复质量；明确它是多轮开放交流，不只是一串事实问答。检索、阅读、生成方法简述后回指相关章节。 |
| N068 | Yao等：[Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract.html) | NeurIPS 2023，方法 | 当任务需要探索多个候选路径、前瞻与回退时，单一路径从左到右生成可能过早固定决定；论文在24点、填字等具有约束的任务以及创作任务上比较搜索式求解。 | 第7章将自然语言问题求解与程序任务合讲，说明候选状态、约束检查、搜索与验证之间的关系；ToT只作代表方法简述。24点可用算术规则核验，创作任务不能按同样方式判定正确；此文不代表形式化数学证明或全部逻辑推理任务。主体地图已有GSM8K，可与其配合而不重复列论文。 |
| N069 | Ma等：[STACL: Simultaneous Translation with Implicit Anticipation and Controllable Latency using Prefix-to-Prefix Framework](https://aclanthology.org/P19-1289/) | ACL 2019，方法；预印本2018 | 源句尚未结束就必须开始输出译文，词序差异使等待信息与提前判断发生冲突；通过前缀到前缀任务形式和wait-k策略研究可控延迟。 | 第5章5.5节加入同时翻译或流式翻译，明确翻译质量与延迟的共同评价；第8章的语音任务承接识别和声音输出。该文主要支持同时文本翻译的方法入口，不能直接用来宣称已覆盖端到端实时语音翻译。 |
| N070 | Zhao等：[DiscoX: Benchmarking Discourse-Level Translation in Expert Domains](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d6b903d62b6a8fb40df8c1dec037ed12-Abstract-Conference.html) | ICLR 2026，任务/基准与评价 | 专业领域的篇章翻译要求跨段连贯和严格术语准确，仅评价片段流畅与准确无法充分反映任务；提供中英专业篇章数据，并研究准确性、流畅性和适切性的细粒度评价。 | 第5章的翻译任务保留篇章与专业领域条件，连接第2章篇章分析中的衔接、连贯和指代内容；译文应在术语、一致性、篇章结构和使用目的上检验。它支持篇章翻译覆盖，不能作为实时翻译证据；官方页为2026会议论文，题名和时间已核验。 |

### 上下文查询与数据库对话的补充依据

| 编号 | 论文及一手来源 | 年份与出处 | 任务问题与大纲用途 |
| --- | --- | --- | --- |
| N071 | Yu等：[SParC: Cross-Domain Semantic Parsing in Context](https://aclanthology.org/P19-1443/) | 2019，ACL | 以连贯问题序列研究上下文依赖、跨领域及未见数据库的SQL解析。用于第2章“语义解析与形式表达”中的数据库查询方法，把单条查询与上下文解析分开；不以单轮准确性替代整段交互效果。 |
| N072 | Yu等：[CoSQL: A Conversational Text-to-SQL Challenge Towards Cross-Domain Natural Language Interfaces to Databases](https://aclanthology.org/D19-1204/) | 2019，EMNLP-IJCNLP | 数据库查询对话包括SQL状态、结果回复及用户行为，涉及澄清与不可回答。用于第2章解析、第6章结构化证据与任务对话的连接；未见数据库、执行结果和交流状态分别核验。 |

## 任务实现方法的一手来源补充

以下补充服务于细纲中的具体算法、计算及恢复步骤，包含2017年以前的经典方法和其后的代表实现。它们不追加到N001—N072的任务研究主表，也不用于扩大“近十年论文”的统计口径。已在主表收录的工作直接复用；LSA／NMF、朴素贝叶斯、SVM、CRF、VAE及Dawid–Skene等一般原理沿用前卷来源。重要实现已在任务小节下设置独立的方法小小节；来源表以任务位置和方法名称定位，通用模型原理仍回指前卷。

通知、矩阵、状态表、代码错误与执行轨迹均为计划中的教学构造。规则校验、单位回查、播放队列及完成谓词是本书建议的实现安排，不声称由某一论文首创；原论文的实际贡献和教材的组合流程分别说明。以下来源已核验基本元信息及所采用的机制，正式写作仍须固定版本、补齐参数和例子，并统一BibTeX。

### 文本分析、信息抽取与记录整合

| 方法或对应位置 | 原始来源及年代／状态 | 讲解机制与边界 |
| --- | --- | --- |
| 有限状态形态分析 | [Helsinki Finite-State Technology](https://hfst.github.io/)；官方项目 | 官方项目说明有限状态转导器用于形态处理；本大纲不要求安装或绑定特定工具。 |
| 双仿射依存解析 | [Deep Biaffine Attention for Neural Dependency Parsing](https://arxiv.org/abs/1611.01734)；2017 | 2016预印本，ICLR 2017论文；边和标签评分与树解码区分。 |
| GlossBERT | [GlossBERT: BERT for Word Sense Disambiguation with Gloss Knowledge](https://aclanthology.org/D19-1355/)；2019 | 已核验语境—释义句对监督分类的机制。 |
| 词义个性化PageRank | [Personalizing PageRank for Word Sense Disambiguation](https://aclanthology.org/E09-1005/)；2009 | 图结构和语境偏置用于词义排序；不是普通全图PageRank直接产生语境相关词义。 |
| CAMR | [A Transition-based Algorithm for AMR Parsing](https://aclanthology.org/N15-1040/)；2015 | 原始转移解析文章；比较依存树／图变换与序列化生成的不同对象。 |
| RAT-SQL | [RAT-SQL: Relation-Aware Schema Encoding and Linking for Text-to-SQL Parsers](https://aclanthology.org/2020.acl-main.677/)；2020 | 关联问题、模式与模式链接，再进行SQL结构解码。 |
| SQLNet | [SQLNet: Generating Structured Queries From Natural Language Without Reinforcement Learning](https://arxiv.org/abs/1711.04436)；2017 | 已核验骨架、依赖关系、序列到集合及列关注机制；限制于论文的查询范围，不代表任意SQL。 |
| PICARD | [PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models](https://aclanthology.org/2021.emnlp-main.779/)；2021 | 逐步增量解析拒绝非法候选词元，不保证目标语义正确。 |
| 移进—归约篇章解析 | [An effective Discourse Parser that uses Rich Linguistic Information](https://aclanthology.org/N09-1064/)；2009 | 原始文章描述修改的移进—归约过程；不把不同核性／关系规范混为同一标注。 |
| 论证单元与ILP结构恢复 | [Parsing Argumentation Structures in Persuasive Essays](https://aclanthology.org/J17-3005/)；2017 | 序列标注后联合优化单元类型及论证关系。 |
| 双仿射论证依存解析 | [End-to-End Argument Mining as Biaffine Dependency Parsing](https://aclanthology.org/2021.eacl-main.55/)；2021 | 将论证结构与依存式边预测相联系；适用结构条件必须先说明。 |
| 实体网格与连贯性 | [Modeling Local Coherence: An Entity-Based Approach](https://aclanthology.org/J08-1001/)；2008 | 角色转移、局部连贯和排序任务；2005较早会议版本另有发表，避免把2008当作唯一提出年份。 |
| 跨轮HMM话语行为 | [Dialogue act modeling for automatic tagging and recognition of conversational speech](https://aclanthology.org/J00-3003/)；2000 | 经典对话行为序列模型；本章只复用任务所需观测及状态映射。 |
| 双仿射跨度NER | [Named Entity Recognition as Dependency Parsing](https://aclanthology.org/2020.acl-main.577/)；2020 | 评分起止词对后按平面或嵌套实体约束选跨度，不是在NER结果上强制建依存树。 |
| 查询式NER | [A Unified MRC Framework for Named Entity Recognition](https://aclanthology.org/2020.acl-main.519/)；2020 | 类别描述／问题到原文答案跨度，支持平面与嵌套任务。 |
| UIE | [Unified Structure Generation for Universal Information Extraction](https://aclanthology.org/2022.acl-long.395/)；2022 | 结构化抽取语言和模式提示；本文的生成后原文核验是教材补充的流程要求，不声称原文强制保证事实正确。 |
| BLINK | [Scalable Zero-shot Entity Linking with Dense Entity Retrieval](https://aclanthology.org/2020.emnlp-main.519/)；2020 | 双编码召回加交叉编码重排；NIL检测需额外规定。 |
| CasRel | [A Novel Cascade Binary Tagging Framework for Relational Triple Extraction](https://aclanthology.org/2020.acl-main.136/)；2020 | 关系视作由主体到客体的映射，比较共享实体三元组绑定。 |
| TPLinker | [TPLinker: Single-stage Joint Extraction of Entities and Relations Through Token Pair Linking](https://aclanthology.org/2020.coling-main.138/)；2020 | 词元对联合链接和handshaking标记恢复三元组。 |
| ATLOP | [Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling](https://ojs.aaai.org/index.php/AAAI/article/view/17717)；2021 | 实体对阈值类别与局部上下文池化，分别处理多标签和多实体条件。 |
| EIDER | [Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion](https://aclanthology.org/2022.findings-acl.23/)；2022 | 关系与证据联合训练，推理融合完整文档和证据输入预测；原论文允许启发式silver证据监督。 |
| DMCNN | [Event Extraction via Dynamic Multi-Pooling Convolutional Neural Networks](https://aclanthology.org/P15-1017/)；2015 | 候选触发／论元位置控制上下文池化，用作经典任务机制对照。 |
| Text2Event | [Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction](https://aclanthology.org/2021.acl-long.217/)；2021 | 事件记录线性化、模式约束解码及课程学习；只在相关环节讲必要机制。 |
| EEQA | [Event Extraction by Answering (Almost) Natural Questions](https://aclanthology.org/2020.emnlp-main.49/)；2020 | 角色问题到论元跨度，避免前置实体识别错误传播的任务设计。 |
| HeidelTime／SUTime | [HeidelTime: High Quality Rule-Based Extraction and Normalization of Temporal Expressions](https://aclanthology.org/S10-1071/)；2010 | 规则、资源与上下文线索处理时间表达提取及归一化。 |
| HeidelTime／SUTime | [SUTime: A library for recognizing and normalizing time expressions](https://aclanthology.org/L12-1122/)；2012 | 可扩展确定性时间规则系统；规则资源须符合所讲语言，不能把英语工具直接声称为中文支持。 |
| Fellegi–Sunter记录匹配 | [A Theory for Record Linkage](https://www.tandfonline.com/doi/abs/10.1080/01621459.1969.10501049)；1969 | 经典似然比及接受／拒绝／可能匹配的判断；网页上线2012不是论文年份。 |
| JSON Schema／SHACL | [JSON Schema Validation: A Vocabulary for Structural Validation of JSON](https://json-schema.org/draft/2020-12/json-schema-validation)；2020 | 结构验证规范，不提供事实真伪保证。 |
| JSON Schema／SHACL | [Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/)；2017 | W3C推荐规范，图约束验证与证据支持分开。 |
| W2NER | [Unified Named Entity Recognition as Word-Word Relation Classification](https://ojs.aaai.org/index.php/AAAI/article/view/21344)；2022 | NNW内部邻接与THW-*带类型首尾关系；依据路径恢复实体，不把整个首尾区间都视为不连续实体文本。 |
| ReVerb | [Identifying Relations for Open Information Extraction](https://aclanthology.org/D11-1142/)；2011 | 原始开放关系抽取文章；关系短语与论元恢复作经典比较。 |
| Hobbs代词消解 | [Resolving pronoun references](https://www.sciencedirect.com/science/article/pii/0024384178900062)；1978 | 按特定次序遍历句法树并筛候选；语言和特征适用条件不能省略。 |

### 文本判定、主题发现与关键短语

| 方法或对应位置 | 原始来源及年代／状态 | 讲解机制与边界 |
| --- | --- | --- |
| pLSA | [Probabilistic Latent Semantic Analysis](https://arxiv.org/abs/1301.6705)；UAI 1999；2013为原文补存 | 4.3.1.3：文档混合、主题词分布与EM；新文档固定词分布后估计比例。 |
| LDA | [Latent Dirichlet Allocation](https://jmlr.org/papers/v3/blei03a.html)；JMLR 2003 | 4.3.1.4：文档先验与主题推断；含主题词先验的贝叶斯扩展回指前卷，不混为原始参数化。 |
| NVDM | [Neural Variational Inference for Text Processing](https://proceedings.mlr.press/v48/miao16.html)；ICML 2016 | 4.3.1.5：神经推断与词袋重构；连续潜在表示的含义区别于LDA主题比例。 |
| ProdLDA | [Autoencoding Variational Inference For Topic Models](https://arxiv.org/abs/1703.01488)；ICLR 2017 | 4.3.1.6：摊销推断和专家乘积式词分布；CTM依据主表N004的CombinedTM。 |
| BERTopic | [BERTopic: Neural topic modeling with a class-based TF-IDF procedure](https://arxiv.org/abs/2203.05794)；2022，预印本 | 4.3.1.8：文档表示、降维、密度聚类和c-TF-IDF；成员得分不等于LDA混合比例。 |
| 监督主题模型 | [Supervised Topic Models](https://www.cs.columbia.edu/~blei/papers/BleiMcAuliffe2007.pdf)；NeurIPS 2007 | 4.3.1.4比较：文档响应标签参与主题估计及预测，不作为无标签主题发现的同一监督条件。 |
| 动态主题模型 | [Dynamic Topic Models](https://www.cs.columbia.edu/~blei/papers/BleiLafferty2006a.pdf)；ICML 2006 | 4.3.1.4比较：按时间片改变主题词分布，增量使用与模型内部时间假设分别说明。 |
| fastText分类 | [Bag of Tricks for Efficient Text Classification](https://aclanthology.org/E17-2068/)；EACL 2017 | 4.1.1：词与词n-gram表示聚合及分类；不与字符子词词向量训练混为同一算法。 |
| TextCNN | [Convolutional Neural Networks for Sentence Classification](https://aclanthology.org/D14-1181/)；EMNLP 2014 | 4.1.1比较：局部窗口特征、池化和分类头，网络完整机制回指模型卷。 |
| DetectGPT | [DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature](https://proceedings.mlr.press/v202/mitchell23a.html)；ICML 2023 | 4.1.4：模型对数概率及扰动评分；所需概率访问和来源条件明确，不作为作者身份确定证明。 |
| SBERT | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://aclanthology.org/D19-1410/)；EMNLP-IJCNLP 2019 | 4.2.1：共享编码、句向量及句对／三元组监督；聚类和检索只复用表示接口。 |
| SimCSE | [SimCSE: Simple Contrastive Learning of Sentence Embeddings](https://aclanthology.org/2021.emnlp-main.552/)；EMNLP 2021 | 4.2.1：dropout正对与NLI监督正负例分别说明；对比学习通用机制回指前卷。 |
| 句长对齐 | [A Program for Aligning Sentences in Bilingual Corpora](https://aclanthology.org/P91-1023/)；ACL 1991 | 4.2.5：长度证据、顺序和一对多配对的经典基线，跨语言表现不能无条件推广。 |
| 词对齐 | [A Simple, Fast, and Effective Reparameterization of IBM Model 2](https://aclanthology.org/N13-1073/)；NAACL 2013 | 4.2.5比较：fast_align输出词间对应，与句对齐的单元和恢复步骤区分。 |
| MinHash近重复 | [On the Resemblance and Containment of Documents](https://cadmo.ethz.ch/education/lectures/FS18/SDBS/papers/broder.pdf)；1997，原论文镜像 | 4.2.5：文档片段集合、相似与包含及抽样表示；任务阈值和事实变更另外核验。 |
| SimHash指纹 | [Similarity Estimation Techniques from Rounding Algorithms](https://www.cs.princeton.edu/cass/publications.htm)；STOC 2002，作者项目原论文入口 | 4.2.5：向量相似估计与指纹比较；不把SimHash的相似关系自动等同于Jaccard。 |
| RAKE | [Automatic Keyword Extraction from Individual Documents](https://onlinelibrary.wiley.com/doi/10.1002/9780470689646.ch1)；2010，原始方法章节 | 4.3.3.2：停用词分割、词频及共现度、候选短语聚合。 |
| YAKE | [YAKE!官方方法与实现文档](https://oss.inesctec.pt/yake/)；官方项目 | 4.3.3.3：单篇文本的局部统计特征、候选评分和去重，不需要参考语料的文档频率。 |
| TextRank | [TextRank: Bringing Order into Text](https://aclanthology.org/W04-3252/)；EMNLP 2004 | 4.3.3.4和5.4.1.1：词共现图与句子关系图分别用于关键词和抽取式摘要，节点与交付物不同。 |
| EmbedRank | [Simple Unsupervised Keyphrase Extraction using Sentence Embeddings](https://aclanthology.org/K18-1022/)；CoNLL 2018 | 4.3.3.5：文档—候选短语表示匹配与MMR去冗余；生成式关键短语另定内容支持要求。 |
| ESIM | [Enhanced LSTM for Natural Language Inference](https://aclanthology.org/P17-1152/)；ACL 2017 | 4.2.3.2：语境编码、软对齐、局部比较和组合，顺序ESIM与树结构扩展分别说明。 |
| ColBERT | [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://arxiv.org/abs/2004.12832)；SIGIR 2020 | 4.2.4.4：查询／文档词元表示与MaxSim后期交互，索引和完整搜索实现回指搜索部分。 |
| CopyRNN | [Deep Keyphrase Generation](https://aclanthology.org/P17-1054/)；ACL 2017 | 4.3.3.7：文档—短语配对、生成与复制、束搜索候选；源文出现与未出现的关键短语分别评价。 |

### 文本生成、转换、问答与对话

| 方法或对应位置 | 原始来源及年代／状态 | 讲解机制与边界 |
| --- | --- | --- |
| 5.1.2.2 | [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751)，ICLR 2020，预印本2019 | 核采样的累积概率截断；不把开放生成的采样结论推广为所有转换任务的正确性保证。 |
| 5.2.1.2 | [Data-to-Text Generation with Content Selection and Planning](https://ojs.aaai.org/index.php/AAAI/article/view/4668)，2019 | 先选择和排列记录，再据内容规划形成文本；记录、规划与文本分别建模。 |
| 5.2.2.1 | [Plan-and-Write: Towards Better Automatic Storytelling](https://ojs.aaai.org/index.php/AAAI/article/view/4726)，2019 | 故事情节规划后写作，静态完整规划与动态交替规划两种安排。 |
| 5.3.1.2 | [Delete, Retrieve, Generate: A Simple Approach to Sentiment and Style Transfer](https://arxiv.org/abs/1804.06437)，2018 | 属性片段删除、目标片段检索、重组；原任务允许改变指定属性，不能当作全部命题或立场保持的保证。 |
| 5.3.2.2 | [GECToR – Grammatical Error Correction: Tag, Not Rewrite](https://aclanthology.org/2020.bea-1.16/)，2020 | 输入—目标对齐、词元变换标签和迭代应用；核读PDF中的KEEP、APPEND、合并及形态变换示例。 |
| 5.6.3.2 | [Better Evaluation for Grammatical Error Correction](https://aclanthology.org/N12-1067/)，2012 | M2以编辑而非完整句子重合作为评价入口。 |
| 5.6.3.2 | [Automatic Annotation and Evaluation of Error Types for Grammatical Error Correction](https://aclanthology.org/P17-1074/)，2017 | ERRANT抽取并分类编辑；语言分析和错误分类规则须与中文另定协议区分。 |
| 5.3.3.2 | [Controllable Sentence Simplification](https://aclanthology.org/2020.lrec-1.577/)，2020，预印本2019 | ACCESS以长度、Levenshtein相似、词频复杂度和依存深度相关属性控制简化；PDF确认属性比例离散为标记。 |
| 5.4.1.2 | [Get To The Point: Summarization with Pointer-Generator Networks](https://aclanthology.org/P17-1099/)，2017 | 词表生成和来源复制的混合、同词复制概率汇总、coverage用于减少重复；不保证绝对忠实。 |
| 5.4.2.1 | [The Use of MMR, Diversity-based Reranking for Reordering Documents and Producing Summaries](https://www.cs.cmu.edu/~jade/)，1998，作者主页收录原论文 | 相关性与已选内容冗余的逐轮折衷。ACM DOI页访问失败，作者主页核验精确题名及SIGIR-98出处；可由主页原论文入口继续核读。 |
| 5.5.1.1 | [The Mathematics of Statistical Machine Translation: Parameter Estimation](https://aclanthology.org/J93-2003/)，1993 | IBM Model 1对齐后验与期望计数更新的短例，隐对齐与词翻译概率。 |
| 5.5.1.1 | [Statistical Phrase-Based Translation](https://aclanthology.org/N03-1017/)，2003 | 对齐、短语、重排及搜索的经典应用路线；现代翻译仍以条件生成展开。 |
| 5.5.1.2 | [Improving Neural Machine Translation Models with Monolingual Data](https://aclanthology.org/P16-1009/)，2016 | 目标语单语经回译形成合成平行样本；不混淆枢轴翻译与回译训练。 |
| 5.5.2.2 | [Context-Aware Monolingual Repair for Neural Machine Translation](https://aclanthology.org/D19-1081/)，2019 | 方法名称为DocRepair，逐句译文的目标语篇章修订；单语篇章与逐句往返翻译形成训练对。不是另一篇CADec方法。 |
| 5.6.1.1 | [SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization](https://aclanthology.org/2022.tacl-1.10/)，2022 | 将来源和摘要分句、形成NLI分数矩阵并聚合，解决句级判定与文档输入粒度差别。 |
| 5.6.1.2 | [QAFactEval: Improved QA-Based Factual Consistency Evaluation for Summarization](https://aclanthology.org/2022.naacl-main.187/)，2022 | 答案选择、问题生成、来源阅读、答案匹配及不可回答处理；PDF确认问题和可回答性组件。 |
| 5.6.2.1 | [Lexically Constrained Decoding for Sequence Generation Using Grid Beam Search](https://aclanthology.org/P17-1141/)，2017 | 按词汇约束完成进度组织搜索。 |
| 5.6.2.2 | [Fast Lexically Constrained Decoding with Dynamic Beam Allocation for Neural Machine Translation](https://aclanthology.org/N18-1119/)，2018 | 与GBS比较约束进度之间的固定束宽分配。 |
| 5.6.2.3 | [FUDGE: Controlled Text Generation With Future Discriminators](https://aclanthology.org/2021.naacl-main.276/)，2021 | 在部分序列上预测未来属性，调整已有生成器概率；软控制与硬约束分开。 |
| 5.6.3.1 | [Bleu: a Method for Automatic Evaluation of Machine Translation](https://aclanthology.org/P02-1040/)，2002 | 截断n-gram精确率和长度惩罚，明确语料汇总。 |
| 5.6.3.1 | [ROUGE: A Package for Automatic Evaluation of Summaries](https://aclanthology.org/W04-1013/)，2004 | 参考内容重合与ROUGE-L的最长公共子序列计算。 |
| 5.6.3.1 | [chrF: character n-gram F-score for automatic MT evaluation](https://aclanthology.org/W15-3049/)，2015 | 字符n-gram精确率、召回率及F分数。 |
| 5.6.3.2 | [Optimizing Statistical Machine Translation for Text Simplification](https://aclanthology.org/Q16-1029/)，2016 | SARI针对保留、增加与删除的简化评价；不套用于一般摘要。 |
| 5.6.3.4 | [COMET: A Neural Framework for MT Evaluation](https://aclanthology.org/2020.emnlp-main.213/)，2020 | 源文、译文、参考与人工质量标签的学习式评价接口。 |
| 5.6.3.4 | [Unbabel/COMET 官方项目](https://github.com/Unbabel/COMET) | 项目文档确认reference-free评价接口及具体QE模型，不能将所有COMET模型称为无参考。 |
| 6.1.1.2 | [Bidirectional Attention Flow for Machine Comprehension](https://arxiv.org/abs/1611.01603)，ICLR 2017，预印本2016 | BiDAF的问文交互与答案跨度预测作为比较；模型内部回指模型卷。 |
| 6.1.1.3 | [Dense Passage Retrieval for Open-Domain Question Answering](https://aclanthology.org/2020.emnlp-main.550/)，2020 | DPR双编码器、内积评分、正确片段与负片段训练；与BM25召回比较。 |
| 6.1.1.5 | [Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering](https://aclanthology.org/2021.eacl-main.74/)，2021 | FiD分别编码问题—候选片段，解码器融合；与RAG隐文档概率混合区分。 |
| 6.1.2.2 | [TaPas: Weakly Supervised Table Parsing via Pre-training](https://aclanthology.org/2020.acl-main.398/)，2020 | 选择单元格及可选聚合算子，无须先生成逻辑形式；与查询执行路线比较。 |
| 6.1.3.1 | [TAT-QA: A Question Answering Benchmark on a Hybrid of Tabular and Textual Content in Finance](https://aclanthology.org/2021.acl-long.254/)，2021 | 论文方法TAGOP通过序列标注选择单元格与文本片段，再用符号算子计算；不是只列基准。 |
| 6.2.2.1 | [A Decomposable Attention Model for Natural Language Inference](https://aclanthology.org/D16-1244/)，2016 | 注意对齐—局部比较—聚合的关系分类；FEVER原始基线实际使用该路线。已核读FEVER原论文PDF并修正JSON，未写成ESIM基线。 |
| 6.3.1.2 | [BERT for Joint Intent Classification and Slot Filling](https://arxiv.org/abs/1902.10909)，2019 | JointBERT句级意图与词元槽位的联合损失、原词与子词对齐；论文也比较了CRF扩展。 |
| 6.3.2.2 | [Transferable Multi-Domain State Generator for Task-Oriented Dialogue Systems](https://aclanthology.org/P19-1078/)，2019 | TRADE槽位门控与复制生成；PDF明确门控类别是ptr、none、dontcare，不能宣称它直接覆盖一切未知或否定。 |
| 6.3.2.3 | [A Simple Language Model for Task-Oriented Dialogue](https://arxiv.org/abs/2005.00796)，2020 | SimpleTOD序列化状态与任务输出；与增量状态更新比较。 |
| 6.3.4.2 | [Semantically Conditioned LSTM-based Natural Language Generation for Spoken Dialogue Systems](https://aclanthology.org/D15-1199/)，2015 | SC-LSTM将对话行为和语义槽位加入回复控制；比较去词汇化模板、槽位回填与条件生成。 |
| 6.4.3.1 | [MoEL: Mixture of Empathetic Listeners](https://aclanthology.org/D19-1012/)，2019 | 情绪分布、多个回应专家及软组合，不把情绪标签预测等同于恰当支持。 |
| 6.4.3.2 | [Towards Emotional Support Dialog Systems](https://aclanthology.org/2021.acl-long.269/)，2021 | ESConv的支持策略标注及策略条件回复接口；论文范围是支持交流，非专业处置效果。 |
| 6.5.1.1 | [Learning to Ask Good Questions: Ranking Clarification Questions using Neural Expected Value of Perfect Information](https://aclanthology.org/P18-1255/)，2018 | 候选问题、可能回答与预期效用用于澄清排序；教学信息减少与交互成本基线是本书构造，不能写成原论文同一公式。 |
| 6.5.2.2、6.6 | [Rank Analysis of Incomplete Block Designs: The Method of Paired Comparisons](https://academic.oup.com/biomet/article-abstract/39/3-4/324/326091)，1952 | Bradley–Terry成对比较模型及偏好聚合；出版方元数据核验题名年份，原文全文受访问限制。 |
| 6.5.3.2 | [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)，2023 | 生成—自反馈—修订的比较路线；反馈来源与人类协作分开，自反馈不能代替用户目标或事实证据。 |
| 5.4.2.2 | [Multi-Sentence Compression: Finding Shortest Paths in Word Graphs](https://aclanthology.org/C10-1037/)；COLING 2010 | 第5章多来源信息综合：词图、候选路径与句子压缩；教材额外检查否定、数值和来源，不能由最短路径保证事实完整。 |
| 6.1.3.2 | [FinQA: A Dataset of Numerical Reasoning over Financial Data](https://aclanthology.org/2021.emnlp-main.300/)；EMNLP 2021 | 第6章混合证据问答：相关证据选择、运算程序生成与执行；与TAGOP的标签和算子路线区分，题意、单位及尺度独立核验。 |

### 可执行求解、程序、工具及语音

| 一手来源及年代／状态 | 讲解位置、机制与边界 |
| --- | --- |
| [Self-Consistency Improves Chain of Thought Reasoning in Language Models（2022预印本，ICLR 2023）](https://arxiv.org/abs/2203.11171) | 采样多条推理序列，汇总一致答案；7.1.2。规范化、分组后投票不等于证明。 |
| [Tree of Thoughts: Deliberate Problem Solving with Large Language Models（NeurIPS 2023）](https://proceedings.neurips.cc/paper/2023/file/271db9922b8d1f4dd7aaef84ed5ac703-Paper-Conference.pdf) | 核读§3、算法1/2：候选生成、状态评分/投票、宽度受限BFS和DFS回溯；7.1.2。原文将A*与MCTS留作后续，JSON只作延伸。 |
| [PAL: Program-aided Language Models（ICML 2023）](https://proceedings.mlr.press/v202/gao23f.html) | 语言题目形成程序中间步骤，由Python解释器执行；7.1.2.4。单位与题目对应检查是额外任务验收。 |
| [Let's Verify Step by Step（2023预印本）](https://arxiv.org/abs/2305.20050) | 结果监督和步骤监督对象不同；7.1.3。PRM/ORM属于预测式评分，不能当形式证明器。 |
| [Z3官方指南](https://microsoft.github.io/z3guide/docs/logic/intro/) | SMT变量、约束、可满足性与模型读取；7.1.1。一般CSP前向检查/回溯是教学比较，不归因为Z3内部算法。 |
| [Lean 4官方教材：Propositions and Proofs](https://lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/) | 命题、证明项及类型核验，注意外加公理；7.1.3。形式化陈述是否对应原题须另查。 |
| [Python官方AST文档](https://docs.python.org/3/library/ast.html) | 源码解析成语法树，节点表示分支、调用、返回等；7.2.1。调用图与数据流需要额外语义分析，AST不独自提供。 |
| [Teaching Large Language Models to Self-Debug（2023）](https://arxiv.org/abs/2304.05128) | 执行结果、代码解释和反馈进入修订；7.2.2。原文有带测试/无测试情境，解释不是独立正确性证据。 |
| [SynCode: LLM Generation with Grammar Augmentation（2024）](https://arxiv.org/html/2403.01632v2) | 语法解析、DFA与词元掩码；7.2.2/7.3.1。soundness与completeness有各自条件，实际短accept序列可能保守放行；定理不保证完整正确终止，不写“保证程序/JSON功能正确”。 |
| [Agentless: Demystifying LLM-based Software Engineering Agents（2024，v2）](https://arxiv.org/html/2407.01489v2) | 层次定位、修复、补丁验证；7.2.3。使用当前三阶段描述，避免只照早期版本写成两阶段。 |
| [Reflexion: language agents with verbal reinforcement learning（NeurIPS 2023）](https://papers.nips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html) | 反馈转成反思文字存入回合记忆，不更新模型权重；7.3.3/7.3.4。外部与内部模拟反馈不能一概作为独立证据。 |
| [Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks（2006）](https://www.cs.toronto.edu/~graves/icml_2006.pdf) | 条件输出分解、扩展标签序列与前向递推；8.1.2.2。观测帧不必独立；先折叠重复再删空白，相邻重复目标需空白分隔。 |
| [Sequence Transduction with Recurrent Neural Networks（2012）](https://www.cs.toronto.edu/~graves/icml_2012.pdf) | 历史条件与路径求和结合，二维格点；8.1.2.5。原声学编码器双向，不能直接推出流式。 |
| [Listen, Attend and Spell（2015预印本）](https://arxiv.org/abs/1508.01211) | listener接受声学特征，speller用注意力输出字符；8.1.2.3。作为早期实现补充，不计近十年新增方向。 |
| [SpecAugment: A Simple Data Augmentation Method for Automatic Speech Recognition（Interspeech 2019）](https://arxiv.org/abs/1904.08779) | 声学特征时间扭曲、频率掩蔽和时间掩蔽；8.1.1。STFT/log-Mel/MFCC是常规信号处理步骤。 |
| [Turning Whisper into Real-Time Transcription System（IJCNLP-AACL 2023演示）](https://arxiv.org/abs/2307.14743) | Whisper原始设计非实时；局部一致性和自适应等待组织流式转写，8.1.2.6。 |
| [Kaldi解码图文档](https://kaldi-asr.org/doc/graph.html)、[HMM拓扑文档](https://kaldi-asr.org/doc/hmm.html) | HCLG组合、HMM路径与对齐接口；8.1.2/8.1.3。模型原理回指前卷。 |
| [X-vectors: Robust DNN Embeddings for Speaker Recognition（ICASSP 2018）](https://danielpovey.com/files/2018_icassp_xvectors.pdf) | 说话者监督、变长声音映射固定嵌入；8.1.3。原任务是说话者识别；与凝聚聚类组合成分段属于教学流程，未归因于原文方法贡献。 |
| [SLURP: A Spoken Language Understanding Resource Package（EMNLP 2020）](https://aclanthology.org/2020.emnlp-main.588/) | 声音、文本、语义资源，流水线基线与实体错误分析；8.2.1。BIO+意图分类/CRF/直接语义生成是代表实现，不说SLURP提出全部算法。 |
| [Neural Text Normalization with Subword Units（NAACL 2019工业论文）](https://aclanthology.org/N19-2024/) | 书面→读出形式的FST规则与句级seq2seq比较；8.3.1。中文多音字、号码和金额为本书案例，未称原文验证中文。 |
| [FastSpeech 2: Fast and High-Quality End-to-End Text to Speech（2020预印本，ICLR 2021）](https://arxiv.org/abs/2006.04558) | 从训练声音提取时长/音高/能量，推理用预测条件；长度调节后并行生成频谱，8.3.2。FastSpeech 2与直接波形的2s区分。 |
| [HiFi-GAN: Generative Adversarial Networks for Efficient and High Fidelity Speech Synthesis（NeurIPS 2020）](https://papers.nips.cc/paper/2020/file/c5d736809766d46260d816d8dbc9eb44-Paper.pdf) | 核读§2：梅尔上采样、多周期/多尺度判别、对抗+梅尔L1+特征匹配；8.3.3。未错写为原HiFi-GAN使用多分辨率STFT损失。 |
| [Seamless: Multilingual Expressive and Streaming Speech Translation（2023）](https://arxiv.org/abs/2312.05187) | Streaming采用EMMA，在未收到完整源语时形成目标；8.4.2。表达保持作为额外条件分别核验。 |
| [Voice Activity Projection: Self-supervised Learning of Turn-taking Events（Interspeech 2022）](https://www.isca-archive.org/interspeech_2022/ekstedt22_interspeech.html) | 核读§2：未来双方活动窗口/离散标签，保持/转移话轮和短回应事件，8.5.1。VAD、轮次结束和业务语义完成不同。 |

## 覆盖范围与后续正文选材

任务研究主表记录72项代表工作，其中67项支持本部分的八章，N041、N044、N046、N054、N055共5项保留为移交索引，详细任务由后续“图像和多模态处理”部分的文献地图承接。各任务覆盖深度仍不相同。少量论文中的一套基准不能代表同一任务的全部语言、领域或输出条件；例如英文纠错数据不能代表中文纠错，多项选择关系判断不能替代端到端抽取，给定候选的局部预测不能替代原始输入上的完整任务。

词义、形态、中文零指代、桥接和话语指示、隐式篇章关系、事件事实性、多元关系、创作和风格控制、对话摘要、共情、多方会话等已在大纲中保留入口；实现来源补充覆盖了这些任务的一批代表方法，但没有对每个分支建立同等规模的研究文献链。正式起草这些小节时继续选择直接支持任务定义与实现的原始材料，不能把已有样本写成完整研究史。

按相同任务和信息条件选择代表实现，至少说明预测单位、训练依据、核心操作、解码或结构恢复、结果核验和典型错误。对预印本保留发表状态与版本，不把作者对自身方法或基准的宣传用语直接写进教材。

一般模型、学习机制、风险保证和系统实现分别回指前文；本部分保留语言任务的输出要求和实现取舍。每章专门评价在当地展开，跨语言、数据污染、模型评审及完整应用比较由第1章约定共同协议，再在各任务章展开。
