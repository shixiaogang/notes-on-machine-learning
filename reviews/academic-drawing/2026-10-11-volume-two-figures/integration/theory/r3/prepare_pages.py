from pathlib import Path
import hashlib,json,re,subprocess
import pymupdf as fitz
R=Path.cwd(); ROOT=R.parent/'volume-two-figures'; B=R/'build/final-root-page-review'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=json.loads((R/'reviews/academic-drawing/2026-10-11-volume-two-figures/theory/asset-manifest.json').read_text())
figs=old['figures']; assert len(figs)==25
representative={'fig:learning-two-randomness','fig:learning-research-problems-map','fig:learning-theory-ds-neighbors','fig:ntk-linearization-remainder','fig:learning-flat-sharp'}
# Representatives resolve by current asset name below; no old page numbers are reused.
rep_names={'learning-theory-two-randomness','learning-theory-map','learning-theory-ds-neighbors','learning-theory-ntk-linearization','learning-theory-flat-sharp'}
gray_names={'learning-theory-uniform-convergence','learning-theory-ds-neighbors','learning-theory-domain-classifier','learning-theory-flat-sharp'}
meta={'date':'2026-10-12','role':'AI自查；本组曾制作25图，当前实际根PDF重新目检','root_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'pdfs':{},'figures':[],'reading_status':'rendered_only_awaiting_actual_visual_review'}
for edition,aux in [('vol2-foundations','02-foundations'),('machine-learning-notes','main')]:
 pdf=ROOT/'target'/f'{edition}.pdf';doc=fitz.open(pdf);auxt=(ROOT/'build'/f'{aux}.aux').read_text();labels={doc[i].get_label():i+1 for i in range(len(doc))}
 meta['pdfs'][edition]={'path':str(pdf),'sha256':sha(pdf),'pages':len(doc),'page_labels':doc.get_page_labels(),'aux_sha256':sha(ROOT/'build'/f'{aux}.aux')}
 for f in figs:
  assets=f['assets'];names={Path(a['path']).parent.name for a in assets}
  if edition=='machine-learning-notes' and not (names&rep_names):continue
  found=re.findall(r'\\newlabel\{'+re.escape(f['label'])+r'\}\{\{([^}]+)\}\{([^}]+)\}',auxt);assert len(found)==1,(f['label'],found);number,printed=found[0];page=labels[printed]
  assert doc[page-1].get_label()==printed
  proof=B/'pages'/edition/f'page-{page:04d}-{f["label"].replace(":","-")}.png';proof.parent.mkdir(parents=True,exist_ok=True)
  if not proof.exists():subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','1600','-png',str(pdf),str(proof.with_suffix(''))],check=True,capture_output=True)
  if edition=='vol2-foundations':
   owner=ROOT/f['owner'];text=owner.read_text();assert text.count('\\label{'+f['label']+'}')==1
   source_start=text.rfind('\\begin{figure',0,text.index('\\label{'+f['label']+'}'));source_end=text.index('\\end{figure',source_start);block=text[source_start:source_end]
   row={'label':f['label'],'owner':f['owner'],'source_sha256':sha(owner),'source_figure_block':block,'assets':[],'editions':{}}
   for a in assets:
    p=ROOT/a['path']; files={str(q.relative_to(ROOT)):sha(q) for q in sorted(p.parent.rglob('*')) if q.is_file()}
    row['assets'].append({'path':a['path'],'sha256':sha(p),'matches_own_final_asset':sha(p)==a['sha256'],'reference_width_mm':a['width_mm'],'source_files_sha256':files})
   meta['figures'].append(row)
  else:row=next(x for x in meta['figures'] if x['label']==f['label'])
  row['editions'][edition]={'figure_number':number,'printed_page':printed,'physical_page':page,'pdf_sha256':meta['pdfs'][edition]['sha256'],'proof_png':str(proof.relative_to(B)),'proof_sha256':sha(proof),'render_scale_to_px':1600,'actual_review_status':'awaiting_review','page_text':doc[page-1].get_text()}
  if edition=='vol2-foundations' and names&gray_names:
   gray=B/'gray'/proof.name;gray.parent.mkdir(parents=True,exist_ok=True)
   if not gray.exists():subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','1600','-gray','-png',str(pdf),str(gray.with_suffix(''))],check=True,capture_output=True)
   row['gray']={'physical_page':page,'pdf_sha256':sha(pdf),'proof_png':str(gray.relative_to(B)),'proof_sha256':sha(gray),'actual_review_status':'awaiting_review'}
assert sum('machine-learning-notes' in f['editions'] for f in meta['figures'])==5
assert sum('gray' in f for f in meta['figures'])==4
assert all(a['matches_own_final_asset'] for f in meta['figures'] for a in f['assets'])
(B/'page-binding.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'pdfs':meta['pdfs'],'pages':[{'label':f['label'],'vol2':f['editions']['vol2-foundations']['physical_page'],'main':f['editions'].get('machine-learning-notes',{}).get('physical_page'),'gray':'gray' in f} for f in meta['figures']]},ensure_ascii=False,indent=2))
