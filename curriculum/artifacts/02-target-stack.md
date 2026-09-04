# Artifact 02 — The Architect's Target Stack (the "to-learn" radar)

**Companion to:** [01-knowledge-pyramid.md](./01-knowledge-pyramid.md) (where I am) · this file + [02-architect-target-radar.csv](./02-architect-target-radar.csv) = where I'm going.
**Rendered:** same tool — https://radar.thoughtworks.com with the CSV URL. 53 blips · 14 Adopt / 18 Trial / 18 Assess / 3 Caution.
**Golden rule of this radar:** every blip is tagged with the curriculum phase (P0–P10) that earns it. Nothing here is homework for its own sake — each ring entry gets picked up during a phase, most via free/local tooling.

## How to read the rings (obligation levels)

| Ring | Count | What it obligates me to | Cost |
|---|---|---|---|
| **Adopt** | 14 | Real depth. Can design, build, debug, and defend in a review. | Time, not money |
| **Trial** | 18 | Hands-on labs. Weekend-scale projects, one per curriculum phase. | Free (local Docker / free tiers / emulators) |
| **Assess** | 18 | Read + recognize. Docs, well-architected guides, demos. Can name it, place it, and know when it matters. | Free (reading time) |
| **Caution** | 3 | Know WHY not. Able to argue against it with evidence. | Free |

## The three moves that matter most

1. **Postgres: Trial → Adopt.** The cheapest, highest-leverage promotion. Supabase already runs it for me; opening the SQL editor converts "abstraction user" into "engine knower".
2. **Docker: nothing → Adopt.** The gateway skill. Kafka, k3d Kubernetes, LocalStack, Redis, Qdrant, Debezium — the entire Trial ring runs inside it. One skill unlocks eighteen.
3. **The AI architect spine: pgvector → Ragas/promptfoo → MCP SDK → vLLM → LiteLLM → Langfuse.** This is the Phase 7–9 sequence; together they cover RAG storage, evaluation, integration, self-hosting, gateway/cost control, and observability — the six pillars of the AI specialism.

## Deliberate Cautions (know why NOT)

- **Apache Hadoop** — lost to object storage + Spark; the classic "pet concern" trap (Frozen Caveman insurance).
- **IBM Cloud** — smallest ecosystem pull for my path; revisit only if an employer pays for it.
- **LangChain** — learn the concepts first; heavy abstractions hide exactly the architecture decisions I'm training to see.

## Gap vs today (radar 01 → radar 02)

- Today's Adopt is 100% the 2024–26 AI *tooling* wave; the target adds the *infrastructure* and *data* halves (Docker, Linux, Postgres, Redis, Terraform, CI/CD).
- Today's Assess wall (clouds, Kafka, Snowflake, MongoDB) gets a concrete free route per blip — LocalStack, k3d, Redpanda, 30-day trials — and only AWS core is asked to become hands-on (Trial); Azure/GCP/IBM stay read-level.
- Re-render both radars at P10.5; the ring migrations between now and then are the measurable outcome of the curriculum.
