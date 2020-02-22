---
date: 2016-11-13
description: My weekly review report.
series:
- What I Touched

---

# What I Touched This Week 2016-11-13


This week I continue work on log system. I wrote a tool to sync Gitlab Issues with a Excel file.

<!--more-->

## Logging System

How to use syslog in [skynet][1]:

- [use syslog instead of logger · jintiao/some-mmorpg@cf7ed70 · GitHub][2]. This is a merge request that using syslog in a real skynet project.
* [lsyslog][3] is a Lua library using syslog C API.

## Sync GUI Tool
-  [JavaFX 8 Tutorial - Part 1: Scene Builder | code.makery.ch][4]
- Java POI
    * [Insert and read hyper link in Excel using Java POI – Ian Yang – Medium][5]
    * POI provides API to list all images using  `Workbook.getAllPictures()`, but it has no image position information nor any caption, name information. 
* [Gitlab Upload API][6] requires multipart to upload file
    * [Upload files from Java client to a HTTP server][7]

### Misc

- [落格输入法 - 专业双拼][8]  强烈推荐的一个 iOS 上的双拼输入法。贴近原生不需要完全访问权限，而且支持小鹤形码。不过因为 macOS 上没有让人满意的小鹤双形的方案，还是用回了五笔。 [清歌][9] 五笔输入法在 macOS 和 iOS 上都很好用。
* [利用 Nginx 的 ngx\_http\_image\_filter\_module 做实时的图片缩略图 · Ruby China][10]
* [What’s Coming in Go 1.8 | tylerchr][11]. Library [plugin][12] is useful to develop plugin based solution.

[1]:    https://github.com/cloudwu/skynet
[2]:    https://github.com/jintiao/some-mmorpg/commit/cf7ed705fc78caacf529e3ecd825ac82af0a3d7e
[3]:    https://gitlab.com/lsyslog/lsyslog/blob/master/lsyslog.c
[4]:    http://code.makery.ch/library/javafx-8-tutorial/part1/
[5]:    https://medium.com/@doitian/insert-and-read-hyper-link-in-excel-using-java-poi-9713d05642a#.pvzlotp7x
[6]:    https://docs.gitlab.com/ce/api/projects.html#upload-a-file
[7]:    http://stackoverflow.com/a/2469587/667158
[8]:    https://im.logcg.com
[9]:    https://qingg.im
[10]:   https://ruby-china.org/topics/31498
[11]:   https://blog.tylerchr.com/golang-18-whats-coming/
[12]:   https://tip.golang.org/pkg/plugin/

