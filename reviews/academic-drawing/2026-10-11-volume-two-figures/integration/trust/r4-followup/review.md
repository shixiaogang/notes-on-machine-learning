# 可信性r4跟进记录

2026-10-12，可信基础01的五处scite后标点修正已经在真实根稿中完成局部C/P/W复读，文本问题5项均关闭，未发现本轮修改引入新语义问题。本人参与原文字与制图，角色为AI自查。

|身份|SHA256|
|---|---|
|改前01正文（r3）|9b1396b291ec22fd1cbd6c4ed044598a9c1fb953076e4e02e6630391b4f53c6c|
|五标点候选=实际根改后01正文|900897bd2d61b6a6394738f5a3368ed8207c30f8e613a3901aff8ec90f466855|
|实际references宏源|0e1180f26093e231bb9c207cb608cd76e06ffb90de7cea4dc4b839c2813faffd|

实际根只读路径为`/Users/robbieshi/Library/Mobile Documents/com~apple~CloudDocs/writings/Notes/Machine Learning/.worktrees/volume-two-figures`，本记录写在自己的`volume-two-figures-trust/build/r4-followup/`。本轮只写忽略目录中的快照、候选和证据，未修改根源或本人正文，未构建、提交或修改PDF。

## 记录与覆盖

- `old-new.json`与`punctuation-only.patch`：r3 L270/343/354/372/381五个完整自然段的old/new及仅五字符的精确差异。四个分号和一个逗号均改为源码中文句号，宏吸收后只输出自身的一个句号。
- `C-local.md`：第一遍局部章级定位，真实章首/研究内容/前沿/小结与五段角色；没有重跑或重签整章C。
- `P-local.md`：第二遍五段及必要邻接上下文的作用、前后关系、入口与范围核查。
- `W-local-and-closure.md`：第三遍21个句子的实际意思和判断依据，E1–E12逐项、适用门槛，以及五个稳定发现与实际根写回闭环。局部句界拆开没有增删对象、条件、量词或证据强度。
- `01-foundations-r3.tex`、`01-foundations-punctuation-candidate.tex`、`01-foundations-root-at-preparation.tex`、`01-foundations-root-applied.tex`：分别保存改前、候选、准备时真实根、写回后真实根；后两个不是口头承诺。
- `references-macro.tex`：实际宏输入快照，`NewDocumentCommand{scite}{m t。}`接受并吸收源码句号，内部固定输出句号。
- `mechanical-closure.json`：实际根与候选一致，五字符替换及引文/term/引用/公式字符未变的机械证据，不生成语义接受判断。

记录结论：局部记录可接受。正文结论：在声明的五段及连续上下文范围内，五项标点发现实际修订后复读通过；没有据此扩大为重新完成全章或全书审查。外部论文、原算法实现和证明没有因本次标点任务重核。

## 最终PDF跟进闭环

r3的70张图页proof和判断继续封存在原`build/final-root-page-review/`，没有覆盖旧记录。r4冻结后另行重新渲染29图两版，共56张彩色完整页和14张灰度完整页，并以稳定图ID和标签重新定位、逐点比较实际页内像素：70张均与r3完全相同，差异页0。新PDF绑定与逐图页码见另存的`build/final-root-page-review-r4/`；图页判断明确继承r3的真实目检，不伪称r4将70张又人工重看。

五处标点则在r4两版的八张实际页面重新目检，宏输出均只有一个句号，原多余分号/逗号消失，没有发现新裁切、碰撞或句界问题。逐项所见、物理页/印刷页和最终PDF SHA见`pdf-punctuation/visual-review.md`；十个发现—版本绑定及八张proof的SHA见`pdf-punctuation/manifest.json`。实际根01正文与五标点候选仍逐字节一致，五项文本及最终视觉输出均闭环，需修0。

当前结论绑定卷二SHA `94ca9126cd7f19bde8dd24827ae8dd70df43ec7b258be5618c864a3344497bbe`、全集SHA `d5ee494d27df547b41b7e02d287ba5489f069975279b45b2c34ad3455f42a1ab`。没有据此宣称其他页面或其他图组通过。

本目录`final-page-bindings.json`还为八张实际保存完整页记录最终PDF路径、物理页、相对proof、150 dpi及RGB，以便后续主工作区生成时间变化后真实重渲染比较。`mechanical-pdf-validation.json`核对当前根01正文、宏、两版PDF及八张proof的冻结SHA，并指向实际人工所见记录；它不生成视觉接受判断。
