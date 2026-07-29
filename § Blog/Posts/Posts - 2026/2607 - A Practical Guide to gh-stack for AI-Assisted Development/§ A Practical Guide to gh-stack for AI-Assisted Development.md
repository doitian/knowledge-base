---
date: 2026-07-30T07:19:53+0800
draft: false
aliases:
  - A Practical Guide to gh-stack for AI-Assisted Development
tags:
  - git
  - automation
  - tool
  - programming
  - productivity
description: Use gh-stack with one worktree per stack, agent-planned focused branches, gh stack rebase --upstack, and AI-assisted JSON sync after squash or amend.
---

# A Practical Guide to gh-stack for AI-Assisted Development

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2026-07-30]]
**URL**:: [blog.iany.me](https://blog.iany.me/2026/07/a-practical-guide-to-gh-stack-for-ai-assisted-development/)

Stacked pull requests let you review a feature in logical slices rather than one enormous diff. The challenge is managing the branches, synchronizing PRs, and surviving rebases without breaking the chain. [gh-stack][] handles the scaffolding. It tracks your branch stack in a local JSON file, generates PRs that base each one to its parent, and works on any GitHub repo regardless of whether your organization has enabled native stacked PR support.

[gh-stack]: https://github.github.com/gh-stack/

<!--more-->

This is the workflow I use, including how an AI coding agent fits into it.

## Start with a Worktree

Before creating any branches, set up a dedicated Git worktree for the stack.

```bash
git worktree add ../project-login-stack login-stack-base
cd ../project-login-stack
```

It's not required but my personal preference. Stacks and worktrees map one-to-one. This matters for a few reasons:

- You can switch between stacks by switching directories, not branches.
- Your shell's working directory tells you exactly which stack you're in.

## Using an Agent to Build the Stack

Stacked PRs only work well if the individual branches are focused. Broad, unfocused branches defeat the point. This is where AI agents help.

When starting a feature, describe it to the agent and ask it to divide the work into discrete units. A typical breakdown might look like:

1. **Database layer** – schema and migrations
2. **Service layer** – business logic and data access
3. **API layer** – endpoints and serializers
4. **UI layer** – frontend components

The agent creates a branch for each, makes commits scoped to that layer, and stacks them in order. You end up with four focused PRs instead of one that mixes migrations, API code, and React components in the same diff.

## Rebasing Without Breaking the Stack

For day-to-day stack updates, use `gh stack rebase --upstack`. Switch to any branch in the stack using `gh stack up/down/switch`, add new commits, and `gh stack rebase --upstack` to reorganize the branch chain. Avoid `git commit --amend` in this workflow – gh-stack cannot track amended commits.

When you need to manually rebase the stack such as moving commits between branches in the stack, check out the topmost branch and rebase from there. With `rebase.updateRefs` enabled, Git updates every intermediate branch ref as it replays commits down the chain. Starting from a middle branch leaves the branches above it with stale refs.

```gitconfig
# ~/.gitconfig or repo .gitconfig
[rebase]
    updateRefs = true
```

```bash
gh stack top # top of the stack
git rebase -i develop
```

Prefer `gh stack rebase --upstack` for the common case. Reserve manual `git rebase` from the top for when you need to move commits between branches in the stack.

## The JSON Sync Problem

gh-stack records branch metadata in `.git/gh-stack`. When you squash or amend commits, or rebase from a middle layer, the SHA that gh-stack recorded no longer matches the branch’s actual HEAD. The JSON goes stale and breaks most features of `gh-stack`

The fix is to sync the JSON with the current state of your branches. Doing this manually means running `git log --oneline` for each branch, reading the current SHAs, and editing the JSON to match. Not difficult, but tedious – especially across a deep stack.

An AI assistant handles this well. Give it access to the repository and ask:

> Read the current HEAD of each branch in my gh-stack and update `.git/gh-stack` so each entry's recorded SHA matches.

## Putting It Together

Stacked PRs reduce review friction. gh-stack makes stacking practical without requiring GitHub-side configuration. The four habits that make it work:

1. One worktree per stack. Isolation by directory, not branch.
2. Agent-planned stacks. Focused units make PRs reviewable.
3. `gh stack rebase --upstack` for routine updates. Manual `git rebase` from the top when moving commits between branches in the stack.
4. AI-assisted JSON sync. Fast recovery after a squash or amend.