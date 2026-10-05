# 第十一部分图像和多模态处理研究文献地图

本文件为[图像和多模态处理大纲](image-processing-outline.md)提供可追溯的研究依据，重点记录视觉任务要解决什么、代表工作怎样组织解决流程，以及教材讲解时应保留哪些条件。主要检索范围为2016年以来约十年，截至2026年10月5日；三篇更早的工作作为概述章的历史入口。选取方法、任务基准与评价研究，不按引用量或排行榜排序，也不声称穷尽各领域。

来源采用正式会议论文页、作者项目页与arXiv原始论文。年份优先注明正式发表年，并在有助于辨认历史时补首次公开年；所链版本是预印本，并不表示工作没有正式发表。2026年新预印本只用于展示公开的研究问题，不据其局部实验作领域整体判断。

表中的解决路线来自已核实的一手材料；边界包含论文任务条件与教材归纳。除明确标注“论文实证”的内容外，限制与评价建议属于依据任务设置作出的分析，不冒充作者已实证的失败结论。后续正文若要引用公式、量化比较、复杂训练细节或历史优先权，应进一步核对全文及补充材料。

文献按九章归类，覆盖概述、共用模型基础及七类应用，每篇在主要用途下列一次，跨章使用通过回指连接。概述集中建立历史与共同评价的依据，多模态模型章集中建立表示、连接、输出及能力组合的依据。图像生成和多模态生成按主要成果及新增约束分工，并非互斥的模态类别。

## 第1章：图像和多模态处理概述

### 研究历史的入口

三篇较早的工作用于建立局部对应、学习式整图识别与密集预测的历史入口，近十年统计以其余工作为主。

