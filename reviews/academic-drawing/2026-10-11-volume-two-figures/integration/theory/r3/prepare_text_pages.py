from pathlib import Path
import hashlib, json, re, subprocess, unicodedata
import pymupdf as fitz

B = Path(__file__).parent
PDF = B / 'inputs-r3/vol2-foundations.pdf'
doc = fitz.open(PDF)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
norm = lambda s: re.sub(r'\s+', '', unicodedata.normalize('NFKC', s))
queries = [
 ('OV-B70', '将候选从4个增至8个', '02-binary-classification.tex', [70,71], 17.14),
 ('OV-B331', '固定两份样本的', '02-binary-classification.tex', [331,331], 2.38),
 ('OV-B817', '展开权重递推可得', '02-binary-classification.tex', [817,818], 24.60),
 ('OV-G1325', '如果固定', '04-convex-learning-and-stability.tex', [1325,1326], 21.32),
 ('OV-G1624', '当前每个损失在欧氏空间上凸且', '04-convex-learning-and-stability.tex', [1624,1626], 7.88),
 ('OV-D252', '谱范数与激活函数共同控制输入扰动', '05-deep-learning-theory.tex', [252,253], 3.99),
 ('OV-D954', '为了精确求解多层谱演化', '05-deep-learning-theory.tex', [954,955], 10.49),
 ('TXT-B94', '固定容限', '02-binary-classification.tex', [94,94], None),
 ('TXT-M225', 'Brukhim等的组合拓扑构造给出该引理', '03-multiclass-classification.tex', [225,225], None),
 ('TXT-F687', 'Rademacher复杂度用随机符号检验', '01-statistical-learning-framework.tex', [687,687], None),
 ('TXT-F778', '恢复复杂度研究达到规定性能所需的代价', '01-statistical-learning-framework.tex', [778,778], None),
 ('TXT-G87', '这一等价刻画的经典形式及必要方向见学习理论教材', '04-convex-learning-and-stability.tex', [87,87], None),
 ('TXT-G1102', 'Russo与Zou用信息量控制', '04-convex-learning-and-stability.tex', [1102,1102], None),
]
rows=[]
for key, query, name, lines, overflow in queries:
 matches=[i for i,p in enumerate(doc) if norm(query) in norm(p.get_text())]
 if key=='OV-G1325':
  matches=[i for i in matches if '平均经验优化误差' in norm(doc[i].get_text()) and '条件互信息' in norm(doc[i].get_text())]
 assert len(matches)==1,(key,query,matches)
 i=matches[0];p=doc[i];out=B/'text-pages'/f'page-{i+1:04d}-{key}.png';out.parent.mkdir(exist_ok=True)
 if not out.exists():
  subprocess.run(['pdftoppm','-f',str(i+1),'-l',str(i+1),'-singlefile','-scale-to','1600','-png',str(PDF),str(out.with_suffix(''))],check=True,capture_output=True)
 line_data=[]
 for b in p.get_text('dict')['blocks']:
  for ln in b.get('lines',[]):
   line_data.append({'text': ''.join(s['text'] for s in ln['spans']), 'bbox':ln['bbox']})
 src=B/'inputs-r3/tex/02-foundations/02-learning-theory'/name
 source_lines=src.read_text().splitlines()
 rows.append({'id':key,'query':query,'source_name':name,'source_sha256':sha(src),'source_line_range':lines,'source_text':'\n'.join(source_lines[lines[0]-1:lines[1]]),'reported_overfull_pt':overflow,'physical_page':i+1,'printed_page':p.get_label(),'pdf_sha256':sha(PDF),'proof_png':str(out.relative_to(B)),'proof_sha256':sha(out),'pdf_page_size_pt':list(p.rect),'page_text':p.get_text(),'pdf_lines':line_data,'actual_review_status':'awaiting_actual_review'})
(B/'text-page-binding.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{k:x[k] for k in ('id','physical_page','printed_page','proof_png')} for x in rows],ensure_ascii=False,indent=2))
