---
date: 2016-10-30
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2016-10-30


This week I work on [terraform-provider-ucloud][1], which already has implemented resource UHost and SecurityGroup, data source host image. I plan to share my experience to write a terraform provider plugin in future posts.

<!--more-->

## terraform-provider-ucloud

* [Paw 里进行 UCloud API 签名验证 – Medium][2]
* [golang - 如何判断字符是不是中文？ - SegmentFault][3] 用`[\p{Han}]+`
* [terraform/helper/resource/testing.go][4] is helper for provider testing. Set environment variable `TF_ACC` to run the acceptance test.
* [dnaeon/go-vcr: Record and replay your HTTP interactions for fast, deterministic and accurate tests][5]

## Game Development

* [【十一充电】十五年经验网易高级美术总监：详解次世代MMO流程管理及设计理念][6]

## Management

* [Becoming a CTO // Juozas Kaziukėnas][7]
* [Culture: Drafting your team’s Constitution][8] How Parsable Builds their Company Culture.

## Tools

* I switched to [Paste – smart clipboard history manager for Mac][9] from Copied. I like Paste UI and the simplicity to pin copied items into list.
* [You don’t need more than one cursor in vim – Medium][10] Use `cgn` and `.` to replace is handy.
* [使用 Alfred 提高你的工作效率 | Matrix 精选 - 少数派][11]
* [vitorgalvao][12] has shared [many useful Alfred workflows][13]. He is also a top contributor in [Packal][14].

## Misc

* [没有了老师，你该如何学习？ – ThoughtWorks洞见][16]，[技术的执念 – ThoughtWorks洞见][17] 和 [The path of software development craftsmanship][18] 都提到了应该避免被层出不穷的技术牵着鼻子走，静下心来把时间投资在底层和顶层不怎么变的技术上，中间易变的用到什么学什么。
* [Task Performance Indicator: A Management Metric for Customer Experience · An A List Apart Article][19]. It Introduced TPI to measure customer experience and how Cisco uses it to improve products.
* [How Uber Manages a Million Writes Per Second Using Mesos and Cassandra Across Multiple Datacenters  - High Scalability -][20]
* [Code Hoarders | 8th Light][21] About Legacy Code and Code Quality.
* [Continuations : Our Need for Purpose and Recognition][22] Importance of Recognition as Motivation.
* [Being More Than "Just the Programmer"][23] Next steps to be a better programmer.
* [Become a Better Coder by Keeping a Programming Journal][24] However I prefer digital journal, since it is simple to keep links and I can click to open them.
* Podcast [Job Preservation][25]First of a short series about the business of dying.

## Bookmarks

* [LightNote][26] This site is an attempt to teach you just enough essential music theory to take you from a tab-reader to a music creator!
* [Kong - Open-Source API Management and Microservice Management][27]. API Gateway built on Nginx.
* [Vue Material][28] Material theme for vue.js
* [Netflix/chaosmonkey: Chaos Monkey is a resiliency tool that helps applications tolerate random instance failures.][29]

[1]:    https://github.com/3pjgames/terraform-provider-ucloud
[2]:    https://medium.com/@doitian/paw-%E9%87%8C%E8%BF%9B%E8%A1%8C-ucloud-api-%E7%AD%BE%E5%90%8D%E9%AA%8C%E8%AF%81-da7d4d5b0471#.o5qfy65nd
[3]:    https://segmentfault.com/q/1010000000595663
[4]:    https://github.com/hashicorp/terraform/blob/master/helper/resource/testing.go
[5]:    https://github.com/dnaeon/go-vcr
[6]:    http://mp.weixin.qq.com/s?__biz=MjM5OTc2ODUxMw==&mid=2649706459&idx=2&sn=e27d742817435bd9c64fd450b7c8054c&chksm=bf2d9775885a1e63a3531e2982f29da459a1383a5080c29efb6f5be2cb66520c87f0e048e731&scene=0#wechat_redirect
[7]:    https://juokaz.com/blog/becoming-a-cto?utm_source=wanqu.co&utm_campaign=Wanqu+Daily&utm_medium=website
[8]:    https://blog.parsable.com/culture-drafting-your-teams-constitution-9506f186db6d#.lkft988e6
[9]:    http://pasteapp.me/
[10]:   https://medium.com/@schtoeffel/you-don-t-need-more-than-one-cursor-in-vim-2c44117d51db#.z7ti8o4id
[11]:   http://sspai.com/35927
[12]:   https://github.com/vitorgalvao
[13]:   https://github.com/vitorgalvao/alfred-workflows
[14]:   http://www.packal.org/
[16]:   http://insights.thoughtworkers.org/how-to-study-without-teacher/
[17]:   http://insights.thoughtworkers.org/obsession-og-technology/?utm_source=external-newsletter&mkt_tok=eyJpIjoiTmpJeU1qUmhPVGhoWkRVNCIsInQiOiI2Z2hydkM4dWdXVzB0ZWxcLytlOG9ubldmOUNnRk9tMWFQR09oaVYwSVJVWTNcL3pyaE1PZTFheWJhQVZZcGdPSUh4U25lYWNzWHhDZDdvT0lKdXdlemRRNjkrR21xRW5Rc3RHc2FpcE02Sm1rPSJ9
[18]:   https://rainsoft.io/the-path-of-software-development-craftsmanship/?utm_source=wanqu.co&utm_campaign=Wanqu+Daily&utm_medium=website
[19]:   http://alistapart.com/article/task-performance-indicator-management-metric-for-customer-experience
[20]:   http://highscalability.com/blog/2016/9/28/how-uber-manages-a-million-writes-per-second-using-mesos-and.html
[21]:   https://8thlight.com/blog/uncle-bob/2014/04/03/Code-Hoarders.html?utm_source=wanqu.co&utm_campaign=Wanqu+Daily&utm_medium=website
[22]:   http://continuations.com/post/151791965100/our-need-for-purpose-and-recognition
[23]:   http://prog21.dadgum.com/224.html
[24]:   http://www.makeuseof.com/tag/become-better-coder-keeping-programming-journal/
[25]:   https://m.signalvnoise.com/job-preservation-cb25f52150ad#.xh5vsbcc9
[26]:   http://www.lightnote.co/
[27]:   https://getkong.org/
[28]:   https://marcosmoura.github.io/vue-material/#/
[29]:   https://github.com/netflix/chaosmonkey
