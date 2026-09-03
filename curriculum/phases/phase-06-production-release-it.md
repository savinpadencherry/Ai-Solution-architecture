# Phase 6 — Production Engineering: Release It!

**Book:** Release It! 2nd Ed. — ch. 1–17 (Parts I–IV: Create Stability, Design for Production, Deliver Your System, Solve Systemic Problems)

**Goal:** Architect systems that survive production: failure-mode literacy (antipatterns), the stability pattern toolbox, production infrastructure (networking, control plane, security), deployment & versioning discipline, and chaos engineering.

**Why this matters for an AI solution architect:** LLM systems are distributed systems with an extra failure mode — a non-deterministic, rate-limited, expensive dependency (the model API). Everything here applies, and Phase 7+ assumes it.

**You are ready for Phase 7 when:** given any failure story, you can name the antipattern, and given any design, you can place the right stability patterns — including on an LLM pipeline.

---

## Part I — Create Stability

### P6.1 — Living in production; aiming for the right target
- Concepts: feature-complete ≠ production-ready; systems designed for QA die in production; design for production (analog of design for manufacturability); cost asymmetry: development cost (one-time) vs operational cost (recurring); "use the force": experience-based judgment of failure.
- Refs: Release It! ch.1.
- Do: List 5 systems you've shipped; classify each: built-for-QA or built-for-production, with evidence.

### P6.2 — Case study: The Exception That Grounded an Airline
- Concepts: the full anatomy of a cascading outage (change window, exception storm, postmortem, the smoking gun); how a single integration point's exception killed a fleet's dispatch system; lesson extraction method: trace failure → root mechanism → pattern name.
- Refs: Release It! ch.2.
- Do: Write the one-page postmortem the airline should have written, naming every antipattern involved.

