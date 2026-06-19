# 安全边界方案

> 完整的数据入口总表和快速安装，请回到 [README](../README.md)。

All in One LLM Wiki 默认应该是"本地优先、私有优先、脱敏后再共享"。下面这套边界适合大多数个人 Agent 场景：

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

## 推荐最小配置

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

## 权限分层建议

不要让 Agent 一上来就读取整个 `.wiki/raw/`。更安全的做法是分层：

| 层级 | 内容 | Agent 默认权限 |
| --- | --- | --- |
| Public / Demo | 脱敏示例、聚合摘要、README、方法论 | 可读 |
| Wiki Summary | `index.md`、实体页、概念页、低敏摘要 | 按任务可读 |
| Sensitive Summary | 健康、浏览、账号、家庭等摘要页 | 需要用户确认 |
| Raw Private | 原始导出、浏览记录、健康 XML、token、账号清单 | 默认不可读 |

## 加密 raw 数据

如果必须保留原始导出，可以考虑：

- 使用系统级磁盘加密。
- 用 Cryptomator / VeraCrypt / age / gpg 管理 `raw/`。
- 只把解密后的聚合摘要交给 Agent。
- 在 `log.md` 记录"原始数据已加密保存，Wiki 只保留摘要"。

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
