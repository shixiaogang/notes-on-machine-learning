"""Mechanical export only; judgments come from manually written r3/r4 records."""
from pathlib import Path
import hashlib, json, shutil, re
import pymupdf as fitz
from PIL import Image, ImageChops

B = Path(__file__).parent
R = B.parent.parent
ROOT = R.parent / 'volume-two-figures'
OLD = B.parent / 'final-root-page-review'
FROZEN = B.parent / 'frozen-review-pdfs-r4'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: json.loads(p.read_text())
def write(name, value):
    (B / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

m = read(B/'r4-binding.json')
manual = read(B/'manual-observations-r4.json')
oldmanual = read(OLD/'manual-observations-r3.json')
oldbinding = read(OLD/'page-binding.json')
edits = read(OLD/'followup-old-new.json')
assert len(m['figures']) == 25 and len(m['text_pages']) == 13
assert all((B/f'followup-{p}-r4.md').is_file() for p in ['C','P','W'])

# Relocate only our own frozen copies; the portable delivery has no large PDF.
FROZEN.mkdir(exist_ok=True)
frozen_rows = []
docs = {}
for edition, info in m['pdfs'].items():
    expected = info['sha256']
    assert sha(ROOT/'target'/f'{edition}.pdf') == expected
    original = B/'inputs-r4'/f'{edition}.pdf'
    destination = FROZEN/f'{edition}.pdf'
    if original.is_file():
        assert not destination.exists()
        assert sha(original) == expected
        shutil.move(str(original), str(destination))
    assert sha(destination) == expected
    info['snapshot_pdf_at_initial_render'] = f'inputs-r4/{edition}.pdf'
    info['snapshot_pdf'] = str(destination.relative_to(B.parent))
    info['snapshot_pdf_location_basis'] = 'relative to the parent build directory; outside portable r4 delivery'
    info['snapshot_in_delivery'] = False
    docs[edition] = fitz.open(destination)
    frozen_rows.append({'edition_pdf':f'target/{edition}.pdf','sha256':expected,
                        'local_frozen_pdf':str(destination),'included_in_delivery':False,
                        'physical_pages':len(docs[edition])})
write('frozen-pdf-bindings.json', frozen_rows)
write('inputs-r4-sha.json', {str(p.relative_to(B/'inputs-r4')):sha(p)
                           for p in sorted((B/'inputs-r4').rglob('*')) if p.is_file()})

# Verify root current source and assets; byte identity is not semantic review.
for row in m['six_chapters_exact_expected_diff']:
    assert sha(ROOT/row['owner']) == row['r4_sha256']
    assert sha(B/'inputs-r4'/row['owner']) == row['r4_sha256']
    prior = (OLD/'inputs-r3'/row['owner']).read_text()
    for e in edits:
        if Path(row['owner']).name == e['source_name']:
            assert prior.count(e['old']) == 1
            prior = prior.replace(e['old'],e['new'])
    assert prior == (B/'inputs-r4'/row['owner']).read_text()
for f in m['figures']:
    assert sha(ROOT/f['owner']) == f['source_sha256_r4']
    for a in f['assets']:
        assert sha(ROOT/a['path']) == a['sha256']
        for path, expected in a['source_files_sha256'].items():
            assert sha(ROOT/path) == expected

entries = []
def binding(edition, v, gray, purpose, identifier):
    proof = B/v['proof_png']
    assert sha(proof) == v['proof_sha256']
    image = Image.open(proof)
    rgb = image.convert('RGB')
    if gray:
        red, green, blue = rgb.split()
        assert ImageChops.difference(red,green).getbbox() is None
        assert ImageChops.difference(red,blue).getbbox() is None
    page = docs[edition][v['physical_page']-1]
    width_pt, height_pt = float(page.rect.width),float(page.rect.height)
    expected_dpi = 1600*72/max(width_pt,height_pt)
    out = {'id':identifier,'purpose':purpose,'edition_pdf':f'target/{edition}.pdf',
           'edition_pdf_sha256':m['pdfs'][edition]['sha256'],
           'physical_page':v['physical_page'],'printed_page':page.get_label(),
           'proof':v['proof_png'],'proof_sha256':sha(proof),
           'dpi':expected_dpi,'colorspace':'GRAY' if gray else 'RGB',
           'render_method':'pdftoppm -singlefile -scale-to 1600 -png' + (' -gray' if gray else ''),
           'dpi_basis':'equivalent DPI from the 1600-pixel longer page dimension; not source-asset DPI',
           'page_size_pt':[width_pt,height_pt],'dimensions_px':list(image.size),
           'effective_dpi_xy':[image.width*72/width_pt,image.height*72/height_pt],
           'png_storage_mode':image.mode,
           'gray_rgb_channels_identical':True if gray else None,
           'comparison_to_r3':v['comparison_to_r3']}
    entries.append(out)

same_views = 0
changed_views = 0
table = []
for f in m['figures']:
    earlier = next(q for q in oldbinding['figures'] if q['label']==f['label'])
    for edition,v in f['editions'].items():
        c=v['comparison_to_r3']
        assert c['png_byte_identical'] == c['pixel_identical']
        if c['pixel_identical']:
            oldview=OLD/earlier['editions'][edition]['proof_png']
            assert oldview.read_bytes()==(B/v['proof_png']).read_bytes()
            same_views+=1
            v['review_status']='r3 actual visually reviewed page rebound to r4: PNG bytes and pixels identical'
            v['actual_review_record_r3']='../final-root-page-review/actual-page-review-r3.md'
            v['actual_review_method_r4']='identical full-page pixels; no claim of a second opening'
        else:
            changed_views+=1
            assert f['label']=='fig:learning-theory-ds-neighbors'
            v['review_status']='r4 changed full page actually reopened and accepted'
            v['actual_review_method_r4']='actual visual inspection of the changed r4 full page'
            v['observation_r4']=manual['changed_figure_views'][f['label']][edition]
        binding(edition,v,False,'theory figure full page',f['label']+'@'+edition)
    if 'gray' in f:
        v=f['gray']; c=v['comparison_to_r3']
        assert c['png_byte_identical']==c['pixel_identical']
        if c['pixel_identical']:
            assert (OLD/earlier['gray']['proof_png']).read_bytes()==(B/v['proof_png']).read_bytes()
            same_views+=1
            v['review_status']='r3 actual gray-page observation rebound to r4: PNG bytes and pixels identical'
            v['actual_review_record_r3']='../final-root-page-review/actual-page-review-r3.md'
        else:
            changed_views+=1
            assert f['label']=='fig:learning-theory-ds-neighbors'
            v['review_status']='r4 changed gray full page actually reopened and accepted'
            v['observation_r4']=manual['changed_figure_views'][f['label']]['gray']
        binding('vol2-foundations',v,True,'theory grayscale full page',f['label']+'@GRAY')
    v=f['editions']['vol2-foundations']
    route='差异页实际重看接受' if not v['comparison_to_r3']['pixel_identical'] else '全页字节/像素一致，重新绑定r3实际观察'
    table.append(f"| {f['label']} | {v['physical_page']}/{v['printed_page']} | {route} | [{v['proof_sha256'][:12]}]({v['proof_png']}) |")
assert same_views==31 and changed_views==3

text_to_issue={'TXT-B94':'CVT-R-B02','TXT-F687':'PDF-SCITE-F687','TXT-F778':'PDF-SCITE-F778',
               'TXT-M225':'PDF-SCITE-M225','TXT-G87':'PDF-SCITE-G87','TXT-G1102':'PDF-SCITE-G1102'}
overfull_table=[]
for v in m['text_pages']:
    if v['id'] in text_to_issue:
        v['review_status']='r4 repaired paragraph and full-page layout actually reread and accepted'
        v['actual_review_r4']=manual['actual_repaired_paragraph_views'][text_to_issue[v['id']]]
        purpose='six repaired paragraphs'
    elif v['id']=='OV-B70':
        assert not v['comparison_to_r3']['pixel_identical']
        v['review_status']='r4 changed full page actually reopened: no crop or margin-note collision; overfull warning retained'
        v['actual_review_r4']=manual['changed_overfull_view']['OV-B70']
        purpose='specified overfull full page'
    else:
        assert v['id'] in manual['rebound_overfull_ids']
        assert v['comparison_to_r3']['png_byte_identical'] and v['comparison_to_r3']['pixel_identical']
        v['review_status']='r3 actual overfull-page observation rebound to identical r4 page; warning retained'
        v['actual_review_record_r3']='../final-root-page-review/overfull-review-r3.md'
        purpose='specified overfull full page'
    binding('vol2-foundations',v,False,purpose,v['id'])
    if v['id'].startswith('OV-'):
        route='新版差异页实际重看' if v['id']=='OV-B70' else '与r3整页字节/像素一致，重新绑定'
        observation=manual['changed_overfull_view'][v['id']] if v['id']=='OV-B70' else oldmanual['overfull_observations'][v['id']]
        overfull_table.append(f"| {v['id']} | {v['physical_page']}/{v['printed_page']} | {v['reported_overfull_r3_pt']} | {route} | {observation} |")
assert len(entries)==47 and len({e['proof'] for e in entries})==47
assert {str(p.relative_to(B)) for p in B.rglob('*.png')}=={e['proof'] for e in entries}
write('final-page-bindings.json',{'schema':'final-page-bindings/1','date':'2026-10-12',
    'stage':'r4 frozen root PDFs','physical_page_numbering':'one-based',
    'scope':'all 47 actually saved complete-page PNG files; repeated physical pages have distinct review uses',
    'colorspace_note':'GRAY means rendered with Poppler -gray and R=G=B pixels verified; PNG container is RGB',
    'dpi_note':'Poppler used -scale-to 1600. Equivalent DPI is 145.454545 for 612x792pt pages; horizontal rounding gives 145.529412. This does not change or upscale figure source assets.',
    'entries':entries})

closed=[]
for e in edits:
    source=B/'inputs-r4/tex/03-foundations/02-learning-theory'/e['source_name']
    content=source.read_text()
    assert content.count(e['candidate_paragraph'])==1
    v=next(q for q in m['text_pages'] if text_to_issue.get(q['id'])==e['id'])
    closed.append({**e,'source_sha256_r4':sha(source),'actual_paragraph_r4':e['candidate_paragraph'],
        'candidate_matches_actual_root_r4':True,'physical_page_r4':v['physical_page'],
        'printed_page_r4':v['printed_page'],'edition_pdf_sha256_r4':v['pdf_sha256'],
        'proof_r4':v['proof_png'],'proof_sha256_r4':v['proof_sha256'],
        'actual_review_r4':manual['actual_repaired_paragraph_views'][e['id']],
        'review_records_r4':['followup-C-r4.md','followup-P-r4.md','followup-W-r4.md'],
        'status_r4':'closed after actual root source, separate local C/P/W and actual revised PDF-page review'})
write('closure-r4.json',closed)
m['actual_review_role_r4']=manual['role']
m['final_status']='25 figures / 5 main representatives / 4 grayscale uses bound to r4; six text issues closed; seven specified overfull warnings retained'
m['comparison_summary']={'identical_figure_view_uses':same_views,'changed_figure_view_uses_actually_reopened':changed_views,
    'identical_overfull_uses_rebound':6,'changed_overfull_uses_actually_reopened':1,
    'six_repaired_paragraphs_actually_reopened':6,'actual_saved_complete_page_png_files':len(entries)}
write('r4-binding.json',m)

(B/'actual-page-review-r4.md').write_text('''# 根r4理论图页：最终绑定与差异页实际复核

2026-10-12，theory_second_half，AI自查。本组曾制作25图，不能称全文独立审查。根源和成品只读，本目录没有构建或修改根输入。

25卷二图页用途、5全集代表、4灰度用途共34张完整页PNG重新从冻结r4 PDF渲染。31张与r3实际目检页字节及像素一致，明确重新绑定r3观察；3张DS图页因邻段标点不同，均重新实际打开。不是仅凭图资产相同判断书页相同。

卷二PDF SHA：`94ca9126cd7f19bde8dd24827ae8dd70df43ec7b258be5618c864a3344497bbe`。
全集PDF SHA：`d5ee494d27df547b41b7e02d287ba5489f069975279b45b2c34ad3455f42a1ab`。

## 卷二25图

| 图label | 物理/印刷页 | 当前验收方式 | 当前proof SHA前12位/页图 |
|---|---|---|---|
'''+ '\n'.join(table)+'''

分布偏移和支持覆盖共用物理279页，因此25图对应24个卷二物理页。全集代表仍为two-randomness p1051、research-map p1072、DS p1114、NTK p1193、flat p1217；其中仅DS像素不同。灰度为UC p133、DS p168、flat p271、domain p284；其中仅DS不同。三张DS实际观察在manual-observations-r4.json，完整SHA、源/成图/图源绑定在r4-binding.json。所有47张实际保存PNG的逐个版名/页码/相对路径/等效DPI/色彩空间在final-page-bindings.json。

六处正文修复均已实际看新版页：B94 p132、F687 p123、F778 p128、M225 p168、G87 p186、G1102 p210。“图中全部候选”可见，五处scite引用均只有一个句号，无旧逗号或双句号。局部C/P/W与闭环在对应记录及closure-r4.json，无新局部缺陷。

物理字号机械数据来自成图阶段，当前图资产SHA及引用宽度完全一致，保持主体8pt/辅助7.5pt；实际r3各图页已新目检，r4相同整页重新绑定、差异整页实际重看。保留默认300DPI阈值报告，规范按实际物理尺寸和字形验收，未人工上采样模型背景。

冻结大PDF保留在本worktree的build/frozen-review-pdfs-r4，不包含在交付目录；frozen-pdf-bindings.json保留受审SHA。交付含源/宏/构建清单快照、47张PNG、人工记录和版本绑定。这里仅验收上述图页与指定正文，不宣称全部全集图页、全书灰度或全书零Overfull。
''')
(B/'overfull-review-r4.md').write_text('''# r4七处指定正文Overfull实页闭环

2026-10-12，theory_second_half，AI自查。此前r3七处均按句义定位并真实查看，记录保留在相邻r3目录。本次全部七页从r4重新渲染比较；六页与r3整页字节及像素一致，重新绑定r3实际判断，只有B70所在p132因下方数量短语改变，已重新打开确认。没有将TeX警告或正文盒外可读字形抹去。

| ID | 物理/印刷页 | 原日志Overfull pt | r4核验方式 | 实际判断 |
|---|---|---|---|---|
'''+ '\n'.join(overfull_table)+'''

这七处没有发现被裁切或与边注相撞。多行内联公式仍有伸入右侧留白及结果换行的排版边界；这些原有警告保留，不宣称全书零Overfull，也不因PDF文字bbox与TeX盒量不同而否认警告。完整源段、当前proof/PDF SHA与比较结果见r4-binding.json，逐个全页渲染参数见final-page-bindings.json。
''')
(B/'README.md').write_text('''# 根最终r4成品：理论部分局部验收交付

本目录位于theory独立worktree的忽略build/，根源/资源和PDF只读。本组曾制作25图，因此这是AI自查和跨卷局部接口复读，不能称全文独立审查。未构建、修改或提交根输入。

- [当前25图、5全集代表、4灰度的验收方式](actual-page-review-r4.md)
- [完整PDF/源/资产/图源/proof SHA及整页比较](r4-binding.json)
- [47张实际保存完整页PNG的版名、物理页、相对proof、DPI与色彩空间](final-page-bindings.json)
- [差异图页及六处改后正文的手写实际观察](manual-observations-r4.json)
- [七处指定Overfull实页闭环](overfull-review-r4.md)
- [六处改后局部C](followup-C-r4.md)、[P](followup-P-r4.md)、[W/特殊单元/E1–E12](followup-W-r4.md)
- [六项实际源及实际PDF闭环](closure-r4.json)
- [当前六章源/宏/构建manifest快照SHA](inputs-r4-sha.json)
- [外部冻结PDF的受审SHA清单](frozen-pdf-bindings.json)
- [本交付全部文件SHA清单](delivery-manifest-r4.json)

31/34个图页用途与r3实际目检页的PNG字节/像素一致；DS在卷二p168、全集p1114、灰度p168三张差异整页均实际重看。6/7个指定Overfull页与r3一致，B70/p132差异页实际重看。六个修改正文页全部实际复读，数量短语与五处scite句末标点均已关闭，无新问题。

原r3诊断保留在相邻final-root-page-review，记录不会事后改为“当时已关闭”。建议同时保存两目录以保留发现与修复链。r4交付不包含大PDF，冻结副本位于本worktree的build/frozen-review-pdfs-r4；根另行归档受审大PDF，不能用后续重建的SHA冒称本次成品。主工作区重建后应依据final-page-bindings.json重渲染这些完整页，相同页重新绑定、差异页实际重看。

图源未改且物理宽度保持原登记，8/7.5pt真字；默认300DPI阈值报告保留，未人工上采样源背景。七处Overfull无实际裁切/边注碰撞，但原警告保留，不宣称全书零Overfull。全集只有五代表和四灰度用途，不声称全量全集/灰度检查。

prepare_r4.py保留初次渲染/比较方法，finalize_r4.py仅机械绑定手写观察、生成SHA清单与表格。已渲染目录不应直接重跑prepare_r4.py覆盖证据；源大PDF已移到本地外部冻结目录。
''')

# End-of-export verification includes actual root frozen PDFs again.
for edition,info in m['pdfs'].items():
    assert sha(ROOT/'target'/f'{edition}.pdf')==info['sha256']
manifest={'stage':'r4 theory portable review delivery','date':'2026-10-12',
          'files':{str(p.relative_to(B)):sha(p) for p in sorted(B.rglob('*'))
                   if p.is_file() and p.name!='delivery-manifest-r4.json'},
          'excludes':'frozen large PDFs retained outside this directory',
          'saved_png_files':len(entries),'frozen_pdf_shas':{e:i['sha256'] for e,i in m['pdfs'].items()}}
assert not list(B.rglob('*.pdf'))
write('delivery-manifest-r4.json',manifest)
print(json.dumps({'portable_files_including_manifest':len(manifest['files'])+1,
                  'saved_png_files':len(entries),'same_figure_uses':same_views,
                  'changed_figure_uses_actually_reviewed':changed_views,
                  'closed_text_issues':len(closed),'portable_pdf_files':0},ensure_ascii=False,indent=2))
