"""Exact Laplace densities and editable process diagram; vector PDF composition."""
from pathlib import Path
import json, hashlib, sys
import numpy as np
import matplotlib.pyplot as plt
import pymupdf as fitz
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
D=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'figures/02-foundations/00-shared/academic-drawing'))
from plot_style import configure,prepare_figure,note,style_record,BLUE,GREEN,BLUE_FILL,GREEN_FILL,GRID,MUTED
configure()
x=np.linspace(0,8,161)
p=.5*np.exp(-np.abs(x-3));q=.5*np.exp(-np.abs(x-4))
assert len(x)==161 and np.isclose(p[60],.5) and np.isclose(q[80],.5)
mask=(x>=5)&(x<=6)
assert np.all(p>0) and np.all(q>0) and np.all(q[mask]/p[mask]<=np.e+1e-12)
fig,ax=plt.subplots(figsize=(112/25.4,57/25.4),layout='constrained')
ax.fill_between(x,0,q,where=mask,color=GREEN_FILL,zorder=0)
ax.fill_between(x,0,p,where=mask,color=BLUE_FILL,zorder=1)
ax.plot(x,p,color=BLUE,label=r'$3+Z$',zorder=3)
ax.plot(x,q,color=GREEN,ls='--',label=r"$4+Z'$",zorder=3)
ax.set(xlim=(0,8),ylim=(0,.58),xlabel=r'发布值 $u$',ylabel='概率密度',xticks=[0,3,4,5,6,8],yticks=[0,.25,.5])
note(ax.text(5.5,.53,r'$E=[5,6]$',ha='center',fontsize=7.5))
ax.legend(loc='upper left')
prepare_figure(fig)
for ext in ['pdf','svg','png']:fig.savefig(D/('density.'+ext),dpi=300)
plt.close(fig)
top=ROOT/'figures/02-foundations/03-trustworthiness/tikz/trust-dp-neighbors-process.pdf'
PT=72/25.4;W=164.6*PT
with fitz.open(top) as a,fitz.open(D/'density.pdf') as b:
    top_h=a[0].rect.height*W/a[0].rect.width
    chart_w=112*PT; chart_h=b[0].rect.height
    out=fitz.open();page=out.new_page(width=W,height=top_h+2*PT+chart_h)
    page.show_pdf_page(fitz.Rect(0,0,W,top_h),a,0)
    page.show_pdf_page(fitz.Rect((W-chart_w)/2,top_h+2*PT,(W+chart_w)/2,top_h+2*PT+chart_h),b,0)
    out.save(D/'figure.pdf')
    page.get_pixmap(dpi=300).save(D/'figure.png')
    (D/'figure.svg').write_text(page.get_svg_image(text_as_path=True))
    mm=[round(v/PT,3) for v in [W,page.rect.height]]
record={'formula':'p_mu(u)=0.5 exp(-abs(u-mu))','means':[3,4],'scale':1,'sensitivity':1,'epsilon':1,'delta':0,'domain':[0,8],'samples':161,'event':[5,6],'adjacency':'one added record','alternative_mechanisms':True,'joint_coupling':'unspecified','x':x.tolist(),'p':p.tolist(),'q':q.tolist(),'style':style_record(),'physical_size_mm':mm,'font_size_pt':{'main':8,'notes':7.5},'upper':'editable TikZ process','lower':'exact Matplotlib densities, vector PDF','status':'rendered; manual science and physical-size review pending'}
(D/'data-and-render.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
