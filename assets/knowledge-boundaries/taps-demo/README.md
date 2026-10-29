# TAPS interactive result, locally embedded

Adapted from [Junwei Zhang and collaborators' original TAPS project page](https://zhangjunwei0233.github.io/projects/taps/), retrieved 2026-10-29.

Primary source files:

- `https://zhangjunwei0233.github.io/projects/taps/` — original hero SVG paths, legend, slider, and readouts.
- `https://zhangjunwei0233.github.io/projects/taps/curves.js` — empirical curves and five fixed abstention-training points.
- `https://zhangjunwei0233.github.io/projects/taps/chart.js` — original interaction and animation behavior.
- [Author's source repository](https://github.com/zhangjunwei0233/zhangjunwei0233.github.io), distributed under the included MIT `LICENSE`.

The two curves contain all **3,138** coverage counts from the author's Qwen3-8B / Natural Questions result. `curves.js` is copied byte for byte, SHA-256 `cc3c674c835c7206b123911a81b9eee8bb18c2c9f039e3844b9d7c43c57e7e85`. SVG curve paths and fixed points are also retained. The module does not synthesize a curve from paper table values.

Local adaptations are limited to al-folio colors, responsive typography, an explicit play/pause control, and iframe integration. The original 12-second sweep, 12%–88% automatic coverage range, point snapping within 0.55 percentage points, manual exploration, and reduced-motion preference are retained. Pointer or keyboard interaction pauses automatic playback. A fixed baseline is shown only when a recorded operating point lies near the selected coverage; it is not extrapolated to other coverages.

## Embed

```html
<iframe src="/assets/knowledge-boundaries/taps-demo/index.html"
        title="TAPS interactive risk–coverage results"
        width="100%" height="700" loading="lazy"></iframe>
```

The module follows its same-origin parent's `data-theme` attribute automatically. A standalone preview also supports `?theme=dark`.

It posts `{type: "knowledge-boundaries:taps-height", height: <pixels>}` to its same-origin parent whenever content height changes. The parent should verify both `event.origin === location.origin` and `event.source === iframe.contentWindow` before applying the height. Natural height follows the available width; use the event rather than a fixed aspect ratio, because labels and controls also need space.

The parent can additionally send `{type: "knowledge-boundaries:taps-theme", theme: "light" | "dark"}`. On iframe load, it can send `{type: "knowledge-boundaries:taps-request-height"}` to force a fresh height reply even when the initial automatic message was missed. All fonts, data, styles, and scripts are local; the only external URL is the visible attribution link.
