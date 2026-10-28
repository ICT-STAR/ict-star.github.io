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
})();
