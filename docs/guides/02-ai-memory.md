# AI 平台记忆导出

适合平台：

- [ChatGPT](https://chatgpt.com/)
- [Claude](https://claude.ai/)
- [Gemini](https://gemini.google.com/)
- [Perplexity](https://www.perplexity.ai/)
- [豆包](https://www.doubao.com/)
- 其他带长期记忆/用户画像的 AI

通用提示词：

```text
请导出或整理你当前记得的关于我的长期记忆。
请按主题分组，区分确定事实、推测、偏好、长期目标、工具链、项目、健康/生活方式等。
不要编造。如果不确定，请标注"可能"或"需要确认"。
请输出 Markdown，方便导入一个私有 LLM Wiki。
```

实践建议：

1. 每个平台单独导出，保存到 `raw/ai-memory/<platform>-memory-export-YYYY-MM-DD.md`。
2. 把重复事实合并进同一个实体页。
3. 把平台特有的信息保留下来，并标注来源。
4. 对冲突信息写入 `needs confirmation`，不要强行合并。

Agent 能力：

- 合并多个 AI 对你的片段理解。
- 发现重复、冲突和遗漏。
- 形成更稳定的长期上下文。

注意：

- 很多平台没有"一键导出记忆"按钮，实际做法通常是直接询问它"你记得我什么"，再手动保存回答。
- 这类数据可能包含健康、家庭、账号、位置等敏感信息，默认只进私有库。
