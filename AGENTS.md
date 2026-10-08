# 项目说明

这是一本基于 `tufte-book` 的中文 LaTeX 机器学习笔记。项目入口与构建环境见 [README](README.md)。

## 开始任务

开始任何修改前必须阅读 [开发要求](specs/development.md)，检查 `git status --short` 与 `git worktree list`。每个独立任务使用自己的 worktree 和分支；继续任务时复用原工作区，所有编辑、资源生成、构建、测试和提交均在该工作区执行。不得覆盖、暂存或清理其他任务的成果，不共享可写的 `build/`、`target/`。

按任务阅读并遵循相关规范，完整索引见 [specs/README.md](specs/README.md)：

- [LaTeX 与数学记号](specs/latex.md)：正文组织、符号、公式、宏、引用与编译。
- [写作](specs/writings.md)：凡涉及正文、大纲、图注或示例文字，必须先阅读，交稿前完成自查；各章保留独立的 `\section{本章小结}`。
- [图像](specs/figures.md)：选型、配色、标注、来源与复现。
- [样式](specs/design.md)：字体、版式与语义环境。

## 内容与资源

- `tex/` 按“卷—部分—章”组织，卷和部分目录使用两位序号；入口分别为 `volume.tex`、`part.tex`。新增章节接入所属入口，不复制全集与单卷正文。
- 内容边界与规划以 [计划索引](plans/README.md) 及其链接的大纲为准；完成状态以实际正文入口为准。结构变化时同步相关大纲与章目映射，不保留已完成的过程讨论。
- `figures/` 按卷、部分和制作方式归档，跨部分资源放入 `00-shared/`；保留图源、数据与生成记录，使用相对路径。字体及许可证位于 `fonts/`。

## 验证与交付

每次提交前必须在任务 worktree 中执行：

```sh
./build.sh all
./build.sh check-target
```

七份 PDF 与 `target/.build-manifest.json` 必须对应当前正文、图源、字体及构建输入，并与源文件一起暂存；不得绕过提交检查。其他测试和 PDF 检查按变更范围及相关规范执行。

主工作区用于查看基线和串行集成；集成后按最终源文件重新构建并校验。交付时说明 worktree、分支、验证结果及是否已提交或集成，清理前确认成果已保存且可恢复。
