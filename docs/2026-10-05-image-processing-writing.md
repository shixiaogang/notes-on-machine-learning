# 图像和多模态处理正文写作

九章正文、统稿与六版验收均已完成，最终结果见[验收记录](2026-10-05-image-processing-validation.md)。以下阶段核查保留当时状态，后续条目记录相应问题的解决结果。

## 范围与基线

- 工作分支：`docs/image-processing-content`。
- 工作目录：`.worktrees/docs-image-processing-content`。
- 远端基线：`origin/main`，`5db7ad4728f14b9ed227ac937cbaf487cc964e03`；2026-10-05执行`git fetch origin`后创建。
- 正文依据：`plans/image-processing-outline.md`中的九章及`plans/image-processing-literature.md`，不调整其任务边界。
- 远端当前仍使用五卷目录；数学准备卷的其他工作区变更不属于本次范围。
- 部分入口沿用`tex/04-applications/02-image-processing/part.tex`及`part:image-processing`标签，显示名称按已定大纲更新为“图像和多模态处理”。

## 文件与讲解职责

| 文件 | 章名 | 主要职责 |
| --- | --- | --- |
| `01-overview.tex` | 图像和多模态处理概述 | 观测、任务、历史与共同约束 |
| `02-image-recognition-and-retrieval.tex` | 图像识别与检索 | 类别、范围、测量、对应与排序 |
| `03-image-restoration-enhancement-and-compression.tex` | 图像复原、增强与压缩 | 观测反演、呈现、实际码流及用途保持 |
| `04-image-generation-and-editing.tex` | 图像生成与编辑 | 条件创建、转换、编辑和新视角渲染 |
| `05-video-recognition-tracking-and-retrieval.tex` | 视频识别、跟踪与检索 | 时间证据、身份、活动与片段 |
| `06-video-restoration-enhancement-and-compression.tex` | 视频复原、增强与压缩 | 跨帧信息、时空采样、解码参考链 |
| `07-multimodal-models.tex` | 多模态模型 | 编码、连接、训练职责及输出接口 |
| `08-multimodal-understanding.tex` | 多模态理解 | 查询、定位、读取、结构和答案证据 |
| `09-multimodal-generation.tex` | 多模态生成 | 视频、配声、联合音画、空间内容及响应 |

## 共同约定

- 读者已具备线性代数、概率、优化、通用神经网络与生成模型基础，第一次系统学习视觉应用；关键接口仍就地解释。
- 各章保留独立“本章小结”。大纲中较深层的方法标题使用LaTeX原有层级，并在本部分局部启用编号，不改变其他部分的样式。
- 标签统一为`chap:vision-*`及`sec:vision-*`；本部分外的引用使用`Book*Ref`范围感知宏。大纲中的内部章号不得直接写入正文。
- 图像用`\bm{X}\in\mathbb{R}^{h\times w\times c}`表示，并说明它是三阶数组；像素以`x_{i,j,k}`表示。视频帧用`\bm{X}_t`；参数优化迭代仍使用括号上标。
- 统一像素坐标：横坐标向右、纵坐标向下，框使用连续边界坐标并以差计算宽高；离散像素中心或归一化坐标需另行说明。
- 街景承接识别、测量与视频；工业零件承接异常定位；玩具狗与花瓶承接创作；固定票据与小表承接读取和问答。
- 手算数据均明确为教学构造，不制造模型实测输出、当前排名或实验结论。
- 每个代表方法说明输入、关键计算、监督或保留信息、推理和输出恢复。完整机制集中解释一次，跨章补充当前用途的差异。
- 新文献集中登记到`tex/references.bib`，复用已有条目；复杂机制核对原文，近期报告固定版本。长作者列表在版面上单独检查。
- TikZ源放在`figures/vision/`，采用项目颜色与`\figurefont`，普通图控制在112mm正文宽内；图形表达计算、空间或时间关系，不以装饰性流程框替代解释。
- 新术语映射进入`tex/index-terms/04-applications.tex`，与全书既有术语对照。

## 验证安排

