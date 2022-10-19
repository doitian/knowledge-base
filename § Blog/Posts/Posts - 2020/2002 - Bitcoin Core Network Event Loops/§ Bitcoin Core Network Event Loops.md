---
comment: true
date: '2020-02-12T20:22:00+08:00'
katex: false
feature: two-loops.png
banner: "![[two-loops.png]]"
series:
- Bitcoin Core Network
share: true
title: Bitcoin Core Network Event Loops
banner_y: 0.26174
---

# Bitcoin Core Network Event Loops

#blockchain #programming

%%TOC%%

This article is an analysis of the network event loops based on bitcoin core [v0.19.0](https://github.com/bitcoin/bitcoin/tree/v0.19.0).

Bitcoin [starts two threads](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net.cpp#L2211) to handle network messages, and each thread runs its own event loop.

<!--more-->

## Socket Handler Thread

The [Socket Handler Thread](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net.cpp#L1282) is responsible for the underlying socket IO.

It loops each connected peer in a round-robin schedule. The handler reads messages from the peer socket into the receiving queue `vProcessMsg`, and sends message in the sending queue `vSendMsg` to peer.

![[socket-handler.png|Socket Handler]]

### Read from Socket

First, the thread tries to read some data from current peer.

1. [Read some data from socket](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net.cpp#L1338).
2. [Decode the message](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net.cpp#L1343). The newly decoded messages are stored in a queue named `vRecvMsg`.
3. [Move](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net.cpp#L1356) the decoded message in `vRecvMsg` to another queue `vProcessMsg`. The queue `vProcessMsg` is the inbox for the Message Handler Thread.
4. If there is any new decoded message in this loop step, try to [wake](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net.cpp#L1360) the Message Handler Thread.

### Write to Socket

Then, the thread [sends](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net.cpp#L1390) queued messages in `vSendMsg` to current peer.


### Code References

* [`CConnman::Start`](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net.cpp#L2211): This is the main entry to start network threads.
* [`CConnman::SocketHandler`](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net.cpp#L1282): The main logic of Socket Handler Thread.
* [`CNode::ReceiveMsgBytes`](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net.cpp#L565): Decode received bytes into message.

## Message Handler Thread

[Message Handler Thread](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net.cpp#L1978) handles the network messages without worrying the socket operations.

The behavior of the Message Handler Thread is similar to the Socket Handler Thread. Both loops each connected peer in the round-robin way. And for each peer, they first process incoming messages, and then send outgoing messages. The difference is that Message Handler Thread reads messages from the queue `vProcessMsg` and queues outgoing messages in the queue `vSendMsg`.

![[message-handler.png|Message Handler]]

The two loops are connected at these two message queues.

![[two-loops.png|Two Loops are connected on two queues.]]

### Process Incoming Messages

The Message Handler Thread [processes the incoming messages](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net.cpp#L1999) one by one in [the function `ProcessMessage` with a huge switch structure](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net_processing.cpp#L1862).

Each peer acts as a state machine. For some reasons, the state is stored in two different locations.

1. The `CNode` structure, which is passed around as a function parameter, such as `pfrom` in `ProcessMessage`.
2. The `CNodeState` stored in a [global table](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net_processing.cpp#L397).

### Schedule more Outgoing Messages

^a17745

Besides the queued messages acting as responses to the incoming messages, the Message Handler Thread also [schedules more outgoing messages](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net_processing.cpp#L3561).

There are mainly two kinds of outgoing messages in this step:

1. Messages depending on timer, either periodic or the follow ups upon time out.
2. Messages queued and should be sent in batch, such as blocks and transactions announcements.

### Code References

* [`CConnman::ThreadMessageHandler`](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net.cpp#L1978): The Message Handler Thread.
* [`::ProcessMessage`](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net_processing.cpp#L1862): This function processes a single incoming message.
* [`PeerLogicValidation::SendMessages`](https://github.com/bitcoin/bitcoin/blob/1bc9988993ee84bc814e5a7f33cc90f670a19f6a/src/net_processing.cpp#L3561): Check timer and batch queue and schedule more outgoing messages.
