# Phase 0 — Setup, Baseline & Architect's Toolkit

**Goal:** Set up the learning environment, establish your baseline, and master the two tools we'll use constantly: trade-off analysis and Architecture Decision Records.

**Sources:** All four books (prefaces + ADR/trade-off material). Hard Parts ch. 1 (ADR + fitness functions intro).

**Outcomes:** Working workspace, ADR template + repo, baseline self-assessment, your personal "knowledge pyramid" mapped.

---

## Pointers

### P0.1 — Orientation & the four-book map
- Concepts: why these 4 books = the full AI solution architect skill stack; how the books interlock (Fundamentals = mindset → Hard Parts = distributed decisions → Release It = production → AI Engineering = the AI layer on top).
- Read: Prefaces of all four books (skim, we extracted the structure already).
- Do: Write a one-paragraph statement of what YOU think an AI Solution Architect does. We'll rewrite it at the end — compare.

### P0.2 — Baseline self-assessment
- Concepts: Fundamentals 2nd ed. Appendix A self-assessment questions; Richards & Ford's knowledge pyramid (stuff you know / know you don't know / don't know you don't know); the architect skill matrix.
- Do: Take the self-assessment honestly; map your current knowledge pyramid for: architecture styles, distributed systems, data, production ops, AI/LLMs. This is your "before" picture.

### P0.3 — Trade-off analysis, the core discipline
- Concepts: "Architecture is the stuff you can't Google"; least-worst design (Hard Parts ch.1); every answer is "it depends" *on what*; the trade-off canvas: context → options → advantages → disadvantages → business-driver weighting → decision.
- Read: Fundamentals ch.1 "Analyzing Trade-offs" (auction queue-vs-topic example); Hard Parts ch.1 intro.
- Do: Run the full trade-off canvas on the auction system example (topics vs queues) — then re-run it with 3 different business driver weightings and watch the answer flip.

### P0.4 — ADRs + fitness functions toolkit
- Concepts: ADR = immutable short record of a decision (context/decision/consequences); why ADRs beat email/wiki pages; ADR antipatterns preview (covering your assets, email-driven architecture, groundhog day); fitness function = any mechanism performing an objective integrity assessment of an architecture characteristic (atomic vs holistic).
- Read: Hard Parts ch.1 §"Architecture Decision Records" + §"Architecture Fitness Functions"; Fundamentals ch.21 "Architecture Decisions" (skim now, deep-dive in P4.2).
- Do: Create `artifacts/adr/` using the Nygard-style template (Title, Status, Context, Decision, Consequences) + write ADR-0001: "Adopt this curriculum's ADR process for all architecture decisions." Then write a tiny fitness function (any language, e.g., a test that fails if two modules import each other) and wire it into a repo.

---

## Checkpoint 0
- A working `artifacts/adr/` repo with ADR-0001, one fitness function committed and passing, and your baseline self-assessment saved to `artifacts/00-baseline.md`.

## Resources we'll browse
- https://github.com/adr/madr — ADR templates
- https://github.com/chiphuyen/aie-book — AI Engineering repo (resources per chapter)
- Architecture katas: https://nealford.com/katas/list.html (we'll use these in Phase 3+)
