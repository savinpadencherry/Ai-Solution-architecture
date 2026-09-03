# Phase 10 — Capstones & Mastery

**Sources:** All four books, everything from Phases 0–9, plus live research.

**Goal:** Prove mastery. Four capstones, each a realistic engagement deliverable, each defended orally. Plus portfolio assembly and the path beyond.

**Rules:** each capstone is timeboxed (I recommend 1 week each); you may use any tooling; I act as stakeholders, reviewers, and chaos gremlin. Every capstone requires: characteristics, ADRs, diagrams, trade-off tables, fitness functions/evals where applicable, and an oral defense.

---

## Capstones

### P10.1 — Capstone A: "Monitor Me" (Fundamentals Appendix B kata, full treatment)
- Brief: design the end-to-end architecture for a personal health monitoring system (devices → cloud → family/care circle), from the book's own kata.
- Required: style selection with matrix, quanta analysis, resilience plan (stability patterns), deployment topology, full ADR set, risk storming session.
- Defense: review board simulation, Fundamentals-style.

### P10.2 — Capstone B: Enterprise RAG platform (multi-tenant, governed)
- Brief: a company-wide "Chat With Our Knowledge" platform for 5,000 employees, 12 source systems, strict permissions, EU data residency.
- Required: tenancy & access-control design at retrieval time, ingestion pipeline (pipeline style!), eval harness with per-source quality gates, cost model with caching strategy, governance section, data-quality scorecard for sources.
- Defense: I attack with tenant-escape attempts, a compliance audit, and a budget cut.

### P10.3 — Capstone C: Monolith → microservices migration (Hard Parts applied)
- Brief: take the Sysops Squad final state (or a real system you know) and plan a 12-month migration: decomposition order, data split, sagas, contracts, strangler-fig cutover, team topology change, rollback strategy at every step.
- Required: decomposition dossier upgraded with deployment/rollback plans (Release It applied), migration ADR sequence, chaos game day for the new architecture, what-you-won't-do list (granularity discipline!).
- Defense: I'm the change-averse VP of Engineering; convince me.

### P10.4 — Capstone D: AI agent platform (the frontier)
- Brief: an internal "AI employee" platform: 3 agent types (support, data analyst, code assistant), shared tool registry, spend controls, HITL escalation — for a 500-person company.
- Required: agent architecture choices per type (vs deterministic pipelines), tool governance (allowlists, scopes, audit), guardrail layers, evaluation strategy per agent, feedback flywheel, gateway/routing/cost design, incident response for agent misbehavior.
- Defense: full panel: security, legal, engineering, and a skeptical CFO.

### P10.5 — Portfolio assembly & the mastery map
- Do: curate `artifacts/` into a presentable portfolio: top 8 artifacts, each with a README; write your architecture principles document (your personal guiding principles, derived from everything); update the P0 baseline self-assessment → the "after" picture; record your rewritten "what an AI solution architect does" statement from P0.1.
- Output: portfolio + principles doc + before/after delta report.

### P10.6 — The path beyond (continued mastery operating system)
- Concepts: the architect's learning loop (fundamentals last, tools change); a personal technology radar (adopt/trial/assess/hold) maintained quarterly; communities, conferences, papers-to-read cadence; how to keep the four books' knowledge alive (teach it — the fastest way to master).
- Do: Write your quarterly learning OS: radar template, 3 sources you'll follow (e.g., Chip Huyen's blog, InfoQ architecture track, thoughtworks radar), and your first "teach-back" topic (schedule it with me — I'll be your student).

---

## Final mastery exam (the exit gate)
One last gauntlet: I generate a **brand-new scenario** (never seen in the curriculum), and you produce in one week: characteristics + ADR set + architecture + AI strategy + resilience plan + risk register. Then defend it.
**Pass bar:** the review board (me, ruthless) signs off. Then you're done — and you'll know it.

## Beyond (optional horizons)
- Cloud AI architect certifications (AWS AI Practitioner→Solutions Architect / Azure AI Engineer / GCP Professional ML Engineer) — the curriculum over-prepares you for the concepts; certs add vendor specifics
- Deep dives: Designing Machine Learning Systems (Chip Huyen) for traditional ML; Building Evolutionary Architecture (fitness functions origin); Designing Data-Intensive Applications (data systems depth)
