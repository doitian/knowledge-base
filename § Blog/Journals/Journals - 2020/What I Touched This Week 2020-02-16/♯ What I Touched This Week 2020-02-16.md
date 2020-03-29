---
date: 2020-02-16
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2020-02-16


## Featured

-   ✒️ [Bitcoin Core Network Event Loops](https://blog.iany.me/2020/02/bitcoin-core-network-event-loops/)

    This is a guide about how bitcoin-core handles network messages in the source code.


-   [The Feynman Technique: How to Learn Anything Quickly ](https://doist.com/blog/feynman-technique/)
    "Why teaching is the key to understanding"

    - Choose a concept to learn
    - Teach it to yourself or someone else
    - Return to the source material if you get stuck
    - Simplify your explanations and create analogies

-   [Podcast Editing Demo - Ferrite + iPad + Apple Pencil ](https://www.youtube.com/watch?v=675gW3a0IAc)
    demonstrates how to edit a podcast on iPad using Ferrite Recording Studio.
    -   [00:59](https://youtu.be/675gW3a0IAc?t=59) Strip silence
    -   [01:39](https://youtu.be/675gW3a0IAc?t=99) ... the stripped silence defaults
    -   [03:42](https://youtu.be/675gW3a0IAc?t=222) Double tap selects everything forward in a single track.
    -   [04:13](https://youtu.be/675gW3a0IAc?t=253) Tapping with two fingers to play and pause
    -   [02:19](https://youtu.be/675gW3a0IAc?t=139) Quick delete with pencil to swipe from right to left

-   [云风的 BLOG: git shallow clone 的一个问题 ](https://blog.codingnow.com/2020/02/git_clone_from_shallow_bundle.html)
    网络抖动和无法断点续传是国内使用 Git 的痛点。之前的做法是服务器上 clone 后把 .git 压缩打包下载回来。随便找了个库对比了下，bzip2 12M, git bundle 11M，打包和恢复速度也快得多。
    -   `git bundle create bundlefile --all`
    -   `git bundle unbundle bundlefile`
    -   git 还不知道是 shallow clone 。好在这个文件很简单，就是 HEAD 的 hash 。手工创建一个就好了。

-   [技术文章配图指南](https://draveness.me/sketch-and-sketch)
    * 选择合适的工具，一定要支持模版或组件库统一配色和风格
    * 直接在配图里添加标题方便单独分
    * 固定宽度，长度可变

## Zero Knowledge Proof

-   [从零开始学习 zk-SNARK（三）——从程序到多项式的构造 - 知乎](https://zhuanlan.zhihu.com/p/102090192)
-   [从零开始学习 zk-SNARK（四）——多项式的约束 - 知乎](https://zhuanlan.zhihu.com/p/103167410)
-   [从零开始学习 zk-SNARK（五）——Pinocchio 协议 - 知乎](https://zhuanlan.zhihu.com/p/103530121)
-   [What are zk-SNARKs? | Zcash](https://z.cash/technology/zksnarks/)
-   [Zero-knowledge proofs, a board game, and leaky abstractions: how I learned zk-SNARKs from scratch](https://medium.com/@weijiek/how-i-learned-zk-snarks-from-scratch-177a01c5514e)

## Programming

-   [After memory safety, what do you think is the next big step for compiled languages to take?](https://graydon2.dreamwidth.org/253769.html)
    -   usable module system
    -   error management
    -   The boundary between synchronous-world and asynchronous world

-   [Write code that is easy to delete, not easy to... — programming is terrible](https://programmingisterrible.com/post/139222674273/write-code-that-is-easy-to-delete-not-easy-to)
    > “Every line of code is written without reason, maintained out of weakness, and deleted by chance” Jean-Paul Sartre’s Programming in ANSI C.

-   [JuliaLang: The Ingredients for a Composable Programming Language](https://white.ucc.asn.au/2020/02/09/whycompositionaljulia.html)
    -   Multiple Dispatch: Open overloading via pattern match

-   [关于 Go1.14，你一定想知道的性能提升与新特性](https://mp.weixin.qq.com/s/8lYuxvAkG9BTGN5_n326Lg)

## Blockchain

-   [Bitcoin’s Initial Block Download](https://blog.bitmex.com/bitcoins-initial-block-download/)
    - Running the scripts is still the bottleneck of IBD.
    - Bitcoin Core 0.12.0 performs well in the above analysis because:
        - libsecp256k is enabled.
        - it does not validate signatures for transaction inputs where the witness is segregated.
-   [P2P Network Guide - Bitcoin](https://bitcoin.org/en/p2p-network-guide)
    -   The primary disadvantage is that the IBD node relies on a single sync node for all of its downloading.
    -   All of these problems are addressed in part or in full by the headers-first IBD method used in Bitcoin Core 0.10.0.

        Sync headers with single sync peers, but download concurrently from multiple peers.

-   [Kevin Wang: Nervos – Scaling Smart Contact Blokchains With Proof of Work and Generalized UTXO](https://epicenter.simplecast.com/episodes/326-gCxdPhtY)
-   [嘉楠耘智一天上涨 82%, 南瓜张邮件透露了什么？](http://mp.weixin.qq.com/s?__biz=MzA4NjUxNTI5Mw==&mid=2649979832&idx=1&sn=b4bc2b40d926962b7e2f9d862c1d29c3&chksm=87c0508ab0b7d99c56c8900570dbab58c056c089c707aa9ce78e0f4730ef50499d273287c9a3&mpshare=1&scene=1&srcid=&sharer_sharetime=1581613933225&sharer_shareid=e7bb68422a42795eb26b0930876fa613)
    -   嘉楠耘智筹备进军基于互联网的算力销售，有的人喜欢把这类业务称为"云算力"

## Productivity

-   [SET 法则：过好每一天的时间管理之道 ](https://sspai.com/post/58761)
-   [RICE: Prioritization for product managers | Inside Intercom ](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/)
    RICE is a scoring system for prioritization
    -   Reach
    -   Impact
    -   Confidence
    -   Effort
    -   How is a RICE score calculated? `RICE = RIC/E`


# COVID-19

-   [经历了这次疫情的考验，这些健康、生活、效率习惯值得你长期坚守 - 少数派](https://sspai.com/post/58811)
    -   "手边常备的健康仪器和药物"
        -   消炎药和抗生素不可混用，抗生素更不可滥用。两者之区别请见 [这篇文章](https://dxy.com/column/2269) 和 [这篇文章](https://dxy.com/column/23368)；
        -   家庭常备、没事儿就翻翻、用药之前先查一下、不要听爸爸妈妈姑姑二大爷老中医建议而是先看一看它的健康资讯来源：[丁香医生](https://dxy.com/)、[腾讯医典](https://baike.qq.com/) 和 [默沙东诊疗手册](https://www.msdmanuals.com/)，三者均有独立 App。
    -   "我最常用的两款电子产品清洁装备是 [iKlear 的清洁套装](https://item.jd.com/57767508229.html) 和 [AM 的清洁套装](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-18497266172.22.20cb6875ILUvEK&id=588092227242)。"
    -   "我推荐每个人都买一个紫外线消毒灯，平时放在没人的房间开上半个小时，杀毒效果极佳。"
-   [家里有孩子，备好这些家庭常备药！ - 丁香医生](https://m.dxy.com/column/1917)
-   [隔离中的“钻石公主号”邮轮](http://mp.weixin.qq.com/s?__biz=MzI2ODExNzg5OQ==&mid=2653626526&idx=1&sn=4fe0eb2554831f35661d892da88fb259&chksm=f12bf27ac65c7b6c1f55adeb6584b0feb2b73b935efbbf6030ec4cc6d884dfaf5c71f65ec4f3&mpshare=1&scene=1&srcid=&sharer_sharetime=1581423277079&sharer_shareid=e7bb68422a42795eb26b0930876fa613)
-   [“亚洲霍乱”背后的恐惧，不止关于死亡](http://mp.weixin.qq.com/s?__biz=MjM5NzIwMTIyMQ==&mid=2650312755&idx=1&sn=02fd6d58479476c5ef241eb06b197ce7&chksm=bed1a41989a62d0f5f144005ea16fa3f8c740b44c6573e5747536fab7bb29656bb0cb1deabd6&mpshare=1&scene=1&srcid=&sharer_sharetime=1581577579468&sharer_shareid=e7bb68422a42795eb26b0930876fa613)
-   [五年远程办公经验告诉你，疫情当前，怎样远程才舒坦？ - 少数派](https://sspai.com/post/58835)
-   [【霍尼韦尔1400021-M-44】EasyChem内置式重型防化服 ](https://i-item.jd.com/100003760180.html)
    P4 防护

## Bookmarks

-   [停工停课不停学，向你推荐 7 门有趣实用的线上课程 - 少数派](https://sspai.com/post/58754)
-   [京东云 不限流量4G路由 吉客猫](https://item.jd.com/100001164126.html)
    - 每天 20G 高速流量 + 20G 中速
    - 30天 79 90天 199 半年 299 一年 499
-   [go.dev](https://go.dev/)
