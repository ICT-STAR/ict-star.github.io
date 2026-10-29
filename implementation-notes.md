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

## 2026-10-29: Knowledge boundaries and uncertainty research project

- Assumptions/decisions: Use English to match the website. Present eight studies as a shared research agenda: an opening diagnosis followed by Access, Assess, and Act. Mark both arXiv works as preprints and keep calibration distinct from error discrimination.
- Tradeoffs/deviations: Use source-table interactions for recall and detection; retain original vector figures for calibration and selective answering rather than inventing continuous curves. Conceptual diagrams are explicitly identified.
- Implementation notes: Add a new collection page and cover without changing the model-editing project. Scoped styles inherit al-folio typography and theme variables. Jekyll renders accessible chart tables from one JSON data file; dependency-free JavaScript reads those same tables. Preserve vector generation/extraction sources and exclude the source directory from the generated website.
- Tests: Full Jekyll build passed using the existing local compatibility Gemfile and ImageMagick override. JavaScript syntax, whitespace, unique IDs, one h1, local assets/anchors, project-list integration, and source-directory exclusion passed. Browser QA passed at 1280, 390, and 320 px with no page overflow, in light and dark themes; all 12 recall pairs and five detection options returned the original values, including SimpleQA decreases. Verified native source-table expansion on a 320 px screen, figure loading, and original vector rendering. No browser console warnings/errors. Independent scientific and implementation reviews found no actionable issues.
- Follow-ups: The local compatibility build retains the previously documented dependency limitations; no dependency files were changed.

## 2026-10-29: Refine the knowledge research page and its discoverability

- Assumptions/decisions: Treat the editing page as an example of a Jekyll project file, not a visual template. Use an editorial overview with a single integrated subtitle, full linked paper titles, larger direct results, and different compositions for different research questions.
- Tradeoffs/deviations: Replace the two dropdown charts with complete static result figures. Keep the original pass@k figure and redraw verified detection values; provide a portrait detection view for phones. Reuse the student's TAPS interaction and empirical data locally, retaining MIT attribution and the original project links.
- Implementation notes: Add a single publication registry for visible headings, citations, JSON-LD, and a downloadable Markdown overview. Metadata is scoped to this project; canonical/title/description behavior remains native to al-folio. Knowledgeable-R1 combines an accurate three-view training schematic with a clearly scoped Table 2 result. Retain all figure generation code. The existing preview stays running for the user's review.
- Tests: Local compatibility build, JavaScript syntax, whitespace, unique IDs, all local asset/anchor references, and all eight full paper headings passed. JSON-LD parses into 12 unique entities with eight ScholarlyArticle records; canonical, OG/Twitter, and Markdown encoding use the production domain even in local preview. Browser checks passed at 1280, 390, and 320 px without page overflow, including portrait result artwork, native TAPS pause/slider interaction, automatic iframe height, and light/dark theme synchronization. At 50.45% coverage the retained empirical TAPS demo gives 41.3% / 37.3% / 33.3% risk as expected. No browser warnings/errors. Primary-paper and implementation reviews passed; original TAPS curves/SVG were verified unchanged. New CSS files pass the site's CSSminify2 compressor independently.
- Follow-ups: The existing 619 KB global stylesheet makes a separate full production-minification check slow; that check was stopped, while normal local builds and direct minification of new CSS passed. Search indexing and AI citation depend on external services; markup and crawlable sources make the content interpretable without promising ranking gains.

## 2026-10-29: Rebalance research figure scale and placement

- Assumptions/decisions: Put Too Consistent and TAPS copy to the left of proportionally smaller figures on desktop. Keep denser, multi-panel figures wider but cap their width separately. Stack these two studies below 1100 px to keep the figures legible.
- Tradeoffs/deviations: Preserve every plot's aspect ratio and the TAPS module's natural reported height. Move TAPS's interaction guide into the left text column instead of cropping or scaling its iframe.
- Implementation notes: Restrict detection and TAPS to approximately 620–650 px; cap Beyond Reasoning at 920 px and Knowledgeable-R1 at 940 px. Bring other figures into a 500–560 px supporting range. Keep full titles, source links, data, and structured metadata intact.
- Tests: Local compatibility Jekyll build and whitespace checks passed. Browser checks at 1280, 1024, and 320 px confirmed desktop side-by-side placement, responsive stacking, proportional image scaling, no page overflow, and a working portrait detection figure. TAPS resized naturally from 697 px high at 620 px wide to 528 px high at 290 px wide; pause and native slider controls still returned the expected 50.45% coverage comparison (41.3% / 37.3% / 33.3% risk). Eight complete paper headings, unique anchors, and all eight structured article records remain intact. No browser warnings/errors; independent DOM/CSS review passed.
- Follow-ups: None identified.

