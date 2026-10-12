from pathlib import Path
import json,re,hashlib
r=Path(__file__).parent;b=[x['text'] for x in json.loads((r/'02-v1-blocks.json').read_text())]
b[10]=b[10].replace('可实现性使ERM几乎必然与样本一致。','题设保证输出几乎必然与样本一致；可实现性也使这样的选解存在。')
b[15]=b[15].replace('这样，即使ERM看过数据再选，经验风险也不会把高风险者误当低风险者。','即使ERM看过数据再选，输出与参照的两次偏差比较仍能控制其超额期望风险。')
b[147]=b[147].replace('便以至少$1-\\delta$的概率同时得到','便以至少$1-\\delta$的概率对所有$f\\in\\operatorname{conv}(\\mathcal B)$同时得到')
b[75]=b[75].replace('只缩放参数而不改分类符号，间隔通常也缩小','只缩小参数而不改分类符号，得分间隔也相应缩小')
b[73]=b[73].replace('改变$a$的得分至多改变$L|a|$损失','得分改变$a$时，损失至多改变$L|a|$')
b[72]=b[72].replace('取$g=g_h$后，定理分别给出总体风险与经验风险，另外两项是替换平均所需的复杂度及抽样代价。','取$g=g_h$后，左侧是总体风险，右侧首项是经验风险，另外两项补偿由样本均值推断总体均值的复杂度与抽样代价。')
b[110]=r'''单个分类器会出错，将多个分类器的回答结合起来能否减少总体错误？重复训练时，平均得分能否减小训练随机性造成的方差？投票或平均多个假设构成\term{集成学习}（ensemble learning）。组合可能减少得分波动，也可能表达单个假设不具备的边界；这些作用采用不同指标，不能由假设更多直接推出分类错误更少。'''
b[131]=b[131].replace('在$m$个有序输入上只有$m+1$种预测','在$m$个互异且有序的输入上恰有$m+1$种预测')
b[139]=b[139].replace('所有轮次有优势的概率便至少','全部实际调用轮次都取得优势的概率便至少')
b[55]=b[55].replace('若VC维有限，Sauer--Shelah引理限制合并样本上的不同预测数；对称化把这种计数变成\n式~\\eqref{eq:vc-uniform-bound}的一致收敛界。在一致收敛事件上，ERM输出与任意比较\n假设的经验风险之差不大于零，而两者的经验风险与期望风险各相差至多$\\eta$，因此输出\n假设的期望风险至多比$\\inf_{h\\in\\mathcal H}R_{\\mathcal P}(h)$高$2\\eta$。令$\\eta=\\varepsilon/2$，\n便得到不可知PAC可学习；不可知保证覆盖可实现分布，因而也推出可实现PAC可学习。','有限VC维先经Sauer--Shelah限制合并样本的预测数，再由对称化得到式~\\eqref{eq:vc-uniform-bound}，所以推出一致收敛。固定一致收敛成功事件，ERM的经验风险不超过任意参照；将输出和参照各用一个$\\eta$连接到总体风险，得超额风险至多$2\\eta$。取$\\eta=\\varepsilon/2$便得到不可知PAC；它覆盖可实现来源，也给出可实现PAC。')
f=Path('tex/03-foundations/02-learning-theory/02-binary-classification.tex');f.write_text('\n\n'.join(s.rstrip() for s in b))
(r/'02-v2.tex').write_text(f.read_text());(r/'02-v2-blocks.json').write_text(json.dumps([{'id':f'02-P{i+1:03}','text':s.rstrip()} for i,s in enumerate(b)],ensure_ascii=False,indent=2))
print('v2 sha',hashlib.sha256(f.read_bytes()).hexdigest())
for lo,hi in [(7,17),(54,60),(69,79),(109,119),(130,151)]:
 print('\nCONTINUOUS',lo,hi)
 for i in range(lo-1,hi):
  if not b[i].startswith(('\\begin{theorem}','\\begin{definition}')):print(f'P{i+1:03}',re.sub(r'\\begin\{(equation\*?|align\*?)\}[\s\S]*?\\end\{\1\}|\\\[[\s\S]*?\\\]','[公式原样]',b[i]))
