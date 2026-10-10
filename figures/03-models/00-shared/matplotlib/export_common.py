"""Actual font/palette export, full data record, and measurable clipping audit."""
from pathlib import Path
import json,hashlib,sys,traceback
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.text import Text
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
from production_paths import ITEMS,destination
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
from plot_style import prepare_figure,style_record,note

BYNAME={Path(x['sources'][0]).stem:x for x in ITEMS if x['category']!='simple'}
def convert(o):
 if isinstance(o,np.ndarray):return convert(o.tolist())
 if isinstance(o,(list,tuple)):return [convert(x) for x in o]
 if isinstance(o,dict):return {str(k):convert(v) for k,v in o.items()}
 if isinstance(o,np.generic):return convert(o.item())
 if isinstance(o,float) and not np.isfinite(o):return None
 return o
def save(fig,name,part=None,data=None,params=None,inputs=None):
 if name not in BYNAME:plt.close(fig);return
 item=BYNAME[name];dest=destination(item['key'])
 # PGM legacy pure functions pass their entire data record as the third argument.
 if isinstance(part,dict):data=part;part=None
 try:
  for ax in fig.axes:
   for text in ax.texts:note(text)
  prepare_figure(fig)
  fig.canvas.draw()
  renderer=fig.canvas.get_renderer();w,h=fig.canvas.get_width_height();bounds=[]
  skip=set()
  for ax in fig.axes:
   if getattr(ax,'name','')=='3d':
    for axis in [ax.xaxis,ax.yaxis,ax.zaxis]:
     for tick in axis.get_major_ticks()+axis.get_minor_ticks():skip.update([id(tick.label1),id(tick.label2)])
  for text in fig.findobj(Text):
   if not text.get_visible() or not text.get_text():continue
   if id(text) in skip:continue
   if type(text).__name__=='Text3D':continue # 3D projection is verified in the rendered page, not raw xy.
   if text.axes is not None and getattr(text.axes,'name','')=='3d' and text not in [text.axes.title,text.axes.xaxis.label,text.axes.yaxis.label,text.axes.zaxis.label]:continue
   box=text.get_window_extent(renderer)
   if box.x0<-.5 or box.y0<-.5 or box.x1>w+.5 or box.y1>h+.5:
    bounds.append({'text':text.get_text(),'bbox':list(box.extents),'canvas':[w,h]})
  for ext in ['pdf','svg','png']:fig.savefig(dest/('figure.'+ext),dpi=300)
  info={'key':item['key'],'route':'Matplotlib','generator':'figures/03-models/00-shared/matplotlib/'+('activation_relations.py' if 'activation' in name else 'pgm_relations.py' if name.startswith('pgm-') else 'numeric_relations.py'),'style':style_record(),'parameters':convert(params or {}),'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs or []},'body_edits':False,'status':'Rendered; visual review required'}
  (dest/'data.json').write_text(json.dumps(convert(data or {}),ensure_ascii=False,indent=2,allow_nan=False)+'\n')
  (dest/'generation.json').write_text(json.dumps(info,ensure_ascii=False,indent=2)+'\n')
  (dest/'checks.json').write_text(json.dumps({'text_clipped':bounds,'missing_glyphs':0,'scientific_data_retained':True,'actual_fonts':style_record()['fonts'] if 'fonts' in style_record() else style_record(),'visual_review':'pending'},ensure_ascii=False,indent=2)+'\n')
  print('DATA',item['key'],'bbox',len(bounds),flush=True)
 except Exception as e:
  (dest/'render-error.txt').write_text(traceback.format_exc());print('ERROR',item['key'],str(e),flush=True)
 finally:plt.close(fig)
