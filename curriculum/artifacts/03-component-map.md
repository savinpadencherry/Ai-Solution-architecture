# Artifact 03 — My Project as Components + Connascence Edges

**Pointer:** P1.3.5 · From Modules to Components (Fundamentals ch. 3 §"From Modules to Components")
**Built from:** live tour — npm spec page for @supabase/supabase-js (facade over 5 components), npmgraph (supabase-js: 8 deps, clean facade vs firebase: 85 modules, peer-dependency hairball), Supabase architecture docs (Envoy → GoTrue/PostgREST/Realtime/Storage/pg-meta/Functions/pg_graphql → Postgres).

## The definition we're using

**Component = a deployable artifact with an entry point.**
- Modules are organized *code*; components are *shipped* units. The dividing line: **what deploys**.
- Dev dependencies are modules, not components — they never deploy.
- Identical version numbers across "independent" packages = a release train = they secretly deploy as ONE component (supabase-js ships all 5 sub-components in lockstep).
- Contracts (HTTP routes, APIs) — not shared code — are what let components be written in different languages (GoTrue=Go, PostgREST=Haskell, Realtime=Elixir).

## My system's component map

| Component | What it is (artifact + entry point) | Language/runtime | Talks to |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## Edges + connascence audit

| Edge (A → B) | Contract type | Connascence on this edge | Weakest acceptable? |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

Connascence reminder from P1.3.4: static = name/type/meaning/position/algorithm (lives in code & contracts) · dynamic = execution(order)/timing/values/identity (lives at runtime). Rule: **stronger forms must live closer together** — a cross-network edge carrying strong connascence (e.g., meaning, timing) is where distributed systems bleed.

## Questions this map must answer (Checkpoint 1 warm-up)

1. Which components could I redeploy right now WITHOUT touching any other? (true components) — which can't? (a hidden monolith)
2. Which edge would break first if the other side changed its schema without telling me?
3. Where does my system have a firebase-style hub (one component everything leans on)?
4. Which components are dev-time only (build tools, MCP servers, IDEs) and correctly NOT on the deployable map?

## Keeper insight
(filled when the map is done)
