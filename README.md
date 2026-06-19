# All in One LLM Wiki

> [中文版](README.md) | [English](README_EN.md)

[![GitHub Stars](https://img.shields.io/github/stars/perinchiang/all-in-one-llm-wiki?style=social)](https://github.com/perinchiang/all-in-one-llm-wiki)

▶️ [视频演示](https://www.bilibili.com/video/BV1qqji6rEyp/)

![Wiki Index Demo](assets/wiki-index-demo.png)

把你的数字生活导出成一个 **AI 可读的 LLM Wiki**，让 Agent 不再从零认识你。

这不是一个“给人看的漂亮知识库”。它更像一个给 AI/Agent 使用的长期上下文层：把笔记、AI 记忆、音乐、影视、视频平台、浏览器、健康、游戏、工具链、NAS 等数据整理成结构化 Markdown Wiki，让 Agent 能在回答、推荐、规划和自动化时读懂你的真实背景。

就像你不会一次性读完所有笔记，而是先看目录再翻到感兴趣的那页。Wiki 把各平台的原始数据蒸馏成一份 index，Agent 按需加载，不需要遍历全部数据。

## 兼容 Agent

本项目是通用 Agent Skill,任何能读取 `SKILL.md` 和本地文件的 Agent 均可使用:

- [OpenClaw](https://github.com/openclaw)
- [Hermes Agent](https://hermes-agent.nousresearch.com/)
- [WorkBuddy](https://workbuddy.ai/)
- [Claude Code](https://claude.ai/)
- [HanaAgent](https://github.com/liliMozi/openhanako)
- 其他支持 Skill / Tool / MCP 机制的 LLM Agent

## 快速安装

```bash
git clone https://github.com/perinchiang/all-in-one-llm-wiki
```

或者直接发给你的 LLM Agent:

> Use https://github.com/perinchiang/all-in-one-llm-wiki to create a private .wiki/ in my Obsidian vault from my exported Bilibili/Spotify/AI memory files.

## Before / After

**没有 LLM Wiki 时:**

```text
你:推荐一部电影
Agent:《盗梦空间》是诺兰的经典作品,评分很高......(泛泛而谈)
```

**有了 LLM Wiki 之后:**

```text
你:推荐一部电影
Agent:你豆瓣标记了 327 部"看过",评分集中在 7-8 分,
偏好悬疑和科幻,对纯爱情片评分普遍偏低。
最近 B 站收藏了几个"高智商烧脑"剪辑。
推荐《看不见的客人》-- 西班牙悬疑片,节奏紧凑,
你之前给《利刃出鞘》打了 8 分,风格接近。
```

Wiki 让 Agent 从"通用百科"变成"了解你的助手"。

## 它解决什么问题

普通 AI 对话的问题是:每次都要重新解释自己是谁、在做什么、喜欢什么、有哪些工具、现在处于什么阶段。

All in One LLM Wiki 的目标是:

- 把分散在各个平台的数据整理成 AI 能检索和引用的 Wiki。
- 保留来源、置信度和隐私边界,避免变成不可审计的"人格猜测"。
- 让 Agent 基于真实上下文做事,而不是只给泛泛建议。

例如:

- 导入 Spotify 后,Agent 可以按你的音乐品味和当前场景选择歌单。
- 导入豆瓣后,Agent 推荐影视和书时不再只看热门榜。
- 导入 B 站 / YouTube 后,Agent 能知道你最近真正关注的学习和娱乐主题。
- 导入 Chrome / Google Takeout 后,Agent 能理解你的工具链、项目现场和注意力分布。
- 导入 Garmin / Apple Health 后,Agent 可以结合睡眠、步数、运动记录给更接地气的生活建议。
- 导入 AI 平台记忆后,Agent 可以合并多个 AI 对你的片段理解,减少重复解释。

## 数据入口总表

| 入口 | 推荐导出方式 | 适合沉淀成什么 | 隐私级别 |
| --- | --- | --- | --- |
| Obsidian / 本地笔记 | 直接读取 Markdown 文件夹 | 学习阶段、项目、概念、术语 | 中 |
| AI 平台记忆 | 向平台询问/导出长期记忆,手动保存 Markdown | 跨平台自我画像、偏好、长期目标 | 高 |
| B 站 | `bilibili-cli` 登录后导出 history / favorites / following | 当前兴趣、学习视频、创作者偏好 | 中高 |
| Garmin | Python `garminconnect` 脚本拉取摘要 | 睡眠、步数、运动、恢复建议 | 高 |
| Apple Health | iPhone 健康 App 头像 → 导出全部健康数据 | 长期健康趋势、运动历史 | 高 |
| Spotify | Spotify Web API / OAuth | 音乐品味、场景歌单、艺术家偏好 | 中 |
| 豆瓣 | 个人主页/条目数据保存或自爬,解析评分和短评 | 影视、书、游戏口味 | 中 |
| Google Takeout | Chrome / YouTube 导出 | 浏览器工具链、YouTube 订阅和播放列表 | 高 |
| Steam | Steam Web API | 游戏库、游玩时长、游戏类型偏好 | 中 |
| NAS / 媒体库 | SSH 扫描 + MoviePilot/qBittorrent/Jellyfin API | 本地媒体库、自动化能力 | 高 |
| 日历 | ICS / CalDAV / 平台导出 | 时间安排、低频/高频日程 | 高 |
| 咖啡 / 生活记录 | Markdown、CSV、表格或手动日志 | 生活偏好、消费习惯、作息线索 | 中 |
| 服务账号 / 工具链 | 手动清单、邮箱摘要、密码管理器分类导出 | 可用工具、云服务、自动化平台 | 高 |

> 详细的逐项导出方法(含代码、脚本、隐私建议):[docs/export-guides.md](docs/export-guides.md)

## 目录结构

```text
.wiki/                    # 私有知识库,默认不要提交到 Git
  SCHEMA.md
  index.md
  log.md
  raw/
    ai-memory/
    platform-exports/
    health/
    notes/
  entities/
  concepts/
  queries/
  _archive/
```

基本流程:

1. 先建 Wiki 结构:`SCHEMA.md`、`index.md`、`log.md`、`raw/`、`entities/`、`concepts/`。
2. 每导入一个来源,先把原始导出放进 `raw/` 的对应目录。
3. 再生成一个或多个 `entities/` 或 `concepts/` 页面。
4. 在 `index.md` 写一行摘要,方便 Agent 先读目录。
5. 在 `log.md` 记录来源、时间、导入方式、隐私处理。
6. 对敏感来源,只保存聚合摘要,不公开原始数据。

## 安全与隐私

默认原则:**本地优先、私有优先、脱敏后再共享**。

核心措施:`.wiki/` 隐藏文件夹 + `.gitignore` 排除 raw 数据 + 权限分层(Agent 默认只读摘要层,不读 raw 层)。

> 完整的安全方案、`.gitignore` 模板、权限分层、加密建议:[docs/security.md](docs/security.md)

## 页面模板

每个实体页建议包含:

```markdown
---
title: Example Profile
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity
tags: [profile, source-name]
sources: [raw/platform-exports/example.json]
confidence: high
---

# Example Profile

> 一句话说明这个页面能让 Agent 理解什么。

## Overview

| Dimension | Value |
| --- | --- |
| Source | API / export / manual |
| Date range | YYYY-MM-DD to YYYY-MM-DD |
| Confidence | high |

## Findings

- 事实 1
- 事实 2
- 推测:需要标注为推测

## Agent affordances

- Agent 现在可以做什么。
- Agent 应该避免什么。

## Open questions

- 需要用户确认的点。

## Cross-links

- [[related-page]]
```

## 推荐的 `log.md` 记录格式

```markdown
## [YYYY-MM-DD] ingest | Source name
- Source: export/API/manual source
- Method: command, script, or manual steps
- Created:
  - entities/example.md - summary
- Updated:
  - index.md - added source summary
- Privacy: raw data private; public version uses aggregates only
- Notes: parser assumptions, skipped files, anomalies
```

## 附录

- 本项目受 Karpathy 的 [LLM-Wiki](https://github.com/karpathy/llm-wiki) 概念启发,可作为 `llm-wiki` 的数据入口层。
- 开源或发布前请按 `PUBLISHING_CHECKLIST.md` 做最后检查。
