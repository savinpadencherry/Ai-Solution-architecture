# Phase 4 — Architect Techniques: Patterns, Decisions, Risk, Diagrams, Teams, Career

**Book:** Fundamentals of Software Architecture, 2nd Ed. — Part III: ch. 20 Architectural Patterns, ch. 21 Architecture Decisions, ch. 22 Analyzing Architecture Risk, ch. 23 Diagramming, ch. 24 Making Teams Effective, ch. 25 Negotiation & Leadership, ch. 26 Architectural Intersections, ch. 27 Laws Revisited, ch. 28 Developing a Career Path (+ Appendices)

**Goal:** Master the architect's day-2 toolkit: patterns, decision records at production quality, risk storming, C4 diagramming, team leadership, negotiation, and career strategy. These skills are what separate "knows architecture" from "architect".

**You are ready for Phase 5 when:** you produce ADRs, risk assessments, and C4 diagrams that would pass a real review board.

---

## Lesson 4.1 — Patterns & decisions

### P4.1.1 — Architectural patterns catalog
- Concepts: pattern = reusable solution at the design level within a style; catalog walkthrough (anti-corruption layer, aggregator, API gateway / backends-for-frontends, circuit breaker — full depth in Phase 6, CQRS, event sourcing, sidecar/service mesh, strangler fig, saga — depth in Phase 5, specification, retry/steady state…); pattern-vs-style placement.
- Refs: Fundamentals ch.20.
- Do: Pattern cards: for 10 patterns write — problem, solution, trade-offs, the style(s) where it lives. Start `artifacts/pattern-cards.md` (grows through Phases 5–6).

### P4.1.2 — Architecture decisions: significance & antipatterns
- Concepts: what makes a decision architecturally significant (structure-changing, hard to reverse, high trade-off significance); the three ADR antipatterns: **Covering Your Assets** (deferring/obfuscating decisions), **Groundhog Day** (remaking decisions without records), **Email-Driven Architecture** (decisions buried in threads).
- Refs: Fundamentals ch.21 §antipatterns.
- Do: Autopsy: find one real Groundhog Day from your career; write the ADR that should have existed.

### P4.1.3 — ADR mastery: structure, storage, standards, LLMs
- Concepts: ADR anatomy (title, status, context, decision, consequences); ADR numbering & immutability (supersede, don't edit); storing ADRs in the codebase; ADRs as living documentation & standards ("we use X because ADR-7"); ADRs for existing/legacy systems; using generative AI to draft ADRs — and why the human still owns the "why".
- Refs: Fundamentals ch.21 (structure → LLM sections).
- Do: Upgrade our ADR template to MADR format; write ADR-0007 (any significant Kitchen Flow decision) at production quality; then have me draft an ADR via "generative AI" and critique what I get wrong without domain input.

## Lesson 4.2 — Risk & diagrams

### P4.2.1 — Analyzing architecture risk & risk storming
- Concepts: risk = impact × likelihood; risk matrix (high/medium/low grid); areas of risk per characteristic; **risk storming** exercise: individual identification → collaborative consolidation → mitigation ADRs; when to re-storm (ecosystem changes).
- Refs: Fundamentals ch.22.
- Do: Risk-storm Kitchen Flow solo (I add "other perspectives"), produce a risk register + 2 mitigation ADRs.

### P4.2.2 — Diagramming: the C4 model
- Concepts: context, container, component, code zoom levels; notation discipline (rectangles/arrows/labels), diagram-per-concern, diagram-as-code (Mermaid C4, Structurizr); how diagrams + ADRs together form architecture documentation; anti-patterns (diagram soup, legend-free diagrams).
- Refs: Fundamentals ch.23.
- Do: Produce C1–C3 diagrams for Kitchen Flow as Mermaid code in `artifacts/diagrams/`; I'll red-team the diagrams for ambiguity.

## Lesson 4.3 — People skills

### P4.3.1 — Making teams effective: the architect as enabler
- Concepts: constraints vs freedom; the control-freak gravity well; developer productivity as an architecture characteristic; architecture briefings & decision broadcasting; coaching through pairing on hard problems; measuring team effectiveness around the architecture (cycle time, deploy frequency — DORA as evidence).
- Refs: Fundamentals ch.24.
- Do: Write your "architecture briefing memo" template + a 5-slide internal tech-talk plan introducing ADRs to a team.

### P4.3.2 — Negotiation skills for architects
- Concepts: why negotiation is a core architect skill (every trade-off is a negotiation); information gathering before persuading; framing decisions in business-driver language; making trade-offs visible to stakeholders; BATNA thinking; negotiating scope of characteristics with product owners; the "yes, if…" technique.
- Refs: Fundamentals ch.25.
- Do: Role-play: I'm the CMO demanding "real-time analytics on everything, this quarter" — negotiate the characteristics down to something buildable; log the outcome as ADR-0008.

### P4.3.3 — Leadership principles
- Concepts: the 7 principles of architecture leadership (from Fundamentals): be pragmatic, center decisions on guiding principles, challenge the status quo within the law, lead by influence not authority, integrate hands-on, own the consequences, lead the risk conversation. Congruence between stated principles and actual decisions.
- Refs: Fundamentals ch.25 §leadership.
- Do: Self-audit: score yourself on the 7; pick one to practice deliberately for the rest of the curriculum (I'll hold you to it).

### P4.3.4 — Architectural intersections (architecture meets everything)
- Concepts: where architecture intersects adjacent disciplines — data architecture, DevOps/platform engineering, security, enterprise architecture, and **AI/ML architecture**; who owns what at the boundary; the AI solution architect as the bridge role (this curriculum's endgame).
- Refs: Fundamentals ch.26.
- Do: Draw your org's discipline-intersection map; mark where AI decisions will get stuck without an architect owning the seam.

### P4.3.5 — Laws revisited & career path
- Concepts: re-derivation of the two laws after everything so far; the architect career lattice (individual contributor paths, breadth-building tactics, portfolio construction: ADRs, diagrams, katas, talks); keeping current without the depth trap; your personal learning operating system.
- Refs: Fundamentals ch.27, ch.28, Appendix B.
- Do: Draft your 12-month architect development plan (after this curriculum, what next); set up your portfolio skeleton in `artifacts/`.

---

## Checkpoint 4 (graded)
**"Review board day":** I assemble a hostile mock architecture review board (I play 3 stakeholders: CFO worried about cost, SRE worried about 3am pages, CISO worried about data). You present Kitchen Flow: C4 diagrams, ADR set, risk register, style choice. You must:
- defend 3 ADRs live, survive 2 rounds of pushback each
- negotiate one scope change live
Pass bar: board signs off or gives you one bounded revision.

## Resources
- c4model.com; Structurizr; Mermaid C4 syntax
- The MADR project (markdown ADRs)
- DORA research (dora.dev) for team-effectiveness measures
