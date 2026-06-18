# Privacy Rules

Use this before reading or publishing sensitive data.

## Default Policy

- Treat raw exports as private.
- Do not place raw browser history, health XML, family details, account credentials, cookies, tokens, or full email data in public artifacts.
- Public examples must be generic or synthetic.
- Prefer aggregate summaries with source checksums for sensitive data.

## Source Handling

| Source | Private raw storage | Public-safe output |
| --- | --- | --- |
| Browser history | Private only | date range, counts, top domains/categories, checksum |
| Apple Health / Garmin | Private only | trends, counts, high-level health categories |
| AI memory exports | Private only | capability summary and non-sensitive themes |
| Family / relationships | Private only | omit or abstract as "personal constraints" |
| Service accounts | Private only | category counts, tool categories |
| Music / media taste | Usually safe after review | taste clusters, examples approved by user |
| Notes / study material | Depends on content | topics, concepts, learning stage |

## Redaction Checklist

Before sharing a prompt, deck, demo page, or screenshot:

- Remove real names unless the user explicitly approves.
- Remove exact addresses, emails, phones, tokens, cookies, and account IDs.
- Remove raw URLs from browser history.
- Remove exact health readings when not necessary.
- Replace private family or legal facts with abstract constraints.
- Use "for example" for capabilities that are inferred rather than already implemented.

## Language

When publishing, say "the agent can use music taste to choose a playlist" instead of exposing the user's actual private playlist names unless approved.
