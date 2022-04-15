---
date: 2020-06-21
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2020-06-21

I'm recently working in Windows, so I take many notes about setting up the Windows environment.

* [[♯ Minimize any window into system tray in Windows]]
* How to open site pinned to taskbar in its own window in Edge?

    1. Open `edge://apps`
    2. Right click the app and uncheck "Open in full browser"

* [Answer: How to access the system tray using the keyboard?](https://superuser.com/a/105828/86193)

    Press <kbd>Win+B</kbd> to activate tray, and use <kbd>Shift+F10</kbd> to show context menu.

<!--more-->

## More windows tips

### Configuration

* [GitHub - Disassembler0/Win10-Initial-Setup-Script: PowerShell script for automation of routine tasks done after fresh installations of Windows 10 / Server 2016 / Server 2019](https://github.com/Disassembler0/Win10-Initial-Setup-Script)

    These scripts are verify useful to keep only minimal feature set. I personally has disabled following presets.

    * `HideQuickAccess` hides quick access in explorer sidebar. I uses quick access to bookmark frequently access folders. 
    * `DisableActionCenter` disables the notifications in the right drawer. Notifications sometimes are helpful. 
    * `ShowTrayIcons` will always show all tray icons. I prefer selecting the icons to show manually.

### Look and feel

* The Chinese characters are ugly in Telegram for Windows when using English locale. A simple fixing is set system region to Chinese and Telegram will choose the right Chinese font. If it is not acceptable to change the region, an alternative solution is using [FontMod](https://iamcristye.github.io/Font/). When I test it, I have to [replace DAOpenSansRegular and DAVazirRegular](https://gist.github.com/70a1f32096ead06544804e6e7ca947fa).

* [how to scale krita UI ?](https://forum.kde.org/viewtopic.php?f=139&t=151602)

    Uncheck `Settings/Configure Krita/General/Window/Enable HiDPI support` to rely on system scale setting.

### Proxy

* [Using Scoop behind a proxy · lukesampson/scoop Wiki](https://github.com/lukesampson/scoop/wiki/Using-Scoop-behind-a-proxy)

    ```
    scoop config proxy [username:password@]host:port
    ```

* [Web authentication broker - UWP applications | Microsoft Docs](https://docs.microsoft.com/en-us/windows/uwp/security/web-authentication-broker)

    Some UWP apps depend on `AuthHost` to connect services like Google. Nebo is an example. So it is not enough to add Nebo to the loopback exempt list, the AuthHost must be in the list as well to ensure Nebo using the system proxy.

    This article has listed the following commands, where I have modified a bit to make them work in PowerShell

    ```
    CheckNetIsolation.exe LoopbackExempt -a "-n=microsoft.windows.authhost.a.p_8wekyb3d8bbwe"
    CheckNetIsolation.exe LoopbackExempt -a "-n=microsoft.windows.authhost.sso.p_8wekyb3d8bbwe"
    CheckNetIsolation.exe LoopbackExempt -a "-n=microsoft.windows.authhost.sso.c_8wekyb3d8bbwe"
    ```

    But I failed using these commands. Instead I find the SID from registry `HKEY_CURRENT_USER\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Mappings`. Search `AuthHost` inside it, and the directory name is the SID. The following command works for me

    ```
    CheckNetIsolation.exe loopbackexempt -a "-p=S-1-15-2-2750798217-1343590035-1234819260-1030354384-3318145141-3720257911-3461195215"
    ```

### Productivity tips

* [Windows 10 will make screenshots easier with new snipping tool - TechSpot](https://www.techspot.com/news/74469-windows-10-make-screenshots-easier-new-snipping-tool.html#:~:text=Using%20the%20alt%2Dtab%20shortcut,and%20automatically%20copied%20to%20clipboard.)

    <kbd>WIN + Shift + S</kbd>

### Programming Environment

* [Git - gitattributes Documentation](https://git-scm.com/docs/gitattributes)

    The exported registry entries are encoded using `UTF-16LE-BOM`. Git recognizes them as binary file. Add the following line in `.gitattributes`

    ```
    *.reg text working-tree-encoding=UTF-16LE-BOM eol=CRLF
    ```

    Then renormalize existing files:

    ```
    git add --renormalize .
    ```

    Now it is able to diff the registry exported files. More details can be found in this [commit](https://github.com/git/git/commit/aab2a1ae48ff65781a5379a01a4abb4f75e5641d)

* [A script to simplify WSL installation via LxRunOffline](https://gist.github.com/doitian/d89bf7b67067c1f4dcbeef066e2a4639)

* [Use the PowerShell Registry Provider to Simplify Registry Access](https://devblogs.microsoft.com/scripting/use-the-powershell-registry-provider-to-simplify-registry-access/)

    List existing mounted registry drives:

    ```
    Get-PSDrive -PSProvider registry | select name, root
    ```

    Mount new roots as drives:

    ```
    New-PSDrive -PSProvider registry -Root HKEY_CLASSES_ROOT -Name HKCR
    ```

* [How to update to PowerShell 7.0 on Windows 10](https://www.addictivetips.com/windows-tips/update-to-powershell-7-0-on-windows-10/)

    I install PowerShell 7.0 and use it as the default shell in Windows Terminal because it supports `cd -`

    ```
    iex "& { $(irm https://aka.ms/install-powershell.ps1) } -UseMSI"
    ```

* [How to stop a PowerShell script on the first error?](http://stackoverflow.com/questions/9948517/how-to-stop-a-powershell-script-on-the-first-error)

    ```
    $ErrorActionPreference = "Stop"
    ```

### GPG and SSH security

* [Share SSH and GPG keys with WSL](https://gist.github.com/doitian/078e6872a017754c28dd5ce0aa10375b)

    Since WSL2 can use Windows executable directly, the most straightforward way is just using the Windows counterparts.

* I finally have a comfortable setup to use YubiKey in Windows for gpg signing and ssh authentication. I'll write a post about it later. The following article helps me a lot: [How to use GPG with YubiKey (bonus: WSL)](https://codingnest.com/how-to-use-gpg-with-yubikey-wsl/).

### OpenSSH server

* [OpenSSH Server Configuration for Windows | Microsoft Docs](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_server_configuration)

    The default shell is cmd, the following command sets the default shell to PowerShell instead

    ```
    New-ItemProperty -Path "HKLM:\SOFTWARE\OpenSSH" -Name DefaultShell -Value "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -PropertyType String -Force
    ```

* [Visual Studio Code Switch Azure Account - Concurrency](https://www.concurrency.com/blog/may-2019/key-based-authentication-for-openssh-on-windows)

    Windows now has bundled OpenSSH server. But the key authorization requires strict restrictions on the authorized keys file permissions. It is not easy to make it right in Windows. I found the solution in this post. Pay attention that so administrator uses should use `C:\ProgramData\ssh\administrators_authorized_keys` save authorized public keys.

    ```
    $acl = Get-Acl C:\ProgramData\ssh\administrators_authorized_keys
    $acl.SetAccessRuleProtection($true, $false)
    $administratorsRule = New-Object system.security.accesscontrol.filesystemaccessrule("Administrators","FullControl","Allow")
    $systemRule = New-Object system.security.accesscontrol.filesystemaccessrule("SYSTEM","FullControl","Allow")
    $acl.SetAccessRule($administratorsRule)
    $acl.SetAccessRule($systemRule)
    $acl | Set-Acl
    ```

## Tech

┌ Productivity

* [How to Scroll Horizontally?](https://support.meistertask.com/hc/en-us/articles/360015778780-How-do-I-scroll-horizontally-in-a-project-)

    I have switched to Logitech Trackball recently and it has no horizontal scroll wheel.

    > You can use the keyboard shortcut <kbd>SHIFT</kbd>+Mouse scroll wheel to scroll horizontally.

* [Learning by Doing and Becoming a Developer at GoodNotes: Bret’s Story](https://medium.goodnotes.com/learning-by-doing-and-becoming-a-developer-at-goodnotes-brets-story-f4265f9a5e02?source=rss----b20d6679c6e9---4)

┌ Programming

* [❤️  How async should have been](https://sobolevn.me/2020/06/how-async-should-have-been)

    Functional way to build function for both sync and async

* [Configure Docker Hub mirror in /etc/containers/registries.conf](https://gist.github.com/2caf68f9a0afa9134b6aac13adee899a)
* [Podman 1.4.4: permission denied mounting volume without "--privileged" flag](https://github.com/containers/libpod/issues/3683)

    I have to pass `--security-opt label=disable` to mount local directory into the container.

* [An example to fix obsoleted gpg keys for apt repositories](https://github.com/mikefarah/yq/issues/217)

    ```
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
    ```

┌ Linux

* [How to generate locale in Slitaz](http://alanyih.blogspot.com/2008/08/slitaz-gcin.html)

    ```
    localedef -i ru_RU -c -f UTF-8 /usr/lib/locale/ru_RU.UTF-8
    ```

* I use Fedora cloud version in WSL2 as the main distribution. By default it lacks the locale packages.

    ```
    sudo dnf install glibc-langpack-en
    ```

* [Network modes in Parallels Desktop for Mac](http://kb.parallels.com/4948)

    The minimal distribution like Slitaz does not bundle the driver for vertio. The workaround is using the 
    `Intel (R) PRO/1000 MT` network adapter first, install `linux-kvm` in Slitaz and then switch to vertio.

* [Patch for Kernel 5.6 | Parallels Forums](https://forum.parallels.com/threads/patch-for-kernel-5-6.349625/)

    The Fedora 32 kernel is too new to install Parallels Gust Tools. Apply the patch in this thread first.

┌ Blockchain

* [干货 | 深入理解 OVM](https://mp.weixin.qq.com/s/mscFztCM89YlM-OjDsEyNQ)

## Non-tech

┌ Business

* [@dhh: Wow. I'm literally stunned. Apple just doubled down on their rejection of HEY's ability to provide bug fixes and new features…](https://twitter.com/dhh/status/1272968382329942017)

    About Apple Tax

┌ History

* [计算机历史 — Alan Kay (2/2) Normal Consider Harmful - Shuo Yang - Medium](https://medium.com/@yang140/computer-history-alan-kay-2-2-2706b3717d6b)

* [WD40 的正确用法——Switch 摇杆漂移自救指南](https://sspai.com/post/60946)

## Misc

* [Obsidian](https://obsidian.md), yet another non-linear note taking app.
* [Welcome! | minikube](https://minikube.sigs.k8s.io/docs/), a devops tool.
* [搭建家庭数据管理中心：QNAP NAS 应用指南](https://sspai.com/post/60856)
* [用开源免费的内网穿透工具 frp，实现远程桌面和文件传输](https://sspai.com/post/60852)
