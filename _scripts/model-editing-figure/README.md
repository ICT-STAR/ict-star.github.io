# Mirage Figure 3 animation

This generator preserves the paper's TikZ artwork and font outlines while progressively revealing the two evaluation procedures. The public SVG is self-contained and script-free; its 28-second SMIL animation loops automatically and respects reduced-motion preferences.

From the repository root:

```sh
python3 _scripts/model-editing-figure/build_animation.py
```

Only the Python standard library is needed. This command updates `assets/img/project/model-editing/mirage-fig3-animated.svg` and writes a private standalone player, timeline data, and inspection SVGs to the ignored `build/` directory. No preview HTML, build data, or TeX auxiliaries need committing.

## Editing

- `build_animation.py`: timing, reveal order, arrow-growth masks, reduced-motion behavior, and private-player step endpoints.
- `source/semantic-base.svg`: original artwork with named layers, compiled from the annotated TikZ.
- `source/Fig/eval_framework_tikz.tex`: original drawing with semantic SVG grouping annotations.
- `source/main.tex`: the paper's 11pt ACL and font context, using the native dvisvgm driver.
- `source/color.tex` and `source/acl.sty`: preserved source dependencies.
- `source/annotation-map-source.json`: correspondence between layers and TikZ commands.
- `source/player-template.html`: standalone development player with Chinese phase narration.

The diagram reproduces the paper's fixed example, not live model inference. Synthetic evaluation receives reference tokens; WILD receives its own previous predictions. Output words appear after their arrows. Summary braces, circled ② labels, output frames, and the left reference frame appear at 16.65 s, after all five outputs finish at 16.47 s. WILD's reference appears only during scoring at 18.5 s. The final metrics are position-wise `3/5` and whole-answer judgment `0`.

The public SVG includes passive metadata with ID `animation-timing` containing JSON `{duration}`. The project page uses this for playback and seeking; step endpoints remain available only in the private development player.

## Recompile the artwork after a TikZ edit

With TeX Live/MacTeX, TikZ, Times, Inconsolata, Dingbats, FontAwesome5, and dvisvgm installed:

```sh
cd _scripts/model-editing-figure/source
latex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
dvisvgm --no-fonts --bbox=min --output=semantic-base.svg main.dvi
cd ..
python3 build_animation.py
```

The source retains semantic group names for inputs, outputs, feedback, summaries, stopping, and metrics. Keep these names when changing the artwork. The animation builder also identifies the original unnamed synthetic metric marker and EOS background by their vector references; review those selectors if recompilation changes glyph IDs or path geometry. Native-DVI metadata warnings are harmless for the preserved drawing, but visually inspect the regenerated complete state and arrow paths after changing TikZ or fonts.
