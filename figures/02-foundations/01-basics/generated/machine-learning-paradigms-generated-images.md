# “学习范式简介”生成式插图记录

## 生成信息

- 生成日期：2026-09-27
- 生成工具：Codex 内置 `image_gen` 工具
- 模型：工具未公开具体模型标识，故不作推测
- 画幅：3:2 横向，输出分辨率为 1536×1024
- 后处理：未修改画面内容，仅将工具输出复制并按项目规范重命名

这些图片是概念过程图，不是数据集样本、论文原图、实验结果或精确模型拓扑。案例事实与出处在 LaTeX 正文和参考文献中给出。

## 共享提示词

下列提示词均以这段共享要求开头，再拼接各图的专用描述：

> Create a scientific-educational illustration for a Chinese machine-learning textbook, 3:2 landscape. Warm off-white paper background, refined flat editorial illustration, vector-like shapes with subtle paper texture. Palette: dark navy, muted teal, slate blue, warm amber, pale gray. Use shapes and pictograms only. No words, letters, numerals, formulas, captions, logos, watermarks, or pseudo-text. No gradients, shadows, glossy effects, or 3D. Leave generous whitespace and make arrows and stages unambiguous.

个别提示词为表达特定案例，允许出现手写数字的说明性笔画、围棋棋盘、抽象符号或问号；这些元素不承担数值或文字说明。

## 各图提示词与案例依据

### `paradigms-curriculum-learning.png`

- 案例依据：Bengio等人的BasicShapes到GeomShapes两阶段几何形状识别实验，正文参考文献 `bengio2009`。图中类别始终为矩形、椭圆和三角形，右侧独立评价样本不参与训练。
- 本轮生成日期：2026-09-27；使用Codex内置 `image_gen`，具体模型标识未公开；输出1536×1024，未做图像后处理。
- 专用描述：Show curriculum learning based on Bengio et al. 2009 geometric-shape classification, a conceptual teaching illustration rather than original dataset samples. Two training stages followed by a distinct evaluation area, read left to right. Left training stage: a small deck of grayscale square image cards containing a square, a circle, and an equilateral triangle; below it a dark-teal learning device with a simple gear pictogram. The cards feed downward into the device. Middle training stage: a larger deck of grayscale image cards containing varied elongated rectangles, ellipses, scalene triangles, AND the simple square/circle/equilateral-triangle cases, all still belonging to the same three shape families. They feed downward into a second depiction of the SAME learning device. A thick horizontal navy arrow connects the first device to the second, clearly conveying one learner continuing across training stages rather than separate models or increasing the number of classes. Right evaluation area: separated by ample whitespace, distinct held-out varied shape cards feed into the resulting device and produce three small shape-family pictograms (rectangle, ellipse, triangle), with NO feedback arrow into training. Keep the cards and two learning stages large and legible at a printed width of 112 mm. Difficulty changes in shape variability, NOT noise, missing labels, new classes, or human annotation. Two training stages only; evaluation is distinct. No charts, no accuracy numbers, no human figures.

### `paradigms-supervised-mnist.png`

- 案例依据：MNIST 手写数字识别，正文参考文献 `lecun1998`
- 专用描述：Show supervised learning in two clear stages. On the left, many small grayscale handwritten-digit-like image cards are paired with colored category chips and enter a learning machine; the machine's predicted chip is compared with the provided chip and a feedback arrow updates the machine. On the right, a new digit-like card enters the trained machine without a target chip, and the machine emits one predicted category chip. Make the training and later-use stages visually distinct. The strokes are teaching illustrations rather than reproductions of MNIST samples.

### `paradigms-unsupervised-topics.png`

- 案例依据：文档主题模型，正文参考文献 `blei2003`
- 专用描述：Show unsupervised topic discovery. A large collection of unlabeled news-document cards containing only abstract line patterns flows into a learning machine. The output is several overlapping thematic clusters represented by coherent pictogram groups such as government buildings, sports equipment, markets and weather. One document may connect to more than one cluster. A human observer interprets the discovered groups only after learning; no topic labels enter the model.

### `paradigms-semi-supervised-images.png`

- 案例依据：CIFAR-10 半监督分类与 FixMatch，正文参考文献 `sohn2020`
- 专用描述：Show semi-supervised image classification. A small set of object-image cards has visible colored category chips, while a much larger set of similar cards has no chips. Both streams enter the same learning machine and jointly improve it. For unlabeled cards, show two altered views of the same object feeding into a consistency comparison, without revealing a hidden true label. The trained model then classifies a new card.

### `paradigms-weak-supervision.png`

- 案例依据：弱监督分类与标注函数，正文参考文献 `zhou2018`、`ratner2017`
- 专用描述：Show weak supervision for review classification. The same collection of abstract review cards is inspected by several separate heuristic-rule devices; each device emits a colored vote, a conflicting vote, or an abstention symbol. A combiner reconciles these noisy sources into soft training chips, which then train a final model. Include a separate small set of carefully checked cards for evaluation. Make conflicts and uncertainty visible without text.

