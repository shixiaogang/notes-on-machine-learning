from pathlib import Path
import hashlib,json,re,subprocess,unicodedata,shutil
import pymupdf as fitz
from PIL import Image,ImageChops

B=Path(__file__).parent;R=B.parent.parent;ROOT=R.parent/'volume-two-figures';OLD=B.parent/'final-root-page-review';I=B/'inputs-r4'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
norm=lambda s:re.sub(r'\s+','',unicodedata.normalize('NFKC',s))
prior=json.loads((OLD/'page-binding.json').read_text());oldtext=json.loads((OLD/'text-page-binding.json').read_text());edits=json.loads((OLD/'followup-old-new.json').read_text())
expected={'vol2-foundations':'94ca9126cd7f19bde8dd24827ae8dd70df43ec7b258be5618c864a3344497bbe','machine-learning-notes':'d5ee494d27df547b41b7e02d287ba5489f069975279b45b2c34ad3455f42a1ab'}
I.mkdir(parents=True,exist_ok=True)
m={'stage':'root final r4','date':'2026-10-12','role':prior['role'],'root_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'pdfs':{},'figures':[],'text_pages':[],'six_chapters_exact_expected_diff':[]}
for owner in sorted({f['owner'] for f in prior['figures']}):
 p=ROOT/owner;old=(OLD/'inputs-r3'/owner).read_text();want=old
 for e in edits:
  if Path(owner).name==e['source_name']:
   assert want.count(e['old'])==1,(e['id'],want.count(e['old']));want=want.replace(e['old'],e['new'])
 assert p.read_text()==want,owner
 out=I/owner;out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,out)
 m['six_chapters_exact_expected_diff'].append({'owner':owner,'r3_sha256':sha(OLD/'inputs-r3'/owner),'r4_sha256':sha(p),'matches_only_six_declared_edits':True})
for rel in ['tex/styles/references.tex']:
 assert (ROOT/rel).read_bytes()==(OLD/'inputs-r3'/rel).read_bytes();out=I/rel;out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/rel,out)
shutil.copy2(ROOT/'target/.build-manifest.json',I/'build-manifest.json')

def render(pdf,page,out,gray=False):
 out.parent.mkdir(parents=True,exist_ok=True)
 assert not out.exists(),f'new r4 proof required: {out}'
 cmd=['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','1600']
 if gray:cmd+=['-gray']
 subprocess.run(cmd+['-png',str(pdf),str(out.with_suffix(''))],check=True,capture_output=True)

def compare(new,old):
 a=Image.open(new).convert('RGB');b=Image.open(old).convert('RGB')
 eq=a.size==b.size and ImageChops.difference(a,b).getbbox() is None
 return {'r3_proof_sha256':sha(old),'r4_proof_sha256':sha(new),'png_byte_identical':new.read_bytes()==old.read_bytes(),'pixel_identical':eq,'dimensions_px':list(a.size)}

