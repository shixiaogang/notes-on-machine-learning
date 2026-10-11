from pathlib import Path
root=Path('tex/02-foundations/02-learning-theory')
fixes={
'04-convex-learning-and-stability.tex':[
('继续使用$[0,1]$上的样本均值','继续使用$z_i\\in[0,1]$的样本均值'),
('每个固定$S,z$下的损失关于$U$可积','每个固定$S,z$下的$\\ell(A(S,U),z)$关于$U$可积'),
('两项都趋于零时，算法PAC学习该问题','当$\\bar\\beta_n\\to0$且$\\rho_n\\to0$时，算法PAC学习该问题'),
('观测恒定时该量为零','观测恒定、即$\\sigma^2=0$时，该量为零'),
('另一个方向可取二值观测：','另一个方向可取$z_i\\in\\{0,1\\}$的二值观测：'),
('得分类复杂度','得分函数类复杂度'),
('\\begin{proof}\n投影不扩大距离，因此定理~\\ref{thm:convex-sgd-stability}', '\\begin{proof}\n若$B=0$，可行集只有$\\bm0$，输出与比较风险相同，结论立即成立。以下设$B>0$。\n投影不扩大距离，因此定理~\\ref{thm:convex-sgd-stability}'),
('梯度条件均值是$\\nabla\\hat R_S(\\bm w^{(t)})$','梯度条件均值满足$\\mathbb E[\\bm g_t]=\\nabla\\hat R_S(\\bm w^{(t)})$'),
],
'05-deep-learning-theory.tex':[
('核正定只保证能够插值','核正定、即$\\lambda_{\\min}(\\bm K_0)>0$，只保证能够插值'),
('如果标签平方和按$n$增长','如果标签平方和$\\|\\bm r\\|_2^2$按$n$增长'),
('投影扰动的绝对值期望至多$s\\kappa$','投影扰动$\\langle\\bm v-\\widehat{\\bm v},\\bm\\varphi_0(\\bm x)\\rangle$的绝对值期望至多$s\\kappa$'),
('风险采用完整平方损失；','风险采用完整平方损失$(\\bm x^\\top\\bm w-y)^2$；'),
('单位方向$\\bm u$的最小经验间隔','单位方向$\\bm u$满足$\\|\\bm u\\|_2=1$，其最小经验间隔'),
('链式法则给出$\\dot{\\bm U}=-\\bm G\\bm V$、$\\dot{\\bm V}=-\\bm G^\\top\\bm U$，从而','链式法则给出\n\\[\n \\dot{\\bm U}=-\\bm G\\bm V,\\qquad\n \\dot{\\bm V}=-\\bm G^\\top\\bm U.\n\\]\n从而'),
('两因子的范数平方都等于$\\operatorname{tr}\\bm\\Sigma$，从而达到等号。','两因子的范数平方都等于$\\operatorname{tr}\\bm\\Sigma$，从而达到等号。当$k>\\operatorname{rank}(\\bm W)$时，在两因子后补零列以满足指定列数。'),
('\\rho_m=m^{-1}\\sum_j\\delta_{(a_j,\\bm w_j)}','\\rho_m=m^{-1}\\sum_{j=1}^m\\delta_{(a_j,\\bm w_j)}'),
('其中$\\delta$为点质量分布','其中$\\delta_{(a,\\bm w)}$是在$(a,\\bm w)$处的点质量分布'),
('对所有输入一致为$L_\\psi$-Lipschitz','对所有$\\bm x\\in\\mathcal X$一致地关于$\\bm\\vartheta\\in\\Theta$为$L_\\psi$-Lipschitz'),
('固定$\\rho$有','固定$\\rho\\in\\mathcal M$有'),
('$a_n,\\xi_n$以分布无关速率趋零时','当$a_n\\to0$且$\\xi_n\\to0$具有分布无关速率时'),
('信息代价为$0.9\\log1.8+0.1\\log0.2\\approx0.368$','信息代价为$D_{\\mathrm{KL}}(Q\\|P_0)=0.9\\log1.8+0.1\\log0.2\\approx0.368$'),
('若平均先验代价至多$K_n$','若平均先验代价满足$\\mathbb E_SD_{\\mathrm{KL}}(Q_S\\|P_0)\\leq K_n$'),
],
'06-transfer-learning-theory.tex':[
('固定假设空间$\\mathcal H$和$[0,1]$值预测损失','固定假设空间$\\mathcal H$和$[0,1]$值预测损失$\\ell(\\widehat y,y)$'),
('亦记$\\ell(h,z)=\\ell(h(x),y)$','对$z=(x,y)\\in Z$亦记$\\ell(h,z)=\\ell(h(x),y)$'),
('取$\\mathcal H\\triangle\\mathcal H$才对应','取$\\mathcal G=\\mathcal H\\triangle\\mathcal H$才对应'),
('\\mathcal P_T^X(B)=\\int_Bw\\,\\mathrm d\\mathcal P_S^X','\\mathcal P_T^X(B)=\\int_B w(x)\\,\\mathrm d\\mathcal P_S^X(x)'),
('几乎处处$w\\leq\\kappa$','几乎处处$w(x)\\leq\\kappa$'),
('若$\\operatorname{VC}(\\mathcal H)=d$','若$\\operatorname{VC}(\\mathcal H)=d<\\infty$'),
('可用$O(p_{\\mathrm{net}}L_{\\mathrm{net}}\\log p_{\\mathrm{net}})$上界代入','可用$d=O(p_{\\mathrm{net}}L_{\\mathrm{net}}\\log p_{\\mathrm{net}})$上界代入'),
('损失有界使每个$h$的加权总体误差至多$b_w$。','损失有界使每个$h$都满足$|\\mathbb E_{(x,y)\\sim\\mathcal P_S}[\\widehat w(x)\\ell(h(x),y)]-R_T(h)|\\leq b_w$。'),
('\\sum_y a_y\\mathsf K_y=0','\\sum_{y=1}^C a_y\\mathsf K_y=0'),
('矩阵$\\bm M$第$y$列为$\\mathbb E_{\\mathsf K_y}\\bm\\psi$，则目标统计为$\\bm M\\bm q$','矩阵$\\bm M\\in\\mathbb R^{m\\times C}$第$y$列为$\\mathbb E_{x\\sim\\mathsf K_y}\\bm\\psi(x)$。记$\\bm q=(q_1,\\ldots,q_C)^\\top$，则目标统计满足$\\mathbb E_{x\\sim\\mathcal P_T^X}\\bm\\psi(x)=\\bm M\\bm q$'),
('且源类别概率统一至少$\\pi_{\\min}>0$','且源类别概率对$y=1,\\ldots,C$统一满足$\\mathcal P_S^Y(\\{y\\})\\geq\\pi_{\\min}>0$'),
('且有样本无关的统一$B_{\\mathrm{KL}}$','且有样本无关的统一上界$D_{\\mathrm{KL}}(Q\\|P_0)\\leq B_{\\mathrm{KL}}$'),
('\\overline{\\mathcal P}=K^{-1}\\sum_e\\mathcal P_e','\\overline{\\mathcal P}=K^{-1}\\sum_{e=1}^K\\mathcal P_e'),
('预测相同的输入没有额外错误','在$h(x)=h^\\star(x)$的输入处没有额外错误'),
('L(h,D)=n^{-1}\\sum_i\\ell(h,z_i)','L(h,D)=n^{-1}\\sum_{i=1}^n\\ell(h,z_i)'),
('固定已知或可估计密度比后，才能用VC维、范数复杂度、稳定性或PAC--Bayes计算有限样本代价。','固定相应跨域联系后，可用VC维、范数复杂度、稳定性或PAC--Bayes计算有限样本代价；重加权路线还须有已知或能在允许族上一致估计的密度比。'),
]}
for f,items in fixes.items():
 p=root/f;s=p.read_text()
 for old,new in items:
  assert s.count(old)==1,(f,old,s.count(old));s=s.replace(old,new)
 p.write_text(s)
