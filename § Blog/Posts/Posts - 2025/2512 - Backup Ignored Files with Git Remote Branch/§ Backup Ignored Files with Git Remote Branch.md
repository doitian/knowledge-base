---
date: '2025-12-12T03:22:58+0800'
draft: false
aliases: ["Backup Ignored Files with Git Remote Branch"]
tags:
  - git
  - automation
  - backup
---

# Backup Ignored Files with Git Remote Branch

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2025-12-12]]
**URL**:: [blog.iany.me](https://blog.iany.me/2025/12/backup-ignored-files-with-git-remote-branch/)

When working with Git repositories, there are often files that need to be backed up but shouldn't be committed to the main branch. These might include local development settings, IDE configuration files, personal notes, or development scripts that are specific to your workflow. The challenge is finding a way to back up these ignored files without polluting the main repository history.

<!--more-->

## The Original Solution

My original approach was to use a separate repository to store backup files for all repositories and create symbolic links. This worked, but had several drawbacks:

- Backup files were disconnected from their source repositories, making it harder to track what belongs where
- Backing up new files required moving them to the backup repository and then creating symbolic links

## A Better Approach: Remote Branch

Instead of using a separate repository, we can use a remote branch within the same repository. This approach offers several advantages:

- Everything stays in one repository
- When you clone the repository, the backup branch comes with it
- Backup files are stored in a separate branch, keeping the main branch clean
- Full Git history for backup files, just like any other branch

## The Script

With AI assistance, I developed `git-store-file`, a tool for managing ignored files by storing them in a remote branch (default: `origin/_store`). This keeps backup files separate from your working branch without interfering with regular development. The script is available in both [Bash](https://github.com/doitian/dotfiles-public/blob/master/default/bin/git-store-file) and [PowerShell](https://github.com/doitian/dotfiles-windows/blob/master/bin/git-store-file.ps1) versions.

### Installation

Download the script and make it executable:

```bash
# Bash version
curl -o ~/bin/git-store-file https://raw.githubusercontent.com/doitian/dotfiles-public/master/default/bin/git-store-file
chmod +x ~/bin/git-store-file

# PowerShell version
# Download to a directory in your PATH
```

### Usage

The script has four main commands: `store`, `status`, `restore`, and `ls`.

#### Store Files

Store one or more files to the remote branch, including files that are ignored by Git:

```bash
# Store a single file
git-store-file config.local.json

# Store multiple files
git-store-file config.local.json secrets.env

# Use a custom branch name
git-store-file --branch backup config.local.json

# Use a custom remote
git-store-file --remote upstream config.local.json
```

When you run the store command, the script will:

1. Create a temporary Git index to avoid conflicts with your working directory
2. Load the target branch's current state into the temporary index
3. Add the specified files using `git add -f` to include ignored files
4. Create a commit with the changes
5. Display commit statistics and prompt for confirmation
6. Push the commit to the remote branch

#### Check Status

Check which files stored in the remote branch have been modified in your local working directory:

```bash
# Check status
git-store-file status

# Show diff for modified files
git-store-file status --diff
```

#### Restore Files

Restore files from the remote branch to your working directory:

```bash
# Restore a specific file
git-store-file restore config.local.json

# Restore all files from the branch
git-store-file restore
```

#### List Files

List all files stored in the remote branch:

```bash
git-store-file ls
```

### Options

- `-b, --branch BRANCH`: Specify the branch name (default: `_store`)
- `-r, --remote REMOTE`: Specify the remote name (default: `origin`)
- `-h, --help`: Show help message

### Examples

```bash
# Store local configuration
git-store-file .env.local

# Check what's changed
git-store-file status -d

# Restore after cloning
git-store-file restore .env.local

# List all backed up files
git-store-file ls
```

## How It Works

The script uses Git's low-level plumbing commands to manipulate the repository without affecting your working directory:

1. **Temporary Index**: Uses the `GIT_INDEX_FILE` environment variable to create a temporary index, completely isolated from your working directory
2. **Read Tree**: Loads the target branch's tree structure into the temporary index
3. **Force Add**: Uses `git add -f` to add files even if they're listed in `.gitignore`
4. **Commit Tree**: Creates a commit object directly using `git commit-tree`, bypassing the normal commit workflow
5. **Direct Push**: Pushes the commit hash directly to the remote branch reference

This low-level approach ensures that:

- Your working directory remains unchanged
- The main branch is never affected
- Ignored files can be stored without modifying `.gitignore`
- The backup branch maintains full Git history

## Conclusion

The `git-store-file` script solves the problem of backing up ignored files in a clean, Git-native way. By leveraging a remote branch, it keeps everything in one repository while maintaining clear separation between your main codebase and backup files. Whether you're managing local configurations, IDE settings, or personal development scripts, this tool provides a simple and reliable backup solution that integrates seamlessly with your existing Git workflow.
