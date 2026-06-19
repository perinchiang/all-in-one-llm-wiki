# Detailed Export Methods

> For the full data ingestion overview and quick install, go back to [README](../README_EN.md).

## 1. Obsidian / Local Notes

Suitable for importing:

- Study notes
- Project notes
- Terminology glossary
- Course notes
- Completed project retrospectives

Steps:

1. Find the local Vault or exported Markdown folder.
2. Place raw files into `raw/notes/`.
3. Generate `concepts/` by topic, and `entities/` by person, tool, project, or platform.
4. Preserve the original file path or source description.

Agent capabilities:

- Explain concepts based on your existing notes.
- Provide practice suggestions tailored to your learning stage.
- Avoid re-explaining from a generic textbook perspective every time.

## 2. AI Platform Memory Export

Suitable platforms:

- [ChatGPT](https://chatgpt.com/)
- [Claude](https://claude.ai/)
- [Gemini](https://gemini.google.com/)
- [Perplexity](https://www.perplexity.ai/)
- [Doubao](https://www.doubao.com/)
- Other AIs with long-term memory / user profiling

Universal prompt:

```text
Please export or organize the long-term memories you currently have about me.
Please group by topic, distinguishing confirmed facts, inferences, preferences, long-term goals, toolchain, projects, health/lifestyle, etc.
Do not fabricate. If uncertain, please mark as "possible" or "needs confirmation."
Please output as Markdown for easy import into a private LLM Wiki.
```

Practical recommendations:

1. Export each platform separately, saving to `raw/ai-memory/<platform>-memory-export-YYYY-MM-DD.md`.
2. Merge repeated facts into the same entity page.
3. Preserve platform-specific information and tag the source.
4. For conflicting information, write "needs confirmation" — do not force-merge.

Agent capabilities:

- Merge fragmented understandings of you from multiple AIs.
- Discover duplicates, conflicts, and gaps.
- Form a more stable long-term context.

Note:

- Many platforms don't have a "one-click export memory" button; the typical approach is to directly ask it "What do you remember about me?" and then manually save the response.
- This type of data may contain sensitive information such as health, family, accounts, and location — by default, it should only go into the private repository.

## 3. Bilibili: via [bilibili-cli](https://github.com/JimmyLJX/bilibili-cli)

Install:

```bash
pip install bilibili-cli
```

After login, export watch history, favorites, and following list:

```bash
bili login
bili history --output raw/platform-exports/bilibili/history-YYYY-MM-DD.json
bili favorites --output raw/platform-exports/bilibili/favorites-YYYY-MM-DD.json
bili following --output raw/platform-exports/bilibili/following-YYYY-MM-DD.json
```

Recommended distillations:

- Recent watch topics
- Favorites categories
- Frequently watched creators
- Learning vs. entertainment ratio
- Current tech / gaming / lifestyle topics of interest

Agent capabilities:

- Know what you're actually watching recently.
- Infer learning paths from your favorites.
- Combine video platform interests to recommend materials, courses, or relaxation content.

Privacy recommendations:

- Do not publicly share complete watch history.
- For public demos, only use category ratios and a few anonymized examples.

## 4. [Garmin](https://connect.garmin.com/): via Python Script

Available library:

```bash
pip install garminconnect
```

Login link — confirm your email and password:

- International: https://connect.garmin.com/app
- China: https://connect.garmin.cn/app/

Recommended approach:

1. Store account credentials in environment variables, not in scripts:

```bash
export GARMIN_EMAIL="your-email@example.com"
export GARMIN_PASSWORD="your-password"
```

2. Use a script to pull:

- daily summary
- sleep
- steps
- recent activities
- personal records

3. Place raw JSON into:

```text
.wiki/raw/health/garmin/
```

4. Start from `scripts/garmin_to_wiki_example.py` and adapt it. The script writes to `.wiki/` by default; set `LLM_WIKI_DIR` to choose another directory.
5. Wiki pages should only contain summaries and trends.

Agent capabilities:

- Suggest recovery or training based on recent sleep and exercise volume.
- Detect abnormal activity records and prompt for confirmation.
- Adjust plans based on long-term habits.

Privacy recommendations:

- Do not publicly share GPS routes, precise locations, account email, or point-by-point heart rate data.
- Public versions should only include trends and aggregate numbers.

## 5. Apple Health: Phone Health App Export

Steps on iPhone:

1. Open the **Health** app.
2. Tap the avatar in the top-right corner.
3. Scroll to the bottom and select **Export All Health Data**.
4. The system will generate a ZIP.
5. After unzipping, you will typically get `export.xml`.

Import recommendations:

1. Parse `export.xml` locally — do not put the full XML in a public repository.
2. Extract aggregate summaries:
   - Time range
   - Total record count
   - Step trends
   - Exercise type statistics
   - Weight/body fat trends
   - Sleep coverage
3. Place the summary JSON at:

```text
.wiki/raw/health/apple-health-summary-YYYY-MM-DD.json
```

Agent capabilities:

- Understand long-term health baselines.
- Combine with current Garmin data to assess changes.
- Give more realistic sleep, exercise, and routine advice.

## 6. [Spotify](https://www.spotify.com/): Spotify Web API

Recommended path:

1. Go to Spotify Developer Dashboard and create an App.
2. Configure Redirect URI.
3. Obtain authorization via OAuth.
4. Pull:
   - saved tracks
   - playlists
   - recently played
   - top artists / top tracks (if scope allows)

Common notes:

- Spotify OAuth callback often requires HTTPS.
- For local development, use tunnels, reverse proxies, or public HTTPS callbacks.
- Do not put client secret in a public repository.

Recommended distillations:

- Number of playlists
- Number of saved songs
- Artist clustering
- Language / style / mood
- Scene playlists: studying, writing, exercise, rest, commuting

Agent capabilities:

- Play appropriate music based on task and mood.
- Understand music preferences from your real playlists.
- Avoid recommending based only on platform trending charts.

## 7. [Douban](https://www.douban.com/): Personal Movie, Book, and Game Data

Feasible methods:

- Save "watched/read/played" entries from your personal profile page.
- Self-crawl your public entry pages.
- Manually export or save entries as Markdown.
- Parse `doubanId`, title, rating, short review, date, and type from entries.

Recommended distillations:

- Number of movies/shows watched
- Number of books read
- Rating distribution
- Frequent genres
- Short review keywords
- Liked and disliked narrative traits

Agent capabilities:

- Recommend movies, books, and games closer to your real taste.
- Avoid genres you clearly dislike.
- Explain "why this recommendation."

Privacy recommendations:

- Short reviews may reveal personal emotions and experiences — review before making public.
- If self-crawling, respect platform rules and rate limits.

## 8. [Google Takeout](https://takeout.google.com/): Chrome / YouTube

Export entry:

1. Open [Google Takeout](https://takeout.google.com/).
2. Check Chrome, YouTube and YouTube Music, or other data you need.
3. Download the ZIP.

Chrome recommended processing:

- Bookmark HTML can be saved.
- Do not publicly share history entries URL by URL.
- Generate aggregate summaries:
  - Date range
  - Total record count
  - Top domains
  - Domain categories
  - AI tool visits
  - Developer tool visits
  - Local service visits
  - Original file SHA256

YouTube recommended processing:

- Categorize subscribed channels.
- Categorize playlists.
- Comment style summary.
- YouTube Music data — even if sparse, record it as-is.

Agent capabilities:

- Understand real toolchain and attention distribution through Chrome.
- Understand long-term content subscriptions and interest structure through YouTube.

Privacy recommendations:

- Chrome history is highly sensitive data — only save aggregate summaries.
- YouTube comments and watch history should also be anonymized before making public.

## 9. Steam

Recommended methods:

- Steam Web API.
- User public profile and game library.
- Local / third-party exported playtime tables.

Recommended distillations:

- Total number of games
- Played / unplayed
- Total playtime
- Top games
- Genre preferences
- Single-player / multiplayer / co-op / competitive tendencies

Agent capabilities:

- Recommend games and relaxation methods.
- Understand entertainment preferences.
- Combine with Bilibili / YouTube / Spotify for cross-media recommendations.

## 10. NAS / Media Library

Available methods:

- SSH scan of directory structure.
- MoviePilot API.
- qBittorrent API.
- Jellyfin / Emby / Plex API.

Recommended distillations:

- Storage device overview
- Media library size
- Downloader status
- PT / subscription sources
- Automation workflows

Agent capabilities:

- Know you may already have local media when recommending movies.
- Design automation workflows that fit your existing NAS.
- Make organization suggestions based on media library status.

Privacy recommendations:

- Do not publicly share internal network addresses, torrent lists, credentials, or full directory listings.

## 11. Calendar Data: Google Calendar / Apple iCloud Calendar

Calendar data is suitable for distilling "time patterns" and "long-term rhythms." Do not publicly share complete schedules, locations, or private events. It is recommended to only let the Agent read the summary layer.

### Recommended Entry Points

| Platform / Data Source | Recommended Method | Official Entry | Suitable for Distilling |
| --- | --- | --- | --- |
| Google Calendar | Export ICS / Google Calendar API | [Export](https://support.google.com/calendar/answer/37111) / [API](https://developers.google.com/workspace/calendar/api/v3/reference/events/list) | Event frequency, fixed schedules, busy/free time, recurring events, long-term rhythms |
| Apple iCloud Calendar | iCloud Calendar / CalDAV / third-party client | [App-Specific Passwords](https://support.apple.com/en-us/102654) | iCloud calendar sync, recurring events, life rhythms, cross-device schedules |

### Recommended Distillations

* Fixed schedules: classes, exams, meetings, training, family matters.
* Time patterns: high-frequency busy periods, free periods, weekend/weekday differences.
* Recurring events: weekly routines, long-term tasks, periodic maintenance items.
* Routine clues: late nights, lunch breaks, exercise, study and work rhythms.
* Actionable suggestions: when is suitable for studying, resting, exercising, or handling errands.

### Agent Capabilities

* Arrange tasks and rest periods more reasonably.
* Avoid fixed schedules and high-pressure periods when recommending plans.
* Give suggestions based on real life rhythms instead of generic time management templates.
* Discover long-term patterns, such as "weekends tend to get out of control" or "evenings are good for light tasks."

### Privacy Recommendations

* Do not publicly share the full calendar.
* Do not publicly share precise locations, family events, medical appointments, or private meetings.
* Public demos should only show aggregate summaries, such as "6 fixed weekly events" or "higher study efficiency in the evenings."
* If using CalDAV / iCloud / Google authorization, do not write account credentials, app-specific passwords, or OAuth tokens into the Wiki.

## 12. Google Account Ecosystem, Email Registration Summary, and GitHub

This section is not a password vault, but a toolchain map. The goal is to let the Agent know what platforms, services, and automation entry points the user already has.
Only record capabilities, categories, authorization methods, and summaries — never store actual credentials.

### Recommended Entry Points

| Type | Recommended Method | Official Entry | Suitable for Distilling |
| --- | --- | --- | --- |
| Google Account Ecosystem | Google Takeout / OAuth / API / App Password fallback | [Takeout](https://support.google.com/accounts/answer/3024190) / [App Passwords](https://support.google.com/accounts/answer/185833) | YouTube, Chrome, Gmail, Calendar, Drive and other Google data entry points |
| Gmail / Email Registration Summary | Gmail API / IMAP | [Gmail API](https://developers.google.com/workspace/gmail/api/guides) | Registered services, subscriptions, billing categories, toolchain clues |
| GitHub | Fine-grained PAT / GitHub App / SSH | [PAT docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) | Repos, Issues, PRs, Stars, project activity, technical interests |

### Recommended Distillations

**Google Account Ecosystem**

* YouTube: subscribed channels, playlists, favorites, watch topic summaries.
* Chrome: bookmarks, top domains, toolchain websites, AI/development/learning visit summaries.
* Gmail: service registration email summaries, subscription categories, billing categories, project email clues.
* Calendar: schedule rhythms, fixed arrangements, busy/free times.
* Drive: project documents, study materials, public/private document classification.

**Email Registration Summary**

* Registered service categories: AI platforms, cloud services, developer tools, communication tools, subscription services.
* Account status: actively used, paid, related to current project.
* Service clues: registration time, billing reminders, product notifications, login alerts.
* Toolchain map: services the user actually owns and potentially callable entry points.

**GitHub**

* Repos: projects currently maintained, long-term projects, abandoned projects.
* Issues / PRs: problems encountered, decision processes, technical debt.
* Stars: technical interests, projects to research, tool preferences.
* Commit activity: what you've actually been doing recently, not just plans.
* README / Docs: project goals, usage methods, automation entry points.

### Agent Capabilities

* Prioritize tools the user already has when recommending solutions.
* Avoid recommending platforms the user has no account for, no budget for, cannot access, or that are unsuitable.
* Know available entry points when designing automation workflows, such as Gmail, Calendar, GitHub, Google Takeout.
* Help users maintain a tool map of "what accounts and services do I actually have."
* Combine GitHub project activity to determine what the user is actually investing time in recently.

### Credentials and Authorization Rules

* Prioritize OAuth, official APIs, and Fine-grained Tokens.
* Google App Passwords only as fallback for legacy clients or special scenarios that don't support OAuth.
* Tokens, Cookies, App Passwords, and API Keys are only allowed in `.env`, system Keychain, password managers, or Secret Managers.
* The Wiki should only record "what permissions are needed" and "where to generate them" — never record actual credentials.
* Email scanning should only produce summaries and categories — do not store full email body content.

### Privacy Recommendations

* Never write passwords, API Keys, recovery codes, Cookies, or OAuth tokens.
* Gmail should only save service categories and summaries — not full private emails.
* Chrome / YouTube / Gmail public demos should only show aggregate statistics — not individual records.
* GitHub private repository information should only go into the private Wiki by default.
* Public demos should only show tool categories, such as "8 AI platforms, 5 cloud service types, 12 GitHub projects."
