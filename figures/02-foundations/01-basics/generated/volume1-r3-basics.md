# 第一卷第1—3章第三轮图像生成记录

日期：2026-10-05。工具：内置 `image_gen`；具体底层模型版本未由工具公开。全部为教学构造，不是实测数据或真实模型拓扑。按用户最新要求，最终生成架构内的中文、变量和公式均由图像模型原生绘制，不使用 TikZ 文字补写；技术图 2.3、3.5、3.6 仍为原生 TikZ。初稿的留白标注方案已被后续原生文字编辑替换。字体经再次编辑为 Source Han Sans / Noto Sans CJK Regular 与 Source Sans 3 Regular 外观，常规字重、水平基线。

## 通用字重编辑提示

```text
Use case: precise-object-edit. Change ONLY the typography in this scientific diagram. Every Chinese label must have attractive Source Han Sans / Noto Sans CJK REGULAR weight, Latin letters Source Sans 3 REGULAR, mathematical glyphs slender normal weight. Absolutely NO bold, heavy, black-weight, compressed or blocky letters. Reduce stroke weight of every label including large digits, while KEEPING current font SIZE, current wording, placement, horizontal baselines, shapes, frames, arrows, colors and topology exactly unchanged. Text must be horizontal and upright, NEVER rotated or italic Chinese. Use size only for hierarchy. No overalltitle, no new sentence text. The letters must look elegant regular-weight, visibly lighter than outlines.
```

## v1r3-nlp-tasks.png

### 架构生成初稿

```text
Use case: scientific-educational. Create a publication-quality LINE-BASED SCIENTIFIC ARCHITECTURE diagram on pure white background. Frame outlines, wires, internal networks and purposeful curved paths are the main content. Flat pale blue data inputs, pale lavender computational modules, pale mint outputs, small coral feedback accents. Dark charcoal crisp outlines substantial at print size, uniform clean vector-like linework, Nature scientific schematic aesthetic. NO overall title, NO words, NO letters, NO digits, NO equation, NO watermark. All scientific text will be added later as editable typesetting. No human figure, no decorative brain, no cartoon storytelling, no shadow, no 3D, no texture, no gradient. Wide landscape canvas at least 2048px wide with generous whitespace. Small icons only support the architecture. Keep empty annotation areas inside modules.
A text processing system receives one shared document and branches into three scientifically distinct computational heads. Wide canvas ratio 1.65:1. Left middle at x18% y50%: pale blue document rectangle with EMPTY interior, no pseudo-text. At x54%, three separated pale-purple modules centered vertically at y22%,50%,78%, each with a tiny internal line mesh on its leftmost fifth and EMPTY main body. At x87%, three mint output forms: top small categorical token with tiny delivery symbol; middle an EMPTY horizontal document with TWO slim underlined spans; bottom EMPTY speech bubble. Dark thin arrows branch from shared input to three heads and to outputs. Leave upper 10% and lower 6% blank. Main information is line architecture, not icon illustration.
```

### 原生中文与数学标注编辑

```text
Use case: text-localization. Edit this scientific architecture so all ESSENTIAL Chinese and mathematical labels are NATIVELY rendered as part of the image. Do NOT leave reserved empty annotation areas. Keep pure white background, soft Nature blue/lavender/mint/coral palette, darkcharcoal crisp frames and curved arrows. Use clean modern Chinese sans-serif, horizontal baselines, perfectly upright text and mathematical symbols, generous spacing, no overall title. Large legible labels equivalent to at least 8.5pt at final book width. All quoted strings must be exactly spelled. No additional sentence explanation or fake text. Preserve all dataflow semantics. Produce high-resolution at least 2048px width if possible.
Add shared input in blue document, four horizontal lines in reading order: "我的星海" / "订单明天" / "能送到" / "北京吗？". Top purple head: "意图识别"; middle "信息抽取"; bottom "答案生成". Top output should be a simple single category chip labelled "物流查询", REMOVE generic three-colored-dotchoice and equalsarrow. Middle output two horizontal lines "星海：商家" / "北京：地点", without behind-lines touching text. Bottomspeechbubble two horizontal lines "预计明日" / "送达北京。". These exact words already express information, no extra titles. Preserve sharedinput threebranches, no arrow from one head to another.
```


阶段原始输出：/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-ce9f5839-1a58-4de1-9d5f-711a19480222.png

## v1r3-data-split.png

### 架构生成初稿

```text
Use case: scientific-educational. Create a publication-quality LINE-BASED SCIENTIFIC ARCHITECTURE diagram on pure white background. Frame outlines, wires, internal networks and purposeful curved paths are the main content. Flat pale blue data inputs, pale lavender computational modules, pale mint outputs, small coral feedback accents. Dark charcoal crisp outlines substantial at print size, uniform clean vector-like linework, Nature scientific schematic aesthetic. NO overall title, NO words, NO letters, NO digits, NO equation, NO watermark. All scientific text will be added later as editable typesetting. No human figure, no decorative brain, no cartoon storytelling, no shadow, no 3D, no texture, no gradient. Wide landscape canvas at least 2048px wide with generous whitespace. Small icons only support the architecture. Keep empty annotation areas inside modules.
A time-ordered data management architecture, ratio1.7:1. Three equal columns centered x17%,50%,83%; top y23% each has a stack of pale blue blank email-record cards. Below each at y63%: first lavender trainable parameter bank with five slender vertical sliders, second lavender selection module containing three tiny alternative curve icons and one small dial, third mint locked evaluation gauge with a small closed padlock. Draw one downward data arrow in each column. At y90% draw a long dark left-to-right timeline arrow. Between second and third column a vertical dashed gate at x67%, covering y10–80%, with a tiny closed lock near y65%. Leave y42% blank for column labels, y76% blank for key role labels. The record count is schematic, no numbers, no percentage pies, no performance values.
```

### 机制线路修正

