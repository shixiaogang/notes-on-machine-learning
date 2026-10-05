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

在项目根目录运行以下命令时，默认只构建全集：

```sh
./build.sh
./build.sh build
```

构建单卷时传入卷目录使用的 slug：

```sh
./build.sh volume 01-mathematical-preliminaries
./build.sh volume 02-foundations
./build.sh volume 03-models
./build.sh volume 04-paradigms
./build.sh volume 05-applications
./build.sh volume 06-systems
```

`volumes` 依次构建六个单卷，`all` 构建全集和六个单卷：

```sh
./build.sh volumes
./build.sh all
```

七个 PDF 均直接写入 `build/`：

| 版本 | 输出文件 |
| --- | --- |
| 全集 | `build/main.pdf` |
| 第一卷 | `build/01-mathematical-preliminaries.pdf` |
| 第二卷 | `build/02-foundations.pdf` |
| 第三卷 | `build/03-models.pdf` |
| 第四卷 | `build/04-paradigms.pdf` |
| 第五卷 | `build/05-applications.pdf` |
| 第六卷 | `build/06-systems.pdf` |

全集和单卷采用同一封面构图。全集封面第二行为“理论、模型和范式”，单卷封面第二行为
“卷一：基础、理论和可信性”等“卷号：卷名”形式；作者名统一为“施晓罡”。

脚本使用 XeLaTeX。`latexmk` 自动调用 Biber 和索引处理器，并重复编译直至交叉引用稳定。
日常构建使用等级 1 的无损压缩，加快含大量图片和嵌入字体的 PDF 输出；不会降低图片分辨率或画质。
各版本使用独立缓存；没有源文件变化时，重复运行会直接复用对应结果。

目前内置编辑器的单文件编译不支持本项目的多个 `\input` 文件；请以 `./build.sh` 生成的 PDF 为准。

`watch` 持续监听全集并更新 `build/main.pdf`；`release` 以最高无损压缩等级构建全集。两者均保持全集语义：

```sh
./build.sh watch
./build.sh release
```

`clean` 清理全集和六个单卷的产物及缓存：

```sh
./build.sh clean
```

如果已安装 GNU Make，可以使用 `make build`、`make volume VOLUME=01-mathematical-preliminaries`、
`make volumes`、`make all`、`make watch`、`make release` 和 `make clean`；
这些目标映射到同名脚本接口。

## 内容入口

- `tex/main.tex`：全集薄入口，只声明全集模式并载入共享驱动。
- `tex/<slug>/main.tex`：六个单卷薄入口，声明卷号、卷名和内容入口。
- `tex/book.tex`：全集与单卷共用的文档驱动，统一载入文档类、前页、正文和后页。
- `tex/frontmatter.tex`：共享前页入口，依次载入封面、内扉页、版权页、前言、数学符号和目录。
- `tex/frontmatter/preface.tex`：共享前言；“参考资料”按六类列出 27 本教材，并通过 `\nocite` 登记完整书目信息。
- `tex/frontmatter/mathematical-notation.tex`：共享数学符号页，依次分为“对象与线性代数”“微积分与优化”“概率与信息论”三组。
- `tex/backmatter.tex`：共享后页入口，输出当前 PDF 实际引用或前页显式登记的参考文献条目，以及只由当前正文 `\term` / `\termalias` 生成的双语主题词索引。
- `tex/preamble.tex`：书籍元数据、中文排版、数学宏包、绘图工具和全局样式。
- `tex/styles/`：字体、页面布局、卷与目录结构、语义环境和文献格式模块。
- `tex/index-terms.tex` 与 `tex/index-terms/`：双语索引词典总入口及按首次出现卷归档的六个分片。
- `tex/references.bib`：集中管理书籍、期刊与会议文献。
- `scripts/audit_index_terms.py`：审计正文词条、英文映射、语义别名和已生成索引产物。
- `tex/styles/tufte-book.cls` 与 `tex/styles/tufte-common.def`：项目固定使用的 Tufte-LaTeX 模板文件。
- `tex/01-mathematical-preliminaries/`：数学准备，包括数学语言与分析、线性代数与几何、概率与统计、离散数学与图论、动力系统与决策。
- `tex/02-foundations/`：基础、理论和可信性，包括机器学习基础、机器学习理论、机器学习可信性。
- `tex/03-models/`：模型，包括经典模型、神经网络模型、概率图模型。
- `tex/04-paradigms/`：范式，包括强化学习、知识的高效利用、知识的演进与迁移。
- `tex/05-applications/`：应用，包括自然语言处理、图像处理、推荐与搜索。
- `tex/06-systems/`：系统，目前设机器学习系统部分，承接数据、训练与部署。
- 每卷的 `volume.tex` 只管理卷及其部分内容，各部分使用子目录中的 `part.tex`。
- 全集中的卷、部分和章连续编号；单卷省略卷首页和卷级目录，部分、章和正文页码均从 1 开始。
- `plans/book-structure.md`：六卷结构、内容边界与目录设计约定。
- `plans/learning-theory-outline.md`：机器学习理论部分的六章大纲。
- [神经网络模型大纲](plans/neural-network-models-outline.md)：九章安排、各节内容与模型、训练、泛化的内容边界。
- `figures/`：书中图像与可编辑绘图源文件。
- `fonts/`：固定版本的中西文与数学字体，以及上游许可证。
- `specs/`：开发与写作规范。

## 样式用法

完整示例见 [书籍样式规范](specs/design.md)。关键术语使用 `\term{机器学习}`，正文仍只显示中文；
索引通过集中词典显示“机器学习，machine learning”。需要稳定排序键时写
`\term[k近邻]{$k$近邻}`。同一中文显示词对应不同技术含义时，先用
`\DeclareBookIndexTermAlias` 登记语义身份，再在正文使用 `\termalias`。
索引使用两栏排版，页标题、目录条目和 PDF 书签统一为“索引”；全集收录六卷正文实际出现的词条，
单卷只收录该卷正文实际出现的词条。

定义、定理、引理和示例分别使用 `definition`、`theorem`、`lemma`、`example`。
`\cite{文献键}` 或 `\sidecite{文献键}` 会在边栏排出完整引文。
普通图表使用 `figure` / `table`；跨正文与边栏的图表使用 `figure*` / `table*`。
所有图表均将 `\caption` 写在对象后面。

## 验收

结构与双语索引检查分别运行：

```sh
bash tests/check-book-editions.sh
make test
```

`make test` 的索引审计基线为 `calls=2291`、`unique=1965`、`mappings=1924`、
`aliases=2`、`errors=0`。交付前还需运行 `./build.sh all`，扫描六份构建日志，
并检查六版封面、前言、数学符号、参考文献和索引的范围、排序、双语格式、合并页码与链接。

## 许可

- 书稿正文与原创图表采用 CC BY-NC-ND 4.0，版权页中的英文许可声明与矢量图标由共享样式统一维护。
- LaTeX 样式、构建脚本、测试和代码示例继续使用 Apache License 2.0，许可证见根目录 `LICENSE`。
- `fonts/` 中的字体继续适用各自的 SIL Open Font License。
