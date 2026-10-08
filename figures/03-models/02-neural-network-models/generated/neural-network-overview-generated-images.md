# 神经网络概述：生成式解剖插画记录

生成日期：2026-10-02。使用内置 `image_gen` 工具；接口未公开具体模型型号，未使用 CLI 或外部 API。生成结果复制到本项目 `figures/`，保留原始像素；不通过程序修改图像。中文、英文脑区缩写、引导线和通路箭头全部由 TikZ 统一排版，使用同一 `\kaishu\footnotesize` 字体与字号。最终图应以 LaTeX 排版后的图和章节 PDF 为准，PNG 原图不含标注。

## 当前使用：一个神经元连接另外两个神经元

- 素材：`neural-overview-neuron-divergence.png`；标注源：`neural-overview-biological-neuron.tex`。
- 单幅完整生成，包含一个轴突分支到两个接收神经元的场景；不拼接或复用三张单细胞图。
- 输入1：[neural-overview-biological-neuron.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/03-models/02-neural-network-models/generated/neural-overview-biological-neuron.png)，只参考早期单细胞图中组件清楚的形态。
- 输入2：`neural-overview-brain-anatomy.png`，只参考自然解剖插画的风格和颜色。
- 该形态为教学构造，不能当作真实回路重建。图像模型仅绘制解剖外形，精确连接方向与结构名称由图源和图注说明。

```text
Use case: scientific-educational.
Asset type: a clear original anatomical illustration to be annotated in a Chinese textbook.
Primary request: ONE integrated landscape drawing with exactly THREE multipolar neurons arranged as ONE presynaptic neuron on the LEFT connecting to TWO postsynaptic neurons on the RIGHT (one upper-right and one lower-right). This is a 1-to-2 divergent circuit, NOT a chain, NOT a montage or separate panels.
Reference roles: Image 1 is the earlier SINGLE neuron as a MORPHOLOGY and component-clarity reference only. Its soma, dendrites, one long axon, separated myelin segments and small terminal arbor are clearly distinguishable. Image 2 is the human BRAIN as a STYLE and color reference only. Match its natural anatomy-atlas rendering while keeping the clean component readability of image 1.
Composition: main neuron 1 soma at left-center; dendrites spread modestly around it, never a huge tangled tree. Its ONE long axon runs rightward through 3 or 4 clearly separated pale myelin sleeves, with visible narrow nodes of Ranvier. After this trunk, the axon bifurcates into an upper and a lower branch. Each branch ends in a small arbor with muted amber terminal boutons close to dendrites of neuron 2 or 3 respectively. Keep a tiny visible synaptic gap, never fuse bouton and receiving dendrite. Both receiving cells have a clearly visible soma with nucleus and a modest dendritic tree, and their OWN thin axons exit toward the right to small terminal arbors. No second axon emerging from the left cell, no linkage between the two receiving cells.
Style: natural, refined anatomical watercolor and graphite line illustration, restrained muted teal-grey neuronal tissue, pale slate-blue-grey myelin, fine navy contours, subtle organic tissue shading matching image 2. Roundish or tapered organically lobed somata rather than geometric stars. Dendrites with a few clear irregular forks, thicker at base and thinner toward tips. Do NOT draw lots of tiny spines or recursive hairline branches. This must read clearly at 169 mm page width.
Layout: wide about 16:9, all cells and terminals completely inside frame, ample white negative space above and below the main axon for annotations later. Pure white background.
Text and overlays: absolutely NO text, labels, letters, numbers, formulas, arrows, leader lines, watermark or pseudo-text. Exact annotations will be added in LaTeX.
Anatomical constraints: conceptual CNS neurons, no Schwann cell nuclei inside sheath segments. Exactly one nucleus in each soma, no extra circular organelles that resemble nuclei. Biological parts must stay distinct and legible.
```

## 当前使用：人脑自然形态与互补视图