```text
Change ONLY architecture topology: the LEFT column has ONLY its email stack and ONE purple slider module beneath, NO other modules and NO feedback. MIDDLE column has ONLY email stack and ONE purple selection module containing tiny curve icons beneath, NO slider bank, NO green gauge, NO feedback. RIGHT column has ONLY email stack and ONE green locked evaluation gauge beneath, NO purple modules and NO feedback. Each column has ONE downward arrow. Preserve 3 columns, whitebackground/pastel/crisp outlines, bottom timeline, middle-right dashed gate. Leave empty space above and below each surviving module for overlaylabels. No letters/text.
```

### 原生中文与数学标注编辑

```text
Use case: text-localization. Edit this scientific architecture so all ESSENTIAL Chinese and mathematical labels are NATIVELY rendered as part of the image. Do NOT leave reserved empty annotation areas. Keep pure white background, soft Nature blue/lavender/mint/coral palette, darkcharcoal crisp frames and curved arrows. Use clean modern Chinese sans-serif, horizontal baselines, perfectly upright text and mathematical symbols, generous spacing, no overall title. Large legible labels equivalent to at least 8.5pt at final book width. All quoted strings must be exactly spelled. No additional sentence explanation or fake text. Preserve all dataflow semantics. Produce high-resolution at least 2048px width if possible.
Add "训练集" ABOVE left recordstack, "验证集" ABOVE center, "测试集" ABOVE right. Below left sliderbank put two lines "拟合参数" / "与预处理"; below middleselectionmodule "选择配置" / "与停止位置"; below rightlockedgauge "冻结后评估". Add "时间" above the long bottom arrow, and "冻结选择" near smalllock on dashedgate. Do not draw feedback from test to model or selection. Keep each column exactlyone emailstack, onemoduleandonearrow.
```


阶段原始输出：/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-06a40c7c-00dc-4ed2-9198-59b1d0456179.png

## v1r3-supervised.png

### 架构生成初稿

```text
Use case: scientific-educational. Create a publication-quality LINE-BASED SCIENTIFIC ARCHITECTURE diagram on pure white background. Frame outlines, wires, internal networks and purposeful curved paths are the main content. Flat pale blue data inputs, pale lavender computational modules, pale mint outputs, small coral feedback accents. Dark charcoal crisp outlines substantial at print size, uniform clean vector-like linework, Nature scientific schematic aesthetic. NO overall title, NO words, NO letters, NO digits, NO equation, NO watermark. All scientific text will be added later as editable typesetting. No human figure, no decorative brain, no cartoon storytelling, no shadow, no 3D, no texture, no gradient. Wide landscape canvas at least 2048px wide with generous whitespace. Small icons only support the architecture. Keep empty annotation areas inside modules.
Supervised classifier architecture with clearly DIFFERENT training and inference paths, ratio1.9:1. Two horizontal bands centered y32% and75%. Each band x10% blank blue image card, x43% lavender neural-network module with sparse line network confined to left edge and blank center, x72% mint prediction card. Only upper band has target card at x90%y12% in pale blue, and coral circular comparison node at x90%y37%. Upper prediction routes to comparison, target routes separately to comparison, comparison has coral dashed curved feedback path BELOW upper band returning to model. The target MUST NOT connect into predictor. Lower band has only blue input→purple model→mint prediction, no target, no loss, no feedback. Blank cards permit adding digits later. Leave y5% blank and x1–5% margin blank. Make modules/edges primary and icons sparse.
```

### 原生中文与数学标注编辑

```text
Use case: text-localization. Edit this scientific architecture so all ESSENTIAL Chinese and mathematical labels are NATIVELY rendered as part of the image. Do NOT leave reserved empty annotation areas. Keep pure white background, soft Nature blue/lavender/mint/coral palette, darkcharcoal crisp frames and curved arrows. Use clean modern Chinese sans-serif, horizontal baselines, perfectly upright text and mathematical symbols, generous spacing, no overall title. Large legible labels equivalent to at least 8.5pt at final book width. All quoted strings must be exactly spelled. No additional sentence explanation or fake text. Preserve all dataflow semantics. Produce high-resolution at least 2048px width if possible.
Top left bluecard render large digit "3" and small identifier "图像 x"; bottom leftbluecard large "8" and small "新输入 x". Upperpurplemodule emptyrightside render "模型 f_θ" and small "参数 θ"; lowerpurplemodule "固定模型 f_θ". Upper mintpredictioncard "预测 ŷ = 8"; lower "预测 ŷ = 8". Upperrightblue targetcard "标签 y = 3". Coralcomparisoncircle should contain ONLY "ℓ", remove the extra tiny arrows/dash inside circle. Add short labels "训练" at farleftupperband and "使用" farleftlowerband. Add "参数更新" above coral dashedfeedback. Label route target→loss "目标", prediction→loss "比较" if fitting. Crucially targets only enter loss, never model.
```


阶段原始输出：/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-7e75ec8c-6003-4189-a147-6867b53e286b.png

## v1r3-reinforcement-upper.png

### 架构生成初稿

```text
Use case: scientific-educational. Create a publication-quality LINE-BASED SCIENTIFIC ARCHITECTURE diagram on pure white background. Frame outlines, wires, internal networks and purposeful curved paths are the main content. Flat pale blue data inputs, pale lavender computational modules, pale mint outputs, small coral feedback accents. Dark charcoal crisp outlines substantial at print size, uniform clean vector-like linework, Nature scientific schematic aesthetic. NO overall title, NO words, NO letters, NO digits, NO equation, NO watermark. All scientific text will be added later as editable typesetting. No human figure, no decorative brain, no cartoon storytelling, no shadow, no 3D, no texture, no gradient. Wide landscape canvas at least 2048px wide with generous whitespace. Small icons only support the architecture. Keep empty annotation areas inside modules.
Three compact top-down local robot-navigation states horizontally aligned, ratio2.7:1. This is a line-based supplemental scientific state scene, NOT an isometric physical illustration. Each state has the EXACT same small orthogonal obstacle layout, drawn flat with gray outlines and pale blue obstacles, and the exact same mint goal disk at the upper-right. A tiny flat two-wheel robot icon at progressively nearer positions: first lower-left, second center, third at goal. First two show thin pale-blue local observation wedges and dotted route, third shows small mint completion ring. Keep all panels separated by whitespace, without decorative frames or title. Curved charcoal transition arrows between panels with space above for short editable labels. Pure white and flat pastel linework. No human.
```

