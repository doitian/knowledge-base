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
- **Note metadata**: Use lower kebab-case frontmatter properties. Classifications use tags: `#i`/`#x`, `#now`/`#later`, `#zettel/...`, and `#kind/...` for flat kinds. Preserve already-nested kind tags unchanged, e.g. `#periodic/weekly` or `#obsidian/plugin`, and retain the order of multiple kinds. Status and zettel classifications live in the public `tags` property; do not infer kinds from public topic tags.
- **Workflow tags**: The blog converter removes private classification tags (`i`, `x`, `now`, `later`, `zettel/...`, `kind/...`, `from/...`) and the note-only `url` and `created` properties from the published frontmatter. Do not turn section-local hashtags into note-level classifications.
- **Links and options**: Use `obsidian-files` and `allow-full-domain-link` for converter options. Use `highlights` for note links and `highlight-count` for numbers. Keep note URL annotations as Markdown links in `url`, preserving their labels and targets; the converter omits `url` from generated Hugo frontmatter, so it is never a permalink override.
