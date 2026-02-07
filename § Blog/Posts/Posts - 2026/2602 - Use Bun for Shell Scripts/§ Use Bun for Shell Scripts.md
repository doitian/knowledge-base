---
date: '2026-02-07T00:00:00+0800'
draft: false
aliases: ["Use Bun for Shell Scripts"]
tags:
  - bun
  - javascript
  - script
  - windows
  - dev-environment
description: "Cross-platform shell scripting with Bun on Windows: avoid shebangs and WSL/Git-bash setup, with single-file executables and a built-in shell."
obsidianFiles:
- para/lets/d/Development Environment/JavaScript Shell Scripting
---

# Use Bun for Shell Scripts

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2026-02-07]]
**URL**:: [blog.iany.me](https://blog.iany.me/2026/02/use-bun-for-shell-scripts/)

I've moved most of my small scripts to Bun. It sidesteps Windows' lack of shebang support and the Git-for-Windows/WSL bash dance, and gives you one runtime for both ad-hoc shell-style commands and full scripts.

<!--more-->

## Problems Bun solves

Windows doesn't execute `#!/usr/bin/env python3` or `#!/bin/bash`, so scripts written for Linux or macOS usually need a separate PowerShell version. Bun compiles JavaScript to native executables, so a single script can run cross-platform without shebangs.

Mise [file tasks](https://mise.jdx.dev/tasks/file-tasks.html) have started to support shebangs on Windows in the latest release, but they rely on system `bash.exe`, which often points at WSL. Bun does not. You run `bun ./script.js` and embed shell commands via `Bun.$`; the script uses Bun's bundled bash environment.

## Why Bun for shell scripts

The command `bun build ./script.ts --compile --outfile script` [produces a single binary](https://bun.com/docs/bundler/executables), so no shebang or interpreter is needed on Windows. The `Bun.build` API is available too; I use a `build.js` script to walk a directory and compile all executables. Pre-built binaries start quickly—Bun's docs cite ~5ms vs Node's ~25ms for a simple script, which helps for small, frequently run scripts.

Bun has strong support for shell-style scripting. [Bun Shell](https://bun.com/docs/runtime/shell) runs bash commands; the main entry point is `Bun.$`, which constructs shell commands from template literals for safe interpolation, similar to [google/zx](https://github.com/google/zx). On Windows, Bun ships with MSYS, so you get a consistent bash environment and common Linux CLI tools without extra setup.

Other useful features:

- `Bun.secrets`—Securely store and retrieve secrets using the OS keystore (Windows Credential Manager, macOS Keychain, Linux libsecret). [Secrets - Bun](https://bun.com/docs/api/secrets)
- Built-in support for glob patterns, YAML parsing, ANSI colors, and more. [Bun Runtime](https://bun.com/docs/runtime)

## Short example

```javascript
import { $ } from "bun";

const out = await $`echo hello`.text();
console.log(out); // hello
```

Run it with `bun run script.js` or `bun ./script.js`.

## Obsidian Notes

- [[JavaScript Shell Scripting]]
