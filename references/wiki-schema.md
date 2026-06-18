# Wiki Schema

## Page Types

- `entity`: people, tools, platforms, media items, devices, services, accounts, projects.
- `concept`: reusable ideas, workflows, study concepts, methods, reflections.
- `comparison`: side-by-side evaluation.
- `query`: saved agent query or frequently asked question.
- `raw`: original or processed source material.

## Frontmatter

```yaml
---
title: "Human-readable title"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity
tags: [profile, music, spotify]
sources: [raw/platform-exports/source-file.json]
confidence: high
---
```

## Entity Page Template

```markdown
# Title

> One-sentence agent-facing summary.

## Overview

| Dimension | Value |
| --- | --- |
| Source | export/API/manual |
| Date range | YYYY-MM-DD to YYYY-MM-DD |
| Confidence | high/medium/low |

## Findings

- Fact with source.
- Inference clearly marked as inference.

## Agent affordances

- What an agent can now do.
- What the agent should avoid.

## Open questions

- Items needing user confirmation.

## Cross-links

- [[related-page]]
```

## Index

`index.md` should begin with a short instruction for agents:

```markdown
# Wiki Index

> Query this page first. It lists high-value pages and one-line summaries.
```

Keep high-value personal profile pages near the top. Long imported catalogs can appear later by category.

## Log

Append-only `log.md` entries:

```markdown
## [YYYY-MM-DD] ingest | Source name
- Source: exact export/API/manual source
- Created:
  - entities/example.md — one-line result
- Updated:
  - index.md — summary
- Privacy: raw data private; public output uses aggregates only
- Notes: parser assumptions, skipped files, anomalies
```

## Confidence

- `high`: direct export/API data or user-confirmed fact.
- `medium`: strong inference from multiple sources.
- `low`: single-source inference, ambiguous text, or model-generated guess.
