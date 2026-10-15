#!/usr/bin/env python3
"""Typeset an arbitrary-length, retained imagegen history illustration.

Coordinates in timeline-data.json use a 1122 x 1402 reference canvas.
Optional label_positions are [text_x, event_y_center], not text top edges.
The illustration itself is never repainted by this script.
"""
from pathlib import Path
import hashlib
import json

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents
            if (p / 'tex/preamble.tex').is_file() and (p / 'fonts').is_dir())
REFERENCE_CANVAS = (1122, 1402)
FONTS = {'primary': 'SourceHanSansSC-Normal.otf',
         'annotation': 'LXGWWenKai-Regular.ttf',
         'latin': 'FiraMath-Regular.otf'}
LICENSES = {'primary': 'SourceHanSans-OFL.txt',
            'annotation': 'LXGWWenKai-OFL.txt',
            'latin': 'FiraMath-README.md'}
COLORS = ['#7188A3', '#829C8B', '#B4A16F', '#A7787D', '#9588A5']
CMAPS = {role: TTFont(ROOT / 'fonts' / name).getBestCmap()
         for role, name in FONTS.items()}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def positions(data):
    """Allocate rows from actual event count, or use audited manual centers."""
    n = len(data['events'])
    if n == 0:
        raise ValueError('At least one historical event is required')
    if 'label_positions' in data:
        coords = data['label_positions']
        if len(coords) != n or any(len(pair) != 2 for pair in coords):
            raise ValueError('label_positions must contain one [x, ycenter] per event')
        return coords
    first, last = data.get('label_center_range', [95, 1307])
    if not 0 <= first <= last <= REFERENCE_CANVAS[1]:
        raise ValueError('Invalid label_center_range')
    return [[26 if i % 2 == 0 else 590,
             (first + last) / 2 if n == 1 else first + i * (last - first) / (n - 1)]
            for i in range(n)]


def draw_label(draw, text, x, y, size, role, color, event_index):
    start = x
    baseline = y + size
    boxes = []
    for ch in text:
        font_role = 'latin' if ord(ch) < 128 or ch == '–' else role
        if ord(ch) not in CMAPS[font_role]:
            raise ValueError(f'Missing glyph: {ch}')
        font = ImageFont.truetype(str(ROOT / 'fonts' / FONTS[font_role]), size)
        box = draw.textbbox((x, baseline), ch, font=font, anchor='ls')
        draw.text((x, baseline), ch, font=font, fill=color, anchor='ls')
        if not ch.isspace():
            boxes.append(box)
        x += draw.textlength(ch, font=font)
    if not boxes:
        raise ValueError('An empty label cannot be typeset')
    return {'text': text, 'xy': [start, y], 'size_px': size, 'role': role,
            'color': color, 'event_index': event_index,
            'bbox': [min(b[0] for b in boxes), min(b[1] for b in boxes),
                     max(b[2] for b in boxes), max(b[3] for b in boxes)]}


def check_labels(labels, width, height):
    for label in labels:
        x0, y0, x1, y1 = label['bbox']
        if not (0 <= x0 < x1 <= width and 0 <= y0 < y1 <= height):
            raise ValueError(f"Outside canvas: {label['text']}")
    for i, label in enumerate(labels):
        for other in labels[i + 1:]:
            a, b, c, d = label['bbox']
            e, f, g, h = other['bbox']
            if max(a, e) < min(c, g) and max(b, f) < min(d, h):
                raise ValueError(f"Label collision: {label['text']} / {other['text']}")


