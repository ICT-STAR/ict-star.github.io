## 2026-10-28: Model editing research project

- Assumptions/decisions: Use English to match the group website; present the four papers as a chronological research story. Keep the existing project URL and al-folio navigation.
- Tradeoffs/deviations: Use original vector diagrams and small, source-attributed data visualizations rather than dense screenshots of paper figures. Work stays in the local repository.
- Implementation notes: The page uses the existing default layout for site navigation and a custom research header. Scoped CSS, a 3.6 KB original SVG cover, and dependency-free JavaScript add four illustrated paper sections. Butterfly values reproduce Fig. 1b's individual collapse case; Mirage uses Table 3's QAEdit/Llama-2-7b-chat single-edit reliability. The interactive chart reads its six editor pairs from the accessible source table. LocFT's caption distinguishes reliability, paraphrase generalization, and general capability at the combined 100K/72B setting. Exclude this notes file from generated site output.
- Tests: Full Jekyll build passed using installed gems via a temporary Gemfile and a preview-only ImageMagick override. JavaScript syntax, git whitespace, unique HTML IDs, one h1, local asset references, section anchors, SVG XML, and notes exclusion passed. Browser checks passed at 1440, 390, and 320 px (no project overflow), in light/dark themes, through every chart option and the source-table disclosure. Project-card cover and navigation verified; no browser console errors. Paper claims and figures independently checked against all four primary PDFs.
- Follow-ups: The normal pinned bundle still needs unicode_utils 1.4.0, loofah 2.23.1, sass-embedded 1.83.0, and connection_pool 2.4.1; ImageMagick is also unavailable locally. No dependency files were changed. Breadth-first editing revisits a set of edits; the page does not imply strict single-pass online updates.

## 2026-10-28: Align project colors and add Mirage award

