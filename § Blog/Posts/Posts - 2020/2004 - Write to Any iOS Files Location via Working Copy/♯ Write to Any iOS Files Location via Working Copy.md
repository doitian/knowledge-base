---
date: '2020-04-24T21:14:17+08:00'
description: "Write to Any iOS Files Location via Working Copy with its two features: Synced Directory and Write Repository File Shortcut"
feature: write-to-files-via-working-copy.png
---

# Write to Any iOS Files Location via Working Copy

#ios #automation

I use file system to manage my knowledge base. The [repository](https://github.com/doitian/knowledge-base/) has a well defined directory structure. I have a bunch of scripts to help me creating these directories on the laptop. But in iOS, I have to create them manually. Recently, I have found out a way to work around it via Working Copy.

<!--more-->

The trick uses two features of Working Copy:

* 2-way synchronized repository with any iOS Files location.
* The shortcut *Write Repository File*.

The shortcut allows writing file into any path in a repository, and the synchronized repository synchronizes changes back to the target iOS Files location.

![[write-to-files-via-working-copy.png|Write to Files via Working Copy]]

In the following I'll show how to create a shortcut which saves files into an iCloud folder and sorts them into sub-directories by date.

First create the target directory and set up the synchronized repository. I use `Desktop/Inbox`.

![[set-up-sync-repo-in-working-copy.jpg|Set Up Sync Repo in Working Copy]]

Then create the shortcut. It accepts the file from Share Sheet and saves it into the synchronized repository sorted by date. It is important to check the option "Create" in the *Write Repository File* step.

![[shortcut-save-files-by-date.jpg|Shortcut: Save Files by Date]]

Now give it a try. Share a text file using the new created action.

![[test-shortcut.jpg|Test Shortcut]]

And the file appears in the `Desktop/Inbox`.

![[file-sorted-into-inbox.jpg|File Sorted into Inbox]]

---

This solution is not perfect and has two major drawbacks:

* It duplicates the files.
* It requires opening Working Copy to synchronize files.

However, it also has a bonus. I can backup the directory by git now.
