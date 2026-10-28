# Historical candidate source. For current publication output, use the canonical replay_labels.py command in generation.json.
"""Read-only verification of text overlays and the model hierarchy.

No tracing, fill correction, or artwork generation is performed here.
"""
from pathlib import Path
import json
import numpy as np
from PIL import Image, ImageFilter

BASE = Path(__file__).resolve().parent

def check(p):
    labels = json.loads((p/'labels.json').read_text())
    content = json.loads((p/'content.json').read_text())
    rgb = np.array(Image.open(p/'background.png').convert('RGB')).astype(int)
    glyphs = np.array(Image.open(p/'text-layer.png'))[:, :, 3] > 64
    # Only colored dark outlines/icons are included, not pale fill regions.
    edges = (rgb.min(axis=2) < 170) & ((rgb.max(axis=2)-rgb.min(axis=2)) > 55)
    intersections = glyphs & edges
    overlaps = []
    for i, label in enumerate(labels):
        x1, y1, x2, y2 = label['boxes'][0]
        for j, other in enumerate(labels[i+1:], i+1):
            u1, v1, u2, v2 = other['boxes'][0]
            if min(x2, u2) > max(x1, u1) and min(y2, v2) > max(y1, v1):
                overlaps.append([i, j])
    edge_image = Image.fromarray((edges*255).astype('uint8'))
    margins = {}
    for distance in [1, 2, 3, 4, 5, 6, 8, 10]:
        nearby = np.array(edge_image.filter(ImageFilter.MaxFilter(distance*2+1))) > 0
        margins[str(distance)] = int((nearby & glyphs).sum())
    leaves = [label for label in labels if label.get('role') == 'leaf']
    child_counts = [sum(label['parent_index'] == i for label in leaves) for i in range(8)]
    expected = [value for questions in content['leaves'].values() for value in questions]
    actual = [''.join(segment['text'] for segment in label['segments']) for label in leaves]
    colors = {}
    samples = {
        'white_top_left': (20,20,100,100),
        'blue_inner': (690,390,730,420), 'blue_middle': (780,245,805,270),
        'blue_outer': (645,115,680,145), 'green_inner': (660,770,685,790),
        'green_middle': (650,950,680,980), 'green_outer': (635,1090,660,1110),
        'peach_inner': (480,395,505,420),
    }
    for name, (x1,y1,x2,y2) in samples.items():
        region = rgb[y1:y2, x1:x2]
        colors[name] = dict(min=region.min(axis=(0,1)).tolist(),
                            max=region.max(axis=(0,1)).tolist(),
                            std=region.std(axis=(0,1)).round(2).tolist())
    result = dict(
        label_count=len(labels), hierarchy_tiers=3, major_themes=3,
        parent_branches=8, finer_questions=len(leaves),
        child_count_by_parent=child_counts, outer_gaps_parent_indices=[2,5,7],
        all_leaf_labels_retained=sorted(actual)==sorted(expected),
        label_pair_overlap=overlaps,
        text_graphic_pixels_intersection=int(intersections.sum()),
        colored_edge_threshold='RGB minimum <170 and channel range >55; glyph alpha >64',
        edge_proximity_pixels_by_distance=margins, color_samples=colors,
        title_adjustment=dict(themes_second_center_x_previous=740,
                              themes_second_center_x_current=680,
                              delta_x_pixels=-60),
        topology_review='Manual visual count of three bands and fifteen cells, plus original source hierarchy verification.',
    )
    (p/'visual-placement-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    assert not overlaps and not intersections.any()
    assert margins['6']==0
    assert sorted(actual)==sorted(expected)
    assert child_counts==[3,3,0,3,3,0,3,0]
    print(p.name, len(leaves), 'leaves; no overlap; at least 6 px edge clearance')

if __name__ == '__main__':
    paths = [BASE] if (BASE/'background.png').exists() else [BASE/key for key in ['learning-theory-map','trustworthiness-map']]
    for path in paths:
        check(path)
