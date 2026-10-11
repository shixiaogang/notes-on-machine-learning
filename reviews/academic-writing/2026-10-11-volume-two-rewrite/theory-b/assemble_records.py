# Only formats hand-authored judgments and verifies IDs/counts. No semantic inference.
import json, hashlib
from pathlib import Path
b=Path(__file__).parent
v1=json.loads((b/'v1-units.json').read_text()); v2=json.loads((b/'v2-units.json').read_text())
def read(name):
 d={}
 for line in (b/name).read_text().splitlines():
  k,x=line.split('\t',1)
  assert k not in d,k
  d[k]=x
 return d
ordinary=read('sentence-meanings.tsv');special=read('special-review.tsv')
assert not set(ordinary)&set(special)
assert len(ordinary)+len(special)==579
for version,units in [('v1',v1),('v2',v2)]:
 o=dict(ordinary);s=dict(special)
 if version=='v2':
  o.update(read('final-overrides.tsv'));s.update(read('final-special-overrides.tsv'))
 lines=[f'# TB-W{1 if version=="v1" else 2}：逐句自查及特殊单元（{version}）','',
 '2026-10-11，AI 作者自查。实际意思与判断依据均来自手写 TSV；本文件仅排版这些既有判断。全文按章、段、句的顺序阅读后记录。普通句逐条；形式命题与其证明因共同完成一项推导合并，明确列出其覆盖句号。标题只检查结构职责，不计作论证句；无中文的纯闭合命令不编造句意。', '',
 '检查含义：W1 当前论点，W2 局部关系，W3 符号与术语，W4 量词与条件，W5 运算与证据，W6 字面准确；G1—G7 另核可检验命题、压缩表达拆解、新对象转换、解释时序、局部入口、公式双门槛及回指范围。每句括号内写出接受或转修依据，不以关键词扫描代替审读。v1 的待修项须结合 TB-R2 读；v2 为修订复读后的最终结论。', '']
 count=0
 for fname,d in units.items():
  source=b/'snapshots'/version/fname
  assert hashlib.sha256(source.read_bytes()).hexdigest()==d['sha256']
  lines += [f'## {fname}', '', f'SHA256 `{d["sha256"]}`。', '']
  for p in d['blocks']:
   pid=p['id'];count+=len(p['sentences'])
   lines += [f'### {pid}（源第 {p["line"]} 行）', '']
   if pid in o:
    meanings=o[pid].split('|');assert len(meanings)==len(p['sentences']),(version,pid,len(meanings),len(p['sentences']))
    for sentence,meaning in zip(p['sentences'],meanings):
     quote=' '.join(sentence['text'].split())
     lines += [f'- **{sentence["id"]}**，短引：`{quote[:100]}`。实际意思与依据：{meaning}。']
   else:
    assert pid in s,pid
    ids='、'.join(x['id'] for x in p['sentences']) or '无中文句：格式闭合单元'
    quote=' '.join(p['text'].split())
    lines += [f'覆盖：{ids}。短引：`{quote[:120]}`。', '', f'合并实际意思与判断依据：{s[pid]}。']
   lines+=['']
 (b/f'pass3-sentences-{version}.md').write_text('\n'.join(lines)+'\n')
 print(version,'P=579','S=',count)
manifest={}
for version in ['v0','v1','v2']:
 manifest[version]={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((b/'snapshots'/version).glob('*.tex'))}
(b/'snapshot-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
