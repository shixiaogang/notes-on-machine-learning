# Task 8 汇总报告

## 状态

Task 8 已完成。七章已接入“知识的获取 / Knowledge Acquisition”部分，参考文献、术语、符号、案例、交叉引用和第 6 至 7 章反馈闭环已经统一；完整构建和 PDF 视觉检查通过。

## 修改

- 将 `part.tex` 标题改为“知识的获取 / Knowledge Acquisition”，设置稳定标签 `part:knowledge-acquisition`，按顺序引入七章。
- 将七个临时 BibTeX 片段的 46 条记录按键和 DOI 核对，向 `tex/references.bib` 合并 43 条唯一记录，并删除七个片段。
- 统一 `seung1992querycommittee`、`wang2023selfinstruct` 和 `pgm-energy-models-richardson2006` 三组复用文献的正文引用键。
- 明确“知识、候选知识、标签、监督信号”的层级与用途，区分未知、不适用、弃权、未请求、执行失败和未决。
- 将类别集合统一为 \(Y\)，类别数统一为 \(K\)；第 2 章候选比较数量改用 \(J\)。
- 将手写章号和“上一章／下一章”改为语义交叉引用。
- 将第 6 章主案例统一为山茶、茶梅和月季，将对象对齐案例统一为林舟与海岬科技。
- 在第 6 章形成知识版本 K17，由第 7 章审计、修正并形成 K18，补齐融合到质量反馈的闭环。
- 修正第 5 章分组机制比较表缺少正文引用的问题。
- 更新第 6 章对象对齐图和输出形式图，使图内标签与统一案例一致。

## 静态检查

- 七章与七个独立“本章小结”均存在。
- 31 幅图、31 个图标签和 31 个图源输入一致。
- 24 项表、24 个表标签均有正文引用。
- 本部分 261 个标签无重复，全部 `ref`、`eqref` 和图源输入均可解析。
- 本部分 60 个唯一正文引用键均存在于 `tex/references.bib`。
- 主参考文献库没有新增重复键或重复 DOI。
- 未发现 TODO、FIXME、占位符或遗留手写章号。
- `git diff --check` 通过。
- `plans/efficient-knowledge-use-outline.md` 未修改。

## 构建

- 命令：`PATH="/opt/homebrew/bin:/Library/TeX/texbin:$PATH" ./build.sh`
- 结果：成功，`latexmk` 完成 Biber、四轮 XeLaTeX 和 `xdvipdfmx`。
- 产物：`build/main.pdf`，1497 个物理页，约 50 MiB。
- 部分页码：正文第 1355 页，PDF 物理第 1372 页。
- 七章起始正文页：1356、1367、1386、1400、1416、1438、1458。
- 七章起始物理页：1373、1384、1403、1417、1433、1455、1475。
- 最终 `build/main.log`：未定义引用 0，重复标签 0，overfull 0。
- 最终 `build/main.blg`：WARN 0，ERROR 0。

## PDF 检查

- 使用 Ghostscript 渲染，并用 `pdfjam` 生成接触表检查。
- 检查了部分页和七章章首页，标题、章号、正文起始位置与定义框均正常。
- 检查了 16 个高风险图表物理页：1377、1390、1408、1424、1425、1435、1451、1456、1461、1463、1467、1471、1476、1480、1486、1489。
- 重点检查了第 50 章宽表、第 51 章多来源记录表、对象对齐图、融合结果表和输出形式图，以及第 52 章收益成本表和版本反馈图。
- 未发现图表裁切、页面越界、文字重叠、标签错位或不可读缩放。

## 剩余警告

- 全书最终日志保留 50 条 underfull 和 124 条 `Marginpar moved`；其中本部分分别为 32 条和 12 条。
- 本部分 underfull 均来自通栏比较表的短文本列或对齐环境，视觉检查未见破坏性空白；边注警告是 Tufte 模板的自动避让结果。
- 主参考文献库仍有 3 组本任务前已经存在的 DOI 重复：`rubin1976missing` / `pgm-parameter-learning-rubin1976`、`clust-dempster1977` / `pgm-overview-dempster1977`、`stone1977regression` / `stone1977consistent`。它们不由本部分引入，本次未改动。
