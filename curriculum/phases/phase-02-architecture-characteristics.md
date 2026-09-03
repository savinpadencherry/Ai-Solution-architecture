# Phase 2 — Architecture Characteristics: Defined, Identified, Measured, Governed

**Book:** Fundamentals of Software Architecture, 2nd Ed. — ch. 4 Architecture Characteristics Defined, ch. 5 Identifying, ch. 6 Measuring & Governing, ch. 7 Scope, ch. 8 Component-Based Thinking

**Goal:** Turn fuzzy requirements ("it must be fast and reliable") into measurable, governable architecture characteristics, scoped correctly, and learn to derive components from a domain.

**You are ready for Phase 3 when:** you can extract a prioritized characteristic set from any business scenario and attach at least one fitness function to each characteristic.

---

## Lesson 2.1 — Defining characteristics

### P2.1.1 — What makes something an architecture characteristic
- Concepts: criteria — affects structure, critical to success, design-wide (system-level); explicit vs implicit characteristics; hidden characteristics (users only reveal them when violated); design principles vs architecture characteristics; the "KPIs of architecture" framing.
- Refs: Fundamentals ch.4 §"Architecture Characteristics Defined" & §"Design Principles vs Characteristics".
- Do: Take 10 requirement sentences, classify each: characteristic / principle / neither; mark implicit ones.

### P2.1.2 — The catalog, part 1: operational characteristics
- Concepts: availability, continuity, performance, recoverability, reliability/robustness, safety, scalability. Precise definitions and how they conflict (scalability vs elasticity; reliability vs availability).
- Refs: Fundamentals ch.4 catalog (operational cluster).
- Do: For each characteristic, write a measurable target (e.g., availability → "99.95% monthly SLO, ≤5 min outage/quarter"). This becomes your reusable glossary card deck.

### P2.1.3 — The catalog, part 2: structural & process (cross-cutting) characteristics
- Concepts: configurability, extensibility, installability, leverageability/reuse, localization, maintainability, portability, supportability, upgradeability; plus process characteristics: agility, deployability, testability, fault tolerance. Why "agility" is a composite, not a measurement.
- Refs: Fundamentals ch.4 catalog (structural/process clusters).
- Do: Decompose "agility" and "AI-readiness" (a modern one: model swap-ability, eval-ability, prompt versioning) into measurable primitives.

### P2.1.4 — Characteristic conflicts & the least-worst balance
- Concepts: no system maximizes everything; characteristic synergy/antagonism matrix (security↔performance, scalability↔consistency); the architect's job is a balanced set, not a maxed one; limiting to 3–5 primary characteristics.
- Refs: Fundamentals ch.4 §"Interacting Characteristics"; Hard Parts ch.1 "least worst".
- Do: Build a conflict matrix for 8 characteristics; then pick the top-5 for the Kitchen Flow scenario and defend omissions.

## Lesson 2.2 — Identifying characteristics

### P2.2.1 — Extraction from domain goals, requirements & implicit sources
- Concepts: domain concerns → characteristics (conversion table); reading between requirement lines; implicit sources: expected growth, competitive pressure, compliance/audit, budget cycle; distinguishing "real" vs "wishlist" characteristics.
- Refs: Fundamentals ch.5 §"Capturing Architecture Characteristics in ADRs" + extraction sections.
- Do: Run a mock stakeholder interview (I play the CEO of Kitchen Flow); extract characteristics from my rambling, then ADR the result.

### P2.2.2 — Prioritization & the "3–5 rule"
- Concepts: why architects must prune; criteria: business criticality, measurability, cost to achieve; expressing priorities as measurable KPIs tied to characteristics; documenting in ADR.
- Refs: Fundamentals ch.5.
- Do: ADR-0003: "Primary architecture characteristics for Kitchen Flow v1" with measurable definitions and rejected candidates (with reasons).

## Lesson 2.3 — Measuring & governing characteristics

### P2.3.1 — Measuring operational characteristics
- Concepts: SLO/SLA/SLI hierarchy; latency percentiles (p50/p95/p99) vs averages; throughput vs capacity; availability math (nines, error budgets); how monitoring defines "measured".
- Refs: Fundamentals ch.6 (operational measurement); Release It! ch.1 (uptime demands) as cross-ref.
- Do: Write an SLO sheet for Kitchen Flow: 5 SLIs with targets, measurement method, and error budget policy.

### P2.3.2 — Measuring structural characteristics with fitness functions
- Concepts: fitness function = objective integrity assessment of a characteristic; atomic vs holistic; temporal (regression tests as time dimension); coupling metrics as fitness; page-load time, cyclomatic complexity, cycles detection.
- Refs: Fundamentals ch.6 §"Architectural Fitness Functions"; Hard Parts ch.1 recap.
- Do: Implement 3 fitness functions: (1) cycle detection, (2) layer-violation check (ArchUnit/NetArchTest/import-linter), (3) a latency budget test in CI.

### P2.3.3 — Governance: from review boards to automated governance
- Concepts: what architecture governance is; manual review boards vs fitness-function-driven governance; evolutionary architecture fit; the "important vs urgent" framing; who owns governance in team topologies.
- Refs: Fundamentals ch.6 §"Governance and Fitness Functions".
- Do: Write a governance one-pager for Kitchen Flow: which characteristics are automated, which are human-reviewed, cadence.

### P2.3.4 — Scope of characteristics: the quantum connection
- Concepts: characteristics apply at component scope, not just system scope; different parts of a system need different characteristics; scope + coupling preview; architecture quantum definition (independently deployable + high functional cohesion + synchronous coupling) — full treatment in Phase 5.
- Refs: Fundamentals ch.7; Hard Parts ch.2 preview.
- Do: Map each of Kitchen Flow's 5 components to the 2 characteristics that matter *locally*; justify the mismatch vs system scope.

## Lesson 2.4 — Component-based thinking

### P2.4.1 — Component identification: actor/actions & event storming
- Concepts: components vs modules; domain-driven boundaries; actor/actions approach (roles → actions → components); event storming walkthrough (domain events → commands → aggregates); project vs application ownership.
- Refs: Fundamentals ch.8 §"Component Identification".
- Do: Run a 45-minute mini event storm on Kitchen Flow; photograph the wall (or Miro); extract ≥6 components.

### P2.4.2 — Component granularity, coupling & composition
- Concepts: right-sizing components; acyclic component graphs; component composition patterns; the flow: domain entity → module → component → service (later); measuring component-level characteristics.
- Refs: Fundamentals ch.8 §"Component Granularity/Coupling/Composition"; Hard Parts ch.5 preview.
- Do: Draw your component graph, verify acyclicity, mark coupling strengths; write one fitness function guarding a component boundary.

---

## Checkpoint 2 (graded)
For the **Insurance Claims** scenario (I supply details): deliver `artifacts/checkpoint-02/`:
1. ADR: prioritized characteristics (3–5) with measurable targets + explicitly rejected ones.
2. SLO sheet + 3 working fitness functions in a sample repo.
3. Event-storm → component graph with acyclicity proof.
Pass bar: every characteristic has a number attached; every component boundary has a governance story.

## Resources
- SRE workbook (SLO/error budgets): sre.google/workbook
- ArchUnit, NetArchTest, import-linter, SonarQube docs
- Event storming primer (Brandolini's "Introducing EventStorming" — free online book)
