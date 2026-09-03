# Phase 7 — AI Engineering Foundations: Models, Evaluation

**Book:** AI Engineering — Chip Huyen — ch. 1 Introduction to Building AI Applications, ch. 2 Understanding Foundation Models, ch. 3 Evaluation Methodology, ch. 4 Evaluate AI Systems

**Goal:** Command the AI engineering discipline: what changed with foundation models, how they're built and why they behave the way they do, and — the hardest problem in AI engineering — **evaluation**. Evaluation is the load-bearing skill of every later phase.

**You are ready for Phase 8 when:** you can explain how a foundation model works under the hood, why it hallucinates, and you've built a working evaluation pipeline with an LLM-as-judge.

---

## Lesson 7.1 — The AI engineering discipline

### P7.1.1 — From ML engineering to AI engineering
- Concepts: what changed: foundation models as general-purpose tech (one model, many applications); iterative development (prompt, not train); the new stack layers: infrastructure → model → application → evaluation & tooling; AI engineering vs ML engineering vs data science; the shift from model-centric to application-centric.
- Refs: AI Engineering ch.1 (§ ML vs AI engineering, § AI stack).
- Do: Draw the 4-layer stack; place 10 real tools (K8s, vLLM, OpenAI API, LangChain, RAGAS, Weights&Biases, Postgres/pgvector, guardrails lib, feature store, Arrow) on the layers.

### P7.1.2 — Should you build it? Use-case analysis & planning
- Concepts: use-case analysis: model capabilities needed, cost, latency, risk (failure cost per use case); the "bartender test"; when NOT to use AI (deterministic rules beat models); solution archetypes: chatbots, copilots, agentic workflows, extraction/embedding pipelines; planning: value prop, cost analysis, risk & mitigation, the "human AI" fallback (human-in-the-loop as a first-class option).
- Refs: AI Engineering ch.1 (§ use cases, § planning AI applications).
- Do: Use-case canvas for Kitchen Flow's support assistant: capabilities, cost model, latency budget, risk table, build/buy/human decision.

### P7.1.3 — The foundation model landscape
- Concepts: proprietary APIs vs open models (and the trade-off table: quality, cost, control, privacy, latency, risk); model families & the LLM/LMM distinction; model size classes (nano → frontier); licensing; the flakiness/limit reality of APIs (rate limits, silent model updates — a Release It integration-point problem!); what "foundation" means.
- Refs: AI Engineering ch.1 (§ foundation models landscape / model selection criteria).
- Do: Model-selection ADR (ADR-0017): pick a model class for Kitchen Flow support across 3 scenarios (startup, scale, regulated) — the choice must flip at least once.

## Lesson 7.2 — Understanding foundation models

### P7.2.1 — How foundation models are made: pretraining
- Concepts: pretraining data (web corpora, curation, dedup), tokens & tokenization (BPE intuition, token economics), the transformer in architect terms (attention, context length, KV cache preview), scaling laws & emergent capabilities, training pipeline stages.
- Refs: AI Engineering ch.2 (pretraining sections).
- Do: Token-budget math: given a model's pricing, compute the cost of a 10-turn support chat with a 2K-token system prompt; explain why system prompts are amortized with prompt caching (preview Phase 9).

### P7.2.2 — Post-training: SFT, RLHF, alignment & why models misbehave
- Concepts: supervised finetuning, preference finetuning (RLHF: reward model, policy; DPO as the simpler alternative); what alignment buys and what it costs (rejection of benign prompts, verbosity); instruction-following vs base models; why models refuse, apologize, and flatter (sycophancy).
- Refs: AI Engineering ch.2 (post-training/alignment sections).
- Do: Explain in 5 bullet points to a non-technical exec why your chatbot refuses a harmless request — and two mitigation levers (prompt vs finetune).

### P7.2.3 — Sampling & generation: temperature, top-p, and the roots of hallucination
- Concepts: autoregressive generation; decoding strategies (greedy, temperature, top-k, top-p, beam); determinism vs creativity; **why hallucination is structural** (likelihood ≠ truth), why outputs are inconsistent, why context and generation settings change quality; when to set temperature 0 vs >0 (extraction vs ideation).
- Refs: AI Engineering ch.2 (sampling/decoding sections).
- Do: Sampling experiment: run the same prompt at temp 0 / 0.7 / 1.3, 5 times each; quantify variance; write generation-setting guidance for 3 task types.

## Lesson 7.3 — Evaluation methodology (the hardest problem)

### P7.3.1 — ML evaluation vs AI evaluation; leaderboards
- Concepts: why classic ML evals (fixed test set, accuracy) break: open-ended outputs, no ground truth, fast-moving models; public leaderboards/benchmarks vs private evals (contamination, benchmark saturation, Goodhart); evaluation as *the* differentiating skill; evaluation-driven development mindset (eval before feature).
- Refs: AI Engineering ch.3 (§ ML vs AI evaluation, benchmarks).
- Do: Pick a public benchmark (e.g., MMLU-style), find its limitations, explain why a passing score wouldn't guarantee your use case works.

### P7.3.2 — What to evaluate: capabilities, metrics & grading
- Concepts: evaluating by task type: classification (accuracy/precision/recall), summarization (coherence, factuality), translation, coding (functional correctness, exec-based evals), open-ended generation (relevance, faithfulness, tone); reference-based vs reference-free metrics; ROUGE/BLEU and why they're weak proxies.
- Refs: AI Engineering ch.3 (§ metrics per capability).
- Do: Metric cards for 6 task types: primary metric, secondary, collection method, failure mode.

### P7.3.3 — LLM-as-judge & comparative evaluation
- Concepts: using strong models to grade weaker ones; pointwise vs pairwise judging; judge reliability problems: position bias, verbosity bias, self-preference, prompt sensitivity; calibration against human labels (agreement metrics: Cohen's kappa intuition); the cost/latency of meta-evaluation.
- Refs: AI Engineering ch.3 (§ AI as a judge).
- Do: Build a pairwise judge prompt; run it on 10 outputs from 2 models; measure its agreement with your own labels; document its biases.

### P7.3.4 — Building the evaluation pipeline (evaluate AI systems)
- Concepts: eval dataset construction (from prod logs, synthesis, human labeling), data contamination & leakage, holdout hygiene; eval experiments: A/B comparisons, variance handling (multiple runs, seeds), regression suites in CI; **error analysis**: failure taxonomy → targeted fixes; eval infrastructure: storing results, dashboards, alerting on quality regressions.
- Refs: AI Engineering ch.4.
- Do: **Lab:** build `artifacts/eval-harness/`: a small CLI that runs 30 test cases against 2 models (or 2 prompts), computes metrics + LLM-judge scores, writes a comparison report. This artifact is reused in Phase 8–9.

---

## Checkpoint 7 (graded)
`artifacts/checkpoint-07/`:
1. "How LLMs work" one-pager written for a CTO (pretraining → post-training → sampling → hallucination).
2. Eval harness artifact applied to a real small task (e.g., product Q&A on 30 cases), with judge calibration notes and a decision (which model/prompt won, and why).
Pass bar: I challenge your eval: show me why your 30 cases aren't contaminated and why your judge isn't just agreeing with itself.

## Resources
- chiphuyen/aie-book GitHub repo (chapter resources)
- "Attention Is All You Need" (skim, architect-level)
- Hugging Face Open LLM Leaderboard / LMSYS Arena (browse, understand methodology)
- Cohen's kappa explainer; RAGAS docs (preview for Phase 8)
