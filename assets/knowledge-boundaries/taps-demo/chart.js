/* Adapted from Junwei Zhang's TAPS project chart.js (MIT; see LICENSE).
 * Original data, sample-count slider, snapping, and 12-second sweep are retained.
 * Additions: explicit playback control, al-folio theme sync, iframe height events.
 */
(() => {
  "use strict";
  const data = window.PROJECT_CHART;
  const slider = document.getElementById("coverage");
  const toggle = document.getElementById("animation-toggle");
  const fixedRisk = document.getElementById("abstention-risk");
  const highlight = document.getElementById("baseline-highlight");
  const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)");
  const x = (coverage) => 75 + 6.78 * coverage;
  const y = (risk) => 440 - 5.6 * risk;
  const nearest = (coverage) => {
    const point = data.points.reduce((best, item) =>
      !best || Math.abs(item.coverage - coverage) < Math.abs(best.coverage - coverage) ? item : best, null);
    return point && Math.abs(point.coverage - coverage) <= 0.55 ? point : null;
  };

  function update() {
    const index = Math.max(0, Math.min(data.count - 1, Number(slider.value) - 1));
    const coverage = (index + 1) / data.count * 100;
    const selective = data.curves[0][index];
    const taps = data.curves[1][index];
    const point = nearest(coverage);
    const fixedLabel = point
      ? `${point.label} risk ${point.risk.toFixed(1)} percent at ${point.coverage.toFixed(2)} percent coverage`
      : "no abstention-training point nearby";
    document.getElementById("coverage-value").textContent = `${coverage.toFixed(2)}%`;
    slider.setAttribute("aria-valuetext", `${coverage.toFixed(2)} percent coverage; TAPS risk ${taps.toFixed(1)} percent; selective answering risk ${selective.toFixed(1)} percent; ${fixedLabel}`);
    document.getElementById("selective-risk").innerHTML = `${selective.toFixed(1)}<small>%</small>`;
    document.getElementById("taps-risk").innerHTML = `${taps.toFixed(1)}<small>%</small>`;
    fixedRisk.innerHTML = point ? `${point.risk.toFixed(1)}<small>%</small>` : "—";
    fixedRisk.title = point ? `${point.label} at ${point.coverage.toFixed(2)}% coverage` : "No abstention-training point at this coverage";
    highlight.setAttribute("opacity", point ? "1" : "0");
    if (point) {
      highlight.setAttribute("cx", x(point.coverage));
      highlight.setAttribute("cy", y(point.risk));
    }
    const guide = document.getElementById("chart-guide");
    guide.setAttribute("x1", x(coverage));
    guide.setAttribute("x2", x(coverage));
    for (const [name, risk] of [["selective", selective], ["taps", taps]]) {
      const marker = document.getElementById(`${name}-point`);
      marker.setAttribute("cx", x(coverage));
      marker.setAttribute("cy", y(risk));
    }
    document.getElementById("chart-desc").textContent = `Risk versus coverage on Qwen3-8B / NQ. At ${coverage.toFixed(2)} percent coverage, selective answering has ${selective.toFixed(1)} percent risk and TAPS has ${taps.toFixed(1)} percent risk; ${fixedLabel}. Squares are fixed abstention-trained models.`;
  }

  slider.max = data.count;
  slider.min = Math.ceil(data.count / 100);
  slider.value = data.initial;
  document.querySelector(".coverage-control").hidden = false;
  update();

  let playing = !reduceMotion.matches;
  let keyboard = false;
  let visible = false;
  let elapsed = 0;
  let previous = 0;
  let phase = Math.asin((data.initial / data.count * 100 - 50) / 38);
  function setPlaying(value) {
    playing = value;
    toggle.textContent = playing ? "Pause animation" : "Play animation";
    toggle.setAttribute("aria-pressed", String(playing));
    if (playing) {
      phase = Math.asin(Math.max(-1, Math.min(1, (Number(slider.value) / data.count * 100 - 50) / 38)));
      elapsed = 0;
    }
  }
  toggle.addEventListener("click", () => setPlaying(!playing));
  slider.addEventListener("pointerdown", () => { keyboard = false; setPlaying(false); });
  slider.addEventListener("focus", () => setPlaying(false));
  slider.addEventListener("keydown", () => { keyboard = true; setPlaying(false); });
  slider.addEventListener("keyup", () => { keyboard = false; });
  slider.addEventListener("input", () => {
    setPlaying(false);
    const point = nearest(Number(slider.value) / data.count * 100);
    if (point && !keyboard) slider.value = point.count;
    update();
  });
  reduceMotion.addEventListener("change", () => { if (reduceMotion.matches) setPlaying(false); });
  new IntersectionObserver((entries) => { visible = entries[0].isIntersecting; }, { threshold: 0.01 })
    .observe(document.querySelector(".hero-result"));
  function tick(time) {
    const delta = previous ? Math.min(time - previous, 64) : 0;
    previous = time;
    if (playing && visible && !document.hidden) {
      elapsed += delta;
      slider.value = Math.round((50 + 38 * Math.sin(phase + elapsed / 12000 * Math.PI * 2)) / 100 * data.count);
      update();
    }
    requestAnimationFrame(tick);
  }
  setPlaying(playing);
  requestAnimationFrame(tick);

  // This locally embedded chart follows the same-origin al-folio theme.
  function setTheme(theme) {
    document.documentElement.dataset.theme = theme === "dark" ? "dark" : "light";
  }
  if (parent !== window) {
    const parentRoot = parent.document.documentElement;
    const sync = () => setTheme(parentRoot.dataset.theme);
    sync();
    new MutationObserver(sync).observe(parentRoot, { attributes: true, attributeFilter: ["data-theme"] });
  } else {
    const requested = new URLSearchParams(location.search).get("theme");
    setTheme(requested || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light"));
  }
  addEventListener("message", (event) => {
    if (event.source !== parent || event.origin !== location.origin) return;
    if (event.data?.type === "knowledge-boundaries:taps-theme") setTheme(event.data.theme);
    if (event.data?.type === "knowledge-boundaries:taps-request-height") reportHeight(true);
  });
  let lastHeight = 0;
  function reportHeight(force = false) {
    const height = Math.ceil(document.body.getBoundingClientRect().height) + 2;
    if ((force || height !== lastHeight) && parent !== window) {
      lastHeight = height;
      parent.postMessage({ type: "knowledge-boundaries:taps-height", height }, location.origin);
    }
  }
  new ResizeObserver(() => reportHeight()).observe(document.body);
  addEventListener("load", () => reportHeight());
})();
