# [Spotify](https://www.spotify.com/): Spotify Web API

Recommended path:

1. Go to Spotify Developer Dashboard and create an App.
2. Configure Redirect URI.
3. Obtain authorization via OAuth.
4. Pull:
   - saved tracks
   - playlists
   - recently played
   - top artists / top tracks (if scope allows)

Common notes:

- Spotify OAuth callback often requires HTTPS.
- For local development, use tunnels, reverse proxies, or public HTTPS callbacks.
- Do not put client secret in a public repository.

Recommended distillations:

- Number of playlists
- Number of saved songs
- Artist clustering
- Language / style / mood
- Scene playlists: studying, writing, exercise, rest, commuting

Agent capabilities:

- Play appropriate music based on task and mood.
- Understand music preferences from your real playlists.
- Avoid recommending based only on platform trending charts.
