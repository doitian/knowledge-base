---
comment: true
date: '2017-08-23T23:11:35+08:00'
description: 使用 Nginx stream 代理作 UDP 负载均衡
katex: false
share: true
title: 使用 Nginx 作 UDP 负载均衡
---

# 使用 Nginx 作 UDP 负载均衡

#nginx

最近把 Graylog 升级到集群。因为使用了 syslog UDP 作为输入，所以需要做个 UDP 的负载均衡。因为机器在阿里云，所以首先是创建了个阿里云内网的 UDP 负载均衡，但是发现负载不平均，而且也没办法关闭检测连接的心跳包。而常见的 HTTP 负载均衡工具 HAProxy 不支持 UDP。最后发现 Nginx 是可以实现 UDP 负载均衡的。

<!--more-->

首先，需要安装 Nginx 比较新的支持 `stream` 配置关键字的版本。比如 Ubuntu 14.04 中的版本就不支持，需要通过 PPA 安装。PPA 安装的版本是需要通过动态链接库来加载 `stream` 功能的。以 Ubuntu PPA 中版本为例，在 `nginx.conf` 靠前的位置添加

```
load_module /usr/lib/nginx/modules/ngx_stream_module.so;
```

下面的片段配置了监听 UDP 1515，把请求平均的发给 3 台机器的 1514 UDP 端口。需要注意的，这个配置片段必须在 `nginx.conf` 的顶层，像 `site-enabled` 下的配置文件一般是嵌套在 `http` 下的，所以不能放那里面。

配置里的 [proxy_responses](https://nginx.org/en/docs/stream/ngx_stream_proxy_module.html#proxy_responses) 是等待代理服务返回包并发回客户端的个数，这个需要根据场景配置。因为我是用来接受 `rsyslog` 的日志转发的，并不需要返回消息，也没有返回消息。同时请求量非常大，如果不设置为 0，Nginx 会因为不断创建连接，最终耗尽而无法响应新的请求。

```
stream {
  upstream syslog_udp {
    server logs1-xy.example.com:1514;
    server logs2-xy.example.com:1514;
    server logs3-xy.example.com:1514;
  }
  server {
    listen 1515 udp;
    proxy_pass syslog_udp;
    proxy_responses 0;
  }
}
```

因为日志转发量大，所以还需要提高 Nginx 进程的 `nofile` 限制和连接数的限制

```
worker_rlimit_nofile 1000000;

events {
    worker_connections 20000;
}
```
