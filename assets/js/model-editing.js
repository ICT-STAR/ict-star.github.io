// The Mirage of Model Editing, Table 3: QAEdit / Llama-2-7b-chat / single-edit reliability.
// Read the per-editor values from the visible source table to keep one source of truth.
(() => {
  const figure = document.getElementById("me-evaluation");
  const editor = document.getElementById("me-editor");
  const rows = [...figure.querySelectorAll("tbody tr")];
  const keys = ["ftm", "mend", "rome", "memit", "grace", "wise"];
  const values = { mean: [96.8, 38.5] };
  rows.forEach((row, index) => {
    values[keys[index]] = [...row.querySelectorAll("td")].map((cell) => Number(cell.textContent));
  });

  editor.addEventListener("change", () => {
    const [synthetic, wild] = values[editor.value];
    document.getElementById("me-synthetic-value").textContent = `${synthetic.toFixed(1)}%`;
    document.getElementById("me-wild-value").textContent = `${wild.toFixed(1)}%`;
    document.getElementById("me-synthetic-bar").style.width = `${synthetic}%`;
    document.getElementById("me-wild-bar").style.width = `${wild}%`;
    figure.querySelector(".me-comparison").setAttribute("aria-label",
      `${editor.selectedOptions[0].textContent}: synthetic evaluation ${synthetic} percent, WILD evaluation ${wild} percent.`);
    document.getElementById("me-gap").innerHTML =
      `<strong>${(synthetic - wild).toFixed(1)} percentage points</strong> between the two evaluations.`;
  });

  const animationObject = document.getElementById("me-mirage-animation");
  const controls = document.getElementById("me-animation-controls");
  const play = document.getElementById("me-animation-play");
  const replay = document.getElementById("me-animation-replay");
  const progress = document.getElementById("me-animation-progress");
  const clock = document.getElementById("me-animation-time");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  let svg;
  let timing;
  let frame;
  let observer;
  let autoStartPending = true;

  function updatePlayback() {
    cancelAnimationFrame(frame);
    const time = svg.getCurrentTime() % timing.duration;
    play.textContent = svg.animationsPaused() ? "Play" : "Pause";
    progress.value = time;
    clock.textContent = `${time.toFixed(1)} / ${timing.duration}s`;
    if (!svg.animationsPaused()) frame = requestAnimationFrame(updatePlayback);
  }

  function manualPlayback() {
    autoStartPending = false;
    observer?.disconnect();
    svg.classList.add("motion-enabled");
  }

  function initializeAnimation() {
    const documentRoot = animationObject.contentDocument?.documentElement;
    if (documentRoot?.localName !== "svg" || documentRoot === svg) return;
    svg = documentRoot;
    timing = JSON.parse(svg.querySelector("#animation-timing").textContent);
    progress.max = timing.duration - 1;
    svg.pauseAnimations();
    svg.setCurrentTime(reducedMotion.matches ? 25 : 0);
    controls.hidden = false;
    autoStartPending = true;
    observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting && autoStartPending) {
        autoStartPending = false;
        observer.disconnect();
        if (!reducedMotion.matches) svg.unpauseAnimations();
        updatePlayback();
      }
    }, { threshold: 0.25 });
    observer.observe(animationObject.closest("figure"));
    updatePlayback();
  }

  play.addEventListener("click", () => {
    manualPlayback();
    if (svg.animationsPaused()) svg.unpauseAnimations(); else svg.pauseAnimations();
    updatePlayback();
  });
  replay.addEventListener("click", () => {
    manualPlayback();
    svg.setCurrentTime(0);
    svg.unpauseAnimations();
    updatePlayback();
  });
  progress.addEventListener("input", () => {
    manualPlayback();
    svg.setCurrentTime(Number(progress.value));
    svg.pauseAnimations();
    updatePlayback();
  });
  reducedMotion.addEventListener("change", () => {
    if (!svg) return;
    autoStartPending = false;
    observer.disconnect();
    svg.classList.remove("motion-enabled");
    svg.pauseAnimations();
    svg.setCurrentTime(reducedMotion.matches ? 25 : 0);
    updatePlayback();
  });
  animationObject.addEventListener("load", initializeAnimation);
  initializeAnimation();
})();
