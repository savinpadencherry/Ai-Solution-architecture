# Phase 8 — Adapting Models: Prompts, RAG, Agents, Finetuning, Data

**Book:** AI Engineering — Chip Huyen — ch. 5 Prompt Engineering, ch. 6 RAG and Agents, ch. 7 Finetuning, ch. 8 Dataset Engineering

**Goal:** Master every lever for making a foundation model perform for your application: instructions (prompts), context (RAG, agents), weights (finetuning), and the data pipeline underneath all three — with an evaluation harness around each.

**The architect's decision spine of this phase:** *prompt → RAG → finetune*: always exhaust the cheaper lever before the expensive one, and prove it with evaluation.

**You are ready for Phase 9 when:** you've built a production-grade RAG system with evals, an agent with guardrails, and can ADR the prompt-vs-RAG-vs-finetune decision for any use case.

---

## Lesson 8.1 — Prompt engineering

### P8.1.1 — What a prompt is & why prompting works
- Concepts: prompt anatomy (task description, examples, context, output format); in-context learning; why prompting works on models trained for instruction-following; instructions vs context vs generation settings (the three response-quality levers from the book's framing); prompt sensitivity.
- Refs: AI Engineering ch.5 (§ prompting overview).
- Do: Dissect a production prompt into its 4 anatomies; make it better by 2 changes, measure with the Phase 7 harness.

### P8.1.2 — The technique catalog
- Concepts: zero-shot vs few-shot (example selection & ordering effects); chain-of-thought & why it helps (and its latency/cost price); task decomposition (sequential chaining, map-reduce/merge, self-consistency); structured output (JSON schemas, function-format constraints); output-format discipline for downstream parsing.
- Refs: AI Engineering ch.5 (technique sections).
- Do: Technique bake-off on one task: baseline vs few-shot vs CoT vs decomposition — measured on quality AND latency/cost; log results in the harness repo.

### P8.1.3 — Defensive prompt engineering & automated optimization
- Concepts: prompt attacks: **direct injection** (jailbreaks), **indirect injection** (poisoned content via RAG/web pages — the scarier one), data/PII extraction, model extraction; defenses: privilege separation (LLM never sees credentials), input/output filtering, instruction hierarchy, content scanning; automated prompt engineering (versioning prompts like code, A/B testing prompts, DSPy-style optimization).
- Refs: AI Engineering ch.5 (§ defensive prompt engineering, § prompt versioning/automation).
- Do: Attack lab: attempt a direct and an indirect injection on your Phase 7 chatbot; then implement 2 defenses and prove they work (this artifact feeds the Phase 9 security review).

## Lesson 8.2 — Context construction: RAG

### P8.2.1 — Why RAG works & the retrieval foundation
- Concepts: external memory & the knowledge problem (cutoff, private data, hallucination-free-ish grounding); text → embeddings → semantic search; chunking strategies (size, overlap, structure-aware); embedding model selection; vector databases & indexing (HNSW intuition); hybrid search (BM25 + dense + rerankers like cross-encoders).
- Refs: AI Engineering ch.6 (§ RAG overview, retrieval internals).
- Do: Build the minimal RAG: chunk 20 documents, embed, store in a vector DB (or in-memory index), retrieve top-k; eyeball retrieval quality; then add a reranker and measure the difference (retrieval metrics: recall@k, MRR).

### P8.2.2 — The full RAG pipeline & its evaluation
- Concepts: query transformation (rewriting, expansion, HyDE-style hypothetical docs); multi-hop & agentic RAG preview; RAG evaluation split in two: **retrieval metrics** (context relevance, recall@k) vs **generation metrics** (faithfulness/groundedness, answer relevance) — RAGAS-style decomposition; the generation-setting interaction (grounding vs temperature); production RAG concerns: freshness, multi-tenancy isolation, access control at retrieval time, cost per query.
- Refs: AI Engineering ch.6 (RAG sections + evaluation).
- Do: Upgrade the minimal RAG to `artifacts/rag-app/`: query rewriting + reranking + citations; wire it into the eval harness with retrieval + faithfulness metrics; include an access-control test (tenant A must not see tenant B's docs).

## Lesson 8.3 — Agents

### P8.3.1 — Agent fundamentals: planning & tool use
- Concepts: what makes something an agent (planning + environment + tools + memory); tool/function calling mechanics (schemas, validation); the agent loop (plan → act → observe); ReAct-style reasoning; when agents are worth it vs a pipeline (the book's agentic pattern vs RAG framing: flexibility vs reliability/cost).
- Refs: AI Engineering ch.6 (§ agents).
- Do: Build a 2-tool agent (search + calculator or DB query) from raw API calls (no framework first); log every loop; count tokens/cost per task.

### P8.3.2 — Agent architecture & multi-agent systems
- Concepts: agent architectures (single agent w/ tools, router, plan-and-execute, multi-agent: vertical vs collaborative); shared memory & state passing; failure modes: loops, deadlocks (Hard Parts' choreography connection!), compounding error rates; guardrails: action validation, permission scoping, human-in-the-loop checkpoints; evaluating agents (task success rate, trajectory analysis).
- Refs: AI Engineering ch.6 (agent architectures, evaluation) + your Hard Parts P5.3.5 notes.
- Do: ADR-0018: agent vs deterministic pipeline for a Kitchen Flow automation; if agent wins, add guardrails: max iterations, tool allowlist, spend cap, HITL trigger.

## Lesson 8.4 — Finetuning

### P8.4.1 — Finetuning fundamentals: when & what
- Concepts: transfer learning applied to FMs; what finetuning can/can't do (add knowledge → use RAG; change behavior/style/format/latency → finetune); supervised finetuning (SFT) vs preference finetuning; data needs; when NOT to finetune (the book's explicit list); cost/risk of owning weights.
- Refs: AI Engineering ch.7 (§ finetuning overview, § when to finetune).
- Do: ADR-0019: for a "brand-voice support bot with a knowledge base", split the problem into RAG part vs finetune part; defend the boundary.

### P8.4.2 — Memory math, PEFT (LoRA/QLoRA), & model merging
- Concepts: parameter/memory footprint calculation (params × bytes per param + optimizer state; the book's technical section), LoRA mechanics (low-rank adapters, rank/alpha trade-offs), QLoRA (4-bit quantized base + adapters), adapter swapping; model merging (experimental: task arithmetic, TIES/DARE intuition) and its risks.
- Refs: AI Engineering ch.7 (§ memory footprint, § PEFT, § model merging).
- Do: Memory-math worksheet: can you finetune a 7B model on your machine (show the arithmetic)? Then run a real LoRA finetune (small model, small dataset) and eval before/after with the harness.

## Lesson 8.5 — Dataset engineering

### P8.5.1 — Data acquisition, annotation & synthesis
- Concepts: data as the bottleneck; acquisition (internal logs, public data, licensing/provenance); **annotation**: guideline design, inter-annotator agreement, quality control workflows; **synthesis**: generating training/eval data with stronger models (distillation, self-instruct patterns), synthesis risks (mode collapse, contamination, distribution shift); synthetic data for evals too.
- Refs: AI Engineering ch.8 (§ acquisition, § annotation, § synthesis).
- Do: Build a 50-example finetune dataset for your use case via synthesis + human spot-check; measure agreement on a 10-sample relabel.

### P8.5.2 — Data processing & quality evaluation
- Concepts: deduplication (exact/fuzzy), PII scrubbing, quality filtering heuristics, formatting for training (chat templates); what **data quality** means (accuracy, completeness, consistency, timeliness, relevance) and how to *evaluate* it systematically; the data flywheel: prod feedback → labeled data → model/prompt improvements (ties to Phase 9 feedback loops).
- Refs: AI Engineering ch.8 (§ processing, § data quality, flywheel).
- Do: Data quality scorecard for your synthesized dataset + one automated cleaning pipeline (dedup + PII + format); document the flywheel design for Kitchen Flow.

---

## Checkpoint 8 (graded)
`artifacts/checkpoint-08/` — **Adaptation Portfolio:**
1. RAG app artifact with retrieval + generation evals + access-control test (P8.2.2).
2. Agent artifact with guardrails + cost/trajectory log (P8.3).
3. Finetune experiment: small LoRA run with before/after evals (P8.4.2).
4. ADR-0020: the full "prompt vs RAG vs finetune" decision for one use case, with eval evidence for the rejected options.
Pass bar: your rejected options must have numbers attached; "we just felt like RAG" fails.

## Resources
- chiphuyen/aie-book GitHub; RAGAS docs; LangSmith/Braintrust (eval platforms, browse); LoRA paper (Hu et al.) at architect depth; DSPy (browse, concept only)
