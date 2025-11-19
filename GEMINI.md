# Gemini Project Context

## Overview
This repository acts as the source of truth for a personal Knowledge Base and Blog. It is structured as an [Obsidian](https://obsidian.md/) vault, containing Markdown files that are processed and published to [blog.iany.me](https://blog.iany.me) via a CI/CD pipeline.

## Directory Structure

- **`§ Blog/`**: The core content directory.
    - **`Posts/`**: Long-form articles and blog posts, organized by year (e.g., `Posts - 2024`).
    - **`Journals/`**: Weekly or daily logs, organized by year (e.g., `Journals - 2024`).
    - **`Games/`**: Content related to games.
- **`bin/`**: Helper scripts for content management.
    - `create-post`: Scaffolds a new blog post.
    - `create-journal`: Scaffolds a new journal entry.
    - `tag-post`: interactive CLI to add/remove tags from a post.
    - `suggest-tags`: Generates an AI prompt to suggest tags for a post based on its content and `tags.txt`.
- **`.github/workflows/`**: Contains the `transpile.yml` workflow which handles the build and deployment.

## Key Files

- **`tags.txt`**: A master list of all tags used across the knowledge base. This file is used by the `bin\suggest-tags` script.
- **`mise.toml`**: Configuration for `mise` (environment manager), defining the git directory path.
- **`README.md`**: General project information and links.

## Workflow & Usage

### 1. Creating Content
Use the scripts in `bin/` to start new entries. These scripts handle folder structure and Frontmatter generation.

```bash
# Create a new post
bin/create-post "Title of the Post"

# Create a new journal entry
bin/create-journal
```

### 2. Tagging
Tags are essential for organization. All tags should be **kebab-case**.

- **Get Suggestions:** Use `bin/suggest-tags` to ask Gemini for tag recommendations based on the existing tag vocabulary.
    ```bash
    bin/suggest-tags "path/to/post.md"
    ```

### 3. Publishing
Pushing changes to the `master` branch triggers the GitHub Action (`Transpile`). This action:
1.  Downloads a transpiler script (`x.py`) from `doitian/blog-autobuild`.
2.  Converts the Obsidian-flavored Markdown to Hugo-compatible Markdown.
3.  Pushes the result to the `doitian/mirror-iany.me` repository, which serves the live site.

## Conventions

- **Line Ending**: Use Linux line endings (LF).
- **Frontmatter:** All posts use YAML Frontmatter for metadata (date, draft status, aliases, tags).
- **Obsidian Features:** The content utilizes Obsidian-specific syntax like Wikilinks (`[[Link]]`) and image embeds (`![[image.png]]`).
- **Tagging:**
    - Maintain a flat list of tags in `tags.txt`.
    - Avoid synonym tags; reuse existing ones where possible.
    - Use `kebab-case` for all tags.
