# Reproduction

Model artwork was generated without text from prompt.txt and two topic-specific references. The original target is a factual source only. Later model revisions preserve the new geometry; see generation.json and prompt-02/03/04.

Run `python3 typeset.py` to reproduce the real-font transparent text layer and final figure.png. Fonts are repository files; only missing mathematical glyphs use STIX Two Math. Typesetting does not repaint the model background.

content.json preserves objects, roles, counts and allowed connections. references.json records the source commit and distinct reference roles. review.json reports visual and quantitative validation at a 164.6 mm book width.
