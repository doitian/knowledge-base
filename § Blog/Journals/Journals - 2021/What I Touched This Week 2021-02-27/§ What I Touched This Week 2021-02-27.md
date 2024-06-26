---
date: 2021-02-27
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2021-02-27

I have read 2 books:

- Extreme Ownership, by Jocko Willink and Leif Babin.
- Ikigai: The Japanese Secret to a Long and Happy Life, by Hector Garcia and Francesc Miralles.

<!--more-->

┌ Extreme Ownership

**Reference**:: [[Shortform - Extreme Ownership by Jocko Willink (Highlights)]]

* A leader must take the responsibility of team failures.
* A leader must help the team to reach high standards.
* A leader has to admit her own mistakes.

┌ Ikigai

**Reference**:: [[Shortform - Ikigai by Héctor García and Francesc Miralles (Highlights)]]

Ikigai means having a life purpose.

* Finding your Ikigai
* Finding Flow

┌ GNU Parallel

**Reference**:: [[Seth Kenlon - Get More Done at the Linux Command Line With GNU Parallel (Highlights)]]

[GNU Parallel](https://opensource.com/article/18/5/gnu-parallel) is similar to `xargs` but runs commands in parallel.

┌ GitHub Actions Manual Trigger

**Reference**:: [[GitHub Authors - GitHub Actions Manual Triggers With Workflow_dispatch - GitHub Changelog (Highlights)]]

GitHub Actions can add [manual triggers](https://github.blog/changelog/2020-07-06-github-actions-manual-triggers-with-workflow_dispatch/). This [article](https://github.com/yihong0618/gitblog/issues/198) introduces the API to fire the trigger.

```bash
curl -H "Content-Type:application/json" \
  -H "Authorization: token $GITHUB_ACCESS_TOKEN" \
  -X POST -d '{"inputs": {}, "ref":"master"}' \
  "https://api.github.com/repos/$ORG/$REPO/actions/workflows/$ACTION_ID/dispatches"
```

┌ [Ask Doist: How Can I Stay Productive and Organized as a Student While Maintaining Work-Life Balance](https://blog.doist.com/ask-doist-student-productivity/)

- Focus on the hard things. Get out of the comfort zones.
- Combine school and relationships by studying together.
- Take care of your home on breaks.

┌ [Git - Switching Branches Without Touching the Working Tree](https://stackoverflow.com/questions/6070179/switching-branches-without-touching-the-working-tree)

**Reference**:: [[CB Bailey et al. - Git - Switching Branches Without Touching the Working Tree (Highlights)]]

```
git symbolic-ref HEAD refs/heads/debug-branch
git reset
```