# [Ebook Reader](https://github.com/ttu-ttu/ebook-reader)

![](https://img.shields.io/github/license/ttu-ttu/ebook-reader?style=flat-square) ![](https://img.shields.io/github/last-commit/scillidan/ebook-reader/main?label=last%20commit%20(fork)&style=flat-square)

## Deploy with Vercel

1. When deploy with [Vercel](https://vercel.com).
2. The Project → Settings
  - General → Build & Development Settings
    ```
    Build Command `pnpm build`
    Output Directory `build`
    Install Command `pnpm install --frozen-lockfile && pnpm svelte-kit sync`
    ```
  - Root Directory → `apps/web`