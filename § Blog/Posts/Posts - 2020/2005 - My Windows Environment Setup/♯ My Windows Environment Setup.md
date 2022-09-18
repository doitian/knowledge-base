---
date: '2020-05-03T22:03:22+0800'
---

# My Windows Environment Setup

#windows

I have only one Windows device, the Surface Go. I work on it occasionally, especially on short trips. I prefer Surface Go because of handwriting. I have a simple setup to meet my work requirements.

<!--more-->

I spend the most time on a computer in three apps: terminal, text editor and web browser. I use Windows Terminal, Visual Studio Code and Chrome in Windows.

I use [ColorTool](https://github.com/microsoft/terminal/tree/master/src/tools/ColorTool) to convert my favorite theme [PaperColor](https://github.com/aseom/dotfiles/blob/master/osx/iterm2/papercolor-light.itermcolors) into Windows Terminal schema. [This](https://gist.github.com/doitian/4677ce2da2eca2eccbb1637ef804bed1) is my full Windows Terminal config file.

Since I don't do heavy development locally, I use PowerShell as default in the Windows Terminal. The command `echo $profile` will print the PowerShell config file path. The essential PowerShell config is enabling the Emacs style keybinding (full version [here](https://gist.github.com/doitian/db79d2dbfaa24093534c7411b0a926bd)).

```
Set-PSReadLineOption -EditMode emacs
```

[Scoop](https://scoop.sh/) is very handy to install essential command line utilities, for example:

```
scoop install mingit ripgrep
```

I use the OpenSSH Client component in Windows, which can be enabled in "Settings / Apps / Manage optional features". I used to set an SSH passphrase, but the ssh agent service is disabled. It can be enabled in PowerShell ran as admin:

```
# Run once as admin
Get-Service ssh-agent | Set-Service -StartupType manual
```

I have set the startup type to manual, so if I want to load the key, I have to start the service first:

```
Start-Service ssh-agent
ssh-add
```

However, the git installed by scoop uses its own bundled ssh client by default. It is easy to fix it by setting an environment variable `GIT_SSH`.

```
# Run once as logged in user
$SSHPath = (Get-Command -Name 'ssh.exe').Source
[Environment]::SetEnvironmentVariable('GIT_SSH', $SSHPath, 'User')
```

Restart Windows Terminal and now git will use the key in ssh agent.

Git has the same issue with GPG. Use `git config` to tell where the GPG program is:

```
git config --global gpg.program (Get-Command -Name 'gpg.exe').Source
```

Following is a list of other apps I used in Windows:

* XMind: Mindmap tool.
* Drawboard PDF: PDF reading and annotation.
* Leonardo: an infinite canvas painting app.
* Nebo: Handwriting notebook.
* Clash for Windows
* OneDrive and Google Keep for quickly synchronize data with other devices.

## Linked mentions

%%+BEGIN: #dataviewx%%
```dataviewx
LIST WITHOUT ID "(Backlinks:: [[" + file.name + "]])"
FROM [[]] and "output"
WHERE !contains(Backlinks, [[]])
SORT file.name
```

- (Backlinks:: [[♯ Vim Setup for Windows]])
- (Backlinks:: [[♯ What I Touched This Week 2020-05-10]])
- (Backlinks:: [[♯ Windows]])
%%+END%%