# JOHN IPTV AUTO v1.0

Automatically combines public IPTV playlists for Azerbaijan, Turkey, Russia and selected international categories, excluding entries labeled as adult content.

## Setup
1. Create a **public** GitHub repository named `john-iptv-auto`.
2. Upload `build.py`, `.github/workflows/update.yml`, and this README, preserving the directory structure.
3. In **Actions**, select **Update IPTV playlist** and click **Run workflow**.
4. In **Settings → Pages**, choose **Deploy from a branch**, `main`, `/docs`, then Save.
5. Once the workflow and Pages deployment succeed, the playlist URL is:
   `https://YOUR_USERNAME.github.io/john-iptv-auto/playlist.m3u`
6. Add that URL to OTTPlayer and enable periodic playlist refresh if supported.

## Limitations
- This initial version checks source download availability, **not** individual stream playback. A link appearing in the playlist may fail on the TV.
- Public playlists may include geo-restricted, expired or unstable links.
- Filtering is based on source metadata and keywords; it cannot guarantee perfect removal of all adult content. Review channels before sharing with children.
- Scheduled GitHub Actions runs can be delayed, and the repository must permit workflow writes.
- Only use sources and streams you have the right to access.
