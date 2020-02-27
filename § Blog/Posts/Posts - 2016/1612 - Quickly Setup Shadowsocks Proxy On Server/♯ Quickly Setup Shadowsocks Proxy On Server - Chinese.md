---
date: '2016-12-10'
description: 使用 Shadowsocks 和 polipo 在服务器上搭建代理
title: 在服务器上快速使用 Shadowsocks 搭建一个代理
---

# Quickly Setup Shadowsocks Proxy On Server

#gfw #systemAdmin

在服务器上有时候需要安装一些软件，但是下载地址被 GFW 给墙了。手上只有 Shadowsocks 可以用，所以研究了下怎么在服务器上用起来。只需要用到 Shadowsocks 的命令行客户端启动一个 SOCKS 代理，然后用 polipo 转化成 HTTP 代理，就可以通过环境变量 `http_proxy` 和 `https_proxy` 在命令行中使用代理了。

<!--more-->

## 安装工具
首先按照 [Shadowsocks 文档](https://github.com/shadowsocks/shadowsocks/blob/master/README.md) 安装客户端：

```
apt-get install python-pip
pip install shadowsocks
```

然后参照 [这个文档](https://github.com/shadowsocks/shadowsocks/wiki/Convert-Shadowsocks-into-an-HTTP-proxy) 安装 polipo 并禁止默认的服务：

```
apt-get install polipo
service polipo stop
update-rc.d polipo disable
```

## 启动代理
使用命令行启动 SOCKS 代理：

```
sslocal -s SERVER_IP -p SERVER_PORT  -m AUTH_METHOD -k PASSWORD -l SOCKS_PROXY_PORT
```

* `SERVER_IP`，`SERVER_PORT`, `AUTH_METHOD`, `PASSWORD` 是用来连接 Shadowsocks 的服务器 IP，端口，加密算法和密码。
* `SOCKS_PROXY_PORT` 是 sslocal 启动的 SOCKS 代理的端口号，需要在 polipo 里用到。

另外开一个 shell 启动 HTTP 代理

```
polipo proxyPort=HTTP_PROXY_PORT logFile=/tmp/polipo${UID}.log socksParentProxy=localhost:SOCKS_PROXY_PORT
```

* `SOCKS_PROXY_PORT` 就是上面启动的 SOCKS 代理的端口号。
* `HTTP_PROXY_PORT` 是 polipo 启动的 HTTP 代理的端口号，需要在环境变量里使用。

## 使用代理
保持 sslocal 和 polipo 运行，在其它的 shell 里就可以通过环境变量来启用代理了：

```
export http_proxy=127.0.0.1:HTTP_PROXY_PORT https_proxy=127.0.0.1:HTTP_PROXY_PORT
git fetch --all
```

在 sslocal 的输出应该能看到通过代理的流量，像这样：

```
2016-10-30 15:31:35 INFO     connecting gitlab.com:443 from 127.0.0.1:43709
```

嗯，是的，这次是 gitlab.com 被墙了。

不需要代理的时候：

```
export http_proxy= https_proxy=
```

因为需要多个 shell 来运行 sslocal, pipolo 并执行命令，建议使用 tmux 或者 screen。
