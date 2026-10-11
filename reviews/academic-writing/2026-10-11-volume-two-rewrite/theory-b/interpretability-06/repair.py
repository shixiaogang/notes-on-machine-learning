from pathlib import Path
import json,hashlib,re
D=Path('reviews/academic-writing/2026-10-11-volume-two-rewrite/theory-b/interpretability-06')
u=json.loads((D/'v0-units.json').read_text())
f=Path(u['file']); t=f.read_text(); assert hashlib.sha256(f.read_bytes()).hexdigest()==u['sha256']
p={b['id'][4:]:b['text'] for b in u['blocks']}
rep={
'P075':r'为了单独看清输入距离，图~\ref{fig:trust-counterfactual-nearest}改用示例~\ref{ex:interpretability-causal-recourse}中的连续申请场景。这里$s$为技能分数，$r$为当期资源，申请在$s+r\geq3$时批准。当前$(1,1)$到批准区域的欧氏最近点为$(1.5,1.5)$，这里只比较输入距离，尚未计算培训和支持的后果及成本。',
'P105':p['P105'].replace('干净与受损运行在同层同位置交换激活后继续前向','将干净运行的激活复制到受损运行的同层同位置后继续前向'),
'P111':p['P111'].replace(r'其中$\hat{\bm\theta}$是局部最优解，$\bm H$可逆。',r'其中$\hat{\bm\theta}$是局部最优解，$\bm H$可逆，且各损失在当前解的邻域内二阶连续可微。'),
'P165':'在上述培训上限为1的条件下，'+p['P165'],
'P029':p['P029'].replace('教学规则可由',r'示例~\ref{ex:interpretability-global-local}的教学规则可由'),
'P035':p['P035'].replace('教学规则的四种组合',r'示例~\ref{ex:interpretability-global-local}的四种组合'),
'P073':r'沿用示例~\ref{ex:interpretability-global-local}，'+p['P073'],
'P082':p['P082'].replace('教学加性规则',r'示例~\ref{ex:interpretability-global-local}的加性规则'),
'P090':p['P090'].replace('教学规则从',r'示例~\ref{ex:interpretability-global-local}的规则从'),
'P139':p['P139'].replace('教学规则中',r'在示例~\ref{ex:interpretability-global-local}的规则中'),
'P175':r'在示例~\ref{ex:interpretability-causal-recourse}中，'+p['P175'],
'P080':p['P080'].replace('窄权重关注当前邻域但减少可识别变化，宽权重则可能超出简单模型的拟合能力。','把较大权重集中在较窄邻域，能突出当前输入，却减少可识别的变化；扩大高权重邻域，则可能超出简单模型的拟合能力。')
}
for k,v in rep.items():
 assert t.count(p[k])==1,k
 t=t.replace(p[k],v)
f.write_text(t)
(D/'snapshots/v1').mkdir(exist_ok=True)
(D/'snapshots/v1'/f.name).write_bytes(f.read_bytes())
bb=[]
for i,m in enumerate(re.finditer(r'\S(?:.*?\S)?(?=\n\s*\n|\Z)',t.rstrip(),re.S),1):
 text=m.group();ss=[]
 for s in re.findall(r'[^。！？]*[。！？]|[^。！？]+$',text):
  if re.search('[一-龥]',s):ss.append({'id':f'I06-P{i:03d}-S{len(ss)+1:02d}','text':s.strip()})
 bb.append({'id':f'I06-P{i:03d}','line':t[:m.start()].count('\n')+1,'text':text,'sentences':ss})
assert len(bb)==len(u['blocks'])
v={'file':str(f),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'blocks':bb,'source':'theory_second_half repairs after independent review'}
(D/'v1-units.json').write_text(json.dumps(v,ensure_ascii=False,indent=2))
print('v1',v['sha256'],'changed',','.join(rep),'P',len(bb),'S',sum(len(b['sentences']) for b in bb))
