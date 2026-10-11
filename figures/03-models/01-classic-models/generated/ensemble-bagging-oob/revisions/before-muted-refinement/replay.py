from pathlib import Path
import sys
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/03-models/00-shared/generated'))
from replay import replay_figure
if __name__=='__main__':replay_figure(Path(__file__).parent)
