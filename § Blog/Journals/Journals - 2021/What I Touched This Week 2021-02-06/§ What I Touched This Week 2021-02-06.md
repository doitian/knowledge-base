---
date: 2021-02-06
description: My weekly review report.
series:
- What I Touched
obsidianFiles:
- para/lets/m/macOS/Set Up a New Mac
---

# What I Touched This Week 2021-02-06

Picks:

-   [Monitoring in the time of Cloud Native | by Cindy Sridharan | Medium](https://copyconstruct.medium.com/monitoring-in-the-time-of-cloud-native-c87c7a5bfa3e)

    Observability is about the ability to let maintainers understand how the system behaves in the production. It's a super set of monitoring. Observability makes debugging possible in production.

    Three pillars of observability:

    * Logs
    * Metrics
    * Traces

-   [@copyconstruct: Hashed and Hierarchical Timing Wheels: Data Structures for the Efficient Implementation of a Timer Facility, paper from 1987 that’s used in Kafka and rust’s tokio library.](https://twitter.com/copyconstruct/status/1354557112731357191)

    The thread has listed several timing wheels implementations and a [seminar video](https://youtu.be/AftX7rqx-Uc).

 -   [[Set Up a New Mac]]

<!--more-->

## Programming

-   [Software development topics I've changed my mind on after 6 years in the industry](https://chriskiehl.com/article/thoughts-after-6-years)
    -   Clever code isn't usually good code. Clarity trumps all other concerns.
    -   So called "best practices" are contextual and not broadly applicable. Blindly following them makes you an idiot
    -   Designing scalable systems when you don't need to makes you a bad engineer.
    -   In general, RDBMS > NoSql

## DevOps

-   [Dynamic Sampling by Example](https://honeycomb.io/blog/dynamic-sampling-by-example)
-   [The DevOps observability platform | Lightstep](https://lightstep.com/)
-   [Application Monitoring for Ruby, PHP, Node.js, Python, and Elixir ~ Scout](https://scoutapm.com/)
-   [OpenTelemetry](https://opentelemetry.io/)
-   [Site Reliability Engineering - Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
-   [Distributed Systems Observability](https://www.goodreads.com/review/show/3820814357)

## Productivity

-   [芯片工程师的一天 | 我如何每天高效工作12小时？【经验分享】](https://www.youtube.com/watch?v=P4bQEvuNapk)
    一个普通芯片工程师在家高效工作的一天，从早8点到凌晨1点半，分享一下保持高效工作和学习的6个方法和技巧。 欢迎关注我的频道“老石谈芯”，我会持续带来更多专注于芯片的科普、硬核知识、以及偶尔极度硬核的技术分析与解读，我也会不断分享高效工作和学习的方法与技巧。更多内容，也欢迎关注公众号和微博。 公众号：老石谈芯 微博：老石谈芯的老石 Music: Ikson - Paradise

## Computer Setup

-   [Setting up a new machine | Alabê's Blog](https://alabeduarte.com/new-env-setup/)

    Use brew bundle to restore Homebrew packages:

    ```
    $ brew bundle dump --file=Brewfile
    $ brew bundle --file=Brewfile
    ```

-   [How To Use Short Passwords On MacOS Big Sur. 4 Characters Not Required. (Updated) | by CHARLES HEARN | Medium](https://hearnofficial.medium.com/how-to-use-short-passwords-on-macos-mojave-4-characters-not-required-4c66a54183eb)

    ```
    pwpolicy -clearaccountpolicies
    ```

-   [Using Your YubiKey as a Smart Card in macOS – Yubico](https://support.yubico.com/hc/en-us/articles/360016649059-Using-Your-YubiKey-as-a-Smart-Card-in-macOS)

    To turn off the pairing user interface in macOS

    ```
    sc_auth pairing_ui -s disable
    ```

## Economics

-   [Ray Dalio: What I Really Think of Bitcoin](https://www.linkedin.com/pulse/what-i-really-think-bitcoin-ray-dalio)
    -   Bitcoin is one hell of an invention
    -   there being a growing need for money or storehold of wealth assets that are limited in supply
    -   there is also a growing need for assets that can be privately held.

## Bookmarks

-   [Element (Riot.im) | F-Droid - Free and Open Source Android App Repository](https://f-droid.org/en/packages/im.vector.app/)
-   [逆「流」而动——如何建立你的数字音乐收藏](https://sspai.com/post/64819)
-   [spaCy · Industrial-strength Natural Language Processing in Python](https://spacy.io/)
-   [9 件创意好物，情人节送 TA 也能送自己](https://sspai.com/post/64837)
-   [Mecabricks.com](https://www.mecabricks.com/en/) Lego models.

## Funny

-   [@Aaaaaa\_Shu: 已经出现超越 Bitcoin 的代币...](https://twitter.com/ashu_eth/status/1356231490997084160)
-   [@andelf: 给吃货的命令行上手指南](https://twitter.com/andelf/status/1356138271638577152)