## 2026-10-29: Match TAPS illustration height to its copy

- Assumptions/decisions: Make the complete desktop TAPS figure approximately as tall as its left text, rather than merely reducing its maximum width. Remove the requested closing research-thread statement.
- Tradeoffs/deviations: Keep the plot's aspect ratio and automatic iframe height. Compact the module's text and spacing while retaining a separate phone typography rule; keep the original data and interaction unchanged.
- Implementation notes: Cap the TAPS figure at 480 px in both column and stacked layouts, balance its two columns within 1060 px, and move the static-paper resource disclosure into the text column. Remove the duplicate outer credit while retaining the author's visible module credit and project links. Delete the closing footer and its unused styles.
- Tests: Local compatibility build and whitespace checks passed. At 1280 px, the left copy measured 561 px high and the complete right figure 548 px high at 480 px wide. At 320 px, the iframe resized to 482 px with no page overflow; labels and all controls remained visible. Native pause/slider checks preserved the 50.45% coverage result (41.3% / 37.3% / 33.3% risk). Verified removal of the closing block and unused styles, valid unique anchors, and all eight structured paper records. No browser warnings/errors.
- Follow-ups: None identified.

## 2026-10-29: Stack the Blinded figure panels vertically

- Assumptions/decisions: Keep the existing (a,b) block intact and move (c) beneath it so the right-column figure can show larger lettering.
- Tradeoffs/deviations: Recompose cropped original vector panels rather than redraw them. Retain the unmodified original figure assets and paper citation.
- Implementation notes: Preserve a reproducible PDF-to-SVG reflow script and document exact panel bounds. The derived 228 × 263 pt asset places C below AB with a 10 pt gap.
- Tests: Original-panel bounds were independently checked. Render comparison after translation gives mean channel difference 0.0075/255, consistent with antialiasing; all arrows, text, and labels are retained. Deterministic rebuild from another working directory, SVG XML, no-raster check, local compatibility build, and whitespace checks passed. Browser QA confirmed the complete stacked figure at 400 px on desktop and 290 px on a 320 px screen, without page overflow.
- Follow-ups: None identified.

## 2026-10-29: Stack the factual-recall plots beside their explanation

- Assumptions/decisions: Place the full Beyond Reasoning text on the left and the three model plots in a vertical right-hand column.
- Tradeoffs/deviations: Retain original vector panels and unequal y-axis ranges, with a single shared legend. Move the result explanation to the text column rather than widen the portrait figure.
- Implementation notes: Preserve exact crop bounds and aligned plotting-area offsets in a standalone reflow script. Keep the original horizontal figure and link an enlarged vertical PDF from the page.
- Tests: Panel/legend crops and alignment offsets were independently verified; rendered results retain every original curve, tick, model title, and axis label. Deterministic rebuild from another working directory, valid SVG XML, no-raster/external-reference checks, local compatibility build, whitespace, unique IDs, and eight structured paper records passed. Browser QA at 1280 px measured left text at 564 px and the portrait figure at 587 px; at 320 px the figure stayed at 280 px with no horizontal overflow. Obsolete horizontal-pan guidance and unused figure-heading styles were removed.
- Follow-ups: None identified.

## 2026-10-29: Correct shared recall-figure labels and balance its frame

- Assumptions/decisions: Natural Questions is the common dataset for all three model panels. Move the dataset and shared metric label into one caption beneath the complete figure.
- Tradeoffs/deviations: Keep original curves, titles, ticks, and individual y-axis ranges. Show the shared sample-budget label once below the last panel.
- Implementation notes: Crop out the first panel's shared labels, use equal-width panel crops with symmetric horizontal padding, and add top/bottom breathing room. Constrain the complete study to a centered 960 px frame with equal columns and the same 64 px gap used by TAPS.
- Tests: Independent review confirmed shared-label removal, full tick preservation, one common x-axis label, and 43/49 pt visible side gutters. Deterministic export, self-contained SVG/no raster, local compatibility build, whitespace, and caption-link checks passed. Browser QA at 1280 px verified the centered 960 px block, common caption, and 591/652 px text/figure heights; at 320 px it stacks correctly with a 290 px figure and no page overflow. Original curves and individual y-axis ranges remain unchanged.
- Follow-ups: None identified.
