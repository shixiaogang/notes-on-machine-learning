"""Scan every page for margin text collisions; candidates require visual triage."""
import fitz,json,sys,hashlib
from pathlib import Path
source=Path(sys.argv[1] if len(sys.argv)>1 else 'target/vol3-foundations.pdf')
pdf=fitz.open(source);out=[];paint=[]
for p in pdf:
 notes=[t for t in p.get_texttrace() if 407<t['bbox'][0]<410 and t['bbox'][1]>60]
 hits=[]
 for typ,box in p.get_bboxlog():
  r=fitz.Rect(box)
  if typ not in ('fill-image','fill-path') or r.width<200 or r.height<80 or r.x1<420:continue
  for t in notes:
   z=r&fitz.Rect(t['bbox'])
   if z.width>10 and z.height>3:
    hits.append(dict(kind=typ,rectangle=list(r),text=''.join(chr(c[0]) for c in t['chars'])))
 if hits:paint.append(dict(page=p.get_label(),pdf_page=p.number+1,hits=hits))
 lines=[]
 for bi,b in enumerate(p.get_text('dict')['blocks']):
  if b['type']!=0:continue
  for li,l in enumerate(b['lines']):
   txt=''.join(s['text'] for s in l['spans']);r=fitz.Rect(l['bbox'])
   if r.y0<60:continue
   lines.append((bi,li,r,txt))
 # Separate independently extracted text lines whose occupied rectangles overlap in margin.
 collisions=[]
 for i,(bi,li,r,t) in enumerate(lines):
  if r.x1<405:continue
  for bj,lj,s,u in lines[i+1:]:
   if bi==bj or s.x1<405:continue
   z=r&s
   if z.width>3 and z.height>2 and z.x1>405:
    collisions.append({'a':t,'b':u,'rect':list(z)})
 if collisions:out.append({'page':p.get_label(),'pdf_page':p.number+1,'collisions':collisions})
report=Path(sys.argv[2] if len(sys.argv)>2 else 'build/reader-layout/caption-margin-review/current-scan.json')
report.write_text(json.dumps(dict(pdf=str(source),sha256=hashlib.sha256(source.read_bytes()).hexdigest(),pages=len(pdf),text_candidates=out,graphic_candidates=paint),ensure_ascii=False,indent=2)+'\n')
for r in out:
 print(r['page'],r['pdf_page'],len(r['collisions']),[(c['a'][:22],c['b'][:22]) for c in r['collisions'][:3]])
print('pages',len(pdf),'candidates',len(out))
print('graphic candidates',len(paint))
