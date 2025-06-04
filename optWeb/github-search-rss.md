# [github-search-rss](https://github.com/azu/github-search-rss)

![](https://img.shields.io/github/license/azu/github-search-rss?style=flat-square) ![](https://img.shields.io/github/last-commit/scillidan/github-search-rss/main?label=last%20commit%20(fork)&style=flat-square)![](https://img.shields.io/badge/GitHub%20Pages-121013?logo=github&logoColor=white)

1. [azu/github-search-rss](https://github.com/azu/github-search-rss) → Fork → Copy the `main` branch only (Off) → Create fork.
2. Fork repo → Actions → Enable.
3. Settings → Pages → Build and deployment → Branch → `gh-pages`, `/(root)` → Save.
4. Edit `BASE_URL`, `SEARCH_ITEMS` in `src/RSS.ts`:
   ```ts
   const BASE_URL = "https://<username>.github.io/github-search-rss";
   export const SEARCH_ITEMS: RSSItem[] = [
       {
           title: "goldendict",
           query: "goldendict sort:updated-desc",
           TYPE: "REPOSITORY",
           link: `${BASE_URL}/goldendict.json`
       },
       {
           title: "keypirinha",
           query: "keypirinha sort:updated-desc",
           TYPE: "REPOSITORY",
           link: `${BASE_URL}/keypirinha-repo.json`
       }
   ];
   ```
5. Commit changes... → Commit changes.
6. Wait for actions to run. Then visit `https://<username>.github.io/github-search-rss/`.