---
comment: true
date: 2018-07-19 01:24:39
description: ''
katex: false
series:
- Blockchain Projects Review
share: true
title: Decred Review
---

# Decred Review

#blockchain

[Official References](https://docs.decred.org/research/overview/)

- Based on Bitcoin
- PoS overlays upon PoW
- Add signature algorithms Ed25519 and Schnorr
- Use BLAKE-256 as hash algorithm
- Enable segwit to solve transaction malleability
- Transaction expiration mechanism

## Hybrid Consensus

[Decredible | Decred hybrid consensus explained](https://decredible.com/mining/hybrid-consensus/)

- PoW miners propose new block.
- PoS miners vote whether accepting the block. The ticket should be purchased first. 5 tickets are selected randomly using the new PoW block header. Block is accepted if 3 tickets agree.
- Block reward is split between PoW and PoS miners.
- PoS tickets are selected using PoW block header. It guaranteed that is has a very high cost to manipulate picking tickets.
