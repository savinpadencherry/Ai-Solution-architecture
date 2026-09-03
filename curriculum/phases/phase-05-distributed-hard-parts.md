# Phase 5 — Distributed Architecture: The Hard Parts

**Book:** Software Architecture: The Hard Parts — ch. 1–15 (Parts I & II: Pulling Things Apart, Putting Things Back Together)

**Running case study:** the **Sysops Squad saga** — we follow the book's ticketing monolith through its full decomposition journey, and we run our own parallel track on Kitchen Flow.

**Goal:** Master the actual hard problems of distributed architecture: coupling analysis, decomposition (code AND data), granularity, reuse, data ownership, distributed data management, concurrency, transactional seams, contracts, analytical data separation, and the meta-skill of trade-off analysis itself.

**You are ready for Phase 6 when:** you can take a monolith and produce a defensible decomposition plan — code, data, transactions, contracts — with fitness functions and ADRs for every decision.

---

## Lesson 5.1 — The distributed mindset

### P5.1.1 — No best practices, only trade-offs; the saga begins
- Concepts: why architect problems are snowflakes; least-worst design as doctrine; ADR + fitness functions as the decision machinery; the Sysops Squad story (monolith pain: ticketing outages, poor deploys, single database); operational vs analytical data — the split that generates half this book's problems.
- Refs: Hard Parts ch.1 (incl. §"Introducing the Sysops Squad Saga").
- Do: Draw Sysops Squad as-is (components + single DB + data model); list its top-3 pains; predict which decomposition decisions will hurt most.

