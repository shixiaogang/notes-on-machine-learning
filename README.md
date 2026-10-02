# 机器学习笔记

这是一个使用 LaTeX 编写的中文机器学习笔记项目，版式基于 Tufte-LaTeX 的 `tufte-book` 文档类。

## 构建环境

- TeX Live，包含 XeLaTeX、`latexmk` 与 Biber
- `ctex`、`stix2`、`amsmath`、`bm`、TikZ、PGFPlots、`tcolorbox`、`listings`、`algpseudocode`、`biblatex`、`needspace` 等宏包
- 项目字体已收录在 `fonts/`，无需另行安装中西文字体；字体清单、来源和许可证见 [字体说明](fonts/README.md)
- Bash
- GNU Make（可选）

项目在 TeX Live 2026 上验证通过。Tufte-LaTeX 的必要源码已固定在 `tex/`，构建时会优先使用本地副本。

## 编译

在项目根目录运行：

```sh
./build.sh
```

默认操作是构建，也可以显式指定：

```sh
./build.sh build
```

脚本使用 XeLaTeX，并将结果写入 `build/`。最终 PDF 位于 `build/main.pdf`。
`latexmk` 会自动调用 Biber 处理边注文献，然后重复编译，直至交叉引用稳定。
日常构建使用等级 1 的无损压缩，加快含大量图片和嵌入字体的 PDF 输出；不会降低图片分辨率或画质。
构建直接读取 `fonts/` 中的字体，并复用文献和交叉引用缓存。没有源文件变化时，重复运行会直接复用结果。

目前内置编辑器的单文件编译不支持本项目的多个 `\input` 文件；请以 `./build.sh` 生成的 PDF 为准。

连续改稿时，可以监听文件变化后自动更新同一个 `build/main.pdf`，不打开新窗口；按 Ctrl+C 退出：

```sh
./build.sh watch
```

需要分发体积更小的 PDF 时，使用最高无损压缩等级 9；字体、图片与版式和日常构建相同：

```sh
./build.sh release
```

两种模式都编译全书并由 `latexmk` 完成必要的文献和引用更新，不省略检查轮次。
切换压缩等级会重新生成 PDF；此后的同模式构建仍可使用增量缓存。

清理编译产物会丢弃缓存，下一次构建更慢。日常改稿不必清理；依赖变更后的完整验证或缓存异常时再执行：

```sh
./build.sh clean
```

如果已安装 GNU Make，也可以使用 `make`、`make watch`、`make release` 和 `make clean`；它们会调用同一个脚本。

## 内容入口

- `tex/main.tex`：全书主文档。
- `tex/preamble.tex`：书籍元数据、中文排版、数学宏包、绘图工具和全局样式。
- `tex/styles/`：字体、页面布局、卷与目录结构、语义环境和文献格式模块。
- `tex/references.bib`：集中管理书籍、期刊与会议文献。
- `tex/styles/tufte-book.cls` 与 `tex/styles/tufte-common.def`：项目固定使用的 Tufte-LaTeX 模板文件。
- `tex/01-foundations/`：基础、理论和可信性，包括机器学习基础、机器学习理论、机器学习可信性。
- `tex/02-models/`：模型，包括经典模型、神经网络模型、概率图模型。
- `tex/03-paradigms/`：范式，包括强化学习、知识的高效利用、知识的演进与迁移。
- `tex/04-applications/`：应用，包括自然语言处理、图像处理、推荐与搜索。
- `tex/05-systems/`：系统，目前设机器学习系统部分，承接数据、训练与部署。
- 每卷使用 `volume.tex`，各部分使用子目录中的 `part.tex`；部分与章节全书连续编号。
- `plans/book-structure.md`：五卷结构、内容边界与目录设计约定。
- `plans/learning-theory-outline.md`：机器学习理论部分的六章大纲。
- [神经网络模型大纲](plans/neural-network-models-outline.md)：九章安排、各节内容与模型、训练、泛化的内容边界。
- `figures/`：书中图像与可编辑绘图源文件。
- `fonts/`：固定版本的中西文与数学字体，以及上游许可证。
- `specs/`：开发与写作规范。

## 样式用法

完整示例见 [书籍样式规范](specs/design.md)。关键术语使用 `\term{机器学习}`；
定义、定理、引理和示例分别使用 `definition`、`theorem`、`lemma`、`example`。
`\cite{文献键}` 或 `\sidecite{文献键}` 会在边栏排出完整引文。
普通图表使用 `figure` / `table`；跨正文与边栏的图表使用 `figure*` / `table*`。
所有图表均将 `\caption` 写在对象后面。

版权页已按作者提供的参考文档写入 Apache 2.0 声明，内容由 `\BookCopyright` 统一维护。
