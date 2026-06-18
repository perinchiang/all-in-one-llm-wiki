---
name: all-in-one-llm-wiki
description: Build an all-in-one AI-readable LLM Wiki from personal exports and app data. Use when a user wants to ingest digital-life data into a private wiki for AI agents, including Obsidian notes, AI memory exports, Bilibili data via CLI, Garmin data via script, Apple Health export, Spotify, Douban, browser history, YouTube/Google Takeout, Steam, calendars, coffee or lifestyle logs, service accounts, NAS/media libraries, and then create a privacy-safe narrative or PPT prompt about the system.
---

# All in One LLM Wiki

## Purpose

Create a private, AI-readable wiki that helps agents understand a user's long-term context. Optimize for agent retrieval, provenance, privacy, and downstream tasks, not for human-perfect publishing.

Do not copy another user's personal profile into outputs. Treat all examples as schema examples, not facts about the current user.

## Core Workflow

1. Inventory available sources and classify them as notes, AI memory, media taste, browsing/tooling, health, lifestyle, or accounts.
2. Read `references/privacy.md` before handling raw exports, browser history, health data, family data, account data, or any publishable artifact.
3. Use `references/data-sources.md` for source-specific ingestion methods.
4. Use `references/wiki-schema.md` to create wiki pages, index entries, raw source storage, and logs.
5. Summarize each source into agent-facing pages: facts, preferences, recurring behaviors, constraints, evidence, and open questions.
6. For a new wiki, use `scripts/init_wiki.py` to create the skeleton; use `--demo` only for synthetic public-safe examples.
7. Create a privacy-safe story or presentation only after the wiki layer exists. Use `references/presentation.md` and `assets/ppt-prompt-template.md`.
8. Before publishing any demo, deck, screenshot, or prompt, use `PUBLISHING_CHECKLIST.md`.

## Output Shape

Prefer this folder layout:

```text
.wiki/
  SCHEMA.md
  index.md
  log.md
  raw/
    articles/
    ai-memory/
    health/
    platform-exports/
  entities/
  concepts/
  queries/
  _archive/
```

Every useful page should include:

- frontmatter: `title`, `created`, `updated`, `type`, `tags`, `sources`, `confidence`
- an overview table
- concrete agent affordances: "What an agent can now do with this"
- cross-links to related entities
- a privacy note when the page is sensitive

## Ingestion Rules

- Keep raw exports private by default.
- Store exact raw data only when the user explicitly wants it and the destination is private.
- For browser, health, family, account, and location data, prefer aggregate summaries plus checksums.
- Record source date, extraction method, command, and parser assumptions in `log.md`.
- Distinguish facts from inferred preferences. Use `confidence: low|medium|high`.
- Add a "needs confirmation" section for inferred or ambiguous items.

## Agent Affordance Pattern

For each imported source, write what it enables:

```markdown
## Agent affordances

- Recommend actions based on real user history, not generic popularity.
- Avoid suggestions that conflict with known constraints.
- Explain why a recommendation fits, citing the source page.
- Ask for confirmation before using sensitive or low-confidence inferences.
```

Examples:

- Music data lets an agent choose playlists by task, mood, or context.
- Douban or movie/book data lets an agent recommend media by actual taste and prior ratings.
- Bilibili/YouTube data lets an agent understand current learning and entertainment streams.
- Browser aggregates let an agent understand tooling, projects, and attention distribution.
- Health data lets an agent suggest rest, training, or routine changes with realistic context.
- AI memory exports let an agent merge scattered self-knowledge across platforms.

## Resources

- `references/data-sources.md`: source-specific import methods.
- `references/wiki-schema.md`: page schema, index, log, linking, and confidence conventions.
- `references/privacy.md`: redaction and publishability rules.
- `references/presentation.md`: converting the wiki process into a video/PPT narrative.
- `assets/ppt-prompt-template.md`: prompt template for Kimi, Claude, Gamma, or other PPT tools.
- `PUBLISHING_CHECKLIST.md`: final public-release redaction checklist.
- `examples/demo-wiki/`: synthetic demo wiki for first-run testing.
- `scripts/init_wiki.py`: create a private `.wiki/` skeleton or copy the synthetic demo.
- `scripts/garmin_to_wiki_example.py`: generic Garmin Connect to wiki JSON/Markdown starter script.
