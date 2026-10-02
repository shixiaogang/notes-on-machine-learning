# 书籍样式规范

## 设计入口

视觉方向是现代简约：实色色块、直角、留白和明确的文字层级。不使用阴影、渐变或装饰性图案。

- `tex/preamble.tex`：书籍元数据与样式校样开关；版权页使用作者确认的 Apache 2.0 声明。
- `tex/styles/fonts.tex`：所有字体与 `\term`、`\code`。
- `tex/styles/layout.tex`：调色板、版心、前置页、卷首页的视觉样式、目录色块、标题、页眉页脚和图表注。
- `tex/styles/structure.tex`：卷首页、分部页、四级目录及 PDF 书签层级。
- `tex/styles/environments.tex`：数学、代码与算法环境。
- `tex/styles/references.tex`：边注文献命令和三类文献驱动。

第三方 `tex/styles/tufte-book.cls` 与 `tex/styles/tufte-common.def` 保持原样；项目修改集中在上述模块。

## 字体与色彩

| 用途 | 中文 | 英文 |
| --- | --- | --- |
| 默认宋体正文、`\songti` | 思源宋体 Source Han Serif CN | STIX Two Text |
| 黑体标题、`\heiti`、`\term` | 思源黑体 Source Han Sans SC | Source Sans 3 |
| `\kaishu`、数学陈述、边注和图表注 | 霞鹭文楷 LXGW WenKai | STIX Two Text |
| 代码 | 霞鹭文楷等宽 LXGW WenKai Mono | Source Code Pro |
| 数学公式 | — | STIX2 数学字族 |

中文斜体以霞鹭文楷替代机械倾斜。英文书名和论文标题使用真正的 STIX Two Text Italic。
块引用 `quote` / `quotation` 也使用文楷与 STIX Two Text。
数学字体采用 `stix2` 的 Type 1 实现，以兼容记号规范中的 `\bm`，不引入 `unicode-math`。
字体缺失时明确报错，不自动降级为另一种视觉风格。
`build.sh` 从常见的系统字体目录解析上述中文字体，并在 `build/fonts/` 中建立构建期链接；
字体文件不纳入 Git，也不依赖操作系统字体注册缓存。

全局颜色：`BookInk` 墨蓝（233342）、`BookTeal` 青（267D82）、`BookBlue` 蓝（42658A）、
`BookAmber` 赭（A66A25）、`BookMuted` 灰（64717B）、`BookPaper` 浅灰（F3F5F5）、`BookRule` 分隔线（DCE3E5）。
图中输入、模型、输出、损失分别使用 `FigureInput`、`FigureModel`、`FigureOutput`、`FigureLoss`。
单张图不重新定义色值。颜色不能是唯一的语义提示。
数学环境另用更鲜明的 `BookTheorem` 蓝（2F65B0）及同色系浅蓝 `BookLemma`；
示例使用 `BookExample` 金黄左线（D3AD38）与 `BookExampleBackground` 浅黄底（FFF8D9）。

## 页面与标题

当前使用 Letter 纸张；正文宽 112 mm，边注宽 48 mm，中缝 9 mm，总版心宽 169 mm。
正文版心位置固定；页眉按奇偶页镜像，奇数页内侧在左，偶数页内侧在右。
封面为墨蓝底，卷首页为整页青色实底，分部页为浅灰底，青色块承载层级信息。内扉页和版权页保持白底。
前置页使用罗马页码，正文重新从阿拉伯数字 1 开始；封面、内扉页、版权页、卷首页和分部页隐藏页码。
卷首页和分部页计入正文页码。所有页脚均不放页码；带章节标题的起始页不放页眉。
普通页的内侧页眉显示“第1章＋章名”，外侧页眉用青色色块显示页码。
封面与内扉页使用大写作者名，年份与版本写作 `2026/第一版`。

