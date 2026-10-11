# Only numbers, validates and renders manually authored semantic records. It does not infer meaning or acceptance.
from pathlib import Path
import json,re
D=Path('reviews/academic-writing/2026-10-11-volume-two-rewrite/theory-b/interpretability-06')
def read_tsv(n):
 rows={}
 for s in (D/n).read_text().splitlines():
  k,v=s.split('\t',1);assert k not in rows,k;rows[k]=v
 return rows
means=read_tsv('sentence-meanings.tsv');meta=read_tsv('metadata-review.tsv');gates=read_tsv('gate-map.tsv');over=read_tsv('final-overrides.tsv')
assert set(means)==set(gates)
for ver in ['v0','v1']:
 u=json.loads((D/(ver+'-units.json')).read_text());items=[];n=0
 intro=f'''# INT-W{1 if ver=='v0' else 2}：逐句与特殊单元记录

2026-10-11，theory_second_half。{'冻结稿独立代理复核（未参与初稿改写）' if ver=='v0' else '修订稿自查（原独立判断对未变单元继承，12个改段已重新逐句与上下文复读）'}。受审正文SHA256 `{u['sha256']}`；可恢复正文位于snapshots/{ver}/06-interpretability.tex。P号按空行自然块固定，句号只作索引，标题单独标为元数据；{len(u['blocks'])}个P。公式、例子、图注包含在实际相应S中，正文中的数学量与推理已实际读过，不能当作免审格式。

下面每一S的实际意思及方括号依据由审查者手写，脚本只取短引、编号、检验覆盖并排版。关注门槛列列出本段实际检查的G/W；不是每句都触发每个门槛，具体触发对象与接受理由以本句义和INT-K1为准。E1—E12在key-units-and-calibration.md逐项列位置；G1可检验、G2压缩拆解、G3对象转换、G4解释时序、G5局部入口、G6公式双门槛、G7回指范围。每句均已检查语序、主干、词义、符号、限定和必要性，只有需说明的具体依据展开。

|句号与位置|位置短引|实际意思与具体依据或发现|关注门槛|
|---|---|---|---|
'''
 for b in u['blocks']:
  p=b['id'][4:]
  if p in meta:
   row=[meta[p]];gate='元数据、标题层级、导航身份'
  else:
   v=over[p] if ver=='v1' and p in over else means[p]
   row=v.split(' | ');gate=gates[p]
  assert len(row)==len(b['sentences']),(ver,p,len(row),len(b['sentences']))
  for s,m in zip(b['sentences'],row):
   quote=s['text'].replace('\n',' ')
   # remove only leading pure formatting so short quote locates the actual prose when possible
   quote=re.sub(r'^\\begin\{[^}]+\}(?:\[[^]]*\])?\s*(?:\\label\{[^}]+\}\s*)?','',quote)
   if len(quote)>68:quote=quote[:68]+'…'
   esc=lambda v:v.replace('|','\\|').replace('\n',' ')
   items.append(f"|{s['id']}（L{b['line']}）|{esc(quote)}|{esc(m)}|{esc(gate)}|");n+=1
 (D/f'pass3-sentences-{ver}.md').write_text(intro+'\n'.join(items)+f'\n\n覆盖核对：{len(u["blocks"])} P，{n} S，含{len(meta)}个标题等元数据S；无漏号。特殊公式与例子另见INT-K1。\n')
print('rendered v0/v1; all manually supplied sentence meanings matched')
