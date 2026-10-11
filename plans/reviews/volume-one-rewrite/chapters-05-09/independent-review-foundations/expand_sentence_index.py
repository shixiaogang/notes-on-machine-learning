"""Expand human-authored ID selections. This never creates semantic judgments."""
from pathlib import Path
import csv
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
for authored in sorted(HERE.glob('chapter-*-sentences-authored.tsv')):
    chapter = authored.name.split('-')[1]
    units = json.loads((ROOT / f'chapter-{chapter}-units.json').read_text())
    valid_ids = {sentence['id'] for sentence in units['sentences']}
    records, seen = [], set()
    with authored.open() as source:
        for row in csv.DictReader(source, delimiter='\t'):
            paragraph, selection = row['sentence_selection'].split(':')
            chosen = []
            for item in selection.split(','):
                bounds = item.split('-')
                chosen.extend(f'{paragraph}-S{i:02d}'
                              for i in range(int(bounds[0]), int(bounds[-1]) + 1))
            assert all(unit in valid_ids and unit not in seen for unit in chosen), row
            seen.update(chosen)
            records.append({'sentence_ids': chosen, 'quote': row['quote'],
                            'manual_meaning_and_decision': row['meaning_and_decision']})
    (HERE / f'chapter-{chapter}-sentences.json').write_text(json.dumps({
        'version': units['sha256'],
        'note': 'IDs expanded mechanically from human-authored selections; no semantic verdict generated',
        'records': records, 'covered_count': len(seen),
        'total_indexed_count': len(valid_ids),
        'unrecorded_ids': sorted(valid_ids - seen)
    }, ensure_ascii=False, indent=2) + '\n')
    print(chapter, len(records), len(seen), len(valid_ids))
