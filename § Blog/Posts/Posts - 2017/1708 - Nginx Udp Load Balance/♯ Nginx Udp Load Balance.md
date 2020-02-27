---
comment: true
date: "2017-08-23T23:11:35+08:00"
description: Use Nginx stream proxy as UDP load balance
katex: false
share: true
title: "Nginx as UDP Load Balance"
---

# Nginx as UDP Load Balance

#nginx

Just upgraded Graylog to cluster in a project. Because syslog UDP is used as input, a UDP load balance is required to distribute logs to servers in the cluster. Since the servers are hosted in Aliyun, I tried Aliyun UDP Load Balance first. But it does not forward requests evenly, and health detection diagram cannot be disabled. The popular HTTP load balance tool HAProxy does not support UDP. Fortunately, Nginx can be used as a UDP load balance.

<!--more-->

First, the latest version of Nginx is required to support `stream` directive.  For example, the default package in Ubuntu 14.04 does not support it, thus use PPA or compile from source.

The PPA version requires loading the feature from dynamic library. Add following line in the beginning of `nginx.conf`.

```
load_module /usr/lib/nginx/modules/ngx_stream_module.so;
```

The following snippet configures Nginx listens on UDP 1515, and forward requests evenly to the 1514 UDP port in three different servers. The snippet must be at the top level of `nginx.conf`. Files in `sites-enabled` usually are embedded in `http` directive, do not put stream config there.

The option [proxy_responses](http://nginx.org/en/docs/stream/ngx_stream_proxy_module.html#proxy_responses) is the number of packets expected from backend servers in responded to client. It should be configured according to scenario. In my case, I use it to accept logs forwarded from `rsyslog`. The client does not expect response, and the server does not respond at all. If the option is not set to 0, Nginx will refuse new connection after used up all of them.

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

Because there are so many logs requests, the open file limit and worker connections must be set to a large value.

```
worker_rlimit_nofile 1000000;

events {
    worker_connections 20000;
}
```
