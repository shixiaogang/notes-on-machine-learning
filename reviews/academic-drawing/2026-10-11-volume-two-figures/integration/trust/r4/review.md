# 可信性01–06最终r4图页绑定与验收

2026-10-12。本轮29图在卷二单卷与全集中的最终图页均重新从根r4 PDF渲染、定位并与冻结r3完整页比较：56张彩色页和14张灰度页全部逐像素一致，变化页0。因此沿用r3已经逐图实际查看的排字、科学连线、图注、正文对应、裁切与碰撞判断，绑定到真实r4最终PDF。没有发现需要修改的问题。

角色为AI自查：本人参与这些图及正文修订，本记录不是独立复核。r3实际目检详见原冻结目录`build/final-root-page-review/visual-notes.md`与`review.md`，根已保存到`integration/trust/r3`。本轮没有把同像素比较伪装成对70张r4图像重新人工目检；没有差异图页需要再看。五处标点所在页面另行实际看过八张，记录在`build/r4-followup/pdf-punctuation/visual-review.md`，不把这八页与图页证据混淆。

|r4最终成品|页数|SHA256|
|---|---|---|
|卷二单卷`target/vol2-foundations.pdf`|495|94ca9126cd7f19bde8dd24827ae8dd70df43ec7b258be5618c864a3344497bbe|
|全集`target/machine-learning-notes.pdf`|2484|d5ee494d27df547b41b7e02d287ba5489f069975279b45b2c34ad3455f42a1ab|

只读根工作区为`/Users/robbieshi/Library/Mobile Documents/com~apple~CloudDocs/writings/Notes/Machine Learning/.worktrees/volume-two-figures`；本任务复用`volume-two-figures-trust`，分支`codex/volume-two-figures-trust`，所有新渲染与记录仅保存在自己的忽略目录。未改根源、PDF或本任务已提交源，未构建、暂存或提交。

## 比较依据与覆盖

先从最终PDF目的地与根实际aux标签重新定位每一稳定图ID及标签，再渲染150 dpi完整页，而非按旧页号直接取图。用Pillow解码RGB后检查尺寸与全部像素字节完全相等，没有容差或平均颜色阈值；每个图—版本—模式均保存旧/新物理页、印刷页、PNG SHA、解码像素SHA与差异边界。`pixel-compare.json`保存这份机械证据，`manifest.json`保存最终PDF、图源、成图和各页proof的SHA及图注、正文引用上下文。

|版本|彩色唯一页|彩色完全一致|灰度唯一页|灰度完全一致|差异页|
|---|---:|---:|---:|---:|---:|
|卷二单卷|28|28|7|7|0|
|全集|28|28|7|7|0|

每版29图共占28页，因为T16和T17共页。灰度代表为T04、T09、T13、T16（同页含T17）、T18、T23、T27。逐图的新绑定详见`page-binding.md`，并由完整页相等证明继承r3对应图的实际判断。图页内排字、箭头、科学关系、图注及相邻正文也在整页像素比较范围内，不只是图框裁片相同。

29张成图和其各图源均与本人已提交55c3d011终稿逐字节一致，实际include路径和物理宽度也与当前根源一致。六章源快照另存于`source-snapshots/`；其中01当前SHA为`900897bd2d61b6a6394738f5a3368ed8207c30f8e613a3901aff8ec90f466855`，相对r3只改变五处scite后标点。该文本输出的实际查看证据与局部C/P/W闭环见另存r4-followup，不以图页一致替代其验证。

`mechanical-validation.json`再次读最终根PDF、正文快照、共享输入、29图源和成图，核对70张proof SHA、图的实际include路径/宽度、两版覆盖计数。该文件只报告输入一致性，不自动生成科学或写作判断。`delivery-inventory.json`列出本目录可复制文件和SHA。

`final-page-bindings.json`为70张实际完整页PNG逐页记录`edition_pdf`、一基物理页、相对proof、150 dpi和RGB/GRAY，供后续主工作区串行构建后重新渲染比较。这里GRAY表示实际调用灰度渲染；本机Poppler把灰度PNG保存为RGB编码，三个通道已验证逐字节相同，额外`png_encoding_mode`如实记录RGB，不将编码模式误当彩色内容。

## 结论边界

最终r4这29图两版的图页无新增待修项，灰度信息继续满足r3逐图所见的轮廓、标记、线型或空间分组辨别。结论仅覆盖声明的图页与7张灰度代表，不称整本PDF无其他问题，不扩大到07/08或其他图组；r3冻结判断继续保留其旧PDF SHA，不改写为当时已经看过r4。
