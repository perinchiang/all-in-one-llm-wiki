# All in One LLM Wiki

> [中文版](README.md) | [English](README_EN.md)

把你的数字生活导出成一个 **AI 可读的 LLM Wiki**，让 Agent 不再从零认识你。

这不是一个"给人看的漂亮知识库"。它更像一个给 AI/Agent 使用的长期上下文层：把笔记、AI 记忆、音乐、影视、视频平台、浏览器、健康、游戏、工具链、NAS 等数据整理成结构化 Markdown Wiki，让 Agent 能在回答、推荐、规划和自动化时读懂你的真实背景。

## 项目定位

当前版本是一个 **通用 Agent Skill / starter kit**：

- `SKILL.md`：给支持 Skill 的 Agent 读取的执行说明。
- `references/`：数据源、隐私、Schema、展示叙事的参考文档。
- `scripts/`：可改造的本地初始化和导入示例。
- `examples/demo-wiki/`：公开安全的合成 demo。

它不是全自动采集器，也不默认读取你的隐私数据。真实导入前，应该由你明确提供数据源或授权范围。

## 快速安装

```bash
mkdir -p ~/.hermes/skills
git clone https://github.com/perinchiang/all-in-one-llm-wiki ~/.hermes/skills/all-in-one-llm-wiki
```

或者直接发给你的 LLM Agent：

> Use https://github.com/perinchiang/all-in-one-llm-wiki to create a private .wiki/ in my Obsidian vault from my exported Bilibili/Spotify/AI memory files.

## 5 分钟本地体验

先不要放真实隐私数据，用合成 demo 跑通结构：

```bash
git clone https://github.com/perinchiang/all-in-one-llm-wiki
cd all-in-one-llm-wiki
python scripts/init_wiki.py --demo
```

运行后会生成：

```text
.wiki/
  SCHEMA.md
  index.md
  log.md
  entities/demo-profile.md
  concepts/context-home.md
  raw/
```

正式给自己建私有 Wiki 时：

```bash
python scripts/init_wiki.py
```

## 它解决什么问题

普通 AI 对话的问题是：每次都要重新解释自己是谁、在做什么、喜欢什么、有哪些工具、现在处于什么阶段。

All in One LLM Wiki 的目标是：

- 把分散在各个平台的数据整理成 AI 能检索和引用的 Wiki。
- 保留来源、置信度和隐私边界，避免变成不可审计的“人格猜测”。
- 让 Agent 基于真实上下文做事，而不是只给泛泛建议。

例如：

