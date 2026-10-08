# 原生标注与常规字重修订

日期：2026-10-05。工具：内置 image_gen，精确模型版本未返回。七张原生标注图经过仅字体修订，最终成品不用任何文字覆盖，只有差分隐私下方的定量密度图仍为独立的解析 TikZ 图。字体名称用于外观参考，生成结果不宣称嵌入指定字库。

## membership-inference

输出：`https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/03-trustworthiness/generated/v1r3-membership-inference.png`。

原生标注提示：

User requires labels to be generated DIRECTLY IN THE IMAGE, not added later. Preserve this exact LINE-BASED ARCHITECTURE and all scientific relationships. Render all specified Chinese labels accurately with clear horizontal upright sans-serif lettering, consistent size and baseline, dark gray. Typeset formulas cleanly. Adjust local spacing if needed so letters do not touch borders, icons or arrows. Do NOT leave any empty text strips; remove unused label strips. No overall title, no paragraphs, no new decorative icons. Preserve white background, pastel blue/lavender/sage/coral, substantial dark-gray lines. Keep original wide aspect and output resolution. Under the five main modules left to right add these exact labels: “候选 z”, “目标 f=A(D)”, “输出 p(z)”, “攻击器 a(z)”, “成员预测 m̂”. Above the small auxiliary database add “辅助训练数据”. These are ALL labels; do not include real membership truth as attack input or numerical probabilities.

字体修订提示：

Change ONLY the typography of this already correct scientific architecture illustration. Every existing letter, Chinese character, number, and mathematical symbol is currently TOO BOLD. Redraw ALL existing text as elegant NORMAL REGULAR-WEIGHT clean sans serif: Chinese visual reference Source Han Sans / Noto Sans CJK SC Regular (400), Latin Source Sans 3 Regular (400), formulas regular weight. All glyph strokes must visibly become about HALF AS THICK as in the input. NO BOLD, NO SEMIBOLD, no black-heavy lettering anywhere, including short headings. Use dark slate gray text rather than pure black. Keep all label wording, capitalization, formulas and punctuation exactly identical and preserve positions, horizontal baselines, original size and legibility. Keep every icon, all architecture, line widths, fills, arrows and every scientific relationship unchanged. Do not add or erase labels, titles or symbols. Render the lighter text DIRECTLY IN THE OUTPUT IMAGE; no blank bands.

检查：字重已明显变细；必要标签水平可读；对象、连线路由、独立权限及已阻断分支保持原意。

## dp-noise

输出：`https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/03-trustworthiness/generated/v1r3-dp-noise.png`。

原生标注提示：

User requires labels to be generated DIRECTLY IN THE IMAGE, not added later. Preserve this exact LINE-BASED ARCHITECTURE and all scientific relationships. Render all specified Chinese labels accurately with clear horizontal upright sans-serif lettering, consistent size and baseline, dark gray. Typeset formulas cleanly. Adjust local spacing if needed so letters do not touch borders, icons or arrows. Do NOT leave any empty text strips; remove unused label strips. No overall title, no paragraphs, no new decorative icons. Preserve white background, pastel blue/lavender/sage/coral, substantial dark-gray lines. Keep original wide aspect and output resolution. At LEFT top dataset label “D”, right top “D′”. Under left count module “计数 3”, right “计数 4”. Replace the brain/database icons in the CENTRAL noise-source module with a simple dice/randomness icon, label “随机噪声”. Label the left released output “3+Z” and right “4+Z′”. Beneath the two alternatives set “Z,Z′ ∼ Laplace(0,1)” in ONE horizontal line. Ensure every label has its own clear space rather than crossing an icon. All three-versus-four record cards and two plus nodes retained; independent noise enters each plus node. No generated density plot or additional headline.

字体修订提示：

