---
date: '2021-02-09T20:08:23+0800'
tags:
  - ssh
  - windows
  - yubikey
---

# SSH Authentication Using a YubiKey on Windows And the OpenSSH Client

As mentioned in [[§ Yubico for Windows]], I used PuTTY/Plink instead of the OpenSSH client together with YubiKey because the OpenSSH Client does not support the socket file created by GnuPG.

Plink does not work well in Windows Terminal. The Visual Studio Code [SSH Remote](https://code.visualstudio.com/docs/remote/ssh-tutorial) does not support Plink as well, because it will pass some command line arguments that are not supported by Plink.

So I decide to switch back to the OpenSSH client. Fortunately, the utility [wsl-ssh-pageant](https://github.com/benpye/wsl-ssh-pageant) can create a tunnel between a Windows pipe and the pageant socket, and the OpenSSH client can use the Windows pipe as `SSH_AUTH_SOCK`. This article is a tutorial to set up wsl-ssh-pageant.

<!--more-->

## Enable PuTTY Support

First edit `gpg-agent.conf` in folder `$(scoop prefix gpg)\home\`, enable PuTTY support

```
enable-putty-support
```

Restart gpg agent to reload the config file.

```
gpg-connect-agent killagent /bye
```

## Install OpenSSH Client

> This section is copied from [Installation of OpenSSH For Windows Server | Microsoft Docs](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse)

To install OpenSSH, start Settings then go to Apps > Apps and Features > Manage Optional Features. Or install it using PowerShell:

```
Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'

# This should return the following output:

Name  : OpenSSH.Client~~~~0.0.1.0
State : NotPresent
Name  : OpenSSH.Server~~~~0.0.1.0
State : NotPresent
```

Then, install the client feature:

```
# Install the OpenSSH Client
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

# It should return the following output:

Path          :
Online        : True
RestartNeeded : False
```

## Set Up wsl-ssh-pageant

Install [wsl-ssh-pageant](https://github.com/benpye/wsl-ssh-pageant) by downloading the binary from the GitHub release or using scoop

```
scoop install wsl-ssh-pageant
```

Create a cmd file `winssh-agent.cmd`

```batch
wsl-ssh-pageant.exe --systray --winssh ssh-pageant
PAUSE
```

Double-clicking this file will start the tunnel.

Add the environment variable to tell OpenSSH client to use the pipe created by `wsl-ssh-pageant`.

```powershell
[Environment]::SetEnvironmentVariable('SSH_AUTH_SOCK', '\\.\pipe\ssh-pageant', 'User')
```

The environment variable is only effective in new windows, so start a new terminal window to try that the tunnel works.

First, start the gpg agent and check that the card reader works:

```
gpg --card-status
```

Now try to authenticate SSH, for example, to GitHub

```
ssh git@github.com
```

## Auto Start wsl-ssh-pageant

Create a shortcut in Windows Start Menu to auto-start wsl-ssh-pageant on login and allow launch it by searching in the start menu by pressing the Windows key.

```powershell
# Change the path to the cmd file.
$SSHAgentLocation = "X:\Path\to\winssh-agent.cmd"
$SSHAgentShortcut = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\SSH Agent.lnk"

$WScriptShell = New-Object -ComObject WScript.Shell
$Shortcut = $WScriptShell.CreateShortcut($SSHAgentShortcut)
$Shortcut.TargetPath = $SSHAgentLocation
$Shortcut.WindowStyle = 7
$Shortcut.Save()
mkdir -Fo "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\SSH Agent"
cp -Fo "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\SSH Agent.lnk" "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\SSH Agent\SSH Agent.lnk"
```