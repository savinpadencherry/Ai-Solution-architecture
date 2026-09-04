# ADR-0001: Adopt Architecture Decision Records for this project

Date: 2026-09-03 | Status: accepted

## Context
Significant architecture decisions were living in chat messages, meetings, and memory.
When someone asks "why did we do this?" in six months, there is no reliable answer —
decisions get silently re-litigated (the "Groundhog Day" antipattern).

## Decision
Every significant architecture decision gets a numbered ADR in this folder, written
with the template. ADRs are **immutable**: we never edit history — a new ADR that
*supersedes* the old one is how a decision changes.

## Consequences
+ A searchable, permanent record of every "why"
+ New team members can read the decision history instead of archaeology
+ Fewer repeated debates
− A small writing tax on every significant decision (worth it)
