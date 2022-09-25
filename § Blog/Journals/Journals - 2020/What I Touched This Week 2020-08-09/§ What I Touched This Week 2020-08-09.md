---
date: 2020-08-09
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2020-08-09

Recommended in the last week:

* [What to Do When You’re Mentally Exhausted](https://doist.com/blog/mental-fatigue/)

    * Acknowledging that fatigue is a natural result of challenging your brain can be freeing in and of itself.
    * Different ways to handle fatigue, such as diet, sleep, exercise and work methods.

<!--more-->

## Productivity

* [The Automation of Note-Taking and the Just-In-Time Future of Work](https://fortelabs.co/blog/the-automation-of-note-taking-and-the-just-in-time-future-of-work/)

    * [See nodes in] random combinations. We need to be able to shuffle our notes around to generate new insights.
    * It’s now more important to do the opposite: finding information that contradicts or disconfirms what we know. Discovering information that contradicts what we currently believe is the new frontier of learning.

* [我们究竟需要怎样的时间管理工具](https://sspai.com/post/61776)

    * 我发现最合适的还是以笔记软件为主、轻量提醒工具为辅的组合（目前我的组合是 Notion + Dislike）。

* [效率提升：让你一天多出几个小时的做事方法！](https://sspai.com/post/61235)

    提前规划，统筹安排

* [Efficiency Is Not Our Goal](https://medium.com/@kgale/efficiency-is-not-our-goal-7ab1e8476adb)

    * Value total organizational throughput.
    * [Pay attention to] how much coordination and agreement cost must be spent preventing inefficiency
    * There are other times when throughput is damaged in pursuit of efficiency.

* [The Freelancer’s Guide to Todoist](https://doist.com/blog/todoist-guide-freelancers/)

    * According to a [2019 UpWork study](https://www.upwork.com/press/economics/freelancing-and-the-economy-in-2019/), 57 million Americans, or 35% of the U.S. population, do freelance work.
    * Labels usage examples:
        * and an “amplify” label to share content created by peers you admire whose work you want to signal boost.
        * Use labels like `$`, `$$`, or `$$$` to differentiate which tasks and assignments have the highest earning potential so you can gauge the worth of a to-do at a glance.

* [Advantages of not using the best tool for the job](https://www.johndcook.com/blog/2020/07/25/worst-tool-for-the-job/)

    > if you need a tool, buy the cheapest one you can find. If it’s inadequate, or breaks, or you use it a lot, then buy the best one you can afford.

* [This simple but powerful analog method will rocket your productivity](https://www.fastcompany.com/90535318/this-simple-but-powerful-analog-method-will-rocket-your-productivity)

    * If an idea has value, it will rise to the surface as more related notes emerge.
    * Note links exponentially increase the value of the system.

* [如何追求精力充沛的生活](https://sspai.com/post/61722)

    * 工作成果 = 工作效率 X 有效工作时间
    * 下一步我们能做的就是提高自己的工作效率，这就需要我们做好精力管理。
    * 应对不同场景，将自己的**行为流程化**
    * Morning Routine 起到了心理暗示的效果，让我可以快速进入到工作状态中。

* [How to Take a Digital Note, by Tiago Forte](https://www.youtube.com/watch?v=T4u4nUsdJbs)

* [如何打造个人核心竞争力](https://sspai.com/post/61633)

## Management

* [Brief explanation of agile - This is Agile](https://www.youtube.com/watch?v=Tj-lavaMkxU)

* [Code review – from good to great](https://sizovs.net/2020/07/19/the-code-review/)

    In a team I sat next to, a junior developer asked a senior to conduct code review for a newly completed feature. According to the process, that Senior had to approve all changes going to production. Here is how it went: Senior: “No, I am busy.”

## Software Development

* [Automated Canary Analysis at Netflix with Kayenta](https://netflixtechblog.com/automated-canary-analysis-at-netflix-with-kayenta-3260bc7acc69)

    * Traffic is split between these two versions such that a portion of incoming requests are diverted to the canary.

* [Local-first software, You own your data, in spite of the cloud](https://www.inkandswitch.com/local-first.html)

    * Most notably are the family of distributed systems algorithms called [Conflict-free Replicated Data Types](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type) (CRDTs).

* [Our remote work future is going to suck](https://www.seanblanda.com/our-remote-work-future-is-going-to-suck/)

    As COVID-19 continues to alter the way we live, there is a scramble to predict what our “new normal” will look like. After the virus fades away or, God help us, becomes a constant in our day-to-day life for years to come, which change brought on by the pandemic will stick?

    * eventually competing with the global talent market
    * Remote enables you to be forgotten

* [How we migrated Dropbox from Nginx to Envoy](https://dropbox.tech/infrastructure/how-we-migrated-dropbox-from-nginx-to-envoy)

    * [Nginx,] although it is event-loop based, is it not fully non-blocking.
    * Envoy uses threads instead of processes. It relies on libevent for event loop implementation. Envoy does not have any blocking IO operations in the event loop.
    * Nginx showed higher long tail latencies. This was mostly due to event loops stalls under heavy I/O
    * Envoy has the ability to stream access logs over gRPC.
    * Envoy has control RPC.
    * Envoy has a unified data-model for configs: all of its configuration is defined in Protocol Buffers.
    * Envoy relies heavily on modern security practices. It uses AddressSanitizer, ThreadSanitizer, and MemorySanitizer. Its developers even went beyond that and adopted fuzzing.

* [SQL style guide by Simon Holywell](https://www.sqlstyle.guide)

* [You've only added two lines - why did that take two days!](https://www.mrlacey.com/2020/07/youve-only-added-two-lines-why-did-that.html)

## Blockchain

* [UTXO Management for Enterprise Wallets](https://blog.bitgo.com/utxo-management-for-enterprise-wallets-5357dad08dd1) introduced two wallet models, Send-Only hot wallet and Send-and-Receive Hot Wallet. It also has many interesting discussions about the utxo management.

* [Field Report: Using Descriptors and PSBT at River Financial](https://bitcoinops.org/en/river-descriptors-psbt/)

* [Idea about the composability of assets in ckb](https://talk.nervos.org/t/idea-about-the-composability-of-assets-in-ckb/4855)

    > Recently, I am working on the prototype of the generic payment channel (GPC). But I find the current model is not completely generic.

## Apps Usage

* [How to Combine Different Structures in XMind and Why - XMind: The Most Popular Mind Mapping Software on The Planet.](https://www.xmind.net/blog/en/how-to-combine-different-structures-in-xmind-and-why/)

* [How GoodNotes Uses GoodNotes](https://medium.goodnotes.com/how-goodnotes-uses-goodnotes-9e0c2acac323)

* [请把这张图打印出来，下次做PPT时对照检查！](https://sspai.com/post/61728)

    * 时间就应该更多花在演示设计上
    * 明确演示目标
        1. 听众（汇报对象）是谁？
        2. 核心信息是什么？
        3. 这个汇报在什么场景下展示？
            * 如果是演讲，那就要考虑「矛盾导入」「发现问题」「分析问题」「解决问题」的逻辑。
            * 如果是工作汇报，那就要考虑「结论先行」「论据补充」的「金字塔逻辑」。
    * 数据
        * 过往案例 (纵向)
        * 其他企业案例 (横向)
    * 有了大概的思路后，可以考虑把提纲画好，并明确清楚哪些素材有了，哪些素材还欠缺。
    * 可以考虑找到一些相关领域的专业知识，用它来提纲挈领，整体便有了高度。
    * 展示准备
        * 设计包袱
        * 互动
        * 视频
        * 幽默

* [用好 Keynote 和 iMovie，在 iPad 上做出有高级感的视频 - 少数派](https://sspai.com/post/61882)

    * 使用 Keynote 神奇移动
    * 用 Videoleap 这个 App 的「色度」工具同样可以抠除背景。
    * 在 Mac 平台出现了一款叫 <a href="https://sspai.com/post/52482">Design Camera</a> 的软件，实质上是高度自动化的 3D 模板带壳截屏，可以生成运动立体的带壳截屏视频。这款叫 SceneShot 的App填补了 [iOS] 这一空白，它可能是目前带壳截屏类App中最高级的了，它提供 3D 模版供你调整，并可以定制背景和环境光线，甚至还有特效滤镜等等功能。
    * 之前介绍过的 Canva，最近刚更新了视频制作功能

## Hardware

* [为什么 ARM 版 Mac 运行效率很高？](https://sspai.com/post/61274)

    * Apple 不仅处理掉了第三方的 CPU，且一并处理掉了第三方的 GPU。
    * Mac 这次的芯片变革需要撑得起未来十年，其最优解便是将专精芯片以最优工艺的整合在 Soc 中。

* [看懂高通的一图流：QC5 将这样改变你的快充体验](https://sspai.com/post/61838)

    * 最高支持 100W 充电功率
    * 与 PD 兼容
    * 考虑购买更为通用的 PD-PPS 充电器，并且尽量购买支持电流到 5A/支持电压到 20V 的充电器，为下一代即将到来的 PD-PPS 快充作准备。而在购买 Type-C 线缆的时候，也请优先考虑购买最大承载电流达到 5A 的充电线。

## Business

* [Microsoft’s TikTok: But why?](https://om.co/2020/08/03/microsofts-tiktok-but-why/)

* [PR FAQs for Product Documents -- Everything Product Managers Need to Know](https://medium.com/pminsider/press-releases-for-product-managers-everything-you-need-to-know-942485961e31)

    A Press Release (PR) Frequently Asked Questions (FAQ) is a customer-centric document for designing new products. It is an idealized future “Press Release” (PR) and associated FAQs. The PR FAQ is the starting point for your other product documents.

## Life

* [氮化镓是如何让充电器变小的？](https://sspai.com/post/61958)

    我们想认真的聊一聊氮化镓是怎么让充电器从一块大砖头变成半块砖头，变成一只口红，甚至变成一个仙贝。

## Misc

* [Timeful Texts](https://numinous.productions/timeful/)

    Book designed with [spaced repetition memory systems](https://en.wikipedia.org/wiki/Spaced_repetition) in mind.

* [How (some) good corporate engineering blogs are written](https://danluu.com/corp-eng-blogs/)

* [大国隐痛：做一个操作系统有多难？](https://mp.weixin.qq.com/s/1YJH1qQmJU-eUsk6WiVytw)

    * 用国产系统可以向指标交账，却做不了业务没资金入账。

* [同样受歧视的印度人，为什么却如此成功？](http://nulishehui.blog.caixin.com/archives/232320)

    * 在英美的留学生人数中国第一，印度第二，为什么我们没听说歧视印度人的呢？！
    * 根据《哈佛商业评论》的一项研究，世界 500 强企业中，30% 的掌舵人都是印度人。
    * 美国的中日韩裔人数是印巴裔人数的 1.5 倍
    * 他们有远远强于我们的沟通能力，更重要的是他们非常有要沟通的意识。
    * 专业也许你不需要最强的，但是你的沟通能力，你的视野才是最重要的
    * 家庭条件很一般甚至很差的情况下，家长只要发现孩子是聪明、愿意用功的，真的会和中国家长一样不惜砸锅卖铁也要去培养孩子成才的。
    * 一方面他们特别保持自己的传统价值观，一方面他们又是非常游刃有余的在跟主流融化有融合
    * 印度文化鼓励辩论和争论
    * 我们大部分情况下，华人是互相忌惮的。
    * H1B 签证的话，印度差不多每年有四五万，中国是他们的十分之一。

## Interesting Stuffs

* [@BntBadglass: 论男朋的拍照技术](https://twitter.com/doitian/status/1290508424694779905)
* [@S7i5FV0JOz6sV3A: 哈士奇 vs 牧羊犬](https://twitter.com/doitian/status/1291109632098873346)

## Bookmarks

* [abseil / abseil.io](https://abseil.io)
* [MemorySanitizer · google/sanitizers Wiki](https://github.com/google/sanitizers/wiki/MemorySanitizer)
* [ThreadSanitizerCppManual · google/sanitizers Wiki](https://github.com/google/sanitizers/wiki/ThreadSanitizerCppManual)
* [AddressSanitizer · google/sanitizers Wiki](https://github.com/google/sanitizers/wiki/AddressSanitizer)
* [Tabler Icons - 550+ Highly customizable free SVG icons](https://tablericons.com)
