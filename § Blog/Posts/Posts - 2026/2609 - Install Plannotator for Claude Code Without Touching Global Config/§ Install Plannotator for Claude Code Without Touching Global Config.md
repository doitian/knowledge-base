---
date: 2026-09-22T17:09:27+0800
draft: false
aliases:
  - Install Plannotator for Claude Code Without Touching Global Config
tags:
  - dev-environment
  - tool
  - automation
  - programming
  - i
  - zettel/permanent
description: Install the Plannotator CLI with --minimal, then its plugin and skills into a single project with --scope local and a subdirectory skills spec, so nothing lands in ~/.claude.
created: "[[2026-09-22]]"
url: "[blog.iany.me](https://blog.iany.me/2026/09/install-plannotator-for-claude-code-without-touching-global-config/)"

---

# Install Plannotator for Claude Code Without Touching Global Config


[Plannotator](https://github.com/backnotprop/plannotator) gives Claude Code a browser UI for marking up plans, files, and pull requests. It ships as three separate things—a **CLI**, a Claude Code **plugin**, and a set of **skills**—and the obvious install path for each one drops it into your user-level environment, where it loads in every project forever. You can keep the whole thing inside one repo instead. Trying it out shouldn't cost you a permanent resident in `~/.claude`.

<!--more-->

## Install the CLI, minimally

The plugin and the skills both shell out to a `plannotator` binary, so that has to exist first. Its installer defaults to a full setup: the `sem` semantic-diff sidecar, the CallDiff and agent-terminal runtimes, and per-agent integrations—skills, hooks, slash commands, and config written into the homes of Claude, Codex, OpenCode, Gemini, and Kiro. That is precisely the global footprint this post is about avoiding.

`--minimal` (aliased `--binary-only`) drops all of it and installs just the binary:

```sh
curl -fsSL https://plannotator.ai/install.sh | bash -s -- --minimal
```

On Windows the installer takes a `-Minimal` switch, but piping into `pwsh` gives you no way to pass it—so download the script, run it, and clean up:

```powershell
$installer = Join-Path ([IO.Path]::GetTempPath()) 'plannotator-install.ps1'
Invoke-WebRequest 'https://plannotator.ai/install.ps1' -OutFile $installer
try { & $installer -Minimal } finally { Remove-Item -LiteralPath $installer -Force -ErrorAction SilentlyContinue }
```

Both exit right after the binary lands—`~/.local/bin/plannotator` on Unix, `%LOCALAPPDATA%\plannotator\plannotator.exe` on Windows, with that directory added to the user PATH. Nothing else is written anywhere. `PLANNOTATOR_MINIMAL=1` in the environment does the same thing if you'd rather not thread the flag through a wrapper, and `--no-minimal` / `-NoMinimal` overrides it back.

The one thing you give up is the CallDiff call-flow runtime, which the review UI offers to install on demand the first time you enable Call flow—so it's deferred, not lost. `plannotator uninstall` removes the binary later.

## Setup

Three commands, all run from the project directory:

```sh
claude plugin marketplace add backnotprop/plannotator --scope local
claude plugin install plannotator@plannotator --scope local
bunx skills add backnotprop/plannotator/apps/skills/core --agent claude-code --yes
```

The plugin and the skills are independent installs. The plugin brings the hooks that intercept plan mode; the skills teach Claude how to drive the CLI. You want both, and each has its own notion of scope.

## Where everything lands

`--scope local` is the key. Claude Code has three scopes—`user`, `project`, and `local`—and only `local` keeps the change out of both your home directory and the repo's committed settings:

- The marketplace and plugin declarations go into `.claude/settings.local.json` in the project.
- The skills are copied into `.claude/skills/<name>/`.
- A `skills-lock.json` is written at the project root.

Nothing touches `~/.claude`. Open Claude in any other directory and Plannotator isn't there.

## The skills path gotcha

This is the part that will bite you. The obvious command is wrong:

```sh
# Don't do this
bunx skills add backnotprop/plannotator --agent claude-code --yes
```

Pointed at the repo root, `skills add` finds and installs `release-plannotator`, `review-renovate`, and `update-deps`. Those are the skills the Plannotator maintainers use to *develop Plannotator*—drafting release notes, reviewing Renovate PRs, auditing dependency bumps. They're useless to you, and they'll happily start suggesting themselves in your own repo.

The user-facing skills live in subdirectories, and `skills add` accepts an `owner/repo/path` spec:

| Path | Skills |
| --- | --- |
| `apps/skills/core` | `plannotator` (CLI reference), `plannotator-annotate` (annotate markdown, config files, HTML, URLs, folders), `plannotator-last` (annotate the latest assistant message), `plannotator-review` (browser code review for a worktree or PR URL) |
| `apps/skills/extra` | `plannotator-compound`, `plannotator-setup-goal`, `plannotator-visual-explainer` |

`core` is what you want. Before installing anything from a repo you don't know, list first:

```sh
bunx skills add backnotprop/plannotator/apps/skills/core -l
```

`-l` clones and prints the skill names and descriptions without writing a thing—worth doing for any skills repo, not just this one.

## Teardown

Removing is fiddlier than installing:

```sh
bunx skills remove plannotator plannotator-annotate plannotator-last plannotator-review --agent claude-code --yes
claude plugin disable plannotator@plannotator --scope local
```

To get rid of it completely rather than just disabling it:

```sh
claude plugin uninstall plannotator@plannotator --scope local -y
claude plugin marketplace remove plannotator
```

Two things make the skills side awkward:

**`skills remove` matches by skill name, not by package.** The symmetric-looking command does nothing:

```sh
$ bunx skills remove backnotprop/plannotator --agent claude-code --yes
■  No matching skills found for: backnotprop/plannotator
```

It exits successfully and removes nothing. So any teardown script has to spell out every skill name, and it silently goes stale when upstream adds or renames one. The `skills-lock.json` does record the source of each installed skill, so the CLI has the information—it just doesn't use it for removal.

## Notes for scripting it

Two behaviours matter if you wrap these in a script:

- **`claude plugin install` is idempotent and re-enables a disabled plugin.** Running it again on an installed plugin prints "already installed" and exits 0; running it on a *disabled* one turns it back on. So one command works as both "install" and "enable"—no need to branch.
- **`claude plugin disable` exits 1 when the plugin is already disabled.** In a script that stops at the first failure, that will abort the rest of your teardown. Remove the skills *before* disabling the plugin, so a redundant disable can't strand the skills in your project.

Which gives a pair of scripts worth keeping around. Setup:

```sh
#!/bin/sh
set -e
claude plugin marketplace add backnotprop/plannotator --scope local
claude plugin install plannotator@plannotator --scope local
bunx skills add backnotprop/plannotator/apps/skills/core --agent claude-code --yes
```

Teardown:

```sh
#!/bin/sh
set -e
bunx skills remove plannotator plannotator-annotate plannotator-last plannotator-review --agent claude-code --yes
claude plugin disable plannotator@plannotator --scope local
```

Run both from the project directory—every path they touch is relative to it.

## What it replaced

Before this I had my own small skill for the review half of the job: [guided-pr-review](https://github.com/doitian/dotfiles-public/tree/master/ai/local-skills/guided-pr-review). It captures a PR against its real merge base, groups the diff into risk-ordered chunks with related context and the questions worth answering, and builds a standalone HTML page with line-level annotations that the agent then answers. A single `SKILL.md` plus optional Python helpers—standard library, Git, and `gh`—so it drops into any project's `.claude/skills/` and works on whatever agent you point it at.

It does that one thing, and does it well. Plannotator does considerably more: plan review through the plan-mode hooks, annotating arbitrary files, folders, and URLs, annotating the last assistant message, exporting and sharing reviews. Once a tool covers the whole surface, keeping a homemade one around for a corner of it stops making sense.

## Why bother

Claude Code's context is a budget. Every globally installed plugin and skill spends a slice of it in every session, including the ones where you're editing a config file and want nothing more than an editor. Local scope makes trying a tool reversible: install it in the one repo where it earns its keep, and if it doesn't, delete the directory and it's gone.
