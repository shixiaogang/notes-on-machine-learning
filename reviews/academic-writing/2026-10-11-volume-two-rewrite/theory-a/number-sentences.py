from pathlib import Path
import json,re
r=Path(__file__).parent
for n in ['02','03']:
 f=r/(n+'-v1-blocks.json')
 if not f.exists():continue
 out=[]
 for x in json.loads(f.read_text()):
  t=x['text']
  t=re.sub(r'\\begin\{(equation\*?|align\*?)\}[\s\S]*?\\end\{\1\}|\\\[[\s\S]*?\\\]','[公式]',t)
  t=re.sub(r'\\(?:chapter|section|subsection|subsubsection|paragraph|label|includegraphics|BookChapterRef|BookSectionRef)\{[^}]*\}', '',t)
  t=re.sub(r'\\(?:begin|end)\{[^}]*\}(?:\[[^]]*\])?', '',t)
  t=re.sub(r'\\centering|\\item','',t)
  t=re.sub(r'\s+',' ',t).strip()
  s=[z.strip() for z in re.findall(r'[^。？！]*[。？！]|[^。？！]+$',t) if re.search(r'[\u4e00-\u9fff]',z)]
  if s:out.append({'id':x['id'],'sentences':[{'id':f"{x['id']}-S{i+1:02}",'text':z} for i,z in enumerate(s)]})
 (r/(n+'-sentences-v1.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2))
 (r/(n+'-sentences-v1.txt')).write_text('\n'.join(s['id']+' '+s['text'] for p in out for s in p['sentences']))
 print(n,len(out),sum(len(x['sentences']) for x in out))