### P6.3 — Defining stability, failure modes & crack propagation
- Concepts: stability = systemic property (a shock doesn't cascade); transaction vs system life span; **failure modes**: crash, hang, slowness, data corruption, silent failure; **stopping crack propagation** — isolating failure so the system degrades gracefully; chain of failure: every integration point is a chance for failure to hop systems.
- Refs: Release It! ch.3.
- Do: Draw a "crack propagation" diagram for a 3-service system where service B hangs; mark where the crack stops with what.

### P6.4 — Stability antipatterns, part 1: the interaction killers
- Concepts: **Integration Points** (every socket = probability of failure; timeouts missing), **Chain Reactions** (synchronized failures from shared state; stop condition), **Cascading Failures** (cracks hopping systems), **Blocked Threads** (the classic connection-pool exhaustion; remote → blocked resource chain), **Self-Denial Attacks** (self-inflicted: retry storms, outbound email storms, budget/quote storms).
- Refs: Release It! ch.4 (first half).
- Do: Antipattern cards part 1; find a self-denial attack in your own history (or the LLM-API retry storm equivalent).

### P6.5 — Stability antipatterns, part 2: load & scale killers
- Concepts: **Users** (close & remote: traffic floods, bots), **Scaling Effects** (server count, client count, input size, orthogonality — how O(n²) hides behind scale), **Unbalanced Capacities** (upstream/downstream mismatch), **Dogpile** (synchronized restarts, thundering herd, cache expiry storms), **Force Multiplier** (management consoles, batch jobs amplifying damage), **Slow Responses** (the sneaky failure that causes blocked threads downstream), **Unbounded Result Sets** (queries without limits eating memory).
- Refs: Release It! ch.4 (second half).
- Do: Antipattern cards part 2; quiz game: I describe a war story, you name the antipattern in <30 seconds.

### P6.6 — Stability patterns, part 1: containment
- Concepts: **Timeouts** (with retries policy), **Circuit Breaker** (closed/open/half-open; trip conditions; the single most valuable pattern), **Bulkheads** (physical separation of resource pools), **Steady State** (no unbounded growth in prod: logs, data, sessions — self-cleaning), **Fail Fast** (check resources before accepting work).
- Refs: Release It! ch.5 (first half).
- Do: Implement a circuit breaker library from scratch (~100 lines) with trip/half-open logic; write unit tests that prove it.

### P6.7 — Stability patterns, part 2: degradation & load management
- Concepts: **Let It Crash** (Erlang-style supervision, restart to known-good), **Handshaking** (servers throttle/slow-accept, refusing gracefully), **Test Harnesses** (simulate faults from upstream), **Decoupling Middleware** (async queues absorb sync failure), **Shed Load** (drop work gracefully under pressure — with a priority story), **Back Pressure** (propagate overload upstream), **Governor** (slow down runaway processes instead of killing).
- Refs: Release It! ch.5 (second half).
- Do: Complete your pattern cards; then design the resilience plan for the Kitchen Flow LLM pipeline: where does the circuit breaker live? (bridging note to Phase 7 — model APIs rate-limit and hang like any integration point).

## Part II — Design for Production

### P6.8 — Case study: Phenomenal Cosmic Powers, Itty-Bitty Living Space + production foundations
- Concepts: the mobile-commerce memory outage story (vital signs, diagnostics, treatment); **Foundations**: virtualization (the big lie: virtualization's extra failure modes), physical hosts/VMs/containers (IP-per-VM, hostnames, VM/OS startup failure, VM sprawl, orphaned disks, CATTLE over pets), instances vs containers.
- Refs: Release It! ch.6, ch.7.
- Do: Container failure-mode table: for a Kubernetes pod — name 6 distinct ways it dies and the detection signal for each.

### P6.9 — Processes on machines: code, configuration, transparency
- Concepts: running software = code + config (version control for config? environment leakage, config servers, secrets); **transparency**: the design for operations — logging discipline (log4j-style levels, "logging considered harmful when unbounded"), health checks (shallow vs deep), telemetry; queue/thread monitoring.
- Refs: Release It! ch.8.
- Do: Audit one of your services: config secrets hygiene + logging quality; rewrite its health check to be deep but cheap.

### P6.10 — Interconnect: DNS, load balancing, demand control, discovery
- Concepts: solutions at different scales; DNS (TTL as cache-poisoning knob; round-robin DNS limits); **load balancing** algorithms (round robin, least used, response-time weighted, session/stateful issues); **demand control** (admission control before overload — ties to shed load); network routing; **service discovery** (self-registration vs third-party registry); migratory virtual IPs.
- Refs: Release It! ch.9.
- Do: Load-balancer decision matrix for 3 traffic shapes (steady, spiky, stateful); explain what breaks session affinity under autoscaling.

### P6.11 — Control plane & platform thinking
- Concepts: **mechanical advantage** (control many from one); platform & ecosystem; development-is-production mindset; **system-wide transparency** (the control plane needs telemetry as first-class); configuration services; provisioning & deployment services; command & control (feature flags, kill switches); the platform players (Kubernetes etc.) & "the shopping list".
- Refs: Release It! ch.10.
- Do: Design the control-plane shopping list for a 40-service fleet: config, provisioning, command & control, with a kill-switch story per critical feature.

### P6.12 — Security in production
- Concepts: OWASP Top 10 as the architect's security floor (injection, broken auth, sensitive data exposure, XXE, broken access control, misconfig, XSS, insecure deserialization, vulnerable components, insufficient logging); principle of least privilege; configured passwords & secrets management; security as ongoing process (not a phase).
- Refs: Release It! ch.11.
- Do: Threat-model Kitchen Flow (STRIDE-lite) + map each OWASP item to your control; write the secrets-rotation ADR.

## Part III — Deliver Your System

### P6.13 — Design for deployment
- Concepts: so many machines; the fallacy of planned downtime; **automated deployments** (scripted installation, separation of build vs deployment); **continuous deployment** (pipelines, cutover); **phases of deployment**: installation → startup → verification (smoke tests, self-checks) → cutover; deploy like the pros: zero-downtime patterns — rolling, blue-green, canary (with the decision matrix between them).
- Refs: Release It! ch.13 (ch.12 is the short "Waiting for Godot" case study — read it as a horror story).
- Do: Zero-downtime deployment design for a DB-migrating service (the hard version: backward-compatible migration in 2 steps); canary plan with rollback triggers.

### P6.14 — Handling versions
- Concepts: every consumer/provider pair is a version negotiation; helping others handle your versions (additive changes, no breaking changes, contract versioning — links to Hard Parts ch.13); handling others' versions (tolerant reader pattern, version negotiation, "don't chase the API" upgrades); deprecation policy design.
- Refs: Release It! ch.14.
- Do: Version-compatibility matrix for a public API + one "tolerant reader" implementation test.

### P6.15 — Load testing & the QA gap
- Concepts: case study "Trampled by Your Own Customers" (launch-day stampede); QA aims at correctness, load testing aims at capacity; load test design: realistic profiles (ramp, spike, soak), measurement in prod-like env, the testing gap (what load tests never catch); capacity math (Little's Law intuition).
- Refs: Release It! ch.15.
- Do: Write a load-test plan for Kitchen Flow including an LLM-API-rate-limit scenario (what happens to the queue at 10x?), with pass/fail SLOs from Phase 2.

## Part IV — Solve Systemic Problems

### P6.16 — Adaptation: systems that evolve
- Concepts: **convex returns** on investment in adaptation (flat early, rocket later); process & organization adaptation (how teams must change as systems grow); system architecture adaptation (abstraction layers, hot swapping implementations, plugin designs — microkernel returns); information architecture (the data model as the slowest-moving architecture artifact; versioned, additive data evolution).
- Refs: Release It! ch.16.
- Do: Adaptation audit of Kitchen Flow: 3 convex-return investments ranked by payoff horizon.

### P6.17 — Chaos engineering
- Concepts: breaking things to make them better; antecedents (the Simian Army: Chaos Monkey, Latency Monkey, Chaos Gorilla…); the discipline: steady-state hypothesis → inject reality (kill instances, inject latency) → observe → automate; adopting your own monkey safely (blast radius, canaries first); disaster simulations/game days.
- Refs: Release It! ch.17.
- Do: Design a game day for Kitchen Flow: 5 experiments (one per layer: pod, network, model API, database, region), each with hypothesis, blast radius, abort criteria.

---

## Checkpoint 6 (graded)
`artifacts/checkpoint-06/` — **Production Readiness Review (PRR)** for the Kitchen Flow LLM pipeline:
1. Fault-tree diagram with antipattern names at every node;
2. Stability pattern placement map (breaker, bulkhead, shed load, back pressure, governor) with trip/roll thresholds;
3. Deployment & versioning plan (zero-downtime + contract compatibility);
4. Game day runbook.
Pass bar: I play chaos gremlin and name one failure your plan misses; if your pattern placement adapts live, you pass.

## Resources
- Principles of Chaos Engineering: principlesofchaos.org; Chaos Toolkit; Litmus/Gremlin docs
- Google SRE book (free online) — pairs with P6.8–6.11
- OWASP Top 10: owasp.org/Top10
