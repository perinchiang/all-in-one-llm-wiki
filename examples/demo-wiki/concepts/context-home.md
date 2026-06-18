---
title: Context Home
created: 2026-01-01
updated: 2026-01-01
type: concept
tags: [llm-wiki, agent-context, demo]
sources:
  - index.md
confidence: high
---

# Context Home

> The wiki is a private context layer for AI agents, not a polished public knowledge base.

## Overview

| Dimension | Value |
| --- | --- |
| Purpose | reusable long-term context |
| Audience | AI agents working for the user |
| Default visibility | private |

## Findings

- The index should be read first so the agent can choose relevant pages.
- Raw exports should stay private unless the user explicitly approves a destination.
- Public stories should use synthetic examples, aggregates, or redacted screenshots.

## Agent affordances

- Start from `index.md` instead of scanning every raw file.
- Cite source-backed pages when giving recommendations.
- Treat sensitive pages as permission-gated context.

## Open questions

- Which pages should be considered safe summaries?
- Which raw sources require encryption or manual review?

## Cross-links

- [[demo-profile]]
