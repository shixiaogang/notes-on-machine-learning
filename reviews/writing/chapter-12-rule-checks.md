# 第12章规则台账试用

本轮检查审查规则与记录方式，未修改书籍正文。原R3的17个待修改项、4个未完成核验、0个关闭项保持原有状态。此前两轮没有按这张表逐项执行，不能由新表追认通过。

## 实际检查与证据

[通用规则表](academic-writing-criteria.json)包含108个检查分组；[项目规则表](project-writing-criteria.json)包含25个分组。每项都有适用条件、动作、所需证据、失败判据和规则原文定位，组合要求按原句归属另留子项。全部规范块均登记映射或排除理由；这证明规则覆盖，不证明正文已按全部规则审查。

[通用台账](chapter-12-general-rule-checks-r4.json)和[项目台账](chapter-12-project-rule-checks-r4.json)固定本轮规则表与源文件版本。试用复用既有R3的定位证据，并核对相应原句和前后文：通用5项、项目5项确认存在未通过内容；其他项保留待检查，子项未核对完也不判通过。这是记录方式试用，不是新一轮全章逐句验收。

| 原文问题 | 实际核对动作 | 对应规则 |
|---|---|---|
| P02/P04密集预告，最不利变化的范围与具体评价要求尚未建立 | 检查场景、定义、评价诉求与公式的引入顺序；指出尚未建立的具体需求 | FP01、BW02 |
| E01两层计算的结果缺解释，P08未交代为何改换评价对象 | 对照逐封取上确界、再平均的作用，以及单封邮件转向整批组成的理由 | FP02、TC06、BW13 |
| P03的“基础章三个问题”、P08的“回归或分类器” | 寻找当前句的对象、所指入口与邮件任务中的具体含义 | LG03、BW09 |
| P08突然转到分布变化 | 回读P07与P08，指出评价对象变了，正文尚未解释为何改变 | LG07、BW06 |
| P02/P03重复并堆叠多个职责 | 比较段落中心意思与前段关系，区分需要展开的问题和重复路线预告 | BW05 |

R1试填的5处子句误判及模板残留见[首轮记录复核](rule-reviews/trial-record-r1-audit.md)。R2/R3为工作修订，均保留完整输入；当前R4改正误判并清除已判定项的待检查模板，剩余工作继续待检查。完整受审台账另存[通用R4输入](chapter-12-general-rule-checks-r4-input.json)和[项目R4输入](chapter-12-project-rule-checks-r4-input.json)，避免当前记录自身被覆盖后只能查到摘要。正文和既有R3记录可按台账所列Git提交恢复。

## 重复执行结构检查

从仓库根目录执行。规则全文快照只用于复核本轮规则版本；今后规则有变化，应重新建表和检查受影响记录。

```sh
python3 reviews/writing/check_review_records.py catalog --root reviews/writing/rule-inputs/academic-writing --catalog reviews/writing/academic-writing-criteria.json
python3 reviews/writing/check_review_records.py catalog --root . --catalog reviews/writing/project-writing-criteria.json
python3 reviews/writing/check_review_records.py record --root reviews/writing/rule-inputs/academic-writing --catalog reviews/writing/academic-writing-criteria.json --record reviews/writing/chapter-12-general-rule-checks-r4.json
python3 reviews/writing/check_review_records.py record --root . --catalog reviews/writing/project-writing-criteria.json --record reviews/writing/chapter-12-project-rule-checks-r4.json
```

新记录用工具的`init`命令生成，每项和子项初始都是待检查。状态分为通过、未通过、待检查、不适用、约定范围外；不适用须证明条件不成立，范围外须有约定依据，缺材料与只查了一部分均属待检查。通过须覆盖范围内全部适用单元及子要求。

结构检查核对版本、漏项、原文定位和状态依据；解释是否充分、规则归属是否正确、范围是否完整仍需阅读复核。记录复核及规则表独立复核见[本轮规则审查报告](rule-audit-20261010.md)。记录可接受，正文仍可待修改。
