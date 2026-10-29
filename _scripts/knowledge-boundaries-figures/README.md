# Knowledge-boundaries project artwork

The cover is an original conceptual vector illustration for the research thread
*From Latent Knowledge to Reliable Answers*. It follows the site's blue accent,
with muted teal and rust for the three possible response actions.

The shapes, fragments, and assessment lines are schematic. They are not sampled
model outputs or measurements from any paper. No scores or experimental values
are encoded in the artwork.

Rebuild from any working directory with Python's standard library:

```sh
python3 /absolute/path/to/ict-star.github.io/_scripts/knowledge-boundaries-figures/generate.py
```

Output: `assets/img/project/cover/knowledge-boundaries.svg`.

The SVG is self-contained and uses system fonts. Its fixed light background
keeps the artwork readable when embedded in either site theme.

## Other assets and research metadata

- `extract_originals.py` and [SOURCES.md](SOURCES.md): original paper figures and their exact crops.
- `reflow_blinded.py`: move original panel (c) beneath (a,b) without redrawing the figure.
- `reflow_passk.py`: stack the original Llama, OLMo, and Qwen panels with aligned axes and their shared legend.
- `build_results.py` and [RESULTS.md](RESULTS.md): direct result figures, including the mobile detection plot.
- `build_knowledge_use.py`: the Knowledgeable-R1 training schematic and its scoped Table 2 result.
- `build_research_summary.py`: the public Markdown overview, generated from `_data/knowledge_publications.json`.
- `build_social.py`: the 1200 × 630 social preview image.

The two standard-library generators run from any working directory:

```sh
python3 /absolute/path/to/ict-star.github.io/_scripts/knowledge-boundaries-figures/build_knowledge_use.py
python3 /absolute/path/to/ict-star.github.io/_scripts/knowledge-boundaries-figures/build_research_summary.py
```

The locally adapted TAPS interaction, unchanged empirical data, source attribution,
and MIT license live in `assets/knowledge-boundaries/taps-demo/`.