Change ONLY the typography of this already correct scientific architecture illustration. Every existing letter, Chinese character, number, and mathematical symbol is currently TOO BOLD. Redraw ALL existing text as elegant NORMAL REGULAR-WEIGHT clean sans serif: Chinese visual reference Source Han Sans / Noto Sans CJK SC Regular (400), Latin Source Sans 3 Regular (400), formulas regular weight. All glyph strokes must visibly become about HALF AS THICK as in the input. NO BOLD, NO SEMIBOLD, no black-heavy lettering anywhere, including short headings. Use dark slate gray text rather than pure black. Keep all label wording, capitalization, formulas and punctuation exactly identical and preserve positions, horizontal baselines, original size and legibility. Keep every icon, all architecture, line widths, fills, arrows and every scientific relationship unchanged. Do not add or erase labels, titles or symbols. Render the lighter text DIRECTLY IN THE OUTPUT IMAGE; no blank bands.

检查：字重已明显变细；必要标签水平可读；对象、连线路由、独立权限及已阻断分支保持原意。

## unlearning

输出：`https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/03-trustworthiness/generated/v1r3-unlearning.png`。

原生标注提示：

User requires labels to be generated DIRECTLY IN THE IMAGE, not added later. Preserve this exact LINE-BASED ARCHITECTURE and all scientific relationships. Render all specified Chinese labels accurately with clear horizontal upright sans-serif lettering, consistent size and baseline, dark gray. Typeset formulas cleanly. Adjust local spacing if needed so letters do not touch borders, icons or arrows. Do NOT leave any empty text strips; remove unused label strips. No overall title, no paragraphs, no new decorative icons. Preserve white background, pastel blue/lavender/sage/coral, substantial dark-gray lines. Keep original wide aspect and output resolution. Upper row exact labels left to right: “D”, “A(D)”, “遗忘 U”, “U(A(D),D,F)”. Over the coral curved input into U place “D,F”. Lower row left dataset label “D∖F”, above long horizontal training arrow “重新训练 A”, under lower model “A(D∖F)”. Under far-right balance/comparison icon label “比较输出分布”. The upper resulting model and lower retrained model are being compared, NOT certified already equal. No check/shield icons. These are ALL labels.

字体修订提示：

Change ONLY the typography of this already correct scientific architecture illustration. Every existing letter, Chinese character, number, and mathematical symbol is currently TOO BOLD. Redraw ALL existing text as elegant NORMAL REGULAR-WEIGHT clean sans serif: Chinese visual reference Source Han Sans / Noto Sans CJK SC Regular (400), Latin Source Sans 3 Regular (400), formulas regular weight. All glyph strokes must visibly become about HALF AS THICK as in the input. NO BOLD, NO SEMIBOLD, no black-heavy lettering anywhere, including short headings. Use dark slate gray text rather than pure black. Keep all label wording, capitalization, formulas and punctuation exactly identical and preserve positions, horizontal baselines, original size and legibility. Keep every icon, all architecture, line widths, fills, arrows and every scientific relationship unchanged. Do not add or erase labels, titles or symbols. Render the lighter text DIRECTLY IN THE OUTPUT IMAGE; no blank bands.

检查：字重已明显变细；必要标签水平可读；对象、连线路由、独立权限及已阻断分支保持原意。

## threat-model

输出：`https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/03-trustworthiness/generated/v1r3-threat-model.png`。

原生标注提示：

User requires labels to be generated DIRECTLY IN THE IMAGE, not added later. Preserve this exact LINE-BASED ARCHITECTURE and all scientific relationships. Render all specified Chinese labels accurately with clear horizontal upright sans-serif lettering, consistent size and baseline, dark gray. Typeset formulas cleanly. Adjust local spacing if needed so letters do not touch borders, icons or arrows. Do NOT leave any empty text strips; remove unused label strips. No overall title, no paragraphs, no new decorative icons. Preserve white background, pastel blue/lavender/sage/coral, substantial dark-gray lines. Keep original wide aspect and output resolution. Three independent panels, upper short labels left to right exactly “知识”, “控制”, “目标”. Lower labels respectively exactly “只见预测类别”, “措辞可改；数据库不可改”, “钓鱼邮件被放行”. Make the second lower label fit in ONE neat line inside its panel. No other text. Retain independent panels, classifier locked/hidden parameters, permitted email edit and outside locked database, false accept event at right.

