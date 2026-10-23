# SVD 构造三部曲：AᵀA → 特征值 → 奇异向量

回应第 6 章“SVD 的左右奇异向量是怎么一步步从矩阵造出来的”的读者问题。解析式固定构造，不是实验数据。

| 文件 | 读图任务 | 建议正文宽度 | 建议图环境 |
| --- | --- | --- | --- |
| `ls-svd-construction.pdf/.png` | 三步：① 形成对称 Gram 矩阵 AᵀA；② 对称谱引理正交对角化得特征值；③ σᵢ=√λᵢ，右奇异向量 vᵢ=特征向量，左奇异向量 uᵢ=Avᵢ/σᵢ | 169 mm | `figure*` |

## 关键精确值
- $\bm A=\begin{smallmatrix}2&0.5\\0.5&1\end{smallmatrix}$，$\bm A^\top\bm A=\begin{smallmatrix}4.25&1.5\\1.5&1.25\end{smallmatrix}$。
- 特征值 $\lambda_1\approx4.87$、$\lambda_2\approx0.63$；奇异值 $\sigma_1\approx2.21$、$\sigma_2\approx0.79$。
- $\bm v_i$ 为右奇异向量（即 $\bm A^\top\bm A$ 的特征向量），$\bm u_i=\bm A\bm v_i/\sigma_i$。

## 运行
```bash
python3 figures/01-mathematical-preliminaries-upper/02-linear-spaces/matplotlib/ls-svd-construction/plots.py
```
不调用 LaTeX，无随机采样；`sources.json` 保存数值分解。
