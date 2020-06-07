---
date: 2020-06-07
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2020-06-07

This week I have installed Fedora 32 on Surface Go. I also switched to use GPG as my private SSH key.

There are several major issues to use Linux on surface:

* The WIFI requires downloading the driver, see [Surface Go: First Impressions : SurfaceLinux](https://www.reddit.com/r/SurfaceLinux/comments/94hjxv/surface_go_first_impressions/).
* The camera does not work.
* The headphone jack generates noise.

<!--more-->

## Use a GPG key for SSH

* [Using YubiKey Neo as gpg smartcard for SSH authentication - stafwag Blog](https://stafwag.github.io/blog/blog/2015/06/16/using-yubikey-neo-as-gpg-smartcard-for-ssh-authentication/)

    This article helped me setting up the Yubico key in Fedora. [→ Wiki](ia-writer://open?path=/Locations/iCloud/§%20Tickler/Tickler-Y/Yubico%20(Fedora)/♯%20Yubico%20(Fedora).md)

* [gnupg-agent: gpg agent refusing ssh agent work - Debian Bug report logs](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=835394)

    I don't know what it does, but when I have trouble I will try to run this

    ```
    gpg-connect-agent updatestartuptty /bye
    ```

* [How to use a GPG key for SSH authentication | Linode](https://www.linode.com/docs/security/authentication/gpg-key-for-ssh-authentication/)

## Tech

* [unicodes.txt](https://gist.github.com/f80a5f885946e10f3b42cc1e0392192b)

    I create it from [allkeys.txt](http://www.unicode.org/Public/UCA/12.0.0/allkeys.txt) so that I can use grep, fzf to search the code points.

┌ Vim

* [tags - quickfix Menu Usage With :tselect and :vimgrep - Vi and Vim Stack Exchange](https://vi.stackexchange.com/questions/21758/quickfix-menu-usage-with-tselect-and-vimgrep)

    * :ltag

* [settings - VIM Disable Automatic Newline At End Of File - Stack Overflow](http://stackoverflow.com/questions/1050640/vim-disable-automatic-newline-at-end-of-file)

    ```
    :set binary noeol
    ```

┌ Programming

* [REPL Driven Design](http://blog.cleancoder.com/uncle-bob/2020/05/27/ReplDrivenDesign.html)

    > So I’ve learned my lesson. REPL driven development feels easier and faster than TDD; but it is not. Next time, it’s back to TDD for me.

* [A note on commit messages](https://bitcrowd.dev/a-note-on-commit-messages)

## Non-tech

* [少数派办公室改造大揭秘，健康与效率兼顾的环境长啥样？](https://sspai.com/post/60762)
* [我们如何获取信息，组织知识](https://mp.weixin.qq.com/s/0tLF_cTbLGgQr1_-kNPFXg)

┌ Design

* [设计师必备字体利器](https://www.hellofont.cn/home)
* [常做海报封面宣传图？试试这 16 款风格强烈的优秀字体](https://sspai.com/post/60768)

## Bookmarks

* [Canvas](https://canvas.apps.chrome), A sketch and handwriting web app .

┌ Tools that share and encrypt files

* [FiloSottile/age: A simple, modern and secure encryption tool with small explicit keys, no config options, and UNIX-style composability.](https://github.com/FiloSottile/age)
* [schollz/croc: Easily and securely send things from one computer to another](https://github.com/schollz/croc)
* [Firefox Send](https://send.firefox.com/)
