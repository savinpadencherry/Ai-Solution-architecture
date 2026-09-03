# Phase 1 — Architectural Thinking & Modularity

**Book:** Fundamentals of Software Architecture, 2nd Ed. — Part I: ch. 1 Introduction, ch. 2 Architectural Thinking, ch. 3 Modularity

**Goal:** Internalize the architect's mindset — architecture vs design, breadth over depth, trade-off analysis, business drivers — and master modularity as a measurable engineering property (cohesion, coupling, connascence, distance from the main sequence).

**You are ready for Phase 2 when:** you can take an unfamiliar system, place any decision on the architecture-vs-design spectrum, and measure its modularity with real metrics.

---

## Lesson 1.1 — What software architecture actually is

### P1.1.1 — Definitions and the structure-behavior-connection triad
- Concepts: multiple competing definitions (structure of the system, things hard to change, 4+1 views, ISO/IEC/IEEE 42010); the three questions every architecture must answer: how is it **structured** (components), how does it **behave** (runtime interaction), how do parts **connect** (interfaces/contracts).
- Refs: Fundamentals ch.1 §"Defining the Architecture".
- Do: Take any app you know; write its structure/behavior/connection summary in 10 lines.

### P1.1.2 — Laws of software architecture
- Concepts: 1st law — *everything in software architecture is a trade-off*; corollary — "why is this a trade-off?" beats "why did you do this?"; 2nd law — *why is more important than how*. How these two laws generate everything else in the curriculum.
- Refs: Fundamentals ch.1 §"Laws of Software Architecture" (and ch.27 "Laws Revisited" preview).
- Do: Write ADR-0002 for a past decision of yours, explicitly naming the trade-off and the "why".

### P1.1.3 — What architects do: the 8 core expectations
- Concepts: define the architecture & guide the team; analyze it continuously; identify & mitigate risks (the architect as risk manager); keep current with the ecosystem; drive business-domain knowledge; ensure alignment between architecture & business goals; be an enabler of the team (not a gatekeeper); coach & mentor. Architect personality types: control-freak vs armchair — and the dysfunctional middle.
- Refs: Fundamentals ch.1 §"Expectations of an Architect".
- Do: Rate yourself 1–5 on each of the 8 expectations; pick the weakest two as personal themes for the curriculum.

## Lesson 1.2 — Architecture vs design & the architect's knowledge

### P1.2.1 — The architecture–design spectrum
- Concepts: three criteria that move a decision toward "architectural": strategic vs tactical, level of effort to change, significance of trade-offs. The spectrum is a gradient, not a wall; ownership and responsibility follow position.
- Refs: Fundamentals ch.2 §"Architecture Versus Design".
- Do: Sort 12 decision cards I'll give you (e.g., "choose a UI framework", "adopt microservices", "rename a field", "choose sync vs async messaging") onto the spectrum; defend placements.

