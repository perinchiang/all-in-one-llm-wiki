# IMA 知识库集成

> 将腾讯 IMA 知识库中的数据导入 LLM Wiki,让 Agent 能搜索你订阅的公域知识库。

## 前置条件

1. 注册腾讯 IMA 账号:访问 [ima.qq.com](https://ima.qq.com) 下载客户端
2. 获取 API 凭证:在 [ima.qq.com/agent-interface](https://ima.qq.com/agent-interface) 生成 Client ID 和 API Key
3. 安装 IMA 技能到你的 Agent(参考 [SKILL.md](../SKILL.md))

## 配置凭证

将凭证写入配置文件:

```bash
mkdir -p ~/.config/ima
echo "your_client_id" > ~/.config/ima/client_id
echo "your_api_key" > ~/.config/ima/api_key
chmod 600 ~/.config/ima/api_key ~/.config/ima/client_id
```

或通过环境变量:

```bash
export IMA_OPENAPI_CLIENTID="your_client_id"
export IMA_OPENAPI_APIKEY="your_api_key"
```

## 浏览和订阅公域知识库

在 IMA 桌面客户端进入「知识库广场」,搜索感兴趣的公域知识库并订阅。

推荐搜索方向:

| 方向 | 推荐关键词 | 说明 |
|------|-----------|------|
| 网络工程 | `HCIE` `华为` `数据中心` `网络安全` | 认证备考、技术文档 |
| AI | `AI` `Agent` `大模型` `提示词` | 行业资料、工具评测 |
| 编程 | `Python` `JavaScript` `算法` | 教程、代码库 |
| 阅读 | `书单` `电子书` `TED` | 书单推荐、演讲笔记 |

## 将 IMA 集成到 LLM Wiki

### 查询 IMA 知识库

Agent 可通过 IMA API 搜索已订阅知识库中的内容:

```bash
# 搜索华为网络知识库
ima_api "openapi/wiki/v1/search_knowledge" '{
  "query": "VXLAN",
  "knowledge_base_id": "<kb_id>",
  "cursor": ""
}'

# 搜索 AI 资料库
ima_api "openapi/wiki/v1/search_knowledge" '{
  "query": "Agent",
  "knowledge_base_id": "<kb_id>",
  "cursor": ""
}'
```

### 自动清洗到 Wiki

在 LLM Wiki 的 `entities/` 目录下创建索引页 `pat-ima-subscriptions.md`:

```markdown
---
title: IMA 知识库订阅索引
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity
tags: [ima, knowledge-base, subscription]
sources: []
confidence: high
---

# IMA 知识库订阅索引

| 知识库 | 文件数 | 说明 |
|--------|--------|------|
| 华为网络知识 | 3,157 | 路由交换/HCIE 认证/华为经典书籍 |
| AI资料库 | 380 | ChatGPT/Agent/提示词/应用 |
| 网络空间安全精品图书馆 | 7,153 | 网络安全/密码学/渗透测试 |
```

### 定时同步

设置每周定时任务,让 Agent 自动搜索 IMA 知识库中的新内容,写入 WASH 总结:

```
🌐 每周自动循环
  ↓
IMA 知识库搜索 → 提取新内容 → 更新 Wiki 索引 → 刷新 Agent 画像
```

### 支持的 API

| 功能 | API | 说明 |
|------|-----|------|
| 列出知识库 | `search_knowledge_base` | 搜索已订阅/创建的知识库 |
| 知识库搜索 | `search_knowledge` | 在指定知识库内搜索内容 |
| 浏览内容 | `get_knowledge_list` | 浏览知识库目录结构 |
| 添加网页 | `import_urls` | 添加网页到知识库 |
| 上传文件 | `create_media` → COS → `add_knowledge` | 上传文件到知识库 |
| 新建笔记 | `import_doc` | 创建新笔记 |
| 追加笔记 | `append_doc` | 追加内容到已有笔记 |

## 隐私说明

- API Key 仅用于 IMA 官方接口认证,只发送到 `ima.qq.com`
- 公域知识库数据来自其他用户的公开分享,导入 Wiki 后按 `.gitignore` 规则管理
- 建议在 `log.md` 中记录每次导入的来源和时间
