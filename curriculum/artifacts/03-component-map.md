# Artifact 03 — My Project as Components + Connascence Edges

**Pointer:** P1.3.5 · From Modules to Components (Fundamentals ch. 3 §"From Modules to Components")
**System mapped:** Balance (Flutter + Firebase + Supabase + Gemini)
**Built from:** Balance `docs/ARCHITECTURE.md` + `docs/BACKEND_SETUP.md`, prior live tours of Supabase facade vs Firebase dep graph.

## The definition we're using

**Component = a deployable artifact with an entry point.**
- Modules are organized *code*; components are *shipped* units. The dividing line: **what deploys**.
- Feature folders (`lib/features/board`, BLoCs, repositories) are modules inside the Balance app component — not components themselves.
- Contracts (HTTP routes, APIs, JWT claims) — not shared code — are what let components be written in different languages.

## Balance component map

| Component | What it is (artifact + entry point) | Language/runtime | Talks to |
|---|---|---|---|
| Balance app | Flutter APK/IPA · `main.dart` | Dart / Flutter on device | SharedPreferences, Firebase Auth/FCM, Supabase gateway, Gemini or proxy, OS calendar/notifs |
| SharedPreferences | On-device KV | Device OS | Balance app |
| Firebase Auth | Firebase Auth service | Google cloud | Balance app (Google sign-in) |
| Firebase Messaging (FCM) | Push delivery | Google cloud | Balance app |
| Supabase API gateway | Project URL front door | Supabase cloud | App → PostgREST / Realtime / Edge Functions |
| PostgREST | REST over Postgres tables | Supabase | Postgres, App |
| Supabase Realtime | Websocket publication (`tickets`) | Elixir on Supabase | Postgres, App |
| Supabase Postgres | Managed database | Postgres | PostgREST, Realtime, Functions |
| Edge: discover-events | `supabase/functions/discover-events` | Deno edge | App, external event sources |
| Edge: push-notify | `supabase/functions/push-notify` | Deno edge | App / push path |
| Edge: Gemini proxy (opt-in) | `GEMINI_PROXY_URL` | Deno edge | Gemini API |
| Gemini API | `generativelanguage.googleapis.com` | Google | Proxy or direct from app |

Dev-only (correctly OFF the deployable map): Flutter analyzer, tests, `flutter_launcher_icons`, local `.env` tooling.

## Edges + connascence audit

| Edge (A → B) | Contract type | Connascence on this edge | Weakest acceptable? |
|---|---|---|---|
| App → SharedPreferences | Local JSON keys | name, type | Strong OK (distance = 0) |
| App → Firebase Auth | OAuth / Firebase UID | meaning ("who is the user") | Prefer explicit identity DTO; don't leak Google account shape into domain |
| App → PostgREST | REST + table/column schema | name, type (and meaning of status enums) | Versioned schema / explicit mappers; never silent column renames |
| App → Realtime | Published table + payload shape | name + dynamic timing | Tiny contract; treat missed events as first-class |
| Firebase UID → Supabase `user_id` / RLS | Cross-vendor identity | **meaning across network** | One identity story (e.g. Firebase JWT verified in Supabase); highest-risk edge |
| App → Gemini (or proxy → Gemini) | Prompt + JSON response schema | meaning, algorithm (parsers) | Weaken via proxy (key stays in edge); freeze response schema; eval harness later |
| App → FCM / local notifications | Channel + action ids | name + dynamic execution order | Keep action vocabulary tiny and versioned |
| Edge proxy → Gemini API | HTTP generateContent | name, type | Isolated inside edge component |

## Answers to the warm-up questions

1. **Redeploy alone:** Gemini proxy, discover-events, push-notify, and (with care) Postgres migrations *if* clients tolerate the schema. **Can't alone:** Balance app if PostgREST column names change; Supabase rows if Firebase identity encoding changes.
2. **Breaks first on silent schema change:** App → PostgREST (`tickets` / `profiles` shapes).
3. **Hub risk:** Balance app is the orchestration hub today (everything leans on it). Supabase Postgres is the data hub. Neither is a Firebase-style 85-module client hairball, but identity straddling Firebase+Supabase is the hidden hub.
4. **Dev-only correctly excluded:** tests, lints, icon generators, MCP/IDE tooling.

## Keeper insight
A component map isn't a box diagram — it's a **risk map of edges**. Dangerous = strong connascence + long distance (Firebase identity ↔ Supabase rows, PostgREST schema ↔ Flutter models, Gemini JSON meaning ↔ parsers).
