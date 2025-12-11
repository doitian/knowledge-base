---
date: 2025-11-26T11:31:37+0800
draft: false
aliases:
  - How to Activate mise for Cursor When It Runs Shell Commands
tags:
  - mise
  - cursor
  - shell
  - zsh
  - vibe-coding
description: Learn how to configure mise to work with Cursor's non-login shell environment by activating it in .zshenv when CURSOR_AGENT is detected.
---

# How to Activate mise for Cursor When It Runs Shell Commands

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2025-11-26]]
**URL**:: [blog.iany.me](https://blog.iany.me/2025/11/how-to-activate-mise-for-cursor-when-it-runs-shell-commands/)

When using [mise](https://mise.jdx.dev/) with Cursor, you may notice that the mise environment is not activated when Cursor executes shell commands. This occurs because Cursor launches a non-login shell, which initializes differently than an interactive login shell and therefore does not automatically source your usual mise setup.

<!--more-->

## The Problem

Cursor runs commands in a non-login shell, which means:

- For **zsh**: Only `.zshenv` is loaded (not `.zshrc`)
- For **bash**: Only `.bash_profile` is loaded (not `.bashrc`)

If you've configured mise activation in `.zshrc` or `.zprofile`, it won't be available when Cursor executes commands.

## The Solution

The solution is to activate mise in `.zshenv` (for zsh) or `.bash_profile` (for bash) when the file is loaded by Cursor. You can detect Cursor by checking for the `CURSOR_AGENT` environment variable.

Add this to your `~/.zshenv` or `~/.bash_profile`:

```shell
# Activate mise when running in Cursor
if [[ -n "$CURSOR_AGENT" ]]; then
  eval "$(mise activate)"
fi
```

## Why This Works

- `.zshenv` (or `.bash_profile`) is always sourced for non-login shells
- The `CURSOR_AGENT` environment variable is set when Cursor runs commands
- By conditionally activating mise only when `CURSOR_AGENT` is present, you avoid potential conflicts or slowdowns in other non-login shell contexts
- This ensures mise and all its configured tools are available when Cursor executes terminal commands

After adding this configuration, rerun Cursor chats, and mise should be available in all Cursor shell commands.
