# 机器学习笔记

使用 LaTeX 编写的中文机器学习笔记，基于 `tufte-book`，分为数学准备、基础与理论、模型、范式、应用、系统六卷。内容边界见 [全书结构](plans/book-structure.md)，当前进度与章纲见 [计划索引](plans/README.md)。

## 构建

需要 TeX Live（含 XeLaTeX、`latexmk`、Biber）、Python 3 和 Bash；项目已在 TeX Live 2026 上验证。字体与 Tufte 模板随仓库提供，无需安装系统字体，详见 [字体说明](fonts/README.md)。

在所属任务 worktree 的根目录执行：

```sh
./build.sh all          # 构建全集与六个单卷
./build.sh check-target # 校验成品与当前输入一致
```

成品位于 `target/`：全集为 `machine-learning-notes.pdf`，单卷为 `volN-<slug>.pdf`；`build/` 保存编译缓存。正文、图源和成品一起纳入版本管理。

全集 PDF 使用 Git LFS 保存。安装 Git LFS 后执行 `git lfs install --skip-repo` 和 `git lfs pull`，
即可取得完整 PDF；`--skip-repo` 保留项目的版本化钩子。提交与推送全集时也需要 Git LFS。
成品校验同时验证 LFS 指针的
SHA-256 和文件大小与本地 PDF 一致。

日常可只构建全集或指定单卷：

```sh
./build.sh build
./build.sh volume 01-mathematical-preliminaries
```

单卷参数与 `tex/` 下的卷目录同名。`volumes` 构建六个单卷，`watch` 监听全集，`release` 高压缩构建全集，`clean` 清理所有成品与缓存；可选的 Make 接口见 [Makefile](Makefile)。构建会自动处理文献、索引与交叉引用。

## 开发

每个任务使用独立 worktree 和分支，流程及提交格式见 [开发要求](specs/development.md)，其余规范见 [规范索引](specs/README.md)。新克隆后启用提交检查：

```sh
git config --local core.hooksPath .githooks
```

提交前完整构建并校验七份 PDF，将源文件、成品与 `target/.build-manifest.json` 一并暂存。按变更范围运行检查：

```sh
make test
bash tests/check-book-editions.sh
```

## 目录与入口

| 目录 | 用途 |
| --- | --- |
| `tex/` | 正文与共享样式；`main.tex` 为全集入口，各卷 `main.tex` 为单卷入口，共用 `book.tex` 驱动 |
| `specs/` | 开发、LaTeX、写作、图像及样式规范 |
| `plans/` | 现行结构、待实施大纲、选材资料与待办 |
| `figures/` | 按卷、部分、制作方式归档的图源、数据与生成记录，见 [图像索引](figures/README.md) |
| `fonts/` | 固定字体、校验清单与上游许可证 |
| `build/` | 不纳入 Git 的编译缓存 |
| `target/` | 纳入 Git 的七份 PDF 与构建清单 |

章节组织、记号与引用见 [LaTeX 规范](specs/latex.md)，写作要求见 [写作规范](specs/writings.md)，字体与环境接口见 [样式规范](specs/design.md)。

## 许可

- 书稿正文与原创图表采用 CC BY-NC-ND 4.0。
- LaTeX 样式、构建脚本、测试和代码示例继续使用 Apache License 2.0，见 [LICENSE](LICENSE)。
- 字体适用各自的上游许可证，见 [字体说明](fonts/README.md)。
