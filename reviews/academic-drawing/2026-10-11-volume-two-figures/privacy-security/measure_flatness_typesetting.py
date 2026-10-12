from pathlib import Path
import json, hashlib
import numpy as np
from PIL import Image
root=Path.cwd()
review=root/'reviews/academic-drawing/2026-10-11-volume-two-figures/privacy-security'
previous=json.loads((review/'measurements.json').read_text())
records=[]
for old in previous['figures']:
    name=old['figure']
    folder=root/'figures/03-foundations/03-trustworthiness/generated'/name
    font_record=json.loads((folder/'typesetting-20261011.json').read_text())
    bg=folder/font_record['background']
    a=np.array(Image.open(bg).convert('RGB'))
    x0,y0,x1,y1=old['blank_ROI_xyxy']
    z=a[y0:y1,x0:x1].reshape(-1,3).astype(float)
    typo=json.loads((folder/'typography-check.json').read_text())
    assert not typo['missing_glyphs'] and not typo['outside_canvas'], name
    labels=json.loads((folder/'labels.json').read_text())
    sizes=sorted({round(s['size']/(a.shape[1]/(164.6/25.4*72)),2) for row in labels for s in row['segments']})
    records.append({'figure':name,'background':str(bg.relative_to(root)),'background_sha256':hashlib.sha256(bg.read_bytes()).hexdigest(),'final_sha256':hashlib.sha256((folder/'figure.png').read_bytes()).hexdigest(),'text_layer_sha256':hashlib.sha256((folder/'text-layer.png').read_bytes()).hexdigest(),'blank_ROI_xyxy':[x0,y0,x1,y1],'blank_RGB_median':np.median(z,axis=0).tolist(),'blank_RGB_std':np.std(z,axis=0).tolist(),'blank_max_absolute_delta_from_white':float(np.abs(z-255).max()),'pixels':[a.shape[1],a.shape[0]],'physical_reference_width_mm':164.6,'actual_source_font_sizes_pt':sizes,'missing_glyphs':typo['missing_glyphs'],'outside_canvas':typo['outside_canvas'],'status':'mechanical measurements and independent figure review complete; current book-page review pending'})
font_hash={}
for p in (root/'fonts').iterdir():
    if p.name in previous['font_sha256']:
        font_hash[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
out={'scope':'After outline-muted selection for four models; PATE and backdoor unchanged. Historical measurements.json retained.','measurement_only':'Descriptive blank ROI/font/glyph metrics do not automatically decide flatness, topology or layout. No pixels modified.','figures':records,'runtime':previous['runtime'],'font_sha256':font_hash,'licenses':previous['licenses']}
(review/'flatness-typesetting-measurements.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print({x['figure']:{'blank_RGB_median':x['blank_RGB_median'],'blank_max_absolute_delta':x['blank_max_absolute_delta_from_white'],'font_sizes_pt':x['actual_source_font_sizes_pt']} for x in records})
