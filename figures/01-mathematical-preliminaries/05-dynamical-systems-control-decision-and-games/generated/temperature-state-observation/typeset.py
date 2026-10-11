from pathlib import Path
import sys
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/01-mathematical-preliminaries/00-shared/generated/typography'))
import typeset_common
# Limited fallback: only explicitly tagged script 𝓔/𝓜, absent from actual Fira Math cmap.
typeset_common.FONT_FILES['stix-missing']='STIXTwoMath-Regular.otf'
from render_labels import render
render(Path(__file__).resolve().parent)
