# 逐项导出方法

> 完整的数据入口总表和快速安装，请回到 [README](../README.md)。

## 1. Obsidian / 本地笔记

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

## 2. AI 平台记忆导出

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

## 3. B 站：通过 [bilibili-cli](https://github.com/JimmyLJX/bilibili-cli)

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

## 4. [Garmin](https://connect.garmin.com/)：通过 Python 脚本

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

## 5. Apple Health：手机健康 App 导出

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

## 6. [Spotify](https://www.spotify.com/)：Spotify Web API

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

## 7. [豆瓣](https://www.douban.com/)：个人影音书数据

可行方式：

- 保存个人主页上的"看过/读过/玩过"条目。
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
- 解释"为什么推荐这个"。

隐私建议：

- 短评可能暴露个人情绪和经历，公开前要筛。
- 如果自爬，请尊重平台规则和频率限制。

## 8. [Google Takeout](https://takeout.google.com/)：Chrome / YouTube

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

## 9. Steam

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

## 10. NAS / 媒体库

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

## 11. 日历数据：Google Calendar / Apple iCloud Calendar

日历数据适合沉淀"时间模式"和"长期节奏"，不要把完整日程、地点、私人事件直接公开。建议只让 Agent 读取摘要层。

### 推荐入口

| 平台 / 数据源 | 推荐方式 | 官方入口 | 适合沉淀 |
| --- | --- | --- | --- |
| Google Calendar | 导出 ICS / Google Calendar API | [导出](https://support.google.com/calendar/answer/37111) / [API](https://developers.google.com/workspace/calendar/api/v3/reference/events/list) | 日程频率、固定安排、忙闲时间、重复事件、长期节奏 |
| Apple iCloud Calendar | iCloud 日历 / CalDAV / 第三方客户端 | [App-Specific Passwords](https://support.apple.com/en-us/102654) | iCloud 日历同步、重复事件、生活节奏、跨设备日程 |

### 建议沉淀

* 固定安排：课程、考试、会议、训练、家庭事务。
* 时间模式：高频忙碌时段、空闲时段、周末/工作日差异。
* 重复事件：每周例行、长期任务、定期维护事项。
* 作息线索：晚睡、午休、运动、学习和工作节奏。
* 可行动建议：什么时候适合学习、休息、运动、处理杂事。

### Agent 能力

* 更合理地安排任务和休息。
* 在推荐计划时避开固定日程和高压时段。
* 结合真实生活节奏给建议，而不是只给通用时间管理模板。
* 发现长期模式，例如"周末更容易失控""晚上适合轻任务"。

### 隐私建议

* 不公开完整日历。
* 不公开精确地点、家庭事件、医疗预约、私人会面。
* 公开 demo 只展示聚合摘要，例如"每周固定日程 6 个""晚上学习效率更高"。
* 如果使用 CalDAV / iCloud / Google 授权，不要把账号、App 专用密码、OAuth token 写入 Wiki。

## 12. Google 账号生态、邮箱注册邮件摘要和 GitHub

这一节不是密码库，而是工具链地图。目标是让 Agent 知道用户已经有哪些平台、服务和自动化入口。
只记录能力、类别、授权方式和摘要，不保存任何真实密钥。

### 推荐入口

| 类型 | 推荐方式 | 官方入口 | 适合沉淀 |
| --- | --- | --- | --- |
| Google 账号生态 | Google Takeout / OAuth / API / App Password 兜底 | [Takeout](https://support.google.com/accounts/answer/3024190) / [App Passwords](https://support.google.com/accounts/answer/185833) | YouTube、Chrome、Gmail、Calendar、Drive 等 |
| Gmail / 邮箱注册邮件摘要 | Gmail API / IMAP | [Gmail API](https://developers.google.com/workspace/gmail/api/guides) | 已注册服务、订阅、账单类别、工具链线索 |
| GitHub | Fine-grained PAT / GitHub App / SSH | [PAT 文档](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) | Repo、Issue、PR、Star、项目活动、技术兴趣 |

### 建议沉淀

**Google 账号生态**

* YouTube：订阅频道、播放列表、收藏、观看主题摘要。
* Chrome：书签、Top domains、工具链网站、AI/开发/学习类访问摘要。
* Gmail：服务注册邮件摘要、订阅类别、账单类别、项目邮件线索。
* Calendar：日程节奏、固定安排、忙闲时间。
* Drive：项目文档、学习资料、公开/私有文档分类。

**邮箱注册邮件摘要**

* 已注册服务类别：AI 平台、云服务、开发工具、通讯工具、订阅服务。
* 账号状态：是否常用、是否付费、是否和当前项目有关。
* 服务线索：注册时间、账单提醒、产品通知、登录提醒。
* 工具链地图：用户实际拥有和可能可调用的服务入口。

**GitHub**

* Repo：正在维护的项目、长期项目、废弃项目。
* Issue / PR：遇到的问题、决策过程、技术债。
* Star：技术兴趣、想研究的项目、工具偏好。
* Commit 活动：最近真正做了什么，而不是只看计划。
* README / Docs：项目目标、使用方式、自动化入口。

### Agent 能力

* 推荐方案时优先使用用户已经有的工具。
* 避免推荐用户没有账号、没有预算、不能访问或不适合的平台。
* 设计自动化工作流时知道可用入口，例如 Gmail、Calendar、GitHub、Google Takeout。
* 帮用户维护"我到底有哪些账号和服务"的工具地图。
* 结合 GitHub 项目活动，判断用户最近真正投入的方向。

### 凭据和授权规则

* 优先使用 OAuth、官方 API、Fine-grained Token。
* Google App Password 只作为不支持 OAuth 的旧式客户端或特殊场景兜底。
* Token、Cookie、App Password、API Key 只允许放在 `.env`、系统 Keychain、密码管理器或 Secret Manager。
* Wiki 里只记录"需要什么权限"和"在哪里生成"，不要记录真实密钥。
* 邮箱扫描只做摘要和分类，不保存完整邮件正文。

### 隐私建议

* 永远不要写入密码、API Key、恢复码、Cookie、OAuth token。
* Gmail 只保存服务类别和摘要，不保存私人邮件全文。
* Chrome / YouTube / Gmail 公开 demo 只展示聚合统计，不展示逐条记录。
* GitHub 私有仓库信息默认只进私有 Wiki。
* 公开 demo 只展示工具类别，例如"AI 平台 8 个、云服务 5 类、GitHub 项目 12 个"。
