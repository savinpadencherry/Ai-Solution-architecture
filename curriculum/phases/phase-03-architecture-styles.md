# Phase 3 — Architecture Styles: The Full Catalog

**Book:** Fundamentals of Software Architecture, 2nd Ed. — Part II: ch. 9 Foundations, ch. 10–18 the styles, ch. 19 Choosing the Appropriate Style

**Goal:** Command the complete style catalog — for each style: topology, taxonomy, trade-offs, data architecture, governance, risks, team considerations — and choose styles via structured analysis rather than fashion.

**Uniform style-analysis template (we apply to every style):**
Topology → Taxonomy → Why you'd pick it → Trade-offs (advantages/disadvantages) → Data topology → Governance & risks → Team topology impact → Best-fit characteristics → Killer failure modes.

**You are ready for Phase 4 when:** you can diagram any style from memory, name its 3 signature trade-offs, and argue for/against it for a given scenario using characteristics.

---

## Lesson 3.1 — Foundations

### P3.1.1 — Styles vs patterns; monolith vs distributed
- Concepts: architecture style = coarse-grained family (the shape); pattern = finer-grained solution within a style; the big taxonomy split: monolithic (single deploy unit, in-process calls) vs distributed (network calls, remote data access); the **8 fallacies of distributed computing** — the backbone for everything in Phase 5.
- Refs: Fundamentals ch.9; Hard Parts ch.2 preview.
- Do: Classify 8 real systems into monolith/distributed; list which fallacies each one has already fallen for.

## Lesson 3.2 — Monolithic styles

### P3.2.1 — Layered architecture
- Concepts: layers of separation (presentation/business/persistence/database); topology variants (open vs closed layers, layer of isolation); sink-hole antipattern (80/20 rule); architecture sinkhole when requests pass through layers doing nothing; trade-offs (simplicity, low cost vs poor agility/testability/deployability, structural sinkhole); modular monolith as the modern fix.
- Refs: Fundamentals ch.10.
- Do: Diagram a layered system; measure its sinkhole ratio; propose 2 tactics to reduce it.

### P3.2.2 — Modular monolith
- Concepts: strictly enforced module boundaries inside one deployable; module independence rules; benefits vs layered (better modularity governance via fitness functions); why it's the recommended default starting point in modern practice; path to extraction later.
- Refs: Fundamentals ch.11.
- Do: ADR-0004: "Start Kitchen Flow as modular monolith, not microservices" — with migration triggers defined as measurable conditions.

### P3.2.3 — Pipeline architecture
- Concepts: pipes & filters topology (filters: producer/transformer/tester/consumer; pipes: one-directional point-to-point); topology variants; ETL/systems-of-record examples; trade-offs (simplicity, modularity, transformability vs performance, filter granularity, data loss across filters).
- Refs: Fundamentals ch.12.
- Do: Design an ingestion pipeline for clickstream data using the style template; note where AI/ML feature pipelines plug in (preview of Phase 8).

### P3.2.4 — Microkernel (plug-in) architecture
- Concepts: core system + plug-in components; registry; contracts between core & plug-ins; standalone vs web variants; product software (IDEs, browsers) vs custom enterprise; trade-offs (extensibility, feature isolation vs scalability/discoverability of plug-ins, contract governance).
- Refs: Fundamentals ch.13.
- Do: Design an AI-model plug-in architecture: core inference hub + swappable model plug-ins (preview: Phase 9 model routing). ADR the contract.

## Lesson 3.3 — Precursor distributed styles

### P3.3.1 — Service-based architecture
- Concepts: macro-layered services (0.5–12 services), separately deployed, DB-per-service (shared vs dedicated database variants, including domain/schema-level separation); class-level vs API-level coupling; contract sharing & duplication; granularity governance; trade-offs (testability, deployability, cost vs some coordination overhead).
- Refs: Fundamentals ch.14.
- Do: ADR-0005: split Kitchen Flow into N service-based services — justify N and the data strategy (this ADR evolves through Phase 5).

