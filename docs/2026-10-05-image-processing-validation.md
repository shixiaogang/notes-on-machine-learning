# 图像和多模态处理正文验收

## 交付范围

本次从远端 `origin/main` 的 `5db7ad4728f14b9ed227ac937cbaf487cc964e03` 创建独立工作区 `.worktrees/docs-image-processing-content`，分支为 `docs/image-processing-content`。按已定大纲完成九章，并接入 `tex/04-applications/02-image-processing/part.tex`。

九章合计109202个中文字（按章节源文件统计，含标题与图表说明）、101个编号公式、31幅TikZ图和8张表。大纲的329项章内标题与章标题均有对应，九章均设置独立“本章小结”。没有未定义的内部引用、重复标签、未引用图表或缺失图源。

| 章 | 内容 | 图 | 表 |
| --- | --- | ---: | ---: |
| 1 | 图像和多模态处理概述 | 2 | 0 |
| 2 | 图像识别与检索 | 4 | 1 |
| 3 | 图像复原、增强与压缩 | 4 | 1 |
| 4 | 图像生成与编辑 | 3 | 1 |
| 5 | 视频识别、跟踪与检索 | 3 | 1 |
| 6 | 视频复原、增强与压缩 | 3 | 1 |
| 7 | 多模态模型 | 4 | 1 |
| 8 | 多模态理解 | 4 | 1 |
| 9 | 多模态生成 | 4 | 1 |

具体来源版本、机制核查及数值复算见[写作记录](2026-10-05-image-processing-writing.md)。手算结果均为教学构造，没有将其表述为模型实测结果；近期扩展案例只按已取得的一手材料说明其范围。

## 编译与产物

完成全集与五个单卷构建，局部版式修订后重建受影响版本，再执行 `./build.sh all`，六版均返回已更新状态。页数为PDF物理页数。

| 产物 | 页数 | 实际书目条数 |
| --- | ---: | ---: |
| `build/main.pdf` | 1687 | 911 |
| `build/01-foundations.pdf` | 480 | 256 |
| `build/02-models.pdf` | 1034 | 591 |
| `build/03-paradigms.pdf` | 16 | 27 |
| `build/04-applications.pdf` | 193 | 152 |
| `build/05-systems.pdf` | 14 | 27 |

图像和多模态处理正文位于应用卷PDF第15—177页，共163页；在全集中为第47—55章，位于PDF第1431—1593页。共享前后页和其他部分首页计入对应版本总页数。

- 六份最终LaTeX日志均无致命错误、未定义引用、重复标签、缺失文献或缺失字形，Biber无错误与警告。
- 六版书目中的条目集合均与该版编译控制文件中的引用集合一致，没有遗漏或额外打印未引用条目。
- 六版书签目标和PDF内部跳转目标均在有效页范围内。已核对全集与单卷的书签层级、前后页、卷首页、部分首页和索引呈现。
- 全集与应用卷最终日志无overfull；新增九章的边注逐行坐标扫描均未发现越过715 pt检查线的文字。扫描只作为定位手段，另做了图表、长公式及重点引文的目视检查。
- 已逐章检查全部31幅图和8张表，并回看全集编号下的图表分页；最终重点复查LVIS与MVTec AD联合引文、SeeClick、ChartQA及Geo3R等此前接近页底的位置。
- 跨卷引用在全集中解析为编号，应用单卷中的生成模型、流模型、范式和系统等外部目标采用可独立理解的文字回退。

本机通用Biber程序调用 `lipo` 失败，构建使用提取到 `build/vision-tools/biber` 的arm64程序（2.21），TeX Live路径为 `/Library/TeX/texbin`。未修改系统安装或构建脚本。实际环境调用如下：

```sh
env PATH="$PWD/build/vision-tools:/Library/TeX/texbin:/opt/homebrew/bin:/usr/bin:/bin" \
  TMPDIR="$PWD/build/vision-tmp" ./build.sh all
```

## 工程检查与配套修订

- `make test`通过27项单元测试及完整索引审计，统计为 `calls=1775, unique=1549, mappings=1510, aliases=2, errors=0`。最终运行在所有编译结束后进行，避免读取正在生成的索引文件。
- `bash tests/check-book-editions.sh`通过，包括范围感知引用与最小索引流水线；`git diff --check`通过。
- 复用既有CLIP书目，新增文献统一登记到 `tex/references.bib`；新增术语登记到应用卷词典。
- 修复基线索引漂移：6项旧名对齐、8项孤立映射删除、22项缺失映射补齐；同步更新审计计数与工程规范。没有为匹配词典而改写其他卷的术语正文。
- 将基线AdaBoost段落的一处跨卷裸引用改为 `BookSectionRef`，消除模型单卷的引用缺口。
- 卷末书目改用左对齐、右侧自然断行，解决长作者列表与题名溢出；保留完整作者、字号与边注样式，并同步设计规范。

详细证据保存在 `build/vision-all-editions.log`、`build/vision-all-final.log`、`build/vision-full-verified.log`、`build/vision-applications-verified.log`、`build/vision-make-test.log`、`build/vision-editions-test.log` 和 `build/vision-final-audit.json`。重点预览位于 `build/vision-preview/`。

## 核验边界

- 模型单卷的降维章定理5.4仍有约1.07 pt的轻微水平溢出。该章节源文件与基线一致；已查看PDF第260页，文字保留在定理色块内，没有遮挡或裁切。本次没有扩展为其他卷的内容重写。
- 当前远端基线的第三卷、第五卷及应用卷相邻两部分仍是结构入口，所以相关单卷页数较少，第三、第五卷的索引为空。没有混入其他工作区尚未合并的正文。
- 内容复核属于作者自查、原始资料核读及教学算例复算，不等同于独立同行评审或模型实验。其他卷只做本次共享改动所需的编译和前后页回归。
- 全部变更保留在本地工作区，未提交、推送或合并。`build/`内PDF、核查脚本、原文缓存和预览为本地构建产物，不纳入Git。