### `paradigms-self-supervised-text.png`

- 案例依据：BERT 掩码语言建模，正文参考文献 `devlin2019`
- 专用描述：Show self-supervised language learning as a clear left-to-right process. A row of abstract token tiles enters a model, one middle tile is visibly masked as an empty pale tile; below, a hidden target tile is separated from the input. The model predicts several candidate tiles; a comparison and feedback connector between the prediction and hidden target updates the model.

### `paradigms-reinforcement-atari.png`

- 案例依据：Atari 深度强化学习，正文参考文献 `mnih2015`
- 专用描述：Explain reinforcement learning through a generic retro arcade interaction. A small agent controller observes an arcade screen containing a paddle and ball, sends an action to the environment, then receives the next screen state and an abstract reward token. Arrange the agent and environment in a strong closed loop with two directional arrows; visually distinguish observation and reward from action. Avoid any real game, character, brand or trademark.

### `paradigms-combination-alphago.png`

- 案例依据：AlphaGo 的专家棋谱学习与自我对弈，正文参考文献 `silver2016`
- 专用描述：Explain a combination of learning paradigms inspired by computer Go in two connected stages. On the left, a human expert beside archived Go-board position cards provides demonstrated moves to an initial policy model. On the right, two abstract agent devices play each other on a Go board; win and loss outcome tokens feed back into an improved policy model. Show a clear transition from imitation using human records to self-play reinforcement. Use a generic Go board only and no identifiable person.

### `paradigms-active-learning.png`

- 案例依据：池式主动学习，正文参考文献 `gal2017`
- 专用描述：Explain active learning as a closed process. A large pool of unlabeled image cards enters a learning model; the model highlights only a few uncertain cards with amber question markers; a human expert annotates those selected cards using colored category chips; labeled cards return to update the model, while most pool cards remain untouched. Make the model's query to the human visually explicit.

### `paradigms-continual-learning.png`

- 案例依据：连续任务学习与灾难性遗忘，正文参考文献 `rebuffi2017`
- 专用描述：Explain continual learning over time in one horizontal sequence. Three successive batches arrive: first birds and small vehicles, then dogs and boats, then flowers and hand tools. Each batch updates the same learning model. After each update, the output memory board visibly retains icons from all earlier batches as well as the new ones. Add a subtle backward memory or rehearsal loop to show protection against forgetting.

### `paradigms-contrastive-learning.png`

- 案例依据：SimCLR 与监督式对比学习，正文参考文献 `chen2020`、`khosla2020`
- 专用描述：Explain contrastive learning visually. One original bird image card branches into two altered views, one cropped and one color-shifted; both pass through the same encoder and become two nearby dots in a representation space. Several unrelated object cards also pass through the encoder and become distant dots. Show an inward attraction connector between the matching pair and outward separation connectors toward nonmatching points.

### `paradigms-transfer-learning.png`

- 案例依据：ImageNet 表示迁移与少样本目标任务，正文参考文献 `yosinski2014`
- 专用描述：Explain transfer learning from source to target. On the left, a large diverse source collection of animals, vehicles and household-object image cards trains a model. In the center, a reusable layered feature prism or encoder is carried forward. On the right, only a few labeled flower image cards adapt that representation into a successful flower-category output. Clearly show abundant source data, transferred representation and scarce target data.

### `paradigms-multi-task-learning.png`

- 案例依据：共享表示的多任务学习，正文参考文献 `caruana1997`、`kendall2018`
- 专用描述：Explain multi-task learning with an autonomous-driving scene. One shared street-scene image with road, cars, trees and buildings enters a single shared encoder trunk. The trunk branches into two task heads: one produces a semantic-segmentation-style panel with distinct flat colored regions, the other produces a depth-style panel ranging from pale nearby shapes to dark distant shapes. Make shared representation and separate outputs obvious.

### `paradigms-meta-learning.png`

- 案例依据：少样本元学习，正文参考文献 `finn2017`
- 专用描述：Explain meta-learning as learning to adapt across tasks. Show several small training episodes arranged around a central adaptable model: each episode contains a few support cards with one abstract handwritten-symbol family and a separate query card. Curved arrows from these episodes update a central reusable initialization. Then show a new unseen symbol family on the right, where only a few support examples rapidly produce a correct matched query output. Use abstract curved strokes rather than recognizable letters or numerals.

### `paradigms-federated-learning.png`

- 案例依据：联邦平均与移动设备语言模型，正文参考文献 `mcmahan2017`、`hard2018`
- 专用描述：Explain federated learning. Arrange five personal devices around a central aggregation hub. Each device contains visibly private local image or message cards inside its boundary. A shared model packet travels outward from the hub; smaller abstract update packets travel inward from devices to the hub. Raw local cards never leave device boundaries. After aggregation, an improved shared model returns to all devices. Use arrows and nested boundaries to make the communication cycle explicit.