### 原生中文与数学标注编辑

```text
Use case: text-localization. Edit this scientific architecture so all ESSENTIAL Chinese and mathematical labels are NATIVELY rendered as part of the image. Do NOT leave reserved empty annotation areas. Keep pure white background, soft Nature blue/lavender/mint/coral palette, darkcharcoal crisp frames and curved arrows. Use clean modern Chinese sans-serif, horizontal baselines, perfectly upright text and mathematical symbols, generous spacing, no overall title. Large legible labels equivalent to at least 8.5pt at final book width. All quoted strings must be exactly spelled. No additional sentence explanation or fake text. Preserve all dataflow semantics. Produce high-resolution at least 2048px width if possible.
Add only three short labels centered beneath navigation states: first "局部观测 oₜ", second "移动后 oₜ₊₁", third "到达目标". Keep sameobstaclemappositions, same goalposition, localobservationcones androbotpositions. No text in paths or objects; labels horizontal notrotated.
```


阶段原始输出：/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-09faac7b-8c2a-45da-b10e-5a40245e716a.png

## v1r3-contrastive.png

### 架构生成初稿

```text
Use case: scientific-educational. Create a publication-quality LINE-BASED SCIENTIFIC ARCHITECTURE diagram on pure white background. Frame outlines, wires, internal networks and purposeful curved paths are the main content. Flat pale blue data inputs, pale lavender computational modules, pale mint outputs, small coral feedback accents. Dark charcoal crisp outlines substantial at print size, uniform clean vector-like linework, Nature scientific schematic aesthetic. NO overall title, NO words, NO letters, NO digits, NO equation, NO watermark. All scientific text will be added later as editable typesetting. No human figure, no decorative brain, no cartoon storytelling, no shadow, no 3D, no texture, no gradient. Wide landscape canvas at least 2048px wide with generous whitespace. Small icons only support the architecture. Keep empty annotation areas inside modules.
A contrastive representation learning architecture, ratio2.1:1. Left x9%y25%: small blank-blue framed thumbnail with tiny bird icon. It branches to two augmented bird thumbnails at x31%y20% and45% (one cropped samebird, one softlydesaturated samebird). A distinct cat thumbnail at x31%y75% is separate, with NO connection from original bird. All three connect into ONE shared pale-lavender encoder hourglass occupying x48–67%, y12–83%, with a sparse internal neural mesh and large EMPTY annotation area. Outputs reach a large blank white representation plane x75–97%, y15–85%, outlined only with thin axes and NO points or curves; all exact dots/attraction arrows will be added later. Leave lower12% blank for short labels. Flat supporting animal line icons, architecture dominates.
```

### 原生中文与数学标注编辑

```text
Use case: text-localization. Edit this scientific architecture so all ESSENTIAL Chinese and mathematical labels are NATIVELY rendered as part of the image. Do NOT leave reserved empty annotation areas. Keep pure white background, soft Nature blue/lavender/mint/coral palette, darkcharcoal crisp frames and curved arrows. Use clean modern Chinese sans-serif, horizontal baselines, perfectly upright text and mathematical symbols, generous spacing, no overall title. Large legible labels equivalent to at least 8.5pt at final book width. All quoted strings must be exactly spelled. No additional sentence explanation or fake text. Preserve all dataflow semantics. Produce high-resolution at least 2048px width if possible.
Add "原图" beneath firstbirdthumbnail; firstaugmentedbird above "裁剪"; second above orbelow "颜色变化"; distinctcat below "其他原图". Add "共享编码器 f_θ" along encoder emptywaist/top, no genericbrain. In rightrepresentationplane draw a SOLID bluecircle at normalized plane(35%,62%) labeled "z₁"; an OPEN bluecircle at plane(62%,57%) labeled "z₂"; a coralSQUARE at plane(77%,19%) labelled "z⁻". A mint doubleheaded short arrow connects the two bluecircles; coral dashedarrow from bluepair outward toward the square only indicatesrelative separation. Avoid exactaxisnumbers; add short label "表示空间" aboveplane. The samebirdtwo views matched, cat is from differentoriginal. Keep separatecatarrow entering sharedencoder, no originalbird→catarrow. Noextraformula.
```


阶段原始输出：/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-f78bfc13-23d3-4ae3-a667-8573488db4d6.png

## v1r3-active-learning.png

### 架构生成初稿

```text
Use case: scientific-educational. Create a publication-quality LINE-BASED SCIENTIFIC ARCHITECTURE diagram on pure white background. Frame outlines, wires, internal networks and purposeful curved paths are the main content. Flat pale blue data inputs, pale lavender computational modules, pale mint outputs, small coral feedback accents. Dark charcoal crisp outlines substantial at print size, uniform clean vector-like linework, Nature scientific schematic aesthetic. NO overall title, NO words, NO letters, NO digits, NO equation, NO watermark. All scientific text will be added later as editable typesetting. No human figure, no decorative brain, no cartoon storytelling, no shadow, no 3D, no texture, no gradient. Wide landscape canvas at least 2048px wide with generous whitespace. Small icons only support the architecture. Keep empty annotation areas inside modules.
Pool-based active learning architecture, ratio1.8:1. Left x5–43% two stacked EMPTY coordinate planes centered y28% and70%, thin dark axes, pale lavender curved separator but NO dots, NO digits, NO text. Right top x68%y23% a small line icon of labeling interface, a blank blue image card and mint tag, no human body. Right middle x85%y52% a mint labeled-data archive with three blank slim records. Center bottom x68%y77% a pale-purple model-update module, tiny internal mesh on left with empty interior. Large dark curved query path from upper left plane to labeling interface, then to data archive, then to model-update module, then to lower left plane; a coral dashed return path loops from lower pool to labeling interface for next iteration. Keep arrows outside modules, whitespace for overlay short labels. Exact uncertainty circles/data points/boundaries will be vector overlays so leave coordinate planes EMPTY, including no separator if uncertain.
```

