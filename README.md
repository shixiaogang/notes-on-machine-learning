# 机器学习笔记

基于 `tufte-book` 的中文 LaTeX 机器学习笔记，按十二卷独立组织与出版，不生成全集。卷目与分部见[全书结构](plans/book-structure.md)，章纲与进度见[计划索引](plans/README.md)，构建目录由 [tex/volumes.json](tex/volumes.json) 登记。每卷总页数不超过600页。

## 构建

需要 TeX Live（XeLaTeX、`latexmk`、Biber、texindy）、Python 3、PyMuPDF 和 Bash。字体与 Tufte 模板随仓库提供，无需安装系统字体，见[字体说明](fonts/README.md)。在所属任务 worktree 根目录执行：

```sh
./build.sh build         # 只编译输入变化、缺失或损坏的卷
./build.sh check-target  # 校验十二卷与各卷输入、页数
./build.sh volume 06-probabilistic-graphical-models # 指定卷
./build.sh all           # 首次构建或全书结构变化时编译十二卷
```

成品为 `target/volN-<slug>.pdf`；`target/.build-manifest.json` 分卷记录正文、图像与图源、使用的文献及词条、引用位置、字体和共享样式。局部变更只更新受影响卷；共享样式、字体或构建工具变更会影响全部使用它们的卷。正文与对应成品一起纳入版本管理。

各卷 PDF 统一由 Git LFS 保存。安装 Git LFS 后执行 `git lfs install --skip-repo` 和 `git lfs pull` 获取完整 PDF，`--skip-repo` 保留版本化钩子；校验同时检查 LFS 指针的 SHA-256 与大小。

`volumes` 与 `all` 均编译十二卷；`watch <slug>` 监听指定卷并更新成品；`release <slug>` 高压缩指定卷；`clean` 清理当前工作区缓存与产物。可选 Make 接口见 [Makefile](Makefile)。

## 开发

每个任务使用独立 worktree 和分支，流程见[开发要求](specs/development.md)，其余规范见[规范索引](specs/README.md)。新克隆后启用提交检查：

```sh
git config --local core.hooksPath .githooks
```

提交前运行 `./build.sh build`、`./build.sh check-target` 及与变更范围对应的检查，将源文件、变化的 PDF 和清单一并暂存。提交钩子只构建受影响卷，并校验全部成品与暂存源文件一致。

```sh
make test
bash tests/check-book-editions.sh
```

## 目录与入口

| 目录 | 用途 |
| --- | --- |
| `tex/` | 十二卷正文、卷目录登记与共享样式；各卷 `main.tex` 共用 `book.tex` |
| `specs/` | 开发、LaTeX、写作、图像及样式规范 |
| `plans/` | 现行结构、章纲、选材资料与待办 |
| `figures/` | 与正文卷、部分对应的图源、数据与生成记录 |
| `fonts/` | 固定字体、校验清单与上游许可证 |
| `build/` | 当前 worktree 的编译缓存，不纳入 Git |
| `target/` | 十二卷 PDF 与分卷构建清单，纳入 Git |

经典模型和神经网络直接按章组织，其余卷可设一层部分。跨卷使用结论时先在当前正文说明所需关系与条件，再标注可参考的卷与位置；不重复正式定义、定理与证明。

## 许可

- 书稿正文与原创图表采用 CC BY-NC-ND 4.0。
- LaTeX 样式、构建脚本、测试和代码示例采用 Apache License 2.0，见 [LICENSE](LICENSE)。
- 字体适用各自的上游许可证，见[字体说明](fonts/README.md)。
