### [Ebook Reader](https://github.com/ttu-ttu/ebook-reader)

![](https://img.shields.io/github/license/ttu-ttu/ebook-reader) [![](https://img.shields.io/github/last-commit/scillidan/ebook-reader/main)](https://github.com/scillidan/ebook-reader) ![](https://img.shields.io/badge/Vercel-black?style=flat&logo=Vercel&logoColor=white)

#### Deploy with Vercel

1. When deploy with [Vercel](https://vercel.com).
2. The Project → Settings
  - General → Build & Development Settings
    ```
    Build Command `pnpm build`
    Output Directory `build`
    Install Command `pnpm install --frozen-lockfile && pnpm svelte-kit sync`
    ```
  - Root Directory → `apps/web`