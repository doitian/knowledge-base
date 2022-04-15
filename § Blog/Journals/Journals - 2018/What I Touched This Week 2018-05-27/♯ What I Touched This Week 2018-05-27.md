---
date: 2018-05-27
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2018-05-27


* [Convert `git diff` output to the format can be recognized by vim quickfix.](https://gist.github.com/doitian/4046a5d53233d8351c1bb981ae2d3b1d)

* Browser auto reload using `osascript` and `watchexec`

    * Save following snippet as executable bash script `reload-chrome`. It reload the active tab of Google Chrome.

            osascript -l JavaScript -e 'Application("Google Chrome").windows[0].activeTab.reload()'

    * Run the script above when files are changed
    
            watchexec -w app -w config -p reload-chrome

* [Devops Security Checklist | Sqreen](https://doitian.notion.site/The-DevOps-Security-Checklist-ed9b5125ff7945e3b3b4ffa9e6643131)

    Best practices to check security before release.

* [Be careful what you copy: Invisibly inserting usernames into text with Zero-Width Characters](https://medium.com/@umpox/be-careful-what-you-copy-invisibly-inserting-usernames-into-text-with-zero-width-characters-18b4e6f17b66)

<!--more-->

## Bookmarks

* [Docusaurus · Easy to Maintain Open Source Documentation Websites](https://docusaurus.io/)
* [Flutter - Beautiful native apps in record time](https://flutter.io/)

    Google crossplatform native mobile app development platform.

* [Cool Backgrounds](https://coolbackgrounds.io/)

    Cool backgrounds created by CSS

* [Royalty Free Music | Filmstro](https://filmstro.com/music)
* [BurntSushi/chan: Multi-producer, multi-consumer concurrent channel for Rust.](https://github.com/BurntSushi/chan)
* [djc/askama: Type-safe, compiled Jinja-like templates for Rust](https://github.com/djc/askama)
* [ambv/black: The uncompromising Python code formatter](https://github.com/ambv/black)
* [Wired Elements](https://wiredjs.com/)

    Hand-drawn UI elements, which can be used in mockup created using code.

* [improbable-eng/thanos at stackshare](https://github.com/improbable-eng/thanos?ref=stackshare)

    Prometheus monitoring integration for Golang.
