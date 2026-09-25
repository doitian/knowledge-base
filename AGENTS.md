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
- **Note metadata**: Use lower kebab-case frontmatter properties. Store `status` and `zettel` as single plain enum strings and `kind` as an ordered list of plain strings, following the vault's schema. Keep private classifications out of public `tags`; do not infer kinds from public topic tags.
- **Workflow tags**: Store other internal note tags in `workflow-tags`, separately from public `tags`. This property is not indexed by `tag:` searches; Bases and searches must include it explicitly. Consumers retain compatibility with legacy `Workflow tags` during migration.
- **Links and options**: Use `obsidian-files` and `allow-full-domain-link` for converter options. Use `highlights` for note links and `highlight-count` for numbers. Keep note URL annotations as Markdown links in `url`, preserving their labels and targets; the compatible converter omits these annotations from generated Hugo frontmatter. Plain `url` paths/URLs remain Hugo permalink overrides, not interchangeable note annotations.
