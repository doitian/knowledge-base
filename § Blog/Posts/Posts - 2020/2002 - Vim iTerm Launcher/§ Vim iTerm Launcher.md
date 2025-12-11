---
comment: true
date: 2020-02-08T16:48:30+08:00
description: I wrote two scripts to help launching Vim in a new iTerm window.
katex: false
share: true
title: Vim iTerm Launcher
tags:
  - automation
  - macos
---

# Vim iTerm Launcher

I prefer using Vim in a terminal. I can switch to the shell with <kbd>Ctrl-Z</kbd> and back with `fg`. However it is hard to integrate a terminal command with other GUI tools, such as editing a file in Vim from Finder.

In macOS, the default Terminal app and iTerm both supports automation. It's easy to write a script to open a new terminal window and run a command like "vim file" in it. But I want to close the window after Vim quits. A quick work around is running the following command:

    vim file; exit 0

Now the problem is that if I suspend Vim via <kbd>Ctrl-Z</kbd>, the terminal window is closed, because shell will continue to execute the next command when the process is suspended.

After research and reading [a StackOverflow answer](https://stackoverflow.com/a/16215525/667158), I wrote [two scripts](https://gist.github.com/doitian/0c8775e88ceed7bac44c4fb4287822d5) to launch Vim in iTerm. I also added features in `iterm-vim-wrapper` to edit clipboard and empty scratch file in temporary directory.

This is [an example](https://github.com/doitian/assets/raw/master/2020/Vim%20File%20Action.alfredworkflow) which uses the scripts to create File Action in Alfred.
