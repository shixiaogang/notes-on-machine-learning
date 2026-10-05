# 第一卷第三轮：隐私与安全架构图生成记录
日期：2026-10-05。工具：Codex 内置 image_gen；工具未返回具体模型版本。参数：白色不透明背景，参考图用于视觉风格，不转移其科研机制。以下是早期候选的生成记录；其留白标注方案已弃用。最终成品的全部标注由图像模型直接生成，见 volume1-r3-native-labels.md；定量密度为独立解析绘图。

参考：[Nature Communications scAGDE Figure 1](https://www.nature.com/articles/s41467-025-57027-x/figures/1)。用户明确选择框、线、箭头、文字为主的架构表达，具象图标为辅；首个较具象的候选未采用。

## membership-inference

资源：`figures/scenes/v1r3-membership-inference.png`。内置工具原始输出：`/Users/robbieshi/.codex/generated_images/01a108ff-bacd-7620-806b-20971b190207/exec-a48ecb75-1507-4415-8353-9ab751a655e0.png`。

生成提示词：

```text
Membership inference architecture. Five horizontal modules, centers x=.10,.32,.53,.73,.92 at y=.48. First is a small blue pair of data-record stacks with one envelope candidate; second lavender closed neural classifier; third sage interface output with a small abstract score icon; fourth lavender attack classifier with magnifying-glass icon (no person); fifth simple two-slot membership decision module. Exactly four forward arrows connecting adjacent modules horizontally. Above fourth module a small auxiliary training-record group feeds it with one curved downward arrow, separated from first three modules. No direct truth signal to attack classifier. All module elements at same height except auxiliary group. Output a clean LINE-BASED SCIENTIFIC ARCHITECTURE FIGURE on white, very wide 3:1. The user's attached reference is STYLE ONLY. Main content must be substantial dark-gray module outlines, neural-line schematics, precise directional connectors and arrowheads. Modest email, brain, database, shield icons inside modules support the structure; NO human characters, NO large conceptual artwork. Muted flat fills: input blue, model lavender, output sage, exceptions coral. Strong 1.2pt-equivalent outlines at final 168mm. Curved arrows only where helpful to feedback; straight horizontal forward connections. No shadows, 3D, gradients, glossy art, decoration, giant titles or logos. No text, letters, numbers or formulas: leave blank room inside/under each module for accurate editable labels. Keep every module/arrow separated from that label space. Match consistent visual language across all requested diagrams.
```

## dp-noise

资源：`figures/scenes/v1r3-dp-noise.png`。内置工具原始输出：`/Users/robbieshi/.codex/generated_images/01a108ff-bacd-7620-806b-20971b190207/exec-b3eeca52-9778-4537-ac59-24ffbad95a7b.png`。

生成提示词：

```text
Differential privacy architecture, two adjacent alternative publish paths. LEFT at x=.25: blue dataset containing exactly THREE simple record icons. RIGHT at x=.75: same THREE blue records plus exactly ONE coral extra record. Beneath each stack a count module, then a circular PLUS node, then a sage released-value module. A single small lavender noise-source module at x=.50 y=.45 connects separately to both plus nodes with symmetric curved arrows; each plus node has ONE count input and ONE independent noise input. Each release is an alternative mechanism execution, not simultaneous joint release. Do not generate plots. Compact layout with clear empty lower label band. Output a clean LINE-BASED SCIENTIFIC ARCHITECTURE FIGURE on white, very wide 3:1. The user's attached reference is STYLE ONLY. Main content must be substantial dark-gray module outlines, neural-line schematics, precise directional connectors and arrowheads. Modest email, brain, database, shield icons inside modules support the structure; NO human characters, NO large conceptual artwork. Muted flat fills: input blue, model lavender, output sage, exceptions coral. Strong 1.2pt-equivalent outlines at final 168mm. Curved arrows only where helpful to feedback; straight horizontal forward connections. No shadows, 3D, gradients, glossy art, decoration, giant titles or logos. No text, letters, numbers or formulas: leave blank room inside/under each module for accurate editable labels. Keep every module/arrow separated from that label space. Match consistent visual language across all requested diagrams.
```

## unlearning

资源：`figures/scenes/v1r3-unlearning.png`。内置工具原始输出：`/Users/robbieshi/.codex/generated_images/01a108ff-bacd-7620-806b-20971b190207/exec-8514019f-7af2-4899-86a1-b3fc1d851352.png`。

生成提示词：

```text
Machine unlearning architecture, TWO horizontal aligned tracks. UPPER centers x=.10,.35,.57,.78 at y=.33: original blue database with one coral withdrawn record; original lavender neural model; circular lavender unlearning operator with small eraser; resulting lavender neural model. Connect upper database to original model, original model to operator, operator to result. One separate curved coral arc from original database reaches the unlearning operator to supply original records and withdrawal set. LOWER at y=.72: cleaned blue database at x=.10; independent fresh lavender retrained model at x=.78, connected by a long straight arrow. A small comparison gate at x=.92 midway accepts output from upper result and lower retrained model. NO direct arrow from deleting a record to changing old model. Output a clean LINE-BASED SCIENTIFIC ARCHITECTURE FIGURE on white, very wide 3:1. The user's attached reference is STYLE ONLY. Main content must be substantial dark-gray module outlines, neural-line schematics, precise directional connectors and arrowheads. Modest email, brain, database, shield icons inside modules support the structure; NO human characters, NO large conceptual artwork. Muted flat fills: input blue, model lavender, output sage, exceptions coral. Strong 1.2pt-equivalent outlines at final 168mm. Curved arrows only where helpful to feedback; straight horizontal forward connections. No shadows, 3D, gradients, glossy art, decoration, giant titles or logos. No text, letters, numbers or formulas: leave blank room inside/under each module for accurate editable labels. Keep every module/arrow separated from that label space. Match consistent visual language across all requested diagrams.
```

## threat-model

资源：`figures/scenes/v1r3-threat-model.png`。内置工具原始输出：`/Users/robbieshi/.codex/generated_images/01a108ff-bacd-7620-806b-20971b190207/exec-99492fc7-bbf8-4b24-a2ac-34a4b7c8919a.png`。

生成提示词：

```text
Threat model architecture with three independent side-by-side panels, not a sequential pipeline. LEFT blue-outlined visibility boundary encloses a locked lavender neural classifier and sage category output; outside a small query-envelope icon. MIDDLE blue-outlined control boundary encloses TWO envelopes, original and edited with same coral fish-hook symbol, connected by one arrow; a database icon outside the boundary has a lock and is uneditable. RIGHT coral-outlined success-condition boundary encloses a fish-hook envelope entering lavender classifier and then sage accept outcome; coral warning mark at acceptance signals the failure event. Only internal causal arrows, NO arrow connecting the three panels. Leave wide blank text label spaces at top and bottom of each panel; no overall title. Output a clean LINE-BASED SCIENTIFIC ARCHITECTURE FIGURE on white, very wide 3:1. The user's attached reference is STYLE ONLY. Main content must be substantial dark-gray module outlines, neural-line schematics, precise directional connectors and arrowheads. Modest email, brain, database, shield icons inside modules support the structure; NO human characters, NO large conceptual artwork. Muted flat fills: input blue, model lavender, output sage, exceptions coral. Strong 1.2pt-equivalent outlines at final 168mm. Curved arrows only where helpful to feedback; straight horizontal forward connections. No shadows, 3D, gradients, glossy art, decoration, giant titles or logos. No text, letters, numbers or formulas: leave blank room inside/under each module for accurate editable labels. Keep every module/arrow separated from that label space. Match consistent visual language across all requested diagrams.
```

## security-entrypoints

资源：`figures/scenes/v1r3-security-entrypoints.png`。内置工具原始输出：`/Users/robbieshi/.codex/generated_images/01a108ff-bacd-7620-806b-20971b190207/exec-0294f81b-c13e-42a0-8ffb-85453142e13c.png`。

生成提示词：

```text
Attack surface architecture. Five aligned modules along one horizontal baseline: blue training database, lavender parameter-update mesh, lavender signed-package component, blue prediction-query interface, sage inbox/action target. Exactly four straight forward arrows form the service chain. Above each module a small distinct coral intrusion token reaches that module with a short downward arrow: corrupted record, malicious update, substituted package, edited query envelope, unauthorized action token. Each arrow terminates at its associated object; do not connect the five red tokens together. Labels will be added underneath. Output a clean LINE-BASED SCIENTIFIC ARCHITECTURE FIGURE on white, very wide 3:1. The user's attached reference is STYLE ONLY. Main content must be substantial dark-gray module outlines, neural-line schematics, precise directional connectors and arrowheads. Modest email, brain, database, shield icons inside modules support the structure; NO human characters, NO large conceptual artwork. Muted flat fills: input blue, model lavender, output sage, exceptions coral. Strong 1.2pt-equivalent outlines at final 168mm. Curved arrows only where helpful to feedback; straight horizontal forward connections. No shadows, 3D, gradients, glossy art, decoration, giant titles or logos. No text, letters, numbers or formulas: leave blank room inside/under each module for accurate editable labels. Keep every module/arrow separated from that label space. Match consistent visual language across all requested diagrams.
```

## prompt-injection

资源：`figures/scenes/v1r3-prompt-injection.png`。内置工具原始输出：`/Users/robbieshi/.codex/generated_images/01a108ff-bacd-7620-806b-20971b190207/exec-340bf2ce-535b-4a5c-ad5e-c748b3ad85bc.png`。

生成提示词：

```text
Prompt injection and authorization architecture. Wide two-row routing. Far left TOP blue user-task envelope; far left BOTTOM third-party email containing coral abstract command stripe. Both feed a central lavender model-context/neural module through distinct paths. Model outputs a two-row proposal module center-right: upper sage archive token; lower coral deletion token. Far right a VERTICAL independent permission gate separates proposals from action objects. ABOVE the gate a trusted blue key/authorization module has one arrow downward into gate. The upper sage proposal passes gate to blue mailbox A. The lower coral proposal stops at a red T-bar before gate; blue email B beyond gate remains intact. IMPORTANT no connection from external email to trusted authorization. Need clean unobstructed editable-label space. Output a clean LINE-BASED SCIENTIFIC ARCHITECTURE FIGURE on white, very wide 3:1. The user's attached reference is STYLE ONLY. Main content must be substantial dark-gray module outlines, neural-line schematics, precise directional connectors and arrowheads. Modest email, brain, database, shield icons inside modules support the structure; NO human characters, NO large conceptual artwork. Muted flat fills: input blue, model lavender, output sage, exceptions coral. Strong 1.2pt-equivalent outlines at final 168mm. Curved arrows only where helpful to feedback; straight horizontal forward connections. No shadows, 3D, gradients, glossy art, decoration, giant titles or logos. No text, letters, numbers or formulas: leave blank room inside/under each module for accurate editable labels. Keep every module/arrow separated from that label space. Match consistent visual language across all requested diagrams.
```

## defense-depth

资源：`figures/scenes/v1r3-defense-depth.png`。内置工具原始输出：`/Users/robbieshi/.codex/generated_images/01a108ff-bacd-7620-806b-20971b190207/exec-758627fc-05ae-48da-bc82-2f8e61e90061.png`。

生成提示词：

```text
Defense-in-depth architecture, TWO aligned horizontal service lanes and one shared audit lane. TOP: coral-marked incoming-record module, blue source-check gate, lavender isolated candidate-training module, sage approved-model package. Three forward arrows. One coral reject branch downward at source gate, one coral hold branch downward at isolated model. LOWER: third-party email, blue query filter, lavender proposal module, independent blue permission gate, safe blue inbox. Forward flow to permission gate, but a coral proposal terminates at a T-bar before the inbox. BOTTOM separate blue audit-log module flows to pause/revoke module then restore module, with subtle dotted observation links from service lanes; observation lines do not grant permissions. Use two compact row outlines only if needed to identify lifecycle boundaries, no nested decorative boxes. Output a clean LINE-BASED SCIENTIFIC ARCHITECTURE FIGURE on white, very wide 3:1. The user's attached reference is STYLE ONLY. Main content must be substantial dark-gray module outlines, neural-line schematics, precise directional connectors and arrowheads. Modest email, brain, database, shield icons inside modules support the structure; NO human characters, NO large conceptual artwork. Muted flat fills: input blue, model lavender, output sage, exceptions coral. Strong 1.2pt-equivalent outlines at final 168mm. Curved arrows only where helpful to feedback; straight horizontal forward connections. No shadows, 3D, gradients, glossy art, decoration, giant titles or logos. No text, letters, numbers or formulas: leave blank room inside/under each module for accurate editable labels. Keep every module/arrow separated from that label space. Match consistent visual language across all requested diagrams.
```
