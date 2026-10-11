# 基础三章图像交付索引

基线b0ffa7f，工作区.worktrees/volume-two-figures-basics，分支codex/volume-two-figures-basics。24个正文图号：引言2、模型7、范式15；0个新增图号。最终路径及文件SHA见final-figure-version-manifest.json；当前七版PDF与构建输入以target/.build-manifest.json为准。

- baseline-review.md：实际查看旧成图/背景后的盘点、选型和新图必要性判断。
- native-figure-review.md：逐图科学关系、理解、视觉、字号与来源判断。
- revision-closure.md：失败轮次、模型修复、TikZ迁移和最终选择。
- book-page-review.md：卷二24图页、6相邻页、全集9代表页及3灰度页的实际视觉验收，阶段像素闭环与最终PDF SHA。
- caption-local-review.md、caption-version-closure.json、snapshots/：8条改动图注及AlphaGo局部段落的人工C/P/W、逐句实际意思、七门槛与E1–E12，以及前后版本。
- fonts-and-references.json、quantitative-generation.json：字体版本/许可/哈希与精确图源生成记录。
- early-generation-tool-calls.json、early-generation-backfill.json：本任务最早实际图像调用的元数据恢复，多任务r5参考登记的修正依据。
- validation-summary.json与保存日志：最终七版构建、check-target、测试的实际范围及结果。
- source-file-list.txt：本次提交相对源文件清单，排除target成品；共用依赖保持父任务协调版本。

generated/generation-20261011.json与generation-addendum-20261012.json保存47次调用完整提示与路径，reference-manifest-20261011.json保存141条参考图SHA。所有候选/失败背景保留，每个实际选用背景有独立透明真实字体层。旧资源自身generation.json/review.json和generation-rounds-in-progress.json是历史阶段记录，不能用其旧候选状态代替本轮验收。

本记录不称全书或跨卷全文独立审查。下一步卷一最新主分支整合后的引用/数学口径检查由父任务另行指定基线。父任务需合并源后重新构建，不能直接以本任务七PDF替代集成验证。
