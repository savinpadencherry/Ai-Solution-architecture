# Master AI Solution Architect — Curriculum Index

**121 pointers · 11 phases · 10 checkpoints · 4 capstones + final exam**

The journey, in one line: **learn to think like an architect → master characteristics & styles → solve the distributed hard parts → survive production → command the AI stack → assemble it all in flagship architectures.**

| Phase | Title | Book(s) | Pointers | Checkpoint |
|-------|-------|---------|----------|------------|
| 0 | Setup, Baseline & Architect's Toolkit | all (prefaces, Hard Parts ch.1) | 4 | Toolkit ready |
| 1 | Architectural Thinking & Modularity | Fundamentals ch.1–3 | 13 | C1: Kitchen Flow trade-off + modularity report |
| 2 | Architecture Characteristics | Fundamentals ch.4–8 | 12 | C2: Insurance Claims characteristics + fitness functions |
| 3 | Architecture Styles: The Full Catalog | Fundamentals ch.9–19 | 13 | C3: 9 style one-pagers + kata |
| 4 | Techniques: Decisions, Risk, Diagrams, Teams, Career | Fundamentals ch.20–28 | 10 | C4: Mock review board |
| 5 | Distributed Architecture: The Hard Parts | Hard Parts ch.1–15 | 19 | C5: Migration dossier |
| 6 | Production Engineering: Release It! | Release It! ch.1–17 | 17 | C6: Production readiness review (LLM pipeline) |
| 7 | AI Engineering Foundations: Models & Evaluation | AI Engineering ch.1–4 | 10 | C7: Eval harness + model explainer |
| 8 | Adapting Models: Prompts, RAG, Agents, Finetuning, Data | AI Engineering ch.5–8 | 11 | C8: Adaptation portfolio |
| 9 | AI Systems at Scale: Inference & End-to-End Architecture | AI Engineering ch.9–10 | 6 | C9: AI Architecture Document |
| 10 | Capstones & Mastery | all | 6 | 4 capstones + final exam |

## The knowledge spine (how the books interlock)

- **Fundamentals** gives you the thinking apparatus: characteristics, trade-offs, styles, ADRs.
- **Hard Parts** stress-tests that apparatus on distributed systems: coupling, decomposition, data, sagas, contracts, mesh.
- **Release It!** makes everything survive reality: failure modes, stability patterns, deployment, chaos.
- **AI Engineering** rebuilds the stack for foundation models — where evaluation replaces correctness, and every LLM call is a distributed-systems integration point (rate limits, timeouts, circuit breakers all return).
- Cross-book threads we deliberately weave: fitness functions (Fundamentals → Hard Parts), circuit breakers (Release It → AI gateways), contracts & versioning (Hard Parts → Release It → prompt/model versioning), team topologies (Fundamentals → data mesh → AI platform teams), risk storming (Fundamentals → AI red teaming).

## Suggested rhythm (adaptable)

- **Weeks 1–2:** Phase 0–1 (mindset + modularity)
- **Weeks 3–4:** Phase 2 (characteristics)
- **Weeks 5–6:** Phase 3 (styles)
- **Week 7:** Phase 4 (techniques & soft skills) + review board
- **Weeks 8–10:** Phase 5 (hard parts — the mountain)
- **Weeks 11–12:** Phase 6 (production)
- **Weeks 13–15:** Phase 7–8 (AI core)
- **Week 16:** Phase 9 (scale + AAD)
- **Weeks 17–21:** Phase 10 (capstones + final exam)

Full lesson detail lives in [`phases/`](phases/). Track everything in [`PROGRESS.md`](PROGRESS.md). Protocol in [`README.md`](README.md).