### P3.3.2 — Event-driven architecture (broker & mediator)
- Concepts: broker topology (lightweight, fully decoupled, fire-and-forget) vs mediator topology (event mediator orchestrates, error handling, recoverability); request/response vs async fire-and-forget; **high architectural scalability**; the event-driven data problem (data gravity — preview Phase 5); error handling & recoverability; broadcast vs message persistence; trade-offs summary (superb scalability/elasticity vs workflow/error handling complexity, eventual consistency).
- Refs: Fundamentals ch.15.
- Do: Design both topologies for "order placed → notify, invoice, analytics"; build the trade-off table; pick per business driver weighting. Include an error/replay story.

### P3.3.3 — Space-based architecture
- Concepts: processing units (with embedded in-memory grid), virtual middleware (messaging grid, data grid, processing grid, deployment manager); how it removes the database bottleneck; elasticity mechanics; trade-offs (extreme elasticity, performance vs complexity, cost, data consistency, testing difficulty); when it's the right answer (bursty auction/ticket-sale loads).
- Refs: Fundamentals ch.16.
- Do: Sketch the space-based topology for a flash-sale system; quantify what "no direct database writes" buys you — and what it costs.

### P3.3.4 — Orchestration-driven service-oriented architecture
- Concepts: taxonomy (business process orchestration, service registry, enterprise service bus, messaging, service composition, integration hub, orchestration engine, process manager, choreography); reuse as the driving force — and the coupling price; why it fell from dominance (Hard Parts ch.1 ecosystem story); cloud considerations; when legacy SOA still matters.
- Refs: Fundamentals ch.17.
- Do: Explain in one page why reuse-centric orchestration lost to microservices — using the coupling/quanta vocabulary (preview P5.2).

## Lesson 3.4 — Microservices

### P3.4.1 — Microservices deep-dive (part 1: topology & taxonomy)
- Concepts: distributed, separately deployed services; single bounded context per service; granularity & the shared-domain antipattern; data architecture: every service owns its data (integration vs data ownership); API layers & versioning; operating model (distributed capabilities, DevOps/NoOps, CI/CD maturity).
- Refs: Fundamentals ch.18 (topology/data/operating model sections).
- Do: Rebuild the Sysops Squad monolith topology from Hard Parts ch.1 as microservices on paper; list everything that gets harder.

### P3.4.2 — Microservices deep-dive (part 2: trade-offs & governance)
- Concepts: elasticity, scalability, agility, deployability, fault tolerance vs cost, complexity, eventual consistency, operational overhead; fitness functions for microservices governance (deployment pipeline gates, contract testing); team topology: independent streams; service ownership & the "you build it you run it" model.
- Refs: Fundamentals ch.18 (trade-offs, governance, team sections).
- Do: Write the "microservices is wrong for this project" memo — argue against microservices for a 5-person team with 40k users. Both ADRs get reused in Phase 5.

## Lesson 3.5 — Choosing styles

### P3.5.1 — The style decision framework
- Concepts: derive characteristics first, then match styles; style comparison matrix; monolith-first strategy & migration readiness; service granularity as style-level decision; domain-driven design's role; the hybrid reality (styles coexist inside one enterprise).
- Refs: Fundamentals ch.19.
- Do: Comparison matrix: score all 9 styles against the top-5 Kitchen Flow characteristics; pick with weighting; defend in ADR-0006.

### P3.5.2 — Kata lab #1: full style selection under fire
- Concepts: applying the whole Phase 1–3 stack under time pressure.
- Do: Architecture kata: pick one from nealford.com/katas (e.g., "Where's My Ride?"); produce ADR + style choice + topology sketch + characteristics. I'll play the sponsor shooting holes in it.

---

## Checkpoint 3 (graded)
`artifacts/checkpoint-03/`: Complete style-analysis one-pagers (using the template) for **all 9 styles**, each hand-drawn or Mermaid-diagrammed from memory (no peeking), plus the Kata lab artifact with my review notes addressed.

Pass bar: given any random business scenario, you can rank your top-2 styles with a defensible trade-off table in under 15 minutes.

## Resources
- nealford.com/katas — architecture katas (we'll do several)
- learnmicroservices.io, developer.jboss "Monolith to Microservices" refs; Fowler's "MonolithFirst" essay
- Fallacies of Distributed Computing (original list + Peter Deutsch)