### P5.1.2 — Discerning coupling: architecture quanta
- Concepts: architecture quantum = independently deployable + high functional cohesion + high static coupling + **synchronous (dynamic) coupling**; static vs dynamic coupling; synchronous communication merges quanta, async decouples them; shared database as the ultimate coupling point; finding quanta in any system.
- Refs: Hard Parts ch.2.
- Do: Identify the quanta of Sysops Squad pre-migration (spoiler: it's one); then identify quanta of your current workplace system.

### P5.1.3 — Architectural modularity drivers (and costs)
- Concepts: the five drivers — maintainability, testability, deployability, scalability, availability/fault tolerance — each mapped to measurable criteria; the cost side: complexity tax, operational overhead, eventual consistency, distributed transactions; the business case: when NOT to break up (the "creating a business case" section).
- Refs: Hard Parts ch.3.
- Do: Score Kitchen Flow on all 5 drivers before/after hypothetical decomposition; build the one-page business case for/against splitting (ADR-0009).

## Lesson 5.2 — Pulling things apart

### P5.2.1 — Is the code base decomposable?
- Concepts: reading a codebase's fitness for decomposition: component cohesion metrics (afferent/efferent, abstractness, instability, D′ from Phase 1 — now weaponized); low instance & high D′ clusters as extraction candidates; composites of quick wins vs deep tangles.
- Refs: Hard Parts ch.4 §"Is the Code Base Decomposable?"
- Do: Run metrics on the sample repo; produce a "decomposability heatmap" (component × metrics table).

### P5.2.2 — Decomposition strategies: component-based vs tactical forking
- Concepts: incremental component-based decomposition (prune/refactor first, extract later) vs **tactical forking** (copy the monolith, chop, delete dead code) — and its trade-offs (speed vs duplicated logic); when each is right (business pressure, unclear domain).
- Refs: Hard Parts ch.4 §"Component-Based Decomposition", §"Tactical Forking".
- Do: ADR-0010: choose the decomposition approach for Sysops Squad's survey feature; defend against my counter-arguments.

### P5.2.3 — The six component decomposition patterns
- Concepts: **Identify & Size Components** (dependencies before sizing), **Gather Common Domain Components** (shared code becomes its own component), **Flatten Components** (orphaned classes die), **Determine Component Dependencies** (commit-order extraction graph), **Create Component Domains** (group components into domains), **Create Domain Services** (the final extraction step); fitness functions governing each pattern (ArchUnit examples).
- Refs: Hard Parts ch.5 (all six patterns).
- Do: Apply all six patterns, in order, to the sample codebase — one commit per pattern, each with its governance test.

### P5.2.4 — Pulling apart operational data: disintegrators vs integrators
- Concepts: data disintegrators (privacy/security, table chatter, scaling against storage, multiple storage technologies, single points of contention, geographic dispersion, library/package/OS dependencies) vs data integrators (cross-domain joins, less distinct tables, shared read-only data, shared high-write data); schema-to-domain mapping.
- Refs: Hard Parts ch.6 §"Data Decomposition Drivers".
- Do: For Sysops Squad's database, classify every major table under disintegrators/integrators; produce the decomposition justification one-pager.

### P5.2.5 — The 5-step data decomposition + database type selection
- Concepts: analyze DB → assign tables to data domains → separate connections → move schemas to separate servers → switch over (sequencing & risk per step); database type landscape: relational, key-value, document, column family, graph, NewSQL, cloud native, time series — and their characteristic sweet spots (polyglot persistence).
- Refs: Hard Parts ch.6 §"Decomposing Monolithic Data" + §"Selecting a Database Type".
- Do: Execute the 5-step plan on paper for Sysops Squad; then ADR-0011: pick DB types per domain (defend at least one non-relational choice).

### P5.2.6 — Service granularity: disintegrators, integrators, and balance
- Concepts: granularity disintegrators (service scope/function, code volatility, scalability & throughput, fault tolerance, security, extensibility) vs integrators (database transactions, data relationships, workflow/choreography, shared code); finding the right balance; granularity as the #1 misjudged decision in distributed systems.
- Refs: Hard Parts ch.7.
- Do: Granularity analysis for the ticket-assignment and customer-registration cases (from the saga); ADR-0012: service boundaries with disintegrator/integrator justification table.

## Lesson 5.3 — Putting things back together

### P5.3.1 — Reuse patterns: replication, library, service, sidecar
- Concepts: the four reuse approaches: **code replication** (fast, drift risk), **shared library** (compile-time coupling, versioning strategies — transitive dependency hell), **shared service** (runtime coupling: change risk, performance, scalability, fault tolerance), **sidecars/service mesh** (operational reuse at the platform layer); reuse via platforms; "reuse is derived via abstraction but operationalized by slow rate of change".
- Refs: Hard Parts ch.8.
- Do: Reuse decision tree for: notification logic, auth, logging, address validation; ADR-0013 with per-capability choice + versioning policy.

### P5.3.2 — Data ownership: single, common, joint
- Concepts: assigning ownership per table (single = easy; common = assign to most-write; joint = the hard one); joint-ownership techniques: **table split**, **data domain** (customer/contact), **delegate** (call-through ownership), plus **service consolidation**; mapping to access patterns.
- Refs: Hard Parts ch.9.
- Do: Ownership map for Sysops Squad post-split: every table gets an owner + technique where joint; defend two.

### P5.3.3 — Distributed transactions: ACID's collapse & sagas
- Concepts: why ACID dies across services; the contract/rollback problem (Figure 9-x: error on billing insert); BASE & eventual consistency; the **saga pattern** family: choreography vs orchestration sagas, compensating updates; semantic locks, commutative updates; when to use 2PC/XA (rarely) vs redesign.
- Refs: Hard Parts ch.9 §"Distributed Transactions" + ch.12 "Transactional Seams".
- Do: Implement a mini saga in code (order → payment → shipment) in your language of choice, with a compensating-action failure path; test it.

### P5.3.4 — Distributed data: caching, synchronization & consistency patterns
- Concepts: **cache-read** vs **cache-write** (write-through) patterns and their trade-offs; event-driven data synchronization (publishing change events); **polling publish** (querying change via timestamp/version — and its staleness/DB-load trade-offs); **transactional outbox** (atomic write + event via outbox table + relay); the **bullwhip effect** of propagated staleness; replication topologies.
- Refs: Hard Parts ch.10 "Distributed Data".
- Do: For the customer→ticketing data flow, implement transactional outbox (schema + relay pseudocode); explain where bullwhip would bite and mitigate it.

### P5.3.5 — Managing decoupled concurrency: orchestration vs choreography
- Concepts: workflow scale & error handling; **choreography** (event-driven, no central owner — great decoupling, hard workflow management, communication-link explosion on errors, domain vs technical partitioning) vs **orchestration** (central workflow owner, state management, recoverability); front controller as domain-owned workflow state; choosing per-workflow, not per-system.
- Refs: Hard Parts ch.11 "Managing Decoupled Concurrency".
- Do: Model ticket-assignment workflow both ways; write ADR-0014 choosing per workflow segment; diagram the error paths for both.

### P5.3.6 — Transactional seams & isolation patterns
- Concepts: the transactional seam = the boundary where ACID ends; **adaptive transactional islands** (in-memory transactions where possible, compensations across); static vs dynamic seam placement; background vs synchronous compensation; seam placement rules via granularity revisited.
- Refs: Hard Parts ch.12.
- Do: Mark every seam on the Sysops Squad service diagram; for each: sync vs background compensation, and the user-facing story when compensation fails.

### P5.3.7 — Contracts: strict vs loose, shared vs standalone
- Concepts: contracts as the API of the architecture; **strict** (schema-enforced, e.g., protobuf/XML schema) vs **loose** (JSON convention, OpenAPI-as-documentation); **shared contract** (common schema — coupling!) vs **standalone** (per service); ideal: strict + standalone; contract versioning policies & deprecation; **consumer-driven contract testing** (Pact) as governance fitness function.
- Refs: Hard Parts ch.13.
- Do: ADR-0015: contract strategy per interface in Kitchen Flow; set up one consumer-driven contract test that gates a mock CI pipeline.

### P5.3.8 — Managing analytical data: the operational/analytical divide
- Concepts: why analytics on operational stores fails (performance, coupling, schema mismatch); the family: ETL/ELT, data warehouse, data lake/lakehouse, streaming ingestion (kappa-ish); access patterns, aggregation, reporting topologies.
- Refs: Hard Parts ch.14 §operational-to-analytical.
- Do: Design the analytics path for ticket data: pick ETL vs streaming; diagram latency/fidelity trade-offs.

### P5.3.9 — Data mesh (Zhamak's four principles)
- Concepts: **data mesh** as sociotechnical approach: domain ownership, data as a product, self-serve data platform, computational federated governance; data product addressability & contracts; data mesh vs architecture quantum coupling; when NOT to use mesh (small orgs, homogeneous data).
- Refs: Hard Parts ch.14 §"The Data Mesh" (+ book's trade-off table 14-x).
- Do: Trade-off table for data mesh at two org scales (50 engineers vs 5000); ADR-0016 with an explicit "not yet" trigger list.

### P5.3.10 — Build your own trade-off analysis (the meta-skill)
- Concepts: the book's decision-analysis method generalized: identify the architecture decision → gather characteristics → enumerate options → quantify advantages/disadvantages per option → weight by business drivers → decide & ADR → govern with fitness functions; how the authors structured every chapter this way.
- Refs: Hard Parts ch.15 "Build Your Own Trade-Off Analysis".
- Do: Write the template as a checklist file; apply it once, end-to-end, on a decision the books never covered (e.g., "self-host open-source LLM vs API for Kitchen Flow's AI features") — this is your bridge to Phase 7.

---

## Checkpoint 5 (graded)
`artifacts/checkpoint-05/` — **The Migration Dossier:** full decomposition plan for Sysops Squad (or a real system you know, with my approval):
1. Quantum analysis before/after; 2. component decomposition (all six patterns, with metrics evidence); 3. data decomposition + DB choices + ownership map; 4. granularity ADRs; 5. saga + outbox + concurrency model with diagrams; 6. contract strategy + one working contract test; 7. ADR set (≥6, MADR format).
Pass bar: I pick two random decisions from your dossier and attack them; your trade-off tables must hold.

## Resources
- Book ADR appendix (all saga ADRs listed) — compare yours against the authors'
- Pact.io for consumer-driven contracts; ArchUnit examples from ch.5
- "Data Mesh" (Dehghani) book — skim principles only
