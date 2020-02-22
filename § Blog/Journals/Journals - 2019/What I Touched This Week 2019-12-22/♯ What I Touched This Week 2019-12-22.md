---
date: 2019-12-22
description: My weekly review report.
series:
- What I Touched

---

# What I Touched This Week 2019-12-22


## Problems I Solved

I tried to setup GPG in a Linux server and met problems when performing
commands that require passphrase. It turns out that I have to set the
`GPG_TTY` to tell `gpg-agent` that it should ask password from current
console.

First kill the `gpg-agent`. Because it may already hang in the background to wait for
a password.

```
pkill -9 gpg-agent
```

Then set the environment variable for the current session

```
export GPG_TTY=$(tty)
```

Or save it for future sessions

```
echo 'export GPG_TTY=$(tty)' >> ~/.profile
```

## Read Articles

* [Mastery: The Complete Guide to Achieving Greatness](https://doist.com/blog/mastery/)

    * “Mastery is not a function of genius or talent. It is a function of time and intense focus applied to a particular field of knowledge.”
    * Play Big and Embrace Failure
    * Find Balance

* [Blocking inside async code | stjepang.github.io](https://stjepang.github.io/2019/12/04/blocking-inside-async-code.html)

    * As said by [@hayeah](https://twitter.com/hayeah/status/1205698254081380353), "the upside is, you get the worst of both worlds".
    * The crate async-std [tries to solve this problem](https://async.rs/blog/stop-worrying-about-blocking-the-new-async-std-runtime/)

* [Generalized Autoref-Based Specialization · Lukasʼ Blog](http://lukaskalbertodt.github.io/2019/12/05/generalized-autoref-based-specialization.html)

    > [*which*] makes it possible to use specialization-like behavior on stable Rust

* [Announcing Mio 0.7-alpha.1 · Tokio](https://tokio.rs/blog/2019-12-mio-v0.7-alpha.1/)

    Major changes:

    * Wrapping native OS types.
    * Moving to edge triggers.

* [醋醋 | 杨振宁的最后一战](https://mp.weixin.qq.com/s?__biz=MjM5OTEyMTE5NA==&mid=2648827014&idx=1&sn=874abcfd3c4f985aac4f59424b348204&chksm=bed51cc389a295d58d245344a9841042052127166499cf5f257a3bf1e0b7b4e5c6bc860b236c#rd)

    * 超弦无法证伪
    * 超弦很难取得突破
    * 超弦难以落地

    不值得投入大量资金建设对撞机

* [为什么中本聪生于1975年4月5日？](https://mp.weixin.qq.com/s?__biz=MzIwMzQ0MTUxMQ==&mid=2247486554&idx=1&sn=8969fd2da90ed47d1a08ac768b8a348f&chksm=96ce1852a1b99144ec3b8ccb2a1a9078bda75593c41ec14146c54c60cc975b07d3daf99dc502#rd)

    * 1933年4月5日: 美国总统签署法案宣布民众持有黄金违法
    * 1975年: 美国总统签署了《黄金合法化》法案

## Read Books

* 读书：「跑步时该如何呼吸」

    > 韵律呼吸会以奇数模式协调足部落地同吸气和呼气之间的时机。

    采用 3:2 模式，吸-2-3-呼-2。强度加大使用 2:1 模式，吸-2-呼。

## Bookmarks

* [Happy Hues - Curated colors in context.](https://www.happyhues.co/)

