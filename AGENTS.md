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
- **Note metadata**: Use lower kebab-case frontmatter properties. Classifications use tags instead of `status`, `done`, `priority`, `zettel`, or `kind` properties: `#i`/`#x`, `#now`/`#later`, `#zettel/...`, and `#kind/...` for flat kinds. Preserve already-nested kind tags unchanged, e.g. `#periodic/weekly` or `#obsidian/plugin`, and retain the order of multiple kinds. Status and zettel classifications live in the public `tags` property; the converter scrubs them from the published site. Do not infer kinds from public topic tags.
- **Workflow tags**: Status and zettel classifications go in frontmatter `tags` like public topic tags; the blog converter removes them (`i`, `x`, `now`, `next`, `later`, `zettel/...`) together with the note-only `url` and `created` properties before Hugo sees them. Existing `workflow-tags` and legacy `Workflow tags` properties remain supported when present and are scrubbed of classification values too. Do not turn section-local hashtags into note-level classifications.
- **Links and options**: Use `obsidian-files` and `allow-full-domain-link` for converter options. Use `highlights` for note links and `highlight-count` for numbers. Keep note URL annotations as Markdown links in `url`, preserving their labels and targets; the converter omits `url` from generated Hugo frontmatter, so it is never a permalink override.
