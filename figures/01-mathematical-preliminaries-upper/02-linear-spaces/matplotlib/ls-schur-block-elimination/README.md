# Schur 补的 2×2 分块消元过程

回应第 6 章“Schur 补在分块求解里到底在做什么”的读者问题。解析式固定构造，不是实验数据。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-schur-block-elimination.pdf/.png` | 左：把 2×2 矩阵按左上块 A=2 分块；右：用第一行消去 x₁ 后，右下角残留 Schur 补 S=3/2，约化系统解出 x₂ 再回代 | 169 mm | `figure*` |

## 关键精确值
- $\bm M=\begin{smallmatrix}2&1\\1&2\end{smallmatrix}$，右端 $(1,3)$；$\bm A=2$ 可逆。
- 第一行 $2x_1+x_2=1$ 给出 $x_1=(1-x_2)/2$；代入第二行得 $(3/2)x_2=5/2$，$x_2=5/3$，回代 $x_1=-1/3$。
- Schur 补 $S=D-CA^{-1}B=2-1\cdot(1/2)\cdot1=3/2$；$\det\bm M=3=\det\bm A\cdot\det S=2\cdot3/2$。

## 运行
```bash
python3 figures/01-mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-schur-block-elimination/plots.py
```
不调用 LaTeX，无随机采样；`sources.json` 保存精确读数。