字体修订提示：

Change ONLY the typography of this already correct scientific architecture illustration. Every existing letter, Chinese character, number, and mathematical symbol is currently TOO BOLD. Redraw ALL existing text as elegant NORMAL REGULAR-WEIGHT clean sans serif: Chinese visual reference Source Han Sans / Noto Sans CJK SC Regular (400), Latin Source Sans 3 Regular (400), formulas regular weight. All glyph strokes must visibly become about HALF AS THICK as in the input. NO BOLD, NO SEMIBOLD, no black-heavy lettering anywhere, including short headings. Use dark slate gray text rather than pure black. Keep all label wording, capitalization, formulas and punctuation exactly identical and preserve positions, horizontal baselines, original size and legibility. Keep every icon, all architecture, line widths, fills, arrows and every scientific relationship unchanged. Do not add or erase labels, titles or symbols. Render the lighter text DIRECTLY IN THE OUTPUT IMAGE; no blank bands.

检查：字重已明显变细；必要标签水平可读；对象、连线路由、独立权限及已阻断分支保持原意。

## security-entrypoints

输出：`https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/03-trustworthiness/generated/v1r3-security-entrypoints.png`。

原生标注提示：

User requires labels to be generated DIRECTLY IN THE IMAGE, not added later. Preserve this exact LINE-BASED ARCHITECTURE and all scientific relationships. Render all specified Chinese labels accurately with clear horizontal upright sans-serif lettering, consistent size and baseline, dark gray. Typeset formulas cleanly. Adjust local spacing if needed so letters do not touch borders, icons or arrows. Do NOT leave any empty text strips; remove unused label strips. No overall title, no paragraphs, no new decorative icons. Preserve white background, pastel blue/lavender/sage/coral, substantial dark-gray lines. Keep original wide aspect and output resolution. The five bottom module labels exactly left to right: “训练数据”, “参数更新”, “发布组件”, “查询接口”, “行动对象”. No other text. Keep each coral intrusion arrow ending at its corresponding module; no claim attacks already succeed.

字体修订提示：

Change ONLY the typography of this already correct scientific architecture illustration. Every existing letter, Chinese character, number, and mathematical symbol is currently TOO BOLD. Redraw ALL existing text as elegant NORMAL REGULAR-WEIGHT clean sans serif: Chinese visual reference Source Han Sans / Noto Sans CJK SC Regular (400), Latin Source Sans 3 Regular (400), formulas regular weight. All glyph strokes must visibly become about HALF AS THICK as in the input. NO BOLD, NO SEMIBOLD, no black-heavy lettering anywhere, including short headings. Use dark slate gray text rather than pure black. Keep all label wording, capitalization, formulas and punctuation exactly identical and preserve positions, horizontal baselines, original size and legibility. Keep every icon, all architecture, line widths, fills, arrows and every scientific relationship unchanged. Do not add or erase labels, titles or symbols. Render the lighter text DIRECTLY IN THE OUTPUT IMAGE; no blank bands.

检查：字重已明显变细；必要标签水平可读；对象、连线路由、独立权限及已阻断分支保持原意。

## prompt-injection

输出：`https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/03-trustworthiness/generated/v1r3-prompt-injection.png`。

原生标注提示：

User requires labels to be generated DIRECTLY IN THE IMAGE, not added later. Preserve this exact LINE-BASED ARCHITECTURE and all scientific relationships. Render all specified Chinese labels accurately with clear horizontal upright sans-serif lettering, consistent size and baseline, dark gray. Typeset formulas cleanly. Adjust local spacing if needed so letters do not touch borders, icons or arrows. Do NOT leave any empty text strips; remove unused label strips. No overall title, no paragraphs, no new decorative icons. Preserve white background, pastel blue/lavender/sage/coral, substantial dark-gray lines. Keep original wide aspect and output resolution. Labels in diagram: upper-left task “用户：整理A”; lower-left external mail “夹带：删除B”; central neural/context module “上下文与模型”; upper proposal “提案：归档A”; lower coral proposal “提案：删除B”; trusted key at top “仅授权A”; gate “执行核验”; upper-right outcome “A已归档”; lower-right untouched outcome “B未改变”. Keep no line from third-party email to trusted authorization, and no outgoing causal arrow reaching B. The coral unauthorized proposal terminates at the T-bar before the permission gate.

