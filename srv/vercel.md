# [Vercel](https://vercel.com)

Refer to running it on local to configure project's settings on Vercel.

## Example 1

1. When deploy [Calcutext](https://github.com/jaredreich/calcutext) with [Vercel](https://vercel.com).
2. The Project → Settings → General → Node.js Version → `16.x`
3. Deployment → More → Redeploy

## Example 2

1. When deploy [QR code designer](https://github.com/kochrt/qr-designer) with [Github Pages](https://pages.github.com/):
2. Visit [source](https://github.com/kochrt/qr-designer) → Fork → Don't select `Copy the main branch only`
3. Fork Repository → Settings → Pages → Build and development
  1. Source → Deploy from a branch
  2. Branch → `gh-pages`, `/(root)`
4. Visit `https://<user>.github.io/qr-designer/`