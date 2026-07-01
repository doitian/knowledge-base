---
date: '2026-07-01T21:27:36+0800'
draft: true
aliases: ["Fix Claude Desktop PATH with CLAUDE_ENV_FILE"]
tags:
  - dev-environment
  - environment-variables
  - automation
  - tool
description: "Point CLAUDE_ENV_FILE at a shell snippet so Claude Code sees the same PATH and env vars as your mise/asdf/nix setup, with full runtime shell semantics."
---

# Fix Claude Desktop PATH with CLAUDE_ENV_FILE

**Status**:: #i
**Zettel**:: #zettel/permanent
**Created**:: [[2026-07-01]]
**URL**:: [blog.iany.me](https://blog.iany.me/2026/07/fix-claude-desktop-path-with-claude-env-file/)

Claude Code runs tools and shell commands on your behalf. Launched from a terminal, the CLI inherits your shell environment and everything just works. But under **Claude Desktop**, Claude Code is spawned from a GUI/desktop session that never sourced your interactive shell config—so if you rely on version managers like mise, asdf, or nix, the tools they install may not be on Claude's `PATH`. The fix is a single setting: `CLAUDE_ENV_FILE`.

<!--more-->

## How it works

Set `CLAUDE_ENV_FILE` in `.claude/settings.local.json` to point at a shell file. Claude sources it before running any command.

```json
{
  "env": {
    "CLAUDE_ENV_FILE": ".claude/mise.env"
  }
}
```

That file is a plain shell snippet—`export` statements, one per line:

```sh
export PATH="/home/ian/.local/share/mise/shims:/home/ian/project/node_modules/.bin:$PATH"
export DATABASE_URL="postgres://localhost/db"
```

The path can be relative—it's resolved from the project root—so `.claude/mise.env` works on any machine and can be committed alongside the project. Write both, and the next Claude session picks up everything.

## Why not just put PATH in settings.json?

You can set `env.PATH` directly in `settings.local.json`, but there's a catch: Claude does not support variable substitution like `${env:PATH}`. You'd have to hardcode the full `PATH`, which breaks the moment dependencies change or you move between machines.

With `CLAUDE_ENV_FILE` you get full shell semantics—`$PATH` expands at runtime, conditionals work, and subshells are fair game.

## Why shell init doesn't help either: the snapshot

There's a deeper reason the obvious fixes fail. At session start, Claude Code freezes a **shell snapshot** to `~/.claude/shell-snapshots/snapshot-zsh-*.sh`, and the Bash tool sources that file before every command it runs.

The snapshot's *final* line is `export PATH=<frozen value>`, and that value is Claude Code's own process `PATH` captured at startup—not re-derived from your shell config. (You can spot it: it contains directories no rc file adds, like Claude's own plugin and session `bin` paths.) Because this `export PATH` is the last thing sourced before each command, it clobbers anything your shell init did:

- `mise activate` in `.zshenv`/`.zshrc` runs, prepends the shims—then the snapshot's trailing `export PATH` overwrites it, burying the shims back where they started.
- Even setting `env.PATH` in `settings.json` as a plain subprocess variable loses, because the snapshot is sourced *after* the process environment is set up.

`CLAUDE_ENV_FILE` wins because it's sourced **after** the snapshot. Its `export PATH="…/shims:$PATH"` is the last word, so the shims land first for every Bash tool call. That's the whole trick: it's not just convenient shell semantics—it's the one hook that runs late enough to survive the snapshot.

## Generating the env file automatically

Writing the env file by hand gets tedious. If you use mise, you can generate both files with a task—I vibe-coded [`preset-claude.js`](https://github.com/doitian/dotfiles-public/blob/master/src/mise-tasks/preset-claude.js) for exactly this (it's a custom mise task, not a built-in). It:

1. Reads `env._.path` from `mise.toml` (so per-project `node_modules/.bin` directories land on `PATH`).
2. Expands `{{config_root}}` to absolute paths.
3. Writes `.claude/mise.env` with shims, extra paths, and all mise env vars.
4. Sets `CLAUDE_ENV_FILE` in `.claude/settings.local.json`.

```sh
mise run preset:claude
```

One command, and Claude sees the exact same tools you do.

## What about other version managers?

The pattern works for anything that can write a shell env file:

- **asdf**: `asdf direnv envrc > .claude/asdf.env`
- **nix**: `nix print-dev-env | grep ^export > .claude/nix.env`
- **direnv**: `direnv export json | jq -r 'to_entries[] | "export \(.key)=\"\(.value)\""' > .claude/direnv.env`

Then point `CLAUDE_ENV_FILE` at it and you're set.

## Caveats

- The file is sourced, not executed—shebang lines are ignored.
- Changes to `settings.local.json` take effect on the next Claude session.
- If `CLAUDE_ENV_FILE` is a relative path, it's resolved from the project root.

A small config file saves you from fighting invisible `PATH` issues. Set it once, and Claude runs the same tools you do.