### 原生中文与数学标注编辑

```text
Use case: text-localization. Edit this scientific architecture so all ESSENTIAL Chinese and mathematical labels are NATIVELY rendered as part of the image. Do NOT leave reserved empty annotation areas. Keep pure white background, soft Nature blue/lavender/mint/coral palette, darkcharcoal crisp frames and curved arrows. Use clean modern Chinese sans-serif, horizontal baselines, perfectly upright text and mathematical symbols, generous spacing, no overall title. Large legible labels equivalent to at least 8.5pt at final book width. All quoted strings must be exactly spelled. No additional sentence explanation or fake text. Preserve all dataflow semantics. Produce high-resolution at least 2048px width if possible.
Inside upper coordinateplane show seven small digit samples: three 3's mainlyleft, three 8's mainlyright, one uncertain3 nearcenter. Add purplecurvedboundarybetween3's and8's, circleuncertain3 withcoraloutline. Label aboveplane "样本池 t". Lowerplane samepositions/digits, retain oldboundarydotted, shift newboundaryrightward toward right-classdigit8, greenoutline on already-labelled3, coraloutline on next uncertain8; label above "样本池 t+1". Label long upper queryarrow ABOVE "查询". Label interface "标注接口", itsbluecard "3", itsminttag "y = 3". Labeleddataarchive "带标签集合 D_L". Purplemodelmodule emptyspace "重训". Label coraldashednextquery abovepath "下一轮". Curvesandpositions areillustrative. Keep meaningful loop pool→interface→labeledset→model→updatedpool→nextquery.
```

### 常规字体与最终机制修正

```text
Use case: precise-object-edit. Typography: replace EVERY label with attractive regular/light sans-serif, Chinese Source Han Sans / Noto Sans CJK REGULAR, Latin Source Sans3 REGULAR; slender normal-weight mathematical glyphs. Absolutely NO bold/heavy/black weight orcompressed/blocky letters. KEEPfont SIZE, Chinese wording, upright horizontal baselines, colors, frames and moduleobjectpositions. Size only for hierarchy. Labels visiblylighterthanframeoutlines. No overalltitle or longnewtext.
Correct exact before/after visualization: upperdecisioncurve should SOLIDpurple. All seven digitcoordinates must be identical inlowerpanel underverticaltranslation: upperfour3's includingCORALcircledcenter3, upperthree8's. Lowerrestorethat same CENTER3 with GREENcircle (currentlywronggreen3atleft); removegreenoutlinefromleft3. Retainall7digits atsameplaces. LowerOLDpurpleboundarysamecoordinatesasupperbutDOTTED; additionally draw a NEW SOLIDpurpleboundary shiftedright, withcoralcircledonnextuncertain8nearnewboundary. Existinglabelcaptionwill explain dashedoldsolidnew. Keepquery3target y=3, DL, retrainingloop, nofakeperformance. Fill modelmodule littleblankinset with short "θ⁽ᵗ⁺¹⁾".
```


阶段原始输出：/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-2dc8e31a-486c-408f-ae42-31c29ca968d2.png

## v1r3-meta-learning.png

### 架构生成初稿

```text
Use case: scientific-educational. Create a publication-quality LINE-BASED SCIENTIFIC ARCHITECTURE diagram on pure white background. Frame outlines, wires, internal networks and purposeful curved paths are the main content. Flat pale blue data inputs, pale lavender computational modules, pale mint outputs, small coral feedback accents. Dark charcoal crisp outlines substantial at print size, uniform clean vector-like linework, Nature scientific schematic aesthetic. NO overall title, NO words, NO letters, NO digits, NO equation, NO watermark. All scientific text will be added later as editable typesetting. No human figure, no decorative brain, no cartoon storytelling, no shadow, no 3D, no texture, no gradient. Wide landscape canvas at least 2048px wide with generous whitespace. Small icons only support the architecture. Keep empty annotation areas inside modules.
Task adaptation and meta-update architecture, ratio1.7:1. At x12%y35% one lavender shared-initialization module, empty interior. Three parallel train-task lanes y15%,35%,55%: at x36% a small pair of EMPTY pale-blue sample cards, x57% lavender adaptive module with tiny sparse mesh and empty center, x77% a pair of EMPTY blue check cards, x93% small coral circular loss node. Initial module branches into each adaptive module; support cards enter adaptive module; adapted output and separate check cards enter loss. Three losses aggregate via a coral dashed exterior feedback arc at bottom of train area y65%, returning ONLY to shared initialization. Thin dashed divider at y73%. New-task test lane at y88% uses same sequence shared initial x12→support x36→adapted x57→check x77→mint score x93, with NO feedback to training. No text or glyphs in cards; leave locations for exact typeset labels. Architecture dominates, not story.
```

### 机制线路修正

```text
Correct only the scientific wiring. CRUCIAL: Shared-initialization lavender module must connect DIRECTLY to each adapted lavender module, via independent curved routes that bypass the support cards. Do NOT route shared initialization into support samples. Support paired blue cards independently connect to adapted model. For each lane, adapted model arrow goes DIRECTLY to coral loss circle, passing BELOW the checkcards; checkpairedbluecards independently point down-and-right into samecoralloss. Do NOT route adapted model INTO checkcards. Three losses aggregate to coral dashedouterfeedback and sharedinitializer. Bottomnewtask: sharedinitial→adaptedmodeldirectly; supportcardsindependently→adapted; adapted→mintscoreDIRECTLY; checksindependently→score. No bottomfeedback. Keep module andcard positions, whitepastelstyling, noletters/text.
```

### 原生中文与数学标注编辑

