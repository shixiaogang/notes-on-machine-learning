# 卷三（基础、理论与可信性）正文表述润色汇总

日期：2026-10-13
Worktree：`.worktrees/volume-three-prose-polish`，分支 `codex/volume-three-prose-polish`，基线 `main` = 5afcc031
技能：`academic-writing`（全局安装），项目规范 `specs/writings.md`

## 范围与原则

覆盖卷三全部 17 章（`tex/03-foundations/` 下 01-basics 三章、02-learning-theory 六章、03-trustworthiness 八章）。按用户要求与技能规范执行保守定点修改：不调整章节结构，不改变各章主要内容，只修改表述；每章逐处记录修改理由。不凑改动量，公式、数值、定理、图表、标签与引用一律不动。

## 各章修改统计

| 章 | 文件 | 修改处数 | 记录 |
| --- | --- | --- | --- |
| 1 引言 | 01-basics/01-introduction.tex | 7 | v3-c01-fix.md |
| 2 模型简介 | 01-basics/02-machine-learning-models.tex | 5 | v3-c02-fix.md |
| 3 范式简介 | 01-basics/03-machine-learning-paradigms.tex | 3 | v3-c03-fix.md |
| 4 统计学习框架 | 02-learning-theory/01-statistical-learning-framework.tex | 2 | v3-c04-fix.md |
| 5 二分类 | 02-learning-theory/02-binary-classification.tex | 3 | v3-c05-fix.md |
| 6 多分类 | 02-learning-theory/03-multiclass-classification.tex | 7 | v3-c06-fix.md |
| 7 凸学习与稳定性 | 02-learning-theory/04-convex-learning-and-stability.tex | 6 | v3-c07-fix.md |
| 8 深度学习理论 | 02-learning-theory/05-deep-learning-theory.tex | 5 | v3-c08-fix.md |
| 9 迁移学习理论 | 02-learning-theory/06-transfer-learning-theory.tex | 6 | v3-c09-fix.md |
| 10 可信性基础 | 03-trustworthiness/01-foundations.tex | 1 | v3-c10-fix.md |
| 11 可靠性 | 03-trustworthiness/02-reliability.tex | 2 | v3-c11-fix.md |
| 12 鲁棒性 | 03-trustworthiness/03-robustness.tex | 2 | v3-c12-fix.md |
| 13 公平性 | 03-trustworthiness/04-fairness.tex | 4 | v3-c13-fix.md |
| 14 目标对齐与行为约束 | 03-trustworthiness/05-alignment.tex | 5 | v3-c14-fix.md |
| 15 可解释性 | 03-trustworthiness/06-interpretability.tex | 4 | v3-c15-fix.md |
| 16 隐私保护 | 03-trustworthiness/07-privacy.tex | 5 | v3-c16-fix.md |
| 17 对抗安全 | 03-trustworthiness/08-adversarial-security.tex | 3 | v3-c17-fix.md |

合计 70 处定点修改。

## 修改类型分布

- 重复定义合并与指代显化（如第 1 章偏置/权重重复定义）
- 句法杂糅修复（如第 7 章"我们讨论的是……时"、第 14 章停止条件句）
- 压缩过度补足（如第 8 章"$p$计数"、第 16 章"逐记录裁剪却把参数解释为用户级"）
- 虚词与语序（如第 13 章"时，却还"、第 16 章"报告除……外"）
- 术语与规范统一（如第 9 章"均匀量词"→"全称量词"，与卷一索引一致）
- 重字笔误（如第 9 章"环境环境"）
- 表述与定义冲突（如第 15 章"越过放行边界"与隔离阈值定义不符）

## 验证

- 每章 `git diff` 复核，改动仅限记录所列各处。
- 各章教学例数值全部手工重算核对，未发现错误（详见各章记录 C4 项）。
- `./build.sh volume 03-foundations` 编译通过；`./build.sh check-target` 通过：十二卷 PDF 与各卷当前输入一致，卷三 505 页，不超过 600 页上限。
- `target/vol3-foundations.pdf` 与 `target/.build-manifest.json` 的卷三记录已随构建更新，与源文件一并暂存提交。

## 备注

构建环境：`/Library/TeX/texbin/biber` 在当前沙箱中不可用（lipo 报错），需将 `/opt/homebrew/bin`（biber 2.22）前置；`check_target_pdfs.py` 依赖 PyMuPDF，需以 `/usr/bin/python3` 运行。本次构建使用 `PATH="/usr/bin:/bin:/usr/sbin:/sbin:$HOME/.local/bin:/opt/homebrew/bin:/Library/TeX/texbin"`。
