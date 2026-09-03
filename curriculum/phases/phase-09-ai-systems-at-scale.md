# Phase 9 — AI Systems at Scale: Inference Optimization & End-to-End Architecture

**Book:** AI Engineering — Chip Huyen — ch. 9 Inference Optimization, ch. 10 AI Engineering (end-to-end architecture, feedback loops)

**Goal:** Architect the serving layer — making inference faster and cheaper without wrecking quality — and assemble the complete AI application architecture: gateways, routing, caching, memory, observability, feedback loops, and the platform/org design around it.

**You are ready for Phase 10 when:** you can produce a complete, defensible AI solution architecture document — the deliverable of your target role.

---

## Lesson 9.1 — Inference optimization

### P9.1.1 — Why inference is expensive & model-level optimization
- Concepts: the cost drivers (memory bandwidth, decode autoregression, attention cost growing with context); optimization taxonomy from the book; **model compression**: quantization (int8/int4, quantization-aware vs post-training), distillation (teacher→student), pruning (structured vs unstructured), the speed/quality/cost triangle; model architectures serving optimization (MoE intuition).
- Refs: AI Engineering ch.9 (§ model-level optimization).
- Do: Compression decision worksheet: for 3 budgets (free tier, pro, enterprise) pick model size + quantization level; predicted quality loss stated as hypothesis to verify with the harness.

### P9.1.2 — Service-level optimization: batching, caching, autoscaling
- Concepts: serving stack (model servers: vLLM/TGI class tools; the KV cache & **paged attention** intuition); **batching** (static vs dynamic/continuous batching — throughput vs latency); **caching layers**: prompt/prefix caching, semantic caching (and its correctness risks), response caching; speculative decoding intuition; **autoscaling** (why GPU autoscaling is harder: model load time, warm pools); API vs self-hosting economics (break-even math).
- Refs: AI Engineering ch.9 (§ inference service-level: batching, caching, autoscaling).
- Do: Latency/cost model for Kitchen Flow support at 100/1k/10k daily conversations, each with a different optimization applied; show the marginal cost curve; ADR-0021: API vs self-host at what scale.

### P9.1.3 — Model routing & the gateway pattern
- Concepts: AI gateway responsibilities (auth, rate limiting, cost tracking, logging, model routing); **router** patterns: cascade (cheap model first, escalate on confidence/failure), semantic routing (classify query → route), ensemble/fallback chains (ties to Release It circuit breakers!); multi-model strategies & abstraction layers (portability vs leaked model-specific features — an architecture-quantum question for models).
- Refs: AI Engineering ch.9 (§ router/gateway sections) + cross-ref Release It P6.x notes.
- Do: Design `artifacts/gateway-spec.md`: your AI gateway spec — 8 required features, fallback chain with trip conditions, and the abstraction boundary (what stays model-specific).

## Lesson 9.2 — End-to-end AI architecture

### P9.2.1 — The reference architecture, assembled
- Concepts: the complete AI application anatomy: client → gateway → orchestration (prompt assembly, retrieval, tools) → models (+ routers/fallbacks) → cache/memory layers → data stores (vector + operational) → observability plane; where each Phase 5–8 artifact slots in; deployment topologies (embedded AI in existing system vs standalone AI service vs AI platform team); failure-mode review of the full chain (every box is an integration point — Release It!).
- Refs: AI Engineering ch.10 (§ architecture).
- Do: C4 diagram (C1–C3) of the full Kitchen Flow AI system, Mermaid-coded, every edge labeled sync/async + failure behavior.

### P9.2.2 — Feedback loops, monitoring & continuous improvement
- Concepts: why AI apps need user feedback design (natural feedback vs explicitly-requested — and why asking users "rate this response" mostly fails); monitoring for AI: quality metrics in prod (sampled evals on live traffic), drift detection, guardrail trip rates, cost & latency SLOs; the improvement loop: logs → failure analysis → prompt/data/model updates → eval gate → deploy (ties to Phase 7 eval-driven development); shadow deploys & canary for prompts (Release It deployment patterns, reborn).
- Refs: AI Engineering ch.10 (§ feedback, § monitoring/observability).
- Do: Feedback design doc: what signal you collect implicitly, your sampled-eval cadence, alert thresholds; define the "prompt release pipeline" (staging evals → canary → full).

### P9.2.3 — Security, safety & cost governance at scale
- Concepts: AI-specific threat surface recap (injection from P8.1.3 + data leakage + model theft/abuse) placed on the architecture diagram; red teaming cadence; safety: guardrails layer, human escalation paths; cost governance: per-feature cost budgets, token accounting, chargeback/showback; the AI platform team pattern (central platform + embedded product teams — Fundamentals team-topology connection).
- Refs: AI Engineering ch.10 + your Phase 6 security notes.
- Do: Write the 2-page "AI governance section" for your architecture doc: controls, owners, budgets, incident response (what happens when the guardrail trips at 2am).

---

## Checkpoint 9 (graded)
`artifacts/checkpoint-09/` — **The AI Architecture Document (AAD)** for Kitchen Flow AI, the flagship artifact of this curriculum:
1. Business drivers → characteristics (Phase 2 method) incl. AI-specific ones (eval-ability, model portability);
2. Full C1–C3 architecture + failure behavior per edge;
3. Inference plan: model choices, optimization, caching, routing, cost model at 3 scales;
4. Feedback & improvement loop; 5. Security/governance section; 6. Complete ADR chain (you should be at ADR-0022+).
Pass bar: I review as a hiring panel for a Senior AI Solution Architect role. Survive 30 minutes.

## Resources
- vLLM docs (paged attention, continuous batching); GPU pricing pages (break-even math)
- OpenAI/Anthropic pricing & rate-limit docs; semantic cache papers (GPTCache)
- DORA/Team Topologies material for the platform-team pattern
