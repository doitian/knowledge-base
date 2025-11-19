---
comment: true
date: '2017-04-09T20:03:10+08:00'
description: 开发服务端程序，nofile 是很重要的配置。它限制了一个进程最多能够打开的文件数量
katex: false
share: true
title: Linux nofile 限制
tags:
- linux
- performance
- system-admin
---

# Linux Nofile Limit

在上一次游戏测试中，因为用了新的机器，并且从 ansible 切换到了 salt stack，其中 `nofile` 相关的配置步骤漏掉了，结果所有进程的 `nofile` 限制是默认的 1024。结果就是当在线人数达到一定数据之后，出现大量 lua 找不到文件的错误，导致后来的玩家没法登录，已经在线的玩家也没法正常游戏。

开发服务端程序，`nofile` 是很重要的配置。它限制了一个进程最多能够打开的文件数量。对于高并发的服务，每个连接都会打开一些文件，尤其是使用像 Lua 这样的脚本语言，更是要打开大量的文件。

当前的限制可以使用 `ulimit  -a` 查看。

要修改也比较简单，以 Ubuntu 为例，最简单的就是修改 `/etc/security/limits.conf`，在该文件中添加下面内容即可，不需要重启，新创建的进程会使用新的配置。

    * hard nofile 1000000
    * soft nofile 1000000

<!--more-->

用来做服务器的机器最好默认都设置得高一些。并且自动化的在所有的新机器上应用。

如果是通过 upstart, supervisor 等工具来启动服务，也可以只改对应的启动器配置。

Supervisor 需要修改 `supervisord.conf`，在 `[supervisord]` 小节中设置  `minfds`，需要重启 Supervisor 本身。

    [supervisord]
    minfds = 1000000

Upstart 是 Ubuntu 之前使用的 init，可以在服务的配置文件里添加下面配置。需要重启服务才能生效。

    limit nofile 1000000 1000000

如果在 macOS 中需要做压力测试之类的，将下面文件保存成 `/Library/LaunchDaemons/limit.maxfiles.plist` 并重启。文件来自 Riak 的文档 [Open Files Limit][1]，里面有更详细的各个平台下的配置方法。

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
      <dict>
        <key>Label</key>
        <string>limit.maxfiles</string>
        <key>ProgramArguments</key>
        <array>
          <string>launchctl</string>
          <string>limit</string>
          <string>maxfiles</string>
          <string>200000</string>
          <string>200000</string>
        </array>
        <key>RunAtLoad</key>
        <true/>
        <key>ServiceIPC</key>
        <false/>
      </dict>
    </plist>

[1]: https://docs.riak.com/riak/kv/2.0.2/using/performance/open-files-limit/