```text
Use case: text-localization. Edit this scientific architecture so all ESSENTIAL Chinese and mathematical labels are NATIVELY rendered as part of the image. Do NOT leave reserved empty annotation areas. Keep pure white background, soft Nature blue/lavender/mint/coral palette, darkcharcoal crisp frames and curved arrows. Use clean modern Chinese sans-serif, horizontal baselines, perfectly upright text and mathematical symbols, generous spacing, no overall title. Large legible labels equivalent to at least 8.5pt at final book width. All quoted strings must be exactly spelled. No additional sentence explanation or fake text. Preserve all dataflow semantics. Produce high-resolution at least 2048px width if possible.
FIRST fixwiredefect: remove shared-initialization→upper SUPPORT cards arrow completely. Sharedinitialization connects ONLYDIRECTLY to three adaptedpurplemodels. Supportcards independentlyenteradaptedmodel, checksindependentlyenterloss, adaptedmodelgoesDIRECTLYtoloss (nevertochecks). Add "元训练" in left topwhitespace; sharedmodule "共同起点 θ". Columnabove supports "支持样本"; columnabove checks "检查样本". Put simple DIFFERENT 2symbol teachingglyphs in each support/checkpair, sameglyphidentities within task but slightlyrotated inchecks; no measuredOmniglotdata. Threeadaptedmodels labels "θ′_τ₁", "θ′_τ₂", "θ′_τ₃"; losscircles "L_τ₁", "L_τ₂", "L_τ₃". Coralfeedbacklabel abovebottompath "汇总损失，更新起点". Below dasheddivider small "元测试"; bottomshared "已学起点 θ"; adapted "θ′_τ*"; mintscore "评分". Bottomsupport/checkglyphs NEW identities, checks only→score, neverfeedback. Alllabels horizontal, readable, notrotated. No extra shared→samples edge.
```

### 常规字体与最终机制修正

```text
Use case: precise-object-edit. Typography: replace EVERY label with attractive regular/light sans-serif, Chinese Source Han Sans / Noto Sans CJK REGULAR, Latin Source Sans3 REGULAR; slender normal-weight mathematical glyphs. Absolutely NO bold/heavy/black weight orcompressed/blocky letters. KEEPfont SIZE, Chinese wording, upright horizontal baselines, colors, frames and moduleobjectpositions. Size only for hierarchy. Labels visiblylighterthanframeoutlines. No overalltitle or longnewtext.
Preserve EXACT currentcorrecttopology: sharedθdirectlytoadaptedθ′_τi, supportsindependentlytoadapted, checksindependentlytoloss, adaptedtolossdirectly. Traininglossesfeedbacktosharedonly; bottomscore nofeedback. AllcurrentChinese labels/glyphsamplesandmathaccurate, retainall. Do not addinitial→supportoradapted→checkedge. Use allChinese labels regularweight, including元训练元测试headers, charactersamplesandredfeedbacklabels.
```


阶段原始输出：/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-a0846edb-74a4-48b8-87b2-0545981bd07e.png

## v1r3-federated.png

### 架构生成初稿

```text
Use case: scientific-educational. Create a publication-quality LINE-BASED SCIENTIFIC ARCHITECTURE diagram on pure white background. Frame outlines, wires, internal networks and purposeful curved paths are the main content. Flat pale blue data inputs, pale lavender computational modules, pale mint outputs, small coral feedback accents. Dark charcoal crisp outlines substantial at print size, uniform clean vector-like linework, Nature scientific schematic aesthetic. NO overall title, NO words, NO letters, NO digits, NO equation, NO watermark. All scientific text will be added later as editable typesetting. No human figure, no decorative brain, no cartoon storytelling, no shadow, no 3D, no texture, no gradient. Wide landscape canvas at least 2048px wide with generous whitespace. Small icons only support the architecture. Keep empty annotation areas inside modules.
Federated model communication architecture, ratio1.55:1. Uppercenter x50%y12% lavender shared parameter module with tiny line network and blank central space. Three participant domains are crisp dark rounded outline frames occupying x5–30%,38–63%,71–96% between y33–73%. Inside EACH: left pale-blue blank local records card at xcolumnleft+7%y53%, right small lavender local model module at y43% and mint updated-parameter module at y65%, connected downward. Data arrow stays INSIDE domain from localrecords into localmodel. Sharedmodel has three blue routes into local models, external to frames. Three mint outbound routes from updated local parameter modules merge into lower-center x50%y89% mint aggregation module, blank interior. A single outer dark loop from aggregate around right margin returns to sharedmodel. Absolutely NO raw-data arrow crossing participant boundary. No text/digits, no decorative clouds/humans, only tiny device symbols as optional supporting icons.
```

### 机制线路修正

```text
Correct only scientific wiring. Remove ALL local coral feedback loops. Remove the center bidirectional vertical arrow. There must be exactly THREE BLUE ONE-WAY DOWN arrows from TOP shared module to the PURPLE MODEL inside each participant, never to data archive. The rawbluearchive must onlysend a short within-frame arrow to its localpurplemodel. Each localpurplemodel→mintupdatedmodule, then greenone-wayarrow from mintmodule toBOTTOMaggregation. Exactly one coral return path bottomaggregate→topshared along rightmargin. No other exterior arrows. Preserveframes, colorsandobjects. All labels and exactmathlater, noletters/text.
```

### 原生中文与数学标注编辑

