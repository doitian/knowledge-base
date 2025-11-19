---
comment: true
date: '2017-02-25T18:46:03+08:00'
description: ''
katex: false
share: true
title: Deploy Concourse CI using Docker
tags:
  - ci
  - docker
---

# Deploy Concourse CI using Docker

[Concourse CI](https://concourse-ci.org/) is an awesome open source continuous integration tool. If you are not using Gitlab, and want to setup a CI server, it is a good choice.

Concourse CI provides Docker image and docker compose sample config. But when I run the hello world example, I have met several problems.

<!--more-->

First, my Docker host kernel version is too low, which caused the error:

    unknown capability "CAP_AUDIT_READ"

The solution is upgrading kernel. Concourse requires version 3.19+[^1]. Ubuntu 14.04 can use following command:

    sudo apt-get install --install-recommends linux-generic-lts-wily

Second, if Concourse is deployed via docker compose, DNS is changed to loopback address. The job will fail because of DNS lookup error:

    lookup registry-1.docker.io on 127.0.0.11:53: read udp 127.0.0.1:54286->127.0.0.11:53: read: connection refused

Just add DNS config based on [official compose sample](https://concourse-ci.org/install.html) to solve this error. I have configured custom DNS for `concourse-web` and `concourse-worker`. It is also required to setup a DNS for  `concourse-worker` using environment variable `CONCOURSE_GARDEN_DNS_SERVER`[^2]。

If your cloud server provider has its own DNS servers, log into any host and check `/etc/resolv.conf`. Use the DNS servers to replace `8.8.8.8` 和 `8.8.4.4` in the example below.

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

The last, Concourse does not pull docker images via the docker daemon in docker host machine. So the config `registry-mirror` is ignored. The config must be added in the resource source config[^3]. It is tedius that cannot be set as a global config.

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
