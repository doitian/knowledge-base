---
date: 2016-12-17
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2016-12-17


This week I was setting up monitoring system using Prometheus.

Some gotchas:

- Both prometheus and alertmanager accept command line flag `-web.external-url` to configure URL used to access the site and API. But if the external URL set in alertmanager contains path portion, alert manager will prepend the path to all web endpoints, which means prometheus should also add the path even access alertmanager through `localhost:9093`.

<!--more-->

## Monitoring

- [My Philosophy on Alerting][1] via Google Engineer.

## Game Programming

- [A Study Path for Game Programmer][2]. Books recommendations for game programmer.
- [cjson中的稀疏数组encode - bigcat133的专栏][3]。用 cjson 输出日志的话，建议打开 `encode_sparse_array`
 - [云风的 BLOG: 用分布式压缩贴图加快 Unity3D 的打包过程][4]

## Misc

- [Fabulous macOS Tips & Tricks][5]
- [Implementation Details for OmniFocus 2.14 Automation - OmniFocus / OmniFocus for iOS][6]. Both iOS and macOS version can import TaskPaper format now. In macOS, just paste into OmniFocus.
- Subscribed [Safari Books Online][7] and started reading 『_Mathematics for 3D Game Programming and Computer Graphics, Third Edition_』on it.
- [Iconfont-阿里巴巴矢量图标库][8]。很丰富，质量也不错的矢量图标库。

[1]:    https://docs.google.com/document/d/199PqyG3UsyXlwieHaqbGiWVa8eMWi8zzAn0YfcApr8Q/edit
[2]:    https://github.com/miloyip/game-programmer
[3]:    http://blog.csdn.net/bigcat133/article/details/46374357
[4]:    http://blog.codingnow.com/2016/12/unity3d_remote_pvrtextool.html
[5]:    https://blog.sindresorhus.com/macos-tips-tricks-13046cf377f8#.q1sqp8ig7
[6]:    https://discourse.omnigroup.com/t/implementation-details-for-omnifocus-2-14-automation/24179
[7]:    https://www.safaribooksonline.com
[8]:    http://www.iconfont.cn/plus
