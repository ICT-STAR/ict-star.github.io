# From Latent Knowledge to Reliable Answers

STAR Group · Knowledge Boundaries & Uncertainty

Canonical project page: https://ict-star.github.io/projects/knowledge_boundaries/
Last checked: 2026-10-29

## Research questions

We study how language models can recall more of their existing knowledge, assess answer reliability, and use evidence or abstain appropriately. The studies form a shared research agenda, rather than a single integrated system.

- Access: improve factual recall and understand knowledge accessibility.
- Assess: study confidence alignment, reference signals, and fact-level judgments.
- Act: resist misleading context and control selective answering.

Calibration, answer accuracy, error discrimination, and selective risk are distinct evaluation dimensions. A failed answer or a finite sample budget does not prove that knowledge is absent.

## Papers and primary sources

### Blinded by Generated Contexts: How Language Models Merge Generated and Retrieved Contexts When Knowledge Conflicts?

Hexiang Tan, Fei Sun, Wanli Yang, Yuanzhuo Wang, Qi Cao, Xueqi Cheng.

ACL 2024 · Published conference paper · ACL Anthology published version

Controlled knowledge-conflict experiments reveal a preference for generated over retrieved context, including incorrect generated passages, and examine the roles of question similarity and semantic completeness.

- Primary paper: https://aclanthology.org/2024.acl-long.337/
- PDF: https://aclanthology.org/2024.acl-long.337.pdf
- Research summary: https://ict-star.github.io/projects/knowledge_boundaries/#blinded
- DOI: https://doi.org/10.18653/v1/2024.acl-long.337
- Code: https://github.com/Tan-Hexiang/RetrieveOrGenerated
- Project: https://tan-hexiang.github.io/Blinded_by_Generated_Contexts

### Too Consistent to Detect: A Study of Self-Consistent Errors in LLMs

Hexiang Tan, Fei Sun, Sha Liu, Du Su, Qi Cao, Xin Chen, Jingang Wang, Xunliang Cai, Yuanzhuo Wang, Huawei Shen, Xueqi Cheng.

EMNLP 2025 · Published conference paper · ACL Anthology published version

Defines self-consistent errors, evaluates their prevalence and the limitations of four error-detection approaches, and introduces a supervised cross-model probe using verifier hidden states.

- Primary paper: https://aclanthology.org/2025.emnlp-main.238/
- PDF: https://aclanthology.org/2025.emnlp-main.238.pdf
- Research summary: https://ict-star.github.io/projects/knowledge_boundaries/#too-consistent
- DOI: https://doi.org/10.18653/v1/2025.emnlp-main.238
- Code: https://github.com/Tan-Hexiang/Too-Consistent-to-Detect

### Beyond Reasoning: Reinforcement Learning Unlocks Parametric Knowledge in LLMs

Wanli Yang, Hongyu Zang, Junwei Zhang, Wenjie Shi, Du Su, Jingang Wang, Xueqi Cheng, Fei Sun.

arXiv 2026 · Preprint · arXiv v1, 8 May 2026

Studies correctness-reward reinforcement learning for one-hop closed-book factual recall without explicit chain-of-thought, finding evidence that RL improves access to suppressed correct answers.

- Primary paper: https://arxiv.org/abs/2605.07153
- PDF: https://arxiv.org/pdf/2605.07153v1
- Research summary: https://ict-star.github.io/projects/knowledge_boundaries/#beyond-reasoning
- DOI: https://doi.org/10.48550/arXiv.2605.07153

### When to Trust LLMs: Aligning Confidence with Response Quality

Shuchang Tao, Liuyi Yao, Hanxing Ding, Yuexiang Xie, Qi Cao, Fei Sun, Jinyang Gao, Huawei Shen, Bolin Ding.

Findings of ACL 2024 · Published conference paper · ACL Anthology published version

CONQORD combines quality and order-preserving alignment rewards to align verbalized confidence with response quality, with an application to deciding when retrieval augmentation may help.