字体修订提示：

Change ONLY the typography of this already correct scientific architecture illustration. Every existing letter, Chinese character, number, and mathematical symbol is currently TOO BOLD. Redraw ALL existing text as elegant NORMAL REGULAR-WEIGHT clean sans serif: Chinese visual reference Source Han Sans / Noto Sans CJK SC Regular (400), Latin Source Sans 3 Regular (400), formulas regular weight. All glyph strokes must visibly become about HALF AS THICK as in the input. NO BOLD, NO SEMIBOLD, no black-heavy lettering anywhere, including short headings. Use dark slate gray text rather than pure black. Keep all label wording, capitalization, formulas and punctuation exactly identical and preserve positions, horizontal baselines, original size and legibility. Keep every icon, all architecture, line widths, fills, arrows and every scientific relationship unchanged. Do not add or erase labels, titles or symbols. Render the lighter text DIRECTLY IN THE OUTPUT IMAGE; no blank bands.

检查：字重已明显变细；必要标签水平可读；对象、连线路由、独立权限及已阻断分支保持原意。

## defense-depth

输出：`https://github.com/shixiaogang/notes-on-machine-learning/blob/5da5ef3277c33d80f2feb5c2b75a693c245d4435/figures/02-foundations/03-trustworthiness/generated/v1r3-defense-depth.png`。

原生标注提示：

User requires labels to be generated DIRECTLY IN THE IMAGE, not added later. Preserve this exact LINE-BASED ARCHITECTURE and all scientific relationships. Render all specified Chinese labels accurately with clear horizontal upright sans-serif lettering, consistent size and baseline, dark gray. Typeset formulas cleanly. Adjust local spacing if needed so letters do not touch borders, icons or arrows. Do NOT leave any empty text strips; remove unused label strips. No overall title, no paragraphs, no new decorative icons. Preserve white background, pastel blue/lavender/sage/coral, substantial dark-gray lines. Keep original wide aspect and output resolution. TOP row labels left to right exactly “待入库记录”, “来源检查”, “隔离训练”, “复测后发布”. Add one short downward coral stopped branch from 来源检查 labeled “拒绝来源”, and one from 隔离训练 labeled “暂停发布”; place between rows with clear spacing. LOWER service row exact labels “外部输入”, “查询过滤”, “模型提案”, “独立授权”, “对象B”. Coral unauthorized attempted action is stopped immediately AFTER independent authorization before B; permitted flow remains. BOTTOM audit lane exact labels “独立记录”, “暂停／撤权”, “恢复可逆状态”. All dotted observation paths go ONLY to audit lane, not between service lanes. Remove leftover empty strips and no overall title.

字体修订提示：

Change ONLY the typography of this already correct scientific architecture illustration. Every existing letter, Chinese character, number, and mathematical symbol is currently TOO BOLD. Redraw ALL existing text as elegant NORMAL REGULAR-WEIGHT clean sans serif: Chinese visual reference Source Han Sans / Noto Sans CJK SC Regular (400), Latin Source Sans 3 Regular (400), formulas regular weight. All glyph strokes must visibly become about HALF AS THICK as in the input. NO BOLD, NO SEMIBOLD, no black-heavy lettering anywhere, including short headings. Use dark slate gray text rather than pure black. Keep all label wording, capitalization, formulas and punctuation exactly identical and preserve positions, horizontal baselines, original size and legibility. Keep every icon, all architecture, line widths, fills, arrows and every scientific relationship unchanged. Do not add or erase labels, titles or symbols. Render the lighter text DIRECTLY IN THE OUTPUT IMAGE; no blank bands.

检查：字重已明显变细；必要标签水平可读；对象、连线路由、独立权限及已阻断分支保持原意。
