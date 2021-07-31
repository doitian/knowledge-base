---
comment: true
date: 2017-11-18 00:43:54
description: ZFS 查看文件错误并修复
katex: false
share: true
title: ZFS 文件恢复
---

# ZFS File Restore

#system-admin

zfs 会在访问文件时记录下问题文件，也可用使用 `scrub` 来扫描文件，其中 `poolname` 是卷名。

```
zpool scrub poolname
```

问题文件可以通过 `status` 列出

```
zpool status -v
```

错误比较多的话，可以考虑通过镜像还原。

```
zfs rollback poolname/path@tag
```

少的话也可以手动恢复问题文件。

错误中不是 `/` 开头，而且带有 `@tag` 这样标签的是 ZFS 镜像。镜像本质是备份，备份出错了可能最简单的办法就是删除了，下面的命令用于删除镜像

```
zfs destroy poolname/path@tag
```

错误比较少，文件不重要可以删除，如果重要并且有备份可以从备份中恢复。不过被删除或者被覆盖的文件不会立即被释放，如果想请空 `zpool status -v` 中已删除文件的错误，可以执行 `zpool scrub poolname`，等几分钟再通过 `zpool scrub -s poolname` 停止。
