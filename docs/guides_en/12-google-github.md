# Google Account Ecosystem, Email Registration Summary, and GitHub

This section is not a password vault, but a toolchain map. The goal is to let the Agent know what platforms, services, and automation entry points the user already has.
Only record capabilities, categories, authorization methods, and summaries — never store actual credentials.

## Recommended Entry Points

| Type | Recommended Method | Official Entry | Suitable for Distilling |
| --- | --- | --- | --- |
| Google Account Ecosystem | Google Takeout / OAuth / API / App Password fallback | [Takeout](https://support.google.com/accounts/answer/3024190) / [App Passwords](https://support.google.com/accounts/answer/185833) | YouTube, Chrome, Gmail, Calendar, Drive and other Google data entry points |
| Gmail / Email Registration Summary | Gmail API / IMAP | [Gmail API](https://developers.google.com/workspace/gmail/api/guides) | Registered services, subscriptions, billing categories, toolchain clues |
| GitHub | Fine-grained PAT / GitHub App / SSH | [PAT docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) | Repos, Issues, PRs, Stars, project activity, technical interests |

## Recommended Distillations

**Google Account Ecosystem**

- YouTube: subscribed channels, playlists, favorites, watch topic summaries.
- Chrome: bookmarks, top domains, toolchain websites, AI/development/learning visit summaries.
- Gmail: service registration email summaries, subscription categories, billing categories, project email clues.
- Calendar: schedule rhythms, fixed arrangements, busy/free times.
- Drive: project documents, study materials, public/private document classification.

**Email Registration Summary**

- Registered service categories: AI platforms, cloud services, developer tools, communication tools, subscription services.
- Account status: actively used, paid, related to current project.
- Service clues: registration time, billing reminders, product notifications, login alerts.
- Toolchain map: services the user actually owns and potentially callable entry points.

**GitHub**

- Repos: projects currently maintained, long-term projects, abandoned projects.
- Issues / PRs: problems encountered, decision processes, technical debt.
- Stars: technical interests, projects to research, tool preferences.
- Commit activity: what you've actually been doing recently, not just plans.
- README / Docs: project goals, usage methods, automation entry points.

## Agent Capabilities

- Prioritize tools the user already has when recommending solutions.
- Avoid recommending platforms the user has no account for, no budget for, cannot access, or that are unsuitable.
- Know available entry points when designing automation workflows, such as Gmail, Calendar, GitHub, Google Takeout.
- Help users maintain a tool map of "what accounts and services do I actually have."
- Combine GitHub project activity to determine what the user is actually investing time in recently.

## Credentials and Authorization Rules

- Prioritize OAuth, official APIs, and Fine-grained Tokens.
- Google App Passwords only as fallback for legacy clients or special scenarios that don't support OAuth.
- Tokens, Cookies, App Passwords, and API Keys are only allowed in `.env`, system Keychain, password managers, or Secret Managers.
- The Wiki should only record "what permissions are needed" and "where to generate them" — never record actual credentials.
- Email scanning should only produce summaries and categories — do not store full email body content.

## Privacy Recommendations

- Never write passwords, API Keys, recovery codes, Cookies, or OAuth tokens.
- Gmail should only save service categories and summaries — not full private emails.
- Chrome / YouTube / Gmail public demos should only show aggregate statistics — not individual records.
- GitHub private repository information should only go into the private Wiki by default.
- Public demos should only show tool categories, such as "8 AI platforms, 5 cloud service types, 12 GitHub projects."