```text
Use case: text-localization. Edit this scientific architecture so all ESSENTIAL Chinese and mathematical labels are NATIVELY rendered as part of the image. Do NOT leave reserved empty annotation areas. Keep pure white background, soft Nature blue/lavender/mint/coral palette, darkcharcoal crisp frames and curved arrows. Use clean modern Chinese sans-serif, horizontal baselines, perfectly upright text and mathematical symbols, generous spacing, no overall title. Large legible labels equivalent to at least 8.5pt at final book width. All quoted strings must be exactly spelled. No additional sentence explanation or fake text. Preserve all dataflow semantics. Produce high-resolution at least 2048px width if possible.
FIRSTfixall3bluedownarrowendpoints: land each arrow on TOP edge of its localPURPLEmodel, notin gap andnotbluearchive. 3 localmintupdatedmodules must connect continuously to bottomaggregation withgreenarrows. Topsharedmodule blankcenter "共享模型 θ⁽ᵗ⁾". Add "模型下发" above threebluepaths. Domains labeled "参与方1","参与方2","参与方3" justaboveframes. Each bluearchive labeled "D₁","D₂","D₃"; each localpurplemodule belowinternalmesh short "本地学习". Each mintupdatedmodule label "θ₁⁽ᵗ⁺¹⁾","θ₂⁽ᵗ⁺¹⁾","θ₃⁽ᵗ⁺¹⁾". Bottomaggregationmodule center twohorizontal lines "加权聚合" / "θ⁽ᵗ⁺¹⁾". Greenpaths short above "模型更新"; outercoralreturnpath shorthorizontal nearupperright "下一轮". No rawdata outboundarrow. No extra localfeedback. Formula subscripts/superscripts accurate.
```

### 常规字体与最终机制修正

```text
Use case: precise-object-edit. Typography: replace EVERY label with attractive regular/light sans-serif, Chinese Source Han Sans / Noto Sans CJK REGULAR, Latin Source Sans3 REGULAR; slender normal-weight mathematical glyphs. Absolutely NO bold/heavy/black weight orcompressed/blocky letters. KEEPfont SIZE, Chinese wording, upright horizontal baselines, colors, frames and moduleobjectpositions. Size only for hierarchy. Labels visiblylighterthanframeoutlines. No overalltitle or longnewtext.
Correct endpointdefects: each blueDOWNmodeldistributionroute must reach TOP CENTER of localPURPLE model, currently center/right arrowheads end inemptygap. Localpurplemodelcentersinthisimage roughlyx355,x866,x1375,y440, TOPedgey378. Set bluearrowheads at (355,378),(866,378),(1375,378) usingcurvedroutingasneeded, neverdataarchive. CenterGREENuploadroute currently starts disconnected fromparticipantframe: start atBOTTOM CENTER of MINTupdatedmodel (x866,y675), curvecontinuouslytowardbottomaggregation (x780,y812); leave NO gap. Left/rightgreenuploadalreadycomefrommintlocalmodelkeep. Preservealltheta mathsubscripts/superscripts,dataarchivesstayinglocal,currentcorrectotherwiring. Nativefont ALLregularweight.
```


阶段原始输出：/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-5b0c4eff-bdf1-402a-a192-a6136e709459.png

## 旧范式改色：v1r3-unsupervised.png

参考图：/Users/robbieshi/Notes/machine-learning/figures/02-foundations/01-basics/generated/paradigms-unsupervised-topics.png

```text
Use case: style-transfer. Edit this existing scientific diagram only to unify its style with Nature-style scientific schematics. Keep every document stack, new document, central learning machine, three topic output clusters (finance, sports, science), ALL arrows and endpoint topology EXACTLY unchanged. Pure white background, remove all paper texture and all shadows. Flat soft pale-blue data, pale-lavender model bodies, mint-green output accents, small muted coral knowledge/feedback accents. Charcoal crisp outlines around objects and paths, substantial elegant linework. Reduce saturation dramatically, remove navy/orange solid fields, no 3D bevel. Original imagery may remain as subordinate small illustrations. NO title, NO text, NO letters/digits, NO watermark. Do not invent a new connection or delete any object.
```

## 旧范式改色：v1r3-semi-supervised.png

参考图：/Users/robbieshi/Notes/machine-learning/figures/paradigms-semi-supervised-signals.png

```text
Use case: style-transfer. Edit this existing scientific diagram only to unify its style with Nature-style scientific schematics. Keep the four labeled top cards, large unlabeled bottom card pool, central learning machine with branching internal network rather than generic brain, and right bird output card EXACTLY at the same positions; keep all arrows/topology. Pure white background, remove all paper texture and all shadows. Flat soft pale-blue data, pale-lavender model bodies, mint-green output accents, small muted coral knowledge/feedback accents. Charcoal crisp outlines around objects and paths, substantial elegant linework. Reduce saturation dramatically, remove navy/orange solid fields, no 3D bevel. Original imagery may remain as subordinate small illustrations. NO title, NO text, NO letters/digits, NO watermark. Do not invent a new connection or delete any object.
```

## 旧范式改色：v1r3-continual.png

参考图：/Users/robbieshi/Notes/machine-learning/figures/paradigms-continual-memory.png

```text
Use case: style-transfer. Edit this existing scientific diagram only to unify its style with Nature-style scientific schematics. Keep all three stage input groups, same model outlines and model partitions, progressively accumulating internal knowledge fill, growing output class sets, stage transition arrows and backward memory arrows EXACTLY unchanged. Preserve object identity and number: bird/car, dog/boat, flower/tools, with cumulative output sets. Pure white background, remove all paper texture and all shadows. Flat soft pale-blue data, pale-lavender model bodies, mint-green output accents, small muted coral knowledge/feedback accents. Charcoal crisp outlines around objects and paths, substantial elegant linework. Reduce saturation dramatically, remove navy/orange solid fields, no 3D bevel. Original imagery may remain as subordinate small illustrations. NO title, NO text, NO letters/digits, NO watermark. Do not invent a new connection or delete any object.
```

## 根节点协助的旧范式改色

3.10、3.11、3.14 已替换为 [v1r3-multi-task-learning.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/01-basics/generated/v1r3-multi-task-learning.png)、`v1r3-transfer-learning.png`、`v1r3-combination-alphago.png`。具体提示与检查记录见 `volume1-r3-paradigm-restyle.md`。

## 最终物理尺寸与接口复核修订

图1.4的小标记“冻结选择”在111mm宽度下偏小，已仅放大该处原生文字。图3.13前几次局部编辑仍保留错误接口，未作为最终版本；随后整体重生成更直接的共享模型—本地模型—更新聚合架构，再修复中央上传连接并统一减轻原生字重。所有替换都经内置图像模型生成，无外加文字。

### data-split：末轮定向编辑（联邦图此阶段后已重生成）

