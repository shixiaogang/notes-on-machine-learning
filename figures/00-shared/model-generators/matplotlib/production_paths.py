from pathlib import Path
import json
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
ITEMS=json.loads((Path(__file__).parent/'registry.json').read_text())
BYKEY={x['key']:x for x in ITEMS}
def destination(key):
    dest=ROOT/BYKEY[key]['archive_folder']
    dest.mkdir(parents=True,exist_ok=True)
    return dest