- Primary paper: https://aclanthology.org/2024.findings-acl.357/
- PDF: https://aclanthology.org/2024.findings-acl.357.pdf
- Research summary: https://ict-star.github.io/projects/knowledge_boundaries/#conqord
- DOI: https://doi.org/10.18653/v1/2024.findings-acl.357

### BaseCal: Unsupervised Confidence Calibration via Base Model Signals

Hexiang Tan, Wanli Yang, Junwei Zhang, Xin Chen, Rui Tang, Du Su, Jingang Wang, Yuanzhuo Wang, Fei Sun, Xueqi Cheng.

ACL 2026 · Published conference paper · ACL Anthology published version

Uses a corresponding base model as a reference for post-trained confidence, through answer reevaluation or an unsupervised representation projection, while retaining the original answering model.

- Primary paper: https://aclanthology.org/2026.acl-long.234/
- PDF: https://aclanthology.org/2026.acl-long.234.pdf
- Research summary: https://ict-star.github.io/projects/knowledge_boundaries/#basecal
- DOI: https://doi.org/10.18653/v1/2026.acl-long.234
- Code: https://github.com/ICT-STAR/BaseCal

### Fact-Level Calibration and Correction for Long-Form Generations

Yige Yuan, Bingbing Xu, Hexiang Tan, Fei Sun, Teng Xiao, Wei Li, Huawei Shen, Xueqi Cheng.

SIGIR 2025 · Published conference paper · SIGIR 2025 published version; author preprint has an earlier title and method name

Studies calibration at the level of atomic facts, incorporating correctness and relevance, and introduces CARE to use high-confidence facts to help refine lower-confidence claims in long responses.

- Primary paper: https://doi.org/10.1145/3726302.3730195
- PDF: https://dl.acm.org/doi/pdf/10.1145/3726302.3730195
- Research summary: https://ict-star.github.io/projects/knowledge_boundaries/#fact-level
- DOI: https://doi.org/10.1145/3726302.3730195
- Code: https://github.com/yuanyige/fact-calibration
- Author preprint: https://arxiv.org/abs/2411.13343

### Resisting Contextual Interference in RAG via Parametric-Knowledge Reinforcement

Chenyu Lin, Yilin Wen, Du Su, Hexiang Tan, Fei Sun, Muhan Chen, Chenfu Bao, Zhonghou Lv.

ICLR 2026 · Published conference paper · ICLR 2026 proceedings version

Knowledgeable-R1 uses paired retrieval-free and retrieval-conditioned training signals to reinforce parametric knowledge and improve robustness to misleading context while using helpful external evidence.

- Primary paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/4dbcd4ba82866fdefc7ea0d15e9a72f2-Abstract-Conference.html
- PDF: https://proceedings.iclr.cc/paper_files/paper/2026/file/4dbcd4ba82866fdefc7ea0d15e9a72f2-Paper-Conference.pdf
- Research summary: https://ict-star.github.io/projects/knowledge_boundaries/#knowledgeable-r1
- Code: https://github.com/lcy80366872/knowledgeable-R1

### Strong yet Controllable LLM Abstention without Learning to Abstain

Junwei Zhang, Yifei Wang, Wanli Yang, Hexiang Tan, Rui Tang, Xin Chen, Jingang Wang, Du Su, Fei Sun.

arXiv 2026 · Preprint · arXiv v2, revised 26 October 2026

TAPS separates accuracy training from confidence-based answer selection, examining answering and distinguishing abilities at matched coverage while keeping the answer rate adjustable.

- Primary paper: https://arxiv.org/abs/2610.16318
- PDF: https://arxiv.org/pdf/2610.16318v2
- Research summary: https://ict-star.github.io/projects/knowledge_boundaries/#taps
- DOI: https://doi.org/10.48550/arXiv.2610.16318
- Project: https://zhangjunwei0233.github.io/projects/taps/
