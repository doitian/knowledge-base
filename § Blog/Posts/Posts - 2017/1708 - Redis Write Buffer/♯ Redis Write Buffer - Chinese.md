---
comment: true
date: '2017-08-19T23:41:07+08:00'
description: 如何使用 Redis 作为写缓存，如何安全地把缓存内容保存并删除
share: true
title: Redis 写缓存
---

# Redis Write Buffer

#redis

Redis 比较常见的是作为读缓存。读取数据的时候检查 Redis 是否存在，存在的话缓存命中，不需要访问后端存储。没命中的话从后端存储中获得，并同时存入 Redis。写数据的时候直接写入后端存储，清除 Redis 中对应的缓存或者更新成新的值。这种模型可以安全的随时删除缓存中的内容而不会造成数据丢失，因为最新的数据一定是写入到后端存储里了。

但如果系统的瓶颈出现在了写入这块，上面的模型就没法解决了。稍加修改可以得到写缓存的模型：

- 读的时候检查 Redis，如果 Redis 存在直接使用 Redis 中的数据，否则从后端存储中读取。
- 写的时候只写入 Redis，通过消息队列通知后台任务把 Reids 中缓存的内容保存到后端存储中。
- 后台任务监听消息队列，在把缓存内容保存成功之后从 Redis 中删除对应的内容。

任务队列可以使用 Redis 的 LIST 来实现，官方的 [RPOPLPUSH – Redis](https://redis.io/commands/rpoplpush/) 命令文档中已经很详细描述了如何实现一个可靠的消息队列。于是剩下的问题就是如何能保证安全的删除已经保存过的缓存？

<!--more-->

保存缓存的步骤肯定是

1. 从 Redis 中读取
2. 把读取的内容写入后端存储
3. 从 Redis 中删除

而如果在 1 和 3 之间，又有新的修改写入，这些修改就因为第 3 步的执行丢失了。要解决这个问题要么就是加锁，要么是通过事务。

研究了一番以后，要[实现锁](https://redis.io/docs/reference/patterns/distributed-locks/)会比较复杂，而通过事务就比较简单了。

Redis 提供了 `MULTI` 和 `EXEC` 将多个命令提交为一个事务。虽然不提供错误回滚，但保证了要么命令都没执行，要么都执行了。而命令 `WATCH` 可以用来监控某个键，如果在执行 `WATCH` 之后到执行事务之前，这个键里的值有所变化，事务将被取消，详情可以查看[官方文档](https://redis.io/topics/transactions)。因此保存缓存的步骤改写成：

1. `WATCH` 要保存的 key
2.  从 Redis 中读取
3. 把读取的内容写入后端存储
4. 使用 `MULTI`  和 `EXEC` 包围从 Redis 中删除该 key 的语句

伪代码如下：

```
redis.send('WATCH', key)
data = redis.get(key)
database.save(key, data)
redis.send('MULTI')
redis.send('DEL', key)
redis.send('EXEC')
```