docs={}
for edition,aux in [('vol2-foundations','02-foundations'),('machine-learning-notes','main')]:
 original=ROOT/'target'/f'{edition}.pdf';assert sha(original)==expected[edition];pdf=I/original.name;shutil.copy2(original,pdf)
 doc=fitz.open(pdf);docs[edition]=doc;auxt=(ROOT/'build'/f'{aux}.aux').read_text();labels={doc[i].get_label():i+1 for i in range(len(doc))}
 m['pdfs'][edition]={'original_path':str(original),'snapshot_pdf':str(pdf.relative_to(B)),'sha256':sha(pdf),'pages':len(doc),'aux_sha256':sha(ROOT/'build'/f'{aux}.aux'),'page_labels':doc.get_page_labels()}
 for f in prior['figures']:
  if edition not in f['editions']:continue
  found=re.findall(r'\\newlabel\{'+re.escape(f['label'])+r'\}\{\{([^}]+)\}\{([^}]+)\}',auxt);assert len(found)==1,(f['label'],found);number,printed=found[0];page=labels[printed]
  out=B/'pages'/edition/f'page-{page:04d}-{f["label"].replace(":","-")}.png';render(pdf,page,out)
  if edition=='vol2-foundations':
   owner=ROOT/f['owner'];source=owner.read_text();idx=source.index('\\label{'+f['label']+'}');start=source.rfind('\\begin{figure',0,idx);end=source.index('\\end{figure',start)
   row={'label':f['label'],'owner':f['owner'],'source_sha256_r4':sha(owner),'source_figure_block_r4':source[start:end],'assets':f['assets'],'editions':{}}
   for a in row['assets']:
    assert sha(ROOT/a['path'])==a['sha256'];assert all(sha(ROOT/q)==s for q,s in a['source_files_sha256'].items())
   m['figures'].append(row)
  else:row=next(x for x in m['figures'] if x['label']==f['label'])
  cmp=compare(out,OLD/f['editions'][edition]['proof_png'])
  row['editions'][edition]={'figure_number':number,'printed_page':printed,'physical_page':page,'pdf_sha256':sha(pdf),'proof_png':str(out.relative_to(B)),'proof_sha256':sha(out),'comparison_to_r3':cmp,'page_text':doc[page-1].get_text(),'review_status':'comparison prepared; pixel-different pages await actual visual review'}
  if edition=='vol2-foundations' and 'gray' in f:
   out=B/'gray'/out.name;render(pdf,page,out,True);row['gray']={'physical_page':page,'pdf_sha256':sha(pdf),'proof_png':str(out.relative_to(B)),'proof_sha256':sha(out),'comparison_to_r3':compare(out,OLD/f['gray']['proof_png']),'review_status':'comparison prepared'}

doc=docs['vol2-foundations'];pdf=I/'vol2-foundations.pdf'
for x in oldtext:
 matches=[i for i,p in enumerate(doc) if norm(x['query']) in norm(p.get_text())]
 if x['id']=='OV-G1325':matches=[i for i in matches if '平均经验优化误差' in norm(doc[i].get_text()) and '条件互信息' in norm(doc[i].get_text())]
 assert len(matches)==1,(x['id'],matches);i=matches[0];p=doc[i]
 out=B/'text-pages'/f'page-{i+1:04d}-{x["id"]}.png';render(pdf,i+1,out)
 src=I/'tex/02-foundations/02-learning-theory'/x['source_name'];lines=src.read_text().splitlines();span=x['source_line_range']
 m['text_pages'].append({'id':x['id'],'source_name':x['source_name'],'source_sha256_r4':sha(src),'source_line_range':span,'source_text_r4':'\n'.join(lines[span[0]-1:span[1]]),'reported_overfull_r3_pt':x['reported_overfull_pt'],'physical_page':i+1,'printed_page':p.get_label(),'pdf_sha256':sha(pdf),'proof_png':str(out.relative_to(B)),'proof_sha256':sha(out),'comparison_to_r3':compare(out,OLD/x['proof_png']),'page_text':p.get_text(),'review_status':'comparison prepared; changed page or six repaired paragraphs await actual review'})
(B/'r4-binding.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
(B/'inputs-r4-sha.json').write_text(json.dumps({str(p.relative_to(I)):sha(p) for p in sorted(I.rglob('*')) if p.is_file()},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'pdfs':m['pdfs'],'figure_pages':[{'label':f['label'],'views':{e:{'page':v['physical_page'],'identical':v['comparison_to_r3']['pixel_identical']} for e,v in f['editions'].items()},'gray_identical':f.get('gray',{}).get('comparison_to_r3',{}).get('pixel_identical')} for f in m['figures']],'text_pages':[{'id':x['id'],'page':x['physical_page'],'identical':x['comparison_to_r3']['pixel_identical']} for x in m['text_pages']]},ensure_ascii=False,indent=2))
