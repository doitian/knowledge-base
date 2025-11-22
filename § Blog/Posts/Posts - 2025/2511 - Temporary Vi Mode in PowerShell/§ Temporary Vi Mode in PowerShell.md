---
date: 2025-11-22T23:17:05+0800
draft: false
aliases:
  - Temporary Vi Mode in PowerShell
tags:
  - powershell
  - vim
  - emacs
  - console
description: "Experience the best of both worlds in PowerShell: temporarily switch to Vi command mode with a keybinding while keeping Emacs as your default editing mode. Learn how to configure PSReadLine for seamless Vi/Emacs mode toggling."
---

# Temporary Vi Mode in PowerShell

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2025-11-22]]
**URL**:: [blog.iany.me](https://blog.iany.me/2025/11/temporary-vi-mode-in-powershell/)

I miss the feature in readline (Bash/Zsh) where `Ctrl+x, Ctrl+v` switches to Vi command mode temporarily. In that workflow, entering Insert mode switches back to Emacs mode. `PSReadLine` has a command `ViCommandMode`, but binding it directly in Emacs mode will report errors on every key input.

The solution requires handling the mode change event to toggle the global `EditMode` between `Emacs` and `Vi`. 

<!--more-->

When entering "Insert" mode (the default for Emacs users), we force the mode to `Emacs` and set up the trigger for the temporary Vi mode. When that trigger (`Ctrl+x, Ctrl+v`) is fired, we switch the edit mode to `Vi` and jump to command mode.

Here is the configuration for your `$PROFILE`:

```powershell
function OnViModeChange {
  if ($args[0] -eq 'Insert') {
    Set-PSReadLineOption -EditMode Emacs
    Set-PSReadlineKeyHandler -Chord "Ctrl+x,Ctrl+v" -ScriptBlock {
      Set-PSReadLineOption -EditMode Vi
      [Microsoft.PowerShell.PSConsoleReadLine]::ViCommandMode()
    }
    # Add other Emacs key bindings here.
    # Switching `EditMode` resets key bindings to their defaults.
    # Remember to reconfigure them.
    # Set-PSReadlineKeyHandler -Chord "Ctrl+w" -Function BackwardKillWord
  }
}
Set-PSReadLineOption -ViModeIndicator Script
Set-PSReadLineOption -ViModeChangeHandler $Function:OnViModeChange
Set-PSReadLineOption -EditMode Emacs
# Reuse the function to start Emacs mode
OnViModeChange Insert
```

Switching `EditMode` resets key bindings to their defaults. Remember to reconfigure them.