### P1.2.2 — Technical breadth vs depth; the knowledge pyramid
- Concepts: the pyramid (know / know-you-don't-know / don't-know-you-don't-know); developers maintain depth, architects expand breadth; expertise atrophies — that's OK; two dysfunctions: trying to keep depth everywhere, and **stale expertise**.
- Refs: Fundamentals ch.2 §"Technical Breadth".
- Do: List 10 technologies in each pyramid layer; pick 3 from "don't know you don't know" — I'll build mini-briefings on them later in the curriculum.

### P1.2.3 — Architect antipatterns: Frozen Caveman & the Bottleneck Trap
- Concepts: Frozen Caveman = reverting to a pet irrational concern (the "what if we lose Italy?" story); Bottleneck Trap = architect owning critical-path code and starving the team. Antidotes: realistic risk assessment, delegating critical path, POCs, tech debt, bug fixes, automation, code reviews.
- Refs: Fundamentals ch.2 §"Frozen Caveman antipattern", §"Balancing Architecture and Hands-On Coding".
- Do: Write down 2 of your own "frozen caveman" instincts. We'll test them with trade-off analysis later.

### P1.2.4 — Analyzing trade-offs deeply (the auction case)
- Concepts: full analysis of queue (point-to-point) vs topic (pub-sub): extensibility, decoupling, security/wiretapping, homogeneous vs heterogeneous contracts, monitoring/autoscaling; AMQP exchange-vs-queue nuance; "it depends" made concrete via business drivers.
- Refs: Fundamentals ch.2 §"Analyzing Trade-offs" (Figures 1-6 → 1-8).
- Do: Rebuild Table 1-1 (topic advantages/disadvantages) from memory, then defend a choice under three scenarios: fintech auction, internal telemetry bus, regulated audit system.

### P1.2.5 — Business drivers → architecture characteristics
- Concepts: architects translate business goals into characteristics (scalability, performance, availability…); requires domain knowledge + stakeholder relationships; the four-chapter characteristics deep-dive preview (Phases 2).
- Refs: Fundamentals ch.2 §"Understanding Business Drivers".
- Do: Interview script: 10 questions you'd ask a CEO/CPO to extract characteristics from business drivers.

## Lesson 1.3 — Modularity as a measurable property

### P1.3.1 — Modularity vs granularity; defining modules
- Concepts: modularity = logical grouping of related code; granularity = size of the pieces ("embrace modularity, beware of granularity"); packaging mechanisms across languages (package/namespace/jar hell history); how poor granularity births Distributed Monolith / Big Ball of Distributed Mud.
- Refs: Fundamentals ch.3 §"Modularity Versus Granularity", §"Defining Modularity".
- Do: Diagram a system you know; mark where granularity is wrong (too big/too small) and what pain it causes.

### P1.3.2 — Cohesion: the 7 levels
- Concepts: functional → sequential → communicational → procedural → temporal → logical → coincidental (best→worst); Constantine's warning (dividing a cohesive module increases coupling); StringUtils as logical cohesion.
- Refs: Fundamentals ch.3 §"Cohesion".
- Do: Classify 6 real modules from a repo; propose how to raise the two worst by one level.

### P1.3.3 — Coupling metrics: abstractness, instability, distance from main sequence
- Concepts: afferent/efferent coupling; abstractness (A) = abstract elements ÷ total; instability (I) = efferent ÷ (efferent + afferent); the main sequence (I + A = 1); normalized distance from main sequence D′; zone of pain vs zone of uselessness.
- Refs: Fundamentals ch.3 §"Coupling", §"Metrics: Abstractness, Instability…", §"Distance from the Main Sequence".
- Do: Compute A, I, and D′ for 3 packages (by hand or JDepend/pymetrics) and plot them on the main sequence graph.

### P1.3.4 — Connascence: the fine-grained coupling taxonomy
- Concepts: connascence = two components change together; static forms (name, type, meaning, position, algorithm) vs dynamic forms (execution/order, timing, values, identity); stronger forms → weaker forms as distance grows; why connascence beats raw coupling counts.
- Refs: Fundamentals ch.3 §"Connascence".
- Do: Find one instance of each static connascence type in a real codebase; refactor one to a weaker form.

### P1.3.5 — From modules to components
- Concepts: component = deployment artifact with an entry point; the role of the component in architecture thinking; measuring component relationships; preview of component-based decomposition (Hard Parts ch.4–5).
- Refs: Fundamentals ch.3 §"From Modules to Components".
- Do: Whiteboard your current project as components + edges; mark each edge with its connascence type.

---

## Checkpoint 1 (graded)
Given the **Kitchen Flow** scenario (I'll supply: a food-delivery app with ordering, routing, and payment), produce in `artifacts/`:
1. Top-3 candidate architecture characteristics derived from business drivers, each with a one-line measurable definition.
2. A trade-off analysis (canvas) for one real decision in the scenario.
3. A modularity report: cohesion classifications, A/I/D′ for its components, and the two riskiest connascence instances with refactoring proposals.
Pass bar: I'll interrogate you as a skeptical CTO; you must survive 10 minutes of "why?" without hand-waving.

## Resources
- `pymetrics` / JDepend / ArchUnit docs; connascence.io (Meilir Page-Jones taxonomy)
- Martin Fowler, "Who Needs an Architect?" (the "hard to change" definition)
