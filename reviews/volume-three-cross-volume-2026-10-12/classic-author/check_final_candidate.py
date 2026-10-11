from pathlib import Path
import json,re,hashlib,shutil,subprocess,difflib

base=Path(__file__).resolve().parent
old=base/'rebased-book-before'
new=base/'candidate-r4'
manifest=json.loads((base/'candidate-r4-manifest.json').read_text())
refpat=re.compile(r'\\(Book(?:Section|Chapter|Volume|Theorem|Equation)Ref)\{([^}]+)\}\{([^}]+)\}')
labels={}
for p in (base/'upstream-a9/tex').rglob('*.tex'):
    s=p.read_text()
    for m in re.finditer(r'\\label\{([^}]+)\}',s):
        labels.setdefault(m.group(1),[]).append({'file':str(p.relative_to(base/'upstream-a9')),'line':s[:m.start()].count('\n')+1})
refs=[]
checks=[]
for entry in manifest['entries']:
    rel=entry['file']
    a=(old/rel).read_text()
    z=(new/rel).read_text()
    for m in refpat.finditer(z):
        refs.append({'file':rel,'line':z[:m.start()].count('\n')+1,'macro':m.group(1),'key':m.group(2),'display':m.group(3),'targets':labels.get(m.group(2),[])})
    record={'file':rel}
    patterns={'headings':r'\\(?:chapter|section|subsection|subsubsection|paragraph)\*?\{[^\n]*','inputs':r'\\input\{[^}]+\}','citations':r'\\(?:scite|cite|parencite|textcite)\{[^}]+\}','figures':r'\\includegraphics(?:\[[^\]]*\])?\{[^}]+\}'}
    for key,pattern in patterns.items():
        record[key+'_equal']=re.findall(pattern,a)==re.findall(pattern,z)
    la=re.findall(r'\\label\{([^}]+)\}',a)
    lz=re.findall(r'\\label\{([^}]+)\}',z)
    record['labels_removed']=[x for x in la if x not in lz]
    record['labels_added']=[x for x in lz if x not in la]
    stack=[]
    errors=[]
    for kind,name in re.findall(r'\\(begin|end)\{([^}]+)\}',z):
        if kind=='begin':
            stack.append(name)
        elif not stack or stack.pop()!=name:
            errors.append(name)
    record['environment_balance_errors']=errors+stack
    checks.append(record)
(base/'reference-inventory-final.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n')
(base/'administrative-boundaries.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
scratch=base/'patch-application-check-r4'
shutil.copytree(old,scratch,dirs_exist_ok=True)
result=subprocess.run(['patch','-p1','--batch','--forward','-i',str(base/'classic-cross-volume-final.patch')],cwd=scratch,capture_output=True,text=True)
(base/'patch-application-check-r4.log').write_text(result.stdout+result.stderr)
assert result.returncode==0,result.stderr
matches=[]
for entry in manifest['entries']:
    if entry['modified']:
        rel=entry['file']
        matches.append({'file':rel,'matches_candidate':(scratch/rel).read_bytes()==(new/rel).read_bytes()})
assert all(x['matches_candidate'] for x in matches)
(base/'patch-application-check-r4.json').write_text(json.dumps({'returncode':result.returncode,'matches':matches},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'references':len(refs),'unique_targets':all(len(x['targets'])==1 for x in refs),'volume_two_refs':sum('第二卷' in x['display'] for x in refs),'boundaries_equal':all(all(v for k,v in x.items() if k.endswith('_equal')) for x in checks),'labels_removed':sum([x['labels_removed'] for x in checks],[]),'balanced':all(not x['environment_balance_errors'] for x in checks),'patch_reproduces_files':len(matches)},ensure_ascii=False))
