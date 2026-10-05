# 搜索推荐和广告研究文献地图

## 检索范围与阅读方法

本文件为[研究课题分类及应用专题](recommendation-and-search-research-topics.md)和后续章纲提供任务、研究脉络和代表方法的来源。检索截止于2026年10月5日，主要覆盖2016—2026年；另补经典基础材料，支持协同过滤、隐式反馈排序和特征交互的首次讲解。文献以能够解释应用问题、提供方法对照或揭示评价边界为纳入依据，来源采用正式论文集、出版社、作者机构页面及作者公开稿。材料数量不用于判断研究趋势，代表材料也不等同领域的完整目录。

下列182项材料按检索来源与主要任务列出：搜索35项、推荐94项、广告28项、混排与体验5项、共同评价与环境7项和经典基础13项。各项的大纲落点对应[当前十章大纲](recommendation-and-search-outline.md)；按个性化及共同问题组织的入口见研究课题分类。搜索与推荐共享的偏差和评价材料集中列一次。年份优先采用正式发表年份；链接指向arXiv时另注明发表信息或仅核验到的预印本状态。正式发表的核验不等于每项实验都已复现；本文件不转录未经独立复核的提升百分比或跨平台效果结论。

重要模型在任务下设独立编号小节，具体计算、训练与使用随模型展开；同类论文及评价材料提供对照。每项应回答“它解决什么应用问题、怎样形成输出、结论依赖什么条件”；网络层、优化器和通用范式的完整机制回指前文。

架构与方法的另一条阅读入口见[应用架构与研究地图](recommendation-and-search-architecture.md)：标出各工作改动的主要模块、输入输出及训练关系。FM、FFM主要登记为T04排序预估方法；SIM的历史检索区别于物品候选召回；TIGER改变候选产生接口，OneRec尝试整合召回与排序。T01解释当前可用历史怎样支持需求建模，T06解释跨时间更新与适应，不能将利用长历史和优化长期价值混为同一问题。

## 搜索需求与候选检索

