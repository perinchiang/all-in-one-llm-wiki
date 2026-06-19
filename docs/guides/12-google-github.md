# Google 账号生态、邮箱注册邮件摘要和 GitHub

这一节不是密码库，而是工具链地图。目标是让 Agent 知道用户已经有哪些平台、服务和自动化入口。
只记录能力、类别、授权方式和摘要，不保存任何真实密钥。

## 推荐入口

| 类型 | 推荐方式 | 官方入口 | 适合沉淀 |
| --- | --- | --- | --- |
| Google 账号生态 | Google Takeout / OAuth / API / App Password 兜底 | [Takeout](https://support.google.com/accounts/answer/3024190) / [App Passwords](https://support.google.com/accounts/answer/185833) | YouTube、Chrome、Gmail、Calendar、Drive 等 |
| Gmail / 邮箱注册邮件摘要 | Gmail API / IMAP | [Gmail API](https://developers.google.com/workspace/gmail/api/guides) | 已注册服务、订阅、账单类别、工具链线索 |
| GitHub | Fine-grained PAT / GitHub App / SSH | [PAT 文档](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) | Repo、Issue、PR、Star、项目活动、技术兴趣 |

## 建议沉淀

**Google 账号生态**

- YouTube：订阅频道、播放列表、收藏、观看主题摘要。
- Chrome：书签、Top domains、工具链网站、AI/开发/学习类访问摘要。
- Gmail：服务注册邮件摘要、订阅类别、账单类别、项目邮件线索。
- Calendar：日程节奏、固定安排、忙闲时间。
- Drive：项目文档、学习资料、公开/私有文档分类。

**邮箱注册邮件摘要**

- 已注册服务类别：AI 平台、云服务、开发工具、通讯工具、订阅服务。
- 账号状态：是否常用、是否付费、是否和当前项目有关。
- 服务线索：注册时间、账单提醒、产品通知、登录提醒。
- 工具链地图：用户实际拥有和可能可调用的服务入口。

**GitHub**

- Repo：正在维护的项目、长期项目、废弃项目。
- Issue / PR：遇到的问题、决策过程、技术债。
- Star：技术兴趣、想研究的项目、工具偏好。
- Commit 活动：最近真正做了什么，而不是只看计划。
- README / Docs：项目目标、使用方式、自动化入口。

## Agent 能力

- 推荐方案时优先使用用户已经有的工具。
- 避免推荐用户没有账号、没有预算、不能访问或不适合的平台。
- 设计自动化工作流时知道可用入口，例如 Gmail、Calendar、GitHub、Google Takeout。
- 帮用户维护"我到底有哪些账号和服务"的工具地图。
- 结合 GitHub 项目活动，判断用户最近真正投入的方向。

## 凭据和授权规则

- 优先使用 OAuth、官方 API、Fine-grained Token。
- Google App Password 只作为不支持 OAuth 的旧式客户端或特殊场景兜底。
- Token、Cookie、App Password、API Key 只允许放在 `.env`、系统 Keychain、密码管理器或 Secret Manager。
- Wiki 里只记录"需要什么权限"和"在哪里生成"，不要记录真实密钥。
- 邮箱扫描只做摘要和分类，不保存完整邮件正文。

## 隐私建议

- 永远不要写入密码、API Key、恢复码、Cookie、OAuth token。
- Gmail 只保存服务类别和摘要，不保存私人邮件全文。
- Chrome / YouTube / Gmail 公开 demo 只展示聚合统计，不展示逐条记录。
- GitHub 私有仓库信息默认只进私有 Wiki。
- 公开 demo 只展示工具类别，例如"AI 平台 8 个、云服务 5 类、GitHub 项目 12 个"。
