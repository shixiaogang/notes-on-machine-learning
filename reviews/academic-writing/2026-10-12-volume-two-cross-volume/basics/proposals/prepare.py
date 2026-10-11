from pathlib import Path
import difflib, hashlib, json, re

base = Path(__file__).resolve().parents[1]
snapshot = base / 'snapshots' / 'basics-7535c2f8'
draft = base / 'proposals' / 'draft'
units = []

def para(source, prefix):
    starts = [m.start() for m in re.finditer(r'(?m)^' + re.escape(prefix), source)]
    assert len(starts) == 1, (prefix, starts)
    start = starts[0]
    end = source.find('\n\n', start)
    if end < 0:
        end = len(source)
    return source[start:end]

def change(source, file, ident, old, new):
    assert source.count(old) == 1, (ident, source.count(old))
    initial = (snapshot / file).read_text()
    assert initial.count(old) == 1, (ident, 'not a unique original unit')
    units.append({'id': ident, 'file': file, 'old': old, 'new': new,
                  'old_line': initial[:initial.index(old)].count('\n') + 1,
                  'old_sha256': hashlib.sha256(old.encode()).hexdigest(),
                  'new_sha256': hashlib.sha256(new.encode()).hexdigest()})
    return source.replace(old, new)

file = 'tex/02-foundations/01-basics/02-machine-learning-models.tex'
original = (snapshot / file).read_text()
s = original
old = para(s, '两个分类器可能给出相同标签')
new = old.replace('第一卷的函数空间、概率推断、范数与评分规则在这里用于解释比较依据。', '候选函数集合、概率关系、向量差异与评分规则，分别为这些比较提供数学依据。')
s = change(s, file, 'M-P01', old, new)
old = para(s, r'\term{朴素贝叶斯}')
new = old.replace('增加条件独立假设：给定类别后，一个特征的值不再改变其他特征的分布。该类别内部的特征联合概率便可由各特征的条件概率相乘计算。', r'增加条件独立假设：给定类别后，各特征相互独立，整组特征的联合条件概率等于各特征条件概率的乘积（可参考\BookSectionRef{sec:probability-moments-independence}{第一卷“随机变量”章的“随机变量的独立关系”}）。')
s = change(s, file, 'M-P02', old, new)
old = s[s.index('得到类别或区间概率'):s.index('记$\\Theta$为参数的允许范围。')]
new = r'''得到类别或区间概率，需要先区分参数已知和参数待估计两种情形。\term{概率推断}（probabilistic inference）利用模型分布和已有信息计算所需概率。参数给定时，可以直接计算类别概率、区间概率等结果；参数未知时，还要用训练数据确定参数或描述参数的不确定性。

\term{似然}（likelihood）把观测到的训练数据$\mathcal D$固定，比较不同允许参数赋予这些数据的概率或密度。在最大值能够取到时，\term{最大似然估计}（maximum likelihood estimation）选择使似然最大的参数（可参考\BookSectionRef{sec:statistics-likelihood-robustness}{第一卷“随机变量”章的“有限维目标的估计”}）。一种做法是用\term{点估计}（point estimation）选出$\hat{\bm{\theta}}$，再使用插件预测$p(y\mid\bm x,\hat{\bm{\theta}})$；另一种做法是用\term{贝叶斯推断}（Bayesian inference）结合\term{先验分布}（prior distribution）与训练数据得到\term{后验分布}（posterior distribution），再对不同参数对应的预测分布加权平均。

'''
s = change(s, file, 'M-P03', old, new)
old = s[s.index('记$\\Theta$为参数的允许范围。'):s.index('即使参数完全给定')]
new = r'''记$\Theta$为参数的允许范围，先考虑参数后验具有相对于Lebesgue测度的密度$p(\bm\theta\mid\mathcal D)$的情形。在新结果$y$给定$\bm x$和$\bm\theta$后与$\mathcal D$条件独立的常见设定下，后验预测写为
\[
  p(y\mid\bm x,\mathcal D)
  =\int_{\Theta} p(y\mid\bm x,\bm\theta)
    p(\bm\theta\mid\mathcal D)\,\mathrm d\bm\theta.
\]
离散参数将积分换成对允许取值的求和；更一般的后验则按其概率测度积分。插件预测固定一个估计参数，后验预测则对允许参数集合中的预测按后验权重求平均（可参考\BookSectionRef{sec:statistics-scoring-calibration}{第一卷“随机变量”章的“预测分布的计算与评价”}）。求和或积分传播的是参数不确定性；使用者最终取得点值、摘要或完整分布，还由输出接口决定。
'''
s = change(s, file, 'M-P04', old, new)
old = para(s, '左式将任意实数得分转为零与一之间的概率。')
new = old.replace('$\\bm{w}^{\\top}\\bm{x}+b=0$，在二维平面中就是一条直线。', '$\\bm{w}^{\\top}\\bm{x}+b=0$。当$\\bm w\\ne\\bm0$时，这个方程在二维平面中给出一条直线；若$\\bm w=\\bm0$，概率不随输入变化，就不存在这样的直线分界。')
s = change(s, file, 'M-P05', old, new)
start = s.index('有限类别的概率分布可以逐项比较。')
old = s[start:s.index(r'\begin{equation}', start)]
new = old.replace(r'正式定义及条件见\BookSectionRef{sec:information-log-score-kl}{第一卷“信息论与统计几何”章的“对数评分与KL散度”一节}和\BookSectionRef{sec:statistics-scoring-calibration}{第一卷“随机变量”章的“评分与校准”一节}，这里说明它们怎样接入模型。', '')
s = change(s, file, 'M-P06', old, new)
old = para(s, '已知样本类别为$c$时')
new = r'其中$p_j=0$的项约定为零，$p_j>0$而$q_j=0$时取无穷大。' + old + r'（可参考\BookSectionRef{sec:information-log-score-kl}{第一卷“概率分布”章的“对数评分的差异”}和\BookSectionRef{sec:statistics-scoring-calibration}{第一卷“随机变量”章的“预测分布的计算与评价”}。）'
# Keep the reference within the preceding final sentence's punctuation.
new = new.replace('本节使用自然对数。（可参考', '本节使用自然对数（可参考').replace('”}。）', '”}）。')
s = change(s, file, 'M-P07', old, new)
old = para(s, '其中$p_j=0$的项约定为零，$p_j>0$而$q_j=0$时取无穷大。散度非负')
new = old.replace('其中$p_j=0$的项约定为零，$p_j>0$而$q_j=0$时取无穷大。', 'KL散度也沿用前面的零质量与零预测概率约定。')
s = change(s, file, 'M-P08', old, new)
old = para(s, '按这个求和定义，评分在$0$到$2$之间。')
new = old.replace('按这个求和定义，评分在$0$到$2$之间。', r'按这个求和定义，评分在$0$到$2$之间。二分类若只用正类概率$q\in[0,1]$和标签$y\in\{0,1\}$计分，常写为$(q-y)^2$；上式同时计算两个类别的偏差，等于这个单项评分的两倍。')
s = change(s, file, 'M-P09', old, new)
old = para(s, '它鼓励模型对已观测样本给出较大的概率或密度')
new = old.replace('且$P\\ll Q_{\\bm\\theta}$、有关对数期望存在', '且$P\\ll Q_{\\bm\\theta}$、真实密度的对数在$P$下可积、模型负对数密度的期望有定义').replace('模型失配时只能得到类内最优近似；', '模型失配时，即使求得类内最优解，它也只能近似真实分布；')
s = change(s, file, 'M-P10', old, new)
(draft / file).parent.mkdir(parents=True, exist_ok=True)
(draft / file).write_text(s)
model_diff = ''.join(difflib.unified_diff(original.splitlines(True), s.splitlines(True), fromfile='a/'+file, tofile='b/'+file))

