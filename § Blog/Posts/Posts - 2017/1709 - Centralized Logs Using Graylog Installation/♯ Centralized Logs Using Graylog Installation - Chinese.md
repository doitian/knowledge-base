---
comment: true
date: '2017-09-17T19:28:47+08:00'
description: Graylog 安装说明和可能出现的问题
katex: false
series:
- Graylog
share: true
title: Graylog 集中日志管理 - 安装
---

# Centralized Logs Using Graylog Installation

#graylog #devops

使用 [Graylog](https://www.graylog.org) 之前试过很多方案，包括流行的 ELK，也用过 fluentd 搭配各种存储，influxdb, mongodb 等等。但这些方案在日志量大了之后出现性能瓶颈都没有提供解决方案。而 Graylog 作为整合方案，使用 elasticsearch 存储，mongodb 缓存，带流量控制 (throttling)，简单易用的查询界面，方便的管理界面，易于扩展。转移到 Graylog 省心了不少。在使用过程中积累了些经验，准备陆续分享出来。

第一篇是关于如何安装 Graylog。

<!--more-->

官方提供了自动化和[手动安装](http://docs.graylog.org/en/2.3/pages/installation/manual_setup.html)，以及[集群配置](http://docs.graylog.org/en/2.3/pages/configuration/multinode_setup.html)的文档。稍微麻烦点的是安装 mongodb 和 elasticsearch 集群，以及配置 graylog 里的各种地址。

Mongodb 在有防火墙保护下，最简单的集群方案是不设置验证，只需要所有节点配置相同的  `replSet`  就行了

```
replSet = graylog
```

然后按照文档[初始化一下](https://docs.mongodb.com/manual/tutorial/deploy-replica-set/)，注意 `_id` 要和配置的 `replSet` 一致。

```
rs.initiate( {
   _id : "graylog",
   members: [ { _id : 0, host : "logs1.example.com:27017" } ]
})
rs.add("logs2.example.com")
rs.add("logs3.example.com")
```

Elasticsearch 类似，配置相同的 cluster name 并列出集群内机器

```
cluster.name: graylog
discovery.zen.ping.unicast.hosts：
- logs1.example.com
- logs2.example.com
- logs2.example.com
```

Graylog 只要保证只有一个节点配置成了 master

```
is_master = true
```

比较容易出错和混淆的就是各种地址的配置，主要是有些没配置会用另外的选项作为默认值。推荐是显式的配置所有下面四个选项：

- `rest_listen_uri` 用来指定 API 启动时监听的网卡，端口和 API 地址前缀。没什么特殊原因，这个配置成  `http://0.0.0.0:9000/api/` 就行了
- `web_listen_uri` 同上，但是是 WEB 资源的 HTTP 服务器，可以和 API 使用相同的端口，一般配置成 `http://0.0.0.0:9000/` 就可以了
- `rest_transport_uri` 这个是节点暴露给集群其它节点访问用的 API 地址，一般把 `rest_listen_uri` 中的 IP 换成内网 IP 或者域名就行了，比如 `http://logs1-internal.example.com:9000/api/`
- `web_endpoint_uri` 是暴露给 WEB 界面里的 Javascript 连接用的 API 地址，一般把 `rest_listen_uri` 中的 IP 换成公网 IP 或者域名就行了，比如 `http://logs1.example.com:9000/api/`。如果设置了负载均衡，或者代理，可以配置成负载均衡和代理的公网地址，也可以通过 HTTP Header 来覆盖该配置，比如 Nginx

```
proxy_set_header X-Graylog-Server-URL http://logs.example.com/api;
```

Graylog 成功启动后在 Web 管理界面就能查看节点状态和 elasticsearch 集群状态。Mongodb 可以在 mongo 命令行客户端里执行以下两个命令验证：

```
rs.conf()
rs.status()
```
