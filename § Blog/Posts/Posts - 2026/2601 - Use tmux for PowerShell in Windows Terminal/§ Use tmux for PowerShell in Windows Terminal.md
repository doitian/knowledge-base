---
date: '2026-01-29T23:30:42+0800'
draft: false
aliases: ["Use tmux for PowerShell in Windows Terminal"]
tags:
  - tmux
  - powershell
  - wsl
  - windows-terminal
description: "Run tmux from WSL in Windows Terminal with PowerShell as the default shell."
---

# Use tmux for PowerShell in Windows Terminal

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2026-01-29]]
**URL**:: [blog.iany.me](https://blog.iany.me/2026/01/use-tmux-for-powershell-sessions-in-windows-terminal/)

You can get tmux session persistence and multiplexing in Windows Terminal by running tmux inside WSL and setting the default shell to PowerShell. New panes and windows will then start `pwsh.exe` instead of a Linux shell. Here’s a minimal setup using small wrappers and the `tmux -C attach` trick to configure new sessions.

<!--more-->

## Why tmux under WSL with PowerShell?

Since tmux does not run natively on Windows, the standard approach is to use it through WSL. However, if you launch `wsl tmux` from Windows Terminal, all panes will default to your WSL shell. When working in a Windows directory, I prefer to use native PowerShell within the Windows environment.

To ensure every tmux pane runs PowerShell, configure tmux to use `pwsh.exe` as its default command. When you launch `pwsh.exe` from WSL within a Windows directory, it brings us back to the Windows environment.

## Wrappers so you can call tmux from PowerShell

Put these in a directory on your `PATH` (e.g. `~/Documents/PowerShell/bin`).

**PowerShell** — `tmux.ps1`:

```powershell
wsl tmux $args
```

**Cmd** — `tmux.cmd`:

```batch
@echo off
wsl tmux %*
```

From PowerShell or Cmd you can then run `tmux new`, `tmux attach`, etc., and they all go to WSL’s tmux.

## Creating PowerShell Sessions

The next piece is a script that creates a new session whose default command is `pwsh.exe`, or attaches if that session already exists. Example usage: `tmux-pwsh dev` or `tmux-pwsh work`.

The script sets the default command only for sessions it creates; it does not affect sessions started with a standard `tmux new-session`.

**`tmux-pwsh.ps1`**:

```powershell
param(
    [Parameter(Mandatory=$true)]
    [string]$SessionName
)

$pwshCommand = "exec pwsh.exe -nologo"

# Check if session exists using exact name match
wsl tmux has-session -t "\=$SessionName" 2>$null

if ($LASTEXITCODE -ne 0) {
    wsl tmux new-session -d -s $SessionName $pwshCommand
    echo "set-option default-command `"$pwshCommand`"" | `
        wsl tmux -C attach -t "\=$SessionName" >$null
}
wsl tmux attach -t "\=$SessionName"
```

Note:

1. The `=` prefix does an exact session name match and must be escaped when sending the command from PowerShell to WSL.
2. The new session specifies command `pwsh.exe` via the command argument.
3. Running `wsl tmux set-option` immediately after creating the session does not work because there's a brief window where the session is not available for setting options. Instead, sending `set-option` via `tmux -C attach` reliably applies the setting.

After this, splitting panes and creating new windows in that session will all start `pwsh.exe -nologo` in Windows Terminal.

## Summary

- Use WSL for tmux and PowerShell as the default command by setting tmux’s default command to `exec pwsh.exe -nologo`.
- **`tmux.ps1`** / **`tmux.cmd`** — thin wrappers so `tmux` from Windows means `wsl tmux`.
- **`tmux-pwsh.ps1 <name>`** — create (or attach to) a named session that uses PowerShell as the default command.

Once these are on your `PATH`, run e.g. `tmux-pwsh dev` from Windows Terminal to get a tmux session where every pane is PowerShell.