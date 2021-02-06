---
date: '2020-07-11T16:38:25+0800'
---

# Yubico for Windows

#windows [[Yubico]]

This post records how I set up Yubico Key in Windows, so I’ll not delve into too much details. I have the model YubiKey 5 NFC. I frequently use 2 GPG keys stored in the key, one for encryption, another for SSH authentication.

The GPG encryption part is simple, GnuPG just works. Using the stored GPG key for SSH is a bit complex, because it requires collaboration between GnuPG and the SSH client. After experiment many different solutions, I decide to use the simplest one, using putty/plink as the SSH client and enabling thepageant support in GnuPG.

<!--more-->

## Windows

I use [scoop](https://scoop.sh) to manage apps in Windows. My configuration requires gpg and putty, where putty is in the extra buckets.

```
scoop bucket add extras
scoop install gpg putty
```

Tells git to use gpg and putty

```
git config --global gpg.program (Get-Command -Name 'gpg.exe').Source
$SSHPath = (Get-Command -Name 'plink.exe').Source
[Environment]::SetEnvironmentVariable('GIT_SSH', $SSHPath, 'User')
```

Edit `gpg-agent.conf` in folder `$(scoop prefix gpg)\home\`, enable putty support

```
enable-putty-support
```

By the way, the putty support means that gpg agent will also act as pageant, so there's no need and it is also forbidden to run pageant manually. If pageant is running, quit it first then restart gpg agent.

Since my GPG keys are already stored in the YubiKey, I just need to export the public keys from somewhere and import them into the Windows host.

Restart gpg agent to check whether the keys are recognized:

```
gpg-connect-agent killagent /bye
gpg --card-status
gpg -K
```

If `gpg --card-status` complains that it cannot find the key card, refer to [this article](https://support.yubico.com/support/solutions/articles/15000014892-troubleshooting-issues-with-gpg) to save `reader-port Yubico Yubi` in the file ``$(scoop prefix gpg)\home\scdaemon.conf` and try again.

## WSL

My solution to use the YubiKey in WSL is straightforward. Just use the Windows executables in WSL.

```
ln -snf "$(which plink.exe)" "$HOME/bin/ssh"
ln -snf "$(which pscp.exe)" "$HOME/bin/scp"
ln -snf "$(which gpg.exe)" "$HOME/bin/gpg"
git config --global core.sshCommand "$(which plink.exe)"
```