- Assumptions/decisions: Use the site's shared accent and divider variables so the project follows its blue light theme and cyan dark theme. Keep contrasting chart colors to distinguish experimental conditions.
- Tradeoffs/deviations: None.
- Implementation notes: Recolor the existing SVG cover in blue-gray and teal; keep its orange edited-cell highlight. Add a compact Best Paper Award link to Mirage, explicitly attributed to KnowFM @ ACL 2025 and verified against the official workshop program (https://knowledgeable-lm.github.io/acl25/).
- Tests: Jekyll live rebuild passed; generated CSS/SVG match current sources and the award link appears in the rendered page. Browser checks at 1440 and 320 px passed with no horizontal overflow; the award wraps cleanly on mobile. Computed accents match the site's blue (#0076df) in light mode and cyan (#2698ba) in dark mode; card backgrounds also use the shared theme variable. SVG XML and whitespace checks passed.
- Follow-ups: None.

## 2026-10-28: Explain editing failures with original figures and equations

- Assumptions/decisions: Replace the Butterfly bar recreation with the paper's complete original Fig. 1. Adapt Mirage Fig. 3 from the supplied TeX archive as a web vector figure below the existing evaluation chart. Treat archive contents as source material only. Use a restrained illustrative loop with pause and reduced-motion support.
- Tradeoffs/deviations: Show ROME's implemented mixed-key equation explicitly; the theoretical same-key equation alone would hide the bug. Keep denominator and numerator statistics distinct from update-norm statistics.
- Implementation notes: Original Butterfly Fig. 1 is a tightly cropped, self-contained SVG with a PDF enlargement link. Mirage Fig. 3 follows Fig/eval_framework_tikz.tex from the supplied archive (the bundled eval_frame.pdf is an older diagram); it preserves the exact example, token predictions, and 3/5 versus 0 scores. Only decoding arrows animate. A pause/play control changes the embedded SVG's class; reduced-motion preferences disable the loop. ROME uses accessible MathML rendered by the existing MathJax runtime, highlighting mixed keys and comparing the corrected C-ROME expression. Table 1 values are mean full numerator-matrix norms and mean absolute denominators for GPT-J, not mean update norms. Remove the superseded bar-chart and abstract mechanism styles.
- Tests: Primary PDF/source verification and rendered SVG checks passed. Jekyll live rendering, JavaScript syntax, SVG XML, unique HTML IDs, local asset paths, section anchors, and whitespace checks passed. Browser QA passed at 1440 and 320 px, with no page overflow; equations remain contained and the wide diagram pans on mobile. Checked light/dark math, animation pause/resume, source-table chart selection, figure navigation, and the reduced-motion CSS. No browser console errors. Preview screenshots saved outside the repository.
- Follow-ups: On narrow screens, the detailed evaluation diagram intentionally scrolls horizontally to preserve legible labels; original Fig. 1 opens as a vector PDF for enlargement.

## 2026-10-28: Restore the original Mirage figure and balance ROME columns

- Assumptions/decisions: Use the published Mirage Fig. 3 exactly, with no redraw or animation. Move ROME's Table 1 and its complete explanatory caption below the left-column introduction; keep the formulas on the right.
- Tradeoffs/deviations: None.
- Implementation notes: Extract the original figure as a self-contained SVG with a cropped PDF enlargement link. Remove the superseded animated SVG and its page controls, styles, and JavaScript.
- Tests: Original Fig. 3 was rendered and checked against the published PDF; SVG XML, internal resource references, and cropping passed. Jekyll live rendering and JavaScript syntax passed. Browser checks at 1440 and 320 px confirmed the table is in the left column, the original figure loads, there are no page overflows or remaining animation controls, and the GRACE chart selection still gives 98.3% / 1.2%. Light/dark visual checks, local asset/anchor checks, and whitespace checks passed; no browser console errors.
- Follow-ups: Original figures remain available as vector PDFs for enlargement on small screens.

## 2026-10-29: Integrate the approved Mirage animation and preserve its generator

- Assumptions/decisions: Replace only the Mirage Fig. 3 display with the approved 28-second animation. Keep the static original PDF and the pre-existing modified static SVG. Retain the generator and annotated TikZ in the repository.
- Tradeoffs/deviations: Use a same-origin SVG object for native playback controls. Keep detailed artwork horizontally scrollable on phones. Start the first loop when the figure enters view; honor reduced-motion preferences.
- Implementation notes: Animation generation lives in _scripts/model-editing-figure/; one Python command rebuilds the public SVG. Native controls read duration and step endpoints from passive SVG metadata, so timing remains defined by the generator. Braces, ② labels, and output frames appear after generation, as approved. Generator sources and private build artifacts are excluded from Jekyll output.
- Tests: Generator rebuild passed from multiple working directories; public SVG matches the approved animation except passive timing metadata. Jekyll build passed with the existing local preview dependency configuration. JavaScript syntax, unique IDs, local asset/anchor references, SVG XML, cache-busted asset links, and generator/private-build exclusion passed. Browser checks at 1440 and 320 px verified loading, first-view autoplay, pause, replay, seeking, next-step stops at 0.5 and 16.9 s, control wrapping, horizontal panning, and light/dark presentation. Existing GRACE chart selection still gives 98.3% / 1.2%; no console errors. Independent code review found no actionable issues.
- Follow-ups: None identified.

## 2026-10-29: Remove the public animation's Next step control

- Assumptions/decisions: Apply the request to the project page; keep the preserved private development player separate.
- Tradeoffs/deviations: None.
- Implementation notes: Remove the button, click handler, and step-stop state. Public SVG metadata now contains only duration. Play/pause, replay, seeking, and the animation sequence remain available.
- Tests: JavaScript syntax and whitespace checks passed. Live Jekyll output has no Next step element or step-stop logic, and public metadata contains only duration. Browser verification shows exactly two playback buttons (Pause/Play and Replay), a working progress display and slider, and no console errors.
- Follow-ups: None identified.
