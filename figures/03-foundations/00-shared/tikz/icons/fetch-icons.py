"""Vendor pinned Lucide outlines and export unchanged paths in semantic colours."""
from pathlib import Path
import base64,hashlib,json,re,subprocess
import pymupdf as fitz

HERE=Path(__file__).resolve().parent
COMMIT='1ef60af944de207e0d5176905a0759ba12e6ee8d'
NAMES='mail file-text files folder archive trash-2 user users database settings sliders-horizontal shield-check shield-x lock-keyhole check x clock calendar-days chart-column chart-line search filter monitor smartphone server brain network scale eye image circle-alert message-square book-open dices target refresh-cw send clipboard-check flower-2 bird cat dog car plane ship tree-pine wrench'.split()
COLORS={'blue':'#7188A3','green':'#829C8B','gold':'#B4A16F','red':'#A7787D','purple':'#9588A5','ink':'#3B4252'}
ALIASES={'trash-2':'trash','filter':'funnel'}

def fetch(url,dest):
    path=url.split('/'+COMMIT+'/')[1]
    api=f'https://api.github.com/repos/lucide-icons/lucide/contents/{path}?ref={COMMIT}'
    result=subprocess.run(['curl','--noproxy','*','-L','--connect-timeout','8','--max-time','20','--retry','2','--fail','--silent','--show-error',api],check=True,capture_output=True)
    dest.write_bytes(base64.b64decode(json.loads(result.stdout)['content']))

def main():
    base=f'https://raw.githubusercontent.com/lucide-icons/lucide/{COMMIT}/'
    if not (HERE/'LICENSE').exists():fetch(base+'LICENSE',HERE/'LICENSE')
    records=[]
    for name in NAMES:
        svg=HERE/(name+'.svg')
        upstream=ALIASES.get(name,name)
        if not svg.exists():fetch(base+'icons/'+upstream+'.svg',svg)
        text=svg.read_text()
        # MuPDF drops near-zero strokes despite round caps. Preserve the visible
        # dot by expanding that stroke's round cap to its equivalent circle.
        text=re.sub(r'<path d="M([\d.]+) ([\d.]+)h\.01"\s*/>',lambda m:f'<circle cx="{float(m[1])+.005}" cy="{m[2]}" r="1" fill="currentColor" stroke="none" />',text)
        for key,color in COLORS.items():
            with fitz.open(stream=text.replace('currentColor',color).encode(),filetype='svg') as doc:
                pdf=doc.convert_to_pdf()
            (HERE/f'{name}-{key}.pdf').write_bytes(pdf)
        records.append({'name':name,'url':base+'icons/'+upstream+'.svg','sha256':hashlib.sha256(svg.read_bytes()).hexdigest()})
    (HERE/'sources.json').write_text(json.dumps({'library':'Lucide','commit':COMMIT,'license':'ISC + Feather MIT notices in LICENSE','changes':'fixed semantic stroke colour; near-zero round-capped point strokes expanded to equivalent circles for PDF export; original SVG preserved','colors':COLORS,'icons':records},indent=2)+'\n')

if __name__=='__main__':main()
