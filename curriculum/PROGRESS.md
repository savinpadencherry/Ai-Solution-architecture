# Progress Tracker

We tick one checkbox per completed pointer. Keep a one-line "keeper insight" under each as we go.

**Legend:** ☐ not started · ✅ done · 🔁 revisit

## Phase 0 — Setup, Baseline & Toolkit (4)
- [x] P0.1 Orientation & the four-book map — insight: The architect owns questions with no Googleable answers; the method (trade-offs → business drivers → decide → record → govern) IS the skill.
- [x] P0.2 Baseline self-assessment — insight: Architects grow the MIDDLE of the knowledge pyramid (breadth), not just the top (depth); baseline file ready in artifacts, fill-in ongoing.
- [x] P0.3 Trade-off analysis, the core discipline — insight: List BOTH columns (advantages AND brutal disadvantages) for every option before choosing; the winner's downsides must land where the business can afford them. Messaging bridge taught: queue = work distribution (one message, one worker, exactly once), topic = event fan-out (one event, all subscribers).
- [x] P0.4 ADRs + fitness functions toolkit — insight: ADR = memory for humans (immutable, superseded never edited); fitness function = memory for robots (automated check that a decision still holds). Together: governance without nagging.

## Phase 1 — Architectural Thinking & Modularity (13)
- [x] P1.1.1 Definitions: structure-behavior-connection — insight: Architecture answers 3 questions — how it's structured (blocks), how it behaves (runtime interaction), how parts connect (contracts). "Hard to change" tells you which decisions are architectural. Quiz 1: 6/6.
- [x] P1.1.2 Laws of software architecture — insight: Law 1: everything is a trade-off (the architect's question is "what does this make WORSE?"). Law 2: why beats how — tools churn, reasoning survives; ADRs record why.
- [x] P1.1.3 The 8 core expectations of an architect — insight: Head-chef frame: design, analyze continuously, manage risk, keep current, know the domain & business, enable the team, navigate politics. Personality trap: control-freak vs armchair — the middle (decide key things, delegate, stay hands-on) wins. Quiz: 2/2.
- [x] P1.2.1 Architecture–design spectrum — insight: Three tests place any decision on the spectrum — strategic vs tactical, effort to change, significance of trade-offs. Position determines WHO decides and HOW MUCH process it needs. (Card sort key: 1-D, 2-A, 3-A, 4-D, 5-A, 6-M, 7-D, 8-A.)
- [x] P1.2.2 Breadth vs depth; knowledge pyramid — insight: Breadth is a scanning practice, not memorization — pyramid layers map to radar rings (know→Adopt, know-you-don't-know→Trial/Assess, the blank ring is populated by touring, not introspecting). Two personal failure modes made visible: option-blindness (can't trade-off against what you can't name — AG-UI example) and abstraction-as-expertise (Postgres sat in Trial while its engine Supabase sat in Adopt). Personal radar: 26 blips — deep in the 2024–26 AI-tooling wave, infrastructure parked in Assess with a money-free path (Docker Kafka, LocalStack, free tiers). Radar CSV: artifacts/01-tech-radar.csv; re-render at P10.5 for the delta.
- [x] P1.2.3 Antipatterns: Frozen Caveman, Bottleneck Trap — insight: Frozen Caveman = one old scar becomes a permanent veto ("what if we lose Italy?"); antidote is realistic risk assessment, not forgetting. Bottleneck Trap = architect holding critical-path code; antidote: delegate critical path, stay hands-on via POCs, tech debt, bugs, automation, reviews.
- [x] P1.2.4 Analyzing trade-offs (auction case) — insight: Consolidated in Lesson 05 simulation (queue-vs-topic + business-driver presets); see curriculum/lessons/lesson-05-architects-translator.html.
- [x] P1.2.5 Business drivers → characteristics — insight: Stakeholder sentences translate into named characteristics WITH numbers; 3–5 rule; conflicts (security↔performance, scale↔simplicity) get decided, not dodged. Interactive translator in Lesson 05.
- [x] P1.3.1 Modularity vs granularity — insight: Splitting = modularity (good); sizing = granularity (the danger). Pieces grow linearly, wiring grows quadratically (N(N−1)/2) — the Splitting Machine simulation makes it visceral. Lesson 06.
- [x] P1.3.2 Cohesion: the 7 levels — insight: Functional → sequential → communicational → procedural → temporal → logical → coincidental. "Same file" ≠ "same family"; splitting a cohesive module only creates coupling. Fake Family Detector game in Lesson 06.
- [x] P1.3.3 Coupling metrics: A, I, distance from main sequence — insight: Afferent=who leans on me, efferent=who I lean on; I = Ce/(Ca+Ce) (stability is a ROLE, not a score); A = abstract fraction; D′ = |A+I−1|; Zone of Pain (stable+concrete) vs Zone of Uselessness (abstract+restless). Draggable map in Lesson 07.
- [x] P1.3.4 Connascence taxonomy — insight: Two components "born together" = change one, other must follow. 9 forms: static (name/type/meaning/position/algorithm) + dynamic (execution/timing/values/identity). Rules: weaken connascence as distance grows; refactors downgrade strong→weak. Pain = SILENT + CROSS-SERVICE. Lesson 08.
- [ ] P1.3.5 From modules to components — insight:

## Phase 2 — Architecture Characteristics (12)
- [ ] P2.1.1 What makes an architecture characteristic — insight:
- [ ] P2.1.2 Catalog: operational characteristics — insight:
- [ ] P2.1.3 Catalog: structural & process characteristics — insight:
- [ ] P2.1.4 Conflicts & least-worst balance — insight:
- [ ] P2.2.1 Identifying characteristics from domain & implicit sources — insight:
- [ ] P2.2.2 Prioritization & the 3–5 rule — insight:
- [ ] P2.3.1 Measuring operational characteristics (SLO/SLI) — insight:
- [ ] P2.3.2 Measuring structural characteristics (fitness functions) — insight:
- [ ] P2.3.3 Governance: review boards → automated — insight:
- [ ] P2.3.4 Scope of characteristics → quantum preview — insight:
- [ ] P2.4.1 Component identification: actor/actions, event storming — insight:
- [ ] P2.4.2 Component granularity, coupling, composition — insight:

## Phase 3 — Architecture Styles (13)
- [ ] P3.1.1 Styles vs patterns; monolith vs distributed; 8 fallacies — insight:
- [ ] P3.2.1 Layered — insight:
- [ ] P3.2.2 Modular monolith — insight:
- [ ] P3.2.3 Pipeline — insight:
- [ ] P3.2.4 Microkernel — insight:
- [ ] P3.3.1 Service-based — insight:
- [ ] P3.3.2 Event-driven (broker & mediator) — insight:
- [ ] P3.3.3 Space-based — insight:
- [ ] P3.3.4 Orchestration-driven SOA — insight:
- [ ] P3.4.1 Microservices I: topology & data — insight:
- [ ] P3.4.2 Microservices II: trade-offs & governance — insight:
- [ ] P3.5.1 Style decision framework — insight:
- [ ] P3.5.2 Kata lab #1: style selection under fire — insight:

## Phase 4 — Techniques & Soft Skills (10)
- [ ] P4.1.1 Architectural patterns catalog — insight:
- [ ] P4.1.2 Decision significance & ADR antipatterns — insight:
- [ ] P4.1.3 ADR mastery: structure, storage, LLMs — insight:
- [ ] P4.2.1 Risk analysis & risk storming — insight:
- [ ] P4.2.2 Diagramming: C4 model — insight:
- [ ] P4.3.1 Making teams effective — insight:
- [ ] P4.3.2 Negotiation skills — insight:
- [ ] P4.3.3 Leadership principles — insight:
- [ ] P4.3.4 Architectural intersections — insight:
- [ ] P4.3.5 Laws revisited & career path — insight:

## Phase 5 — Distributed: The Hard Parts (19)
- [ ] P5.1.1 No best practices; saga begins; operational vs analytical data — insight:
- [ ] P5.1.2 Architecture quanta & coupling — insight:
- [ ] P5.1.3 Modularity drivers & costs — insight:
- [ ] P5.2.1 Is the codebase decomposable? — insight:
- [ ] P5.2.2 Decomposition strategies vs tactical forking — insight:
- [ ] P5.2.3 Six component decomposition patterns — insight:
- [ ] P5.2.4 Data disintegrators vs integrators — insight:
- [ ] P5.2.5 5-step data decomposition + DB types — insight:
- [ ] P5.2.6 Service granularity — insight:
- [ ] P5.3.1 Reuse patterns (replication/library/service/sidecar) — insight:
- [ ] P5.3.2 Data ownership: single/common/joint — insight:
- [ ] P5.3.3 Distributed transactions & sagas — insight:
- [ ] P5.3.4 Distributed data: caching, outbox, bullwhip — insight:
- [ ] P5.3.5 Concurrency: orchestration vs choreography — insight:
- [ ] P5.3.6 Transactional seams — insight:
- [ ] P5.3.7 Contracts: strict/loose, shared/standalone, CDC — insight:
- [ ] P5.3.8 Operational vs analytical data management — insight:
- [ ] P5.3.9 Data mesh four principles — insight:
- [ ] P5.3.10 Build your own trade-off analysis — insight:

## Phase 6 — Production Engineering: Release It! (17)
- [ ] P6.1 Living in production — insight:
- [ ] P6.2 Case study: airline grounding — insight:
- [ ] P6.3 Stability, failure modes, crack propagation — insight:
- [ ] P6.4 Antipatterns I: integration points, chains, blocked threads, self-denial — insight:
- [ ] P6.5 Antipatterns II: users, scaling, dogpile, slow responses, unbounded sets — insight:
- [ ] P6.6 Stability patterns I: timeout, breaker, bulkhead, steady state, fail fast — insight:
- [ ] P6.7 Stability patterns II: crash, handshake, middleware, shed load, back pressure, governor — insight:
- [ ] P6.8 Cosmic powers case + production foundations — insight:
- [ ] P6.9 Processes: code, config, transparency — insight:
- [ ] P6.10 Interconnect: DNS, LB, demand control, discovery — insight:
- [ ] P6.11 Control plane & platform — insight:
- [ ] P6.12 Security: OWASP, least privilege — insight:
- [ ] P6.13 Design for deployment & zero-downtime — insight:
- [ ] P6.14 Handling versions — insight:
- [ ] P6.15 Load testing & the QA gap — insight:
- [ ] P6.16 Adaptation & convex returns — insight:
- [ ] P6.17 Chaos engineering — insight:

## Phase 7 — AI Engineering Foundations (10)
- [ ] P7.1.1 ML engineering → AI engineering; the stack — insight:
- [ ] P7.1.2 Use-case analysis & planning — insight:
- [ ] P7.1.3 Foundation model landscape — insight:
- [ ] P7.2.1 Pretraining: data, tokens, transformers, scaling — insight:
- [ ] P7.2.2 Post-training: SFT, RLHF, alignment — insight:
- [ ] P7.2.3 Sampling & the roots of hallucination — insight:
- [ ] P7.3.1 ML eval vs AI eval; leaderboards — insight:
- [ ] P7.3.2 What to evaluate: capabilities & metrics — insight:
- [ ] P7.3.3 LLM-as-judge & comparative evaluation — insight:
- [ ] P7.3.4 Building the evaluation pipeline — insight:

## Phase 8 — Adapting Models (11)
- [ ] P8.1.1 Prompt anatomy & why prompting works — insight:
- [ ] P8.1.2 Technique catalog: few-shot, CoT, decomposition — insight:
- [ ] P8.1.3 Defensive prompting & automated optimization — insight:
- [ ] P8.2.1 RAG: retrieval foundation — insight:
- [ ] P8.2.2 Full RAG pipeline & evaluation — insight:
- [ ] P8.3.1 Agents: planning & tool use — insight:
- [ ] P8.3.2 Agent architectures, guardrails & evaluation — insight:
- [ ] P8.4.1 Finetuning: when & what — insight:
- [ ] P8.4.2 Memory math, PEFT/LoRA, model merging — insight:
- [ ] P8.5.1 Data acquisition, annotation, synthesis — insight:
- [ ] P8.5.2 Data processing, quality, flywheel — insight:

## Phase 9 — AI Systems at Scale (6)
- [ ] P9.1.1 Model-level optimization: compression — insight:
- [ ] P9.1.2 Service-level: batching, caching, autoscaling — insight:
- [ ] P9.1.3 Model routing & the AI gateway — insight:
- [ ] P9.2.1 The reference architecture, assembled — insight:
- [ ] P9.2.2 Feedback loops, monitoring, continuous improvement — insight:
- [ ] P9.2.3 Security, safety & cost governance — insight:

## Phase 10 — Capstones & Mastery (6)
- [ ] P10.1 Capstone A: Monitor Me — insight:
- [ ] P10.2 Capstone B: Enterprise RAG platform — insight:
- [ ] P10.3 Capstone C: Monolith → microservices migration — insight:
- [ ] P10.4 Capstone D: AI agent platform — insight:
- [ ] P10.5 Portfolio assembly & mastery map — insight:
- [ ] P10.6 Continued mastery operating system — insight:

## Checkpoints & exams
- [ ] C0 Toolkit ready
- [ ] C1 Kitchen Flow trade-off + modularity report
- [ ] C2 Insurance Claims: characteristics + fitness functions
- [ ] C3 Nine style one-pagers + kata
- [ ] C4 Mock review board
- [ ] C5 Migration dossier
- [ ] C6 Production readiness review
- [ ] C7 Eval harness + model explainer
- [ ] C8 Adaptation portfolio
- [ ] C9 AI Architecture Document
- [ ] Capstones A–D defended
- [ ] Final mastery exam: PASSED
