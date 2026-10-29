/* The TAPS module retains the author's interaction and reports its natural height. */
(() => {
  const frame = document.getElementById("kb-taps-demo");
  if (!frame) return;
  window.addEventListener("message", (event) => {
    if (event.origin !== location.origin || event.source !== frame.contentWindow) return;
    if (event.data?.type !== "knowledge-boundaries:taps-height") return;
    if (Number.isFinite(event.data.height) && event.data.height > 0) {
      frame.style.height = `${Math.ceil(event.data.height)}px`;
    }
  });
  frame.addEventListener("load", () => {
    frame.contentWindow.postMessage({ type: "knowledge-boundaries:taps-request-height" }, location.origin);
  });
})();
