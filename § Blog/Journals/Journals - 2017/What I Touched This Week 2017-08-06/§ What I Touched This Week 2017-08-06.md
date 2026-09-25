---
date: 2017-08-06
description: My weekly review report.
series:
  - What I Touched
---

# What I Touched This Week 2017-08-06


## Programming

- [Source Directories Not Being Created In New Project – IDEs Support (IntelliJ Platform) | JetBrains](https://intellij-support.jetbrains.com/hc/en-us/community/posts/206806425-Source-Directories-Not-Being-Created-In-New-Project)

    Check the option, otherwise the directories must be created manually before creating Java/Kotlin new files using context menu.

- [PostgreSQL's Powerful New Join Type: LATERAL - Heap Blog](https://blog.heapanalytics.com/postgresqls-powerful-new-join-type-lateral/)

    `LATERAL` scopes sub SELECT with columns in preceding FROM items. It is useful to query completed associative information in one SQL.

- [Auto raise Python Tkinter main window](https://stackoverflow.com/a/37235492/667158)

- [Qt API设计原则 (译) | 酷 壳 - CoolShell](http://coolshell.cn/articles/18024.html)

- [debian apt-get update：public key 错误修复 - NILYANG](https://web.archive.org/web/20151022045219/https://my.oschina.net/lxrm/blog/466837)

    ```
    apt-get install debian-keyring debian-archive-keyring
    apt-get update
    ```

- Update using columns in joined table:
    - [PostgreSQL](http://www.postgresqltutorial.com/postgresql-update-join/)

        ```
        UPDATE A
        SET A.c1 = expresion
        FROM B
        WHERE A.c2 = B.c2;
        ```

    - [MySQL](http://www.mysqltutorial.org/mysql-update-join/)

        ```
        UPDATE T1, T2,
        [INNER JOIN | LEFT JOIN] T1 ON T1.C1 = T2. C1
        SET T1.C2 = T2.C2,
            T2.C3 = expr
        WHERE condition
        ```

<!--more-->

## Design

- [Sketch App Awesomeness 👌 – Design + Sketch – Medium](https://medium.com/sketch-app-sources/sketch-app-awesomeness-d6db04bf9ccb)

    Sketch tips.

- [weixin/WeSketch: A set of plugins for Sketch include drawing links & marks, UI Kit & Color sync, font & text replacing.](https://github.com/weixin/WeSketch)

    微信团队 Sketch 插件集

## Misc

- [The Stanley Parable：一场反设计与荒谬哲学的狂欢 - 知乎专栏](https://zhuanlan.zhihu.com/p/24265418)

- [A safe and accurate .gitignore for Unity3D (Unity5 onwards) | T-machine.org](https://web.archive.org/web/20171214032324/http://t-machine.org/index.php/2017/08/03/a-safe-and-accurate-gitignore-for-unity3d-unity5-onwards/)

- [Powershell Cmdlets That'll Improve Your Windows Admin Skills](http://www.makeuseof.com/tag/powershell-cmdlets-windows-admin/)

- [入门智能家居，从米家到HomeKit （一） - 少数派](https://sspai.com/post/39851)

    用树莓派适配智能家居系列文章

- [免费全平台的文件分享利器：SendAnywhere - 少数派](https://sspai.com/post/40047)
