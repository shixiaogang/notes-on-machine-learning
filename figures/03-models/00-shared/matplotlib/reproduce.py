"""Reproduce current figure assets without changing book text."""
from pathlib import Path
import argparse,os,sys,shutil
from production_paths import ROOT,ITEMS,destination
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--route',choices=['all','data','simple'],default='all')
    args=p.parse_args();os.chdir(ROOT)
    os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'build/matplotlib-config'))
    if args.route!='simple':
        import numeric_relations as n
        n.classic();n.extra_classic();n.neural()
        import lloyd_relations as l;l.draw()
        import activation_relations,pgm_relations,mixed_and_extra
    if args.route!='data':
        sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
        from render_tikz import render
        for x in ITEMS:
            if x['category']!='simple':continue
            d=destination(x['key']);render(d/'source.tex',d)
            for ext in ['pdf','svg','png']:shutil.move(d/('source.'+ext),d/('figure.'+ext))
