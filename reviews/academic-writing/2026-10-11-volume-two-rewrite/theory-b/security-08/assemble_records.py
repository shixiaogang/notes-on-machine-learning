# Formats manually authored judgements. Never derives sentence meanings.
import re,json,hashlib
from pathlib import Path
b=Path(__file__).parent

def read(n):
 d={}
 for x in (b/n).read_text().splitlines():
  k,v=x.split('\t',1);assert k not in d;k0=k;d[k0]=v
 return d
base=read('sentence-meanings.tsv');meta=read('metadata-review.tsv');para=read('pass2-paragraphs.tsv')
assert len(para)==180 and len(base)+len(meta)==180 and not set(base)&set(meta)
for version in ['v1','v2']:
 u=json.loads((b/f'{version}-units.json').read_text());o=dict(base)
 if version=='v2':o.update(read('final-overrides.tsv'))
 lines=[f'# SEC-W{1 if version=="v1" else 2}：逐句与特殊单元自查（{version}）','',f'2026-10-11，AI作者自查；正文SHA256 `{u["sha256"]}`，完整可恢复正文见snapshots/{version}/{Path(u["file"]).name}。', '',
 '句子实际意思与接受依据由审查者手写于sentence-meanings.tsv，修订后的受影响判断为final-overrides.tsv；脚本只复制并补定位/短引。标题作为元数据检查，图注、程序、例子和公式所在句均逐条列入。v1发现需结合修订记录读取，v2为最终闭环。', '',
 'W1主干与指代，W2词义及关系，W3术语符号，W4逻辑条件，W5技术证据，W6逐词必要性；G1可检验命题，G2压缩表达，G3对象转换，G4解释时序，G5局部入口，G6公式双门槛，G7回指范围。每句括号给具体判断，不用统一通过标记。', '']
 for p in u['blocks']:
  k=p['id'];lines +=[f'## {k}（源第{p["line"]}行）','']
  if k in o:
   mm=o[k].split('|');assert len(mm)==len(p['sentences']),(k,len(mm),len(p['sentences']))
   for s,m in zip(p['sentences'],mm):
    anchor=' '.join(s['text'].split())[:100]
    lines +=[f'- **{s["id"]}**：`{anchor}`。实际意思与依据：{m}。']
  else:
   assert k in meta
   lines +=[f'覆盖元数据句号：{p["sentences"][0]["id"]}。`'+p['text'].split('\n')[0]+'`。职责判断：'+meta[k]]
  lines+=['']
 (b/f'pass3-sentences-{version}.md').write_text('\n'.join(lines)+'\n')
manifest={v:{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (b/'snapshots'/v).glob('*.tex')} for v in ['v0','v1','v2']}
(b/'snapshot-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
a=(b/'snapshots/v0/08-adversarial-security.tex').read_text();z=(b/'snapshots/v2/08-adversarial-security.tex').read_text()
patterns={'展示公式':r'\\begin\{equation\}.*?\\end\{equation\}|\\\[.*?\\\]','标题':r'\\(?:chapter|section|subsection|paragraph)\{[^}]*\}','引文':r'\\scite\{[^}]*\}','标签':r'\\label\{[^}]*\}'}
lines=['# 源码保全静态核验','', '2026-10-11；脚本只比表达和计数，不生成语义判断。','', '|项|基线数量|最终数量|逐序一致|','|---|---|---|---|']
for k,p in patterns.items():
 x=re.findall(p,a,re.S);y=re.findall(p,z,re.S);assert x==y,k;lines+=[f'|{k}|{len(x)}|{len(y)}|是|']
p=r'(?<!\$)\$(?!\$).*?(?<!\$)\$(?!\$)';xx={re.sub(r'\s+','',q) for q in re.findall(p,a,re.S)};yy={re.sub(r'\s+','',q) for q in re.findall(p,z,re.S)};assert not xx-yy,xx-yy
u0=json.loads((b/'v0-units.json').read_text());u2=json.loads((b/'v2-units.json').read_text());changed=sum(p['text']!=q['text'] for p,q in zip(u0['blocks'],u2['blocks']));assert len(u0['blocks'])==len(u2['blocks'])==180
lines+=['',f'修改{changed}/180个段/特殊单元。最终531个中文句与标题片段，标题34项另作职责判断。所有原行内数学表达均在最终稿保留（忽略空白比较），新增$i$、$k$等只明确原含义。展示公式逐字不变。','', '未构建，未进行图片像素或PDF验收；由主集成代理构建七版。']
(b/'verification.md').write_text('\n'.join(lines)+'\n');print('hand-record coverage checked',changed,'final sha',u2['sha256'])
