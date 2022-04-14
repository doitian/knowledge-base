---
date: 2016-11-06
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2016-11-06


This week I worked on rsyslog research and management. The work on terraform-provider-ucloud is postponed. 

<!--more-->

## rsyslog

* Use template in output action

    ```
    $template PJL_Format,"%timegenerated%|%HOSTNAME%|%syslogtag%|%msg%\n"
    $template PJL_File,"/tmp/local-%programname%.log"
    local6,local7.* ?PJL_File;PJL_Format
    ```

* Use tag to filter log. Facilities are fixed and cannot add new custom facility, but app can specify arbitrary tag. The tag format is `programname[PROCID]`
* `Syslog::Logger` in Ruby reserves higher priorities (crit, alert and emerge) for system message. The mapping to Logger severity is one level lower:
    * Ruby -\> syslog
    * debug -\> debug
    * info -\> info
    * warn -\> notice
    * error -\> warning
    * fatal -\> err
* Ruby 2.0 cannot specify facility when creating `Syslog::Logger`, 2.2 has the third parameter to specify the facility.
* [20.2. Basic Configuration of Rsyslog][1] via Redhat

## Game

* [The Illusion of Choice - 一点儿也不宅 - 知乎专栏][2] 游戏中的选择
* [地牢战争，魔性节奏的像素塔防佳作 | Matrix 精选 - 少数派][3]

## Management

* [Why you should argue with your employees][4] 适当的争吵
* [出口就容易伤人？试试“三明治法则”吧！][5] 表扬，批评，期望

## Misc

* [Moving away from puppet: SaltStack or Ansible? | Ryan D Lane][7] Comparison between SaltStack and Ansible. The author prefers SaltStack.
* [Need to specify `--with-opt-dir` on OSX 10.11 El Capitan. · Issue #718 · puma/puma][8] Bundle can configure build options for specific gem: `bundle config build.puma --with-opt-dir=/usr/local/opt/openssl`
* [tencent/libco][9]. Coroutine for C, from WeChat team.

[1]:    https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/s1-basic_configuration_of_rsyslog
[2]:    https://zhuanlan.zhihu.com/p/23314649
[3]:    http://sspai.com/35894
[4]:    https://m.signalvnoise.com/why-you-should-argue-with-your-employees-ab8189fcd1c4#.khcwz2hp0
[5]:    http://mp.weixin.qq.com/s?__biz=MjM5NjAyMDE5Mg==&mid=2649813638&idx=1&sn=3badc5dbbb3fa6c31a493d5c2948eaa1&chksm=beebf809899c711f00a2b54cd67e7a161d8b6f11079fc650cad9400bc6f7c7342c97d870af77&scene=0#rd
[7]:    http://ryandlane.com/blog/2014/08/04/moving-away-from-puppet-saltstack-or-ansible/
[8]:    https://github.com/puma/puma/issues/718
[9]:    https://github.com/tencent/libco