```text
Change ONLY text size of the small label 冻结选择 beside dashed gate. Enlarge that exact label by 50% so it matches the other role-label size such as 冻结后评估, keeping Source Han Sans REGULAR upright horizontal, not bold. Place it just ABOVE the little lock with clear whitespace and no collision. All other font sizes, texts, frames, objects, arrows and colors unchanged. No overalltitle.
```

### federated：末轮定向编辑（联邦图此阶段后已重生成）

```text
Fix ONLY scientific arrow endpoint and typography/palette defects; do NOT add/delete any model or archive. MOST IMPORTANT: the blue arrow above the RIGHT participant currently ends to the LEFT of its purple model in empty space. REDRAW ONLY its final curved segment to reach the TOP-CENTER EDGE OF THE RIGHT PURPLE rectangle labelled 本地学习. The arrowhead must TOUCH that rectangle, landing above its central network node, not over its left neighboring blue D₃ archive. Route that final segment rightward before turning downward. Similarly center blue arrow should TOUCH top-center of middle purple rectangle 本地学习, not empty gap. Keep correct continuous green upload from each mint updatedmodel. Desaturate blue/green/coral path colors to muted soft Nature palette. All colored path labels 模型下发/模型更新/下一轮 and 加权聚合 must be thin REGULAR Source Han Sans/Noto Sans CJK, visibly lighter than frame outlines, not bold. Preserve exact wording and theta subscripts/superscripts, allpositions and internalobjects. No long explanation/newtitle.
```

### 3.13：完整架构重生成

```text
Use case: scientific-educational. Generate a NEW scientific LINE-BASED federated learning ARCHITECTURE with COMPLETE NATIVE Chinese and mathematical labels. This replaces a diagram whose arrows failed to touch their targets: ALL ARROWHEADS MUST TOUCH the intended module boundary with continuous wiring, especially ALL THREE model-downloading arrows. Show linework, frames, wires, neural meshes as main information; tiny deviceicons are supporting only. Pure white background, flat pale lavender models, pale-blue local data, pale-mint parameter updates, muted blue/green paths and muted coral outerreturn. Darkgray crisp substantial outlines. NO shadows, no gradient, no 3D, no overalltitle, no placeholder annotation strips. Native Chinese typography Source Han Sans/Noto Sans CJK REGULAR appearance, Latin Source Sans3 REGULAR, slender normalweight Greekmath; NO bold/heavy/blocky type. All labels horizontal, about 9pt at169mm width. Request crisp 2560×1600 pixel landscape canvas.
Precise layout and topology:
Top centered at(x50%,y12%) one sharedmodel lavender module label "共享模型 θ⁽ᵗ⁾", sparse internal mesh.
Three participant domains arranged left/center/right with rounded darkgray boundaryframes spanningy35%–74%, respective centersx17%,50%,83%. Frame identifiers "参与方1", "参与方2", "参与方3" just above frames.
Insideeachdomain: one BLUE dataarchive on LEFT (atdomaincenter−7%,y52%), labelled "D₁"/"D₂"/"D₃"; one PURPLE neuralmodule on RIGHT (atdomaincenter+5%,y45%) labelled "本地学习"; one MINT updatedparameter module BELOW that purple module(atdomaincenter+5%,y65%) labelled "θ₁⁽ᵗ⁺¹⁾"/"θ₂⁽ᵗ⁺¹⁾"/"θ₃⁽ᵗ⁺¹⁾". Local dataarchive sends shortwithin-framearrow directly into purplemodule. Purplemodule→mintupdatedmodule verticalarrow. Tiny laptop/monitor/phoneicons in lower-left of each participantoptional.
EXACTLY THREE MUTED BLUE ONE-WAY DOWNWARD ROUTES: sharedmodel BOTTOM boundary→TOP CENTER BOUNDARY of each PURPLE localmodule. Endpoints: atx22%,55%,88%,y37% respectively, touchingpurpleframe topedge. Noarrowmustendinemptygap orata dataarchive. Label above these routes "模型下发".
Bottom center at(x50%,y90%) MINT aggregation module with native "加权聚合" and "θ⁽ᵗ⁺¹⁾".
EXACTLY THREE MUTED GREEN uploadroutes: BOTTOM CENTER BOUNDARY of each local MINTupdatedparameter module→TOP boundary of bottomaggregate. CONTINUOUS paths originate FROM updatedmodel, notfrom participantboundary. Label upload "模型更新".
ExactlyONE mutedCORAL outerreturn path: aggregationRIGHT edge→alongRIGHTcanvasmargin→sharedmodelRIGHT edge, labelled "下一轮", touchingbothends.
NO otherconnections, NO localfeedbackloops, NO bidirectionalarrows. Rawdata NEVERcross participantboundary. Label texts/formulas must be correct and regularweight. Frame and neuralmesh details purposeful, no decorativefilledscene.
```

### 3.13：中央绿色上传修复

```text
Edit only the central green upload connection in this scientific architecture diagram. Preserve every object, module, native Chinese label, formula, blue downward path, coral outside next-round loop, and all colors exactly. The CENTRAL participant currently has a mint local-update module θ₂^(t+1), whose existing short green line descends from its bottom center to the participant-frame bottom. A separate wrong green vertical upload starts further left, leaving a disconnected gap. Delete that separate wrongly-left central green upload. Extend the existing green line STRAIGHT DOWN from the bottom center of the middle mint local-update module continuously, through the frame bottom, until it meets the TOP EDGE of the large bottom aggregation module at the same x coordinate, with a green arrowhead touching that top edge. This straight continuous route is the central participant's model update, not local data. Move its native horizontal label 模型更新 to the LEFT of the new vertical route with clear whitespace so the line never crosses any letter. Preserve the other two green uploads and their arrowheads. No new labels, no overlays, no added title. Keep all Chinese and mathematical characters regular/light clean sans-serif, no bold or heavy strokes. White background, pale Nature-style fills, crisp dark gray module outlines. The only change is to repair that central green connectivity and relocate its existing label slightly left.
```

