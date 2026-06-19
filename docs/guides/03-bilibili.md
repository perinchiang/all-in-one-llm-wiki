# B 站：通过 [bilibili-cli](https://github.com/public-clis/bilibili-cli)

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
