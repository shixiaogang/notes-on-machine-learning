# 最新候选 r5：实际跨卷协调审查入口

源候选candidate-r5，基线33a06c0706bd8242083eb8d5d1abad367fe50117，上游a9cebd3ad6820d90e3f033822cdecd5a3002f547。精确版本补丁candidate-r5.patch SHA **9e44ad36e44ebef193159d618e9082143cf5205f73b42cf4aa27a0b135256cac**；candidate-r5-manifest.json SHA **e05d98114fcea51d821129f92b0db1ead89a544c45d2d0d2b20087469d69d1e3**。22文件中12变动，before/after完整SHA见该manifest与modified-source-sha-r5.tsv。

前r1→r4分别执行的作者C/P/W、13项闭环、37个变动块逐句及特殊单元覆盖，见index.md。r5仅改classification/05-ensemble.tex L24（源SHA f572233a87b69b1c9161604dd7905c3727c9d15491d10ad1f9aac1c3ffe7f598）；其它21文件与r4逐字相同。

独立复核IC-P34指出原“投票理想下降需要独立与统一优势”可能把充分保证说成必要。r5明写奇数二分类等权多数票的充分条件，P-a.e.输入标签下关于训练随机性条件独立、每成员统一正条件优势；结论是平均训练随机性后的投票风险有随成员数指数下降的上界。actual a9二分类L723–770的对象/条件/概率空间已重新实际读取。作者按固定r5单独C-r5→P-r5→W-r5执行并关闭；最终独立增量复核由figure_audit负责，本索引不代其结论。

target-reading-record.md覆盖旧15卷二与19卷一引用；r5只更新C025局部多数票条件，新增投票风险平均训练随机性的概率空间，不变目标key。最终38引用（16卷二/22卷一）actual目标唯一，reference-inventory-r5.json提供精确源行和目标行。G1/G2/G4/G6与E1/E10/E12在W-r5重新校准；其它G/E继承calibration-and-gates.md的同SHA范围。

行政结果administrative-boundaries-r5.json：全部标题/input/cite/图路径宽度保持，仅4授权通用thm退役，环境成对；patch-application-check-r5.json确认在ignored actual基线副本应用版本补丁后逐字等于12候选。341.tex/.md真实入站与去重身份见inbound-and-deduplication-decision.md（r4/r5的四去重部分同SHA）。

此版作者局部自查无已知技术未修项；独立返修关闭、root正式应用后源绑定、构建/测试/PDF检查/提交推送仍在后续阶段。旧candidate-r2/3/4.patch分别恢复且SHA等于各冻结manifest，版本名补丁优先于共享final.patch别名，避免混用。
