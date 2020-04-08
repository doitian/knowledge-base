---
date: 2016-12-25
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2016-12-25


This week I mainly worked on setting up monitoring system using prometheus and grafana.

<!--more-->

## Monitoring and Logging

- Example of [how to write a graylog output plugin][1]
- Add graylog2 stored data in grafana:
    - Type: elasticsearch
    - Connect to the configured elasticsearch instances used in graylog2
    - Leave 『Index name』empty
    - Time field name: timestamp
- Prometheus client libraries keep all metrics, do not use keep increasing value as a tag, such as user id.
 - Rsyslog writes logs to file using user and group syslog

## Misc

- Recreate Postgres database on macOS installed via Homebew

        rm -rf /usr/local/var/postgres && initdb /usr/local/var/postgres -E utf8

- Homebrew 镜像，和其它一些软件源镜像 [开源镜像使用帮助列表 [LUG@USTC]][2]
- Maven 镜像仓库

        <mirror>
          <id>nexus-aliyun</id>
          <mirrorOf>*</mirrorOf>
          <name>Nexus aliyun</name>
          <url>http://maven.aliyun.com/nexus/content/groups/public</url>
        </mirror> 

- An example that caches maven dependencies in Gitlab CI:

        cache:
          paths:
            - .m2/
        
        variables:
          MAVEN_OPTS: "-Dmaven.repo.local=.m2"
        
        maven_job:
          script:
            - mvn clean install

- Automate game testing using image recognition
  - [Image Recognition for Android and iOS Game Testing][3]
  - [Image Recognition in Mobile Game Testing][4]
  - [《腾讯Android自动化测试实战》][5] 也有在测试中使用 OpenCV 做图像识别的例子。
- [如何做一款有趣有毒的游戏：独立团队 Laser Dog 新游戏的幕后故事 - 少数派][6]
- [Groundera — Indie books by entrepreneurs][7]


[1]:  [graylog-plugin-slack/SlackMessageOutput.java%20at%20master%20%C2%B7%20Graylog2/graylog-plugin-slack](%20https://github.com/Graylog2/graylog-plugin-slack/blob/master/src/main/java/org/graylog2/plugins/slack/output/SlackMessageOutput.java%20)
[2]:  https://lug.ustc.edu.cn/wiki/mirrors/help
[3]:  http://bitbar.com/how-to-use-image-recognition-for-mobile-app-and-game-testing/
[4]:  http://bitbar.com/mobile-game-testing-part-2-ui-and-functionality-image-recognition/
[5]:  https://item.jd.com/11985901.html
[6]:  http://sspai.com/36392
[7]:  https://groundera.com/
