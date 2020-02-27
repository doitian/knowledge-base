---
comment: true
date: '2017-08-19T23:41:07+08:00'
description: "How to use Redis as Write Buffer, and how to savely flush cached data to backend storage and remove cache from Redis."
share: true
title: Redis as Write Buffer
---

# Redis as Write Buffer

#redis

It is common to use Redis as read buffer。To read data, first check whether it exists in Redis. If so, use the cached data, otherwise read from the backend storage and save a copy into Redis. To write data, first save into backend storage, then clear or update Reids cache.

But if the system bottleneck is in writing, the solution above does not work. But it is easy to modify it into a write buffer.

<!--more-->

- Read: Check whether the data exists in Redis. Read from backend storage if not.
- Write: Just write into Redis. Notify background worker via message queue to flush the cache into backend storage.
- The background worker watches message queue, save data and delete from Redis.

The message queue can be implemented using Redis LIST. Official [RPOPLPUSH – Redis](https://redis.io/commands/rpoplpush) command document already described how to implement a reliable queue. The remaining issue is how to safely delete saved data from Redis.

The save step can be split into:

1. Read from Redis.
2. Save into backend storage.
3. Delete from Redis.

If new change comes between 1 and 3, the change is discarded in step 3. It must be resolved using lock, or transaction.

After research, it is a bit complex to [implement a lock](https://redis.io/topics/distlock). Fortunately, it is easy to use transaction.

Redis provides `MULTI`  and  `EXEC` to wrap several commands into a transaction. Although it does not support rollback on error, it guarantees that either none of the commands are executed, or all of them have been executed. Command  `WATCH` can monitor the changes on a key. If the key changes after `WATCH` and before executing the transaction, the transaction is cancelled. See details in official document [here](https://redis.io/topics/transactions). So the save step can be implemented in following steps:

1. `WATCH` the key to flush
2. Read from Redis.
3. Save into backend storage.
4. Wrap command in `MULTI`  and  `EXEC`  to delete the key from Redis

Pseudocode：

```
redis.send('WATCH', key)
data = redis.get(key)
database.save(key, data)
redis.send('MULTI')
redis.send('DEL', key)
redis.send('EXEC')
```
