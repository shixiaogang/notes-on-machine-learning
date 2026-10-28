#!/usr/bin/env python3
"""Typeset retained history artwork; never regenerate or repaint the model background."""
from pathlib import Path
import hashlib
import json
import shutil
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
FONT_NAMES = {
    "primary": "SourceHanSansSC-Normal.otf",
    "annotation": "LXGWWenKai-Regular.ttf",
    "latin": "FiraMath-Regular.otf",
}
FONT_LICENSES = {
    "primary": "SourceHanSans-OFL.txt",
    "annotation": "LXGWWenKai-OFL.txt",
    "latin": "FiraMath-README.md",
}
INK = "#3B4252"
MUTED = "#6B7280"
COLORS = ["#A7787D", "#7188A3", "#829C8B", "#B4A16F", "#9588A5", "#829C8B"]
EVENTS = [
    ("1805–1886", "从观测误差到回归",
     ["1805 Legendre：最小二乘", "1809 Gauss：误差的概率解释", "1886 Galton：亲子身高与回归"]),
    ("1901–1948", "从几何压缩到类别判别",
     ["1901 Pearson、1933 Hotelling：主成分", "1936 Fisher：线性判别", "1948 Rao：多总体判别"]),
    ("1964–1979", "非线性表示与局部规律",
     ["1964 势函数；1967 近邻理论、K-means", "1972 GLM；1977 EM", "1979 Cleveland：局部加权平滑"]),
    ("1984–1991", "由数据选择分区与曲线",
     ["1984 CART：递归分裂与剪枝", "1986 GAM：平滑函数相加", "1991 MARS：铰链基函数与交互"]),
    ("1995–1997", "容许误差、聚合预测与密度连接",
     ["1995 Cortes / Vapnik：支持向量网络", "1996 Bagging、DBSCAN", "1997 Freund / Schapire：AdaBoost"]),
    ("2001", "以不同方式组合多棵树",
     ["Breiman：随机森林", "Friedman：梯度提升", "随机化减小相关性；逐轮修正当前误差"]),
]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

def draw_label(draw, text, xy, size, role, color):
    x, y = xy
    baseline = y + size
    start_x = x
    boxes = []
    for char in text:
        font_role = "latin" if ord(char) < 128 or char in "–" else role
        path = ROOT / "fonts" / FONT_NAMES[font_role]
        font = ImageFont.truetype(str(path), size)
        cmap = FONT_CMAPS[font_role]
        if ord(char) not in cmap:
            raise ValueError(f"Missing glyph {char!r} in {path.name}")
        bbox = draw.textbbox((x, baseline), char, font=font, anchor="ls")
        draw.text((x, baseline), char, font=font, fill=color, anchor="ls")
        if char != " ":
            boxes.append(bbox)
        x += draw.textlength(char, font=font)
    bbox = [min(b[0] for b in boxes), min(b[1] for b in boxes),
            max(b[2] for b in boxes), max(b[3] for b in boxes)]
    return {"text": text, "xy": [start_x, y], "size_px": size,
            "role": role, "color": color, "bbox": bbox}

FONT_CMAPS = {role: TTFont(ROOT / "fonts" / name).getBestCmap()
              for role, name in FONT_NAMES.items()}

def main():
    background = Image.open(HERE / "background.png").convert("RGBA")
    width, height = background.size
    # Coordinates were inspected against this retained background. Scaling is
    # typography placement only; the background pixels remain unchanged.
    sx, sy = width / 1122, height / 1402
    overlay = Image.new("RGBA", background.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    labels = []
    for i, (date, title, lines) in enumerate(EVENTS):
        x = 26 if i % 2 == 0 else 590
        y = [80, 292, 515, 725, 936, 1145][i]
        specs = [(date, x, y, 35, "primary", COLORS[i]),
                 (title, x, y + 46, 21, "primary", INK)]
        specs += [(line, x, y + 80 + 26*j, 20, "annotation", MUTED)
                  for j, line in enumerate(lines)]
        for text, tx, ty, size, role, color in specs:
            labels.append(draw_label(draw, text, (round(tx*sx), round(ty*sy)),
                                     round(size*sx), role, color))
    for label in labels:
        x0, y0, x1, y1 = label["bbox"]
        if not (0 <= x0 < x1 <= width and 0 <= y0 < y1 <= height):
            raise ValueError(f"Label outside canvas: {label['text']}")
    collisions = []
    for i, a in enumerate(labels):
        for b in labels[i+1:]:
            x0, y0, x1, y1 = a["bbox"]
            u0, v0, u1, v1 = b["bbox"]
            if max(x0, u0) < min(x1, u1) and max(y0, v0) < min(y1, v1):
                collisions.append([a["text"], b["text"]])
    if collisions:
        raise ValueError(f"Label overlap: {collisions}")
    overlay.save(HERE / "typography.png")
    Image.alpha_composite(background, overlay).convert("RGB").save(HERE / "figure.png")
    save_json(HERE / "labels.json", {"canvas_px": [width, height], "labels": labels})
    font_info = [{"role": role, "path": f"fonts/{name}",
                  "sha256": digest(ROOT / "fonts" / name),
                  "license": f"fonts/licenses/{FONT_LICENSES[role]}",
                  "license_sha256": digest(ROOT / "fonts" / "licenses" / FONT_LICENSES[role])}
                 for role, name in FONT_NAMES.items()]
    save_json(HERE / "font-provenance.json", {"fonts": font_info,
              "artificial_bold": False, "missing_glyphs": []})
    save_json(HERE / "typography-check.json", {
        "canvas_px": [width, height], "label_count": len(labels),
        "outside_canvas": [], "label_overlap": [], "missing_glyphs": [],
        "body_width_mm": 157.406, "minimum_annotation_pt": 20 * (157.406/25.4) * 72/1122,
        "year_pt": 35 * (157.406/25.4) * 72/1122,
        "year_hierarchy": "Enlarged dates follow the user's timeline design reference.",
        "artwork_collision_check": "Visual review at the retained background and book size required.",
    })
    save_json(HERE / "generation.json", {
        "key": HERE.name, "route": "generated", "date": "2026-10-12",
        "tool": "image_gen.imagegen", "model": "not exposed by built-in tool",
        "prompt": "prompt.txt", "references": "references/sources.json",
        "body_owner": "tex/07-classic-models/01-overview.tex",
        "label": "fig:classic-models-history",
        "replay": "python3 figures/07-classic-models/00-shared/generated/classic-models-history/typeset.py",
        "replay_scope": "Real-font overlay on retained generated background; model generation is nondeterministic.",
        "postprocessing": "Typography only; background pixels are not repainted.",
        "source_sha256": {"typeset.py": digest(Path(__file__))},
        "assets_sha256": {name: digest(HERE / name) for name in
            ["background.png", "typography.png", "labels.json", "figure.png", "prompt.txt"]},
    })
    print(f"{HERE.name}: {len(labels)} labels, no missing glyphs, no label overlaps")

if __name__ == "__main__":
    main()
