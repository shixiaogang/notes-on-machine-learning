# 根最终r4成品：理论部分局部验收交付

本目录位于theory独立worktree的忽略build/，根源/资源和PDF只读。本组曾制作25图，因此这是AI自查和跨卷局部接口复读，不能称全文独立审查。未构建、修改或提交根输入。

- [当前25图、5全集代表、4灰度的验收方式](actual-page-review-r4.md)
- [完整PDF/源/资产/图源/proof SHA及整页比较](r4-binding.json)
- [47张实际保存完整页PNG的版名、物理页、相对proof、DPI与色彩空间](final-page-bindings.json)
- [差异图页及六处改后正文的手写实际观察](manual-observations-r4.json)
- [七处指定Overfull实页闭环](overfull-review-r4.md)
- [六处改后局部C](followup-C-r4.md)、[P](followup-P-r4.md)、[W/特殊单元/E1–E12](followup-W-r4.md)
- [六项实际源及实际PDF闭环](closure-r4.json)
- [当前六章源/宏/构建manifest快照SHA](inputs-r4-sha.json)
- [外部冻结PDF的受审SHA清单](frozen-pdf-bindings.json)
- [本交付全部文件SHA清单](delivery-manifest-r4.json)

31/34个图页用途与r3实际目检页的PNG字节/像素一致；DS在卷二p168、全集p1114、灰度p168三张差异整页均实际重看。6/7个指定Overfull页与r3一致，B70/p132差异页实际重看。六个修改正文页全部实际复读，数量短语与五处scite句末标点均已关闭，无新问题。

原r3诊断保留在相邻final-root-page-review，记录不会事后改为“当时已关闭”。建议同时保存两目录以保留发现与修复链。r4交付不包含大PDF，冻结副本位于本worktree的build/frozen-review-pdfs-r4；根另行归档受审大PDF，不能用后续重建的SHA冒称本次成品。主工作区重建后应依据final-page-bindings.json重渲染这些完整页，相同页重新绑定、差异页实际重看。

图源未改且物理宽度保持原登记，8/7.5pt真字；默认300DPI阈值报告保留，未人工上采样源背景。七处Overfull无实际裁切/边注碰撞，但原警告保留，不宣称全书零Overfull。全集只有五代表和四灰度用途，不声称全量全集/灰度检查。

prepare_r4.py保留初次渲染/比较方法，finalize_r4.py仅机械绑定手写观察、生成SHA清单与表格。已渲染目录不应直接重跑prepare_r4.py覆盖证据；源大PDF已移到本地外部冻结目录。
