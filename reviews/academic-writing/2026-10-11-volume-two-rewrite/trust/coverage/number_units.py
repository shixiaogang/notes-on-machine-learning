import re,json
from pathlib import Path
r=Path(__file__).resolve().parent.parent
pat=r'\\begin\{(equation\*?|align\*?)\}.*?\\end\{\1\}|\\\[.*?\\\]'
def arg(t,key):
 q=t.find(key)
 if q<0:return ''
 a=q+len(key);j=a;d=1
 while d:
  d+=(t[j]=='{')-(t[j]=='}');j+=1
 return t[a:j-1]
for p in sorted((r/'snapshots/review-input').glob('*.tex')):
 units=[]
 for i,b in enumerate(re.split(r'\n\s*\n',p.read_text()),1):
  uid=f'P{i:03}';formula=[m.group() for m in re.finditer(pat,b,re.S)]
  if '\\caption{' in b:t=arg(b,'\\caption{')
  else:
   t=re.sub(pat,'[显示公式]',b,flags=re.S)
   t=re.sub(r'\\(?:chapter|section|subsection|paragraph|label|Needspace|BookSectionRef|includegraphics)\{[^}]*\}','',t)
   t=re.sub(r'\\(?:begin|end)\{[^}]*\}(?:\[[^]]*\])?','',t)
   t=re.sub(r'\\(?:phantomsection|centering|item)\b','',t)
   t=re.sub(r'(?m)^[ \t]*%[^\n]*(?:\n|$)','',t)
  t=re.sub(r'\s+',' ',t).strip();ss=[s.strip() for s in re.split(r'(?<=[。？！])',t) if s.strip()]
  units.append({'id':uid,'source':b,'sentences':[{ 'id':f'{uid}.S{j:02}','text':s} for j,s in enumerate(ss,1)],'formulas':[{ 'id':f'{uid}.F{j:02}','tex':s} for j,s in enumerate(formula,1)]})
 (r/'coverage'/f'{p.stem}-units.json').write_text(json.dumps(units,ensure_ascii=False,indent=2))
 with (r/'coverage'/f'{p.stem}-numbered.md').open('w') as f:
  for u in units:
   if u['sentences'] or u['formulas']:
    f.write(f"\n## {u['id']}\n")
    for s in u['sentences']:f.write(f"{s['id']} {s['text']}\n")
    for s in u['formulas']:f.write(f"{s['id']} {s['tex']}\n")