书籍采用“卷—部分—章—节”层级。部分与章节全书连续编号，卷首页不重置计数。
卷使用 `\bookvolume{中文名称}{English Title}`，卷标签紧跟卷命令。
卷首页整页铺满与分部编号块相同的 `BookTeal`，只保留卷号、中文标题和英文标题。
三者距页面左缘均为 23 mm，文字组位于页面中部偏上，底部保留大面积留白。
卷号使用 18 pt 常规黑体浅白字，距页顶 82 mm；中文标题使用 38 pt 常规黑体白字，距页顶 110 mm。
英文标题使用 13 pt 常规无衬线浅白字，跟随中文标题下缘留出 10 mm 间距，避免标题换行后发生覆盖。
不设导读、分部索引或额外数字。
视觉样式由 `layout.tex` 中的 `\bookvolumetitlepage` 统一控制。

分部页使用 `\bookpart{中文名称}{English Title}`，不显示所属卷号、卷名或页眉，
英文标题以 Source Sans 3 常规体排在中文标题下方。部分标签紧跟分部命令。
分部页青色色块显示“第一部分”等中文编号；章节标题的色块显示“第1章”等阿拉伯数字编号。
目录使用全版心宽度，保留到节：卷条目采用全行青色背景与白色卷号、标题和页码，部分编号保留青色背景块，部分标题采用青色；
卷条目使用常规字重，章条目使用墨蓝黑体，节条目使用灰色小字。各级标题统一从目录左缘 29 mm 处开始；
卷与部分编号从 4 mm 处开始，章、节编号均从 7 mm 处开始并左对齐，只在编号栏保留轻微缩进。
各级页码共用 10 mm 宽的右对齐栏，右边界距目录右缘 4 mm；部分使用浅色引导线。
PDF 书签使用相同的卷、部分、章、节嵌套层级。
目录页码预留三位数字的宽度；使用 `needspace` 在卷条目前预留 60 mm，避免卷标题与短分部组被页底拆开。
目录标题使用与无编号章节一致的青色条和标题字形。
前言保留独立页面，但不加入目录。版权页所有段落取消首行缩进，书籍信息与许可声明共用左边界。
章节使用 `\chapter{名称}`，小节使用 `\section`、`\subsection`。
只有独立设计校样为便于比较不同环境，显式分开测试页面；正式章节不照搬校样中的 `\clearpage`。

关键名词使用 `\term{经验风险最小化}`。该命令局部切换到粗黑体，不影响后续正文，也不用于普通强调的滥用。

## 数学环境

```tex
\begin{definition}[经验风险]
  \label{def:empirical-risk}
  定义的条件、对象与公式。
\end{definition}

\begin{theorem}[收敛性]
  \label{thm:convergence}
  写清前提，再写结论。
\end{theorem}
\begin{proof}
  证明过程。
\end{proof}
```

`lemma`、`example` 使用相同的可选标题接口。定义、定理、引理、示例共享“章.序号”，
分别用青、深蓝、浅蓝、金黄的细左线与浅底色区分；定理和引理采用同一蓝色系的深浅层级，示例为浅黄色底。
正文为楷体，标题为黑体。环境允许跨页，不给整个陈述套不可分割的盒子。
证明不加色块，末尾使用黑色实心方块。
公式按章独立编号，使用 `equation` / `align`；不手动写公式号。
公式、图、表、定理类、代码和算法的编号以阿拉伯章号开头。
脚注与边注引文标记只显示章内序号，不加章号前缀。各计数器均在新章开始时重置；
例如第二章的第一个公式为 `2.1`，第一个边注引文标记为 `1`。
章节标题使用阿拉伯数字编号，不改变对象编号中的阿拉伯章号。页码与代码／算法行号不加章号前缀。

## 代码与算法

代码基于 `listings`，不要求 Python、Pygments 或 shell escape。支持中文注释和长行折行。

```tex
\begin{codeblock}[language=Python,label={code:step}]{参数更新}
w = w - learning_rate * gradient
\end{codeblock}
```

