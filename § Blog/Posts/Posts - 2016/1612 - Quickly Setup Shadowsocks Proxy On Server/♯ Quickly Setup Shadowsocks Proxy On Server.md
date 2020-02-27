---
date: '2016-12-10'
description: "Setup an HTTP and HTTPS proxy using Shadowsocks server via Shadowsocks client and polipo proxy."
title: Quickly Setup Shadowsocks Proxy on Server
---

# Quickly Setup Shadowsocks Proxy on Server

#gfw #systemAdmin

Sometimes I want to install some apps, but the site is blocked by GFW. I only have a Shadowsocks server, so I made some research how to setup up an HTTP and HTTPS proxy using Shadowsocks server.

The solution is using Shadowsocks client, which will establish a socket proxy, then convert the socket proxy to HTTP/HTTPS proxy using polipo.

<!--more-->

## Install Tools

Follow [Shadowsocks README][1] to install client:

```
apt-get install python-pip
pip install shadowsocks
```

Then follow [this document][2] to install polipo and disable the default service:

```
apt-get install polipo
service polipo stop
update-rc.d polipo disable
```

## Start Proxy

Start SOCKS proxy using Shadowsocks client:

```
sslocal -s SERVER_IP -p SERVER_PORT  -m AUTH_METHOD -k PASSWORD -l SOCKS_PROXY_PORT
```

* `SERVER_IP`，`SERVER_PORT`, `AUTH_METHOD`, `PASSWORD` are used to connect Shadowsocks server, see sslocal manual.
* `SOCKS_PROXY_PORT` is the SOCKS proxy port, which will be used in polipo.

Start another shell and launch HTTP proxy

```
polipo proxyPort=HTTP_PROXY_PORT logFile=/tmp/polipo${UID}.log \
  socksParentProxy=localhost:SOCKS_PROXY_PORT
```

* `SOCKS_PROXY_PORT` is the SOCKS proxy port established by sslocal
* `HTTP_PROXY_PORT` is the HTTP proxy will be used later in environment variables.

## Use HTTP/HTTPS Proxy

Keep sslocal and polipo running, set environment variables to use the proxy in other shell sessions:

```
export http_proxy=127.0.0.1:HTTP_PROXY_PORT https_proxy=127.0.0.1:HTTP_PROXY_PORT
git fetch --all
```

Command sslocal should prints something like this:

```
2016-10-30 15:31:35 INFO     connecting gitlab.com:443 from 127.0.0.1:43709
```

Yes, gitlab.com access is unstable in China, it is blocked sometimes.

To disable the proxy:

```
unset http_proxy https_proxy
```

It is recommended to use tmux or screen, because multiple shell sessions are required to run sslocal, pipolo and execute commands.

---

The original [Chinese version](https://medium.com/@doitian/在服务器上快速使用-shadowsocks-搭建一个代理-94b7fbf7f712#.1gje4qqod) is posted on Medium.

[1]:	https://github.com/shadowsocks/shadowsocks/blob/master/README.md
[2]:	https://github.com/shadowsocks/shadowsocks/wiki/Convert-Shadowsocks-into-an-HTTP-proxy
