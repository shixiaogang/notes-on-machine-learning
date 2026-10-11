from pathlib import Path
import re,json,hashlib,collections
r=Path(__file__).parent
orig=json.loads((r/'07-privacy-v0-blocks.json').read_text())
maps={}
for suffix in ['', '-b','-c','-d']:
 t=(r/f'07-privacy-rewrite{suffix}.txt').read_text()
 for m in re.finditer(r'^@@ (\d+)(-caption)?\n([\s\S]*?)(?=^@@ |\Z)',t,re.M):
  i=int(m[1]);assert i not in maps,i
  maps[i]=(bool(m[2]),m[3].strip().replace('因此須','因此须').replace('检查点加密会增加','检查点越密集会增加'))
math=re.compile(r'\\\[[\s\S]*?\\\]|\\begin\{(equation\*?|align\*?|gather\*?)\}[\s\S]*?\\end\{\1\}')
def caption_replace(s,t):
 pos=s.index('\\caption{')+len('\\caption{');level=1;j=pos
 while level:
  if s[j]=='{':level+=1
  elif s[j]=='}':level-=1
  j+=1
 return s[:pos]+t+s[j-1:]
blocks=[]
for p in orig:
 i=int(p['id'][-3:]);s=p['text']
 if i in maps:
  cap,t=maps[i]
  if cap:s=caption_replace(s,t)
  else:
   ms=[m[0] for m in math.finditer(s)]
   for j,x in enumerate(ms):
    assert t.count('{{M'+str(j)+'}}')==1,(i,j)
    t=t.replace('{{M'+str(j)+'}}',x)
   assert '{{M' not in t,i
   wrapper=re.match(r'(\\begin\{(definition|example)\}(?:\[[^]]*\])?\n\\label\{[^}]+\}\n)',s)
   if wrapper:t=wrapper[1]+t+'\n\\end{'+wrapper[2]+'}'
   s=t
 blocks.append({'id':p['id'],'text':s})
out='\n\n'.join(x['text'] for x in blocks)+'\n'
base=(r/'07-privacy-v0.tex').read_text()
for name,pat in [('labels',r'\\label\{[^}]+\}'),('heads',r'\\(?:chapter|section|subsection|subsubsection|paragraph)\{[^}]+\}'),('refs',r'\\(?:ref|eqref|Book\w*Ref)\{[^}]+\}'),('cites',r'\\(?:scite|cite\w*)\{[^}]+\}')]:
 a=collections.Counter(re.sub(r'\s+','',x) for x in re.findall(pat,base));b=collections.Counter(re.sub(r'\s+','',x) for x in re.findall(pat,out));print(name,sum(a.values()),a==b,a-b,b-a);assert a==b,name
assert [re.sub(r'\s+','',m[0]) for m in math.finditer(base)]==[re.sub(r'\s+','',m[0]) for m in math.finditer(out)]
f=Path('tex/02-foundations/03-trustworthiness/07-privacy.tex');f.write_text(out)
(r/'07-privacy-v1.tex').write_text(out);(r/'07-privacy-v1-blocks.json').write_text(json.dumps(blocks,ensure_ascii=False,indent=2))
print('rewrite blocks',len(maps),'all blocks',len(blocks),'hash',hashlib.sha256(out.encode()).hexdigest())
(r/'07-privacy-read-v1.txt').write_text('\n\n'.join(p['id']+'\n'+p['text'] for p in blocks))