`codeblock` 的可选参数传给 `tcolorbox`，提供 `language` 快捷选项；标题是必选参数。
更细的语法高亮设置使用 `listing options={style=book code,...}`。标签使用 `label` 选项，
不要把 `\label` 写在代码正文中。引用时写 `代码~\ref{code:step}`。
行内代码使用 `\code{learning\_rate}`，仍须转义 LaTeX 特殊字符。

```tex
\begin{algorithm}[梯度下降]
  \label{alg:gradient-descent}
  \begin{algorithmic}[1]
    \Require 目标 $f$ 与初始参数 $\bm{w}^{(0)}$
    \Ensure 更新后的参数
    \State 计算梯度并更新参数
  \end{algorithmic}
\end{algorithm}
```

算法使用 `algpseudocode` 的 `\State`、`\For`、`\If` 等命令；输入和输出标签为中文。
代码和算法各自按章编号，均可跨页，默认不浮动。二者的标题统一左对齐，标题左留白相同，
不受代码行号区宽度影响。不要另加载会占用同名环境的 `algorithm` / `algorithm2e`。

## 边注引文

所有条目集中在 `tex/references.bib`，由 Biber 处理。
正文使用 `\cite{bishop2006}` 或同义的 `\sidecite{bishop2006}`，正文产生上标标记，
边栏打印完整条目。作者名采用名字首字母加姓氏，不省略作者列表。

- 书籍：作者，*标题*，出版社，年份，edition。
- 期刊：作者，*标题* In 期刊名，年份，vol.，no.，pp.。
- 会议：作者，*标题* In 会议名，年份，pp.。

单个可选参数是后注，例如 `\cite[第 3 章]{bishop2006}`；两个参数分别为前注和后注，
例如 `\cite[参见][第 3 章]{bishop2006}`。不把页码混入文献标题字段。
`book` 的 `edition` 填数字；`article` 使用 `journaltitle`、`volume`、`number`、`pages`；
`inproceedings` 使用 `booktitle` 和 `pages`。缺失字段应查证，不编造。

不要把会生成边注的 `\cite` 放入章节标题、图表标题、代码或盒子中。
确需在图注注明来源时，用不生成边注的 `\fullcite{key}` 排在图注内；正文相应段落可另用 `\sidecite`。
边注容量有限，密集引用或长作者列表须在 PDF 中检查，不能靠缩成不可读的小字解决。
跨栏图表附近避免边注与对象落在相同的垂直位置。

## 图表

```tex
\begin{figure}[htbp]
  \centering
  \input{figures/learning-pipeline}
  \caption{可独立理解的图注。}
  \label{fig:pipeline}
\end{figure}
```

`figure` / `table` 默认只占正文宽度；宽图表用 `figure*` / `table*`，跨正文和边注区。
星号环境不是双栏排版。无论哪种宽度，都用 `\linewidth` 控制对象尺寸，
并将 `\caption` 写在图像或 `tabularx` 后面。所有图注、表注都在对象下方，使用文楷与 STIX Two Text。
普通三线表使用 `booktabs`；列宽自适应使用 `tabularx`。
TikZ 可直接使用 `book node` 和 `book arrow` 样式。

## 检查清单

运行 `./build.sh`，确认 XeLaTeX、Biber 和交叉引用全部完成，然后渲染检查：

1. 封面、内扉页、版权页、目录、五个卷首页、十三个分部页和章节标题。
2. 定义／定理／引理／示例的标题、公式编号、跨页和引用。
3. 三种文献的字段顺序、英文斜体和中文楷体；边注不覆盖正文或页脚。
4. 代码行号、中文注释、折行、算法行号及输入输出。
5. 普通图表和星号图表的宽度、下置图表注、字体与越界警告。
6. 不得有缺失字形、未定义引用、重复标签或影响阅读的溢出。
