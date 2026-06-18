# Publishing Checklist

Use this before publishing a README screenshot, demo wiki, deck, video script, or exported prompt.

## Must Remove

- Passwords, API keys, OAuth tokens, cookies, recovery codes, and app-specific passwords.
- Email addresses, phone numbers, account IDs, exact addresses, and private usernames.
- Raw browser history URLs, search queries, and full watch history.
- Full health exports, GPS routes, exact locations, and point-by-point heart-rate streams.
- Private family, legal, financial, medical, or workplace details.
- NAS internal addresses, torrent lists, full media directories, and private repo names.

## Prefer Instead

- Synthetic examples.
- Aggregate counts and date ranges.
- Top-level categories instead of raw records.
- Checksums for raw files when provenance matters.
- Screenshots of mock pages rather than real private pages.

## Final Pass

- Search the repository for `token`, `secret`, `password`, `cookie`, `email`, and `Takeout`.
- Confirm `.wiki/`, `raw/`, `.env`, exports, and databases are ignored by Git.
- Open every public demo page and check that it does not describe a real person.
- Mark inferred capabilities as examples unless they are already implemented.
