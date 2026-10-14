# 十二卷结构 rebase 验收

日期：2026-10-14。

- 审查基线：`75175dea03ad6c4d9b20299835b48c087a052505`
- rebase 目标：`d44808e5011b41201ac189a77ce189b3b4a160a9`
- 可恢复备份：`backup/docs-reinforcement-learning-content-pre-rebase-20261014`
- 当前分支：`docs/reinforcement-learning-content`

## 内容迁移

八章正文从旧 `tex/04-paradigms/01-reinforcement-learning/` 迁入
`tex/07-reinforcement-learning/` 的三个部分。将当前图源路径还原为审查时路径，
并还原十二卷迁移所需的两处跨卷显示文字后，八章分别与 rebase 前终审稿逐字节
一致。标题、层级、顺序和标签没有因 rebase 迁移改变。

图源迁入 `figures/07-reinforcement-learning/` 的对应部分；生成式场景图元数据
位于同一图的 `generated/` 目录。主题词映射归入
`tex/index-terms/07-reinforcement-learning.tex`。旧六卷 PDF、全集 PDF 和旧目录
没有重新引入。

## 验证

| 检查 | 结果 |
| --- | --- |
| `./build.sh volume 07-reinforcement-learning` | 卷七生成成功，437页 |
| `./build.sh check-target` | 十二份PDF与各卷当前输入一致，均不超过600页 |
| `make test` | 通过；28项索引单测、22项成品/结构单测、清理及部首页回归通过 |
| 索引审计 | 2776次调用、2366个唯一词条、2312项映射、2项别名、0错误 |
| `bash tests/check-book-editions.sh` | 十二卷、85章、卷内编号、无部分卷和标签唯一性通过 |
| 卷七日志 | 无致命错误、未定义引用/文献、重复标签、缺字或overfull |
| 非审查归档 `git diff --check` | 通过 |
| 第1章目录层级 | 用户后续要求的1.1.3–1.1.6及后续1.2–1.4编号通过 |

卷七 PDF：`target/vol7-reinforcement-learning.pdf`，SHA-256
`153af2d67954eaf19f7aa03ccc432a64735444a49c1ae9f27ff5a08c59b9f1ed`，
大小3284704字节。

rebase 后，用户另行要求将原第1.2至1.5节放到第1.1节下。正文段落和句子未改，
12个标题命令下沉一级；复读证据见 `../ch01/structure-adjustment-v1.md`。

## 状态

rebase 只更新当前任务分支；未推送远端，也未集成 `main`。