对应大纲3.2、3.3、3.4.1及9.2.2。候选产生区分目录检索或访问、基于标识生成的候选召回两个接口；词项、稀疏、稠密和多向量属于目录检索内部的方法，混合属于融合安排。匹配证据与输出接口分别判断。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| S01 | [Dense Passage Retrieval for Open-Domain Question Answering](https://aclanthology.org/2020.emnlp-main.550/) | EMNLP 2020 | 用问题—相关片段监督训练双编码检索器，为问答提供候选证据，展示不同措辞下的语义匹配。 | 含答案片段命中与一般文档相关性不同。问答流程回指NLP。 | 9.2.2.1.2 |
| S02 | [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://arxiv.org/abs/2004.12832) | SIGIR 2020；链接为作者稿 | 预编码文档，再以查询词元与文档词元的局部交互打分，兼顾细粒度匹配与候选检索。 | 多向量存储和访问成本仍须计入；实验主要针对段落搜索。 | 9.2.2.1.4 |
| S03 | [Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval](https://openreview.net/pdf?id=zeFrfgyZln) | ICLR 2021；ANCE | 用持续更新的近邻索引寻找困难负例，使训练更接近全语料检索中的候选竞争。 | 负例质量、误负例及索引更新条件影响训练。 | 3.4.1.2、4.3.3.2、9.2.2.1 |
| S04 | [SPLADE: Sparse Lexical and Expansion Model for First Stage Ranking](https://www.piwowarski.fr/publication/formalspladesparselexical2021/) | SIGIR 2021；作者出版页 | 学习带词项扩展的稀疏表示，改善词汇不匹配，并保留倒排检索接口。 | 稀疏程度与效果、代价有关；扩展词项不保证满足精确条件。 | 9.2.2.1.3 |
| S05 | [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | NAACL 2022 | 结合表示压缩与改进监督，缓解多向量检索的存储负担。 | 压缩与效果比较依赖论文的表示、语料和监督。 | 9.2.2.1.5 |
| S06 | [Transformer Memory as a Differentiable Search Index](https://proceedings.neurips.cc/paper_files/paper/2022/hash/892840a6123b5ec99ebaab8be1530fba-Abstract-Conference.html) | NeurIPS 2022；DSI | 将查询映射为文档标识，探索以模型参数承载文档访问关系的检索路线。 | 静态集合的实验不足以证明已解决大规模动态目录的增删更新。 | 3.2.2、3.3.2、9.2.2.1.6 |
| S07 | [Hybrid Hierarchical Retrieval for Open-Domain Question Answering](https://aclanthology.org/2023.findings-acl.679/) | Findings of ACL 2023 | 在文档候选与片段候选两阶段组合稀疏和稠密检索，考察不同粒度的融合。 | 效果、延迟及存储取舍来自特定QA集合，不是混合检索的普遍优势。 | 9.2.2.2 |
| S08 | [STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases](https://proceedings.nips.cc/paper_files/paper/2024/hash/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS Datasets and Benchmarks 2024 | 为商品、论文等对象查找建立同时含文本和关系条件的半结构化检索任务。 | 数据包含大量合成查询，也补充人工查询；不能直接等同真实流量。 | 2.2.3、9.1、9.3 |

## 搜索排序结果与交互

对应大纲9.2.3—9.2.5及9.3，去偏学习和效果验证分别连接第4、8章。复杂指令和需要推理的查询改变了相关性判定，不能只用是否谈论同一主题判断结果。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| S09 | [Unbiased Learning-to-Rank with Biased Feedback](https://www.microsoft.com/en-us/research/publication/unbiased-learning-rank-biased-feedback/) | WSDM 2017；预印本2016 | Propensity SVM-Rank按检查倾向对点击项的排序损失加权，用查询—文档特征学习线性排序器。 | 无偏性质依赖观察机制与倾向条件，不等于处理全部日志偏差。 | 4.3.3.4.1；9.2.3复用 |
| S10 | [Unbiased Learning to Rank with Unbiased Propensity Estimation](https://ciir-publications.cs.umass.edu/getpdf.php?id=1297) | SIGIR 2018；DLA；DOI 10.1145/3209978.3209986 | 排序与位置倾向以相互加权的列表损失联合学习，线上使用排序分数。 | 主要分析位置偏差及特定点击假设，任意日志中的真实相关性并不能自动识别。 | 4.3.3.4.3 |
| S11 | [Asking Clarifying Questions in Open-Domain Information-Seeking Conversations](https://ciir-publications.cs.umass.edu/getpdf.php?id=1339) | SIGIR 2019；Qulac数据集及BERT-LeaQuR、NeuQS方法 | 把澄清问题的取得、选择和后续文档检索组成流程，并建立离线会话评价数据。 | 高质量澄清问题的上限实验不意味着任何追问都有收益，须计交互成本。 | 2.3.1、9.2.5.1、9.2.5.2 |
| S12 | [Few-Shot Conversational Dense Retrieval](https://arxiv.org/abs/2105.04166) | SIGIR 2021；链接为作者稿，ConvDR | 利用会话上下文形成检索表示，以独立改写查询的教师表示辅助训练，减少会话监督需求。 | TREC CAsT和OR-QuAC的结果不能直接代表真实开放会话。 | 9.2.5.3 |
| S13 | [BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/65b9eea6e1cc6bb9f0cd2a47751a186f-Abstract-round2.html) | NeurIPS Datasets and Benchmarks 2021 | 在多领域、多任务集合中比较未针对目标集训练的检索器，建立跨域评价入口。 | 方法排序依赖当时模型与选定集合，不能把平均结果写成永久的算法优劣。 | 2.3.1、8.4.2、9.3 |
| S14 | [Is ChatGPT Good at Search? Investigating Large Language Models as Re-Ranking Agents](https://aclanthology.org/2023.emnlp-main.923/) | EMNLP 2023；RankGPT | 用指令让语言模型比较并重排既有候选，研究新知识条件和通过蒸馏降低使用代价。 | 候选池、提示、列表顺序、模型版本与预算影响结果。 | 4.3.1.3.3、9.2.3.4 |
| S15 | [BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html) | ICLR 2025；预印本2024 | 用需要理解代码、数学或领域问题的查询检验推理密集检索，并研究查询推理的作用。 | 困难集合的低分不表示日常搜索均失效，增加推理须计算成本。 | 9.2.5、9.3 |
| S16 | [FollowIR: Evaluating and Teaching Information Retrieval Models to Follow Instructions](https://aclanthology.org/2025.naacl-long.597/) | NAACL 2025；预印本2024 | 利用相关性评判指令构造数据，检查指令条件变化后结果排序能否对应变化，并训练检索器。 | 主题相关和满足限定条件分别判断，任务范围取决于指令与标注覆盖。 | 9.1、9.2.3、9.3 |

## 推荐候选个性化与生成式选择

对应第3—4章，并连接1.5的语言模型角色索引、2.2.3的语义与协同匹配和5.2.1的展示内容组织与列表构造。评分预测、候选检索、响应排序和生成真实物品标识是不同任务接口，文献里的“生成式”也不总指自然语言生成。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| R01 | [Deep Neural Networks for YouTube Recommendations](https://research.google/pubs/deep-neural-networks-for-youtube-recommendations/) | RecSys 2016 | 将海量视频选择分为候选生成和独立排序，说明输入、目标及规模约束怎样促成阶段分工。 | 单平台经验不能当作所有应用的统一结构；观看时长与点击目标也不同。 | 1.3、3.2.1.5、4.3.4.2 |
| R02 | [DropoutNet: Addressing Cold Start in Recommender Systems](https://papers.nips.cc/paper_files/paper/2017/hash/dbd22ba3bd0df8f385bdac3e9f8be207-Abstract.html) | NIPS 2017 | 训练时模拟交互信息缺失，使模型利用内容信息处理新用户或新物品。 | 需要可用且有预测价值的辅助内容，不能凭空恢复偏好。 | 2.3.1.1 |
| R03 | [Graph Convolutional Neural Networks for Web-Scale Recommender Systems](https://ai.stanford.edu/~jure/pubs/pinsage-kdd18.pdf) | KDD 2018；PinSage | 从物品—收藏板图及节点内容形成物品表示，再用于相关候选选择。 | 图的边语义、内容和平台规模决定使用条件，图网络结构回指模型卷，这里讲候选用途。 | 3.2.1.9 |
| R04 | [Sampling-Bias-Corrected Neural Modeling for Large Corpus Item Recommendations](https://research.google/pubs/sampling-bias-corrected-neural-modeling-for-large-corpus-item-recommendations/) | RecSys 2019 | 用物品频率估计修正热门分布下的训练负采样偏差，应用于大规模召回。 | 校正的是训练采样分布，不能与曝光选择偏差或评价采样混同。 | 3.4.1.1、4.3.3.2 |
| R05 | [Controllable Multi-Interest Framework for Recommendation](https://arxiv.org/abs/2005.09347) | KDD 2020；作者稿，ComiRec | 从行为中提取多个兴趣进行候选检索，再用可调聚合权衡命中与多样性。 | 离线权衡须通过实际用户反馈验证，用户兴趣也不能只凭簇数定义。 | 2.2.1、3.2.1.8、3.3.1、5.2.1 |
| R06 | [Recommender Systems with Generative Retrieval](https://proceedings.neurips.cc/paper_files/paper/2023/hash/20dcab0f14046a5c6b02b61da9f13229-Abstract-Conference.html) | NeurIPS 2023；TIGER | 用内容构造语义物品标识，再根据用户历史生成下一物品标识，探索新的候选检索接口。 | 输出需映射到真实物品；新物品泛化实验不等于无条件解决目录更新和冷启动。 | 3.2.2.1 |
| R07 | [Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations](https://proceedings.mlr.press/v235/zhai24a.html) | ICML 2024；HSTU | 将异质用户行为组织为序列转导任务，研究计算规模、推荐质量及工业应用。 | 行为序列转导不同于自由生成商品名称；网络计算与应用架构整合的范围分别说明。 | 1.5、2.2.1.12 |
| R08 | [OneRec: Unifying Retrieve and Rank with Generative Recommender and Iterative Preference Alignment](https://arxiv.org/abs/2502.18965) | 2025，arXiv预印本；本次仅核验到预印本 | 直接生成推荐列表，并利用偏好反馈尝试整合召回与排序，论文报告快手场景实验。 | 平台结果与奖励模型反馈有各自范围，不能据此宣称普遍替代多阶段推荐。 | 1.5、5.2.1.6 |
| R09 | [OneRec-Think: In-Text Reasoning for Generative Recommendation](https://aclanthology.org/2026.acl-long.123/) | ACL 2026，Long Papers | 将对话、文字推理与个性化物品推荐结合，通过物品—文本对齐及推荐专用反馈改善语义落地。 | 文字理由的可读性不证明解释了用户真实偏好的因果机制。 | 2.2.3、2.3.1、3.2.2.2、5.2.1、5.2.3 |

## 推荐序列会话列表与长期互动

对应2.2.1的历史交互理解及第5—7章的展示与问题扩展。下一行为预测描述用户可能怎样选择；列表和长期策略还需研究系统改变展示后用户会怎样选择。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| R10 | [Session-based Recommendations with Recurrent Neural Networks](https://arxiv.org/abs/1511.06939) | ICLR 2016；初稿2015，GRU4Rec | 利用一次短会话的连续行为预测下一物品，适用于缺少长期身份或画像的条件。 | 会话内意图不等于跨会话稳定偏好，也不解决长期价值。 | 2.2.1.1 |
| R11 | [Self-Attentive Sequential Recommendation](https://arxiv.org/abs/1808.09781) | ICDM 2018；SASRec | 从历史行为中选择与当前预测相关的部分，完成下一物品推荐。 | 需要明确时间与候选协议；下一物品命中不代表长期决策收益。 | 2.2.1.2 |
| R12 | [Deep Interest Network for Click-Through Rate Prediction](https://arxiv.org/abs/1706.06978) | KDD 2018；初稿2017，DIN | 针对不同候选广告选择相关历史，避免用同一固定用户表示压缩全部兴趣。 | 本身是广告CTR任务；候选相关兴趣可跨推荐复用，但不声称其完整建模行为顺序。 | 2.2.1.5、4.3.1.2.1、10.2.2 |
| R13 | [Session-Based Recommendation with Graph Neural Networks](https://ojs.aaai.org/index.php/AAAI/article/view/3804) | AAAI 2019；SR-GNN | 把会话转为物品转移图，以局部图关系及当前兴趣构造会话推荐。 | 图构造与会话边界改变可用关系；不等于长期用户图或跨会话记忆。 | 2.2.1.4 |
| R14 | [TransAct: Transformer-based Realtime User Action Model for Recommendation at Pinterest](https://arxiv.org/abs/2306.00248) | KDD 2023；作者稿 | 将即时行为与批量计算的长期表示结合，使当前推荐及时反映短期意图。 | 平台部署结果有场景范围，实时特征及服务实现归系统卷。 | 2.2.1.11、2.3.2 |
| R15 | [Fast Greedy MAP Inference for Determinantal Point Process to Improve Recommendation Diversity](https://proceedings.neurips.cc/paper/2018/hash/dbbf603ff0e99629dda5d75b6f75f966-Abstract.html) | NeurIPS 2018 | 加速DPP贪心选择，使物品质量与列表中相互差异能够共同进入重排。 | 加速贪心计算不等于求得组合优化的全局最优，相似性定义影响多样性含义。 | 5.2.1.2 |
| R16 | [Recommending What Video to Watch Next: A Multitask Ranking System](https://research.google/pubs/recommending-what-video-to-watch-next-a-multitask-ranking-system/) | RecSys 2019 | 在视频排序中共同利用多种参与和满意度反馈，处理竞争目标及选择偏差。 | 预测多个反馈与决定业务权衡是两步，不能用多任务平均成绩替代展示价值。 | 4.2.1.1、6.1.1 |
| R17 | [Equity of Attention: Amortizing Individual Fairness in Rankings](https://arxiv.org/abs/1805.01788) | SIGIR 2018；作者稿 | 将多次排序中累计注意与累计相关性相匹配，研究排序质量约束下的机会分配。 | 公平标准和注意模型需明确，不是每个物品平均曝光。 | 6.1.1、6.1.2、6.2.3.1 |
| R18 | [SlateQ: A Tractable Decomposition for Reinforcement Learning with Recommendation Sets](https://www.ijcai.org/proceedings/2019/360) | IJCAI 2019 | 将推荐列表的长期价值分解为物品价值与用户选择关系，缓解列表行动的组合规模。 | 一次最多消费一个物品，也可不消费；给定当前状态后，奖励和转移仅依赖消费对象，学习需选择概率模型。 | 7.2.1.1、7.2.2.1 |
| R19 | [FairRec: Two-Sided Fairness for Personalized Recommendations in Two-Sided Platforms](https://cse.iitkgp.ac.in/~abhijnan/papers/patro_FairRec_WWW20.pdf) | WWW 2020 | 将个性化推荐映射为带用户与生产者约束的分配问题，兼顾用户获得的质量与生产者的曝光。 | 保证对应论文的两侧分配标准，不自动适用于所有公平定义或现实市场。 | 6.1.2、6.2.3.2 |

## 长历史与语言模型推荐补充

对应2.2.1的序列与长历史、2.2.3的语言语义与协同匹配，以及LLM4Rec各任务路线；统一角色索引在1.5，候选评分在4.3.1.3。生成式候选、行为序列与列表的代表工作仍见R06—R09，不重复登记。长历史输入、长期行动效果和语言模型参与的角色分别定义。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| R20 | [Search-based User Interest Modeling with Lifelong Sequential Behavior Data for Click-Through Rate Prediction](https://arxiv.org/abs/2006.05639) | CIKM 2020；SIM，作者稿 | 以候选为依据从长行为历史检索相关子序列，再作精细兴趣匹配，研究长历史的选择与响应预估。 | 原始应用为展示广告CTR；历史长度、候选相关选择与服务条件分别评价，不能把利用长历史当作长期策略优化。 | 2.2.1.9、4.3.1.2.2 |
| R21 | [Recommendation as Language Processing (RLP): A Unified Pretrain, Personalized Prompt & Predict Paradigm (P5)](https://arxiv.org/abs/2203.13366) | RecSys 2022；P5 | 将交互、描述和多个推荐相关任务转为文本输入输出，研究共享语言接口与个性化提示。 | 各任务输出、可用信息与目录映射仍需分别定义；统一文本接口不证明各任务具有相同效果。 | 1.5、4.3.1.3.1 |
| R22 | [TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation](https://arxiv.org/abs/2305.00447) | RecSys 2023；作者稿 | 将推荐数据用于语言模型适应，研究任务与预训练目标不一致时怎样取得推荐能力。 | 具体实验的数据规模、领域和输出协议限定结论；语言任务适应不自动提供全目录召回和列表决策。 | 2.3.1、4.3.1.3.2 |
| R23 | [Large Language Models meet Collaborative Filtering: An Efficient All-round LLM-based Recommender System](https://arxiv.org/abs/2404.11343) | KDD 2024；A-LLMRec | 将协同推荐器的表示与语言模型结合，使语义信息和用户—物品交互共同支持推荐。 | 冷、热及跨域条件分别评价；特定数据上的比较不足以证明所有语言模型都应采用同样融合。 | 2.2.3.1、2.3.1 |

## 行为理解、候选与评分模型补充

下列材料支持模型层次的独立讲解。行为模型按序列组织、候选相关性及长历史处理比较，候选模型说明怎样实际取得目录对象，评分模型说明字段交互或任务共享怎样形成响应输出。方法之间可组合，发表年份不构成必须替代前项的次序。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| R24 | [Deep Interest Evolution Network for Click-Through Rate Prediction](https://ojs.aaai.org/index.php/AAAI/article/view/4545) | AAAI 2019；初稿2018 | 用下一行为辅助监督学习兴趣状态，再以AUGRU按候选相关性调整兴趣演化。 | 原任务为CTR；预测兴趣轨迹不等于真实心理或长期行动效果，辅助监督不能泄露未来输入。 | 2.2.1.6、4.3.1.2、10.2.2 |
| R25 | [Deep Session Interest Network for Click-Through Rate Prediction](https://www.ijcai.org/Proceedings/2019/319) | IJCAI 2019 | 按会话划分历史，以会话内注意力和跨会话Bi-LSTM建立兴趣，再按候选聚合预估CTR。 | 会话划分决定证据组织；双向计算只使用请求前历史，不保证全部行为都满足会话内同质假设。 | 2.2.1.7、4.3.1.2、10.2.2 |
| R26 | [BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer](https://arxiv.org/abs/1904.06690) | CIKM 2019；作者稿 | 以随机遮蔽物品的完形填空目标训练双向历史编码，推断在历史末端追加MASK预测下一物品。 | 完整历史只能来自请求前；历史重建目标与实时下一物品预测接口需要区分。 | 2.2.1.3 |
| R27 | [Practice on Long Sequential User Behavior Modeling for Click-Through Rate Prediction](https://arxiv.org/abs/1905.09248) | KDD 2019；作者稿 | 以增量记忆读写和多通道兴趣状态压缩长行为历史，UIC在行为触发时维护状态以供请求读取。 | 固定容量记忆可能丢失历史细节；降低请求时开销不等于全部计算和状态维护成本消失。 | 2.2.1.8、2.3.2 |
| R28 | [TWIN: TWo-stage Interest Network for Lifelong User Behavior Modeling in CTR Prediction at Kuaishou](https://arxiv.org/abs/2302.02352) | KDD 2023；作者稿 | 使粗检索和精细注意力使用一致的候选—行为相关性，以特征拆分、预计算和偏置压缩控制长历史计算。 | 共享相关性度量缓解两阶段不一致，仍受历史选取容量、索引更新和计算预算限制。 | 2.2.1.10、4.3.1.2 |
| R29 | [Multi-Interest Network with Dynamic Routing for Recommendation at Tmall](https://arxiv.org/abs/1904.08030) | CIKM 2019 | 动态路由形成多个兴趣向量，训练中用标签感知注意关联正物品，服务时各兴趣近邻检索。 | 目标物品只在训练的兴趣关联中可用，服务时移除该模块；兴趣向量个数不等于真实兴趣数。 | 3.2.1.7 |
| R30 | [LightGCN: Simplifying and Powering Graph Convolution Network for Recommendation](https://arxiv.org/abs/2002.02126) | SIGIR 2020 | 用户—物品交互二部图上的归一化线性传播及层组合形成协同表示，以内积和BPR完成推荐。 | 原设定仅利用交互图，不自动提供新物品内容表示；图传播不等同在线关系遍历。 | 3.2.1.10 |
| R31 | [Wide & Deep Learning for Recommender Systems](https://arxiv.org/abs/1606.07792) | 2016作者稿；Google机构入口按arXiv:1606.07792著录 | 显式交叉线性分支与嵌入深层分支联合学习，在推荐响应任务中比较记忆与泛化。 | 原应用为Google Play应用推荐，不标为RecSys主会论文；若要登记DLRS正式会议版需另核对应论文DOI。 | 4.3.1.1.3 |
| R32 | [DeepFM: A Factorization-Machine based Neural Network for CTR Prediction](https://www.ijcai.org/proceedings/2017/0239.pdf) | IJCAI 2017 | FM与深层分支共享原始特征嵌入，把低阶交互和隐式复杂交互联合用于CTR预估。 | 不同分支共享与目标量按具体响应任务说明，不声称较高阶无条件改善。 | 4.3.1.1.4 |
| R33 | [Deep & Cross Network for Ad Click Predictions](https://arxiv.org/abs/1708.05123) | ADKDD 2017（KDD研讨会） | 交叉网络对原始输入与当前层显式交互，和深层分支共同产生广告响应分数。 | 有界阶显式交叉的参数表达能力仍有限；ADKDD不标成KDD主会。 | 4.3.1.1.5 |
| R34 | [DCN V2: Improved Deep & Cross Network and Practical Lessons for Web-scale Learning to Rank Systems](https://arxiv.org/abs/2008.13535) | WWW 2021；作者稿始于2020 | 用矩阵交叉提高表达能力，再用低秩与低秩专家混合控制任务计算代价。 | 低秩、混合与部署收益保留具体数据及计算预算；交叉模块的专家不同于任务共享MMoE。 | 4.3.1.1.6 |
| R35 | [xDeepFM: Combining Explicit and Implicit Feature Interactions for Recommender Systems](https://arxiv.org/abs/1803.05170) | KDD 2018 | CIN形成向量级显式交互，与线性及深层分支联合产生响应输出。 | 显式向量交互、隐式交互和计算负担分别说明，不简单称为更深的FM。 | 4.3.1.1.7 |
| R36 | [AutoInt: Automatic Feature Interaction Learning via Self-Attentive Neural Networks](https://arxiv.org/abs/1810.11921) | CIKM 2019；作者稿始于2018 | 同维字段表示经残差多头自注意力学习特征交互，输出CTR。 | 注意对象是输入字段，区别于DIN候选—历史兴趣；注意权重不自动是因果解释。 | 4.3.1.1.8 |
| R37 | [Modeling Task Relationships in Multi-task Learning with Multi-gate Mixture-of-Experts](https://research.google/pubs/modeling-task-relationships-in-multi-task-learning-with-multi-gate-mixture-of-experts/) | KDD 2018 | 多个响应任务共享专家，各任务独立门控及预测头，按任务学习共享程度。 | 处理预测任务关系与负迁移，不自动求解最终多目标决策，不以门控权重证明因果关系。 | 4.2.1.2 |
| R38 | [Progressive Layered Extraction (PLE): A Novel Multi-Task Learning (MTL) Model for Personalized Recommendations](https://dl.acm.org/doi/10.1145/3383313.3412236) | RecSys 2020 | 分开共享与任务专属专家，逐层路由联合提取并分离信息，研究复杂任务关系下的负迁移。 | 当前大纲保留共享结构和应用接口；任务改善需按标签与预算实测，不声称任意相关条件同时提高。 | 4.2.1.3 |

## 特征交互、联合评分与跨阶段共享

这一组分别支持特征交互扩展、完整评分器组织和跨阶段共享三个问题。RankMixer继续使用先行序列模块；MTGR、OneTrans和MixFormer联合组织字段与历史评分；OneTrans-V2进一步保留阶段职责而共享骨干。它们与R08的OneRec列表生成具有不同输入输出和整合范围。

| 编号 | 代表材料与来源 | 年份与发表状态 | 解决的问题与方法 | 使用边界 | 大纲主讲位置 |
| --- | --- | --- | --- | --- | --- |
| R39 | [RankMixer: Scaling Up Ranking Models in Industrial Recommenders](https://arxiv.org/abs/2507.15551) | CIKM 2025；[大会程序](https://www.cikm2025.org/program/conference-program)核验 | 多头特征混合、各特征单元前馈网络及稀疏专家变体，研究特征交互的有效规模扩展。 | 原始历史先经独立序列模块；统一特征交互不等于联合原始序列，也不等于跨阶段模型共享。 | 4.3.1.1.9；4.3.2.1复用 |
| R40 | [MTGR: Industrial-Scale Generative Recommendation Framework in Meituan](https://arxiv.org/abs/2505.18654) | CIKM 2025；[正式DOI](https://doi.org/10.1145/3746252.3761565)由作者全文核验 | 保留候选交叉特征，以HSTU编码器、语义组归一化、用户聚合及动态掩码组织候选响应计算。 | 作者释义为Meituan Generative Recommendation；编码器输出候选得分，需要外部候选，不能按名称当作列表生成。 | 4.3.2.2.1；HSTU基础回指2.2.1.12 |
| R41 | [OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender](https://arxiv.org/abs/2510.26104) | WWW 2026 Industry Track；[大会名单](https://www2026.thewebconf.org/accepted/industry.html)核验，作者稿首发2025-10-30 | 在共同因果Transformer堆栈中处理行为与字段，采用共享／特征专属参数、金字塔查询缩减及历史计算复用。 | 统一候选评分内部计算；历史不能读取后置候选字段，候选侧仍分别计算，不表示已统一召回及列表决策。 | 4.3.2.2.2 |
| R42 | [MixFormer: Co-Scaling Up Dense and Sequence in Industrial Recommenders](https://arxiv.org/abs/2602.14110) | KDD 2026；[正式DOI](https://doi.org/10.1145/3770855.3818447)由作者全文核验 | 逐层字段查询混合、历史交叉注意及输出融合，研究特征容量与历史长度联合扩展；解耦变体复用用户计算。 | 按共同层级计算归入联合骨干；参数组织与OneTrans不同，输出为多任务响应，不能推断生成物品列表。 | 4.3.2.2.3 |
| R43 | [OneTrans-V2: Unifying Retrieval, Pre-rank, and Fine-rank with One Transformer in Industrial Recommender](https://arxiv.org/abs/2609.28589) | 预印本，2026-09-23；截至检索日未核验正式发表 | 保留召回、粗排、精排，共享因果用户上下文并联合训练；DCGR按交互结果前缀生成候选，序列训练组织复用用户计算。 | 阶段及曝光特征隔离，分别读取请求时点可见历史；目标偏置是软引导，不能替代资格与预算约束，平台效果不外推。 | 4.3.4.2.1；DCGR主讲3.2.2.3 |

## 广告候选响应与反馈观测

对应10.1、10.2。广告价值输入不仅需要区分能力，还需要正确的条件概率、校准与可解释的标签成熟规则。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| A01 | [Beyond Keywords and Relevance: A Personalized Ad Retrieval Framework in E-Commerce Sponsored Search](https://arxiv.org/abs/1712.10110) | WWW 2018；初稿2017 | 将查询、历史及实时行为组织成多条广告候选路径，学习个性化候选价值。 | 广告检索还受供给和投放资格约束，不等于文本相关性。 | 10.2.1.1 |
| A02 | [OKG: On-the-Fly Keyword Generation in Sponsored Search Advertising](https://aclanthology.org/2025.coling-industry.10/) | COLING Industry Track 2025 | 使用搜索、广告API、记忆与计算工具取得信息，按上一轮KPI分配新类别扩展与成功类别细化的数量，迭代生成广告主关键词。 | 关键词维护与在线检索分开；原文离线比较用语义近邻关键词的KPI代理，不是新词真实投放的增量。 | 10.2.1.2 |
| A03 | [Entire Space Multi-Task Model: An Effective Approach for Estimating Post-Click Conversion Rate](https://arxiv.org/abs/1804.07931) | SIGIR 2018；ESMM | 用展示、点击和转化之间的条件关系，在全展示空间学习相关任务，缓解稀疏与点击样本选择问题。 | 联合预测不自动保证CVR无偏，须与A04一起讲。 | 10.1、10.2.2.1.1 |
| A04 | [ESCM²: Entire Space Counterfactual Multi-Task Model for Post-Click Conversion Rate Estimation](https://arxiv.org/abs/2204.05125) | SIGIR 2022 | 分析ESMM仍存在的估计偏差和任务依赖问题，用反事实风险正则作修正。 | 去偏仍依赖倾向及相关假设；“全空间”是数据制度，不能独自证明因果识别。 | 4.3.3.3、10.2.2.1.2 |
| A05 | [Field-aware Calibration: A Simple and Empirically Strong Method for Reliable Probabilistic Predictions](https://arxiv.org/abs/1905.10713) | WWW 2020；初稿2019 | 用字段信息进行后处理校准，处理总体校准掩盖广告位等分组失准的问题。 | 校准集须有足够数据且代表部署分布，跨时段或流量变化后需重验。 | 4.3.4.1、10.2.2.2.1 |
| A06 | [Capturing Delayed Feedback in Conversion Rate Prediction via Elapsed-Time Sampling](https://ojs.aaai.org/index.php/AAAI/article/view/16587) | AAAI 2021；ES-DFM | 通过经过时间采样和重要性修正平衡新鲜反馈与标签成熟，连接观察到的标签和最终转化。 | 时间采样机制与辅助权重估计是条件；等待窗口改变目标观察范围。 | 4.3.3.1、10.2.2.1.3 |
| A07 | [Asymptotically Unbiased Estimation for Delayed Feedback Modeling via Label Correction](https://arxiv.org/abs/2202.06472) | WWW 2022；DEFUSE | 分别处理即时正例、假负例、真实负例与迟到正例，细化标签与重要性修正。 | 渐近结论依赖辅助概率估计及论文的数据机制，不能简写为任意延迟日志均无偏。 | 4.3.3.1、10.2.2.1.4 |

## 广告竞价预算与市场互动

对应10.3。单次分配、单个投放任务的周期控制和多任务或跨渠道分配构成嵌套的控制范围；市场互动作为共同验证条件讨论。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| A08 | [Robust Auction Design in the Auto-bidding World](https://papers.nips.cc/paper/2021/file/948f847055c6bf156997ce9fb59919be-Paper.pdf) | NeurIPS 2021 | 在带回报约束的自动竞价者模型中研究保留价及加性调整，联系机制设计与收益、福利。 | 保证针对价值最大化及回报约束等设定，不将GSP无条件称为诚实机制。 | 10.3.1.1.3、10.3.1.2、10.3.2 |
| A09 | [A Field Guide for Pacing Budget and ROS Constraints](https://proceedings.mlr.press/v235/balseiro24a.html) | ICML 2024 | 比较预算与投产比控制变量的串联、最小值组合和联合对偶优化，研究约束协调。 | 保证需保留论文条件；平台数据支持的半合成实验不等于全面线上验证。 | 10.3.1.2.2、10.3.1.2.3、10.3.1.2.4 |
| A10 | [Optimization-Based Budget Pacing in eBay Sponsored Search](https://dspace.mit.edu/entities/publication/7993db5c-f306-4f12-8cf6-909c6bb6d7a8) | WWW Companion 2024 | 将AdaptivePacing调整到eBay广告业务环境，处理真实预算消耗与广告主差异。 | 正式入口为Companion；业务调整及平台结果不能推广为所有市场保证。 | 10.3.1.2.1 |
| A11 | [Autobidders with Budget and ROI Constraints: Efficiency, Regret, and Pacing Dynamics](https://proceedings.mlr.press/v247/lucier24a.html) | COLT 2024；论文集条目为3642–3643页 | 研究多个自动竞价器在预算与回报约束下的学习，连接个体遗憾和整体分配效率。 | 使用特定遗憾比较基准，市场效率采用论文定义的liquid welfare口径；不泛化到任意策略。 | 10.3.1.2、10.3.2 |
| A12 | [Multi-channel Autobidding with Budget and ROI Constraints](https://proceedings.mlr.press/v202/deng23c.html) | ICML 2023 | 在只能设置各渠道预算与目标回报等接口时，研究跨渠道自动竞价和整体约束下的价值优化。 | 需要明确平台接口与渠道响应假设，不能把渠道局部最优直接当成整体最优。 | 10.3.1.3.1 |

## 广告创意归因与增量效果

对应10.4、10.5。创意优化、归因记账与增量测量分别列出，避免把预测路径贡献当成真实干预收益。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| A13 | [Automated Creative Optimization for E-Commerce Advertising](https://arxiv.org/abs/2103.00436) | WWW 2021；AutoCO | 对创意元素组合建模，以后验估计和Thompson采样分配探索流量，处理大量版本的有限反馈。 | 研究素材组合与试验分配，通用图像生成另讲；美观指标不能替代累计投放效果。 | 5.3、10.4.2.1 |
| A14 | [HLLM-Creator: Hierarchical LLM-based Personalized Creative Generation](https://arxiv.org/abs/2508.18118) | 2025，arXiv预印本；本次仅核验到预印本 | 结合用户关注的卖点与商品事实生成个性化广告标题，并以分层设计控制开销。 | 论文报告抖音搜索广告实验，不能直接推广到所有广告形态；事实和落地页一致性另验。 | 10.4.1.1 |
| A15 | [Learning Multi-touch Conversion Attribution with Dual-attention Mechanisms for Online Advertising](https://arxiv.org/abs/1808.03737) | CIKM 2018；DARNN | 联合点击与转化路径信息学习多触点信用分配，并研究面向预算决策的代理评价。 | 注意权重与预测移除效应都不自动等于因果增量。 | 8.1、10.5.1.2 |
| A16 | [Ghost Ads: Improving the Economics of Measuring Online Ad Effectiveness](https://journals.sagepub.com/doi/10.1509/jmr.15.0297) | Journal of Marketing Research 2017 | 在随机对照中记录控制组本会获得展示的机会，提高投放机会与效果比较的对应程度。 | 需要投放侧配合记录反事实机会，实验仍须处理相应识别及干扰条件。 | 10.5.2.1 |
| A17 | [A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook](https://pubsonline.informs.org/doi/abs/10.1287/mksc.2018.1135) | Marketing Science 2019 | 将观察数据估计与大型随机广告实验对照，检验丰富用户特征能否重现实验效果。 | 所测场景中多种观察方法仍有偏差，不推出所有观察方法均无效。 | 8.3.1、8.3.2、10.5.2 |

## 共同评价与经典基础

反馈证据在2.1建立，训练标签与观测偏差对应4.1、4.3.3，评价协议与效果识别对应第8章，并与各任务的基本评价衔接。经典基础材料按讲解需要选取，2016年前的论文不列入近十年研究样本，经典方法也不能只用一句历史介绍代替必要机制。

| 编号 | 原始论文及入口 | 年份与版本 | 研究作用 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| E01 | [Recommendations as Treatments: Debiasing Learning and Evaluation](https://proceedings.mlr.press/v48/schnabel16.html) | ICML 2016 | 把推荐反馈的自选择与系统选择作为观测机制，用倾向校正训练与评价。 | 倾向准确、非零支撑及相关识别条件不能省略，小倾向会增大方差。 | 4.3.3.3、8.3.1.1 |
| E02 | [On Sampled Metrics for Item Recommendation](https://research.google/pubs/on-sampled-metrics-for-item-recommendation/) | KDD 2020 | 分析采样候选上的排名指标为何可能不保持全目录的相对优劣，并研究校正。 | 训练负采样与评价候选采样是两件事；采样协议不能隐藏。 | 8.2.2.2 |
| E03 | [A Critical Study on Data Leakage in Recommender System Offline Evaluation](https://arxiv.org/abs/2010.11060) | TOIS 2023；初稿2020 | 分析未按全局时间线划分数据造成未来交互和物品泄漏，提出时间线评价方案。 | 逐用户留出最后一次行为不能独自保证全局无未来信息。 | 8.4.1.1 |
| H01 | [The Probabilistic Relevance Framework: BM25 and Beyond](https://www.ccs.neu.edu/home/vip/teach/IRcourse/IR_surveys/robertson_foundations.pdf) | Foundations and Trends in Information Retrieval 2009；作者论文的公开镜像 | 提供词项检索及BM25的概率依据、假设与扩展，支持传统检索背景与有效基线。 | 这是整理性文献，不将2009记为BM25的起源。 | 9.2.2.1.1 |
| H02 | [Counterfactual Risk Minimization: Learning from Logged Bandit Feedback](https://proceedings.mlr.press/v37/swaminathan15.html) | ICML 2015 | 将已执行行动的日志反馈用于反事实风险学习，为搜索、推荐和广告的共同反馈问题提供前置材料。 | 需要日志策略信息与覆盖条件，重要性权重的方差需控制。 | 8.3.1 |
| H03 | [Item-based Collaborative Filtering Recommendation Algorithms](https://archives.iw3c2.org/www10/cdrom/papers/519/index.html) | WWW 2001；正式会议存档 | 利用物品间的交互相似性形成推荐，支持邻域计算、加权与候选构造的经典讲解。 | 交互相似性不同于内容相似性；原始评分设定与隐式反馈条件应分开。 | 3.2.1.2 |
| H04 | [BPR: Bayesian Personalized Ranking from Implicit Feedback](https://arxiv.org/abs/1205.2618) | UAI 2009；作者稿2012上传arXiv | 为隐式反馈建立成对排序准则，可与矩阵分解及其他评分模型结合。 | BPR是训练准则及相应学习方法，不是矩阵分解的别名；采样与未观测交互的解释须明确。 | 4.2.2.1 |
| H05 | [Factorization Machines](https://www.libfm.org/) | ICDM 2010；链接为作者资料及论文入口 | 通过低秩参数化学习稀疏特征的交互，为用户、物品及情境的联合响应预估建立模型。 | 讲清特征工程、损失与输出；模型可用于多个任务，应用中的字段和标签需另定义。 | 4.3.1.1.1 |
| H06 | [Field-aware Factorization Machines for CTR Prediction](https://www.csie.ntu.edu.tw/~cjlin/papers/ffm.pdf) | RecSys 2016；作者公开稿 | 让特征的表示依赖交互对象所属字段，研究比FM更细的交互参数化，并分析训练与代价。 | 额外参数与计算成本随字段和特征规模变化；特定CTR实验不能推出对所有任务优于FM。 | 4.3.1.1.2、10.2.2 |

补充经典原文，用于用户邻域、潜在因子、独立编码、学习排序、列表重排和日志估计的必要讲解。这些材料单独标明年份，不计入近十年的新方向。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| H07 | [GroupLens: An Open Architecture for Collaborative Filtering of Netnews](https://www.presnick.people.si.umich.edu/papers/cscw94/GroupLens.htm) | CSCW 1994 | 根据相似用户的评分预测未见对象，建立用户邻域聚合的经典实现。 | 原文是netnews显式评分与开放系统；隐式行为共现的推荐召回须另外定义。 | 3.2.1.1 |
| H08 | [Matrix Factorization Techniques for Recommender Systems](https://doi.org/10.1109/MC.2009.263) | Computer 42(8):30–37 | 整理潜在因子、偏置、正则化和观测评分上的拟合机制，为推荐矩阵分解的必要讲解提供依据。 | 整理性技术文章，不将2009视为矩阵分解推荐的唯一发端；原文评分与教学构造的目录访问分别说明。 | 3.2.1.3 |
| H09 | [Collaborative Filtering for Implicit Feedback Datasets](https://yifanhu.net/PUB/cf.pdf) | ICDM 2008 | 区分隐式反馈的偏好目标与置信度，对交互和未观测条目加权拟合并用ALS求解。 | 未观测的零目标是模型约定，行为强度不直接等同满意度；置信度及优化代价按原文定义。 | 3.2.1.4 |
| H10 | [Learning Deep Structured Semantic Models for Web Search using Clickthrough Data](https://www.microsoft.com/en-us/research/?p=165215) | CIKM 2013 | 分别编码查询与文档，用点击监督学习共同语义空间与匹配分数，提供独立编码的历史实现。 | 原始任务为搜索文档排序；推荐双塔迁移是教学改造，需重设用户条件、物品输入与行为监督。 | 3.2.1.6 |
| H11 | [From RankNet to LambdaRank to LambdaMART: An Overview](https://www.microsoft.com/en-us/research/publication/from-ranknet-to-lambdarank-to-lambdamart-an-overview/) | Microsoft Research Technical Report MSR-TR-2010-82 | 以原始作者技术报告完整讲解RankNet、LambdaRank与LambdaMART的相关性排序计算和训练依赖。 | 查询分组、等级或成对偏好、指标与特征定义限定目标；不保证离散指标全局最优，不作为近十年新研究样本。 | 9.2.3.1、9.2.3.2、9.2.3.3 |
| H12 | [The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing Summaries](https://www.cs.cmu.edu/afs/cs/Web/People/jgc/publication/MMR_DiversityBased_Reranking_SIGIR_1998.pdf) | SIGIR 1998 | 在相关性与已选对象冗余之间作贪心取舍。 | 权重及相似性定义决定取舍，贪心不保证全局最优或全面需求覆盖。 | 5.2.1.1 |
| H13 | [Doubly Robust Policy Evaluation and Learning](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/double_robust.pdf) | Proceedings of the 28th International Conference on Machine Learning (ICML 2011) | 在上下文行动日志中结合结果预测与倾向校正估计目标策略价值。 | 仍需覆盖和识别条件；单个辅助模型正确的稳健性不解决未覆盖行动、未记录混杂或两模型同时错误，也不保证所有有限样本更准。 | 8.3.1.2 |

## 混排、广告负载与体验

对应研究课题T15、T16，并连接T09多目标、T11长期价值和T19因果效果。混排需要决定类型、数量与位置，重复和负反馈还会改变之后的展示价值，不能仅将不同来源的分数排序后拼接。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| M01 | [Ads Allocation in Feed via Constrained Optimization](https://www.kdd.org/kdd2020/accepted-papers/view/ads-allocation-in-feed-via-constrained-optimization.html) | KDD 2020 | 自然内容与广告分别排序后，以受约束插入协调收入与参与度，提供轻量分配算法和线上检验。 | 保持来源内部顺序与同时改动全部候选的整列表优化是不同设定；算法保证依赖所采用的假设。 | 5.2.1.3、5.2.2 |
| M02 | [Blending Advertising with Organic Content in E-commerce via Virtual Bids](https://ojs.aaai.org/index.php/AAAI/article/download/26835/26607) | IAAI 2023部署应用轨；收入AAAI-23论文集 | 用虚拟出价表达平台对不同目标的估值，预测广告与自然商品共同展示时的交互，并连接分配与支付。 | 参与度是长期健康的代理，不能直接外推长期留存；具体分配与支付性质取决于机制设定。 | 5.2.1.4、10.3.1.1 |
| M03 | [Soft Frequency Capping for Improved Ad Click Prediction in Yahoo Gemini Native](https://arxiv.org/abs/2312.05052) | CIKM 2019；作者稿2023上传arXiv | 将用户—广告的重复曝光次数纳入响应预测，学习重复展示的价值变化，补充统一频次阈值。 | CTR衰减与收入评价不足以独自测量主观厌烦或长期留存；不能把arXiv上传年份当成发表年份。 | 5.2.4.1 |
| M04 | [Ad Close Mitigation for Improved User Experience in Native Advertisements](https://doi.org/10.1145/3336191.3371798) | WSDM 2020 | 预测广告关闭概率，将关闭损失纳入分配分数，并在收入约束下减少负反馈。 | 关闭是可观察体验信号，不能代表全部打扰感；企业页面的2019日期不同于正式发表年份。 | 5.2.5、5.3.1.1 |
| M05 | [Ad-load Balancing via Off-policy Learning in a Content Marketplace](https://arxiv.org/abs/2309.11518) | WSDM 2024；预印本2023 | 将每次信息流获取的广告负载作为决策，考虑用户差异与会话阶段，从随机日志学习策略并做线上实验。 | 日志估计需要倾向和覆盖条件；退出、滚动深度和次日回访各是部分体验代理，不能代表任意长期满意度。 | 5.2.1.5、5.2.2、5.3、8.3.1 |

M02的网页发布日期及自动引文显示2024，但论文PDF标为AAAI-23、版权2023，且[IAAI-23正式日程](https://aaai-23.aaai.org/wp-content/uploads/2023/01/IAAI-23-Program-Schedule-FEB07-1.pdf)列出该论文。本书按IAAI 2023应用轨引用，并保留这项元数据差异说明。

## 搜索查询表达与候选方法补充

查询表达、目录表示与标识输出分开登记；通用语言机制回指NLP，具体候选访问和成本由大纲第9章解释。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| S25 | [Contriever：Unsupervised Dense Information Retrieval with Contrastive Learning](https://arxiv.org/abs/2112.09118) | 作者稿首发2021，当前公开版2022；OpenReview审阅入口由原文提供 | 缺少查询—相关文档标签时，稠密候选表示仍需获得训练依据。 同一文档的不同裁剪和增强片段形成正对，以其他文档为对比对象学习单向量表示，文档预编码后通过向量访问取得候选 | 同源片段提供训练信号，不等同用户已经认可的相关文档；跨域、跨语言和后续监督微调分别评价。 | 9.2.2.1.7 |
| S26 | [E5：Text Embeddings by Weakly-Supervised Contrastive Pre-training](https://arxiv.org/abs/2212.03533) | 作者公开稿，2022；更新2024 | 单向量检索需要利用规模更大的文本配对，同时保持查询与对象的接口。 从筛选的弱监督文本对学习对比表示，再按具体检索任务使用或微调；查询与文档分别编码，文档向量可预计算并用于候选访问 | 弱监督配对和领域标签承担不同作用，通用嵌入效果不能直接当作商品偏好或所有条件满足的证据。 | 9.2.2.1.8 |
| S27 | [BGE-M3：M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation](https://aclanthology.org/2024.findings-acl.137/) | Findings of ACL 2024；正式题名M3-Embedding | 跨语言与长文本条件下，单一表示未必兼顾词项匹配和细粒度语义。 同一模型产生稠密、稀疏及多向量检索表示，并由多种匹配分数组成自蒸馏信号；按不同表示建立相应目录访问路径 | 共享编码器不消除三类访问与存储成本，长文本支持也不保证每个局部证据都被命中。 | 9.2.2.1.9 |
| S28 | [NCI：A Neural Corpus Indexer for Document Retrieval](https://proceedings.neurips.cc/paper_files/paper/2022/hash/a46156bd3579c3b268108ea6aca71d13-Abstract.html) | NeurIPS 2022 | 生成文档标识还需让标识结构和解码计算对应目录中的语义关系。 采用语义文档标识、前缀相关的权重适应解码、查询生成及一致性正则训练查询到标识的映射，解码后恢复实际文档 | 目录组织与合成查询均影响覆盖，静态集合实验不能直接证明已支持任意文档增删。 | 9.2.2.1.10 |
| S29 | [ReasonIR: Training Retrievers for Reasoning Tasks](https://arxiv.org/abs/2504.20595) | 作者公开稿，2025 | 需要推理的查询与短事实问句不同，候选训练要区分同主题与真正有帮助的文档。 构造需要推理的相关查询和看似相关但不能解决问题的困难负例，与公开数据共同训练稠密检索器，形成可访问目录的表示 | 合成标签与负例须核验，BRIGHT等特定集合结果保留范围，改写更长还会增加推理与检索成本。 | 9.2.2.1.11 |
| S30 | [HyDE：Precise Zero-Shot Dense Retrieval without Relevance Labels](https://aclanthology.org/2023.acl-long.99/) | ACL 2023 | 没有领域相关性标签时，原查询与文档表达可能相差较大。 语言模型生成假设相关文档，再由无监督检索编码器把该文本转换为向量，访问真实文档集合；生成模型及编码基础回指NLP | 假设文档可含错误，必须保留原查询的限定条件，实际结果来自目录并另行核验；生成文本不作为事实证据。 | 9.2.1.1 |
| S31 | [Query2doc: Query Expansion with Large Language Models](https://aclanthology.org/2023.emnlp-main.585/) | EMNLP 2023 | 补充查询表达需要同时考虑词项检索和稠密检索的输入。 通过少样例提示生成伪文档，再将原查询与伪文档组合用于扩展，分别接词项或向量候选路径，保持检索器及模型版本可追溯 | 查询扩展并不核实伪文档事实，词项重复、偏离需求和推理预算分别评价；与HyDE比较实际编码输入。 | 9.2.1.2 |

## 搜索相关性评分与重排补充

以下模型固定相关性任务，分别改变词项匹配、联合编码、排序监督及列表或推理计算。列表次序输出与展示页面决策分开。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| S17 | [DRMM：A Deep Relevance Matching Model for Ad-hoc Retrieval](https://arxiv.org/abs/1711.08611) | CIKM 2016；作者机构核验，arXiv上传2017 | 相近文本未必满足检索需求，相关性需要保留精确匹配与查询词的重要性。 查询词与文档词的相似度组成匹配直方图，匹配网络逐词形成证据，再由查询词门控汇总相关性分数；按查询内的相关与不相关文档比较训练 | 直方图汇总会丢失部分位置及上下文，词向量相近不代替实体、否定或数值条件核验。 | 9.2.3.5 |
| S18 | [K-NRM：End-to-End Neural Ad-hoc Ranking with Kernel Pooling](https://arxiv.org/abs/1706.06613) | SIGIR 2017；作者论文核验 | 固定匹配分箱难以随相关性标签一起调整词语匹配。 查询—文档词相似度经多个核函数形成不同强度的软匹配统计，排序层合成分数，以成对排序损失共同更新词嵌入及匹配计算 | 核池化关注匹配强度，不能自动恢复全部词序和限定关系；与DRMM比较时保持查询与标签相同。 | 9.2.3.6 |
| S19 | [DUET：Learning to Match Using Local and Distributed Representations of Text for Web Search](https://www.microsoft.com/en-us/research/publication/learning-match-using-local-distributed-representations-text-web-search/) | WWW 2017；作者机构正式出版页 | 词项精确匹配与语义表示提供不同的相关性证据。 局部表示分支处理查询词与文档词的精确匹配，分布式表示分支学习语义匹配，两个分支联合训练并共同产生网页相关性分数 | 两分支共享训练不等于所有输入双向交互，网页排名实验与商品个性化排序分别设任务。 | 9.2.3.7 |
| S20 | [monoBERT：Passage Re-ranking with BERT](https://arxiv.org/abs/1901.04085) | 作者公开稿，2019 | 独立编码压缩了查询与文档的细节关系，已有候选可以使用更精细的联合计算。 把查询与候选片段拼入BERT，利用联合表示的分类头学习相关性标签，逐候选恢复分数并重排；BERT机制回指NLP | 候选池和文本截断限定能改善的范围，分类输出是否校准需要另测；该模型不直接完成全目录检索。 | 9.2.3.8 |
| S21 | [monoT5：Document Ranking with a Pretrained Sequence-to-Sequence Model](https://aclanthology.org/2020.findings-emnlp.63/) | Findings of EMNLP 2020 | 文本生成模型服务排序时，需要明确输出怎样成为可比较的相关性分数。 把查询与文档输入T5，以相关／不相关目标词元监督生成，再从指定目标词元的logit归一化得到重排分数；通用生成模型回指NLP | 标签词选择、长文截断与候选池影响结论；生成相关性标签与生成文档标识具有不同用途。 | 9.2.3.9 |
| S22 | [RankT5: Fine-Tuning T5 for Text Ranking with Ranking Losses](https://research.google/pubs/rankt5-fine-tuning-t5-for-text-ranking-with-ranking-losses/) | SIGIR 2023；作者机构正式出版页 | 相关性分类损失与最终比较候选次序的目标存在差异。 T5编码器或编码器—解码器直接输出查询—文档分数，用成对或列表排序损失微调，连接4.2.2的比较目标与查询分组 | 列表损失学习次序，并不联合决定展示素材或整页布局；跨领域效果须固定监督与评价集合。 | 9.2.3.10 |
| S23 | [RankZephyr: Effective and Robust Zero-Shot Listwise Reranking is a Breeze!](https://arxiv.org/abs/2312.02724) | 作者公开稿，2023；本次未核验正式发表 | 闭源列表重排难以稳定复现，也需要减少输入次序对结果的影响。 以教师生成的候选次序分阶段适应开放语言模型，并改变训练窗口和输入排列，服务时用列表提示与滑动窗口恢复完整次序 | 教师次序是训练依据，仍须用独立相关性判断评价；生成编号需检查重复、遗漏与允许候选范围。 | 9.2.3.11 |
| S24 | [Rank1: Test-Time Compute for Reranking in Information Retrieval](https://arxiv.org/abs/2502.18418) | 作者公开稿，2025 | 复杂限定条件可能需要更多推理，固定的一步打分难以解释计算增加的作用。 用查询—片段的教师推理轨迹蒸馏相关性判断，服务时生成推理及判定，为既有候选提供重排依据；推理与蒸馏机制回指NLP | 可读推理不能独自证明理由忠实或事实正确，计算增加须同时记录时延、预算及独立相关性结果。 | 9.2.3.12 |

## 行为理解、语义匹配与缺失信息补充

长历史选择、语义与关系匹配、少样本适应具有不同输入条件；序列辅助表示学习完整放在召回训练中。本表记录原始任务及主要讲解位置。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| R76 | [ETA：End-to-End User Behavior Retrieval in Click-Through Rate Prediction Model](https://arxiv.org/abs/2108.04468) | 2021 作者预印本；本次未核验到正式会议出版。作者稿中的 Conference '17 与占位 DOI 是模板信息，不作出版依据。 | 在候选相关的长历史 CTR 预测中，检索用的表示与最终点击目标可能不同步；全量候选注意力的计算又随历史长度增长。 用当前 CTR 网络的物品向量构造 SimHash 指纹，在长历史中按汉明距离选取相关行为；在选取的行为上计算候选注意力，与短期兴趣及其他特征联合预估点击。共享表示随 CTR 目标训练，哈希检索替代大量浮点相似度计算。 | 端到端是共享表示与 CTR 训练的衔接，不能改写成离散哈希和 top-k 选择全程可微；候选相关检索仍可能漏掉相关历史，扫描、缓存及指纹更新也有成本。 | 2.2.1.13 |
| R77 | [SDIM：Sampling Is All You Need on Modeling Long-Term User Behaviors for CTR Prediction](https://arxiv.org/abs/2205.10249) | CIKM 2022；会议状态由作者 PDF 首页核验，稿中占位 DOI 不登记。 | 候选逐一计算长历史注意力，即使先选 top-k，在线候选规模增大后仍昂贵；需要更便宜的候选相关聚合。 多轮随机投影将候选与历史编码成 SimHash 签名，直接聚合与候选落入同一桶的行为。相似行为有更高碰撞概率，以采样方式近似相似度加权兴趣；行为序列编码与主预测路径分离，并维护桶内聚合表示。 | 与 ETA 的按距离选择后再注意力不同，SDIM 直接聚合同桶行为；哈希宽度和轮数影响覆盖与误差。解耦将一部分计算移到另一条路径，并未消除计算或保证等价于全量 softmax 注意力。 | 2.2.1.14 |
| R78 | [PinnerFormer: Sequence Modeling for User Representation at Pinterest](https://arxiv.org/abs/2205.04507) | KDD 2022；作者 PDF 首页核验。 | 只预测下一次动作容易过度关注近期行为，且为每次请求更新用户表示的服务代价较高；需要可离线更新、能预测较长窗口兴趣的用户向量。 因果 Transformer 编码历史，训练时在多个历史位置构造面向未来窗口中多次正反馈的 dense all-action 目标，将用户向量与未来参与的物品对齐。用户向量可离线批量更新，供多个下游模型使用。 | 未来窗口偏好预测属于表示目标的扩展，不等于学习推荐动作如何改变未来行为，也不证明长期留存的因果增益。离线更新仍可能落后于实时需求，宜与 TransAct 对照。 | 2.2.1.15 |
| R79 | [TWIN-V2：TWIN V2: Scaling Ultra-Long User Behavior Sequence Modeling for Enhanced CTR Prediction at Kuaishou](https://arxiv.org/abs/2407.16357) | CIKM 2024；作者全文首页核验，DOI 10.1145/3627673.3680030。 | TWIN 的一致检索与精细注意力仍受原始行为规模限制；用户生命周期历史达到极长规模时，直接保留所有记录难以服务。 离线按播放完成情况划分历史，再进行限制簇大小的层次聚类，每个簇形成虚拟物品；在线检索相关簇并进行精细建模。两阶段共享簇级注意机制，并以簇大小调整注意力。 | 簇表示不能完整保留簇内事件顺序及细粒度区别；压缩粒度、簇更新与服务成本均依赖应用。不能把平台实验中的超长规模写成普遍需求或无损压缩保证。 | 2.2.1.16 |
| R80 | [LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders](https://arxiv.org/abs/2505.04421) | RecSys 2025；作者版本与 journal reference 核验，DOI 10.1145/3705328.3748065。 | 依靠检索或离线聚类缩短历史可能提前丢失信息；直接扩大 Transformer 上下文又受注意力和训练服务成本限制。 把候选与全局特征组织为全局词元，以邻近 TokenMerge 和局部 InnerTrans 压缩序列；第一层通过交叉因果注意力让少量查询读取较长历史，后续对缩短后的序列使用因果掩码编码，限制历史信息读取方向。配合训练与服务缓存，延长可处理历史。 | 相邻合并与局部处理会改变信息粒度；序列变短但宽度、前馈与缓存仍有开销。缓存依赖注意力可见性与模型更新条件，不能写成任意双向候选交互均可复用。 | 2.2.1.17 |
| R84 | [KGAT: Knowledge Graph Attention Network for Recommendation](https://arxiv.org/abs/1905.07854) | KDD 2019；作者全文首页核验，DOI 10.1145/3292500.3330989。 | 用户—物品交互仅给出协同邻域，难以利用物品与作者、品牌、类别等实体的多跳关系匹配用户偏好。 构造包含协同交互和知识关系的统一图；学习关系投影与实体表示，用关系相关注意力传播多跳邻居，再组合各层表示。交替使用知识图谱三元组目标和 BPR 协同推荐目标训练。 | 原任务是联合用户—物品推荐评分，不能改写为信息抽取。需要实体链接及可用关系；注意力权重不等于因果解释，未建图对象也不会自动具备可用表示。 | 2.2.3.2 |
| R85 | [LATTICE：Mining Latent Structures for Multimedia Recommendation](https://arxiv.org/abs/2104.09036) | ACM Multimedia 2021；作者全文首页核验，DOI 10.1145/3474085.3475259。 | 协同图缺少物品之间的内容联系，直接融合多模态向量又可能忽略内容揭示的物品邻域。 按各模态相似度构造稀疏物品图，学习特征投影以更新关系，混合初始图与学习图，再以模态权重融合。沿物品图传播 ID 表示，将所得表示加入协同模型的物品表示，以 BPR 联合训练。 | 内容用于构图，传播的主体是物品 ID 表示，不能写成直接传播所有原始图文内容。相似边不是经核实的互补或替代关系；无交互目录节点实验不等于无限新物品的无训练归纳能力。 | 2.2.3.3 |
| R86 | [Recformer：Text Is All You Need: Learning Language Representations for Sequential Recommendation](https://arxiv.org/abs/2305.13731) | KDD 2023；作者预印本 accepted 信息核验。 | 物品 ID 表示跨目录迁移困难，冷物品缺乏交互；需要让文本属性直接成为历史和对象共享的匹配依据。 把物品键值属性组织为文本序列，用词元、类型、词元位置和物品位置区分结构；Longformer 编码用户历史及单个物品，以掩码语言任务和物品对比任务预训练，再微调下一物品匹配并维护目录表示。 | 已知历史的双向编码不允许访问未来事件；相似度匹配输出目录对象，不是生成任意物品名称。文本质量、目录文本与推荐语义对齐仍限制冷启动和迁移。 | 2.2.3.4 |
| R87 | [HLLM: Enhancing Sequential Recommendations via Hierarchical Large Language Models for Item and User Modeling](https://arxiv.org/abs/2409.12740) | 2024 作者预印本；本次未核验到原工作正式会议出版。与 2025 HLLM-Creator 是不同任务、不同论文。 | 将全部物品文本拼入一个用户编码器成本高，物品语义与用户历史又处在不同层次；需要分别利用语言模型先验。 Item LLM 用物品文本及专用词元得到物品向量；User LLM 以物品向量序列替代词元嵌入输入，聚合用户历史。训练以实际下一物品和随机负例进行 InfoNCE 对齐；点击判别比较候选参与用户编码的早融合与独立编码后的后融合。 | 主序列任务是向量预测与目录匹配，不是文本或语义 ID 生成。物品向量缓存须与编码器冻结或版本同步配合；不能将原 HLLM 推断为已具备创意生成能力。 | 2.2.3.5 |
| R88 | [KAR：Towards Open-World Recommendation with Knowledge Augmentation from Large Language Models](https://arxiv.org/abs/2306.10933) | RecSys 2024；正式会议 accepted contributions 页面核验；首稿 2023。 | 有限行为和物品描述难以覆盖开放领域中的偏好因素，语言模型的文本知识又不能直接接入传统推荐表示。 按领域因素组织提示，在离线阶段生成用户推理和物品知识并进行文本编码；混合共享与任务专属专家的适配器把文本表示转成推荐特征，与下游预测目标联合训练。 | LLM 生成的物品事实需核验，推理文本也不是用户真实动机的观测或因果证据；原任务是在知识增广后预估响应，不是直接用语言回答替代候选资格与推荐验证。 | 2.3.1.2 |
| R89 | [MeLU: Meta-Learned User Preference Estimator for Cold-Start Recommendation](https://arxiv.org/abs/1908.00413) | KDD 2019；作者论文核验。 | 新用户只有少量反馈，独立训练用户偏好模型容易过拟合；需要从已有用户学习可快速适应的偏好估计器。 把每个已有用户作为元学习任务，以其支持集局部更新预测层，在查询集上衡量适应后的误差并更新共享初始化。局部适应保持用户与物品嵌入部分不变；另外研究用于获取反馈的证据候选选择。 | 少样本适应要求获得反馈标签，不能表述为无行为用户也可完成同样的更新；效果依赖元训练用户与新用户任务分布及可用属性。它改变学习初始化，不替代曝光探索策略。 | 2.3.1.3 |

## 候选访问、标识生成与表示训练补充

目录访问、标识生成和训练信号是不同坐标。PinRec生成向量后访问近邻目录；RPG并行预测一个物品的代码；OneRec-V2按原文单目标物品主体登记。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| R59 | [TDM：Learning Tree-based Deep Model for Recommender Systems](https://arxiv.org/abs/1801.02294) | KDD 2018；https://www.kdd.org/kdd2018/accepted-papers/view/learning-tree-based-deep-model-for-recommender-systems 官方论文页核验 | 复杂用户—对象交互不能分解成独立向量点积时，怎样避免全目录逐物品打分。输入用户与历史，输出树叶物品候选。 以树组织物品，用用户—节点深层模型从根到叶选择高分节点，逐层beam搜索；分层样本训练并可学习更匹配兴趣分布的树。 | 固定分支／beam预算下约对数深度访问，并非任意搜索规模都对数；路径误删造成候选损失，不保证全目录真实top-k。 | 3.2.1.11 |
| R62 | [LC-Rec：Adapting Large Language Models by Integrating Collaborative Semantics for Recommendation](https://arxiv.org/abs/2311.09049) | ICDE 2024；初稿2023，作者稿v4确认接收 | 语言模型词汇与协同物品标识不一致，单独预测物品代码不足以接入语言知识。原任务为全目录下一物品推荐。 以向量量化及均匀语义映射构造无冲突标识；用下一物品预测、标识与文本互译、非对称预测及意图/偏好任务共同微调LLaMA，推理受目录标识约束。 | 语义/协同对齐不同于用户价值的偏好对齐；辅助意图数据包含合成信号，仍须核验预测时可用信息。标识更新与目录约束独立管理。 | 3.2.2.4 |
| R63 | [LETTER：Learnable Item Tokenization for Generative Recommendation](https://arxiv.org/abs/2405.07314) | CIKM 2024；作者稿v3 | 仅重构内容的物品编码可能丢协同信号并出现分配集中，导致生成器难以学习偏好。 RQ-VAE语义重构、量化表示与协同表示的对比对齐、代码分配多样性正则；生成训练另用温度控制的ranking-guided token loss，Trie限定合法物品标识。 | 代码使用多样性不是展示列表多样性；温度目标的token层解释不能无条件外推为所有真实物品排序指标提升。 | 3.2.2.5 |
| R64 | [SEATER：Generative Retrieval with Semantic Tree-Structured Identifiers and Contrastive Learning](https://ai.ruc.edu.cn/uploads/20241223/6187e0ab7717b2651935eb098d67c58b.pdf) | SIGIR-AP 2024；初稿2023；RUC正式作者稿与DOI确认 | 生成检索中代码层次含义混乱、路径长度不均，候选寻址结构需与偏好关系一致。 对协同向量递归约束k-means形成平衡k叉树，各节点使用唯一标识；encoder-decoder学习路径生成，InfoNCE和triplet loss对齐层次位置与相似路径顺序。 | 其叶标识/节点嵌入随目录规模增长，不能套用RQ共享小码本的存储结论；建树和目录变更代价须单独报告。 | 3.2.2.6 |
| R65 | [IDGenRec: LLM-RecSys Alignment with Textual ID Learning](https://arxiv.org/abs/2403.19021) | SIGIR 2024；作者稿v2确认 | 原子数字ID缺少语言含义，完整标题冗长且不唯一；怎样学习简洁且能映射物品的文本标识。 T5式ID生成器与推荐生成器交替训练，固定推荐器时以软词嵌入代理离散ID梯度；多样生成维护唯一映射，Trie约束推荐解码。 | 跨域零样本结果限已报告领域；唯一ID、目录解析和版本一致性仍是必要外部状态，不等于开放世界名称生成。 | 3.2.2.7 |
| R66 | [TransRec：Bridging Items and Language: A Transition Paradigm for Large Language Model-Based Recommendation](https://arxiv.org/abs/2310.06491) | KDD 2024；会议题名为A Multi-facet Paradigm to Bridge Large Language Model and Recommendation，最新作者稿改题 | 物品唯一身份与描述语义难由一种标识同时承载，开放文本生成又会出现目录外结果。 多方面指令微调；FM-index限定合法子串并允许从标识任意位置开始，按片段覆盖、频率校正和跨方面聚合计算实际物品分数。 | 该FM-index是压缩文本索引，和第四章因子分解机FM无关；子串有效不保证最终商品满足业务资格，复杂查询相关性另检验。 | 3.2.2.8 |
| R67 | [ETEGRec：Generative Recommender with End-to-End Learnable Item Tokenization](https://arxiv.org/abs/2409.05546) | SIGIR 2025 Research Track；初稿2024，作者稿v3确认 | 预先训练并冻结的物品量化器不能根据推荐目标调整代码分配。 双encoder-decoder分别用于RQ tokenizer和生成器；sequence-item token distribution对齐及preference-semantic InfoNCE连接两者，交替优化，量化器收敛后冻结。 | 这里的端到端范围是编码器与生成器，不是召回排序展示全流程；代码缓存与目录映射随训练版本协调。 | 3.2.2.9 |
| R68 | [RPG：Generating Long Semantic IDs in Parallel for Recommendation](https://arxiv.org/abs/2506.05781) | KDD 2025；作者稿评论与作者发布确认 | 一个物品含较长代码时逐token束搜索增加前向次数，短代码又限制表征。 OPQ将向量分解为不同子空间代码，聚合每个历史物品的代码嵌入，多个输出头并行预测目标代码位；基于合法ID相似图迭代搜索候选。 | 并行的是一个物品的代码位，不是同时决定多物品展示列表；条件独立是建模假设，图构建、访问和候选数量仍影响真实成本。 | 3.2.2.10 |
| R69 | [LIGER：Unifying Generative and Dense Retrieval for Sequential Recommendation](https://openreview.net/pdf?id=jxdnFIsjCb) | TMLR 2025-06；初稿2024；OpenReview正式PDF确认 | 生成ID减少目录比较但可能难以产生新物品；稠密内容匹配保留细粒度信息但检索成本不同。 训练联合SID next-token目标和编码器输出与目标文本向量的余弦softmax目标；推理束搜索产生候选，与冷启动集合并集，再用文本向量相似度排序。 | 论文明确假定冷启动物品较少并可直接并入；保留O(N)固定文本向量，不能说彻底消除全目录存储或无条件解决大规模目录更新。 | 3.2.2.11 |
| R70 | [COBRA：Sparse Meets Dense: Unified Generative Recommendations with Cascaded Sparse-Dense Representations](https://proceedings.neurips.cc/paper_files/paper/2025/hash/86ba836d4c5dd859d795a172911745e2-Abstract-Conference.html) | NeurIPS 2025 Main Conference；正式论文集确认 | 离散代码压缩可能损失细粒度偏好，纯稠密检索难同时保留粗粒度语义寻址与生成接口。 统一Transformer交替处理SID和dense tokens，学习P(SID／history)及条件dense matching；生成稀疏分支后在分支中向量细检索，融合束概率及近邻分数。 | 结合的是两种候选表示与访问方法，未替代资格、完整精排和广告竞价；BeamFusion参数对召回覆盖和多样性影响在相同预算下比较。 | 3.2.2.12 |
| R71 | [PinRec: Unified Generative Retrieval for Pinterest Recommender Systems](https://arxiv.org/abs/2504.10507) | KDD 2026；初稿2025，最新v7；Pinterest Labs及作者稿正式首部确认 | 跨搜索/信息流/相关对象入口的异质历史、不同反馈目标与多步兴趣变化，难由各自单步召回器统一利用。 decoder-only在跨入口轨迹预训练，再以各入口曝光日志微调；conditioned output head预测目标行为向量，抽一目标向量回输形成自回归，多向量预算与合并后访问ANN。 | 作者最新正文明确仅作Candidate Generator，随后精排混排照旧；这里budget是候选名额，不是广告金额；不同条件控制不等于硬保证业务结果。 | 3.2.1.12 |
| R72 | [PLUM: Adapting Pre-trained Language Models for Industrial-scale Generative Recommendations](https://arxiv.org/abs/2510.07784) | WWW 2026 Industry Track；初稿2025；会议官网接收及正式日程确认 | 语言预训练知识怎样接入推荐SID，而不只把从头训练的行为Transformer叫作LLM推荐。 SID-v2结合多模态、协同共现、多分辨率码本与渐进遮掩；扩展LLM词汇并在SID-文本-历史及普通文本上继续预训练，召回SFT以反馈权重训练目标SID。 | LLM预训练与领域CPT分别消融；生成多个下一物品候选不同于会话列表联合生成，仍可能出现无效SID与映射碰撞；全成本包含CPT。 | 3.2.2.13 |
| R73 | [OneRec-V2 Technical Report](https://arxiv.org/abs/2508.20900) | 2025技术报告；截至2026-10-05本次仅核验到arXiv，不臆造会议 | 生成式推荐反复编码长历史的计算分配，以及仅依赖奖励模型对齐的反馈局限。 Context Processor直接产出共享KV，Lazy Decoder通过cross-attention读取静态context、因果self-attention处理目标SID；时长分桶的用户播放分位数奖励，GBPO以动态概率分母限制梯度，混合真实生成曝光与传统日志。 | 不能因V1是session-wise而把V2单物品主体写成完整列表生成；传统pipeline日志无法取得真实策略概率，原文以当前概率代理，不拥有一般OPE无偏性质；真实播放代理不等于长期价值。 | 3.2.2.14 |
| R81 | [S3-Rec：S^3-Rec: Self-Supervised Learning for Sequential Recommendation with Mutual Information Maximization](https://arxiv.org/abs/2008.07873) | CIKM 2020；作者 PDF 首页核验，DOI 10.1145/3340531.3411954。 | 稀疏下一物品反馈不能充分训练序列表示，而已有历史中还包含物品、属性和片段间的关联。 设计物品—属性、上下文—被遮蔽物品、上下文—被遮蔽属性和序列—片段四类关联任务，以互信息最大化思想构造自监督预训练。双向预训练后，用初始化后的单向序列编码器微调下一物品推荐。 | 属性是额外输入，不能称为完全无附加信息；自监督重复利用已有证据，不生成真实新用户反馈。预训练双向不意味着线上可以访问未来行为，微调及推理必须遵守可用时间。 | 3.4.1.3 |
| R82 | [CL4SRec：Contrastive Learning for Sequential Recommendation](https://arxiv.org/abs/2010.14395) | ICDE 2022，作者主页正式条目核验；首稿 arXiv 2020，v2 2021。DOI 10.1109/ICDE53745.2022.00099。 | 单一下一物品监督难以在稀疏数据下得到稳定序列表示；同一已知序列可以产生多个视图提供辅助约束。 对历史做裁剪、遮蔽或重排，用共享序列编码器编码；对比目标拉近同序列视图、区分其他序列，与下一物品损失联合训练。 | 增强不天然保持用户意图，裁剪可能删掉关键行为，重排可能改变时序含义；批内其他序列也未必都是偏好负例。主讲数据增强的假设，而非把所有扰动解释为等价历史。 | 3.4.1.4 |
| R83 | [DuoRec：Contrastive Learning for Representation Degeneration Problem in Sequential Recommendation](https://arxiv.org/abs/2110.05730) | WSDM 2022；作者全文首页核验，DOI 10.1145/3488560.3498433。 | 下一物品模型的物品表示可能集中在狭窄方向，影响区分能力；序列裁剪等增强又可能改变原始偏好。 同序列用不同 dropout 生成模型层视图，并将训练标签中具有相同下一目标物品的历史作为额外正例；联合推荐和对比正则化改善序列及物品共享空间的分布，同目标序列不作为负例。 | 相同下一目标物品是正例采样准则，不证明整段历史意图相同；目标标签只在训练可用，不能在推理时访问。几何改善与所有用户群体的偏好识别不可等同。 | 3.4.1.5 |

## 特征评分、模块组合与阶段衔接补充

字段计算、分支融合、评分骨干和跨阶段共享分别核验。场景差异作为评分使用条件，区别于时间漂移和预测目标；模型名字中的统一不作为完整流程整合的证据。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| R46 | [PNN：Product-based Neural Networks for User Response Prediction](https://arxiv.org/abs/1611.00144) | ICDM 2016；会议论文，DOI:10.1109/ICDM.2016.0151；与2018 TOIS扩展稿区分 | 多字段类别特征经过嵌入后，怎样显式引入乘性交互再学习复杂响应。原任务为广告点击预测，输入用户、广告、发布者字段，输出点击概率。 嵌入层、内积或外积乘积层、全连接层及sigmoid；点击交叉熵训练。外积实现有叠加降本而非完整保留每对外积。 | 原研究是响应评分，不是可分解的全目录检索；高阶能力不保证识别任意独立高阶组合。 | 4.3.1.1.10 |
| R47 | [NFM：Neural Factorization Machines for Sparse Predictive Analytics](https://arxiv.org/abs/1708.05027) | SIGIR 2017；[作者原文](https://hexiangnan.github.io/papers/sigir17-nfm.pdf)及作者发表记录核验 | FM二阶交互汇总以后，怎样学习非线性响应而无需逐对保留交互。原论文评估上下文预测与个性化标签推荐的回归目标。 Bi-Interaction pooling把非零特征嵌入的逐元素二阶乘积求和，保留为潜在维度向量，接非线性隐层与线性项；原论文平方误差训练。 | 不是原生CTR论文；若用sigmoid和交叉熵迁移，要明确改变任务头与标签；汇总会丢失具体交互对身份。 | 4.3.1.1.11 |
| R48 | [AFM：Attentional Factorization Machines: Learning the Weight of Feature Interactions via Attention Networks](https://www.ijcai.org/proceedings/2017/435) | IJCAI 2017；正式论文页及全文 | 二阶交互同等汇总会混入无用组合，怎样为每个交互赋权。原文是稀疏监督回归，非直接CTR应用。 对嵌入两两逐元素乘积使用注意网络和softmax加权，投影为输出；保留线性项。 | 显式交互对象是特征对；非线性注意赋权不能直接视为已识别的高阶交互，注意权重也不是因果证据。 | 4.3.1.1.12 |
| R49 | [FiBiNET: Combining Feature Importance and Bilinear feature Interaction for Click-Through Rate Prediction](https://arxiv.org/abs/1905.09433) | RecSys 2019；arXiv Journal reference与DOI:10.1145/3298689.3347043核验 | 字段的重要性与字段对的变换不相同，怎样联合选择字段并计算细粒度交互。输入稀疏字段，输出CTR。 SENET先压缩各字段、生成字段权重，分别在原嵌入和重加权嵌入上做双线性交互，浅／深版本输出响应。 | 字段赋权与AFM交互对赋权不同；不同共享范围的双线性矩阵有不同参数代价。 | 4.3.1.1.13 |
| R50 | [Fi-GNN: Modeling Feature Interactions via Graph Neural Networks for CTR Prediction](https://arxiv.org/abs/1910.05552v1) | CIKM 2019；作者稿v1 comments核验；v2(2020)方法实现有变化，教材以会议版为准 | 字段拼接缺乏明确关系结构，怎样把不同字段的交互表达为消息传递。输入一个样本的多字段表示，输出CTR。 字段为节点，字段间边承担交互；学习边权、边变换与节点更新，再聚合点击预测。 | 这是单个样本内的特征字段图，与用户—物品协同图、会话转移图不同；注意边权并非因果关系。 | 4.3.1.1.14 |
| R51 | [DLRM：Deep Learning Recommendation Model for Personalization and Recommendation Systems](https://arxiv.org/abs/1906.00091) | 2019，arXiv作者预印本；不凭后续系统基准用途追认成会议论文 | 稀疏类别与连续数值怎样进入统一响应评分器，同时便于系统比较。输入多字段稀疏与稠密特征，输出响应概率。 类别嵌入、连续特征bottom MLP、向量两两点积；交互与稠密表示送top MLP和sigmoid；原文还分开嵌入并行与稠密数据并行。 | 显式两两交互不限制最终MLP只含二阶作用；仅应用计算主讲此处，并行训练机制回指系统卷。 | 4.3.1.1.15 |
| R52 | [MaskNet: Introducing Feature-Wise Multiplication to CTR Ranking Models by Instance-Guided Mask](https://arxiv.org/abs/2102.07619) | 2021，arXiv预印本；仅核验到作者稿 | MLP的加性映射难有效学习部分乘性组合，怎样按请求生成逐维掩码。输入用户、对象、情境字段，输出CTR。 输入引导掩码与嵌入或隐藏层逐元素相乘，MaskBlock结合层归一化、掩码与前馈层，串联或并联组成评分。 | 掩码是连续软缩放，通常不表示稀疏计算路由或被屏蔽字段真实不重要；不是缺失标签修正。 | 4.3.1.1.16 |
| R53 | [FinalMLP: An Enhanced Two-Stream MLP Model for CTR Prediction](https://arxiv.org/abs/2304.00902) | AAAI 2023；arXiv comments核验 | 双分支评分一定需要两种不同网络吗，怎样形成互补表示及有效融合。输入类别／多值／数值字段，输出CTR。 双MLP分支；上下文条件下的分支特征门控；分支输出经多头双线性融合，配线性与交互项；交叉熵训练。 | 主讲完整评分器组织而非“第三种输入信息”；不证明所有任务里简单MLP足够，分支输入也可共享特征。 | 4.3.2.1.1 |
| R54 | [Wukong: Towards a Scaling Law for Large-Scale Recommendation](https://proceedings.mlr.press/v235/zhang24ao.html) | ICML 2024；正式PMLR论文页核验；作者arXiv:2403.02545v4 | 扩大嵌入表之外，怎样随计算预算扩展评分网络的交互容量。输入字段向量，输出响应预测。 每层FMB计算二阶向量交互并经MLP转为新嵌入；LCB保留压缩后的低阶表示，两路拼接并加残差与归一化，堆叠后预测。 | 研究稠密交互容量的扩展，不统一行为序列与阶段；随层数的交互阶直觉不是实际数据上的无限收益保证。 | 4.3.1.1.17 |
| R55 | [Hiformer: Heterogeneous Feature Interactions Learning with Transformers for Recommender Systems](https://arxiv.org/abs/2311.05884) | 2023，arXiv预印本；作者Ed Chi发表页仍列预印本；不误标WWW 2024；区别医学图像HiFormer和2026 HyFormer | 用户、对象、情境字段不同，统一投影参数能否充分刻画交互；怎样控制部署代价。输入类别与稠密字段、任务token，输出任务响应。 异质注意层按字段设置投影和FFN，Hiformer复合投影进一步考虑字段对；低秩近似及末层只保留任务查询降低成本。 | 特征交互模型，不是原始历史长序列编码器；模型版本HeteroAtt与Hiformer复合投影须区分，低秩收益不是无损定理。 | 4.3.1.1.18 |
| R56 | [InterFormer: Effective Heterogeneous Interaction Learning for Click-Through Rate Prediction](https://arxiv.org/abs/2411.09852) | CIKM 2025；大会程序核验https://www.cikm2025.org/program/conference-program；作者初稿2024，v4正式标题去掉Towards | 先压缩历史再拼接字段会过早损失信息，单向条件化也没有让行为反过来改变字段交互。输入非序列字段和行为序列，输出候选CTR。 Interaction Arch与Sequence Arch保留各自粒度，每层Cross Arch交换选择性摘要；字段摘要通过个性化FFN／注意作用于序列，历史CLS／PMA／近期token摘要反作用字段。 | 仍保留分离的字段交互与序列模块，通过双向桥接交错学习，不是所有原token共用单Transformer；不统一召回排序。 | 4.3.2.1.2 |
| R57 | [STAR：One Model to Serve All: Star Topology Adaptive Recommender for Multi-Domain CTR Prediction](https://arxiv.org/abs/2101.11427) | CIKM 2021；https://www.cikm2021.org/accepted-papers 官方名单核验 | 多个业务场景既共享用户和物品又有不同分布，怎样共享数据同时避免一个全共享评分器失配。输入字段与domain ID，输出该场景CTR。 共享中心参数与场景专属参数逐元素相乘、偏置相加；Partitioned Normalization保留场景统计及全局／场景尺度，auxiliary network等。 | 需要已知场景归属；不同场景不是不同预测目标，未知场景与时变漂移不自动解决。 | 4.3.4.4.1 |
| R58 | [PEPNet: Parameter and Embedding Personalized Network for Infusing with Personalized Prior Information](https://arxiv.org/abs/2302.01115) | KDD 2023；作者稿comments与正式DOI:10.1145/3580305.3599884 | 同一场景内不同用户和对象对多个反馈目标也存在差异，怎样以先验信息条件化共享评分器。输入用户／对象／作者先验、场景字段，输出多任务概率。 EPNet基于场景先验缩放共享嵌入；PPNet基于用户／对象／作者先验对各任务隐层单元连续门控，含stop-gradient接口；联合BCE。 | PPNet通过隐藏贡献缩放产生有效参数适配，并非每个用户独立生成完整网络权重；条件先验和标签决定可学习差异。 | 4.3.4.4.2 |
| R60 | [IntTower: the Next Generation of Two-Tower Model for Pre-Ranking System](https://arxiv.org/abs/2210.09890) | CIKM 2022；作者稿comments及全文DOI:10.1145/3511808.3557072核验 | 粗排双塔复用物品编码但交互太晚，怎样在候选级打分里提高表达并保留缓存。输入用户及已召回候选字段，输出粗排CTR分数。 Light-SE字段选择；各用户层与物品末层多头表示做sum-of-max相似度并跨层求和；CIR对比正则；物品表示预存。 | sum-of-max及多层交互不自动归约成普通单向量点积ANN；研究既有候选粗排，未统一各阶段训练。 | 4.3.4.2.2 |
| R61 | [HCCP：A Hybrid Cross-Stage Coordination Pre-ranking Model for Online Recommendation Systems](https://arxiv.org/abs/2502.10284) | WWW Companion 2025，621–630；DOI:10.1145/3701716.3715208；作者稿正文明确WWW Companion；HTML另混入SPEC模板字样，不采纳模板名称 | 粗排只拟合精排已选候选会继承选择偏差，怎样兼顾下游一致性与上游长尾候选。输入全链路候选和部分曝光反馈，输出粗排响应／顺序。 采样精排未曝光序列、被粗排过滤候选、批内和目录负样本；曝光反馈重排教师序列；ListMLE全局／局部一致性＋Margin InfoNCE及响应损失。 | 未曝光候选的反馈未知，教师次序和难度先验不是无偏真实标签；原方法仍保留各阶段且可移植粗排器。 | 4.3.4.2.3 |
| R74 | [UniR²：Unifying Generative Recall and Multi-Objective Ranking in a Single Decoder-Only Sequence](https://arxiv.org/abs/2607.24439) | 2026-07-27预印本v1；截至2026-10-05仅核验到作者稿 | 召回/排序交接丢失生成路径并重复用户计算，且生成与多目标排名可见信息和训练梯度不同。 dual-query prefix-causal attention为生成查询保留历史及SID前缀，为排名查询保留画像/完整SID轨迹/候选字段而丢弃长历史；共享基础注意权重，独立FFN、ranking LoRA和stop-gradient隔离更新。 | 统一骨干不意味一项联合损失更新所有参数；排序仍需候选字段和任务头，也不生成展示列表。长时线上测试不能自动证明长期策略价值。 | 4.3.4.2.4 |

## 列表决策、多目标与策略学习补充

给定候选的整组选择、偏好权重下的排序学习和大目录策略采样分别说明；长期效果不能仅凭策略梯度或未来标签证明。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| R44 | [PRM：Personalized Re-ranking for Recommendation](https://arxiv.org/abs/1904.06813) | RecSys 2019；作者全文核验 | 逐对象评分没有直接利用整组候选的关系与用户差异。 已有候选特征与个性化表示进入Transformer，自注意力编码候选间上下文，再从各对象输出列表相关得分并学习反馈 | 候选关系参与评分不等同所有多样性与展示约束已被满足，训练日志的曝光条件由5.3及第8章检验。 | 5.2.1.7 |
| R45 | [Seq2Slate: Re-ranking and Slate Optimization with RNNs](https://research.google/pubs/seq2slate-re-ranking-and-slate-optimization-with-rnns/) | 作者公开稿，2018；修订2019 | 整组内容的选择需要让后续对象知道已选了什么。 在既有候选上使用序列编码与指针式解码，逐步选择下一对象，以点击等弱监督学习列表策略，已选对象约束后续选择 | 它在给定候选内构造列表，与OneRec从目录标识生成的访问范围不同；列表反馈及用户选择模型限定效果解释。 | 5.2.1.8 |
| R75 | [NAR4Rec：Non-autoregressive Generative Models for Reranking Recommendation](https://arxiv.org/abs/2402.06871) | KDD 2024；作者稿v6确认 | 从既有候选生成排列时逐物品解码延迟高，独立并行分布又易缺少整组协调。 候选编码器与位置编码器形成位置-候选匹配概率矩阵；高效用序列likelihood、低效用unlikelihood训练；contrastive decoding利用已选对象关系去重/调整，列表evaluator挑选。 | 非自回归指概率矩阵并行计算，最终对比解码仍依赖已选择对象；不作全目录召回，评价器估计不能当真实整组价值。 | 5.2.1.9 |
| R90 | [PE-LTR：A Pareto-Efficient Algorithm for Multiple Objective Optimization in E-Commerce Recommendation](https://yongfeng.me/attach/lin-recsys2019.pdf) | RecSys 2019；作者 PDF 首页核验，DOI 10.1145/3298689.3346998。 | 电商排序同时追求点击、购买或 GMV，固定损失权重难以应对目标梯度冲突，也难以观察不同取舍方案。 依据多个目标的梯度自适应确定非负且归一化的标量化权重，对权重设下界限制其偏好范围，求解加权梯度范数子问题，再与模型参数更新交替进行。比较不同权重下界得到的取舍方案。 | 下界约束的是权重，不是 CTR、GMV 等业务指标的可行性底线。论文梯度条件对应 Pareto 驻点，不能在一般非凸模型中无条件声称全局 Pareto 最优；多目标预测头共享也不是此算法要点。 | 6.2.1.1 |
| R91 | [Top-K REINFORCE：Top-K Off-Policy Correction for a REINFORCE Recommender System](https://arxiv.org/abs/1812.02353) | WSDM 2019；作者 PDF 首页核验，DOI 10.1145/3289600.3290999。 | 连续推荐希望优化累计参与收益，但数据来自历史多个策略；候选空间很大，系统又一次提供列表而非单一动作。 循环状态表示支撑物品策略；另学习历史行为策略概率，以离策略加权修正 REINFORCE。独立抽取 K 次物品再去重，在列表收益可加假设下，用物品被包含的概率及其导数修正梯度。 | 独立有放回采样后去重，列表大小可变化，不是直接枚举所有定长有序列表。修正采用近似与估计行为概率，覆盖不足和权重截断仍带来误差；单项收益相加并不适用于任意列表交互。 | 7.2.2.2 |

## 广告少样本、延迟响应与周期控制补充

新广告初始化、观测时间修正和投放控制对应不同任务。生成轨迹、代理价值与实际金额约束分别判断；仅核验到作者稿的近期工作保留预印本状态。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| A18 | [DEFER：Real Negatives Matter: Continuous Training with Real Negatives for Delayed Feedback Modeling](https://arxiv.org/abs/2104.14121) | KDD 2021；作者全文核验 | 延迟正例回流后，重复训练仍可能缺少已经确认的负例。 将成熟真实负例也送回持续训练，用重要性加权纠正重复及观测机制带来的分布变化，利用更确定的标签学习CVR | 真实负例依据约定转化窗口定义，加权依赖观测及辅助估计条件；追踪缺失和任意数据漂移不能仅凭回流解决。 | 10.2.2.1.5 |
| A19 | [DDFM：Dually Enhanced Delayed Feedback Modeling for Streaming Conversion Rate Prediction](https://gsai.ruc.edu.cn/uploads/20231029/c10996dc48c439c8da4724be72532503.pdf) | CIKM 2023；作者机构全文及DOI核验 | 新到达曝光与早期样本回流可能同时具有不同的分布偏差。 将两类记录分别建模，以共享底层估计相关潜变量，形成两个加权CVR估计器，再共同训练流式预估 | 无偏与收敛结论采用论文的延迟反馈和估计条件，持续分布变化及辅助模型误差仍需检验。 | 10.2.2.1.6 |
| A20 | [RLB：Real-Time Bidding by Reinforcement Learning in Display Advertising](https://arxiv.org/abs/1701.02490) | WSDM 2017；作者全文及DOI核验 | 当前机会的出价会改变剩余预算及之后还能竞争的机会。 以剩余时间、预算和机会价值定义周期状态，依据竞价价格分布构建状态转移与价值计算，神经网络近似价值后产生出价 | 价格分布、机会模型和奖励定义限制策略结论，预算状态必须随实际支付更新；强化学习通用推导回指第7章及范式卷。 | 10.3.1.2.5 |
| A21 | [DRLB：Budget Constrained Bidding by Model-free Reinforcement Learning in Display Advertising](https://arxiv.org/abs/1802.08365) | CIKM 2018；作者全文及DOI核验 | 显式估计所有价格转移并不总是可行，局部即时奖励也可能误导周期控制。 从投放状态与反馈学习出价控制，利用按周期收益设计并学习的奖励支持模型无关策略更新；展开控制因子与实际出价的接口 | 奖励塑形要与真正累计目标对应，学习出的控制因子仍需结合预算资格执行；离线回放依赖机会与竞争条件。 | 10.3.1.2.6 |
| A22 | [DiffBid（AIGB）：AIGB: Generative Auto-bidding via Diffusion Modeling](https://arxiv.org/abs/2405.16141) | KDD 2024；作者全文会议信息核验 | 长周期的相关状态可以作为整体轨迹学习，而非只在单步输入中压缩历史。 条件扩散模型学习状态轨迹与收益或约束条件的关系，生成未来状态轨迹，再由逆动力学恢复可执行的竞价参数；训练复用离线轨迹 | 生成条件表达期望方向，实际硬预算及资格仍需执行核验；生成未来是模型预测，不能作真实机会。 | 10.3.1.2.7 |
| A23 | [GAVE：Generative Auto-Bidding with Value-Guided Explorations](https://arxiv.org/abs/2504.14587) | SIGIR 2025；作者机构全文及DOI核验 | 离线轨迹生成容易只重复旧行动，还需判断探索动作是否有价值。 以收益到终点的条件模块连接多种广告目标，学习价值函数指导动作探索，并用轨迹价值评价支持策略更新 | 离线价值对新动作的误差影响探索，模型评估的高收益不等于已满足实际预算、成本或市场响应要求。 | 10.3.1.2.8 |
| A24 | [GUIDE：Generative Auto-Bidding with Unified Modeling and Exploration](https://arxiv.org/abs/2605.19457) | SIGIR 2026；作者全文及正式DOI核验 | 探索动作与模仿历史的动作提供不同的投放依据，需要共同评价和选择。 Decision Transformer预测状态与动作，逆动力学模块提供基于训练行为的备选动作，双Q估计参与训练并在推断时选择估计价值较高的动作 | 备选和价值比较不构成任意市场上的安全保证，预测误差、日志覆盖、累计预算与实际支出分别检验。 | 10.3.1.2.9 |
| A25 | [AIGB-Pearl：Enhancing Generative Auto-bidding with Offline Reward Evaluation and Policy Search](https://arxiv.org/abs/2509.15927) | 作者公开稿，2025 | 生成轨迹的质量需要独立评价，静态模仿也限制策略搜索。 训练不依赖后继价值自举的轨迹评价器，用逐轨迹及成对反馈、专家信息学习奖励，再指导生成规划器的策略搜索 | 评价器的分布外误差仍会影响优化，离线奖励代理与真实投放价值分别验证；反馈信息和模拟条件须公开。 | 10.3.1.2.10 |
| A26 | [AIGB-R1: Self-Evolving Generative Auto-Bidding via Hierarchical Planner-Executor Optimization](https://arxiv.org/abs/2607.17281) | 预印本，2026-07-19；模板占位会议信息不作出版依据 | 宏观策略判断和实时数值动作具有不同的时间及计算要求。 语言模型规划投放周期的结构化策略，轻量Prompt Decision Transformer结合策略与数值历史产生实时竞价参数，以离线预训练及模拟交互对齐两层策略 | 公开集合与模拟收益保留范围，策略提示需转换为可执行参数并核验资格和资金；语言理由不直接证明决策正确。 | 10.3.1.2.11 |
| A28 | [MetaEmb：Warm Up Cold-start Advertisements: Improving CTR Predictions via Learning to Learn ID Embeddings](https://arxiv.org/abs/1904.11547) | SIGIR 2019；论文与官方会议作者报告核验，DOI 10.1145/3331184.3331268。 | 新广告没有成熟 ID 向量，随机初始化会影响开始投放时的点击估计及后续少量反馈下的学习速度。 在已有广告上模拟冷启动，用广告特征生成 ID 嵌入。两组少量样本分别衡量初始化预测和一次嵌入更新后的预测，以元目标学习生成器；固定已有 CTR 主网络，把可学习部分限定在嵌入初始化及适应。 | 原论文是广告 CTR 的冷物品任务，迁移到一般推荐需注明任务映射；内容资格、出价和预算不由该模型解决。无反馈只能初始化，反馈到来后才有少样本更新。 | 2.3.1.4 |

## 评价数据与交互环境补充

数据资源与模拟环境按性质登记。KuaiRec改善反馈覆盖，KuaiRand提供随机曝光，RecSim和AuctionNet提供用户或市场交互环境；它们不作为预测模型，也不相互替代真实实验。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| A27 | [AuctionNet: A Novel Benchmark for Decision-Making in Large-Scale Games](https://papers.nips.cc/paper_files/paper/2024/hash/ab9b7c23edfea0011507f7e1eae82cd2-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS Datasets and Benchmarks 2024 | 多个竞价者会共同改变价格与机会，固定旧日志难以检验这种响应。 由机会生成、竞价代理及可配置拍卖组成交互基准，并提供生成数据和控制算法比较；以同一机会、预算及竞争设置测试周期策略 | 这是评价环境与数据，不是一个竞价预测模型；生成机会和代理行为的逼真性不能直接替代真实市场实验。 | 10.3.2.2.1 |
| E04 | [RecSim: A Configurable Simulation Platform for Recommender Systems](https://arxiv.org/abs/1909.04847) | 2019 作者预印本与 Google 作者代码；本次未核验到同题正式会议出版。 | 静态日志难以试验推荐动作对未来兴趣、参与和疲劳的连锁影响，需要可配置环境检查连续策略的假设。 把用户状态、文档候选、列表选择和动态反馈拆成可配置组件，策略与环境循环交互；可改变兴趣演化、消费或疲劳机制并比较策略。 | 模型驱动的模拟轨迹依赖配置假设，不是真实用户反事实或真实留存的因果识别；需要以现实反馈校验模拟规律、适用范围和敏感性，不能仅凭模拟胜出推出上线收益。 | 7.3.1 |
| E05 | [RecSim NG: Toward Principled Uncertainty Modeling for Recommender Ecosystems](https://arxiv.org/abs/2103.08057) | 2021 扩展作者预印本；Google 官方出版页说明短版演示发表于 RecSys 2020，短版题为 Demonstrating Principled Uncertainty Modeling for Recommender Ecosystems with RecSim NG。 | 单一确定性用户环境不足以表达行为的不确定性及用户、内容供给者等多方互动，手设参数也难以结合日志学习。 基于概率编程描述多个行动者，把随机状态与动态联系显式建模；使用自动微分与概率推断从观察数据学习潜变量模型，并以可扩展运行时进行多轮模拟。 | 概率模型能表达和推断配置内的不确定性，但模型没有包含的动态不会自动恢复；拟合日志也不消除策略转移和因果识别假设。平台细节及通用概率推断应回指模型与系统卷。 | 7.3.1 |
| E06 | [KuaiRec: A Fully-observed Dataset and Insights for Evaluating Recommender Systems](https://arxiv.org/abs/2202.10842) | CIKM 2022；作者 PDF 首页核验，DOI 10.1145/3511808.3557220。 | 通常只观察曝光过的用户—物品反馈，离线未交互对象不能简单当作负例；反馈缺失方式及密度会改变模型比较。 在固定小矩阵内提高用户对目录视频的反馈覆盖，用大矩阵构造训练数据并区分重叠范围，控制观察密度及缺失机制，检查推荐算法评价结果随曝光覆盖如何变化。 | 近全观测只指所收集的小矩阵，反馈仍是特定用户、时间和平台下的行为，不是所有真实偏好的无误真值；不能推广为全目录或长期策略的因果效果识别。 | 8.2.2.3 |
| E07 | [KuaiRand: An Unbiased Sequential Recommendation Dataset with Randomly Exposed Videos](https://arxiv.org/abs/2208.08696) | CIKM 2022；作者数据项目及 BibTeX 核验，DOI 10.1145/3511808.3557624。 | 自然曝光同时受到历史策略和用户选择影响，难以把推荐反馈差异解释为对象或决策变化的效果；完全随机系统又缺少真实历史上下文。 在真实推荐流程的部分曝光机会中，从预定义视频池随机注入视频并记录反馈，将随机曝光与原历史序列关联。共同固定用户、候选池与随机机制，比较观察反馈和随机曝光反馈。 | 随机性只覆盖注入机制中的视频池、参与用户及曝光机会，不保证全目录、全部人群或任意长期策略都有无偏效果估计。随机替换反馈与完整策略随机试验是不同识别对象。 | 8.3.2.1 |

## 位置、信任与流行度纠偏补充

这组材料服务4.3.3的观测条件分析。S09的Propensity SVM-Rank与S10的DLA已在前表登记；这里补充倾向估计、推荐CTR分解、信任偏差校正和专门的双重稳健排序估计，并把流行度因素分离作为另一种条件。倾向估计协议、排序训练方法与表示分离方法具有不同职责，不构成必须依次执行的流程。

| 编号 | 原始论文及入口 | 年份与版本 | 问题与解决思路 | 适用条件 | 大纲落点 |
| --- | --- | --- | --- | --- | --- |
| S32 | [Position Bias Estimation for Unbiased Learning to Rank in Personal Search](https://research.google.com/pubs/archive/46485.pdf) | WSDM 2018；Regression-based EM；DOI 10.1145/3159652.3159732 | 私人查询与文档组合重复不足，用特征回归相关性并估计检查潜变量，交替更新位置参数与回归模型，为加权排序提供倾向。 | 依赖位置点击模型、特征表达及估计条件；普通日志上的EM拟合不单独保证检查与相关性可被识别。 | 4.3.3.4.2 |
| S33 | [Estimating Position Bias without Intrusive Interventions](https://research.google/pubs/estimating-position-bias-without-intrusive-interventions/) | WSDM 2019，474–482；作者预印本2018 | 从多个历史排序器的日志中提取同一查询—文档位于不同位置的记录，估计相对位置倾向；作为后续排序训练的数据与估计协议。 | 依赖位置点击模型、跨位置覆盖及记录可比性；多排序器记录不自动等于随机干预。 | 4.3.3.4.1 |
| S34 | [When Inverse Propensity Scoring does not Work: Affine Corrections for Unbiased Learning to Rank](https://arxiv.org/abs/2008.10242) | CIKM 2020；作者全文会议信息核验 | 信任导致靠前的不相关结果也较易被点击，单纯缩放不足；用位置相关的缩放与偏移构造仿射点击校正，再训练排序器。 | 系数与点击模型必须符合设定；校正贡献可以为负或大于一，不能解释为点击概率。 | 4.3.3.4.5 |
| S35 | [Doubly Robust Estimation for Correcting Position Bias in Click Feedback for Unbiased Learning to Rank](https://harrieo.github.io/files/2023-doubly-robust.pdf) | TOIS 41(3)，Article 61，2023；作者预印本2022；DOI 10.1145/3569453 | 偏好预测提供基准，位置条件下的加权点击残差提供校正，以预期检查作用处理实际检查不可观测的问题，构造排序目标。 | 位置与信任参数仍须正确；在此前提下，每对象的位置分布估计及无截断条件或该对象偏好回归准确支持无偏性。 | 4.3.3.4.6；8.3.1.2比较目标 |
| R92 | [PAL: A Position-bias Aware Learning Framework for CTR Prediction in Live Recommender Systems](https://doi.org/10.1145/3298689.3347033) | RecSys 2019，452–456；作者上传全文核验 | CTR拆成位置检查概率与查看后点击概率的乘积，联合训练，线上仅使用后者，避免给待排序候选预设位置。 | 检查只依赖位置、查看后响应不再依赖位置是分解条件；双分支不单独保证真实偏好的因果识别。 | 4.3.3.4.4；10.2.2复用 |
| R93 | [MACR: Model-Agnostic Counterfactual Reasoning for Eliminating Popularity Bias in Recommender System](https://arxiv.org/abs/2010.15363) | KDD 2021；作者预印本2020；DOI 10.1145/3447548.3467289 | 联合训练匹配、用户及物品分支；服务扣除匹配被置为参考常数时的反事实分数，调整流行度对候选次序的影响。 | 差值是排序分数；因果含义依赖结构函数、分支解释及参考值，未包含的质量与曝光因素仍需检验。 | 4.3.3.5.1 |
| R94 | [DICE: Disentangling User Interest and Conformity for Recommendation with Causal Embedding](https://fi.ee.tsinghua.edu.cn/~gaochen/papers/WWW2021-DICE.pdf) | WWW 2021；作者预印本2020；DOI 10.1145/3442381.3449788 | 以流行度关系构造辅助偏好约束，分离用户和物品的兴趣、从众嵌入；默认服务将两个内积分数相加。 | 依赖两原因结构、独立性、加性评分及热门度代理；未点击可能未曝光，嵌入分离不证明潜在原因已唯一识别。 | 4.3.3.5.2 |

## 由文献形成的研究脉络

以下分组是教材组织判断，不是互斥的研究阶段。多数路线长期并存，列出的年份是代表材料的发表年份，不是整个方向的起源。

| 时间范围 | 搜索 | 推荐 | 广告 |
| --- | --- | --- | --- |
| 2016—2019 | DRMM/K-NRM/DUET神经匹配与monoBERT重排（S17—S20）；位置偏差与澄清（S09—S11） | 阶段分工、树访问与字段评分（R01、R46—R51、R59）；少样本适应、知识匹配、列表与策略学习（R84、R89、R44、R45、R91） | 展示到转化的联合预测、价值与反馈竞价、新广告初始化（A03、A20、A21、A28）；路径归因和随机效果测量 |
| 2020—2023 | 稠密、稀疏、多向量、生成标识；弱监督表示与生成扩展（S01—S07、S25、S26、S28、S30、S31）；T5及列表重排（S21—S23） | 历史检索、哈希聚合与窗口表示（R20、R76—R78）；序列辅助学习（R81—R83），门控、分支融合和场景适配，近全观测与随机曝光（E06、E07） | 校准、延迟分布和成熟负例回流（A04—A07、A18、A19）；自动竞价约束、创意组合与跨渠道投放 |
| 2024—2026 | 多种表示共享、复杂指令和推理需求（S08、S15、S16、S24、S27、S29） | 长历史压缩与规模扩展（R07、R79、R80）；标识学习及混合访问（R62—R73），模块融合及阶段共享（R39—R43、R56、R61、R74），候选排列与目录列表 | 预算回报及竞价者互动（A09—A11）；生成轨迹、价值探索与分层竞价（A22—A26），交互基准（A27）、关键词与创意生成 |

搜索新工作扩展了相关性的条件，推荐新工作扩展了展示的对象和时间范围，广告新工作扩展了价值观测、资源控制和效果识别的条件。这样的脉络能够解释应用为何需要相应方法，也能避免将历史写成模型名称的轮流替代。

## 近期问题与正文落点

| 持续研究的问题 | 代表材料与已有回答 | 本大纲需要保留的未决条件 |
| --- | --- | --- |
| 语义相近却违反具体要求 | S08、S15、S16分别检验关系、推理与指令条件；混合及重排提供可组合接口 | 查询限制覆盖、额外推理成本、真实流量及跨时间泛化 |
| 对象选择怎样利用生成能力 | R62—R68、R72研究标识与生成学习，R69—R71混合稠密访问，R73复用单物品上下文，R74跨阶段共享，R08和R75具有不同列表范围 | 标识碰撞、合法映射、目录增删、冷启动范围、候选/列表多样性、共享范围与总成本 |
| 评分模块与选择阶段怎样共享计算 | R54、R55、R39扩展字段计算，R53、R56融合分离模块，R40—R42联合骨干，R60、R61、R43、R74研究粗排、阶段学习与共享 | 相同信息与算力下的作用，用户／候选计算、参数更新范围、截断、时间可见性与总成本 |
| 当下需求怎样与历史信息结合 | S11、S12及序列兴趣模型建立依据；R76—R80比较长历史访问与压缩、窗口预测，R84—R88连接语言、知识和多模态，R81—R83利用额外训练信号 | 缺身份、压缩损失、生成知识错误、兴趣冲突、时间可见性和额外询问负担 |
| 高预测分怎样变成有用展示 | R15—R19将列表差异、多种反馈、累计机会、长期价值和双方约束放入决策 | 目标权重、注意及选择模型、未点击曝光的影响和真实长期证据 |
| 转化反馈怎样支持正确价值估计 | A03—A07处理链路、选择、校准及延迟，DEFER/DDFM（A18、A19）处理成熟标签回流和双估计器 | 追踪缺失、辅助估计、概率支撑、成熟窗口、重复观测及流量变化 |
| 单次收益怎样满足整个周期约束 | A08—A12建立约束机制，A20—A26学习价值、反馈与生成轨迹控制，A27提供多竞价者环境 | 离线动作覆盖、代理价值误差、实际支出、约束违反、机会及竞争变化和模拟范围 |
| 生成创意怎样形成可验证收益 | A02、A13、A14处理关键词、素材组合及个性化标题 | 事实一致性、冷启动测试流量、创意疲劳、维护成本和真实增量 |
| 可观察的成交怎样支持效果结论 | A15—A17与E01、H02区分路径信用、随机增量和日志估计 | 未观测混杂、实验干扰、跨设备及跨渠道缺失、有限支撑和长期影响 |

隐私受限条件下的聚合效果测量、跨场景联合个性化和长期广告负载仍需补充材料。新增M01—M05支持混排、频次和负反馈的任务定义及方法对照，不足以全面评价长期营销感。正文写作时若展开营销组合模型、特定增量学习算法或完整频次优化，需要继续补充相应原始论文。

## 使用文献时的易混边界

- DPR的问答证据命中与一般搜索相关性分别设标签，RAG答案生成及引用核验回指NLP。
- 生成文档标识、物品标识、推荐列表、行为序列和自然语言理由分别说明输出，不统称为自由文本推荐。
- DIN处理候选相关的兴趣提取，DIEN增加兴趣演化，DSIN利用会话划分；这些模型的原始任务为CTR，预测兴趣轨迹不等于长期行动效果。
- MIMN的记忆压缩、SIM的历史检索与TWIN的两阶段相关性一致分别说明信息损失及维护代价；历史检索与目录召回具有不同对象。
- RankMixer的特征交互扩展、OneTrans等的联合评分骨干、OneTrans-V2的跨阶段共享与OneRec的列表生成分别标明统一范围。Transformer、混合专家或generative名称不能替代输入输出核验。
- Qulac是澄清数据集，具体问题检索和选择由BERT-LeaQuR、NeuQS展开；BEIR、STaRK、BRIGHT等按基准标注，不作为预测模型。
- 训练负采样、曝光选择、位置注意、点击选择与转化延迟分别诊断；一种修正不能自动覆盖其他机制。
- 多任务预测不等于多目标决策；总体校准不等于所有分组校准；下一行为预测不等于长期策略优化。
- 全展示空间训练不自动保证CVR无偏，ESMM和ESCM²应并列说明目标、信息与假设。
- 归因信用、预测移除效应与因果增量分别解释；购买预测准确也不自动证明广告效果识别准确。
- BRIGHT与FollowIR采用2025正式发表年份；eBay节奏控制标为WWW Companion；OneRec及HLLM-Creator仅按本次核验到的预印本状态使用。

这些区别应进入对应任务的正文解释与例子，不另行堆成一组通用方法章节。