- 素材：`neural-overview-brain-anatomy.png`；标注源：`neural-overview-visual-cortex.tex`。
- 输入：[neural-overview-neuron-circuit.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/03-models/02-neural-network-models/generated/neural-overview-neuron-circuit.png)，只作为自然解剖绘制的风格参考；该三细胞链式中间方案未在正文使用。
- 模型仅提供脑的外侧与内侧形态。脑区点位、中央沟和距状沟标注、what与where箭头由 TikZ 绘制。
- 排版叠加中，what使用赭色实线，where使用蓝色虚线，两者加粗并衬白，以提高在浅色脑组织底图上的辨识度；这不改变生成式原图像素。
- 点位为教学定位或位置投影，不表示个体脑的实测功能区边界。
- 定位依据：Wandell等（2007），doi:10.1016/j.neuron.2007.10.012；通路依据：Purves等（2001）《Neuroscience》与Goodale、Milner（1992），doi:10.1016/0166-2236(92)90344-8。生成式外形不承担精确解剖测量。

```text
Use case: scientific-educational.
Asset type: anatomical brain illustration for a Chinese machine-learning textbook.
Primary request: Draw a naturally shaped, anatomically credible HUMAN cerebral hemisphere with clear organic gyri and sulci, in two complementary views within ONE wide page illustration: a large lateral view occupying the left two-thirds, and a smaller medial view at the upper-right. Both show the anterior end to the LEFT and the posterior occipital end to the RIGHT (the main is left hemisphere lateral, the inset can be right hemisphere medial). These are two anatomical views of the same kind of human brain, not copies of the same outline. No skull, no face. Main lateral view shows realistic frontal, parietal, temporal and occipital surfaces, with a recognizable central sulcus descending obliquely from the superior midline toward the anterior/inferior side and a lateral/Sylvian fissure above the temporal lobe. Medial view shows recognizable corpus callosum and the calcarine sulcus in the posterior occipital region. Include only enough underside tissue to keep anatomy natural, no dominant cerebellum.
Style reference: the supplied three-neuron image is ONLY a style reference, not a composition or content reference. Match its refined natural anatomy atlas look: delicate graphite-like ink contours, subtle watercolor shading and organic tissue texture. This brain should have convincing folds and soft volume, not geometric blobs, an icon, a cartoon or glossy 3D. Muted pale teal-grey and slate-grey tissue, navy fine contours; light enough to receive crisp labels and colored pathway arrows later.
Composition: landscape about 16:9, large lateral brain fully contained in left 68% of canvas, small medial view fully contained in upper-right 28%, blank lower-right for a later legend. Leave generous white margin around both forms. Bright pure white background matching the neuron illustration.
Text and overlays: NO labels, words, letters, numerals, arrows, leader lines, legends, artificial colored regions, highlighted circles, watermark or pseudo-text. All exact region labels and pathways will be added separately.
Scientific constraints: a HUMAN brain, preserve plausible relative lobe shapes, sulci and orientation. Avoid a generic walnut-like symmetric hemisphere with decorative grooves. The image supplies anatomy only; do not invent visual-area boundaries.
```

## 中间风格参考：三细胞链式画面（未用于正文）

素材：[neural-overview-neuron-circuit.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/03-models/02-neural-network-models/generated/neural-overview-neuron-circuit.png)。用户随后将连接要求改为“一对二”，故不使用这一版回路，仅留作人脑插画的风格来源记录。

```text
Use case: scientific-educational.
Asset type: original anatomy illustration for a Chinese neuroscience introduction in a machine learning textbook.
Primary request: Draw ONE continuous, coherent wide scene containing exactly THREE biologically natural multipolar neurons communicating in a chain. NOT three panels, NOT repeated or pasted identical neurons. Give all three different organic dendritic trees and poses. Neuron 1 lies upper-left, neuron 2 in the center, neuron 3 lower-right, all in the same scene with ample negative space. Each soma has one visible nucleus. Each neuron has one distinguishable slender axon, thicker branching dendrites, and delicate terminal arborization. Neuron 1's long axon extends to neuron 2's dendrites; neuron 2's axon extends to neuron 3's dendrites. At these two contacts, a small amber presynaptic bouton approaches but does not fuse into the receiving dendrite: preserve a tiny gap. Axons can curve naturally but do not tangle ambiguously. At least neuron 1's axon has a few pale segmented myelin sheaths with exposed narrow nodes of Ranvier, clear enough to label. The third neuron also has its own axon and terminal arbor, going toward the lower-right open edge.
Style/medium: refined, natural anatomical scientific illustration, hand-rendered fine graphite-like contours and subtle watercolor shading, credible organic cell shapes and delicate branching, similar to a classic neuroscience atlas drawing; elegant and detailed rather than cartoon, flat icon, geometric star or glossy 3D. Muted teal-grey neuronal tissue, slate-blue-grey myelin, navy fine outlines and very restrained amber terminal boutons. Soft local shading gives natural volume; no cast shadows or decoration.
Composition: landscape approximately 16:9, three complete cells fit inside frame, clearly spaced but actually interconnected in one image. Keep room above and below the cell circuit for labels to be added later. White pure background.
Text: absolutely NO text, labels, numbers, formulas, arrows, leader lines, watermark or pseudo-letters. All annotation will be typeset separately.
Scientific constraints: central nervous system neurons, do not draw Schwann-cell nuclei in sheath segments. Dendrites taper and branch irregularly; avoid identical repeating spines. No artificial extra nucleus-like circular objects. This is a conceptual anatomical reconstruction, not a measured connectome.
```

