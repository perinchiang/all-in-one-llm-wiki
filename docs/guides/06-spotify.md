# [Spotify](https://www.spotify.com/)：Spotify Web API

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
