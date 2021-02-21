---
date: 2021-02-21
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2021-02-21

I published 2 posts:

* [[♯ Install macOS Big Sur in 2021]]
* [[♯ SSH Authentication Using a YubiKey on Windows And the OpenSSH Client]]

During the holiday, I have migrated my information hub from Diigo to Readwise.

<!--more-->

┌ [Reclipped](https://www.reclipped.com/)

Reclipped is a tool to take timestamped notes on videos. It supports popular video platforms, such as YouTube and Vimeo.

┌ Hashed and Hierarchical Timing Wheels

Keeping a lot of timers is a common problem in many distributed system. The paper “Hashed and Hierarchical Timing Wheels: Data Structures for the Efficient Implementation of a Timer Facility – Varghese & Lauck 1987” has listed 7 data structures and recommended the last two: Hashing Wheel with Unordered Timer Lists and Hierarchical Timing Wheels.

The morning paper has a good [summary](https://blog.acolyer.org/2015/11/23/hashed-and-hierarchical-timing-wheels/) and [this video](https://reclipped.com/docs?q=uri:https:%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DAftX7rqx-Uc) have listed several implementations.

┌ [How to Efficiently Choose the Right Database for Your Applications](https://en.pingcap.com/blog/how-to-efficiently-choose-the-right-database-for-your-applications)

In this post, the author shared two decision trees to choose SQL and NoSQL databases. He also shared some tips for choosing a database.

┌ [How to Craft the Perfect Daily Schedule (According to Science)](https://blog.doist.com/daily-schedule/)

Know your energy pattern and match your tasks to your energy.

┌ [Mutation Driven Testing – When TDD Just Isn’t Good Enough](https://software.rajivprab.com/2021/02/04/mutation-driven-testing-when-tdd-just-isnt-good-enough/)

Write tests and ensure they all pass.

Repeat following procedure:

* Mutate the code to introduce some bugs.
* Check whether the bug is captured by test. If not, modify the existing test cases or add new ones.
* Revert the bugs and ensure test is green again.

┌ [Fail at Scale - ACM Queue](https://queue.acm.org/detail.cfm?id=2839461)

Ben Maurer shared several software reliability techniques used in Facebook.

┌ [Writing a Time Series Database from Scratch](https://fabxc.org/tsdb/)

Fabian Reinartz introduced how he designed the V3 storage structure of Prometheus.

The essential of the design is splitting the data by time ranges.