- 导入 [Spotify](#6-spotifyspotify-web-api) 后，Agent 可以按你的音乐品味和当前场景选择歌单。
- 导入 [豆瓣](#7-豆瓣个人影音书数据) 后，Agent 推荐影视和书时不再只看热门榜。
- 导入 [B 站](#3-b-站通过-bilibili-cli) / [YouTube](#8-google-takeoutchrome--youtube) 后，Agent 能知道你最近真正关注的学习和娱乐主题。
- 导入 [Chrome](#8-google-takeoutchrome--youtube) / [Google Takeout](#8-google-takeoutchrome--youtube) 后，Agent 能理解你的工具链、项目现场和注意力分布。
- 导入 [Garmin](#4-garmin通过-python-脚本) / [Apple Health](#5-apple-health手机健康-app-导出) 后，Agent 可以结合睡眠、步数、运动记录给更接地气的生活建议。
- 导入 [AI 平台记忆](#2-ai-平台记忆导出) 后，Agent 可以合并多个 AI 对你的片段理解，减少重复解释。

## 和 llm-wiki 的关系

本项目受 Karpathy 的 LLM-Wiki 概念启发，也可以和已有的 `llm-wiki` skill 配合使用。

区别在于：

- `llm-wiki` 更偏“知识库框架”：初始化 Wiki、消化文章/文件、生成图谱、维护页面。
- `All in One LLM Wiki` 更偏“数字生活入口”：告诉你各种个人数据从哪里导出、如何脱敏、如何变成 Agent 可用的长期上下文。

你可以把本项目当成 `llm-wiki` 的数据入口层。

## 快速开始

推荐目录结构：

```text
.wiki/                    # 私有知识库，默认不要提交到 Git
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

> 如果你想公开演示，可以另外维护一个 `examples/` 或 `public-demo/`，只放脱敏后的模拟数据和聚合摘要。

基本流程：

1. 先建 Wiki 结构：`SCHEMA.md`、`index.md`、`log.md`、`raw/`、`entities/`、`concepts/`。
2. 每导入一个来源，先把原始导出放进 `raw/` 的对应目录。
3. 再生成一个或多个 `entities/` 或 `concepts/` 页面。
4. 在 `index.md` 写一行摘要，方便 Agent 先读目录。
5. 在 `log.md` 记录来源、时间、导入方式、隐私处理。
6. 对敏感来源，只保存聚合摘要，不公开原始数据。

## 安全边界方案

All in One LLM Wiki 默认应该是“本地优先、私有优先、脱敏后再共享”。下面这套边界适合大多数个人 Agent 场景：

| 方案 | 作用 | 安全等级 |
| --- | --- | --- |
| `.wiki/` 隐藏文件夹 | 防止误看、误扫、误提交；把真实私有 Wiki 和公开仓库分开 | 低 |
| `.gitignore` | 防止 raw 导出、健康数据、浏览器记录、密钥文件上传到 GitHub | 中 |
| `chmod 700 .wiki` | 限制同一台机器上其他用户读取私有 Wiki | 中 |
| `.env` 分离 token | 防止 API key、OAuth token、账号密码进入代码仓库 | 中 |
| 本地优先处理 | 原始导出默认在本机解析，不先上传给第三方模型或云服务 | 高 |
| 加密 raw 数据 | 即使磁盘或备份泄露，也降低原始导出被直接读取的风险 | 高 |
| 脱敏再进 Wiki | 防止 prompt、截图、公开 demo 泄露浏览、健康、家庭、账号等隐私 | 高 |
| 权限分层 | 防止 Agent 默认读取全部数据；按任务只开放需要的目录或页面 | 高 |

推荐最小配置：

```bash
mkdir -p .wiki/raw .wiki/entities .wiki/concepts .wiki/queries .wiki/_archive
chmod 700 .wiki
touch .env
```

`.gitignore` 至少应该包含：

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

### 权限分层建议

不要让 Agent 一上来就读取整个 `.wiki/raw/`。更安全的做法是分层：

| 层级 | 内容 | Agent 默认权限 |
| --- | --- | --- |
| Public / Demo | 脱敏示例、聚合摘要、README、方法论 | 可读 |
| Wiki Summary | `index.md`、实体页、概念页、低敏摘要 | 按任务可读 |
| Sensitive Summary | 健康、浏览、账号、家庭等摘要页 | 需要用户确认 |
| Raw Private | 原始导出、浏览记录、健康 XML、token、账号清单 | 默认不可读 |

### 加密 raw 数据

如果必须保留原始导出，可以考虑：

- 使用系统级磁盘加密。
- 用 Cryptomator / VeraCrypt / age / gpg 管理 `raw/`。
- 只把解密后的聚合摘要交给 Agent。
- 在 `log.md` 记录“原始数据已加密保存，Wiki 只保留摘要”。

## 数据入口总表

| 入口 | 推荐导出方式 | 适合沉淀成什么 | 隐私级别 |
| --- | --- | --- | --- |
| Obsidian / 本地笔记 | 直接读取 Markdown 文件夹 | 学习阶段、项目、概念、术语 | 中 |
| AI 平台记忆 | 向平台询问/导出长期记忆，手动保存 Markdown | 跨平台自我画像、偏好、长期目标 | 高 |
| B 站 | `bilibili-cli` 登录后导出 history / favorites / following | 当前兴趣、学习视频、创作者偏好 | 中高 |
| Garmin | Python `garminconnect` 脚本拉取摘要 | 睡眠、步数、运动、恢复建议 | 高 |
| Apple Health | iPhone 健康 App 头像 → 导出全部健康数据 | 长期健康趋势、运动历史 | 高 |
| Spotify | Spotify Web API / OAuth | 音乐品味、场景歌单、艺术家偏好 | 中 |
| 豆瓣 | 个人主页/条目数据保存或自爬，解析评分和短评 | 影视、书、游戏口味 | 中 |
| Google Takeout | Chrome / YouTube 导出 | 浏览器工具链、YouTube 订阅和播放列表 | 高 |
| Steam | Steam Web API | 游戏库、游玩时长、游戏类型偏好 | 中 |
| NAS / 媒体库 | SSH 扫描 + MoviePilot/qBittorrent/Jellyfin API | 本地媒体库、自动化能力 | 高 |
| 日历 | ICS / CalDAV / 平台导出 | 时间安排、低频/高频日程 | 高 |
| 咖啡 / 生活记录 | Markdown、CSV、表格或手动日志 | 生活偏好、消费习惯、作息线索 | 中 |
| 服务账号 / 工具链 | 手动清单、邮箱摘要、密码管理器分类导出 | 可用工具、云服务、自动化平台 | 高 |

## 逐项导出方法

### 1. Obsidian / 本地笔记

适合导入：

- 学习笔记
- 项目笔记
- 术语库
- 课程笔记
- 已完成项目复盘

做法：

1. 找到本地 Vault 或导出的 Markdown 文件夹。
2. 原始文件放进 `raw/notes/`。
3. 按主题生成 `concepts/`，按人物、工具、项目、平台生成 `entities/`。
4. 保留原文件路径或来源说明。

Agent 能力：

- 按你的已有笔记解释概念。
- 结合你的学习阶段给练习建议。
- 避免每次都从通用教材角度重新讲。

### 2. AI 平台记忆导出

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
不要编造。如果不确定，请标注“可能”或“需要确认”。
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

- 很多平台没有“一键导出记忆”按钮，实际做法通常是直接询问它“你记得我什么”，再手动保存回答。
- 这类数据可能包含健康、家庭、账号、位置等敏感信息，默认只进私有库。

### 3. B 站：通过 [bilibili-cli](https://github.com/JimmyLJX/bilibili-cli)

安装：

```bash
pip install bilibili-cli
```

登录后导出观看历史、收藏夹、关注列表：

```bash
bili login
bili history --output raw/platform-exports/bilibili/history-YYYY-MM-DD.json
bili favorites --output raw/platform-exports/bilibili/favorites-YYYY-MM-DD.json
bili following --output raw/platform-exports/bilibili/following-YYYY-MM-DD.json
```

建议沉淀：

- 最近观看主题
- 收藏夹分类
- 高频 UP 主
- 学习类 vs 娱乐类占比
- 当前关注的技术/游戏/生活主题

Agent 能力：

- 知道你最近真实在看什么。
- 根据收藏夹判断学习路线。
- 结合视频平台兴趣推荐资料、课程或休息内容。

隐私建议：

- 不建议公开完整观看历史。
- 公开展示时只用分类占比和少量脱敏示例。

### 4. [Garmin](https://connect.garmin.com/)：通过 Python 脚本

可用库：

```bash
pip install garminconnect
```

登录链接确认邮箱和密码：

- 国际版：https://connect.garmin.com/app
- 中国版：https://connect.garmin.cn/app/

推荐做法：

1. 用环境变量保存账号密码，不要写进脚本：

```bash
export GARMIN_EMAIL="your-email@example.com"
export GARMIN_PASSWORD="your-password"
```

2. 用脚本拉取：

- daily summary
- sleep
- steps
- recent activities
- personal records

3. 原始 JSON 放进：

```text
.wiki/raw/health/garmin/
```

4. 可从 `scripts/garmin_to_wiki_example.py` 开始改造；脚本默认输出到 `.wiki/`，也可以用 `LLM_WIKI_DIR` 指定目录。
5. Wiki 页面只写摘要和趋势。

Agent 能力：

- 根据近期睡眠和运动量建议恢复或训练。
- 发现异常运动记录并提示确认。
- 根据长期习惯调整计划。

隐私建议：

- 不公开 GPS 路线、精确位置、账号邮箱、逐点心率。
- 公开版本只写趋势和聚合数。

### 5. Apple Health：手机健康 App 导出

iPhone 上操作：

1. 打开 **健康** App。
2. 点击右上角头像。
3. 滚动到底部，选择 **导出所有健康数据**。
4. 系统会生成一个 ZIP。
5. 解压后通常会得到 `export.xml`。

导入建议：

1. 本地解析 `export.xml`，不要直接把完整 XML 放到公开仓库。
2. 提取聚合摘要：
   - 时间范围
   - 总记录数
   - 步数趋势
   - 运动类型统计
   - 体重/体脂趋势
   - 睡眠覆盖情况
3. 摘要 JSON 放到：

```text
.wiki/raw/health/apple-health-summary-YYYY-MM-DD.json
```

Agent 能力：

- 理解长期健康基线。
- 结合 Garmin 当前数据判断变化。
- 给更贴近现实的作息和运动建议。

### 6. [Spotify](https://www.spotify.com/)：Spotify Web API

推荐路径：

1. 到 Spotify Developer Dashboard 创建 App。
2. 配置 Redirect URI。
3. 通过 OAuth 获取授权。
4. 拉取：
   - saved tracks
   - playlists
   - recently played
   - top artists / top tracks（如果 scope 允许）

常见注意点：

- Spotify OAuth 的回调地址经常要求 HTTPS。
- 本地开发可用隧道、反代或公网 HTTPS 回调。
- 不要把 client secret 放进公开仓库。

Hermes Agent 用户可直接使用内置 Spotify 集成，详见 [Spotify 文档](https://hermes-agent.nousresearch.com/docs/user-guide/features/spotify)。

建议沉淀：

- 歌单数量
- 收藏歌曲数量
- 艺人聚类
- 语种/风格/情绪
- 场景歌单：学习、写作、运动、休息、通勤

Agent 能力：

- 按任务和心情播放合适音乐。
- 用你的真实歌单理解音乐偏好。
- 避免只按平台热门推荐。

### 7. [豆瓣](https://www.douban.com/)：个人影音书数据

可行方式：

- 保存个人主页上的“看过/读过/玩过”条目。
- 自爬自己的公开条目页面。
- 手动导出或保存条目 Markdown。
- 解析条目中的 `doubanId`、标题、评分、短评、日期、类型。

建议沉淀：

- 看过影视数量
- 读过书数量
- 评分分布
- 高频类型
- 短评关键词
- 喜欢和讨厌的叙事特征

Agent 能力：

- 推荐影视和书时更贴近真实品味。
- 避开你明显不喜欢的类型。
- 解释“为什么推荐这个”。

隐私建议：

- 短评可能暴露个人情绪和经历，公开前要筛。
- 如果自爬，请尊重平台规则和频率限制。

### 8. [Google Takeout](https://takeout.google.com/)：Chrome / YouTube

导出入口：

1. 打开 [Google Takeout](https://takeout.google.com/)。
2. 勾选 Chrome、YouTube and YouTube Music，或其他需要的数据。
3. 下载 ZIP。

Chrome 建议处理：

- 书签 HTML 可以保存。
- 历史记录不要公开逐条 URL。
- 生成聚合摘要：
  - 日期范围
  - 总记录数
  - Top domains
  - 域名分类
  - AI 工具访问
  - 开发工具访问
  - 本地服务访问
  - 原始文件 SHA256

YouTube 建议处理：

- 订阅频道分类。
- 播放列表分类。
- 评论风格摘要。
- YouTube Music 数据如果很少，也要如实记录。

Agent 能力：

- 通过 Chrome 理解真实工具链和注意力分布。
- 通过 YouTube 理解长期内容订阅和兴趣结构。

隐私建议：

- Chrome history 是高敏数据，只建议保存聚合摘要。
- YouTube 评论和观看历史公开前也要脱敏。

### 9. Steam

推荐方式：

- Steam Web API。
- 用户公开资料和游戏库。
- 本地/第三方导出的游戏时长表。

建议沉淀：

- 游戏总数
- 玩过/未玩
- 总时长
- Top games
- 类型偏好
- 单机/多人/合作/竞技倾向

Agent 能力：

- 推荐游戏和休息方式。
- 理解娱乐偏好。
- 结合 B 站/YouTube/Spotify 做跨媒体推荐。

### 10. NAS / 媒体库

可用方式：

- SSH 扫描目录结构。
- MoviePilot API。
- qBittorrent API。
- Jellyfin / Emby / Plex API。

建议沉淀：

- 存储设备概览
- 媒体库规模
- 下载器状态
- PT/订阅源
- 自动化流程

Agent 能力：

- 推荐影视时知道你可能已有本地片源。
- 设计自动化流程时能贴合现有 NAS。
- 结合媒体库状态做整理建议。

隐私建议：

- 不公开内网地址、种子列表、认证信息、完整目录。

### 11. 日历数据：Google Calendar / Apple iCloud Calendar

日历数据适合沉淀"时间模式"和"长期节奏"，不要把完整日程、地点、私人事件直接公开。建议只让 Agent 读取摘要层。

#### 推荐入口

| 平台 / 数据源              | 推荐方式                         | 官方入口                                                                                                                                                                                      | 适合沉淀                        |
| --------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| Google Calendar       | 导出 ICS / Google Calendar API | [Google Calendar 导出](https://support.google.com/calendar/answer/37111) / [Google Calendar API Events.list](https://developers.google.com/workspace/calendar/api/v3/reference/events/list) | 日程频率、固定安排、忙闲时间、重复事件、长期节奏    |
| Apple iCloud Calendar | iCloud 日历 / CalDAV / 第三方客户端  | [Apple App-Specific Passwords](https://support.apple.com/en-us/102654)                                                                                                                    | iCloud 日历同步、重复事件、生活节奏、跨设备日程 |

#### 建议沉淀

* 固定安排：课程、考试、会议、训练、家庭事务。
* 时间模式：高频忙碌时段、空闲时段、周末/工作日差异。
* 重复事件：每周例行、长期任务、定期维护事项。
* 作息线索：晚睡、午休、运动、学习和工作节奏。
* 可行动建议：什么时候适合学习、休息、运动、处理杂事。

#### Agent 能力

* 更合理地安排任务和休息。
* 在推荐计划时避开固定日程和高压时段。
* 结合真实生活节奏给建议，而不是只给通用时间管理模板。
* 发现长期模式，例如"周末更容易失控""晚上适合轻任务"。

#### 隐私建议

* 不公开完整日历。
* 不公开精确地点、家庭事件、医疗预约、私人会面。
* 公开 demo 只展示聚合摘要，例如"每周固定日程 6 个""晚上学习效率更高"。
* 如果使用 CalDAV / iCloud / Google 授权，不要把账号、App 专用密码、OAuth token 写入 Wiki。

### 12. Google 账号生态、邮箱注册邮件摘要和 GitHub

这一节不是密码库，而是工具链地图。目标是让 Agent 知道用户已经有哪些平台、服务和自动化入口。
只记录能力、类别、授权方式和摘要，不保存任何真实密钥。

#### 推荐入口

| 类型               | 推荐方式                                           | 官方入口                                                                                                                                                 | 适合沉淀                                              |
| ---------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Google 账号生态      | Google Takeout / OAuth / API / App Password 兜底 | [Google Takeout](https://support.google.com/accounts/answer/3024190) / [Google App Passwords](https://support.google.com/accounts/answer/185833)     | YouTube、Chrome、Gmail、Calendar、Drive 等 Google 数据入口 |
| Gmail / 邮箱注册邮件摘要 | Gmail API / IMAP / Hermes Email 集成             | [Gmail API Guides](https://developers.google.com/workspace/gmail/api/guides)                                                                         | 已注册服务、订阅、账单类别、工具链线索                               |
| GitHub           | Fine-grained PAT / GitHub App / SSH            | [GitHub Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) | Repo、Issue、PR、Star、项目活动、技术兴趣                      |

#### 建议沉淀

##### Google 账号生态

* YouTube：订阅频道、播放列表、收藏、观看主题摘要。
* Chrome：书签、Top domains、工具链网站、AI/开发/学习类访问摘要。
* Gmail：服务注册邮件摘要、订阅类别、账单类别、项目邮件线索。
* Calendar：日程节奏、固定安排、忙闲时间。
* Drive：项目文档、学习资料、公开/私有文档分类。

##### 邮箱注册邮件摘要

* 已注册服务类别：AI 平台、云服务、开发工具、通讯工具、订阅服务。
* 账号状态：是否常用、是否付费、是否和当前项目有关。
* 服务线索：注册时间、账单提醒、产品通知、登录提醒。
* 工具链地图：用户实际拥有和可能可调用的服务入口。

##### GitHub

* Repo：正在维护的项目、长期项目、废弃项目。
* Issue / PR：遇到的问题、决策过程、技术债。
* Star：技术兴趣、想研究的项目、工具偏好。
* Commit 活动：最近真正做了什么，而不是只看计划。
* README / Docs：项目目标、使用方式、自动化入口。

#### Agent 能力

* 推荐方案时优先使用用户已经有的工具。
* 避免推荐用户没有账号、没有预算、不能访问或不适合的平台。
* 设计自动化工作流时知道可用入口，例如 Gmail、Calendar、GitHub、Google Takeout。
* 帮用户维护"我到底有哪些账号和服务"的工具地图。
* 结合 GitHub 项目活动，判断用户最近真正投入的方向。

#### 凭据和授权规则

* 优先使用 OAuth、官方 API、Fine-grained Token。
* Google App Password 只作为不支持 OAuth 的旧式客户端或特殊场景兜底。
* Token、Cookie、App Password、API Key 只允许放在 `.env`、系统 Keychain、密码管理器或 Secret Manager。
* Wiki 里只记录"需要什么权限"和"在哪里生成"，不要记录真实密钥。
* 邮箱扫描只做摘要和分类，不保存完整邮件正文。

#### 隐私建议

* 永远不要写入密码、API Key、恢复码、Cookie、OAuth token。
* Gmail 只保存服务类别和摘要，不保存私人邮件全文。
* Chrome / YouTube / Gmail 公开 demo 只展示聚合统计，不展示逐条记录。
* GitHub 私有仓库信息默认只进私有 Wiki。
* 公开 demo 只展示工具类别，例如"AI 平台 8 个、云服务 5 类、GitHub 项目 12 个"。

## 页面模板

每个实体页建议包含：

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
- 推测：需要标注为推测

## Agent affordances

- Agent 现在可以做什么。
- Agent 应该避免什么。

## Open questions

- 需要用户确认的点。

## Cross-links

- [[related-page]]
```

## 隐私边界

建议分成两套：

- 私有完整库：保存真实来源、原始导出、敏感细节，只给自己和可信 Agent 使用。
- 公开脱敏版：只展示结构、方法、聚合统计和模拟样例。

不要公开：

- 浏览器逐条历史
- 健康原始 XML / GPS 路线 / 逐点心率
- 家庭、法律、财务等私人细节
- 账号、邮箱、手机号、API Key、OAuth token
- NAS 内网地址、完整媒体目录、种子列表

安全底线：

- 私有 Wiki 放 `.wiki/`，公开仓库只放方法、模板和脱敏 demo。
- 原始数据先本地解析，必要时加密保存。
- Agent 默认读摘要层，不默认读 raw 层。
- 每次生成 PPT、视频、README、截图前，先做一次脱敏检查。
- 开源或发布前按 `PUBLISHING_CHECKLIST.md` 做最后检查。

## 推荐的 `log.md` 记录格式

```markdown
## [YYYY-MM-DD] ingest | Source name
- Source: export/API/manual source
- Method: command, script, or manual steps
- Created:
  - entities/example.md — summary
- Updated:
  - index.md — added source summary
- Privacy: raw data private; public version uses aggregates only
- Notes: parser assumptions, skipped files, anomalies
```
