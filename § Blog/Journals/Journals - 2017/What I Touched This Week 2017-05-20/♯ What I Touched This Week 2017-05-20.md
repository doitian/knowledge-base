---
date: 2017-05-20
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2017-05-20



- [我所養成的 10 個最有生產力習慣，以及我如何養成這些習慣](http://www.playpcesor.com/2017/05/10-habit.html)

    要有效的利用时间。通过记录清空大脑并减少下次相似事情时的成本。

- [Why you should totally switch to Kotlin – Magnus Vinther – Medium](https://medium.com/@magnus.chatt/why-you-should-totally-switch-to-kotlin-c7bbde9e10d5)

    For me, Kotlin is powerful, and is under control not like Scala.

- ..., and it is [offically supported in Android Development](http://marketingland.com/google-io-2-214945).

- [The Horror in the Standard Library](https://www.zerotier.com/blog/2017-05-05-theleak.shtml)

    libstdc++ is broken. Set GLIBCPP_FORCE_NEW, link jemalloc

- [“Why We Didn’t Use A Framework” (Case Study) – Smashing Magazine](https://www.smashingmagazine.com/2017/05/why-no-framework/)

    > ... needed 100% control over the UX of the video call ...

    so they choose to use vanilla JavaScript.

- [和 Android 相比，人工智能才是 Google 更想介绍的 ：Google I/O 2017 回顾 - 少数派](https://sspai.com/post/39283)

    - 主题：人工通知
    - 产品：Google Assitant for iOS, Google Lens, Google Home, Android O, VR Headset.

- [Firebase Costs Increased by 7,000%! – Startups & Venture Capital](https://medium.com/@contact_16315/firebase-costs-increased-by-7-000-81dc0a27271d)

    > Due to a change in how they report data usage, our monthly costs for Firebase, a SaaS provided by Google, has increased from $25 a month to what is now moving towards the $2,000 mark — with no changes to our actual data use. This change was made without warning.

    Do not lock your product to 3rd party service. Make it cheap to switch services.

- [golang IO包的妙用 - 简书](http://www.jianshu.com/p/8c33f7c84509)

    `Read` 和 `Write` 接口简单，容易组合

- Gotchas when using ktor, a Kotlin web framework
    - `ktor-netty` is buggy when used with `ktor-websockets`, use `ktor-jetty` instead.
    - `jetty-server` should also be added as a dependencies when using `ktor-jetty`

<!--more-->

## Projects

- [Kawoou/FlexibleImage: A simple way to play with the image!](https://github.com/Kawoou/FlexibleImage) Swift image library.
- [dgraph-io/badger: Fastest key/value store in Go.](https://github.com/dgraph-io/badger)
- [Aerobatic - Professional static web publishing](https://www.aerobatic.com/). Easy static web hosting solution.
- [Siege Home](https://www.joedog.org/siege-home/). An HTTP benchmark tool.
- [lovoo/goka: Goka is a compact yet powerful distributed stream processing library for Apache Kafka written in Go.](https://github.com/lovoo/goka)
- [zetcd: running ZooKeeper apps without ZooKeeper | CoreOS](https://coreos.com/blog/introducing-zetcd). Proxy of etcd that acts as ZooKeeper server.
- [bloomberg/comdb2: Bloomberg's distributed RDBMS](https://github.com/bloomberg/comdb2)

## Misc

- [How a Blind Developer uses Visual Studio - YouTube](https://www.youtube.com/watch?v=iWXebEeGwn0)
- [Rust turns Two](https://blog.rust-lang.org/2017/05/15/rust-at-two-years.html)
