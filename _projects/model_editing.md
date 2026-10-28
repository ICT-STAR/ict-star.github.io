---
layout: default
title: Model Editing
author:
  - Wanli Yang
  - Fei Sun
description: From diagnosing model collapse to reliable, scalable knowledge updates. Four studies on model editing, 2024–2026.
img: model-editing.svg
date: 2026-10-28
time: 2026-10-28
---

<link rel="stylesheet" href="{{ '/assets/css/model-editing.css' | relative_url }}">

<article class="me-project">
  <header class="me-hero">
    <div>
      <a class="me-back" href="{{ '/projects/' | relative_url }}">← All projects</a>
      <p class="me-eyebrow">STAR GROUP &nbsp; / &nbsp; MODEL EDITING</p>
      <h1>Editing knowledge.<br><em>Preserving intelligence.</em></h1>
      <p class="me-deck">How do we change what a language model knows<br class="me-desktop-break"> without breaking what it can do?</p>
      <p class="me-byline">A research thread by Wanli Yang, Fei Sun &amp; collaborators<br><span>Four papers · 2024–2026</span></p>
    </div>
    <img class="me-cover" src="{{ '/assets/img/project/cover/model-editing.svg' | relative_url }}" width="1200" height="900" alt="A single highlighted weight in a model connects to knowledge, language, and reasoning: a local change can affect the whole model.">
  </header>

  <div class="me-intro">
    <p>Model editing promises to update a language model’s knowledge without retraining it from scratch. But changing a fact is only part of the problem: the updated model must still reason, generate coherent language, and use its new knowledge beyond the edit prompt. Our research asks what it takes to make those updates reliable.</p>
    <p>Across four studies, we move from <a href="#butterfly">discovering collateral damage</a> to <a href="#rome">explaining a failure mechanism</a>, then from <a href="#mirage">measuring real-world effectiveness</a> to <a href="#locft">building a more scalable editor</a>. Together, these works connect three requirements: understand the update, evaluate it honestly, and preserve the model’s broader abilities.</p>
  </div>

  <nav class="me-thread" aria-label="The research story">
    <a href="#butterfly"><span>01 / ACL 2024</span>Discover the risk <span aria-hidden="true">↗</span></a>
    <a href="#rome"><span>02 / EMNLP 2024</span>Explain the failure <span aria-hidden="true">↗</span></a>
    <a href="#mirage"><span>03 / ACL 2025</span>Rethink evaluation <span aria-hidden="true">↗</span></a>
    <a href="#locft"><span>04 / ICLR 2026</span>Scale the solution <span aria-hidden="true">↗</span></a>
  </nav>

  <section class="me-work" id="butterfly" aria-labelledby="butterfly-title">
    <div class="me-copy">
      <p class="me-eyebrow">01 &nbsp; / &nbsp; FINDINGS OF ACL 2024</p>
      <h2 id="butterfly-title">The Butterfly Effect<br>of Model Editing</h2>
      <p class="me-takeaway">One factual update can disrupt a whole model.</p>
      <p>We show that even a single ROME edit can severely damage general capabilities, while challenging edit sequences expose collapse across multiple methods. Perplexity offers an efficient signal of downstream degradation; our HardEdit dataset helps stress-test these failures. The lesson: editing success alone cannot tell us whether a model remains useful.</p>
      <p class="me-paper-title">The Butterfly Effect of Model Editing: Few Edits Can Trigger Large Language Models Collapse</p>
      <div class="me-links"><a href="https://aclanthology.org/2024.findings-acl.322/">Paper ↗</a><a href="https://github.com/WanliYoung/Collapse-in-Model-Editing">Code &amp; HardEdit ↗</a></div>
    </div>
    <figure class="me-figure me-paper-figure">
      <div class="me-figure-heading"><h3>One edit can break the whole model.</h3><span>Original Fig. 1</span></div>
      <a class="me-original-figure" href="{{ '/assets/img/project/model-editing/butterfly-fig1.pdf' | relative_url }}" target="_blank" rel="noopener" aria-label="Open the original Butterfly Figure 1 as an enlarged PDF">
        <img src="{{ '/assets/img/project/model-editing/butterfly-fig1.svg' | relative_url }}" width="888" height="398" alt="Original Figure 1: after the ROME edit Twitter was acquired by Elon Musk, GPT-J's coherent story becomes repetitive gibberish. PIQA, HellaSwag, and LAMBADA accuracy falls sharply toward the random baselines.">
      </a>
      <figcaption>Original <a href="https://aclanthology.org/2024.findings-acl.322.pdf#page=1">Fig. 1</a>, including generation and capability tests for one GPT-J collapse case. Tap the figure to enlarge.</figcaption>
    </figure>
  </section>

  <section class="me-work" id="rome" aria-labelledby="rome-title">
    <div class="me-copy">
      <p class="me-eyebrow">02 &nbsp; / &nbsp; FINDINGS OF EMNLP 2024</p>
      <h2 id="rome-title">The Fall of ROME</h2>
      <p class="me-takeaway">From observing collapse to understanding why.</p>
      <p>We trace a class of ROME failures to inconsistent use of contextualized and unprefixed key representations. For subjects at the first token, this mismatch can shrink the update’s denominator and amplify the parameter change. Using prefixed keys consistently stabilizes the update; matching the context at evaluation recovers edit efficacy. This explains a concrete single-edit failure, while cumulative editing remains a broader challenge.</p>
      <p class="me-paper-title">The Fall of ROME: Understanding the Collapse of LLMs in Model Editing</p>
      <div class="me-links"><a href="https://aclanthology.org/2024.findings-emnlp.236/">Paper ↗</a><a href="https://github.com/WanliYoung/Collapse-in-Model-Editing">Code ↗</a></div>
      <figure class="me-rome-evidence">
        <table class="me-rome-data"><caption>What changes in GPT-J collapse cases?</caption><thead><tr><th scope="col">Mean quantity</th><th scope="col">Normal</th><th scope="col">Collapse</th></tr></thead><tbody><tr><th scope="row">Numerator norm</th><td>88.69</td><td>140.27</td></tr><tr><th scope="row">Absolute denominator</th><td>12.78</td><td class="me-key-unprefixed">0.04</td></tr></tbody></table>
        <figcaption><a href="https://aclanthology.org/2024.findings-emnlp.236.pdf#page=3">Table 1</a> · Normal: 1,000 sampled COUNTERFACT edits; collapse: HardCF. The mean absolute denominator is about 320× smaller. Numerator and denominator statistics are averaged separately.</figcaption>
      </figure>
    </div>
    <figure class="me-figure me-formula-card">
      <div class="me-figure-heading"><h3>Where the implementation goes wrong</h3><span>§3.1</span></div>
      <p class="me-equation-label">ROME implementation · mixed keys</p>
      <div class="me-equation">
        <math display="block" aria-label="ROME update: numerator is v target minus W times unprefixed key, multiplied by transpose of C inverse times prefixed key; denominator mixes the prefixed and unprefixed keys.">
          <msub><mi>Δ</mi><mtext>ROME</mtext></msub><mo>=</mo>
          <mfrac>
            <mrow><mo>(</mo><msub><mi>v</mi><mo>*</mo></msub><mo>−</mo><mi>W</mi><msup class="me-key-unprefixed"><mi>k</mi><mi>u</mi></msup><mo>)</mo><msup><mrow><mo>(</mo><msup><mi>C</mi><mn>−1</mn></msup><mover class="me-key-prefixed"><mi>k</mi><mo>¯</mo></mover><mo>)</mo></mrow><mo>⊤</mo></msup></mrow>
            <mrow class="me-denominator"><msup><mrow><mo>(</mo><msup><mi>C</mi><mn>−1</mn></msup><mover class="me-key-prefixed"><mi>k</mi><mo>¯</mo></mover><mo>)</mo></mrow><mo>⊤</mo></msup><msup class="me-key-unprefixed"><mi>k</mi><mi>u</mi></msup></mrow>
          </mfrac>
        </math>
      </div>
      <p class="me-formula-note"><span class="me-key-prefixed">Prefixed k̄</span> and <span class="me-key-unprefixed">unprefixed kᵘ</span> can differ sharply at the first token, making the denominator tiny. The mismatch is in the implementation; theoretical Eq. 3 uses consistent keys.</p>
      <p class="me-equation-label">C-ROME · consistent prefixed keys</p>
      <div class="me-equation">
        <math display="block" aria-label="C-ROME uses the prefixed mean key consistently in the residual and denominator.">
          <msub><mi>Δ</mi><mtext>C-ROME</mtext></msub><mo>=</mo>
          <mfrac>
            <mrow><mo>(</mo><msub><mi>v</mi><mo>*</mo></msub><mo>−</mo><mi>W</mi><mover class="me-key-prefixed"><mi>k</mi><mo>¯</mo></mover><mo>)</mo><msup><mrow><mo>(</mo><msup><mi>C</mi><mn>−1</mn></msup><mover class="me-key-prefixed"><mi>k</mi><mo>¯</mo></mover><mo>)</mo></mrow><mo>⊤</mo></msup></mrow>
            <mrow><msup><mrow><mo>(</mo><msup><mi>C</mi><mn>−1</mn></msup><mover class="me-key-prefixed"><mi>k</mi><mo>¯</mo></mover><mo>)</mo></mrow><mo>⊤</mo></msup><mover class="me-key-prefixed"><mi>k</mi><mo>¯</mo></mover></mrow>
          </mfrac>
        </math>
      </div>
      <p class="me-symbols">k̄: mean prefixed key; kᵘ: unprefixed key; W: MLP output projection; C: cached key second moment; v<sub>*</sub>: target value.</p>
      <figcaption>Equations follow the implementation analysis in <a href="https://aclanthology.org/2024.findings-emnlp.236.pdf#page=3">§3.1</a>.</figcaption>
    </figure>
  </section>

  <section class="me-work" id="mirage" aria-labelledby="mirage-title">
    <div class="me-copy">
      <p class="me-eyebrow">03 &nbsp; / &nbsp; ACL 2025</p>
      <h2 id="mirage-title">The Mirage<br>of Model Editing</h2>
      <p class="me-award"><a href="https://knowledgeable-lm.github.io/acl25/"><span aria-hidden="true">★</span> <strong>Best Paper Award</strong> <span>KnowFM @ ACL 2025 Workshop</span></a></p>
      <p class="me-takeaway">Does the model know it, or does the test help it?</p>
      <p>We introduce QAEdit and WILD to evaluate edits through freely generated answers. Teacher forcing and answer-length hints can make synthetic evaluations overly optimistic. On Llama-2-7b-chat and QAEdit, mean single-edit reliability across six editors drops from 96.8% to 38.5% under WILD. Realistic evaluation turns apparent success into a more demanding test of usable knowledge.</p>
      <p class="me-paper-title">The Mirage of Model Editing: Revisiting Evaluation in the Wild</p>
      <div class="me-links"><a href="https://aclanthology.org/2025.acl-long.745/">Paper ↗</a><a href="https://github.com/WanliYoung/Revisit-Editing-Evaluation">Code, QAEdit &amp; WILD ↗</a><a href="#mirage-protocols">Compare the protocols ↓</a></div>
    </div>
    <figure class="me-figure" id="me-evaluation">
      <div class="me-figure-heading"><h3>The evaluation gap</h3><span>Reliability (%)</span></div>
      <label class="me-select-label" for="me-editor">Explore an editor <select id="me-editor"><option value="mean">Six-editor mean</option><option value="ftm">FT-M</option><option value="mend">MEND</option><option value="rome">ROME</option><option value="memit">MEMIT</option><option value="grace">GRACE</option><option value="wise">WISE</option></select></label>
      <div class="me-comparison" role="img" aria-label="Six-editor mean: synthetic evaluation 96.8 percent, WILD evaluation 38.5 percent.">
        <div class="me-comparison-row"><div><span>Synthetic evaluation</span><strong id="me-synthetic-value">96.8%</strong></div><div class="me-eval-track"><span id="me-synthetic-bar" style="width:96.8%"></span></div></div>
        <div class="me-comparison-row"><div><span>WILD evaluation</span><strong id="me-wild-value">38.5%</strong></div><div class="me-eval-track"><span id="me-wild-bar" style="width:38.5%"></span></div></div>
      </div>
      <p class="me-gap" id="me-gap" aria-live="polite"><strong>58.3 percentage points</strong> between the two evaluations.</p>
      <figcaption><a href="https://aclanthology.org/2025.acl-long.745.pdf#page=5">Table 3</a> · Same model (Llama-2-7b-chat), dataset (QAEdit), and single-edit setting. Only the evaluation protocol changes.</figcaption>
      <details class="me-data"><summary>View all source values</summary><table><caption>Single-edit reliability on QAEdit (%)</caption><thead><tr><th scope="col">Editor</th><th scope="col">Synthetic</th><th scope="col">WILD</th></tr></thead><tbody><tr><th scope="row">FT-M</th><td>100.0</td><td>61.1</td></tr><tr><th scope="row">MEND</th><td>94.2</td><td>33.3</td></tr><tr><th scope="row">ROME</th><td>95.5</td><td>58.5</td></tr><tr><th scope="row">MEMIT</th><td>92.9</td><td>55.2</td></tr><tr><th scope="row">GRACE</th><td>98.3</td><td>1.2</td></tr><tr><th scope="row">WISE</th><td>99.8</td><td>21.6</td></tr></tbody></table></details>
    </figure>
    <figure class="me-figure me-wide-figure" id="mirage-protocols">
      <div class="me-figure-heading"><h3>Same question. Two very different tests.</h3><span>Original Fig. 3</span></div>
      <a class="me-original-figure" href="{{ '/assets/img/project/model-editing/mirage-fig3.pdf' | relative_url }}" target="_blank" rel="noopener" aria-label="Open the original Mirage Figure 3 as an enlarged PDF">
        <img src="{{ '/assets/img/project/model-editing/mirage-fig3.svg' | relative_url }}" width="1804" height="660" alt="Original Figure 3 from The Mirage of Model Editing: the synthetic and WILD evaluation frameworks side by side, including their context, token-by-token generation, stopping rules, and evaluation metrics.">
      </a>
      <figcaption>Original <a href="https://aclanthology.org/2025.acl-long.745.pdf#page=4">Fig. 3</a>, reproduced directly from the published paper. Tap the figure to enlarge.</figcaption>
    </figure>
  </section>

  <section class="me-work" id="locft" aria-labelledby="locft-title">
    <div class="me-copy">
      <p class="me-eyebrow">04 &nbsp; / &nbsp; ICLR 2026</p>
      <h2 id="locft-title">Fine-tuning Done Right<br>in Model Editing</h2>
      <p class="me-takeaway">Revisit the procedure. Recover the potential.</p>
      <p>Fine-tuning’s weakness in editing is partly a training-procedure problem: optimizing each edit to convergence can overfit and interfere with other edits. LocFT-BF combines epoch-based mini-batches with carefully localized parameter updates. Tested with WILD, it scales to 100K edits and 72B-parameter models while largely retaining general capabilities. Reliability, paraphrase generalization, and capability preservation remain distinct measures of success.</p>
      <div class="me-links"><a href="https://proceedings.iclr.cc/paper_files/paper/2026/hash/74b8ccb5ad21871fd436867df19c35ac-Abstract-Conference.html">Paper ↗</a><a href="https://github.com/ICT-STAR/LocFT">LocFT code ↗</a></div>
    </div>
    <figure class="me-figure">
      <div class="me-figure-heading"><h3>Change how edits are learned.</h3><span>Training procedure</span></div>
      <div class="me-training"><div><span class="me-training-label">Depth-first</span><p>Finish one edit, then move on</p><div class="me-tokens" aria-label="Edit A repeatedly, then edit B repeatedly"><span>A</span><span>A</span><span>A</span><i>→</i><span>B</span><span>B</span><span>B</span></div></div><div><span class="me-training-label">Breadth-first · LocFT-BF</span><p>Revisit a set of edits across mini-batch epochs</p><div class="me-tokens me-tokens-bf" aria-label="An epoch over edits A B C, then another epoch over A B C"><span>A</span><span>B</span><span>C</span><i>→</i><span>A</span><span>B</span><span>C</span></div></div></div>
      <div class="me-scale"><div><strong>100K</strong><span>knowledge edits</span></div><div><strong>72B</strong><span>model parameters</span></div></div>
      <figcaption>Procedure schematic based on <a href="https://proceedings.iclr.cc/paper_files/paper/2026/file/74b8ccb5ad21871fd436867df19c35ac-Paper-Conference.pdf#page=3">Fig. 2</a>. At the combined scale above: Qwen2.5-72B, 100K ZsRE edits; WILD reliability 99.80%, paraphrase generalization 57.60%, capability score 62.54% (64.84% before editing). <a href="https://proceedings.iclr.cc/paper_files/paper/2026/file/74b8ccb5ad21871fd436867df19c35ac-Paper-Conference.pdf#page=10">§5.2</a>.</figcaption>
    </figure>
  </section>

  <footer class="me-outlook"><p class="me-eyebrow">THE THREAD THAT CONNECTS THEM</p><p>Reliable editing means more than changing an answer.<br>It means keeping the model worth asking.</p><a href="{{ '/publications/' | relative_url }}">Explore our publications <span aria-hidden="true">↗</span></a></footer>
</article>

<script src="{{ '/assets/js/model-editing.js' | relative_url }}" defer></script>
