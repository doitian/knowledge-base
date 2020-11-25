---
date: 2020-08-29
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2020-08-29

I did research on Blockchain timestamp and timejacking attack last week.

I have completed the course [Stanford CS166](http://web.stanford.edu/class/cs166/) and shared [my notes](https://www.dropbox.com/sh/xztn2u8wq0x1n52/AADHN-itkC2jAEQTvr0e3KwFa?dl=0) via Evernote.

<!--more-->

## Blockchain Timestamp Research

* [Discussion on CKB Block Timestamp Improvements](https://talk.nervos.org/t/discussion-on-ckb-block-timestamp-improvements/4916)

* [Bitcoin’s Block Timestamp Protection Rules | BitMEX Blog](https://blog.bitmex.com/bitcoins-block-timestamp-protection-rules/)

    * Two hours is only a small fraction of the difficulty adjustment cycle, two weeks.

* [culubas: Timejacking & Bitcoin](http://culubas.blogspot.com/2011/05/timejacking-bitcoin_802.html)

    * Block timestamp is valid if
        * it is greater than median of previous 11 blocks
        * it is less than or equal to network time + 2h
    * Network time = local time + median offset from 5~200 peers
        * Max allowed adjustment is 70 minutes.
    * "Poison Pill" Block
        * Make a group of nodes 70 minutes faster, the target 70 minutes slower. That's a 140 minutes gap, and the max allowed future block time offset is 2 hours.
    * Solutions
        * Use the node's system time instead of the network time to determine the upper limit of block timestamps and when creating blocks.
        * Tighten the acceptable time ranges.
        * The node's network time could be restricted to a value within 30 minutes.
        * Use only trusted peers.
        * Use the median block chain time exclusively when validating blocks.

## Blockchain

* [wallet - What's the most efficient way to create a raw transaction with a specific fee rate? - Bitcoin Stack Exchange](https://bitcoin.stackexchange.com/questions/98392/whats-the-most-efficient-way-to-create-a-raw-transaction-with-a-specific-fee-ra)

    Coin selection algorithms.

* [探索 DeFi 世界下一个宝藏领域：加密原生保险的机遇和挑战](https://mp.weixin.qq.com/s/OBlZEYmrr8HoP1vA7z21Ig)

    >  「投机」在这里具备积极的社会意义：有助于为寻求「真实」投保范围的人实现流动市场的**冷启动**，并为不同 DeFi 元素的安全性提供了**晴雨表**。

* [探索流动性挖矿的设计空间](https://mp.weixin.qq.com/s/PymTIDU7LnWQU8_YZIdEDQ)

    * 谁获得奖励
    * 他们都获得多少奖励
    * 他们什么时候获得奖励

* [2020年币圈下半场投资主题：公链的桥化和侧链化趋势](https://mp.weixin.qq.com/s/wFEhOJSs2cZrfojRJY2htg)

* [以太坊免费时代之死：智能钱包的机遇和挑战](https://mp.weixin.qq.com/s/_vj2TDc-lMXsm0rZArNAbw)

## Productivity

* [Productivity Advice, Based on Your Enneagram Personality Type](https://doist.com/blog/enneagram-and-work/)

## Interesting

* [This equation will change how you see the world (the logistic map)](https://www.youtube.com/watch?v=ovJcsL7vyrk)

## Bookmarks

* [Ikea and Lego built the storage boxes of your dreams](https://www.theverge.com/2020/8/27/21403760/ikea-lego-storage-boxes-bygglek-availability)
* [返校季 | 有壶热水就能做，顶饱又方便的宿舍美食](https://sspai.com/post/62286)
* [比奶茶和快乐水更清凉低卡，用这杯冷泡茶留住你的夏天 - 少数派](https://sspai.com/post/62308)
