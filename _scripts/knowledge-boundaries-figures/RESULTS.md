# Direct result figures

These assets replace the dropdown comparisons with results that can be read at a glance.

## Too Consistent to Detect

- Assets: `assets/img/project/knowledge-boundaries/results-too-consistent.svg` and `.pdf`.
- Source: [published EMNLP 2025 Table 2, PDF page 4](https://aclanthology.org/2025.emnlp-main.238.pdf#page=4).
- Values: `_data/knowledge_boundaries.json`, `self_consistent_errors.rows`.
- Setting: Qwen2.5-7B-Instruct / TriviaQA. All five selected methods are shown at once. Blue is inconsistent-error AUROC; rust is self-consistent-error AUROC. Numeric labels reproduce all four decimal places.
- The scale is explicitly **0.4–1.0**, with a dashed chance reference at 0.5. Connecting lines compare each method's scores on the two different subsets; they do not represent repeated measurements of the same questions. Training-free and supervised methods are identified separately.
- The cross-model row is the one immediately following Probe (ID), not Probe (OOD). Its external verifier is Qwen2.5-14B.
- The SVG uses system fonts; the corresponding PDF uses standard Helvetica fonts and retains vector marks.
- `results-too-consistent-mobile.svg` is a **440 × 760** portrait layout of the same five methods and all ten values. Each row keeps its full 0.4–1.0 comparison axis. Use it in a `<picture>` source on small screens; a maximum displayed width around 440 px avoids unnecessary enlargement. The portrait layout changes no values or method order.

## Beyond Reasoning

- Assets: `assets/img/project/knowledge-boundaries/results-beyond-reasoning-fig5.svg` and `.pdf`.
- Source: [arXiv:2605.07153v1 Figure 5, PDF page 7](https://arxiv.org/pdf/2605.07153v1#page=7).
- Extraction: export the original page's `/Im5` vector Form with its untouched bounding box (1363.2991 × 368.0825 pt), then convert with Poppler. No points, labels, values, colors, or curves are redrawn or estimated. Fonts become vector paths in the SVG.
- The three panels compare pre-RL/post-RL pass@k on Natural Questions, for Llama, OLMo, and Qwen. Pass@k measures whether a correct answer occurs within the sample budget; it is not majority-vote accuracy.
- The gap narrows at larger budgets, especially for Llama/OLMo; the Qwen gap remains visible at k=256. Do not claim complete convergence for every model or that this directly proves facts are stored in model parameters.
- The retained original is horizontal. The project page uses the vertical arrangement described below, with a linked vector PDF for enlargement.

### Vertical presentation

`reflow_passk.py` reads the retained original figure PDF and creates
`beyond-reasoning-fig5-stacked.pdf` and `.svg` on a 500 × 1023.0825 pt canvas.
The shared legend sits above Llama, OLMo, and Qwen. All panels use the same
426 pt crop width and 37 pt horizontal placement, giving balanced side gutters.
The common dataset and metric labels are moved into the page's figure caption;
they do not belong to the first model alone. The common sample-budget label
appears once below the bottom panel. Every curve, model title, tick, and original
y-axis range is retained without redrawing or rescaling inside the asset.

Source SVG-coordinate crops (`x, y, width, height`) and destination positions:

| Part | Source crop | Destination |
| --- | --- | --- |
| Legend | `525, 5, 310, 30` | `95, 12` |
| Llama | `74, 37, 426, 297` | `37, 54` |
| OLMo | `508.252761, 37, 426, 297` | `37, 365` |
| Qwen | `942.505522, 37, 426, 331.0825` | `37, 676` |

The Qwen crop extends 5.21 pt beyond the original canvas into blank space,
intentionally preserving the common panel width; no plotted content is lost.

After generating the original figure, run:

```sh
python3 /absolute/path/to/ict-star.github.io/_scripts/knowledge-boundaries-figures/reflow_passk.py
```

## Rebuild

Requires Python with `pypdf` and `reportlab`, plus Poppler's `pdftocairo`. Download the exact v1 primary PDF first, then run from any working directory:

```sh
python3 /absolute/path/to/ict-star.github.io/_scripts/knowledge-boundaries-figures/build_results.py \
  --beyond-pdf /absolute/path/to/beyond-reasoning-v1.pdf
```

Only the five assets listed above are rewritten. The JSON remains the single source of tabular values; the published vector Form remains the source for pass@k curves.
