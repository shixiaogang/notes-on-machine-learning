# 插图入口与图注

第一章图由第一章编辑者插入；这里保留统一入口，不应再次插入。三幅分析图使用跨正文与边注区的 `figure*`，保持 169 mm 宽度。统一导数图建议只插入一次，在一阶与二阶导数两节分别引用同一图的相应面板。

## 最小值与下确界

放在下确界、上确界与是否达到的比较段之后。

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=\linewidth]{figures/math-preparation/analysis-concepts/language-minimum-infimum.pdf}
  \caption{同一函数 $f(x)=x$ 的边界对照。左图定义域为 $(0,1)$，空心端点不属于图像，函数值可任意接近 $0$，却不能取到；右图定义域为 $[0,1]$，实心端点 $(0,0)$ 达到下确界。两图的下确界相同，最小点是否存在取决于可行端点是否保留。图为解析教学示例。}
  \label{fig:prelim-minimum-infimum}
\end{figure}
```

## 度量与收敛

放在通常与离散度量的同一数列对照之后，连续性小节可再引用右面板。

```latex
\begin{figure*}[htbp]
  \centering
  \includegraphics[width=\linewidth]{figures/math-preparation/analysis-concepts/analysis-metric-convergence.pdf}
  \caption{数值相同，距离不同。（a）数列 $x_n=1/n$ 到 $0$ 的通常距离趋于零，离散距离却恒为 $1$，所以收敛要连同度量说明。（b）恒等映射从通常度量空间映入离散度量空间时，任意非零且很小的输入位移仍对应输出距离 $1$，不能进入 $\varepsilon=1/2$ 的输出邻域，故它在 $0$ 处不连续。图为解析教学示例。}
  \label{fig:analysis-metric-convergence}
\end{figure*}
```

## 连续、跳跃与不可导

放在连续性解释后，一元导数小节回用右面板。

```latex
\begin{figure*}[htbp]
  \centering
  \includegraphics[width=\linewidth]{figures/math-preparation/analysis-concepts/analysis-continuity-counterexamples.pdf}
  \caption{三个不同的局部性质。（a）$f(x)=x^2$ 在 $0$ 处可用 $\delta=1/2$ 控制 $\varepsilon=1/4$：严格位于输入邻域内的点，其函数值严格落在输出邻域内。（b）阶跃函数在 $0$ 的左极限为 $0$，取值却为 $1$，空心点和实心点区分两者。（c）$|x|$ 在 $0$ 处连续，但左右导数分别为 $-1$ 和 $1$，不存在共同的双侧导数。图中曲线均为解析教学示例。}
  \label{fig:analysis-continuity-counterexamples}
\end{figure*}
```

## 一阶与二阶导数

在一阶近似教学例之后插入，二阶导数与曲率节引用同一图比较二次修正。

```latex
\begin{figure*}[htbp]
  \centering
  \includegraphics[width=\linewidth]{figures/math-preparation/analysis-concepts/analysis-derivative-orders.pdf}
  \caption{统一函数 $f(x)=x^3-3x$ 在 $x_0=1/2$ 处的两阶近似，记 $h=x-x_0$。（a）蓝线为真函数，红虚线为切线近似 $T_1(h)=f(x_0)+f'(x_0)h$，黄点线加入二次项 $f''(x_0)h^2/2$，得到 $T_2(h)$。（b）扣除各近似后的带符号余项分别为 $3h^2/2+h^3$ 与 $h^3$，标出 $h=\pm0.1$ 的精确结果。一阶导数确定切线，二阶导数补充局部曲率；余项的正负表示真值位于近似值的哪一侧。图为解析教学示例。}
  \label{fig:analysis-derivative-orders}
\end{figure*}
```