## 早期单细胞参考记录（已由一对二画面替代）

# 神经网络概述：生成式插图记录

## 生物神经元形态

- 文件：[neural-overview-biological-neuron.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/03-models/02-neural-network-models/generated/neural-overview-biological-neuron.png)。
- 生成日期：2026-10-02。
- 生成方式：内置 `image_gen.imagegen` 工具；工具未公开具体模型名称或版本。
- 使用位置：`tex/03-models/02-neural-network-models/01-overview.tex`，由 `neural-overview-biological-neuron.tex` 复用三次并添加中文标注及连接箭头。
- 参考一：用户提供的灰度神经元示意图（原附件 `codex-clipboard-1cb846c4-e579-40dd-8541-539f2d85726a.png`），仅用于形态和构图参考，重新生成插画；附件来源和许可证未提供，未直接嵌入书中。
- 参考二：本书第三章 `paradigms-transfer-learning.png`，仅用于扁平插画风格和全书配色参考。
- 后处理：复制原始 PNG，保留透明通道；未修改图像像素。文字、引导线、连接与方向箭头均用 TikZ 另行排版。
- 使用边界：教学概念插画，不是显微照片或解剖重建；不承载精确比例、统计量或脑连接拓扑。图示为一种多极、有髓鞘神经元，不代表所有脑内神经元。
- 检查：有胞体、细胞核、分支树突、单条连续轴突、四段髓鞘及段间间隙、分支末梢；未引入属于周围神经系统的施旺细胞标注。

### 最终提示词

```text
Use case: scientific-educational.
Asset type: unlabeled anatomical illustration for a Chinese machine-learning textbook, later combined with precise LaTeX labels and artificial-neuron diagrams.
Primary request: Draw one representative multipolar myelinated neuron of the human central nervous system, inspired by the anatomy in Image 1, with the editorial visual language of Image 2. This is a NEW illustration, not a copy of the old figure.
Input images: Image 1 is only an anatomical composition reference. Image 2 is only a style and palette reference; do not include its animals, cards, prisms, arrows or flowers.
Composition: a wide horizontal silhouette, fully visible. Soma in the left quarter, a clearly visible darker nucleus inside the soma, several short branching tapering dendrites extending left, up and down. Exactly one much longer axon leaves the soma towards the right, curves gently horizontally, has four separate pale-blue myelin sheath internodes with narrow exposed gaps between them, then ends on the far right in a small branching terminal arbor with rounded synaptic boutons. Axon stays continuously visible through the sheath regions. Distinct axon and dendrite morphology. Nothing is cropped. Large enough nucleus, myelin gaps and terminals to label clearly at textbook size. Compact vertical extent and generous transparent space around the silhouette, approximately 3:1 subject aspect ratio.
Style: refined flat editorial scientific illustration, clean vector-like outlines and subtle paper-like texture confined to the filled neuronal material, matching the existing chapter illustrations. Palette dark navy #233342 outlines, muted teal #267D82 soma/dendrites/axon, pale slate blue myelin, small warm amber #A66A25 terminal boutons. No gradients, shadows, glossy or photorealistic effects, no 3D.
Background: genuinely transparent alpha.
Text: absolutely NO words, letters, labels, numerals, formulas, caption, arrows, leader lines, logos, watermark or pseudo-text. All labels will be added in LaTeX.
Scientific constraints: central nervous system, so do NOT draw Schwann cell nuclei in individual sheath segments; do NOT imply every human neuron is myelinated or has this morphology. The neuron is a representative conceptual anatomy illustration, not a complete brain architecture or experimentally reconstructed neuron.
```
