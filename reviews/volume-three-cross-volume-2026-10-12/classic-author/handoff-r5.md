# 最新补丁交接（r5，替代r4应用入口）

采用candidate-r5.patch，SHA 9e44ad36e44ebef193159d618e9082143cf5205f73b42cf4aa27a0b135256cac；冻结source在candidate-r5/，before/after逐SHA在candidate-r5-manifest.json（SHA e05d98114fcea51d821129f92b0db1ead89a544c45d2d0d2b20087469d69d1e3）。12变动源SHA列表是modified-source-sha-r5.tsv。r4与r5只差分类集成L24的充分条件/训练随机性平均风险说明，来自独立发现IC-P34，已作者三遍增量复读。

最新审查入口review/index-r5.md；此前实际C/P/W与38目标核验继承记录，独立审核仍按figure_audit结论。真实基线33a06c/upstreama9不变；正式tex未修改、未构建/提交。实际341.tex/.md入站、4通用定理身份去重、GP/KRR/JL边界均已核，模型特殊结论保留。实际补丁已在ignored scratch应用并逐字还原候选，环境/结构/引用行政结果为administrative-boundaries-r5.json、patch-application-check-r5.json。

可复制文件集见handoff-r5-manifest.json。旧handoff.md与index.md保留r4历史身份；不要把它们的旧patch SHA当作r5。
