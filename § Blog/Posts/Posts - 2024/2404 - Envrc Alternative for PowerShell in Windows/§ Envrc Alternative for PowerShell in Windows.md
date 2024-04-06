---
date: 2024-04-06T08:55:34+0800
draft: false
aliases:
  - Envrc Alternative for PowerShell in Windows
---

# Envrc Alternative for PowerShell in Windows

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2024-04-06]]
**URL**:: [blog.iany.me](https://blog.iany.me/2024/04/envrc-alternative-for-powershell-in-windows/)
**Reference**:: [[Envrc Alternative for Windows]]

This post introduces a solution for automatically setting up and tearing down shell environments for PowerShell in Windows. It is proposed as a potential alternative to the bash-based tool [direnv](https://github.com/direnv/direnv), which, while effective at loading `.envrc` files in the current or nearest ancestor directory, has limited compatibility with PowerShell in Windows.

<!--more-->
## .envrc.ps1

The basic idea is creating a file `.envrc.ps1` with two entries: setup and teardown. The setup entry is responsible for setting up the environment up entering the directory, and the teardown entry is used when leaving it.

PowerShell allows code to be executed from a file using the dot command. This means that the entire file can be used as the setup entry. For the teardown entry, a function can be defined within the same file, and I use the function name `down`.

The layout of the file `.envrc.ps1` looks like:

```powershell
# setup
$env:GH_TOKEN = "secret"

# teardown
function global:down {
    $env:GH_TOKEN = ""
}
```

The `global:` scope before the function name is necessary when this file is loaded in the hook, as I will do later.

The corresponding commands for setup and teardown entries:

- Setup: `. .envrc.ps1`
- Teardown: `down`

## Hook

To hook the setup and teardown entries, I reference [this example](https://github.com/PowerShell/PowerShell/issues/14484#issuecomment-1731647083). 

```powershell
using namespace System;
using namespace System.Management.Automation;

$hook = [EventHandler[LocationChangedEventArgs]] {
  param([object] $source, [LocationChangedEventArgs] $eventArgs)
  end {
    # 1. `down` for $eventArgs.OldPath
    # 2. `. .envrc.ps1` for $eventArgs.NewPath
  }
};
$currentAction = $ExecutionContext.SessionState.InvokeCommand.LocationChangedAction;
if ($currentAction) {
  $ExecutionContext.SessionState.InvokeCommand.LocationChangedAction = [Delegate]::Combine($currentAction, $hook);
} else {
  $ExecutionContext.SessionState.InvokeCommand.LocationChangedAction = $hook;
};
```

To run the code snippet, PowerShell 7 or later is required. You can install it from the [repository](https://github.com/PowerShell/PowerShell).

Here is the algorithm for identifying setup and teardown entries:

1. Find the nearest `.envrc.ps1` for the old path.
2. Find the nearest `.envrc.ps1` for the new path.
3. If the two paths are the same, skip the next step.
4. If they differ, invoke the `down` function and remove it if it exists. Then, if found, load the `.envrc.ps1` file for the new path.

The full code example to be added into PowerShell `$PROFILE` file.

```powershell
using namespace System;
using namespace System.Management.Automation;

# existing PowerShell profile contents

# skip when version is less than 7
if ($PSVersionTable.PSVersion.Major -lt 7) {
  return
}

# find the .envrc.ps1 in the currenct directory or the nearest ancestor directory.
function Find-NearestEnvrc {
  param (
    [Parameter(Mandatory=$true)]
    [string]$StartDir
  )

  $currentDir = Resolve-Path $StartDir
  while ($currentDir -ne "") {
      $envrcPath = Join-Path $currentDir ".envrc.ps1"
      if (Test-Path $envrcPath) {
          return $envrcPath
      }
      $currentDir = Split-Path $currentDir -Parent
  }

  return ""
}

# hook the setup and teardown entries
$hook = [EventHandler[LocationChangedEventArgs]] {
  param([object] $source, [LocationChangedEventArgs] $eventArgs)
  end {
    $oldEnvrc = Find-NearestEnvrc $eventArgs.OldPath
    $newEnvrc = Find-NearestEnvrc $eventArgs.NewPath
    if ($oldEnvrc -ne $newEnvrc) {
      Get-Command down -ErrorAction SilentlyContinu
      if (Get-Command down -ErrorAction SilentlyContinu) {
        down
        Remove-Item Function:down
      }
      if ($newEnvrc -ne "") {
        . $newEnvrc
      }
    }
  }
};
$currentAction = $ExecutionContext.SessionState.InvokeCommand.LocationChangedAction;
if ($currentAction) {
  $ExecutionContext.SessionState.InvokeCommand.LocationChangedAction = [Delegate]::Combine($currentAction, $hook);
} else {
  $ExecutionContext.SessionState.InvokeCommand.LocationChangedAction = $hook;
};
```

## Example Usage

```powershell
# setup
# set environment variable
$env:GH_TOKEN = "secret"
# load python virtual env
. .venv\Scripts\Activate.ps1
# add a helper function
function global:build {
    cargo build
}

# teardown
function global:down {
    # unset environment variable
    $env:GH_TOKEN = ""
    # unload python virtual env
    deactivate
    # remove the helper function
    Remove-Item Function:build
}
```