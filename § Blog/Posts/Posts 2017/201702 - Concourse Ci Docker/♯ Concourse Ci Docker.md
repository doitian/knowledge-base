---
comment: true
date: '2017-02-25T18:46:06+08:00'
description: ''
katex: false
share: true
title: 使用 Docker 部署 Concourse CI
---

# Concourse Ci Docker

#docker #ci

[Concourse CI](https://concourse.ci) 是个很不错的开源持续集成工具，安装和上手都相当简单。如果没有在用 Gitlab 又想自己架设 CI 服务的话是个不错的选择。

Concouse CI 提供了 Docker 镜像，部署起来相当方便。不过可能会踩到一些坑。

<!--more-->

首先如果 Docker 宿主机器内核版本太低的话，运行任务的时候会碰到这样的错误

    unknown capability "CAP_AUDIT_READ"

解决办法只需要升级内核就行了，Concourse 需要 3.19+ 版本内核[^1]，Ubuntu 14.04 中可以执行以下命令

    sudo apt-get install --install-recommends linux-generic-lts-wily 

然后如果使用 docker compose 进行部署的话，DNS 地址一般被改成了本地 loopback 地址，导致运行任务时无法解析域名而出现这样的错误

    lookup registry-1.docker.io on 127.0.0.11:53: read udp 127.0.0.1:54286->127.0.0.11:53: read: connection refused

这个问题可以在[官方 Compose 示例](https://concourse.ci/installing.html)的基础上配置下 DNS。为保险可以为 `concourse-web` 和 `concourse-worker` 都配置上自定义 DNS，并且在 `concourse-worker` 里配置下环境变量 `CONCOURSE_GARDEN_DNS_SERVER`[^2]。

如果使用云主机一般提供了内网用的 DNS 服务器，可以随便登录一台查看下 `/etc/resolv.conf` 然后替换下面例子中使用的公共 DNS 地址 `8.8.8.8` 和 `8.8.4.4`。

``` yaml
concourse-db:
  image: postgres:9.5
  environment:
    POSTGRES_DB: concourse
    POSTGRES_USER: concourse
    POSTGRES_PASSWORD: "${POSTGRES_PASSWORD}"

concourse-web:
  image: concourse/concourse
  links: [concourse-db]
  command: web
  ports: ["8080:8080"]
  volumes: ["keys:/concourse-keys"]
  environment:
    CONCOURSE_BASIC_AUTH_USERNAME: admin
    CONCOURSE_BASIC_AUTH_PASSWORD: "${CONCOURSE_BASIC_AUTH_PASSWORD}"
    CONCOURSE_EXTERNAL_URL: "${CONCOURSE_EXTERNAL_URL}"
    CONCOURSE_POSTGRES_DATA_SOURCE: "postgres://concourse:${POSTGRES_PASSWORD}@concourse-db:5432/concourse?sslmode=disable"
  dns:
    - 8.8.8.8
    - 8.8.4.4

concourse-worker:
  image: concourse/concourse
  privileged: true
  links: [concourse-web]
  command: worker
  volumes: ["keys:/concourse-keys"]
  environment:
    CONCOURSE_TSA_HOST: concourse-web
    CONCOURSE_GARDEN_DNS_SERVER: 8.8.8.8
  dns:
    - 8.8.8.8
    - 8.8.4.4
```

最后的坑是有中国特色的。Concourse 拉取 docker 镜像时没有连宿主机器上的 Docker Daemon，所以配置的 `registry-mirror` 不起作用，需要自己在使用到 Docker 镜像的位置配置下[^3]。这个不能全局配置还是比较麻烦的。

``` yaml
jobs:
- name: hello-world
  plan:
  - task: say-hello
    config:
      platform: linux
      image_resource:
        type: docker-image
        source:
          registry_mirror: https://changeme.mirror.aliyuncs.com
          repository: alpine
      run:
        path: echo
        args: ["Hello, world!"]
```

[^1]: [unknown capability "CAP_AUDIT_READ" · Issue #488 · concourse/concourse]( https://github.com/concourse/concourse/issues/488#issuecomment-229209912 )
[^2]: [\[support\] guardian inside docker cannot access docker-local DNS · Issue #18 · concourse/bin]( https://github.com/concourse/bin/issues/18 )
[^3]: [Adding registry mirror parameter on source by gregarcara · Pull Request #42 · concourse/docker-image-resource]( https://github.com/concourse/docker-image-resource/pull/42 )
