# Security Boundary Plan

> For the full data ingestion overview and quick install, go back to [README](../README_EN.md).

All in One LLM Wiki should by default be "local-first, privacy-first, anonymize before sharing." The following boundaries suit most personal Agent scenarios:

| Measure | Purpose | Security Level |
| --- | --- | --- |
| `.wiki/` hidden folder | Prevent accidental viewing, scanning, or committing; separate the real private Wiki from the public repository | Low |
| `.gitignore` | Prevent raw exports, health data, browser history, and key files from being uploaded to GitHub | Medium |
| `chmod 700 .wiki` | Prevent other users on the same machine from reading the private Wiki | Medium |
| `.env` for token separation | Prevent API keys, OAuth tokens, and account passwords from entering the code repository | Medium |
| Local-first processing | Raw exports are parsed locally by default, not uploaded to third-party models or cloud services first | High |
| Encrypt raw data | Even if disk or backup leaks, reduce the risk of raw exports being directly read | High |
| Anonymize before entering Wiki | Prevent prompts, screenshots, and public demos from leaking browsing, health, family, and account privacy | High |
| Permission layering | Prevent the Agent from reading all data by default; only open needed directories or pages per task | High |

## Recommended Minimum Configuration

```bash
mkdir -p .wiki/raw .wiki/entities .wiki/concepts .wiki/queries .wiki/_archive
chmod 700 .wiki
touch .env
```

`.gitignore` should at least contain:

```gitignore
.wiki/
raw/
.env
.env.*
*.zip
*.xml
*.db
*.sqlite
*Takeout*
*export.xml*
*apple-health*
*garmin*
*history*
*cookies*
*token*
```

## Permission Layering Recommendations

Don't let the Agent read the entire `.wiki/raw/` right away. A safer approach is layering:

| Layer | Content | Agent Default Permission |
| --- | --- | --- |
| Public / Demo | Anonymized examples, aggregate summaries, README, methodology | Readable |
| Wiki Summary | `index.md`, entity pages, concept pages, low-sensitivity summaries | Readable per task |
| Sensitive Summary | Health, browsing, account, family, etc. summary pages | Requires user confirmation |
| Raw Private | Raw exports, browsing history, health XML, tokens, account lists | Not readable by default |

## Encrypting Raw Data

If you must keep the original exports, consider:

- Use system-level disk encryption.
- Use Cryptomator / VeraCrypt / age / gpg to manage `raw/`.
- Only hand the decrypted aggregate summaries to the Agent.
- Record in `log.md`: "Raw data encrypted and stored, Wiki only retains summaries."

## Privacy Boundaries

It is recommended to maintain two versions:

- Private complete library: stores real sources, raw exports, and sensitive details — for personal use and trusted Agents only.
- Public anonymized version: only shows structure, methodology, aggregate statistics, and mock examples.

Do not publicly share:

- Browser history entry by entry
- Health raw XML / GPS routes / point-by-point heart rate
- Family, legal, financial, and other private details
- Accounts, email addresses, phone numbers, API Keys, OAuth tokens
- NAS internal addresses, full media directory listings, torrent lists

Security baseline:

- Private Wiki goes in `.wiki/`; public repository only contains methods, templates, and anonymized demos.
- Parse raw data locally first; encrypt when necessary.
- Agent reads the summary layer by default — not the raw layer.
- Before generating any PPT, video, README, or screenshot, perform an anonymization check first.
- Before publishing, use `PUBLISHING_CHECKLIST.md` as a final pass.