### 3.13：原生字重修订

```text
Revise ONLY native typography in this finished scientific architecture diagram. Absolutely preserve every module, network node, color, line route, arrowhead endpoint, and connectivity; all three continuous green local-update uploads and the blue model-to-model downloads are now correct. Do not add or delete any element. Keep the same exact Chinese text and mathematical formulas, the same font sizes, label positions, and horizontal baselines. Reduce ALL Chinese label stroke thickness by about 40–50%, especially the blue 模型下发 and green 模型更新, to attractive clean regular/light sans-serif consistent with the black 本地学习 labels. Appearance reference: Source Han Sans/Noto Sans CJK Regular or Light for Chinese and Source Sans 3 Regular for Latin; this is an appearance request, not a claim of actual font embedding. No bold, heavy, black-weight, compressed, or blocky letters anywhere, including 参与方1/2/3, 共享模型, 加权聚合 and 下一轮. Keep math typesetting light regular italic where appropriate, with readable indices and superscripts. Preserve the white background and soft pale blue/lavender/mint modules exactly. No overall title and no added text.
```

## 最终采用的原始输出

这些源图以工作区 `figures/scenes/v1r3-*.png` 文件为实际引用；前述“阶段输出”只保留生成轨迹。字体名称仅表示外观参考，不声称栅格图片嵌入了某种字体。

- [v1r3-nlp-tasks.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/01-basics/generated/v1r3-nlp-tasks.png)：`/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-ce9f5839-1a58-4de1-9d5f-711a19480222.png`
- [v1r3-data-split.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/01-basics/generated/v1r3-data-split.png)：`/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-b0df4cde-e780-40da-b44e-de4ebf0a08d6.png`
- [v1r3-supervised.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/01-basics/generated/v1r3-supervised.png)：`/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-7e75ec8c-6003-4189-a147-6867b53e286b.png`
- [v1r3-reinforcement-upper.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/01-basics/generated/v1r3-reinforcement-upper.png)：`/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-09faac7b-8c2a-45da-b10e-5a40245e716a.png`
- [v1r3-contrastive.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/01-basics/generated/v1r3-contrastive.png)：`/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-f78bfc13-23d3-4ae3-a667-8573488db4d6.png`
- [v1r3-active-learning.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/01-basics/generated/v1r3-active-learning.png)：`/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-b9d2b25d-9c35-4675-81a8-b92beae2ba2c.png`
- [v1r3-federated.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/01-basics/generated/v1r3-federated.png)：`/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-1ef98ae6-1be7-480b-8dca-c5c55e7c4b54.png`
- [v1r3-unsupervised.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/01-basics/generated/v1r3-unsupervised.png)：`/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-b9c83d10-540c-4557-ac80-08ab7bbd2cef.png`
- [v1r3-semi-supervised.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/01-basics/generated/v1r3-semi-supervised.png)：`/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-b41df9bd-325d-4abb-bc36-bc8dbafbb54d.png`
- [v1r3-continual.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/01-basics/generated/v1r3-continual.png)：`/Users/robbieshi/.codex/generated_images/01a1095d-88df-7112-97e9-3d6f1631669b/exec-bd526713-cabb-43ea-b47c-3a28533d7c63.png`

图3.12最终字体细化由根节点完成并直接保存 [v1r3-meta-learning.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/01-basics/generated/v1r3-meta-learning.png)，原始输出及具体提示见 `volume1-r3-meta-fonts.md`。图3.10、3.11、3.14见 `volume1-r3-paradigm-restyle.md`。最终书中宽度111mm或168mm；未为提高名义DPI进行人工插值放大。

## 图3.8：实际书宽下的最终字重修订

大图预览通过后，169mm独立校样仍显示局部中文粗于图3.12，故减轻所有中文笔画；数据中的手写数字仍作为样本图元保留。第二次仅将仍偏粗的“下一轮”改成细常规字重、深灰文字，所有已核对边界、样本、箭头与公式保持。

```text
Edit ONLY native typography in this scientific active-learning architecture, preserving the complete correct content, all sample glyphs and their exact positions, all rings, every solid and dotted old/new boundary, every module frame, every arrow route and arrowhead. Chinese text currently looks bold, particularly 样本池 t, 样本池 t+1, 查询, 标注接口, 带标签集合 D_L and 重训. Replace ALL Chinese labels with substantially lighter elegant regular/light sans-serif, reducing stroke thickness by approximately 50%. Preserve current FONT SIZE exactly: do not make any label smaller. Appearance reference: Source Han Sans/Noto Sans CJK Regular or Light; Latin Source Sans 3 Regular, delicate normal-weight math. No bold, heavy, black-weight, condensed or blocky letters anywhere. Keep exact spelling of every label, all indices and superscripts, horizontal baselines, and same placement. Preserve the handwritten 3 and 8 SAMPLE DIGITS as glyph samples rather than converting them to text; these data samples may retain their handwritten appearance. Do not alter the purple decision boundaries or the central green-ringed acquired 3 and right coral-ringed next-query 8 in the lower pool. The upper current boundary is solid; the lower previous boundary is dotted and the lower updated boundary is solid. The next-round dashed path and all other scientific wiring must remain unchanged. No new text and no overall title. Pure white background and current pale Nature colors preserved exactly.
```

```text
Modify ONLY the Chinese text label 下一轮 near the center-left dashed coral feedback route. That one label is still bold, while the other labels are now elegant regular/light weight and correct. Make 下一轮 thin REGULAR/LIGHT sans-serif with approximately HALF its current stroke thickness, same current font SIZE, exact same wording and horizontal baseline, same position; render it in dark gray #222222 for legibility. Do not alter any other text, sample digit, color, fill, module, boundary curve, ring, arrow route, endpoint, spacing or layout. In particular preserve upper solid boundary and lower dotted previous plus solid updated boundaries, the lower acquired central green-ringed 3, next-query right coral-ringed 8, all continuous correct arrows, and all accurate formulas. Only replace the appearance of the existing 下一轮 label. No overall title, no extra text.
```
