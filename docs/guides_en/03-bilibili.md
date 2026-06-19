# Bilibili: via [bilibili-cli](https://github.com/public-clis/bilibili-cli)

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
