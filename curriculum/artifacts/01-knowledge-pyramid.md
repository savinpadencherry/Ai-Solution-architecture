# Artifact 01 — My Knowledge Pyramid → Personal Tech Radar

**Pointer:** P1.2.2 · Technical breadth vs depth (Fundamentals ch. 2 §"Technical Breadth")
**Built from:** live browser tour — CNCF Landscape, roadmap.sh/software-architect, ThoughtWorks Radar Vol. 34 + Build-Your-Own-Radar
**Canonical data:** [01-tech-radar.csv](./01-tech-radar.csv) (name, ring, quadrant, isNew, description) — re-render anytime at https://radar.thoughtworks.com by hosting this CSV and pasting the URL. First render: 2026-09-04, 26 blips.

## Layer 1 — KNOW (Adopt ring, 13)

> **Shape:** the entire 2024–26 AI tooling wave. Real depth, market-hot — but note it is depth in *tools around* AI, not yet in *infrastructure under* AI.

Cursor · Claude Code · Codex · ZCode · Antigravity · VSCode · GitHub · Figma Make (Tools)
Figma MCP · Firebase · Supabase (Platforms)
Python · Flutter (Languages & Frameworks)

## Layer 2 — KNOW I DON'T KNOW (Trial/Assess rings, 10 + practice)

Postgres (Trial — *the teaching blip: Supabase sits in Adopt while its engine sits next door; using an abstraction ≠ knowing the core*) · Technology Radar as a practice (Trial — adopted via this curriculum)
Kafka · AWS · Azure · Google Cloud · IBM Cloud · Apache Hadoop · Snowflake · MongoDB (Assess)
**Honest constraint logged:** cloud hands-on blocked by budget → free/local path chosen (see below).

## Layer 3 — DIDN'T KNOW IT EXISTED (harvested today, 3)

| # | Technology | Found where | What it does |
|---|---|---|---|
| 1 | AG-UI Protocol | TW Radar Vol. 34 (blip 42, Trial) | Open protocol standardizing streaming between agent backends and UIs |
| 2 | LiteLLM | Radar tooltip (Tools, Assess) | AI gateway unifying 100+ LLM provider APIs behind one interface |
| 3 | Backstage | CNCF Landscape wall (Application Definition) | Spotify's open-source internal developer portal |

*Harvest is now a standing habit: every lesson adds candidate blips from whatever we tour.*

## The two dysfunctions, checked against myself

1. **Depth everywhere?** No — Adopt ring capped at 13, all genuinely current. ✅
2. **Stale expertise?** The risk is different for me: my whole Adopt ring is <2 years old, so the danger is **fragile monoculture** — one wave, one generation of tools. The infra/data arc (Kafka → Snowflake → clouds) is the breadth side of the house and it's empty of hands-on. That's the gap this curriculum's Phase 5–9 will fill.

## Money-free path for the Assess ring (so cost stops being the excuse)

| Target | Free route | Gets me |
|---|---|---|
| Kafka | Redpanda or Strimzi in Docker, locally | Streaming + event-driven Phase 3–5 hands-on |
| Postgres | Already in my life via Supabase — open the SQL editor | The Trial→Adopt promotion, zero cost |
| AWS | Free tier + LocalStack (local AWS emulator) | VPC/IAM/S3/Lambda concepts without a bill |
| Kubernetes-era clouds | k3d/kind locally | The orchestration layer all three clouds share |
| Snowflake | 30-day trial + DuckDB locally | Warehouse concepts (the concepts transfer, the bill doesn't) |

**Breadth costs reading time, not money.** The Assess ring grows by reading radars, docs, and well-architected frameworks — all free. Hands-on depth is only owed to the ring I get paid in.

## My rendered radar
- Rendered live in session: `radar.thoughtworks.com/?documentId=http://localhost:8123/01-tech-radar.csv` (local server on :8123 serving this folder)
- Screenshot: saved in session artifacts; re-render anytime from the CSV above.
- Re-render planned at P10.5 — the delta between the two radars is the curriculum's receipt.

## Keeper insight
The pyramid isn't a trivia test, it's an honesty audit of where my opinions are allowed to be strong. My worst future decisions would come from (a) not naming options like AG-UI, or (b) trusting "Supabase fluency" as "Postgres mastery". Rings make both visible — and visible is fixable.
