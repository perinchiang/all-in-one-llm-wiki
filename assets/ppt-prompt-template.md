# LLM Wiki PPT Prompt Template

Use this prompt with Kimi, Claude, Gamma, or another PPT-generation tool.

```text
You are a Bilibili-style tech video PPT planner and visual designer.

Create a 12-14 slide, 16:9 presentation about building an AI-readable LLM Wiki from personal exports.

Audience:
People who use AI agents and want to give them long-term private context.

Core idea:
This is not a beautiful wiki for humans. It is an AI-readable context system. The goal is to let agents understand the user's notes, media taste, tools, health context, learning goals, and prior AI memories without repeatedly asking the user to explain everything.

Tone:
First-person, real, exploratory, slightly self-aware. Do not sound like enterprise marketing.

Visual style:
Warm off-white background, warm orange titles, dark gray body text, subtle teal/blue accents, three-card information layouts, clean diagrams. Avoid dark cyberpunk, dense tables, and raw private screenshots.

Story:
1. I first saw the LLM-Wiki concept and thought it meant making a beautiful wiki for humans.
2. Then I realized the wiki is mainly for AI to read.
3. I imported notes first; the agent understood my learning context better.
4. I imported AI memory exports; the agent merged scattered self-knowledge across platforms.
5. I imported more digital-life data; each source gave the agent a new capability.
6. The result is a private context home for agents, with a public redacted version for sharing.

Available data sources:
- Obsidian or local notes: learning notes, projects, concepts.
- AI memory exports: ChatGPT, Claude, Gemini, Perplexity, Doubao, or similar.
- Bilibili via CLI: history, favorites, following.
- Garmin via script: sleep, steps, activities, personal records.
- Apple Health export: long-term aggregate health data.
- Spotify: saved tracks, playlists, artists, moods, listening scenes.
- Douban: watched movies/TV, read books, ratings, short reviews.
- Google Takeout: Chrome aggregate browsing profile and YouTube subscriptions/playlists/comments.
- Steam: games, playtime, genre preferences.
- Calendar, coffee, lifestyle logs: routines and preferences.
- Service accounts and toolchain: cloud, dev, automation, self-hosted services.

Important:
Each slide must include what the data teaches the agent and what the agent can do now.
Do not expose raw private data. Use aggregate counts, high-level patterns, and synthetic examples.
Do not invent exact numbers if they are not provided.

Suggested slides:
1. Cover: I built an LLM Wiki for my AI agent.
2. The misunderstanding: I thought it was a human-facing wiki.
3. The realization: AI-readable beats human-pretty.
4. Notes import: the agent understands my concepts and learning stage.
5. AI memory import: scattered memory becomes one profile.
6. Data map: notes, AI memories, media, browsing, health, tools, lifestyle.
7. Spotify: the agent can choose music by mood/task.
8. Douban: the agent recommends books and films by real taste, not hot lists.
9. Bilibili/YouTube: the agent sees current interests and learning streams.
10. Chrome/Google Takeout: the agent understands tools and attention distribution.
11. Garmin/Apple Health: the agent gives grounded rest and routine suggestions.
12. Toolchain/accounts/NAS: the agent knows what systems it can design around.
13. Privacy boundary: private complete wiki vs public redacted story.
14. Close: not a data dump, but a context home for agents.

Return:
For each slide, provide title, 2-4 card bullets, visual direction, and 1-2 lines of speaker notes.
Then provide a 3-5 minute narration script.
```
