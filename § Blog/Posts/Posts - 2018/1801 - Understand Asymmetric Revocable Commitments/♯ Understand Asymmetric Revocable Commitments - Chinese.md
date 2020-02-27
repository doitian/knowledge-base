---
comment: true
date: 2018-01-14 07:44:51
description: 通过一步一步分析每一步可能的结果，理解 Asymmetric Revocable Commitments 工作原理
katex: false
share: true
title: 理解 Asymmetric Revocable Commitments
---

# Understand Asymmetric Revocable Commitments

#blockchain

Asymmetric Revocable Commitments 是 Lighting Network 的基础，是非对称加密技术很巧妙的应用。它用于互不信任的双方在链下通过协商完成一系列交易。最终需要提交到链上的只需要最初的创建和最后的结算两个交易，大大提高了交易处理速度。

<!--more-->

Wikipedia 上有[介绍和例子]([Lightning Network - https://en.wikipedia.org/wiki/Lightning_Network)。一开始比较懵的是，如果交易可以被 Revoke，一方可以拿走所有资金，为什么不直接提交 Revoke 交易呢？而一系列的交换可以把整个系统当作状态机。如果把每个步骤完成后双方可以做的事，以及最终导致的结果列出来，就可以弄明白为什么了。因为 Revoke 的前提是它对应的交易被提交到链上被执行后才行，而那个交易是自己单方签名后提交给对方的，只有对方才能构造出并提交的。这样 Revoke Key 的作用就是监听链上的交易，一旦发现它对应的交易，马上 Revoke 它已获得所有的资金。

通过分析也立即明白了在哪些步骤上是有风险的，安全上需要注意什么。

交易是由买方提起的，买方会提议新的资金划分，把本次交易需要的资金划分给对方，这时对方是可以直接把这个交易提交到链上执行的，简单说就是卖方可以收了钱不发货。可见 Lighting Network 适合高频小额的场景，如果是价值很高，而且不可拆分是不适合使用 Lighting Network 的。

在安全性方面：

- 生成 Revoke Key 的一方必须妥善保管并备份，并做好保密工作，不过一旦给对方后就可以忘记了。而一旦给对方后，对应的交易如果已经签好名并保存了就不能泄露出去，不然对方可以拿去提交然后 Revoke。
- 所有接收到的 Revoke Key 都必须保存起来并备份。同时需要监听链上交易随时行使 Revoke 的权利。


原始笔记如下

``` text
## Initial

### Alice closing (A1)

- Alice: $5 1000 blocks later
- Bob: $5 immediately

### Bob closing (B1)

- Alice: $5 immediately
- Bob: $5 1000 blocks later

## Alice offers $1 payment

### Alice closing (A1)

- Alice: $5 1000 blocks later
- Bob: $5 immediately

### Bob closing (B2)

- Alice: $4 immediately
- Bob: $6 1000 blocks later

Bob can close the channel and get the payment. Alice can get remainder immediately but cannot cancel the payment. But Bob cannot trust the payment yet, since Alice can broadcast the state before the payment first.

## Bob replies the payment

### Alice closing (A2)

- Alice: $4 1000 blocks later
- Bob: $6 immediately

Alice has no reason to broadcast it, since she has a better state of 5:5 split.

### Bob closing (B2)

- Alice: $4 immediately
- Bob: $6 1000 blocks later

## Alice give revocation key to Bob

Bob knows the revocation key, so Alice cannot broadcast prior state A1

- Alice: $5 1000 blocks later
- Bob: $5 immediately

Since Bob can revoke Alice $5 immediately before Alice spend it after 1000 blocks.

Bob ensures he owns $6 now.

## Bob give revocation key to Alice
Although Bob unlikely broadcast its B1 now, but it may become better state for him later, so Bob should also invalidate it by give revocation key to Alice.
```
