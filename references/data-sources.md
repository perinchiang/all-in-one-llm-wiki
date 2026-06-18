# Data Sources

Use only the sources the user actually provides or authorizes. Store commands, dates, and assumptions in `log.md`.

## Obsidian Notes

Method:

1. Locate the user's vault or exported notes.
2. Import notes by folder into `raw/notes/`.
3. Convert stable study/project topics into `concepts/`.
4. Convert durable people/tools/projects into `entities/`.

Agent value:

- The agent can answer using the user's existing terminology, learning stage, and project history.

## AI Platform Memory Exports

Supported pattern: [ChatGPT](https://chatgpt.com/), [Claude](https://claude.ai/), [Gemini](https://gemini.google.com/), [Perplexity](https://www.perplexity.ai/), [豆包](https://www.doubao.com/), or any platform that can expose "memory" or long-term profile text.

Manual prompt to give each AI platform:

```text
Please export everything you remember about me or have stored as long-term memory.
Group it by topic. Include uncertainties and avoid inventing details.
Return Markdown or JSON that can be imported into a private personal wiki.
```

Ingestion:

1. Save each export under `raw/ai-memory/<platform>-memory-export-YYYY-MM-DD.md`.
2. Extract durable facts into existing entity/concept pages.
3. Mark platform-specific claims and conflicts.
4. Deduplicate repeated facts across platforms.

Agent value:

- Merge scattered self-knowledge.
- Preserve differences between platforms.
- Reduce repeated user onboarding.

## Bilibili Via [bilibili-cli](https://github.com/JimmyLJX/bilibili-cli)

Method:

1. Install and authenticate bilibili-cli:

   ```bash
   pip install bilibili-cli
   ```
2. Export:
   - recent watch history
   - favorite folders and items
   - following list
3. Save raw JSON/CSV under `raw/platform-exports/bilibili/`.
4. Summarize categories, top creators, recent themes, and learning vs entertainment split.

Example command pattern, adapt to the chosen CLI:

```bash
bili login
bili history --output raw/platform-exports/bilibili/history-YYYY-MM-DD.json
bili favorites --output raw/platform-exports/bilibili/favorites-YYYY-MM-DD.json
bili following --output raw/platform-exports/bilibili/following-YYYY-MM-DD.json
```

Agent value:

- Understand current video interests.
- Detect active learning topics.
- Connect creators and playlists to goals.

Privacy:

- Do not publish raw watch history without review.

## [Garmin](https://connect.garmin.com/) Via Script

Method:

1. Use [Garmin Connect](https://connect.garmin.com/app) credentials or an approved local session.
   - 国际版：https://connect.garmin.com/app
   - 中国版：https://connect.garmin.cn/app/
2. Fetch recent daily summaries, sleep, steps, activities, and personal records.
3. Save raw JSON privately under `raw/health/garmin/`.
4. Summarize trends and anomalies in `entities/health-garmin.md`.

Use `scripts/garmin_to_wiki_example.py` as a starter, then adapt fields and auth handling.

Agent value:

- Suggest rest, training, routines, or recovery based on real recent activity.

Privacy:

- Avoid publishing exact GPS routes, location traces, raw heart-rate streams, or account emails.

## Apple Health Export

Export on iPhone:

1. Open Health app.
2. Tap the avatar/profile icon.
3. Choose "Export All Health Data".
4. Save/share the generated ZIP.
5. Extract `export.xml` locally.

Ingestion:

1. Parse `export.xml` locally.
2. Create aggregate summaries: date range, record counts, activity types, sleep coverage, body metrics trends.
3. Store summary JSON under `raw/health/apple-health-summary-YYYY-MM-DD.json`.
4. Store the full XML only in private storage if needed.

Agent value:

- Understand long-term health baselines and changes.

Privacy:

- Do not put full `export.xml` into a public repository.

## [Spotify](https://www.spotify.com/)

Method options:

- Spotify Web API for saved tracks, playlists, recently played tracks, and top artists/tracks when authorized.
- Manual export or playlist CSV when API access is unavailable.

Summarize:

- saved track count
- playlist count
- genre/mood clusters
- recurring artists
- scene-based listening: work, study, exercise, commute, rest

Agent value:

- Choose music by task, mood, or context.
- Explain recommendations through taste clusters rather than generic popularity.

## [豆瓣](https://www.douban.com/)

Method options:

- User-provided export, scraped own profile data, or manually saved movie/book/game pages where permitted.

Summarize:

- watched movies/TV count
- read books count
- ratings distribution
- short-review themes
- disliked patterns
- favorite genres, creators, eras, regions, or narrative traits

Agent value:

- Recommend films, shows, books, and games based on actual ratings and comments.

## [Google Takeout](https://takeout.google.com/) / Chrome / YouTube

Chrome:

1. Use [Google Takeout](https://takeout.google.com/) for Chrome bookmarks/history/settings when available.
2. For history, prefer aggregate summary over raw URL storage.
3. Summarize top domains, categories, date range, AI tools, dev tools, study tools, local services.

YouTube:

1. Use Google Takeout for subscriptions, playlists, comments, watch history when available.
2. Summarize channel categories and creator clusters.

Agent value:

- Understand tools, projects, attention distribution, and content preferences.

Privacy:

- Do not publish raw browser history or exact watch history without user review.

## Steam

Method:

1. Use Steam Web API or user export for owned games and playtime.
2. Summarize top games, genres, played/unplayed split, and social/co-op patterns.

Agent value:

- Recommend games, leisure plans, media, or music with game context.

## Calendar, Coffee, Lifestyle Logs

Method:

- Import CSV/ICS/Markdown/manual logs into `raw/`.
- Summarize sparingly: frequency, patterns, preferences, constraints.

Agent value:

- Help plan routines, breaks, work sessions, purchases, or recommendations with real context.

Privacy:

- Calendar and lifestyle logs often contain location or relationship details; publish only aggregates.

## Service Accounts and Toolchain

Method:

- Scan user-provided account lists, email summaries ([Hermes Email 集成](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/email)), password manager exports, or manual inventory only with explicit permission.

Summarize:

- tool categories
- available platforms
- active subscriptions
- self-hosted services
- cloud providers

Agent value:

- Recommend solutions that match the user's actual stack.

Privacy:

- Never store passwords, API keys, recovery codes, or full credentials in the wiki.
