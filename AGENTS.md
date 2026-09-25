# Project Context: The Blog (`output/`)

## Overview
Staging area for [blog.iany.me](https://blog.iany.me).

## Structure
- **`§ Blog/`**: Content (Posts, Journals, Games).
- **`bin/`**: Management scripts. Run from `output/`.
- **`tags.txt`**: Kebab-case tags.
- **`mise.toml`**: Env config (`GIT_DIR`).

## Workflow
1.  **Create**: `bin/create-post "Title"` or `bin/create-journal "Title"`.
2.  **Tag**: Use the blog-tagging skill. Strict `kebab-case` from `tags.txt`.
3.  **Publish**: Push to `master`. triggers `Transpile` action -> `doitian/mirror-iany.me`.
4.  **Preview**: `mise run build` (in `~/codebase/blog-autobuild`) -> `hugo server -D` (in `~/codebase/iany.me`).

## Conventions
- **Format**: Linux (LF), YAML Frontmatter, Obsidian syntax.
- **Tags**: Flat list, no synonyms, `kebab-case`.
- **Note metadata**: Use lower kebab-case frontmatter properties. Classifications use tags instead of `status`, `done`, `priority`, `zettel`, or `kind` properties: `#i`/`#x`, `#now`/`#later`, `#zettel/...`, and `#kind/...` for flat kinds. Preserve already-nested kind tags unchanged, e.g. `#periodic/weekly` or `#obsidian/plugin`, and retain the order of multiple kinds. Keep private classifications out of public `tags`; do not infer kinds from public topic tags.
- **Workflow tags**: Internal workflow tags may remain in a note-level inline line such as `**Tags**:: #x`, separately from public frontmatter `tags`. Preserve the line and tag order during migration; do not force it into `workflow-tags` or copy it into public `tags`. Inline hashtags participate in native tag searches. Existing `workflow-tags` and legacy `Workflow tags` properties remain supported when present and need explicit property queries. Use this separation for workflow, zettel, and kind tags; do not turn section-local hashtags into note-level classifications.
- **Links and options**: Use `obsidian-files` and `allow-full-domain-link` for converter options. Use `highlights` for note links and `highlight-count` for numbers. Keep note URL annotations as Markdown links in `url`, preserving their labels and targets; the compatible converter omits these annotations from generated Hugo frontmatter. Plain `url` paths/URLs remain Hugo permalink overrides, not interchangeable note annotations.
