# 可信机器学习概念插图记录

- 生成日期：2026-10-02。
- 工具：Codex 内置 `image_gen`；工具未公开具体模型标识。
- 风格参考：第3章“学习范式简介”的生成式概念插图，浅纸色背景、深蓝轮廓、蓝绿与暖橙配色。
- 输出：1536×1024 PNG；原样复制至本目录，未修改画面内容。
- 性质：原创教学情景，不是论文原图、真实案例数据、实验结果或精确模型拓扑。中文解释、情景假设与适用边界放在 LaTeX 正文和图注中。

## 自动处理与人工复核

文件：[trust-reliability-review.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/03-trustworthiness/generated/trust-reliability-review.png)

提示词：

> Use case: scientific-educational. Create a textbook conceptual illustration, 3:2 landscape, 1536x1024. Warm off-white paper background, refined flat editorial illustration, vector-like shapes with subtle paper texture, dark navy outlines, muted teal, slate blue, warm amber and pale gray. No gradients, shadows, 3D, logos or watermarks. No text, letters, numerals, formulas or pseudo-text. Generous whitespace and few large objects, readable at printed width 112 mm. Explain cautious use of an email classifier: left, two incoming email cards, one clearly recognizable newsletter card with a small megaphone icon and one ambiguous envelope with both a personal portrait seal and a megaphone seal; center, a single teal classifier device containing a simple connected-node pictogram; right, two clearly separated routing destinations. Upper destination is a reversible quarantine folder containing the recognizable newsletter card; lower destination is a human reviewer at a desk inspecting the ambiguous card with a magnifying glass. Clear arrows run from input into classifier, then separately to each destination. Above each outgoing route place a small icon-only decision marker: a single solid teal category token on the upper route; two differently shaped competing category tokens on the lower route. The image illustrates selective automation and referral, not a probability calibration chart and not a guarantee that the reviewer is infallible. Do not show deletion or a trash bin.

## 相同资格下的不同待遇

文件：[trust-fairness-opportunity.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/03-trustworthiness/generated/trust-fairness-opportunity.png)

提示词：

> Use case: scientific-educational. Textbook conceptual illustration, 3:2 landscape. Warm off-white paper background, refined flat editorial illustration, vector-like shapes with subtle paper texture. Dark navy outlines, muted teal, slate blue, warm amber, pale gray. No gradients, shadows, 3D, text, letters, numerals, formulas, pseudo-text, logos, or watermarks. Generous whitespace, large pictograms readable at printed width 112 mm. Not an experimental result or precise system diagram. Show unequal opportunity through two comparable training-course applicants. Two balanced horizontal rows separated by ample whitespace. In each row, one anonymous adult applicant holds a portfolio bearing the SAME three task qualification pictograms (a gear, a completed puzzle, a pencil). Their clothing is neutral and their faces schematic. Their folder covers differ only in an irrelevant decorative corner pattern: upper has diagonal stripes and lower has dots. Both applicant rows each point to the SAME-looking teal decision device. Upper row continues through an open door to a classroom with chairs and a blackboard bearing only a gear pictogram. Lower row stops at a closed gate in front of the same classroom. Use small distinct circular check and cross markers by the gates if needed, no words. Make equal qualification but different treatment visually evident. Do not encode ethnicity, gender, disability or real protected traits; this is a constructed example of irrelevant-template discrimination, with the assumption explained in the external caption.

## 可测指标与实际目标

文件：[trust-alignment-mail-goal.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/03-trustworthiness/generated/trust-alignment-mail-goal.png)

提示词：

> Use case: scientific-educational. Textbook conceptual illustration, 3:2 landscape. Warm off-white paper background, refined flat editorial illustration, vector-like shapes with subtle paper texture. Dark navy outlines, muted teal, slate blue, warm amber, pale gray. No gradients, shadows, 3D, text, letters, numerals, formulas, pseudo-text, logos, or watermarks. Generous whitespace, large pictograms readable at printed width 112 mm. Not an experimental result or precise system diagram. Show two different ways an automated assistant can make an inbox look empty, with different actual consequences. A split-panel illustration separated by a thin vertical pale rule. Both panels have the same compact teal assistant device and the same original three envelope icons; one envelope bears a prominent amber star denoting important content. Left panel: assistant empties an inbox by sending ALL envelopes including the star-marked important one into a wastebasket. Right panel: assistant empties the inbox by moving the same envelopes into orderly, retrievable folders, with the starred envelope prominently visible and intact. A human user next to the right panel can retrieve the starred envelope. Empty inbox trays visible in both panels; actual outcomes different. No reward charts, no numeric claims. The amber star must identify the SAME important message throughout. A large navy curved arrow to each chosen destination is enough; keep the scene uncluttered.

## 删除记录与消除训练影响

文件：[trust-privacy-deletion.png](https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/03-trustworthiness/generated/trust-privacy-deletion.png)

提示词：

> Use case: scientific-educational. Textbook conceptual illustration, 3:2 landscape. Warm off-white paper background, refined flat editorial illustration, vector-like shapes with subtle paper texture. Dark navy outlines, muted teal, slate blue, warm amber, pale gray. No gradients, shadows, 3D, text, letters, numerals, formulas, pseudo-text, logos, or watermarks. Generous whitespace, large pictograms readable at printed width 112 mm. Not an experimental result or precise system diagram. Show why deleting a training record is different from removing its influence from a trained model. Two side-by-side still-life scenes separated by whitespace. Left: a person removes one distinctive envelope card marked with an amber flower seal from a small archive drawer of plain envelope cards, placing that distinctive card in a shredding slot; the drawer is now missing that card. Right: a previously trained teal model device (simple connected-node icon, not exact topology) still produces a small envelope fragment bearing the SAME amber flower seal at its output. A small magnifying glass is aimed at the fragment. A faint arrow from the original archive area to the device indicates earlier learning, while deletion acts only at the archive. This is a schematic illustrative possibility of memorization, not a claim every deleted record can be reconstructed. Avoid any readable private text, locking icons that would wrongly imply a guarantee, literal people inside a model, or precise metrics.
