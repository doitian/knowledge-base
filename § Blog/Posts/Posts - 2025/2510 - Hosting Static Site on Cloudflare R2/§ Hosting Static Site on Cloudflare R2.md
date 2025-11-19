---
date: 2025-10-22T18:46:38+0800
draft: false
aliases:
  - Hosting Static Site on Cloudflare R2
allowFullDomainLink: true
tags:
  - ci
  - automation
---

# Hosting Static Site on Cloudflare R2

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2025-10-22]]
**URL**:: [blog.iany.me](https://blog.iany.me/2025/10/hosting-static-site-on-cloudflare-r2/)

This post explains how to set up a static site on Cloudflare R2.

I recently migrated my blog to Cloudflare R2, and the process went smoothly until I encountered R2's lack of native support for rewriting URLs to `index.html` files. This post explains how I resolved this issue.

## Setting Up

1. Create the bucket.
2. Add the custom domain `blog.iany.me`. To redirect `iany.me` and `www.iany.me` to the blog, add these as custom domains as well. Since I host the domain in Cloudflare, the DNS record is automatically configured.

## Publishing

I use `rclone` to deploy the site to R2. Below is the GitHub workflow I employ. Noting that the `fetch-depth` option for `actions/checkout` retrieves the complete repository history. This works with Hugo's `--enableGitInfo` flag to accurately determine article creation dates.

```yaml
name: Deploy Hugo Site to Cloudflare R2

on:
  push:
    branches:
      - master
  workflow_dispatch:

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Install latest Hugo
        run: |
          TAG=$(curl -s https://api.github.com/repos/gohugoio/hugo/releases/latest \
            | grep '"tag_name":' \
            | head -1 \
            | sed -E 's/.*"([^"]+)".*/\1/')
          curl -L "https://github.com/gohugoio/hugo/releases/download/${TAG}/hugo_${TAG#v}_Linux-64bit.tar.gz" \
            -o hugo.tar.gz
          tar -xzf hugo.tar.gz hugo
          sudo mv hugo /usr/local/bin/
          hugo version

      - name: Install rclone
        run: |
          curl https://rclone.org/install.sh | sudo bash

      - name: Build site with Hugo
        run: hugo --minify --enableGitInfo

      - name: Configure rclone for Cloudflare R2
        env:
          R2_ACCESS_KEY_ID: ${{ secrets.R2_ACCESS_KEY_ID }}
          R2_SECRET_ACCESS_KEY: ${{ secrets.R2_SECRET_ACCESS_KEY }}
          R2_ENDPOINT: ${{ secrets.R2_ENDPOINT }}
        run: |
          rclone config create r2 s3 \
            provider Cloudflare \
            access_key_id "${R2_ACCESS_KEY_ID}" \
            secret_access_key "${R2_SECRET_ACCESS_KEY}" \
            endpoint "${R2_ENDPOINT}" \
            --quiet

      - name: Deploy to Cloudflare R2
        env:
          R2_BUCKET: ${{ secrets.R2_BUCKET }}
        run: |
          rclone copy public/ r2:"${R2_BUCKET}" \
            --checksum \
            --no-traverse \
            --verbose
```

## Rules

Go to the dashboard of the domain `iany.me` and go to the section `Rules`.

### Redirect Rules

I have added 3 redirect rules:

1. When incoming requests have a hostname `iany.me` or `www.iany.me`, redirect to `concat("https://blog.iany.me", http.request.uri.path)`.
2. Redirect `https://blog.iany.me/*/index.html` to `https://blog.iany.me/${1}/`.
3. Redirect `http://*` to `https://${1}`

Although the Redirect Rules manual says if multiple rules make the same modification, the last executed rule wins, I have to put rule 2 before 3.

### URL Rewrite Rules

I added 2 rewrite rules for `index.html`:

1. When the request URL is `https://blog.iany.me` or `https://blog.iany.me/`, rewrite the URL path to `/index.html`.
2. When the request URL matches `https://blog.iany.me/*/`, rewrite the path to `${1}/index.html`

### Cache Rules

I added 2 cache rules for images and static content:

1. Set cache TTL to 1 month for `png`, `jpg`, `jpeg`, and `svg` files.
2. Set cache TTL to 1 year for files in `/js`, `/fonts`, `/css`, and `/uploads`.