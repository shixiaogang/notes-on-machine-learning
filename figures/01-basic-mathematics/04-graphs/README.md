# 卷一第4部分“图”图像

本目录保存第15—20章（图与连接结构、图的遍历与结构计算、图上的组合优化、集合函数与子集选择、图上的动态规划、图上的谱方法）独用的图像。全部为 TikZ 图源（含 pgfplots 曲线），图中数值均来自正文算例，并已按正文逐项复算；图名前缀 `c1`—`c6` 对应本部分第1—6章。

每幅图一个目录，`figure.tex` 为可编辑图源，`figure.pdf/png/svg` 与 `figure.render.json` 由下列命令导出（从项目根目录运行）：

```sh
python3 figures/00-shared/academic-drawing/render_tikz.py figures/01-basic-mathematics/04-graphs/tikz/<图名>/figure.tex
```

`c1-spanning-trees/generate.py` 枚举贯穿四点图的全部生成树并写出图源；`c6-filter-responses/chebyshev_coefficients.py` 计算图中 Chebyshev 逼近的系数。

| 图名 | 引用位置（章目录/节文件） | 物理尺寸（mm） |
| --- | --- | --- |
| `c1-adjacency-square-walks` | 01-graphs-and-connectivity/05-representations.tex | 110.352×37.984 |
| `c1-components` | 01-graphs-and-connectivity/03-connectivity-and-separation.tex | 110.808×31.962 |
| `c1-cut-vertex-bridge` | 01-graphs-and-connectivity/03-connectivity-and-separation.tex | 106.765×30.939 |
| `c1-directed-cycle-dag` | 01-graphs-and-connectivity/02-adjacency-and-paths.tex | 85.937×29.947 |
| `c1-direction-orientation` | 01-graphs-and-connectivity/01-basic-concepts.tex | 98.189×36.953 |
| `c1-four-representations` | 01-graphs-and-connectivity/05-representations.tex | 89.524×79.202 |
| `c1-isomorphism-relabeling` | 01-graphs-and-connectivity/06-isomorphism.tex | 97.688×31.958 |
| `c1-running-graph-drawings` | 01-graphs-and-connectivity/01-basic-concepts.tex | 106.765×33.962 |
| `c1-separator-sets` | 01-graphs-and-connectivity/03-connectivity-and-separation.tex | 104.186×32.456 |
| `c1-spanning-trees` | 01-graphs-and-connectivity/04-trees-and-forests.tex | 97.652×47.173 |
| `c1-subgraph-induced` | 01-graphs-and-connectivity/01-basic-concepts.tex | 112.187×33.613 |
| `c1-tree-forest` | 01-graphs-and-connectivity/04-trees-and-forests.tex | 107.685×28.201 |
| `c1-tree-properties` | 01-graphs-and-connectivity/04-trees-and-forests.tex | 99.688×73.963 |
| `c1-walk-path-cycle` | 01-graphs-and-connectivity/02-adjacency-and-paths.tex | 110.688×33.429 |
| `c1-weight-semantics` | 01-graphs-and-connectivity/01-basic-concepts.tex | 106.768×60.219 |
| `c2-bfs-queue-trace` | 02-traversal-and-structure/01-breadth-first-traversal.tex | 106.733×42.556 |
| `c2-bfs-weighted-counterexample` | 02-traversal-and-structure/01-breadth-first-traversal.tex | 87.778×26.684 |
| `c2-components-spanning-forest` | 02-traversal-and-structure/03-connected-structures.tex | 104.835×32.978 |
| `c2-dfs-cycle-detection` | 02-traversal-and-structure/02-depth-first-traversal.tex | 102.919×34.311 |
| `c2-dfs-stack-trace` | 02-traversal-and-structure/02-depth-first-traversal.tex | 109.844×42.972 |
| `c2-dfs-topological-order` | 02-traversal-and-structure/04-topological-order.tex | 93.768×47.025 |
| `c2-kahn-diamond` | 02-traversal-and-structure/04-topological-order.tex | 94.823×40.27 |
| `c2-kosaraju-condensation` | 02-traversal-and-structure/03-connected-structures.tex | 146.547×46.461 |
| `c2-multi-source-bfs` | 02-traversal-and-structure/01-breadth-first-traversal.tex | 98.975×28.187 |
| `c2-separator-blocks` | 02-traversal-and-structure/05-separator-blocks.tex | 103.886×37.807 |
| `c2-union-find` | 02-traversal-and-structure/03-connected-structures.tex | 110.486×38.894 |
| `c2-wl-cycle-triangles` | 02-traversal-and-structure/06-vertex-labeling.tex | 79.46×42.189 |
| `c2-wl-path-refinement` | 02-traversal-and-structure/06-vertex-labeling.tex | 93.998×35.74 |
| `c3-assign-hungarian` | 03-combinatorial-optimization/06-assignment.tex | 107.714×46.087 |
| `c3-cut-exchange` | 03-combinatorial-optimization/02-minimum-spanning-tree.tex | 99.187×37.758 |
| `c3-dag-labels` | 03-combinatorial-optimization/01-shortest-paths.tex | 71.635×45.092 |
| `c3-dijkstra-counterexample` | 03-combinatorial-optimization/01-shortest-paths.tex | 105.583×35.613 |
| `c3-dijkstra-trace` | 03-combinatorial-optimization/01-shortest-paths.tex | 147.687×41.921 |
| `c3-distance-outcomes` | 03-combinatorial-optimization/01-shortest-paths.tex | 73.801×44.768 |
| `c3-edmonds-karp-layers` | 03-combinatorial-optimization/03-max-flow-min-cut.tex | 119.567×37.606 |
| `c3-flow-network-cut` | 03-combinatorial-optimization/03-max-flow-min-cut.tex | 82.564×32.748 |
| `c3-kruskal-steps` | 03-combinatorial-optimization/02-minimum-spanning-tree.tex | 106.5×36.072 |
| `c3-match-augment` | 03-combinatorial-optimization/05-matching.tex | 117.094×43.706 |
| `c3-match-flow-network` | 03-combinatorial-optimization/05-matching.tex | 100.76×45.494 |
| `c3-match-maximal-maximum` | 03-combinatorial-optimization/05-matching.tex | 67.07×27.951 |
| `c3-max-flow-certificate` | 03-combinatorial-optimization/03-max-flow-min-cut.tex | 104.186×42.037 |
| `c3-mcf-lower-bound-shift` | 03-combinatorial-optimization/04-min-cost-flow.tex | 109.767×41.952 |
| `c3-mcf-network` | 03-combinatorial-optimization/04-min-cost-flow.tex | 68.527×37.165 |
| `c3-mcf-residual-cycle` | 03-combinatorial-optimization/04-min-cost-flow.tex | 103.579×39.977 |
| `c3-mst-vs-spt` | 03-combinatorial-optimization/02-minimum-spanning-tree.tex | 95.793×30.293 |
| `c3-ns-artificial-start` | 03-combinatorial-optimization/04-min-cost-flow.tex | 132.186×49.706 |
| `c3-ns-degenerate` | 03-combinatorial-optimization/04-min-cost-flow.tex | 96.054×41.3 |
| `c3-ns-pivots` | 03-combinatorial-optimization/04-min-cost-flow.tex | 142.053×47.128 |
| `c3-ns-tree-basis` | 03-combinatorial-optimization/04-min-cost-flow.tex | 149.144×48.542 |
| `c3-prim-steps` | 03-combinatorial-optimization/02-minimum-spanning-tree.tex | 129.858×37.948 |
| `c3-problem-relations` | 03-combinatorial-optimization/06-assignment.tex | 103.914×46.951 |
| `c3-relaxation` | 03-combinatorial-optimization/01-shortest-paths.tex | 102.993×32.868 |
| `c3-residual-arc` | 03-combinatorial-optimization/03-max-flow-min-cut.tex | 74.186×28.861 |
| `c3-undo-flow` | 03-combinatorial-optimization/03-max-flow-min-cut.tex | 113.901×36.523 |
| `c4-budget-ratio-failure` | 04-set-functions-and-subset-selection/05-budget-selection.tex | 109.146×30.702 |
| `c4-budget-rule-comparison` | 04-set-functions-and-subset-selection/05-budget-selection.tex | 98.538×23.911 |
| `c4-cut-submodular-cases` | 04-set-functions-and-subset-selection/02-properties.tex | 110.723×45.484 |
| `c4-greedy-rounds-vs-optimum` | 04-set-functions-and-subset-selection/04-cardinality-selection.tex | 107.177×35.158 |
| `c4-marginal-gain-overlap` | 04-set-functions-and-subset-selection/01-set-functions.tex | 91.74×35.161 |
| `c4-mobius-divisor-poset` | 04-set-functions-and-subset-selection/03-mobius-inversion.tex | 52.613×46.186 |
| `c4-pairwise-config-table` | 04-set-functions-and-subset-selection/06-pairwise-binary-minimization.tex | 72.383×38.396 |
| `c4-property-counterexamples` | 04-set-functions-and-subset-selection/02-properties.tex | 108.687×58.244 |
| `c4-sensor-coverage` | 04-set-functions-and-subset-selection/01-set-functions.tex | 87.027×33.651 |
| `c4-st-cut-construction` | 04-set-functions-and-subset-selection/06-pairwise-binary-minimization.tex | 104.687×45.501 |
| `c4-subset-binary-cube` | 04-set-functions-and-subset-selection/01-set-functions.tex | 103.209×46.186 |
| `c4-subset-lattice-cumulative` | 04-set-functions-and-subset-selection/03-mobius-inversion.tex | 99.187×69.688 |
| `c5-bag-message-table` | 05-dynamic-programming-on-graphs/06-bag-dynamic-programming.tex | 105.65×53.7 |
| `c5-chain-recursion` | 05-dynamic-programming-on-graphs/02-chain-and-tree-dp.tex | 109.587×41.466 |
| `c5-chordal-four-cycle` | 05-dynamic-programming-on-graphs/05-decomposition-construction.tex | 106.306×38.933 |
| `c5-clique-in-bag` | 05-dynamic-programming-on-graphs/04-tree-decomposition.tex | 102.648×55.651 |
| `c5-clique-tree-mst` | 05-dynamic-programming-on-graphs/05-decomposition-construction.tex | 102.306×43.0 |
| `c5-configuration-scopes` | 05-dynamic-programming-on-graphs/01-local-functions.tex | 109.269×49.541 |
| `c5-elimination-orders` | 05-dynamic-programming-on-graphs/03-variable-elimination.tex | 105.004×69.49 |
| `c5-elimination-step` | 05-dynamic-programming-on-graphs/03-variable-elimination.tex | 102.687×47.188 |
| `c5-elimination-to-bags` | 05-dynamic-programming-on-graphs/04-tree-decomposition.tex | 103.283×33.186 |
| `c5-elimination-to-decomposition` | 05-dynamic-programming-on-graphs/05-decomposition-construction.tex | 104.369×69.846 |
| `c5-min-degree-min-fill` | 05-dynamic-programming-on-graphs/05-decomposition-construction.tex | 96.778×58.141 |
| `c5-running-intersection` | 05-dynamic-programming-on-graphs/04-tree-decomposition.tex | 111.016×44.327 |
| `c5-three-representations` | 05-dynamic-programming-on-graphs/01-local-functions.tex | 111.936×46.2 |
| `c5-tree-messages` | 05-dynamic-programming-on-graphs/02-chain-and-tree-dp.tex | 108.514×58.963 |
| `c6-component-null-modes` | 06-spectral-methods/04-spectrum-and-connectivity.tex | 108.546×70.421 |
| `c6-cut-indicator` | 06-spectral-methods/07-spectral-partition.tex | 108.423×39.204 |
| `c6-cycle-fourier-basis` | 06-spectral-methods/05-graph-fourier-transform.tex | 112.698×45.103 |
| `c6-degree-weighted-length` | 06-spectral-methods/03-normalized-laplacian.tex | 96.979×38.523 |
| `c6-energy-edge-weights` | 06-spectral-methods/02-graph-laplacian.tex | 112.924×27.922 |
| `c6-filter-responses` | 06-spectral-methods/06-graph-filtering.tex | 98.005×49.668 |
| `c6-four-path-sweep` | 06-spectral-methods/07-spectral-partition.tex | 93.751×52.839 |
| `c6-laplacian-two-routes` | 06-spectral-methods/02-graph-laplacian.tex | 111.887×37.232 |
| `c6-path-modes` | 06-spectral-methods/04-spectrum-and-connectivity.tex | 79.855×31.485 |
| `c6-polynomial-locality` | 06-spectral-methods/06-graph-filtering.tex | 110.046×47.269 |
| `c6-spectral-projection` | 06-spectral-methods/05-graph-fourier-transform.tex | 91.038×27.929 |
| `c6-three-laplacians` | 06-spectral-methods/03-normalized-laplacian.tex | 97.702×43.688 |
| `c6-vertex-edge-functions` | 06-spectral-methods/01-vertex-and-edge-functions.tex | 112.088×39.599 |
