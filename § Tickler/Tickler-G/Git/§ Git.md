# Git

#command-line

## Tips

⚡ [Diff per word or character](https://makandracards.com/makandra/28067-git-diff-per-word-or-character)

**Reference**:: [[Git Diff per word or character - makandra dev (Highlights)]]

```
git diff --color-words
git diff --color-words=.
```

⚡ [Synchronize Between Clones](https://stackoverflow.com/a/28381311)

**Reference**:: [[How to push to a non-bare Git repository - Stack Overflow (Highlights)]]

```
git config --local receive.denyCurrentBranch updateInstead
```

It also requires the remote clone working directory is clean.

⚡ [Display Unicode Path](https://stackoverflow.com/a/22828826/667158)

```
git config --global core.quotepath off
```
