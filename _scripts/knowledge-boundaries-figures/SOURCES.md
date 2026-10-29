# Original paper figures

These are faithful exports of the original vector artwork, not recreated plots or simulated data. Text is converted to vector outlines by Poppler. The page supplies an accessible description and a linked source caption; the cropped PDF provides an enlargement view. No paper text, captions, colors, labels, or plotted values are rewritten inside the figures.

| Public asset stem | Primary source | Figure / PDF page | Extraction |
| --- | --- | --- | --- |
| `original-basecal-fig1` | [BaseCal, ACL 2026](https://aclanthology.org/2026.acl-long.234.pdf) | Fig. 1 / page 1 (proceedings p. 5172) | Page crop `(305.5, 512, 524, 624)` in PDF points; 218.5 × 112 pt. |
| `original-taps-fig1` | [TAPS, arXiv 2610.16318v2](https://arxiv.org/pdf/2610.16318v2) | Fig. 1 / page 2 | Export the page's original `/Im1` vector Form with its original bounding box, 555.400625 × 473.116531 pt. |
| `original-blinded-fig2` | [Blinded by Generated Contexts, ACL 2024](https://aclanthology.org/2024.acl-long.337.pdf) | Fig. 2 / page 3 (proceedings p. 6209) | Page crop `(70, 632, 524, 773)` in PDF points; 454 × 141 pt. |
| `blinded-fig2-stacked` | Same original Fig. 2 | Panels (a), (b), then (c) | Original AB crop `(70, 632, 298, 773)` plus C crop `(308, 646, 524, 758)`, translated onto a 228 × 263 pt canvas. No scaling or redrawing inside the asset. |

Crop coordinates use PDF's bottom-left origin: `(left, bottom, right, top)`. Each asset stem has both `.pdf` and `.svg` exports.

## Interpretation

- **BaseCal:** Original reliability diagrams for OLMo2-7B Base and Instruct on TriviaQA. ECE is 0.044 and 0.212 respectively. The figure diagnoses calibration before the proposed calibration method; it is not a before/after BaseCal result. The diagonal indicates perfect calibration, with bars below it denoting overconfidence. These values do not establish that the base model is more accurate.
- **TAPS:** Original empirical risk–coverage curves for Qwen3-8B on Natural Questions, comparing post-hoc selective answering with a probe, TAPS with a probe, and one operating point from TruthRL. The dashed vertical line makes a matched-coverage comparison. This is one setting, not a guarantee that TAPS dominates every method at every coverage. Risk is error rate among answered questions; coverage is the fraction answered. The source is explicitly arXiv **v2**, revised 2026-10-26.
- **Blinded:** The original three-protocol example compares retrieved, generated, and combined contexts for the Bermuda Winter Olympics question. Generated context is distinct from parametric knowledge; the paper studies preference between supplied context sources.

## Rebuild

Install `pypdf` and Poppler (`pdftocairo`) if they are not already available. Place the three primary PDFs in a directory with these names:

```text
basecal.pdf
taps-v2.pdf
blinded.pdf
```

From any working directory, run:

```sh
python3 /absolute/path/to/ict-star.github.io/_scripts/knowledge-boundaries-figures/extract_originals.py --source-dir /absolute/path/to/papers
```

The extraction command rewrites only the six original assets. Source PDFs are not committed to the repository. The `_scripts/knowledge-boundaries-figures/` directory is a development source directory and should be excluded from Jekyll output.

For the vertically arranged Blinded figure, first create the original assets, then run:

```sh
python3 /absolute/path/to/ict-star.github.io/_scripts/knowledge-boundaries-figures/reflow_blinded.py
```

This separate command reads the retained original figure PDF and creates only
`blinded-fig2-stacked.pdf` and `.svg`. Panel C is centered below the existing AB
block with a 10 pt gap. All original glyphs, arrows, colors, and labels are retained.
