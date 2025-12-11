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
2.  **Tag**: `bin/suggest-tags "path/to/post.md"`. Strict `kebab-case` from `tags.txt`.
3.  **Publish**: Push to `master`. triggers `Transpile` action -> `doitian/mirror-iany.me`.
4.  **Preview**: `mise run build` (in `~/codebase/blog-autobuild`) -> `hugo server -D` (in `~/codebase/iany.me`).

## Conventions
- **Format**: Linux (LF), YAML Frontmatter, Obsidian syntax.
- **Tags**: Flat list, no synonyms, `kebab-case`.