def main():
    data = json.loads((HERE / 'timeline-data.json').read_text())
    background = Image.open(HERE / 'background.png').convert('RGBA')
    width_px, height_px = background.size
    sx, sy = width_px / REFERENCE_CANVAS[0], height_px / REFERENCE_CANVAS[1]
    coords = positions(data)
    overlay = Image.new('RGBA', background.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    labels = []
    for i, event in enumerate(data['events']):
        x, center = coords[i]
        lines = event.get('lines', [])
        if len(lines) > 2:
            raise ValueError(f"Keep at most two annotation lines: {event['title']}")
        specs = [(event['date'], x, center - 53, 30, 'primary', COLORS[i % len(COLORS)]),
                 (event['title'], x, center - 15, 21, 'primary', '#3B4252')]
        specs += [(line, x, center + 18 + 26 * j, 20, 'annotation', '#6B7280')
                  for j, line in enumerate(lines)]
        for text, tx, ty, size, role, color in specs:
            labels.append(draw_label(draw, text, round(tx * sx), round(ty * sy),
                                     round(size * sx), role, color, i))
    check_labels(labels, width_px, height_px)
    overlay.save(HERE / 'typography.png')
    Image.alpha_composite(background, overlay).convert('RGB').save(HERE / 'figure.png')
    save('labels.json', {'canvas_px': [width_px, height_px],
                         'reference_canvas_px': list(REFERENCE_CANVAS),
                         'label_positions': coords,
                         'label_positions_semantics': '[text_x, event_y_center]',
                         'event_count': len(data['events']), 'labels': labels})
    fonts = []
    for role, name in FONTS.items():
        path = ROOT / 'fonts' / name
        license_path = ROOT / 'fonts/licenses' / LICENSES[role]
        fonts.append({'role': role, 'path': str(path.relative_to(ROOT)),
                      'sha256': sha(path), 'license': str(license_path.relative_to(ROOT)),
                      'license_sha256': sha(license_path)})
    save('font-provenance.json', {'fonts': fonts, 'artificial_bold': False,
                                  'missing_glyphs': []})
    body_width = data['body_width_mm']
    point_scale = body_width / 25.4 * 72 / width_px
    annotation_pt = round(20 * sx) * point_scale
    save('typography-check.json', {
        'canvas_px': [width_px, height_px], 'event_count': len(data['events']),
        'label_count': len(labels), 'outside_canvas': [], 'label_overlap': [],
        'missing_glyphs': [], 'body_width_mm': body_width,
        'minimum_annotation_pt': annotation_pt,
        'primary_pt': round(21 * sx) * point_scale,
        'year_pt': round(30 * sx) * point_scale,
        'figure_height_mm': body_width * height_px / width_px,
        'maximum_height_ratio': data['maximum_height_ratio'],
        'colors_encode': 'Visual rhythm only; color count does not set the event count.',
        'artwork_collision_check': 'Must be visually checked against background and final book pages.'})
    revision_prompts = [name for name in ['revision-prompt.txt', 'second-revision-prompt.txt']
                        if (HERE / name).is_file()]
    source_files = ['typeset.py', 'timeline-data.json', 'data-definition.json',
                    'references/sources.json'] + revision_prompts
    archived_backgrounds = {name: sha(HERE / name) for name in ['background-initial.png']
                            if (HERE / name).is_file()}
    save('generation.json', {
        'key': data['key'], 'route': 'generated', 'date': '2026-10-13',
        'tool': 'image_gen.imagegen', 'model': 'not exposed by built-in tool',
        'prompt': 'prompt.txt', 'references': 'references/sources.json',
        'body_owner': data['owner'], 'label': data['label'],
        'event_count': len(data['events']),
        'revision_prompts': revision_prompts,
        'background_generation': ('Final background retained after imagegen local revisions.'
                                  if revision_prompts else 'Initial imagegen background retained.'),
        'archive_sha256': archived_backgrounds,
        'archive_scope': 'Initial backgrounds preserve generation history; they are not body assets.',
        'first_publication_convention': data.get('historical_boundary',
                                               'Dates identify the cited representative work.'),
        'replay': 'python3 ' + str(Path(__file__).relative_to(ROOT)),
        'replay_scope': 'Real-font overlay is deterministic; retained model artwork is nondeterministic.',
        'postprocessing': 'Typography only; no artwork editing, recoloring, tracing or repainting.',
        'source_sha256': {name: sha(HERE / name) for name in source_files},
        'assets_sha256': {name: sha(HERE / name) for name in
                          ['background.png', 'typography.png', 'labels.json', 'figure.png', 'prompt.txt']}})
    print(f"{data['key']}: {width_px}x{height_px}, {len(data['events'])} events, "
          f"{len(labels)} labels, annotation {annotation_pt:.2f} pt, "
          'no overlap or missing glyphs')


if __name__ == '__main__':
    main()
