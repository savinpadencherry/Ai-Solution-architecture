# Master AI Solution Architect Curriculum — Operating Manual

**Mission:** Transform you into a master **AI Solution Architect** — an engineer who can (1) think architecturally about any system, (2) design and evolve distributed architectures with rigorous trade-off analysis, (3) ship systems that survive production, and (4) architect applications on top of foundation models (LLMs, multimodal models, agents, RAG) with evaluation-driven rigor.

This curriculum is built from a deep analysis of the **four source books** in this repository:

| # | Book | Role in your mastery |
|---|------|---------------------|
| 1 | **Fundamentals of Software Architecture, 2nd Ed.** — Mark Richards & Neal Ford | The *mindset*: architectural thinking, architecture characteristics, all major architecture styles, decisions, diagramming, soft skills, career |
| 2 | **Software Architecture: The Hard Parts** — Ford, Richards, Sadalage, Dehghani | The *distributed muscle*: coupling/quanta, decomposition, data ownership, sagas, contracts, data mesh, trade-off analysis |
| 3 | **Release It! 2nd Ed.** — Michael T. Nygard | The *production edge*: stability antipatterns & patterns, production infrastructure, deployment, versioning, chaos engineering |
| 4 | **AI Engineering** — Chip Huyen | The *AI specialism*: foundation models, evaluation, prompt engineering, RAG, agents, finetuning, dataset engineering, inference optimization, end-to-end AI architecture |

---

## How we work (the learning protocol)

We go **one pointer at a time**. Every pointer (`P<phase>.<lesson>.<n>`) is a small, complete unit of mastery — typically 30–90 minutes.

### The 6-step pointer loop
1. **READ** — I extract the relevant sections from the PDF and teach you the concepts with my own explanations, diagrams (ASCII/Mermaid), and examples. I supplement with live web research (papers, docs, benchmarks) via the browser when it adds value.
2. **ASK** — You drive. Ask any question the moment a doubt appears — that's where learning happens. No quizzes, no graded gates from my side; depth follows your curiosity, and I re-teach anything from a different angle on request.
3. **DO** — A hands-on exercise or artifact: an ADR, a fitness function, a diagram, code, an eval harness, a migration plan. We build these together.
4. **CONNECT** — We explicitly link this pointer to 2–3 other pointers across books (e.g., how Release It!'s circuit breaker shows up inside Chip Huyen's inference infrastructure).
5. **ARTIFACT** — Everything you produce goes into `curriculum/artifacts/` — by the end, this folder is your portfolio proof of mastery.
6. **MARK** — We tick the checkbox in `PROGRESS.md` and log one "keeper insight" per pointer.

### Working rules
- **You drive the questions.** I teach; interrupt the moment something is unclear.
- **Plain language first.** Every concept starts with an everyday analogy before any jargon; every technical term is defined the moment it first appears. If a lesson assumes something not yet taught, say "go back" — the gap gets filled before we continue.
- **Quizzes and puzzles only on request.** You say "quiz me" or "give me a puzzle" when you want one — I never assign unrequested exercises or homework. You ask questions whenever doubts appear; doubts set the depth.
- **Artifacts over notes.** Each artifact should be usable in a real job (ADR, diagram, runbook, eval report, architecture doc).
- **Spaced re-connection:** each pointer explicitly links back to earlier ones so nothing rots.
- **Say "next"** to move to the next pointer; say **`review P5.3`** to revisit any pointer anytime.

### Cadence & duration
- **121 pointers** across 11 phases (Phase 0–10).
- At a comfortable 6–8 pointers/week: **~16–20 weeks** to complete.
- Fast lane (10+/week): ~10 weeks. Slow lane is fine — mastery is the only metric.

### Mastery rubric (you are done when you can…)
1. Take any business problem → derive top-3 architecture characteristics with measurable definitions.
2. Choose between architecture styles using structured trade-off analysis and defend it in an ADR.
3. Decompose a monolith (code + data) and design data ownership, sagas, and contracts correctly.
4. Design for failure: name and apply the right stability patterns to a given failure mode.
5. Build the AI stack: eval harnesses, RAG, agents, finetuning decisions — and justify prompt vs RAG vs finetune with an ADR.
6. Architect inference for cost/latency/scale and design feedback loops that continuously improve an AI product.
7. Present and defend a complete architecture in front of a hostile review board (me, playing the part).

### Repository layout
```
curriculum/
├── README.md          ← this file (protocol)
├── CURRICULUM.md      ← master index of all phases & pointers
├── PROGRESS.md        ← checkbox tracker (we tick as we go)
├── phases/            ← ultra-detailed lesson plans, one file per phase
├── lessons/           ← interactive HTML visual guides (the actual lessons — served at http://localhost:8123)
└── artifacts/         ← your portfolio: ADRs, diagrams, code, eval reports, capstones
```

### Delivery format
- **Lessons are visual.** Every pointer gets an interactive HTML guide in `curriculum/lessons/` (graphics, simulations, click-to-explore), served locally at `http://localhost:8123`. Plain text is only for answers to your questions.

### How each lesson plan is structured
Every `phases/phase-XX-*.md` contains:
- **Goal & outcomes** — what mastery looks like at phase end
- **Source mapping** — exact book chapters covered
- **Pointers** — numbered, each with: concepts covered, book section refs, hands-on/artifact
- **Checkpoint** — the graded mini-project
- **Supplementary resources** — repos, papers, docs we'll browse together
