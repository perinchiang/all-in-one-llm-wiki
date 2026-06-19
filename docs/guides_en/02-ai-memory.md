# AI Platform Memory Export

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