| 代表工作（完整题名与论文链接） | 年份与版本 | 应用问题与解决路线 | 讲解时的条件与边界 |
| --- | --- | --- | --- |
| [Distinctive Image Features from Scale-Invariant Keypoints](https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf) | IJCV 2004 | 提取可跨尺度、旋转及一定外观变化匹配的局部特征，用于识别、图像对应和几何验证。 | 作为传统局部对应的例子，不将特征不变性解释为任意视角、遮挡或成像变化下都可正确匹配。 |
| [ImageNet Classification with Deep Convolutional Neural Networks](https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c-Abstract.html) | NIPS 2012 | 在大规模图像类别任务上学习视觉表示，作为后续学习式视觉应用的历史参照。 | 只回顾任务与表示学习的联系；网络结构已由模型卷展开，不从分类结果推出定位或区域理解能力。 |
| [Fully Convolutional Networks for Semantic Segmentation](https://openaccess.thecvf.com/content_cvpr_2015/html/Long_Fully_Convolutional_Networks_2015_CVPR_paper.html) | CVPR 2015 | 将分类网络适配为像素到像素的预测，组合粗层语义与细层位置形成语义分割。 | 用于定位密集预测的历史入口；语义类别图与对象实例掩码是不同输出。 |

### 共同评价资料

共同比较协议放在概述章，具体指标、应用案例与研究方向归各任务章，不设置独立评价章。

| 代表工作（完整题名与论文链接） | 年份与版本 | 应用问题与解决路线 | 讲解时的条件与边界 |
| --- | --- | --- | --- |
| [Benchmarking Neural Network Robustness to Common Corruptions and Perturbations](https://arxiv.org/abs/1903.12261) | ICLR 2019；ImageNet-C与ImageNet-P | 标准化常见图像退化与扰动下的分类评价，区分干净图像与变化条件的表现。 | 合成退化、常见扰动和对抗最坏情况不同；分类基准不直接评价检测、分割或生成保真。 |
| [WILDS: A Benchmark of in-the-Wild Distribution Shifts](https://arxiv.org/abs/2012.07421) | ICML 2021；首次预印本2020 | 将医院、拍摄设备、时间、地点等真实条件变化纳入数据与协议，比较同分布及分布变化下表现。 | 依据具体数据集的领域划分和模型选择协议解释结果；领域差异与任务定义变化分别确认。 |

## 第2章：图像识别与检索

按类别、对象、区域、姿态、空间属性和实例相似性组织文献。几何用于测量与匹配，检测、分割和检索按各自输出评价。

| 代表工作（完整题名与论文链接） | 年份与版本 | 应用问题与解决路线 | 讲解时的条件与边界 |
| --- | --- | --- | --- |
| [The iNaturalist Species Classification and Detection Dataset](https://openaccess.thecvf.com/content_cvpr_2018/html/Van_Horn_The_INaturalist_Species_CVPR_2018_paper.html) | CVPR 2018 | 将外观相近物种、拍摄条件变化和不均衡类别纳入真实图像识别，提供分类与检测基准。 | 区分类别平均和样本平均，以及细粒度识别与少见类别问题；不将均衡分类基准的结果直接外推。 |
| [Revisiting Oxford and Paris: Large-Scale Image Retrieval Benchmarking](https://arxiv.org/abs/1803.11285) | CVPR 2018 | 修订实例检索的标注与难度协议，并加入大量干扰图像，比较局部匹配与全局表示。 | 检索协议、相关图像定义与图库规模影响结果；同类相似和同一实例匹配分别评价。 |
| [Fine-tuning CNN Image Retrieval with No Human Annotation](https://arxiv.org/abs/1711.02512v2) | TPAMI 2018；arXiv v2；首次公开2017 | 用广义均值池化（GeM）形成紧凑全局描述，利用三维重建和相机几何选择正例与困难负例，学习实例检索表示。 | 在2.4.2.1节解释聚合、归一化、图像对监督与排序；无需人工检索标签不等于没有监督依据，全局距离也不能替代局部对应及几何核验。 |
| [SuperPoint: Self-Supervised Interest Point Detection and Description](https://arxiv.org/abs/1712.07629) | CVPR 2018 Workshops；首次公开2017 | 共享编码器预测兴趣点与局部描述，经合成图形预训练和单应变换适应取得真实图像伪标签，为局部对应提供输入。 | 在2.4.2.2节区分点检测、描述采样与后续匹配；兴趣点没有对象或部位语义，单应变换训练不保证任意三维视角变化都能正确匹配。 |
| [LightGlue: Local Feature Matching at Light Speed](https://arxiv.org/abs/2306.13643) | ICCV 2023；arXiv版本 | 从已有关键点与描述形成上下文匹配，利用层间置信判断、提早停止和点裁减调节图像对的计算。 | 在2.4.3.1节解释配对监督、匹配输出与自适应计算；匹配器不负责从像素检测兴趣点，速度和精度比较须固定特征、分辨率、硬件与输入难度。 |
| [Graph-Cut RANSAC](https://arxiv.org/abs/1706.00984v2) | CVPR 2018；arXiv v2；首次公开2017 | 在鲁棒几何估计的局部优化中，利用图割和邻近对应的联系划分内外点，服务单应及两视图几何等估计。 | 在2.4.3.2节连同RANSAC基本流程说明样本、残差、模型选择与重排；图割的局部标记优化不保证整个几何估计全局最优，视差和平面假设须分别检查。 |
| [Towards Total Recall in Industrial Anomaly Detection](https://openaccess.thecvf.com/content/CVPR2022/html/Roth_Towards_Total_Recall_in_Industrial_Anomaly_Detection_CVPR_2022_paper.html) | CVPR 2022；PatchCore | 训练时主要有无缺陷图像，用代表性的正常局部特征记忆，按距离形成异常分数与区域线索。 | 正常样本覆盖和特征选择影响适用范围；整图异常判断、缺陷区域定位与业务不合格定义分别核验。 |
| [DINOv3](https://arxiv.org/abs/2508.10104) | 2025年8月；技术报告 | 提供可复用于多个视觉任务的图像与稠密特征，并比较不微调整体表示时的下游用途。 | 这里只讨论表示怎样进入识别、检索与密集任务；自监督与训练规模回指范式卷，收益需在目标条件下确认。 |
| [You Only Look Once: Unified, Real-Time Object Detection](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Redmon_You_Only_Look_CVPR_2016_paper.pdf) | CVPR 2016；首次预印本2015 | 在整幅图像上直接预测空间分布的框与类别，将多目标定位组织成统一预测流程。 | 作为单阶段检测的代表，讨论定位、密集对象及速度条件；不以历史帧率作当前硬件的性能承诺。 |
| [Feature Pyramid Networks for Object Detection](https://openaccess.thecvf.com/content_cvpr_2017/html/Lin_Feature_Pyramid_Networks_CVPR_2017_paper.html) | CVPR 2017 | 结合不同尺度层的语义与分辨率，为大小不同的对象提供多尺度预测特征。 | 小目标、输入分辨率和计算预算相互制约；不能只比较不同骨干和输入预算下的总体平均精度。 |
| [Focal Loss for Dense Object Detection](https://arxiv.org/abs/1708.02002) | ICCV 2017；RetinaNet | 密集预测中背景远多于前景，降低易分类样本的损失权重，使训练集中于困难样本。 | 前景背景失衡与长尾类别并非同一问题；解释当前任务为何改变训练权重，不重复共享优化机制。 |
| [FCOS: Fully Convolutional One-Stage Object Detection](https://arxiv.org/abs/1904.01355) | ICCV 2019 | 按位置预测类别和到边界的距离，避免预定义锚框及相关设计。 | 不使用锚框并不等于无需预测分配或后处理；原工作仍使用非极大值抑制。 |
| [End-to-End Object Detection with Transformers](https://arxiv.org/abs/2005.12872) | ECCV 2020；DETR | 把检测组织成无序集合预测，以二分匹配将预测与真实对象对应，处理重复预测和空输出。 | 本章重点是匹配与集合目标；原始方法的训练与小目标条件应与后续改进分开，不泛指全部Transformer检测器。 |
| [Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields](https://arxiv.org/abs/1611.08050) | CVPR 2017；首次预印本2016；OpenPose路线 | 同时预测部位位置与关联信息，再自下而上组合多人的二维姿态。 | 关键点位置与不同人的部位关联分别检查；二维姿态不能直接提供带尺度的三维位置。 |
| [Single-Image Crowd Counting via Multi-Column Convolutional Neural Network](https://openaccess.thecvf.com/content_cvpr_2016/html/Zhang_Single-Image_Crowd_Counting_CVPR_2016_paper.html) | CVPR 2016；MCNN | 用不同感受范围处理密集人群的尺度变化，预测密度图并汇总人数。 | 计数结果正确不等于逐个对象的位置与身份正确；透视、密度和数据变化应分别考察。 |
| [Mask R-CNN](https://openaccess.thecvf.com/content_iccv_2017/html/He_Mask_R-CNN_ICCV_2017_paper.html) | ICCV 2017 | 在对象检测基础上为每个实例预测像素掩码，并可扩展到关键点任务。 | 框、掩码与关键点具有不同评价对象；实例分割须区分同类的不同个体。 |
| [Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation](https://arxiv.org/abs/1802.02611) | ECCV 2018；DeepLabv3+ | 结合多尺度上下文和解码恢复，改善语义分割中的对象边界。 | 上下文与边界恢复解决不同困难，像素类别不能直接提供实例身份。 |
| [Panoptic Segmentation](https://openaccess.thecvf.com/content_CVPR_2019/papers/Kirillov_Panoptic_Segmentation_CVPR_2019_paper.pdf) | CVPR 2019；首次预印本2018 | 将全图类别归属与可数对象实例统一为全景分割任务，并提出全景质量评价。 | 同时建立任务与指标，不能与只处理前景实例或只处理类别图的结果混比。 |
| [LVIS: A Dataset for Large Vocabulary Instance Segmentation](https://openaccess.thecvf.com/content_CVPR_2019/html/Gupta_LVIS_A_Dataset_for_Large_Vocabulary_Instance_Segmentation_CVPR_2019_paper.html) | CVPR 2019 | 建立大词表、长尾类别的实例分割基准，使少见对象与精细掩码成为评价重点。 | 文中数据规模有采集计划与实际版本之别，使用时按发布版本记录；长尾评价不由整体指标替代。 |
| [Masked-Attention Mask Transformer for Universal Image Segmentation](https://openaccess.thecvf.com/content/CVPR2022/html/Cheng_Masked-Attention_Mask_Transformer_for_Universal_Image_Segmentation_CVPR_2022_paper.html) | CVPR 2022；Mask2Former | 通过区域掩码及局部特征组织同一类输出，支持语义、实例与全景分割。 | 原工作在不同任务和数据上分别训练；统一架构不等于同一组参数已无条件完成所有分割任务。 |
| [Segment Anything](https://openaccess.thecvf.com/content/ICCV2023/papers/Kirillov_Segment_Anything_ICCV_2023_paper.pdf) | ICCV 2023；SAM | 建立提示分割任务，结合图像、提示及掩码输出，在交互式数据收集下形成可复用分割能力。 | 正式使用中的点、框等提示与语义识别分开；需要记录提示来源、歧义及纠错预算。 |
| [SAM 3: Segment Anything with Concepts](https://arxiv.org/abs/2511.16719) | 2025年11月预印本；ICLR 2026 | 用概念短语、图像示例或二者组合，检测、分割并跟踪图像和视频中匹配的对象实例。 | 概念提示扩展了目标选择方式；对象存在、概念区分、掩码与身份仍需分别评价，不推断任意复杂指令已解决。 |
| [Deep Image Matting](https://openaccess.thecvf.com/content_cvpr_2017/html/Xu_Deep_Image_Matting_CVPR_2017_paper.html) | CVPR 2017 | 输入图像及前景、背景、未知区域提示，预测并细化alpha，以恢复发丝和混合边界。 | 原工作需要三分图提示；alpha估计与二值分割不同，效果还需检查边界及合成质量。 |
| [Remote Sensing Image Change Detection with Transformers](https://arxiv.org/abs/2103.00208) | 2021年首次公开；链接为arXiv版本；BIT | 将双时相影像压缩为上下文表示并交换信息，恢复用于变化判断的像素特征。 | 变化区域预测仍依赖同一区域观测的对应；配准、季节与传感器差异是任务条件，不能将任意外观差异视为语义变化。 |
| [MVSNet: Depth Inference for Unstructured Multi-view Stereo](https://openaccess.thecvf.com/content_ECCV_2018/html/Yao_Yao_MVSNet_Depth_Inference_ECCV_2018_paper.html) | 2018，ECCV | 多张照片如何共同确定深度？利用已知相机几何将跨视角特征对齐，构造匹配代价并学习深度推断，将多视图约束与学习方法结合。 | 需要相机参数与有重叠的观测。弱纹理、反光和遮挡会影响匹配；评价应分别检查深度误差、几何准确性与重建完整度。 |
| [DUSt3R: Geometric 3D Vision Made Easy](https://arxiv.org/abs/2312.14132) | 2024，CVPR；预印本首发于2023年 | 相机标定和位姿未知时如何恢复几何？从图像对预测共同坐标中的三维点图，再对多幅图像的预测进行全局对齐，关联相机、深度与对应关系。 | 图像之间仍需提供可用的场景证据。讲解应指出弱重叠、尺度歧义和跨图一致性问题，并区分成对预测与多图对齐的职责。 |
| [VGGT: Visual Geometry Grounded Transformer](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html) | 2025，CVPR | 相机、深度、点云和点轨迹能否协同估计？由同一前馈模型从多个视角联合输出三维属性，连接原本分别处理的几何任务。 | 应检查学习到的几何先验在不同场景中的适用性，以及尺度、动态物体和长序列资源要求。联合输出也需要几何一致性验证。 |
| [Depth Anything V2](https://arxiv.org/abs/2406.09414) | 2024年6月；链接为arXiv版本 | 结合合成深度与真实图像的训练桥接，提供多种规模的单目深度预测，并构造更丰富的评价。 | 相对深度与使用度量深度标签适配后的模型区分；未确认尺度时不能直接用于带单位的距离测量。 |
| [A Simple yet Effective Baseline for 3D Human Pose Estimation](https://arxiv.org/abs/1705.03098) | ICCV 2017 | 从二维关节位置预测三维姿态，分离二维视觉定位与二维到三维映射的误差来源。 | 论文在其人体姿态数据条件下评价；用于比较预测二维关键点、已知关键点和三维恢复，尺度、遮挡及坐标对齐须单独说明。 |
| [MVTec AD — A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection](https://openaccess.thecvf.com/content_CVPR_2019/html/Bergmann_MVTec_AD_--_A_Comprehensive_Real-World_Dataset_for_Unsupervised_Anomaly_CVPR_2019_paper.html) | CVPR 2019 | 提供正常训练图像及带像素缺陷标注的测试图像，分别评价工业异常判断与定位。 | 基准覆盖的对象和缺陷类型不等于全部产线条件；实际工作还需定义正常变化和业务阈值。 |

## 第3章：图像复原、增强与压缩

比较观测忠实性、感知质量与实际编码成本，保留退化、传感器和配对条件。连续画面的新增要求由第6章承接。

| 代表工作（完整题名与论文链接） | 年份与版本 | 应用问题与解决路线 | 讲解时的条件与边界 |
| --- | --- | --- | --- |
| [Beyond a Gaussian Denoiser: Residual Learning of Deep CNN for Image Denoising](https://arxiv.org/abs/1608.03981)；[正式论文关联DOI](https://doi.org/10.1109/TIP.2017.2662206) | 2016年8月预印本v1；2017年IEEE Transactions on Image Processing。核读arXiv v1全文，arXiv元数据列出正式论文关联DOI。 | DnCNN预测观测与干净目标之间的残差，训练以残差配对监督，使用时从观测中减去预测残差；DnCNN-3把高斯去噪、插值后的超分辨率及JPEG去块效应组织为残差学习。 对应3.1.1.1噪声残差预测；3.1.3.1插值输入与超分辨率残差监督。 | 区分固定噪声、盲高斯去噪和DnCNN-3的具体训练设置；未知高斯噪声级不等于任意真实退化，监督残差不保证恢复不可辨识细节。 |
| [Image Inpainting for Irregular Holes Using Partial Convolutions](https://arxiv.org/abs/1804.07723) | ECCV 2018；核读arXiv v2（2018年12月camera-ready版本，元数据明确Published at ECCV 2018）。 | 对卷积窗口仅使用掩码标明的有效内容，并按有效数量重归一化；每层更新掩码，使可用上下文逐层进入不规则缺失区域，在编码解码网络中形成修补结果。 对应3.1.4.1有效像素归一化与掩码更新。 | 中间层掩码更新表示可计算支持范围扩大，不表示原观测新增；修补内容仍须区分可见区域保持与缺失区域的合理补充。 |
| [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](https://cs.stanford.edu/people/jcjohns/eccv16/) | 2016，ECCV；历史延伸阅读 | 逐像素误差较小的输出仍可能缺少自然纹理。利用预训练网络提取的特征定义感知损失，将风格迁移和超分辨率中的视觉要求纳入训练。 | 感知损失改变了优化目标，不保证输出细节来自原始观测。可借此说明感知质量的研究动机，具体损失机制回引前面的模型与范式内容。 |
| [Learning to See in the Dark](https://openaccess.thecvf.com/content_cvpr_2018/html/Chen_Learning_to_See_CVPR_2018_paper.html) | 2018，CVPR | 极低照度下，简单提亮会同时放大噪声。利用短曝光原始传感器数据与长曝光参考图像的配对数据，学习从原始观测到增强图像的映射，将成像管线纳入处理。 | RAW保留未经常规图像处理管线转换的传感器观测；配对采集、相机差异和运动条件影响数据与使用场景。应区别低照度增强、去噪与曝光调整。 |
| [The Perception-Distortion Tradeoff](https://openaccess.thecvf.com/content_cvpr_2018/papers/Blau_The_Perception-Distortion_Tradeoff_CVPR_2018_paper.pdf) | 2018，CVPR；评价延伸阅读 | 接近对应原图与输出符合自然图像分布是不同目标。论文在其形式化框架下分析感知质量与失真的取舍，并据此讨论复原方法的评价。 | 讲解应保留论文中感知质量、失真及分布距离的定义，不把结论改写成所有指标必然同时下降。应用章可解释目标取舍，深入的理论证明参阅原论文。 |
| [The Unreasonable Effectiveness of Deep Features as a Perceptual Metric](https://openaccess.thecvf.com/content_cvpr_2018/papers/Zhang_The_Unreasonable_Effectiveness_CVPR_2018_paper.pdf) | 2018，CVPR；常称LPIPS工作 | 逐像素距离不能充分反映人类对图像相似性的判断。通过人类感知判断数据比较并校准深层特征距离，建立可学习的感知相似度指标。 | 感知相似度只回答评价的一部分问题，不能单独证明文字、主体身份、语义关系或事实细节正确。应与失真、任务指标和人工检查配合使用。 |
| [Real-ESRGAN: Training Real-World Blind Super-Resolution with Pure Synthetic Data](https://openaccess.thecvf.com/content/ICCV2021W/AIM/papers/Wang_Real-ESRGAN_Training_Real-World_Blind_Super-Resolution_With_Pure_Synthetic_Data_ICCVW_2021_paper.pdf) | 2021，ICCV Workshops（AIM）；非ICCV主会 | 现实低清图像可能经过多次模糊、缩放、加噪与压缩，退化过程通常未知。用高阶合成退化构建训练配对数据，学习面向真实图像的盲超分辨率复原。 | 合成退化覆盖了哪些现实情形，需要与实际输入比较。视觉上自然的纹理可能包含补出的内容，应分别检查感知质量与原始细节保真。 |
| [DiffBIR: Toward Blind Image Restoration with Generative Diffusion Prior](https://eccv2024.ecva.net/virtual/2024/poster/696) | 2024，ECCV；2023年[预印本](https://arxiv.org/abs/2308.15070)题名使用“Towards” | 严重退化会造成无法直接反演的信息缺失。分离退化移除与内容再生成，利用预训练生成先验处理盲超分辨率、面部复原和去噪等任务。 | 补出的纹理不等于观测证据。除感知质量外，还应检查结构、身份及文字的保持程度；对需要证据忠实性的图像，须明确生成式补全的使用范围。 |
| [Variational image compression with a scale hyperprior](https://arxiv.org/abs/1802.01436) | ICLR 2018 | 联合学习图像表示与概率模型，用辅助信息捕获潜变量依赖，服务量化后的实际编码。 | 应同时记录码率、失真、辅助比特及解码过程；不同失真目标的视觉结果不同，不仅看重建图像。 |
| [Restormer: Efficient Transformer for High-Resolution Image Restoration](https://openaccess.thecvf.com/content/CVPR2022/html/Zamir_Restormer_Efficient_Transformer_for_High-Resolution_Image_Restoration_CVPR_2022_paper.html) | CVPR 2022 | 组织适合高分辨率处理的网络，并在去噪、去雨及不同模糊任务中使用。 | 作为多复原任务的流程案例；这些实验不等于未知真实退化全覆盖，模型原理回指前文。 |

## 第4章：图像生成与编辑

以单幅图像的条件控制、转换、主体和局部保持为主，补充基于观测的新视角图像；文生图本身涉及文字与图像。

| 代表工作（完整题名与论文链接） | 年份与版本 | 应用问题与解决路线 | 讲解时的条件与边界 |
| --- | --- | --- | --- |
| [Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks](https://arxiv.org/abs/1703.10593) | ICCV 2017；预印本v1发表于2017年3月，核读当前arXiv v7（2020年扩展版本，修正笔误与实现说明），不把后续修订当作新的2017年实验。 | 用两个无配对图像集合训练双向映射与域判别，循环一致性要求往返后接近输入，为仅有目标域分布的转换增加约束；使用时沿所需方向转换图像。 对应4.2.2.2无配对双向映射。 | 循环一致不保证语义逐项保持或获得唯一正确映射；域差异较大、重要局部结构变化时需核验输入对应，不能用于无依据的事实性补全。 |
| [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](https://www.matthewtancik.com/nerf) | 2020，ECCV | 如何从若干照片生成未拍摄视角？拟合场景的体密度和随观察方向变化的颜色，再沿相机射线渲染，使预测图像与输入观测一致。 | 经典设定依赖静态场景、相机位姿和逐场景优化。应解释未观测区域、视角覆盖及优化成本；图像渲染质量不能单独证明几何准确。 |
| [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) | 2023，SIGGRAPH / ACM Transactions on Graphics | 新视角渲染怎样达到交互速度？用显式三维高斯表示场景，通过可微光栅化优化外观与空间分布，并快速生成目标视角图像。 | 相机估计、初始化和观测覆盖影响重建。帧率需结合图像分辨率、场景规模与硬件解释；还应考虑存储、几何表面和编辑需求。 |
| [Image-to-Image Translation with Conditional Adversarial Networks](https://openaccess.thecvf.com/content_cvpr_2017/papers/Isola_Image-To-Image_Translation_With_CVPR_2017_paper.pdf) | 2017，CVPR；常称pix2pix | 如何把边缘、语义布局或一种成像结果转成目标图像？以配对样本学习图像之间的条件映射，使输出满足输入结构与目标图像的视觉要求。 | 依赖对齐训练数据。一个输入可能对应多种合理结果，应讨论输出多样性与结构保持，而不把所有图像转换任务视作唯一答案的回归。 |
| [High-Resolution Image Synthesis with Latent Diffusion Models](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html) | 2022，CVPR | 文生图、布局生成、修补和超分辨率怎样共用生成能力？在压缩后的图像表示中生成内容，并接入文本或空间条件，降低高分辨率合成的成本。 | 应用章重点是输入条件、输出要求和使用成本；生成模型机制回引前面的模型章节。文本遵循、细节保持和生成多样性须分别评价。 |
| [GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models](https://arxiv.org/abs/2112.10741v3) | 2022年3月；arXiv v3；首次公开2021年12月 | 比较CLIP引导与无分类器引导的文字条件扩散生成，并以DALL-E的CLIP重排序区分过程引导和候选选择。 | 本文CLIP引导使用适配噪声图像的模型，重排序发生在生成之后；相似度提高不等于图像质量和文字遵循同时改善，比较结论限于论文设置。 |
| [Adding Conditional Control to Text-to-Image Diffusion Models](https://arxiv.org/abs/2302.05543) | 2023，ICCV；常称ControlNet | 文字难以精确指定姿态、轮廓或布局时怎么办？向预训练文生图模型接入边缘、深度、分割或人体姿态等空间条件，约束生成结果的结构。 | 多种条件可能冲突。应检查生成结果对输入结构的遵守程度，并说明条件准确性和控制强度对结果的影响。 |
| [DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation](https://openaccess.thecvf.com/content/CVPR2023/html/Ruiz_DreamBooth_Fine_Tuning_Text-to-Image_Diffusion_Models_for_Subject-Driven_Generation_CVPR_2023_paper.html) | 2023，CVPR；预印本首发于2022年 | 如何生成某个具体主体在新场景中的图像？用少量参考图片微调预训练模型，将主体绑定到特殊标识，再通过文本指定新的场景和外观变化。 | 主体保持与场景变化可能相互制约。应检查身份细节、参考图背景的干扰、多主体情形及过拟合；不能只凭画面自然判断主体保持成功。 |
| [InstructPix2Pix: Learning to Follow Image Editing Instructions](https://openaccess.thecvf.com/content/CVPR2023/html/Brooks_InstructPix2Pix_Learning_To_Follow_Image_Editing_Instructions_CVPR_2023_paper.html) | 2023，CVPR | 如何按自然语言指令直接编辑已有图像？结合语言模型与图像生成模型合成编辑配对数据，学习从原图和编辑指令到结果图像的映射。 | 应同时检查指定修改是否完成和未指定区域是否保持。合成训练数据的指令及变化范围会影响实际编辑能力，复杂指令需要分项评价。 |

## 第5章：视频识别、跟踪与检索

保留帧与片段表示、跨帧身份、动作区间、历史检索和在线观察条件；语言查询与证据回答可在第8章回指。

| 代表工作（完整题名与论文链接） | 年份与版本 | 应用问题与解决路线 | 讲解时的条件与边界 |
| --- | --- | --- | --- |
| [MS-TCN: Multi-Stage Temporal Convolutional Network for Action Segmentation](https://openaccess.thecvf.com/content_CVPR_2019/html/Abu_Farha_MS-TCN_Multi-Stage_Temporal_Convolutional_Network_for_Action_Segmentation_CVPR_2019_paper.html) | 2019，CVPR；arXiv v2为2019年4月定稿 | 对未剪辑视频的每个时间位置形成动作标签，多阶段空洞时间卷积依次修正前一阶段的类别概率，配合逐帧分类与截断的时间平滑损失减少过度分段；用于5.4.2.2.2。 | 原方法使用逐帧动作标注，并采用可以读取后续帧的非因果卷积；时间平滑不能代替边界核验，不直接视为流式动作识别。 |
| [VGGT-Ω](https://arxiv.org/abs/2605.15195) | 2026，CVPR；前沿延伸阅读，版本说明见[作者项目页](https://vggt-omega.github.io/) | 将前馈重建扩展到静态与动态场景，并通过更高效的信息交换、数据标注及自监督训练讨论重建表示与空间理解的关系。 | 只作前沿延伸，不据初版结果写排行榜结论。作者项目页于2026-09-18发布新的参考检查点，以回应原检查点的可复现性疑虑；后续比较应使用该参考版本并注明版本。 |
| [RAFT: Recurrent All-Pairs Field Transforms for Optical Flow](https://arxiv.org/abs/2003.12039) | ECCV 2020 | 构造像素间多尺度对应证据，并反复更新稠密光流，用于相邻图像的位移估计。 | 光流是二维观测位移，遮挡、边界和相机运动需单独分析，不直接等于物体三维速度。 |
| [Temporal Segment Networks: Towards Good Practices for Deep Action Recognition](https://arxiv.org/abs/1608.00859) | ECCV 2016；2016年8月公开预印本 | 完整动作可能跨越多个片段，连续读取全部帧又会增加计算。方法对视频分段稀疏采样，汇总不同片段的证据并预测视频级动作类别。 | 适合讲解采样范围与覆盖动作的关系。视频级类别不直接给出动作起止时间，须与未裁剪视频的时间定位区分。 |
| [Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset](https://openaccess.thecvf.com/content_cvpr_2017/html/Carreira_Quo_Vadis_Action_CVPR_2017_paper.html) | CVPR 2017；2017年5月公开预印本 | 小型动作数据集难以区分方法的实际能力。工作发布Kinetics数据集，并用I3D从视频中提取联合的空间与时间证据，研究大规模训练对动作分类的作用。 | 片段分类与完整视频中的事件定位具有不同输出。这里讨论数据及任务变化带来的应用问题，I3D的构造原理回指模型卷。 |
| [AVA: A Video Dataset of Spatio-Temporally Localized Atomic Visual Actions](https://openaccess.thecvf.com/content_cvpr_2018/html/Gu_AVA_A_Video_CVPR_2018_paper.html) | CVPR 2018 | 同一画面中的不同人物可能同时执行多个动作。AVA对人物位置、时间和原子动作作密集标注，使任务从整段分类转向“哪个人在何时做什么”。 | 人物可同时对应多个动作标签。电影素材中的原子动作标注不能直接替代日常活动流程、长事件边界或步骤完成情况的标注。 |
| [ActionFormer: Localizing Moments of Actions with Transformers](https://arxiv.org/abs/2202.07925) | ECCV 2022；2022年2月公开预印本，8月修订 | 未裁剪视频中只有部分时间包含目标动作。方法在多尺度时间特征上逐时刻预测类别和动作边界，无须先生成动作候选区间或预设锚窗口。 | 输出为预设类别及时间区间。讲解须同时说明类别判定、起止边界与时间区间重叠的评价，不能只报告动作分类准确率。 |
| [ByteTrack: Multi-Object Tracking by Associating Every Detection Box](https://arxiv.org/abs/2110.06864) | ECCV 2022；2021年10月公开预印本，2022年4月修订 | 遮挡会降低检测得分，直接丢弃低分框可能造成轨迹断裂。方法将低分检测与已有轨迹关联，恢复可匹配的目标并过滤背景候选。 | 多目标跟踪输出目标框及身份，检测与关联应分别检查。方法依赖检测候选；目标完全缺少观测时，轨迹预测不能当作已取得新的视觉证据。 |
| [XMem: Long-Term Video Object Segmentation with an Atkinson-Shiffrin Memory Model](https://arxiv.org/abs/2207.07115) | ECCV 2022；2022年7月公开预印本 | 视频变长后，保存全部历史特征会增加存储，过早删除又会损失目标信息。方法结合不同时间尺度的记忆，通过合并和更新长期记忆延续目标掩码。 | 主要设置是给定首帧目标标注，再分割后续帧。应与无需首帧标注的自动发现目标区分，并同时讨论存储、长期遮挡与错误传播。 |
| [SAM 2: Segment Anything in Images and Videos](https://arxiv.org/abs/2408.00714) | 2024年8月公开预印本，10月修订；ICLR 2025 | 用户选定一个对象后，希望系统持续标出它在后续帧中的像素区域。方法结合提示分割、流式记忆与交互式数据收集，统一处理图像和视频中的目标分割。 | 点、框或掩码提示是任务输入的一部分。提示分割与自动发现并命名全部对象具有不同要求，评价还应考察用户纠错次数和交互成本。 |
| [Ego4D: Around the World in 3,000 Hours of Egocentric Video](https://openaccess.thecvf.com/content/CVPR2022/html/Grauman_Ego4D_Around_the_World_in_3000_Hours_of_Egocentric_Video_CVPR_2022_paper.html) | CVPR 2022 | 第一视角应用需要查询过去的经历、理解当前手物交互并预测未来活动。工作提供大规模第一视角视频及相应的任务和标注，使视频理解扩展到日常经历。 | 第一视角的遮挡、相机运动和可见范围与第三视角不同。数据中部分视频配有音频、视线或其他传感信息，不能假定所有样本具有相同输入模态。 |
| [Flash-VStream: Efficient Real-Time Understanding for Long Video Streams](https://arxiv.org/abs/2506.23825) | ICCV 2025；2025年6月公开预印本 | 在线观看时，系统须维护已有历史并及时响应。方法结合概括长期上下文的记忆和保留细节的记忆，按信息分布取回回答所需的内容。 | 在线处理只能利用已到达的帧。响应时间须连同硬件、帧率、输入长度和处理协议说明，离线完整视频问答成绩不能直接代替流式交互能力。 |
| [SiamRPN++: Evolution of Siamese Visual Tracking with Very Deep Networks](https://arxiv.org/abs/1812.11703) | CVPR 2019；首次预印本2018 | 给定一个目标，以模板与后续搜索区域的特征匹配预测目标位置，改进深层表示在单目标跟踪中的使用。 | 目标初始化是任务输入；模板匹配不要求每帧识别预设类别，遮挡、漂移、出画面及模板更新应按跟踪协议比较。 |
| [CLIP4Clip: An Empirical Study of CLIP for End to End Video Clip Retrieval](https://arxiv.org/abs/2104.08860) | 2021年；arXiv v2 | 将已有图文表示用于文字到视频检索，比较帧间聚合与时间关系，为候选视频或片段形成排序。 | 视频级检索命中不等于事件起止区间准确；5.5.2.2节解释帧表示、聚合与排序学习，8.1.2.2节展开跨模态查询，记录采样及图库条件。 |

## 第6章：视频复原、增强与压缩

围绕邻帧对齐与聚合、超分、插帧和视频编码组织应用，记录未来帧、等待、时间一致性和实际码率。

| 代表工作（完整题名与论文链接） | 年份与版本 | 应用问题与解决路线 | 讲解时的条件与边界 |
| --- | --- | --- | --- |
| [BasicVSR: The Search for Essential Components in Video Super-Resolution and Beyond](https://openaccess.thecvf.com/content/CVPR2021/html/Chan_BasicVSR_The_Search_for_Essential_Components_in_Video_Super-Resolution_and_CVPR_2021_paper.html) | 2021，CVPR | 独立放大每一帧会遗漏跨帧细节，也难以保持时间一致性。以传播、对齐、聚合和上采样组织视频复原管线，利用双向传播和光流对齐整合前后帧信息。 | 遮挡、运动估计误差和传播误差会影响多帧信息的利用。应同时考察单帧质量、时间闪烁、延迟及计算资源，区分离线双向处理与实时使用。 |
| [Recurrent Video Restoration Transformer with Guided Deformable Attention](https://proceedings.neurips.cc/paper_files/paper/2022/hash/02687e7b22abc64e651be8da74ec610e-Abstract-Conference.html) | NeurIPS 2022；RVRT | 在局部相邻帧共同更新特征，并通过跨片段对齐与传播使用更长时间的信息，评价视频超分、去模糊和去噪。 | 这些任务的实验不直接证明低照度增强能力；记录观测范围、显存、时序质量与延迟，网络机制回指模型卷。 |
| [FILM: Frame Interpolation for Large Motion](https://arxiv.org/abs/2202.04901) | ECCV 2022；链接为arXiv版本 | 根据两侧输入帧估计中间内容，使用多尺度运动与特征处理较大帧间运动，服务插帧和慢动作呈现。 | 中间运动与遮挡内容是估计，增加帧率不保证恢复真实事件；在线使用需记录等待后帧的延迟。 |
| [DVC: An End-To-End Deep Video Compression Framework](https://openaccess.thecvf.com/content_CVPR_2019/html/Lu_DVC_An_End-To-End_Deep_Video_Compression_Framework_CVPR_2019_paper.html) | CVPR 2019；首次预印本2018 | 将运动估计、运动编码、帧间预测与残差编码组织为联合学习的视频压缩流程。 | 码率统计首帧或关键帧、运动、残差与辅助信息，统一序列及关键帧间隔，记录解码依赖与错误传播；标准比较限于论文配置，不作为当前持续排名。 |

## 第7章：多模态模型

按多模态理解模型、生成模型及统一模型组织文献，生成模型内部区分语言响应与媒体内容。理解可利用表示匹配或语言生成接口，两种能力可以共存；模型章解释结构、训练职责和使用接口，分类、检索、问答、创作及成果评价留给任务章，统一模型解释这些能力怎样共享与组合。

| 代表工作（完整题名与论文链接） | 年份与版本 | 应用问题与解决路线 | 讲解时的条件与边界 |
| --- | --- | --- | --- |
| [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) | 2021 年；研究论文，链接为 arXiv 预印本 | 图文检索需要比较不同模态表达的同一语义。CLIP 学习可比较的图像与文本表示，并利用自然语言指定视觉概念。 | **论文设置：**以大规模互联网图文配对学习表示，并测试多种下游迁移任务。**教材推论：**应用章以语义检索和开放词汇分类为案例，生成系统中的表示复用、引导与候选筛选见第4章；原始CLIP不直接生成句子或图像，全图相似度不能直接替代对象位置、数量和关系的核验。 |
| [ImageBind: One Embedding Space To Bind Them All](https://arxiv.org/abs/2305.05665v2) | CVPR 2023；arXiv v2 | 以图像配对联系图像、文字、音频、深度、热成像和惯性传感器数据，形成可比较的共同表示，支持跨模态识别与检索等用途。 | 未见模态对的联系属于论文设置中的经验能力，不保证任意模态自动对齐；音频到图像生成示例还需外接生成模块，表示模型本体与完整系统分别解释。 |
| [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198v2) | NeurIPS 2022；arXiv v2 | 连接已有视觉与语言模块，利用图文交错序列组织图像或视频条件的描述、问答和少样本使用。 | 作为视觉接入与交错上下文的路线，不将上下文示例等同于参数更新；输入数量、例子来源及具体任务条件分别记录。 |
| [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597) | 2023 年；ICML 2023；链接为 arXiv 预印本 | 多种视觉语言任务希望复用已有视觉和语言能力。BLIP-2 连接已有图像编码器与语言模型，实现视觉问答和图像到文本生成。 | **论文设置：**冻结已有图像编码器和语言模型，训练连接两者的模块，并评价若干视觉语言任务。**教材推论：**用来比较专用任务系统与可复用视觉语言接口；视觉接入与学习阶段在7.3.1.1节解释，共有注意力机制和预训练范式回指前卷。 |
| [Visual Instruction Tuning](https://arxiv.org/abs/2304.08485) | 2023 年；NeurIPS 2023；链接为 arXiv 预印本 | 多模态助手需要响应自由形式的图像问题与指令。LLaVA 使用生成的视觉指令数据，将图像理解组织为问答、描述和对话。 | **论文设置：**早期评估包含合成的多模态指令测试及 ScienceQA 等任务。**教材推论：**自然对话能力与视觉事实准确性分开检查；不能把特定测试分数直接等同于真实应用中的可靠性。 |
| [Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631) | 2025 年 11 月；技术报告；arXiv 版本 | 多图、长文档和长视频应用需要保留、检索并交叉关联分散的视觉证据。报告介绍支持交错文本、图像与视频上下文的模型，并评价多种视觉理解与推理任务。 | **论文设置：**报告的模型支持最长 256K token 的交错上下文，覆盖单图、多图及视频测试。**教材推论：**把上下文容量与证据检索、细节保持的准确性分开，模型版本和测试预算须明确。 |
| [Qwen2.5-Omni Technical Report](https://arxiv.org/abs/2503.20215) | 2025 年 3 月；技术报告；arXiv 版本 | 音视频助手需要关联画面、声音和语言，并及时响应。报告将图像、音频、视频与文本联合处理，按时间组织音视频输入，支持流式文字及语音输出。 | **论文设置：**报告涉及多模态理解、指令遵循与语音生成等测试。**教材推论：**模型章解释多源接入、音画时间组织及文字和语音输出的职责，模态互补与视觉条件响应见第8、9章；不将文字和语音输出扩写为视频生成能力，离线分数不能单独说明流式交互质量。 |
| [Hierarchical Text-Conditional Image Generation with CLIP Latents](https://arxiv.org/abs/2204.06125) | 2022年；arXiv v1；DALL-E 2的unCLIP路线 | 先根据文字预测CLIP图像表示，再由以该表示为条件的生成解码器形成图像，复用图文表示建立生成条件。 | CLIP提供表示，另外的先验模型预测表示、解码器生成图像；不能把整个生成系统归为原始CLIP的直接能力，图像表示也不保留全部细节。 |
| [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747v2) | 2023年2月；arXiv v2；首次公开2022年10月 | 通过回归指定条件概率路径上的向量场训练连续生成模型，使用预测的速度场将随机初始表示转成目标数据。 | 作为7.3.2.4节补充生成目标的依据，再供7.4.1节解释统一模型的视觉输出；生成路径、训练目标与求解方式分别说明，生成时间不等于视频中的真实时间。 |
| [Show-o2: Improved Native Unified Multimodal Models](https://arxiv.org/abs/2506.15564v3) | NeurIPS 2025；2025年9月修订的arXiv v3 | 将语言的自回归建模与视觉的流匹配结合，在同一系统中支持文本、图像和视频的理解与生成。 | 在7.4.1节解释共享视觉表示及不同输出头的组成；支持多种任务不证明各项事实、空间关系和时间一致性已满足，理解任务见第8章，生成成果见第4、9章。 |

条件媒体生成中的GLIDE和联合音视频路线LTX-2分别回指第4、9章文献，模块分工在本章解释，生成过程、预算及成果核验在任务章展开。

## 第8章：多模态理解

覆盖图文与视频查询、描述和问答、文字与页面结构、界面、音画证据及空间核验。最终答案和输入证据分别检查。[自然语言处理文献地图](natural-language-processing-literature.md)中的N041（VQA v2）、N044（TextVQA）、N046（DocVQA）、N054（OmniDocBench）和N055（Video-MME-v2）按视觉证据归本章，具体任务与边界见下表。语音识别、口语理解、语音合成、语音翻译与实时口语对话由自然语言处理第8章展开；依赖画面、页面或音画联合证据的任务在这里组织。

| 代表工作（完整题名与论文链接） | 年份与版本 | 应用问题与解决路线 | 讲解时的条件与边界 |
| --- | --- | --- | --- |
| [PubTables-1M: Towards comprehensive table extraction from unstructured documents](https://arxiv.org/abs/2110.00061) | 2021年首次公开；CVPR 2022；链接为arXiv论文页 | 表格解析需要从页面得到表格区域及内部行列结构。工作采用DETR分别检测表格和结构对象，并用规范化标注减少表头过度切分歧义；本次作为8.3.3.1的完整代表实现。 | 原工作主要使用科学文档表格，明确不覆盖跨页表格；结构恢复不代替文字识别或字段问答。Table Transformer的表格结构对象与通用DETR原理分别讲解。 |
| [HowTo100M: Learning a Text-Video Embedding by Watching Hundred Million Narrated Video Clips](https://openaccess.thecvf.com/content_ICCV_2019/papers/Miech_HowTo100M_Learning_a_Text-Video_Embedding_by_Watching_Hundred_Million_Narrated_ICCV_2019_paper.pdf) | ICCV 2019 | 人工编写大量视频描述成本高。工作从教学视频的自动转写旁白建立视频与语言的对应，用于文本检索视频和教学视频中的动作定位。 | 旁白可能包含转写错误，也可能未描述当前画面。语言与视频配对不意味着时间上精确同步；相关训练范式回指前卷，只在这里说明任务所需的对应关系。 |
| [NExT-QA: Next Phase of Question-Answering to Explaining Temporal Actions](https://arxiv.org/abs/2105.08276) | CVPR 2021；2021年5月公开预印本 | 描述场景正确仍可能答错事件先后和人物反应。基准分别设置因果动作推理、时间关系推理及场景理解问题，并比较多选和开放回答。 | 论文中的因果问题属于视频问答语义，不直接等同于因果识别或干预推断。多选答案正确也不能自动说明模型能生成正确的开放回答。 |
| [MovieChat: From Dense Token to Sparse Memory for Long Video Understanding](https://openaccess.thecvf.com/content/CVPR2024/html/Song_MovieChat_From_Dense_Token_to_Sparse_Memory_for_Long_Video_CVPR_2024_paper.html) | CVPR 2024；2023年公开预印本 | 长视频问答面临存储开销和跨越较长时间的信息连接。方法将密集帧信息转入长短期记忆，并提供MovieChat-1K基准检验长视频理解。 | 压缩降低保留历史信息的成本，也可能丢失回答所需的细节；这是由压缩过程形成的讲解边界。应区分全局问题与针对某一时间位置的问题。 |
| [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://arxiv.org/abs/2407.15754) | 2024年7月公开预印本 | 面对较长视频，模型须找到问题所指的上下文，再利用细节回答。基准以最长一小时的视频及字幕构造指向特定上下文的多选推理问题。 | 视频和字幕共同构成输入，应说明字幕能提供哪些独立证据。多选准确率没有同时核验回答对应的空间位置和时间区间，不能代替完整的证据定位评价。 |
| [Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis](https://openaccess.thecvf.com/content/CVPR2025/html/Fu_Video-MME_The_First-Ever_Comprehensive_Evaluation_Benchmark_of_Multi-modal_LLMs_in_CVPR_2025_paper.html) | CVPR 2025；2024年公开预印本 | 单一场景和短片段不足以检验视频问答的应用能力。基准按视频领域、时长及视频帧、字幕和音频组合开展评价，比较不同输入条件下的表现。 | 不同模态和时长条件不能只汇成一个总分。需要结合模态消融、任务细分与观察预算解释结果；论文题名中的“First-Ever”不作为本书自行作出的优先权判断。 |
| [Video-MME-v2: Towards the Next Stage in Benchmarks for Comprehensive Video Understanding](https://arxiv.org/abs/2604.05015v1) | 2026年4月6日；arXiv v1预印本 | 视频问答需要汇集多处视觉信息、恢复时序变化并组合多模态证据。基准用关联问题的成组评价检查回答一致性，分析字幕线索与视觉观察对推理的作用。 | 成组评价补充单题准确率，一致回答仍需核验内容与证据。作为2026年公开的评价研究问题使用，不把局部结果或作者对基准权威性的宣称推广为全部模型的结论。 |
| [VideoZeroBench: Probing the Limits of Video MLLMs with Spatio-Temporal Evidence Verification](https://arxiv.org/abs/2604.01569) | 2026年4月2日公开预印本 | 答对问题未必意味着找到了真实视觉证据。基准将答案、时间区间和空间框分层核验，区分回答生成、时间定位及空间定位。 | 这是截至检索日期公开的新预印本，可用来展示证据核验问题。单个新基准的结果不足以推断所有视频模型和应用场景的能力，不据此报告无条件结论。 |
| [TempoGround: State-Aware Streaming Visual Grounding with Vision-Language Models](https://arxiv.org/abs/2609.02359) | 2026年9月2日公开预印本 | 自由语言指定的目标在视频流中可能出现、持续可见或离开。方法显式建立跨帧对象对应及存在状态，并输出二维位置和相机坐标系中的三维框。 | 流式语言定位同时涉及语义指代、身份与几何位置，可连接第5章的身份维护、第8章的语言定位和第2章的空间测量。新预印本只用于说明研究问题，不能把其测试范围推广为任意视频的长期一致性保证。 |
| [Making the V in VQA Matter: Elevating the Role of Image Understanding in Visual Question Answering](https://arxiv.org/abs/1612.00837) | 2016 年首次公开；CVPR 2017；链接为 arXiv 预印本 | 视觉问答模型可能根据问题中的语言规律猜答案。VQA v2 为同一问题收集答案不同的相似图像，减弱仅靠语言作答的捷径。 | **论文实证：**论文测试的模型在平衡后的数据上表现下降。**教材推论：**讲解问答评价时加入替换图像和成对问题检查，不能仅凭答案准确率判断模型是否使用了视觉证据。 |
| [Bottom-Up and Top-Down Attention for Image Captioning and Visual Question Answering](https://arxiv.org/abs/1707.07998) | 2017 年首次公开；CVPR 2018；链接为 arXiv 预印本 | 图像描述与问答需要选出与当前语言内容相关的对象。方法先提出对象及显著区域，再根据语言为区域特征分配权重。 | **论文设置：**候选区域由基于 Faster R-CNN 的模块产生。**教材推论：**适合解释局部证据的作用，同时应说明候选区域遗漏和固定检测词表如何限制下游回答。 |
| [MDETR — Modulated Detection for End-to-End Multi-Modal Understanding](https://arxiv.org/abs/2104.12763) | 2021 年；ICCV 2021；链接为 arXiv 预印本 | 读者需要把“左侧穿红衣的人”等自由文本对应到图中区域。MDETR 根据文本查询检测对象，训练时利用短语与对象区域的显式对齐。 | **论文设置：**预训练数据具有文本短语与图像对象的对齐标注，并适配短语定位、指代表达理解和分割等任务。**教材推论：**区分全图语义匹配与局部定位，说明定位监督影响可覆盖的表达。 |
| [Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection](https://arxiv.org/abs/2303.05499) | 2023 年首次公开；ECCV 2024；链接为 arXiv 预印本 | 固定类别检测难以直接响应用户给出的新类别或指代表达。Grounding DINO 用语言输入指定检测目标，在图像中输出相应对象区域。 | **论文设置：**同时评价新类别检测和包含属性的指代表达理解。**教材推论：**开放词汇识别与完整表达的对象定位分别评价；语言输入并不自动保证复杂关系表达都能定位正确。 |
| [Audio-Visual Event Localization in Unconstrained Videos](https://arxiv.org/abs/1803.08842) | ECCV 2018 | 定义片段中既可见又可听的事件，融合音画证据作时间定位，并比较一种模态查询另一种模态的定位。 | 事件定义要求音画同时提供证据，不能把仅有声音的画外事件当成已经看见；输入监督与时间对齐条件分别说明。 |
| [Localizing Visual Sounds the Hard Way](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_Localizing_Visual_Sounds_the_Hard_Way_CVPR_2021_paper.html) | CVPR 2021 | 用声音与图像区域的对应分数定位可见声源，以困难区域比较改善跨模态定位，并建立VGG-SS评价。 | 原任务定位可见的声源，空间区域与声音事件类别不同；多个声源、画外声音和时间错配需要另外核验。 |
| [Towards VQA Models That Can Read](https://arxiv.org/abs/1904.08920) | 2019 年；CVPR 2019；链接为 arXiv 预印本 | 识别图中物体仍不足以回答路牌、包装和仪表上的文字问题。TextVQA 提供依赖图中文字的问答，LoRRA 联合图像、识别文字和问题，并允许从图中字符串构造答案。 | **论文设置：**问题需要读取并推理自然图像中的文字，答案可包含图中出现的字符串。**教材推论：**区分场景文字识别错误与后续理解错误，说明文字候选提取质量对回答的影响。 |
| [DocVQA: A Dataset for VQA on Document Images](https://arxiv.org/abs/2007.00398) | 2020 年首次公开；WACV 2021；链接为 arXiv 预印本 | 文档问答需要同时利用文本与版面结构。DocVQA 在文档图像上提出问题，建立视觉问答及阅读理解基线，检验模型能否找出所需信息。 | **论文设置：**原始单文档任务的答案是从给定文档图像中抽取的一段文字；论文指出理解文档结构的问题仍有较大性能差距。**教材推论：**与跨页推理、自由生成和外部知识问答区分，评价应适配答案的抽取形式。 |
| [OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations](https://openaccess.thecvf.com/content/CVPR2025/html/Ouyang_OmniDocBench_Benchmarking_Diverse_PDF_Document_Parsing_with_Comprehensive_Annotations_CVPR_2025_paper.html) | CVPR 2025；2024年首次公开预印本 | 真实文档需要同时恢复文字、版面、表格、公式及阅读顺序。基准提供多类文档和细粒度标注，比较流水线与端到端视觉语言方法的完整解析和模块表现。 | 文档类型、结构标签和解析任务需分别报告；完整解析正确与后续问答正确不同，解析误差应追踪到所用页面与结构。该基准为解析任务提供证据，不直接代替文档问答评价。 |
| [ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning](https://arxiv.org/abs/2203.10244) | 2022 年；Findings of ACL 2022；链接为 arXiv 预印本 | 图表问答可能要求识别颜色、对应数据项并执行比较或算术操作。论文建立相关基准，并联合图表视觉特征与底层数据表回答问题。 | **论文设置：**所提出的模型使用图表视觉特征和数据表，基准包含人工问题及由图表摘要生成的问题。**教材推论：**必须说明是否提供真实数据表；从像素恢复数据与在正确数据上计算是不同错误来源。 |
| [Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding](https://arxiv.org/abs/2210.03347) | 2022 年首次公开；ICML 2023；链接为 arXiv 预印本 | 文档、网页和界面包含混合的文字与视觉结构。Pix2Struct 学习从截图生成简化 HTML，并适配文档、图解、界面及自然图像任务。 | **论文设置：**使用截图到结构文本的学习任务和可变分辨率输入表示，测试覆盖四类领域。**教材推论：**强调结构化输出和分辨率选择；页面解析正确仍需与问答正确、操作正确分别评价。 |
| [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://aclanthology.org/2024.acl-long.505/) | 2024 年；ACL 2024 正式论文 | 界面助手需要把“点击保存”等指令对应到屏幕位置。SeeClick 使用截图进行界面元素定位，并建立覆盖移动端、桌面和网页的 ScreenSpot 基准。 | **论文实证：**论文的测试显示，提高界面定位能力与改善下游界面任务表现相关。**教材推论：**点击目标命中率与多步任务完成率分别报告；定位改进不能作为任意操作流程都能完成的保证。 |
| [ScreenSpot-Pro: GUI Grounding for Professional High-Resolution Computer Use](https://arxiv.org/abs/2504.07981) | 2025 年 4 月；链接为 arXiv 预印本 | 专业软件的高分辨率画面常包含密集的小目标。ScreenSpot-Pro 提供真实专业界面的目标定位测试，ScreenSeekeR 用规划引导的逐级搜索缩小候选区域。 | **论文设置与实证：**基准覆盖 23 个应用、五类行业和三个操作系统；论文测试中，缩小搜索范围提高了目标定位准确率。**教材推论：**解释整图缩放、小目标辨识与局部裁剪的取舍；收益需结合屏幕、目标和搜索预算评价。 |
| [Character Region Awareness for Text Detection](https://openaccess.thecvf.com/content_CVPR_2019/papers/Baek_Character_Region_Awareness_for_Text_Detection_CVPR_2019_paper.pdf) | CVPR 2019；CRAFT | 预测字符区域与相邻字符关联，将弯曲、倾斜或复杂形状文字组合为文字实例。 | 输出文字位置而非最终字符串；字符关联与识别错误分别检查。 |
| [TrOCR: Transformer-based Optical Character Recognition with Pre-trained Models](https://arxiv.org/abs/2109.10282) | 2021年首次公开，2022年修订；链接为arXiv版本 | 将文字图像编码后解码为文本，利用合成数据与目标标注适配印刷、手写及场景文字。 | 文字识别输入的区域及质量应说明；图像到字符串不能替代完整页面的阅读顺序与版面恢复。 |
| [LayoutLMv3: Pre-training for Document AI with Unified Text and Image Masking](https://arxiv.org/abs/2204.08387) | ACM MM 2022；链接为arXiv版本 | 结合文字、图像及布局信息，服务表单理解、文档分类、版面分析和文档问答。 | 这里只比较输入信息与文档任务流程；多模态预训练机制回指范式卷，OCR与文字图像对应的条件须明确。 |
| [GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering](https://arxiv.org/abs/1902.09506) | 2019 年；CVPR 2019；链接为 arXiv 预印本 | 视觉问答的总分难以区分关系推理、答案偏置和证据定位。GQA 借助场景图构造组合问题，并评价一致性、视觉依据和答案合理性。 | **论文设置：**问题由场景图和问题程序生成，论文控制答案分布以减弱部分偏置。**教材推论：**细分问题类型与错误来源，但不能把该生成流程当作真实用户问题的完整分布。 |
| [Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162) | 2022 年；CVPR 2022；链接为 arXiv 预印本 | 图文匹配系统需要区分词汇相同、关系不同的描述。Winoground 使用词汇集合相同但词序不同的描述，与成对图像进行匹配。 | **论文实证：**论文当时测试的视觉语言模型在该组合任务上表现接近机会水平。**教材推论：**用于解释属性和关系绑定的诊断价值；历史结果不能直接外推到 2026 年的全部模型。 |
| [Evaluating Object Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2305.10355) | 2023 年；EMNLP 2023；链接为 arXiv 预印本 | 自由描述可能生成图中不存在的对象。POPE 通过询问对象是否存在，较稳定地检查这一类视觉幻觉，即回答与输入图像不符的现象。 | **论文设置：**关注对象存在性，分析了指令与对象共现规律对幻觉的影响。**教材推论：**对象存在性测试不能覆盖属性、关系、文字读取和自由长回答中的全部错误。 |
| [Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces](https://arxiv.org/abs/2412.14171) | 2024 年首次公开；CVPR 2025；链接为 arXiv 预印本 | 视频空间问答要求在连续观察后记住场景配置。VSI-Bench 检查计数、距离、方向、路线、尺寸和出现顺序，并分析空间记忆的表达方式。 | **论文实证：**在论文测试范围内，常见语言推理技巧没有提高基准表现，显式认知地图改善了部分距离任务。**教材推论：**区分语言推理和空间信息保存，说明坐标参照及跨视角整合的重要性。 |
| [More Thinking, Less Seeing? Assessing Amplified Hallucination in Multimodal Reasoning Models](https://arxiv.org/abs/2505.21523) | 2025 年 5 月首次公开，6 月修订；arXiv 预印本 | 延长视觉推理过程可能伴随输入证据偏离。论文提供 RH-Bench 和 RH-AUC，检查推理长度变化时感知准确性如何变化。 | **论文实证：**所研究的模型和任务中，较长推理链可能降低对视觉输入的关注并增加幻觉。**教材推论：**推理质量与感知忠实性一起评价；不能把“推理更长”写成视觉回答必然更准或必然更差。 |
| [Video-MSR: Benchmarking Multi-hop Spatial Reasoning Capabilities of MLLMs](https://arxiv.org/abs/2601.09430) | 2026 年 1 月；arXiv 预印本 | 动态视频中的空间问题可能要求连续定位和多步推断。Video-MSR 检查约束定位、链式指代检索、路线规划和反事实物理推断，并提供针对性的训练数据。 | **论文实证：**论文评价的模型在多跳空间推理中出现明显性能下降，针对性训练在该基准上改善了表现。**教材推论：**单步感知与多步推断分开检查；基准内改进不能直接作为真实导航与物理预测可靠性的保证。 |
| [Geo3R: Mitigating Spatial Reasoning Hallucination in Multimodal Large Language Models](https://arxiv.org/abs/2607.21085) | 2026 年 7 月；页面标注 ACM MM 2026 接收；当前为非终稿的 arXiv 预印本 | 空间回答可能受透视、物体朝向和视角变化影响。Geo3R 在推理时引入几何证据和结构化三维推断，处理二维视觉表达与三维空间关系之间的差距。 | **论文实证：**论文在三个基准、18 类任务上报告减少空间推理幻觉。**教材推论：**几何约束是一条可讨论的应用路线，但效果依赖几何证据质量和任务条件，不能表述为普遍消除视觉幻觉。 |

## 第9章：多模态生成

从文字、图像与空间条件扩展到视频、声音、多视角和三维成果。区分固定视频配声、联合音视频生成与基于观测的动态呈现，Qwen2.5-Omni及Show-o2的模型组成回指第7章文献，视觉条件响应与统一生成成果在本章核验。

| 代表工作（完整题名与论文链接） | 年份与版本 | 应用问题与解决路线 | 讲解时的条件与边界 |
| --- | --- | --- | --- |
| [4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_4D_Gaussian_Splatting_for_Real-Time_Dynamic_Scene_Rendering_CVPR_2024_paper.html) | 2024，CVPR；Wu等人的4D-GS工作 | 场景随时间变化时，怎样同时表示外观与运动？结合三维高斯和随时间变化的表示，预测高斯变形，生成不同时间、不同视角的动态场景图像。 | 快速运动、遮挡、拓扑变化和稀疏观测值得单列检查。本篇须用完整题名区分其他同名或近名的4DGS工作，不能混用各自方法与结果。 |
| [DreamFusion: Text-to-3D Using 2D Diffusion](https://dreamfusion3d.github.io/) | 2023，ICLR；预印本首发于2022年 | 缺少大量标注三维资产时，如何由文字创建三维对象？用预训练二维生成模型提供约束，优化三维表示，使不同视角的渲染符合文本条件。 | 逐对象优化成本、跨视角一致性和可用几何质量是应用关注点。生成资产的形状、表面及后续编辑需求应另行评价，几何测量回指第2章，观测场景拟合回指第4章，共有表示机制回指前卷。 |
| [Lumiere: A Space-Time Diffusion Model for Video Generation](https://arxiv.org/abs/2401.12945) | 2024，预印本；核实到v2（2024-02-05） | 高质量图像逐帧生成仍可能闪烁或跳变。联合处理视频的完整时间范围，在多个时空尺度生成运动，支持文生视频、图生视频、修补和风格化生成。 | 短视频的时间一致性不能直接回答长程身份保持、多镜头叙事或物理正确性。应按视频长度、运动类型和编辑范围讨论适用条件。 |
| [VBench: Comprehensive Benchmark Suite for Video Generative Models](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_VBench_Comprehensive_Benchmark_Suite_for_Video_Generative_Models_CVPR_2024_paper.html) | 2024，CVPR | 生成视频该怎样评价？分维度考察主体与背景一致性、运动、时间闪烁、画面质量和文本遵循，并利用人类偏好标注检验评价的对应关系。 | 一个总分可能掩盖不同能力的缺陷。应结合具体应用报告分项表现，说明自动指标、人类判断与任务成功之间的关系。 |
| [Wan: Open and Advanced Large-Scale Video Generative Models](https://arxiv.org/abs/2503.20314) | 2025，技术报告；核实到v2（2025-04-19） | 如何将视频生成扩展为可复用的应用能力？报告将时空压缩、数据整理与规模化训练结合，覆盖文生视频、图生视频、指令编辑和个性化等任务。 | 适合作为近期应用与系统案例。资源要求、视频长度和控制类型应对应具体模型与配置；作者报告中的比较结论不能写成持续有效的性能排名。 |
| [VBench-2.0: Advancing Video Generation Benchmark Suite for Intrinsic Faithfulness](https://arxiv.org/abs/2503.21755) | 2025，预印本；核实到v2（2025-08-20）；评价延伸阅读 | 视频在视觉上可信，还需符合哪些约束？从人体可信度、可控制性、创造性、物理和常识等维度评价，将检查从画面与时间一致性扩展到内容遵循的现实原则。 | 自动评价结合通用模型与专项方法，仍需核对其与人类判断的对应关系。基准中的物理与常识表现不直接证明生成模型已经具备完整的世界建模能力。 |
| [Wonder3D: Single Image to 3D using Cross-Domain Diffusion](https://openaccess.thecvf.com/content/CVPR2024/html/Long_Wonder3D_Single_Image_to_3D_using_Cross-Domain_Diffusion_CVPR_2024_paper.html) | CVPR 2024 | 从单幅参考图像生成多个视角的颜色与法线，再融合几何信息恢复带纹理表面。 | 参考图像提供部分外观证据，未观测视角由生成先验补充；跨视角一致、原视图保持和三维资产可用性分别评价。 |
| [Movie Gen: A Cast of Media Foundation Models](https://arxiv.org/abs/2410.13720v1) | 2024年；arXiv v1 | 模型族分别处理文字生成视频、参考人物个性化、视频编辑，以及视频与可选文本条件下的音频生成，组成媒体制作流程。 | 不能写成单一模型同时联合生成所有模态；原音频路线以一般声音、音效和器乐为主，不作为可靠对白生成的主要例证。 |
| [MMAudio: Taming Multimodal Joint Training for High-Quality Video-to-Audio Synthesis](https://arxiv.org/abs/2412.15322v2) | CVPR 2025；首次公开2024；arXiv v2 | 固定输入视频与可选文字，利用图文声训练数据及帧级条件生成语义、时间对应的声音。 | 多模态联合训练不同于联合生成视频和音频；视频保持固定，环境声和音效结果不直接证明可理解人类语音生成。 |
| [Ovi: Twin Backbone Cross-Modal Fusion for Audio-Video Generation](https://arxiv.org/abs/2510.01284v1) | 2025年；arXiv v1 | 文字提示共同约束视频与音频，两条生成分支在过程中交换语义与时间信息，联合生成画面和声音。 | 原版本主要评价短片段，长叙事、镜头转换和全局故事一致性另外验证；分别核验单模态质量与音画内容、时间同步。 |
| [LTX-2: Efficient Joint Audio-Visual Foundation Model](https://arxiv.org/abs/2601.03233v1) | 2026年1月6日；arXiv v1预印本 | 两条生成流通过跨模态联系共同生成视频和音频，利用时间组织与条件控制形成同步的音视频成果。 | 作为联合音视频生成的近期路线，分别评价画面、声音、语义对应与时间同步；报告中的资源和性能比较限于相应配置，不外推为长叙事或物理一致性保证。 |
