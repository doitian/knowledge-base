---
date: '2026-08-10T12:45:09+0800'
draft: false
aliases: ["My AI-Assisted Development Workflow"]
tags:
  - automation
  - git
  - productivity
  - programming
  - tool
description: "Plan into units, let AI stack branches with gh-stack, review the PRs yourself, then hand review comments back to the agent."
---

# My AI-Assisted Development Workflow

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2026-08-10]]
**URL**:: [blog.iany.me](https://blog.iany.me/2026/08/my-ai-assisted-development-workflow/)

AI agents write code fastest when the work is sliced small and a human stays on judgment. My workflow runs a four-step loop: plan the feature into units, hand the branch stack to the agent, review each PR myself, then let the agent address my comments.

<!--more-->

I wrote a separate guide on the branch-management mechanics: [[§ A Practical Guide to gh-stack for AI-Assisted Development]]. That post covers worktrees, rebase habits, and JSON sync. This post is the loop around that tool.

## 1. Plan and split into units

Start with a written plan, not "build the feature." The plan names the goal, records the product decisions already made, and breaks work into Implementation Units: U1, U2, U3, and so on.

Each unit is small enough to fit one agent session and one human review. Specific, not vague. "Design the data model for board columns" is a unit. "Do the backend" is not. Dependencies between units are explicit – U3 depends on U2 because it queries the schema U2 defines.

Before any code, I do a quick plan review across three axes: product (is this the right thing?), feasibility (can we build it this way?), and scope (are the units the right size?). Fixing a bad unit boundary in a markdown file takes a minute. Fixing it across five stacked PRs takes an afternoon.

When the plan turns out to be wrong mid-implementation, I stop and revise it before writing more code. The plan is the source of truth, not the branches.

## 2. Let AI manage branches with gh-stack

Once the units are stable, I give the agent one prompt to build the stack:

> Implement U1 and U2 from the plan. Use gh-stack to add a branch per unit. Include the Jira ticket number in branch names.

The agent creates branches, writes scoped commits, opens stacked PRs with each PR based on the unit below, and runs `gh stack rebase --upstack` when a lower layer changes. I do not hand-manage the branch chain day to day.

One worktree per stack, one branch per unit. The [[§ A Practical Guide to gh-stack for AI-Assisted Development|gh-stack guide]] has the full setup for worktrees, branch naming, and how to keep the JSON in sync.

## 3. Review the PR and leave comments

This step belongs to me.

I read each stacked PR as a focused slice. Small units mean the diff is narrow enough to actually read. I leave inline comments or a review summary – whatever makes the problem clear. I do not fix code during the review pass.

Good review comments say what is wrong, what I want instead, and which layer owns the change. Ambiguous comments waste the next agent session. The review is the quality gate; I treat it like one.

## 4. Let AI address the review comments

I hand the PR back with a prompt:

> Address review comments on PR #42. Stay on the matching stack branch. Add new commits; don't amend unless I ask.

The agent reads the threads, fixes issues on the correct layer, replies to comments, and resolves what it can. Anything that requires a product call comes back to me. After fixes on a lower layer, it rebases upstack.

Then I re-review or approve and merge bottom-up. One loop per unit. Repeat.

## Why this shape works

| Step | Owner |
| ---- | ----- |
| Plan and units | Human + agent |
| Branches and PRs | Agent + gh-stack |
| Review | Human |
| Address comments | Agent |

Agents do well with bounded units and explicit comment lists. They do worse at deciding where one unit ends and another begins, or at choosing between two product directions. The plan and the review are where those decisions happen – both belong to the human.

The loop: plan → stack → review → fix.
