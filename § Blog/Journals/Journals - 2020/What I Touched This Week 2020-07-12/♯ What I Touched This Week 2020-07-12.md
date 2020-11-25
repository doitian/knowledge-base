---
date: 2020-07-12
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2020-07-12

I have posted [♯ Yubico for Windows](ia-writer://open?path=/Locations/_Publish/§%20Blog/Posts/Posts%20-%202020/2007%20-%20Yubico%20for%20Windows/♯%20Yubico%20for%20Windows.md).

I have finished the book [Regretting You](https://www.goodreads.com/review/show/3149842860).

<!--more-->

## Tacit Knowledge

I have read [a series about tacit knowledge](https://commoncog.com/blog/the-tacit-knowledge-series/) by Cedric Chin recently.

> The sort of tacit knowledge [the author is] interested in is that of ‘expert intuition’.

In the second post, the author has introduced the Recognition-Primed Decision Making Model.

* Recognition of goals, cues, expectancies and actions.
* Perform the actions if there's a pattern match. If there are several candidates, people usually try them one by one and adopt the first one which meets all the requirements.
* If the pattern is abnormal, analyze and collect more data and rerun the loop.

## Tech

┌ Programming

* [Ringbahn II: the central state machine](https://without.boats/blog/ringbahn-ii/)

    Last time I wrote about ringbahn, a safe API for using io-uring from Rust. I wrote that I would soon write a series of posts about the mechanism that makes ringbahn work. In the first post in that series, I want to look at the core state machine of ringbahn which makes it memory safe.

┌ Blockchain

* [RFC: Swappable Signature Verification Protocol Spec - English / Development & Technical Discussion - Nervos Talk](https://talk.nervos.org/t/rfc-swappable-signature-verification-protocol-spec/4802)

    This proposal describes a solution to decouple the lock script app logic and signature verification logic.

* [Bitcoin Optech Newsletter #105 | Bitcoin Optech](https://bitcoinops.org/en/newsletters/2020/07/08/)

    * Prevent network topology leaks by [caching responses to `getaddr`](https://bitcoincore.reviews/18991).
    * [Bitcoin Core #19204](https://github.com/bitcoin/bitcoin/issues/19204) eliminates a source of wasted bandwidth during Initial Block Download (IBD) by setting `feefilter`.

┌ Security

* [maxgoedjen/secretive: Store SSH keys in the Secure Enclave in macOS](https://twitter.com/doitian/status/1280115029967241221)

┌ Apps

* [How Did Vim Become So Popular](https://pragmaticpineapple.com/how-did-vim-become-so-popular/)
* [6 Google Sheets functions that do more than math](https://zapier.com/blog/google-sheets-functions/)

    My picks

    * Google translate: `=GOOGLETRANSLATE("A2", "fr", "es")`
    * Import HTML and RSS:
      * `=IMPORTHTML("https://en.wikipedia.org/wiki/List_of_most_popular_given_names", "table", 3)`
      * `=IMPORTFEED("https://rss.nytimes.com/services/xml/rss/nyt/PersonalTech.xml")`
    * Embedded line chart: `=SPARKLINE(B3:B22)`

┌ Software Engineer

* [Blog: Failing (and winning) at planning software projects](https://simplabs.com/blog/2020/06/17/failing-and-winning-at-planning-software-projects/)

    When it comes to planning software projects on the macro level, there's two extremes – trying to plan everything up-front or accepting the impossibility of getting that right and not bothering to plan anything at all.


## Non-tech

┌ Social

* [Welcome to the 21st Century](https://www.oreilly.com/tim/21stcentury/)

    > The choices our societies make now can have an enormous impact on the course of the next few decades.

┌ Productivity

* [Which Productivity Method is Right For You? A Complete List + Quiz](https://todoist.com/productivity-methods)
* [The 35 Best Productivity Apps for 2020 (By Category)](https://doist.com/blog/best-productivity-apps/)
* [The Technium: 68 Bits of Unsolicited Advice](https://kk.org/thetechnium/68-bits-of-unsolicited-advice/)
* [Are You Wasting Time On A Bullet Journal? | by Chris Kyle | Medium](https://medium.com/@ChrisKyle/are-you-wasting-time-on-a-bullet-journal-a93b46c8e929)

┌ Life

* [挑选一台字体显示效果出色的显示器，要注意哪些问题？](https://sspai.com/post/61252)

## Interesting

* [@ThingsWork: This is how cartoons used to be made](https://twitter.com/doitian/status/1281680744062971904)
* [@CNqdsoa: 开了小二十年车了从来没见过这么牛逼的操作目瞪口呆…](https://twitter.com/doitian/status/1280889440261398531)
* [@xds2000: 这真是巧劲](https://twitter.com/doitian/status/1280467027212349440)

## Bookmarks

* [Home - Canva](https://www.canva.com), a design tool with a lot quick started templates.
* The macOS apps which can control the external displays.
  * [Lunar](https://lunar.fyi)
  * [MonitorControl: ](https://github.com/MonitorControl/MonitorControl)
* [mermaid - Markdownish syntax for generating flowcharts, sequence diagrams, class diagrams, gantt charts and git graphs.](https://mermaid-js.github.io/mermaid/)
* [HackMD - Collaborative Markdown Knowledge Base](https://hackmd.io)
* [Semantic Scholar | AI-Powered Research Tool](https://www.semanticscholar.org)
