---
date: 2016-11-27
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2016-11-27


This week I worked on syslog integration in [skynet][1] and delve into details of skynet. I also started using Gitlab CI.

<!--more-->

## skynet

- [云风的 BLOG: 代理服务和过载保护][2]。使用 debug 命令 PING 可以检查服务是否还在，目前平均响应时间怎么样。命令 LINK 可以用来监控服务是否退出。
* 弄了一套脚本来编译，安装 skynet，生成和管理  skynet 项目。大概用起来

    ``` sh
    # 创建项目 helloworld
    sx new helloworld
    # 启动 skynet 应用
    cd helloworld
    sx skynet boot/helloworld.lua
    # 创建新的 skynet 应用
    sx new-app server
    sx skynet boot/server.lua
    # 执行 Lua
    sx lua
    ```

## Gitlab CI

*   Gitlab documentation does not mention how to setup docker registry key. Indeed, it requires a pair of RSA keys, use private key in Gitlab and public key in docker registry.

*   In `.gitlab-ci.yml`, variables defined in job level is also effective in top fields, such as `before_script` and `services`. Here is an example to test Rails using MySQL and Postgres

    ```yaml
    image: rails

    services:
        - redis
        - $DB

    cache:
        key: bundle
        paths:
            - vendor/bundle

    variables:
        POSTGRES_DB: center_test
        POSTGRES_USER: runner
        POSTGRES_PASSWORD: ""
        MYSQL_DATABASE: center_test
        MYSQL_ROOT_PASSWORD: root

    before_script:
        - cp config/database.ci-$DB.yml config/database.yml
        - cp .ci.env .env
        - bundle install --jobs $(nproc) --path=vendor/bundle

    .test: &test_template
        script:
            - bundle exec rake db:create RAILS_ENV=test
            - RAILS_ENV=test bundle exec rake db:reset
            - bundle exec rake test

    test_pg:
        <<: *test_template
        variables:
            DB: postgres

    test_mysql:
        <<: *test_template
        variables:
            DB: mysql
    ```

*   [Using Docker Build - GitLab Documentation][3]. I use dind to build docker images in Gitlab CI. It requires starting docker in privilege mode, which breaks some containers such as mysql. A simple solution is registering 2 docker runners, one is in privilege and another is not. Tag runners and add tags in `.gitlab-ci.yml` to filter runner.
*   In Mac, `gitlab-ci-multi-runner` must be started in user desktop environment. The runner may stuck at checkout code because the GUI is asking for keychain access. Just approve the access in desktop environment.

## DevOps
* [GitHub - 3pjgames/terraform-provider-dnspod: Terraform Provider Plugin which manages DNS records in dnspod.cn][4]
* [ubuntu - How can I selectively override some A records on a Bind DNS Server? - Server Fault][5]. I need to override some A record to speed up internal SVN and Git access in Office. I used to setup zone file for the whole domain. However if I need to update DNS records, I have to update office zone config files and update in DNS provider. This solution saves my time, thanks a lot.
* [服务发现：Zookeeper vs etcd vs Consul  - DockOne.io][6]. Etcd does only one thing, Consule is more feature rich.
- [Backing up your minions’ databases to the Salt master][7]. Let minion push files to master.

## Misc
* [最近转到 Bear 作为主力笔记应用][8]
* [GitHub - tj/git-extras: GIT utilities — repo summary, repl, changelog population, author commit percentages and more][9]. Bundle of useful git commands.
* [GitHub - tpope/vim-eunuch: eunuch.vim: helpers for UNIX][10]. I love `Rename`.
* [Bugsnag Blog - Benefits of using tmux - lessons from streamlining a development environment][11]
- [how to remove Google’s secret update software from your mac |][12].
* [A shining example of how to teach – Signal v. Noise][13]

[1]: https://github.com/cloudwu/skynet
[2]: http://blog.codingnow.com/2016/05/skynet_proxy.html
[3]: https://docs.gitlab.com/ce/ci/docker/using_docker_build.html
[4]: https://github.com/3pjgames/terraform-provider-dnspod
[5]: http://serverfault.com/questions/615641/how-can-i-selectively-override-some-a-records-on-a-bind-dns-server/615684
[6]: http://dockone.io/article/667
[7]: https://web.archive.org/web/20170121012541/http://www.afewmorelines.com/backing-up-your-minions-databases-to-the-salt-master/
[8]: https://medium.com/@doitian/bear-%E6%8E%A5%E8%BF%91%E6%88%91%E5%BF%83%E7%9B%AE%E4%B8%AD%E5%AE%8C%E7%BE%8E%E7%9A%84%E7%AC%94%E8%AE%B0%E5%BA%94%E7%94%A8-27c511af778c#.tdynedo3q
[9]: https://github.com/tj/git-extras
[10]: https://github.com/tpope/vim-eunuch
[11]: https://blog.bugsnag.com/benefits-of-using-tmux/
[12]: http://applehelpwriter.com/2014/07/13/how-to-remove-googles-secret-update-software-from-your-mac/
[13]: https://web.archive.org/web/20170505012341/https://m.signalvnoise.com/a-shining-example-of-how-to-teach-91b718009b33
