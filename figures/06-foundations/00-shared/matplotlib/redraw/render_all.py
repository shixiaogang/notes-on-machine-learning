"""Reproduce volume2 previews inside the task worktree; no book edits/build."""
from pathlib import Path
import argparse,json,subprocess,sys
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
OUT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
from render_tikz import render
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--only',nargs='*');p.add_argument('--skip-charts',action='store_true');a=p.parse_args()
 if not a.skip_charts:
  subprocess.run([sys.executable,str(OUT/'charts.py')],cwd=ROOT,check=True)
  if json.loads((OUT/'chart-failures.json').read_text()):raise RuntimeError('Chart generation failed')
 subprocess.run([sys.executable,str(OUT/'tikz_sources.py')],cwd=ROOT,check=True)
 records=[]
 for item in json.loads((OUT/'tikz-records.json').read_text()):
  if a.only and item['key'] not in a.only:continue
  r=render(ROOT/item['source']);r.update(key=item['key']);records.append(r);print(item['key'],'rendered',flush=True)
 (OUT/'reproduction-render.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
