# 最终验证及适用边界

2026-10-12，`codex/volume-two-figures-theory`，基线 `b0ffa7ff`，工作区 `.worktrees/volume-two-figures-theory`。25幅实际引用图包含24幅修订图和新增DS六顶点邻接图；平坦性混合图有上下两个组件，因此工具检查26个组件。科学、样式、字体与书页的判断为本组AI逐图自查，未声称六章全文独立审查。根协调者对最新two-randomness与DS图做过限定范围的独立只读核对，这不扩大本记录的角色范围。

## 工程验证

最终 r3 冻结源执行 `./build.sh all`、`./build.sh check-target`、`make test`，均退出0。全集和六单卷共七份PDF及`target/.build-manifest.json`与当前输入一致；`make test`包含成品一致性、清理回归、部首页分页回归及21项数学结构单元测试，全部成功。另执行`bash tests/check-book-editions.sh`，确认全集与六单卷接口完整，退出0。精确日志路径、SHA及全部七版日志扫描保存于 [validation-summary.json](validation-summary.json)。提交时仍执行正常仓库钩子，不以本记录替代钩子。

最终七版日志没有Missing character、undefined、multiply defined、Float too large或致命错误。日志仍有Overfull hbox提示：全集33、卷一9、卷二16、卷三10、卷四至卷六各1；没有Overfull vbox。本图像任务实际检查25图的卷二页、5张全集代表页及4张灰度页，未发现图像、图内标注或对应图注裁切与碰撞，不把这一有限范围结论写成全书文字版式零告警。

机械一致性复查确认：25图的实际引用源、图资产、渲染页、两个所审PDF的SHA均与最终清单一致；六章各保留一个独立本章小结，旧导航目标及次数未遗漏，原引文序列不变；9张模型背景与选定原始模型输出逐字节相同，文字层报告没有缺字、越界或标签相互重叠。8张当前TikZ为矢量PDF；9个当前Matplotlib PDF组件没有嵌入栅格图，均保存真实字体的矢量字形。共同9文件与根协调版本保持一致，没有自行改写其他组依赖。

## 默认文件检查结果

保留 [file-validation.json](file-validation.json) 的默认300DPI阈值，不降低阈值、不将退出1改写为通过：26次组件检查中9次退出0、17次退出1；17个PNG的有效物理分辨率低于默认300DPI，此外9个Matplotlib PDF有“possibly unembedded”字体提示。

这些结果分别解释如下。

- 模型PNG保留实际模型原图像素和独立真实字层；部分1536宽图在164.6mm宽度下约237DPI，部分1774宽图约274DPI。规格`specs/figures.md`要求按真实物理尺寸、缩放后字号和真实字形验收，并未规定300DPI硬门槛。根协调者已明确采用此适用边界。最终原生图及卷二／代表性全集页实际看过，8pt主体、7.5pt辅助文字可读，未见明显模糊、裁切或边注碰撞，故实际验收通过；不人为上采样制造阈值通过。
- 数据PNG原生按300DPI导出，整数像素舍入后在精确物理宽度下约299.8DPI，默认工具仍如实报失败。正文实际引用同宽矢量PDF，PNG用于预览，不通过提高元数据或上采样伪造分辨率。
- Matplotlib PDF使用Type3矢量字形，默认工具通过FontDescriptor查字体时给出可能未嵌入提示。已直接读取当前9个PDF的字体xref，确认每个Type3均含`/CharProcs`真实字形对象，各PDF嵌入栅格图数为0，证据见 [matplotlib-vector-font-audit.json](matplotlib-vector-font-audit.json)。因此不将它们误称为位图或缺字体文件。

25图的实际字体角色统一为思源黑体主体、霞鹜文楷辅助、Fira Math拉丁／数字／数学；仅Fira实际缺字使用STIX Two Math。字体版本、SHA与许可证沿用全局font-manifest，未修改共享字体。代码图与文字层采用精确五色；模型原图为低饱和近似五色，原生目检记录保留局部偏差，不声称模型像素逐点等于色码。

## 交给集成方的事项

全局`figures/00-shared/academic-drawing/integration-manifest.json`与相关全局登记不在本组写权限内；本组没有宣称旧全局登记检查已通过。集成方应依据 [asset-manifest.json](asset-manifest.json) 的新DS图、实际文件路径、引用宽度和最终SHA同步登记，再在最终集成源上重建和检查七版。本组七份成品只证明本工作区一致性，不替代集成后的构建。

卷一跨卷文字对照按根后续提供的新基线另行执行；本次未提前依赖未完成上传的卷一或进行rebase。
