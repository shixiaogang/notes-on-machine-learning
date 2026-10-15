import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
SOURCE = ROOT / 'tex/01-mathematical-preliminaries-upper/02-linear-algebra-and-geometry/03-functional-analysis-and-approximation.tex'
def replace(old, new):
    s = SOURCE.read_text()
    assert s.count(old) == 1, (old[:90], s.count(old))
    SOURCE.write_text(s.replace(old, new))
def record(ids, severity, before, after, action, reread, reason, decision='修改'):
    p = OUT / 'consolidated-findings.json'
    entries = json.loads(p.read_text()) if p.exists() else []
    entries.append(dict(merged_id=f'CH07-M-{len(entries)+1:02d}', original_ids=ids.split(),
        severity=severity, decision=decision, location_before=before, location_after={'quote':after},
        action=action, reread_range=reread, closure_reason=reason))
    p.write_text(json.dumps(entries, ensure_ascii=False, indent=2)+'\n')
def note(text):
    with (OUT/'repair-notes.md').open('a') as f: f.write(text+'\n')
