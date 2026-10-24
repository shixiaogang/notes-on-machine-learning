# 张量积槽位

回应第 5 章“运算”中“二阶张量为什么能看成基槽位上的一组数”的读者问题。网格与外积数值由解析式直接求出，是教学构造。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-tensor-product-slots.pdf/.png/.svg` | 乘积基 $e_i\otimes f_j$ 排成 2×2 槽位；秩一张量即外积矩阵 | 112 mm | `figure` |

## 图中元素含义

- 上方：红轴 $e_1,e_2$ 为行、蓝轴 $f_1,f_2$ 为列，四块槽位 $e_i\otimes f_j$，一个二阶张量就是这四块上的数。
- 下方：秩一张量 $u\otimes v$，$u=(1,2)$，$v=(3,1)$，外积矩阵 $(u\otimes v)_{ij}=u_iv_j$。

## 关键精确值

- 外积矩阵：$\begin{pmatrix}1\cdot3&1\cdot1\\2\cdot3&2\cdot1\end{pmatrix}=\begin{pmatrix}3&1\\6&2\end{pmatrix}$。

## 运行

```bash
python3 figures/01-mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-tensor-product-slots/plots.py
```

从任意目录运行均可，不调用 LaTeX，无随机采样。`sources.json` 保存向量与外积矩阵。