file = 'tex/02-foundations/01-basics/03-machine-learning-paradigms.tex'
original = (snapshot / file).read_text()
s = original
old = para(s, '建立基准时，我们先固定任务与单个智能体')
new = old.replace('按第一卷有限时域口径，', '在有限时域中，').replace('给定当前状态与动作后，', '在固定时刻，给定当前状态与动作后，') + r'（可参考\BookSectionRef{sec:policy-induced-trajectories}{第一卷“策略的价值与优化”章的“策略诱导的轨迹”}。）'
new = new.replace('不属于MDP元组本身。（可参考', '不属于MDP元组本身（可参考').replace('”}。）', '”}）。')
s = change(s, file, 'R-P01', old, new)
old = para(s, '策略、轨迹、折扣及长期平均回报已在')
new = r'''一条交互轨迹记录状态、动作及其后果。将阶段奖励与终点奖励相加，得到这次执行的累计回报；策略的期望回报则按策略与环境产生各轨迹的概率取平均。这里以奖励越大越好；若改以成本评价，令奖励等于成本的负值，并将最大化与最小化成套转换（可参考\BookSectionRef{sec:policy-trajectory-return}{第一卷“策略的价值与优化”章的“轨迹收益与策略价值”}）。辨认范式时，我们检查策略与环境怎样产生轨迹，训练怎样使用过程或终点奖励，而不只看模型是否连续输出动作。\term{折扣因子}（discount factor）改变不同时间奖励的权重，长期平均回报则比较单位时间的收益。使用这些准则时，应限定时域、平均方式和所需可积条件，并按任务加入风险要求\scite{sutton2018}。'''
s = change(s, file, 'R-P02', old, new)
(draft / file).parent.mkdir(parents=True, exist_ok=True)
(draft / file).write_text(s)
paradigm_diff = ''.join(difflib.unified_diff(original.splitlines(True), s.splitlines(True), fromfile='a/'+file, tofile='b/'+file))

(base / 'proposals' / 'basics-cross-volume.patch').write_text(model_diff + paradigm_diff)
(base / 'proposals' / 'units.json').write_text(json.dumps(units, ensure_ascii=False, indent=2) + '\n')
hashes={str(p.relative_to(draft)): hashlib.sha256(p.read_bytes()).hexdigest() for p in draft.rglob('*.tex')}
(base / 'proposals' / 'draft-manifest.json').write_text(json.dumps(hashes, ensure_ascii=False, indent=2)+'\n')
print('Proposal units:', len(units), '; hashes:', hashes)
