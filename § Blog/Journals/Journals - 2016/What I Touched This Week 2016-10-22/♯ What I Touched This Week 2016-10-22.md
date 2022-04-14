---
date: 2016-10-22
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2016-10-22


## Programming

* How to write terraform provider plugin. Read the [brief official documentation][1]. Follow this [vsphere plugin][2] to see sample `main.go` and builtin [vms provider][3] as the reference. Must read files: `provider.go` and `resource_aws_instance.go`. My project is [terraform provider ucloud][4].
* [云风的 BLOG: 继续谈网络游戏的同步问题][5] 分两个 model 分别同步共享状态和私有状态。如果出现冲突服务器将修正的操作的参数再通知回客户端。
* [Lessons Learned from Scaling Uber to 2000 Engineers, 1000 Services, and 8000 Git repositories - High Scalability -][6]. Introduce the micro services architecture in Uber, the cons and pros and experience.
* [How to correctly use context.Context in Go 1.7 – Medium][7] How to use context and how to not abuse context values.
* [go - Separating unit tests and integration tests in GoLang (testify) - Stack Overflow][8] The difference of using build flag integration and short test flag is that: integration build flag does not run integration test by default, and short flag will run all tests.

## Game Development

* Scott Brodie (@brodiegames) tweets about [builtin support of circular UIs in Unity][9]
* [NGUI三大基础机制][10] NGUI 渲染底层的一些分享

<!--more-->

## Web Development

* [Debunked: 10 Misconceptions about AMP][11] What AMP is not. It is also a good introduction to AMP.

## Management

* [All you ever wanted to know about all-hands (but were afraid to ask) – Medium][12] Share why and how to run all-hands.

## Tips

* [How to make "spoiler" text in github wiki pages? - Stack Overflow][13] How to create collapsed section using HTML tag *details* and *summary*.

## Open Source Projects

* [Microsoft/LightGBM][14] a fast, distributed, high performance gradient boosting framework.
* [Disney open source projects][15]

## Apps and Tools

* [Woboq Code Browser - Explore C\++ code on the web][16] Semantic info is extracted using LLVM.
* [A Sharper Scaling][17] Image upscaling tool.
* [coala][18] One command to lint code in many different languages.

## Game

* [Don't Starve 中文维基][19]

## Misc

* [Jean-Marc Denis - Black][20] Black wallpapers for phone and desktop.
* [Tech Tips, Tricks & Trivia: Tips for more effective white-boarding][21]
* [中文文案排版指北][22]

[1]:    https://www.terraform.io/docs/plugins/
[2]:    https://github.com/rakutentech/terraform-provider-vsphere
[3]:    https://github.com/hashicorp/terraform-provider-aws
[4]:    https://github.com/3pjgames/terraform-provider-ucloud
[5]:    http://blog.codingnow.com/2016/10/gamesync.html
[6]:    http://highscalability.com/blog/2016/10/12/lessons-learned-from-scaling-uber-to-2000-engineers-1000-ser.html
[7]:    https://medium.com/@cep21/how-to-correctly-use-context-context-in-go-1-7-8f2c0fafdf39#.pmk4vjiow
[8]:    http://stackoverflow.com/a/28007631/667158
[9]:    https://twitter.com/brodiegames/status/786041246321999873
[10]:   http://mp.weixin.qq.com/s?__biz=MzA4MDc5OTg5MA==&mid=2650586822&idx=4&sn=cca55822c77793d8aa093cfed8ea7ab5&chksm=8796af3bb0e1262dfc24fb4ed354f498e502d2dd98e7bb75d56564059ceab717b111cc1018af&scene=0#wechat_redirect
[11]:   https://paulbakaus.com/2016/10/13/debunked-10-misconceptions-about-amp/?utm_source=wanqu.co&utm_campaign=Wanqu+Daily&utm_medium=website
[12]:   https://medium.com/@gokulrajaram/all-you-ever-wanted-to-know-about-all-hands-but-were-afraid-to-ask-b13f7b97f2d9#.ovwq0mbix
[13]:   http://stackoverflow.com/questions/32814161/how-to-make-spoiler-text-in-github-wiki-pages/39920717?stw=2#39920717
[14]:   https://github.com/Microsoft/LightGBM
[15]:   http://disney.github.io/
[16]:   https://code.woboq.org/
[17]:   http://a-sharper-scaling.com/
[18]:   http://coala.io/
[19]:   http://zh.dontstarve.wikia.com/wiki/Don't_Starve_%E4%B8%AD%E6%96%87%E7%B6%AD%E5%9F%BA
[20]:   https://jmd.im/black
[21]:   http://mvark.blogspot.jp/2016/10/tips-for-more-effective-white-boarding.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed:+WebDevelopmentTipsTricksTrivia+(Tech+Tips,+Tricks+&+Trivia)
[22]:   https://github.com/sparanoid/chinese-copywriting-guidelines