- 分别进行结构覆盖、技术公式与算例、首次阅读逻辑、术语与引文核查。
- 执行`bash tests/check-book-editions.sh`、`make test`和`./build.sh all`，工具路径通过运行环境设置，不改构建脚本。
- 检查全集与五个单卷的引用、索引、字形及错误日志；逐章查看应用卷的图表、长公式、深层标题与边注。
- 构建产物留在`build/`；交付记录报告实际覆盖、页数、检查结果及未解决限制。未经用户另行要求不提交、推送或合并。

## 阶段核查

- 概述章与识别检索章已形成初稿，后者覆盖大纲全部标题，约1.46万中文字，含22个编号公式、4幅TikZ图和1张协议表；这不是九章整体完成声明。
- SAM 3存在分支、实例条件分数及训练门控核对`2511.16719v2`的模型与实现章节；LightGlue双向归一化、缩放、提前停止和点裁剪核对作者仓库的`lightglue.py`；PatchCore整图重加权核对CVPR 2022原文式(6)–(7)。
- 文献元数据缓存于`build/vision-sources/`，约定以题名核对ID后再合入集中书目。MCNN直接采用CVF 2016记录，不能使用`1602.06525`，该编号属于无关数学论文。
- 当前机器的通用Biber包调用`lipo`时失败。已将其arm64切片提取至`build/vision-tools/biber`，以临时PATH供本工作区构建；`biber --version`返回2.21，手动生成应用卷书目成功。未修改系统工具、模板或构建脚本。
- 数学环境中的中文标点使用`\text{。}`、`\text{，}`，避免STIX数学字体缺字；后续章节沿用。
- `make test`的27个单元测试通过，仓库索引审计失败。对`git archive HEAD`的独立快照复核得到相同44项审计错误：14个既有孤立映射、28个既有缺失映射、2项基线计数漂移。原稿统计为`calls=1708, unique=1493, mappings=1440`；新增两章后为`1742,1519,1466`，本次新增术语没有缺失映射。基线记录在`build/vision-baseline/audit.log`。
- 全书最终验收前需更新索引计数，并决定如何处理已核实的既有映射漂移；不得把当前失败报告成通过。后续章的前向交叉引用将在对应正文写入后解析。
- 两章接入应用卷后生成`build/04-applications.pdf`（阶段产物50页，包含共享前后页和空的相邻部分首页）。文献全部解析，公式中文标点缺字已消除；余下14处未解析引用均指向尚未编写的后续章或节。后续须定义`sec:vision-models-contrastive`、`sec:vision-generation-novel-view`、`sec:vision-understanding-evaluation`。
- 已检查阶段PDF第15、21、28、29、32、37、41、45页，覆盖6幅图、深层方法标题、SAM 3与长作者书目。图中坐标、箭头和标签可读。Grounding DINO与DeepLabv3+的边注在当前分页下过于接近页底，需在终稿分页稳定后修复；不得只检查LaTeX日志。预览位于`build/vision-preview/`。
- 第三、四章已接入应用卷，分别覆盖大纲的31项和33项标题，各约1.03万中文字。两章共增加28个编号公式、7幅TikZ图和2张表；前四章合计约4.16万中文字、52个编号公式、13幅图和3张表。
- 第三章核读DnCNN、Restormer、Real-ESRGAN、部分卷积、DiffBIR v2和尺度超先验全文相关机制。Restormer通道注意力又对照作者实现；DiffBIR明确区分生成模块训练所用条件预处理器和推理时的任务复原模块。SID使用CVPR正文核查RAW打包、黑电平、放大比例和参考监督。
- 第四章核查ControlNet零初始化连接、DreamBooth类别先验保持、GLIDE噪声感知CLIP与掩码条件、pix2pix的非饱和生成器目标、CycleGAN往返约束、固定风格Gram统计、InstructPix2Pix双条件引导及其补充材料中的自注意力替换。NeRF和3D Gaussian Splatting核对积分、投影、合成与加密职责，不将逼真渲染当作几何测量。
- 可复算结果保存在`build/vision-sources/ch3-ch4-numerical-checks.txt`：算术编码`ABC`对应前缀`01011`、射线权重`(1/2,3/8,1/8)`与颜色`(5/8,1/8,1/2)`、双条件引导`(1.25,-0.95)`、PSNR约26.0206 dB、RAW提亮约0.113414及部分卷积输出0.5。八点反卷积由离散傅里叶变换复算，图中未裁剪过冲。
- 最新应用卷阶段稿为84页，日志`build/vision-ch4-recheck.log`。正文无overfull、缺字、重复标签或缺失文献；保留16处后续章/节的前向引用。书目末尾仍有两处约1.11 pt和1.55 pt的小幅溢出，待最终分页检查。除已有前向目标，还须定义`sec:vision-models-media-generation`；`sec:vision-generation-novel-view`已定义。
- 已查看第三、四章全部7幅图及双条件引导公式、RAW章节、长引文等关键页。宽图用局部`\FloatBarrier`保持在相关子节内，避免插入后续段落中间；ControlNet及固定风格转换的引文移至更早的相关句末以留出边注空间。最终全文分页稳定后仍须复核长边注。预览继续保存在`build/vision-preview/`。
- 第五、六章已接入应用卷，分别覆盖既定大纲全部39项、25项标题，中文字约1.21万、0.84万。前六章共62168个中文字、70个编号公式、19幅TikZ图和5张表；55个独立术语均有既有或新增映射，未发现本部分重复标签及未在正文引用的图表。
- 第五章核读SiamRPN++的骨干共享与分支投影、RAFT相关金字塔、ByteTrack两次关联及作者`byte_tracker.py`的低分/轨迹状态限制、XMem加权距离与长期原型巩固、TSN得分共识、I3D初始化、AVA人物动作流程、ActionFormer边界回归、MS-TCN截断平滑和CLIP4Clip双向排序损失。MS-TCN明确保留仅对当前时刻一侧求梯度的条件。
- SAM 2依据`2408.00714v2`已取得的模型与训练正文核查，并在正文注明修订版对应公开SAM 2.1，不混用初版实验。该HTML下载在后部超时，未据未取得的补充材料作额外断言。VGGT-$\Omega$仅作动态空间恢复的简短延伸，题名、作者和范围核对arXiv原始摘要，未引用其数值实验或详细结构。
- 第六章核读RVRT的跨片段引导取样、前一层查询/键与当前层值的来源、交替方向传播，BasicVSR双向特征对齐，FILM中间帧到两端的取样位移及两类损失配置，以及DVC的解码运动、残差、率失真目标与训练参考缓存。DVC最终使用`1812.00101v3`完整HTML方法正文核对；下载不完整的CVF PDF不作为公式验收依据。
- 第五、六章数值复算记录为`build/vision-sources/ch5-ch6-numerical-checks.txt`，包括三帧加权得分0.690625、一对一分配代价0.90/0.31、TSN概率0.880797、MS-TCN平滑项、IDF1为0.6、tIoU为7/9、双线性取样0.425、正确/错误融合0.41875/0.775、DVC四像素MSE为0.0001，以及300000字节教学码流的240000 bit/s与0.03472 bit/像素。
- 最新阶段产物`build/04-applications.pdf`为117页，日志`build/vision-ch6-final-stage.log`。正文无overfull、缺字、重复标签或缺失文献；17处未解析引用只涉及后续三章及`sec:vision-models-contrastive`、`sec:vision-models-media-generation`、`sec:vision-understanding-evaluation`。
- 第五、六章全部6幅图与2张表已查看，另查看Ego4D、SAM 2、RVRT、FILM、VGGT-$\Omega$等长引文及关键公式。Ego4D引文移至章首第一段后已完整落在版心内，FILM引文移至相关机制段落，BasicVSR图及章末表采用局部浮动体屏障以免打断后续句子或小结。时间采样图末端标签与9秒刻度的重叠已消除。
- 终稿仍需复查第二章Grounding DINO与DeepLabv3+边注，以及所有章节在最终分页中的边注位置。参考文献现有3处溢出约1.11 pt、12.04 pt、1.55 pt，其中12.04 pt来自CLIP4Clip条目；第六章末表的“随机访问”在当前窄列中有单字换行，可在最终统稿时压缩措辞。索引既有44项审计问题及全书六版构建仍待统一处理。
- 第七章已完成初稿并接入应用卷，完整覆盖大纲29项标题，约1.40万中文字，新增10个编号公式、4幅TikZ图和1张接口比较表。前七章合计76156个中文字、80个编号公式、23幅图和6张表；58个独立标记术语均有映射，正文引用和图表标签未发现重复或新增缺失映射。
- 核读CLIP v1、ImageBind v2、BLIP-2 v2、Flamingo v2、原始LLaVA v2、Qwen3-VL v1、Qwen2.5-Omni v1、LDM v2、unCLIP v1、流匹配v2、LTX-2 v1及Show-o2 v3的方法正文；CLIP与BLIP-2书目另对照PMLR正式记录。完整HTML及公式文本保存在`build/vision-sources/`。
- 重点核清BLIP-2三种掩码与两阶段更新模块、Flamingo最近图像交叉注意力与零门控、原始LLaVA线性投影、Qwen3-VL前三语言层的DeepStack接入及独立文字时间戳、Qwen2.5-Omni的40毫秒位置尺度与2秒块输入，以及语音编码到频谱再到波形的输出路径。
- 生成部分区分LDM空间潜网格与unCLIP整图语义向量，明确LDM原条件编码器共同训练及unCLIP扩散先验预测干净表示。流匹配补上训练路径、条件均值速度的平方损失分解与推理ODE；LTX-2区分两个潜空间及双向时间联系，未采用报告正文与结论不一致的参数规模数字。Show-o2说明语义蒸馏、双路径融合、因果块与块内全注意力、两阶段更新范围及较大7B变体的视频训练边界。
- 第七章数值记录为`build/vision-sources/ch7-numerical-checks.txt`，复算脚本为同目录`check_ch7_numbers.py`。结果包括CLIP正确配对概率0.731059、双向平均损失0.313262、行梯度(-0.268941,0.268941)、裁剪坐标(500,360)、流匹配速度(2,-2)、预测欧拉更新(0.8,-0.2)及注意力成对位置数倍率11.56。
- 最新阶段PDF为138页，日志`build/vision-ch7-recheck.log`。正文无overfull、缺字、重复标签或缺失文献；14处未解析引用均涉及第八、九章及`sec:vision-understanding-evaluation`、`sec:vision-understanding-grounding`。参考文献新增LTX-2作者行约8.77 pt溢出，连同前述3处留待终稿统一处理。
- 已查看第七章全部4幅图和1张表，并检查BLIP-2、Flamingo、LLaVA、Qwen3-VL、Qwen2.5-Omni、LDM、unCLIP、LTX-2、Show-o2引文及流匹配推导所在关键页。Qwen3-VL长作者边注初次被页底截断，已移至后续架构段落，重编译确认完整；LTX-2引文也已移至训练段落。最终预览在`build/vision-preview/ch7-final-*.png`，全部阶段预览按`ch7-*.png`保存。
- 第八章已完整覆盖大纲59项标题，约1.76万中文字，新增11个编号公式、4幅TikZ图和1张核验表。前八章约9.38万中文字、91个编号公式、27幅图和7张表；62个独立标记术语均有集中映射。该章所有交叉引用及书目键均已解析，新增的`sec:vision-understanding-grounding`与`sec:vision-understanding-evaluation`也消除了前章相应引用缺口。
- 核读HowTo100M v2、MDETR v1、Localizing Visual Sounds the Hard Way v1、音画事件定位v1、SeeClick v2、ScreenSpot-Pro v1、CRAFT v1、TrOCR v3、LayoutLMv3 v3、Pix2Struct v1、PubTables-1M v3、ChartQA v1、LoRRA v1、DocVQA v2和Bottom-Up/Top-Down v2的方法正文；缓存均已检查含HTML结束标记。MDETR的两个对齐损失另对照作者`mdetr.py`实现。BLIP-2的检索微调与128候选重排复用前章已缓存全文核查。
- 第八章明确了HowTo100M同视频负例加权、MDETR多正词元的均匀目标、可见声源软阈值中间带不是严格零贡献、同步距离与逐秒事件分类的任务边界，以及ScreenSeekeR按定位框中心投票的候选评分。SeeClick坐标为归一化数值文字，点击命中与操作完成分别核验。
- 页面与问答部分区分CRAFT位置、TrOCR字符串、LayoutLMv3任务头和Pix2Struct简化结构序列；补充行列交叉、跨格合并与文字归属的完整小表。核清LoRRA采用逐候选二元交叉熵且只复制一个OCR候选，DocVQA原基线使用首次字符串匹配近似标注跨度，VisionTaPas新增差值/比值操作及其有噪单元监督，同时保留不支持任意嵌套计算的边界。
- 评价与近期扩展论文使用原始摘要、元数据和已定文献地图核对题名、问题定义及适用范围，没有据摘要推断未取得的方法细节，也未引用榜单数字。2026年TempoGround、VideoZeroBench、Video-MME-v2、Video-MSR、Geo3R均固定v1，More Thinking, Less Seeing?固定v3。
- 第八章数值复算脚本及结果为`build/vision-sources/check_ch8_numbers.py`和`ch8-numerical-checks.txt`。包括间隔损失0.05、三个音画窗口距离3.00499/0.3/3.01980、全屏点(784,400)、嵌套裁剪点(550,310)、12个基本格合并为10个单元、图表读数12/18、区域权重0.75、单行差值6、嵌套求和差值8、CER为1/6和证据交集成功率0.3。
- 第八章初次版面检查覆盖全部章节缩略页、全部4幅图和1张表及密集引文页。修复了图表读数图和问答操作图打断后续段落的问题、表头网格穿过文字的问题，以及SeeClick、OmniDocBench、VQA v2、Winoground等边注触底问题。最终分页仍须随着第九章接入统一复查。
- 终稿新增待核项：CLIP已有`radford2021`条目与新增`vision-clip2021`题名重复，应合并并复用；第八章加入后，参考文献末尾共有8处溢出，除前四处外，另有TempoGround约37.89 pt、ScreenSpot-Pro约2.21 pt、HowTo100M约6.14 pt和NExT-QA约10.37 pt。这是书目版式问题，正文公式与图表未产生overfull。
- 第八章最终阶段编译产物为168页应用卷，日志`build/vision-ch8-verified.log`。仅剩5处指向第九章`chap:vision-multimodal-generation`的前向引用；无正文溢出、缺字、重复标签或缺失文献。第八章26页的边注坐标扫描未发现超过715 pt的文字，长引文与修订图表已再看。对More Thinking与Video-MME-v2两个完整作者边注增加局部`\Needspace`，保证来源与论述开头有足够分页空间；未改全局样式。全部阶段预览位于`build/vision-preview/ch8-*.png`，`git diff --check`通过。
- 第九章已完整覆盖大纲36项标题，约1.54万中文字，新增10个编号公式、4幅TikZ图和1张验收表。九章合计109204个中文字、101个编号公式、31幅TikZ图和8张表，均保留独立章末小结；本部分121个不同书目键参与句末引用，内部引用目标全部定义。
- 核读Lumiere v2、Wan v2、Movie Gen v1、MMAudio v2、Ovi v1、DreamFusion v1、Wonder3D v1、Wu等人的4D Gaussian Splatting v1、VBench v1及VBench-2.0 v2完整HTML方法正文，全部缓存检查到HTML结束标记；LTX-2 v1、Qwen2.5-Omni v1及Show-o2 v3复用前章已核材料。Movie Gen 2024年的版本日期和完整贡献者名单另与v1正文及附录核对，未采用BibTeX接口返回的后续年份。
- 第九章区分整段前向与多步采样、Wan的16+16+4通道组成及任务微调、Movie Gen编辑回译的真实目标方向、MMAudio联合训练与仅音频输出、Movie Gen原音频任务不含语音或带人声音乐。说明Ovi的同一生成时刻与媒体时间不同，LTX-2引导以完整条件预测为基准，分阶段联合分布的链式分解本身不造成概率表达能力损失。
- SDS补全从固定方差高斯与二维先验KL到参数梯度的推导，注明分数近似、非零噪声日程、零均值控制变量及不反传噪声网络Jacobian的条件。Wonder3D说明法线由SDF一阶空间梯度形成，参数优化才涉及进一步求导；法线赋权显式保留分母非零条件。4D-GS说明六平面乘积、多尺度拼接、合法旋转与正尺度恢复，以及观测拟合与物理模拟的边界。
- 第九章复算脚本与结果为`build/vision-sources/check_ch9_numbers.py`、`ch9-numerical-checks.txt`。包括覆盖计数1/1/1/2/2/1/1/1、窗口平均0.5、Wan尺寸5×32×32×16及36输入通道、八秒音频128000采样点/250潜位置、音画偏移120与-20毫秒、平均绝对偏移70毫秒、联合欧拉状态0.35与0、引导预测1.5、SDS参数更新(0.49,0.21)、法线损失0.175508、投影位移10像素、流式播放2.3秒完成及0.2秒停顿。
- 已查看第九章全部21页缩略图及图表、SDS推导、长作者边注重点页。调整了Wan、Movie Gen、DreamFusion和VBench-2.0标题前的局部分页空间，消除标题与正文被分页要求拆开的情况；SDS图补入原始噪声到差值计算的连接，4D-GS长公式改为两行，表格压缩“语音与时序”的措辞以免单字换行。
- 统稿已合并重复CLIP书目，统一复用`radford2021`。整部边注坐标回查发现第二至四章新增分页下的长引文触底，已对Grounding DINO、DeepLabv3+、SuperPoint、DUSt3R、Real-ESRGAN、LPIPS、GLIDE、固定风格转换、InstructPix2Pix及NeRF做局部留空或移动引文，后续仍按最终PDF复扫。
- 已对照基线修复索引漂移：6项映射改为现行中文名，删除8项正文已不再调用的旧映射，补22项缺失映射。仅变更集中词典，没有为通过审计而修改其他卷的术语正文。更新审计计数及`specs/latex.md`后，`make test`的27项单元测试及索引审计均通过，统计为`calls=1775, unique=1549, mappings=1510, aliases=2, errors=0`。
- 版本结构检查另发现基线AdaBoost段落一处跨卷裸引用`sec:boosting`，已按同文件既有写法改为`BookSectionRef`并提供第一卷回退说明。重跑`bash tests/check-book-editions.sh`通过；日志为`build/vision-editions-test.log`。
- 卷末长书目仍会在强制两端对齐下溢出，单加2em紧急断行弹性只解决了其中6处。已将卷末书目统一设为左对齐、右侧自然断行，并同步记录至`specs/design.md`；保留字号、完整作者、题名和边注样式。最终六版构建与回归尚待完成，当前不能声明整体交付验收通过。
- 最新阶段应用卷为193页，日志`build/vision-applications-final-layout.log`。正文和书目均无overfull、未定义引用、缺字或重复标签；已看左对齐书目、全部第九章图表及长公式。整部边注回扫只余第二章末LVIS与MVTec AD联合引文触底，已在该段前增加95mm局部分页空间，尚待下一次构建验证。其余已发现的边注问题均不再出现在扫描结果中。
- 最终六版全部完成构建：全集1687页，五个单卷分别为480、1034、16、193、14页。应用卷的九章占PDF第15—177页，全集中为第47—55章。329个大纲标题全部对应；最后一次措辞修订后，章节源文件中文字计数为109202。
- LVIS与MVTec AD联合引文已完整显示。全集编号下另修正SeeClick局部分页、ChartQA与Geo3R引文位置及BLIP-2交叉引用所在长行。最终全集和应用卷均无overfull，整部边注逐行扫描无超过715 pt检查线的文字，关键位置已目视复核。
- `./build.sh all`最终确认六版均为已更新状态；在编译完成后执行`make test`，27项单元测试及索引审计通过，版本结构检查通过。六版书目集合、书签目标与内部跳转范围检查通过。完整结果保存在`build/vision-final-audit.json`，最终限制及既有卷二1.07 pt轻微溢出见验收记录。
