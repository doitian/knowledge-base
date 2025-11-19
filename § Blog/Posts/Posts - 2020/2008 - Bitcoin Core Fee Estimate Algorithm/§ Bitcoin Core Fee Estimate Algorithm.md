---
date: '2020-08-16T14:38:10+0800'
description: 'An introduction to the fee stimate algorithm in the Bitcoin Core'
tags:
- algorithm
- bitcoin
- fee-market
---

# Bitcoin Core Fee Estimate Algorithm

In bitcoin, the total size of transactions added to the chain in a specific time is limited. This creates a fee market. Transactions with a higher fee rate are likely to be confirmed more quickly. A good fee estimator predicates which fee rate to pay where there is a high probability the transaction will be confirmed into the chain within the target period.

Bitcoin core has the builtin support to estimate the fee rate. Understanding its algorithm can help us to migrate it and improve it.

This first part of this article introduces the core estimation algorithm. The algorithm determines which statistics data to track, and the second part shows how Bitcoin Core tracks them. The last part describes the extensions to the core algorithm for better performance.

<!--more-->

The main reference of the algorithm is the [source code](https://github.com/bitcoin/bitcoin/blob/master/src/policy/fees.cpp) and [the post](https://gist.github.com/morcos/d3637f015bc4e607e1fd10d8351e9f41) from the author.

## The Core Estimation Algorithm

The algorithm must predicate which fee rate to pay where there is a high probability the transaction will be confirmed into the chain within the target period.

The basic idea is checking whether there is **enough fraction** of transactions with **similar fee rate** which has been confirmed within the target period.

### Fee Rate Bucket

Bitcoin groups transactions into different buckets by fee rate to provide statistics for transactions with a similar fee rate.

The buckets are distributed exponentially. The buckets are configured via three parameters:

* U: the first bucket upper bound.
* S: spacing. The latter bucket upper bound is S times of the former bucket upper bound.
* B: the total number of buckets.

The B buckets are separated by B - 1 upper bounds, which split the fee rate range from 0 to infinity into B segments, each segment corresponds to a bucket. The first upper bound is U, and the other bound is S times of its preceding bound.

The following is an example of 4 buckets.

![[fee-rate-buckets.png|Fee Rate Buckets|fit]]

### Confirmation Fraction

Bitcoin tracks the number three kinds of transactions in each bucket to compute the confirmation fraction.

* Unconfirmed: the transactions remained in the memory pool. The lifespan of an unconfirmed transaction is the current chain height minus the chain height when the transaction was added to the pool.
* Confirmed: the transactions included in the chain. The lifespan of a confirmed transaction is the number of the block containing the transaction minus the chain height when the transaction was added to the pool.
* Failed: the transactions removed from the memory pool but not included in the chain. The lifespan of a failed transaction is the chain height when it is removed minus the chain height when it was added.

Further splitting transactions lifespan by the target period X blocks gives the following categories:

* U: Unconfirmed and the lifespan is greater than or equal to X blocks
* C: Confirmed and the lifespan is less than or equal to X blocks
* T: Total number of confirmed transactions
* F: Failed and the lifespan is greater than X blocks.

The confirmation fraction is:

```
Confirmation Fraction = C / (U + T + F)
```

![[confirmation-fraction.png|Confirmation Fraction|fit]]

The estimator needs to find the bucket in which confirmation fraction is larger than a specific threshold.

### Buckets Scan

With the tracking data, the estimation algorithm scans the buckets to find an optimal bucket in which confirmation fraction is larger than a specific threshold for the given confirmation target.

There are two modes to find the optimal bucket which fee rate meets the confirmation target.

* *Greater All Passed* looks for the lowest fee rate that all higher values pass. It starts at the bucket with the highest fee rate and looks at successively smaller buckets until reaching failure. The best bucket is the last passed bucket in the scan.
* *Less All Failed* looks for the highest fee rate that all lower values fail. It starts at the bucket with the lowest fee rate and looks at successively larger buckets until passing the threshold. The best bucket is the last failed bucket in the scan.

Not every bucket has enough data points, Bitcoin will merge consecutive buckets until there are enough transactions, a.k.a, the total number of confirmed transactions are larger than a specific threshold. At the end of the scan, if all the remaining blocks combined have no enough data points, the estimation fails.

![[scan-and-merge.png|Buckets Merge|fit]]

If the found best bucket is a merged bucket range, the one containing the transaction with the median fee rate is selected. And the estimated fee rate is the average fee rate of all the confirmed transactions in the bucket.

![[median-bucket.png|Median Bucket|fit]]

## Tracking

From the analysis in the previous chapter, given a specific bucket, the estimator has to use the following statistic metrics:

* U: Unconfirmed and the lifespan is greater than or equal to X blocks
* C: Confirmed and the lifespan is less than or equal to X blocks
* T: Total number of confirmed transactions
* F: Failed and the lifespan is greater than X blocks.
* R: Sum of fee rates of all the confirmed transactions.

C and R are required to compute the average fee rate in the best bucket which equals to R / C.

For performance issues, Bitcoin tracks up to N blocks and uses a scale S to aggregate data. Pay attention that N and S will be used in the counters defined in the following chapters.

The tracking is performed on each chain height once thus ignores the fork chain which has the same height as a tracked chain.

The estimator needs to monitor following three kinds of events to track the statistics:

* A new block is added to the chain.
* A new transaction is added to the pool.
* A transaction is removed from pool and the reason is not that it has been added to the chain.

### Unconfirmed Transactions

Bitcoin uses a data structure to track the number of unconfirmed transactions for each lifespan between 0 (inclusively) and N (exclusively) and the number of all unconfirmed transactions which lifespan is greater or equal to N. It can give the answer to *U: Unconfirmed and the lifespan is greater than or equal to X blocks*, when X is not greater than N.

To avoid moving data around, the first N counters 0 to N-1 are organized as a ring. Assume that the current chain height is H, the transactions added at the height `H - i` belongs to counter r where r is the remainder after dividing `H - i` by N.

![[tracking-unconfirmed-transactions.png|Tracking Unconfirmed Transactions|fit]]

![[rotating-unconfirmed-transactions-counters.png|Rotating Unconfirmed Transactions|fit]]

The counter N, the last counter, records the number of unconfirmed transactions which lifespan is greater than or equal to N. When a counter in the ring is about to be replaced, the count is added to the counter N.

See `TxConfirmStats::unconfTxs` and `TxConfirmStats::oldUnconfTxs` in the source code.

### Failed Transactions

There are N / S counters, 0 to N/S-1, for each fee rate bucket to track failed transactions number. The counter i tracks the removed transactions in which lifespan is greater than `i * S + 1`. The counter `ceil(X / S) - 1` gives an approximate answer to *F: Failed and the lifespan is greater than X blocks*.

![[tracking-failed-transactions.png|Tracking Failed Transactions|fit]]

The counters are keeping moving average instead of the total count, which means at the beginning of each new chain height, the old counter decays with a configured percentage `decay` which is less than 1.

```
count = count * decay
```

![[decaying-moving-average.png|Decaying Moving Average|fit]]

See `TxConfirmStats::failAvg` in the source code.

### Confirmed Transactions

There are N / S counters, 0 to N/S-1, for each fee rate bucket to track confirmed transactions number. The counter i tracks the confirmed transactions which lifespan is less than or equal to `(i + 1) * S`. The counter `ceil(X / S) - 1` gives an approximate answer to *C: Confirmed and the lifespan is less than or equal to X blocks*

![[tracking-confirmed-transactions.png|Tracking Confirmed Transactions|fit]]

There are two extra counters, one tracks the total number of confirmed transactions and another tracks the total fee rates of all confirmed transactions. They provide answers to *T: Total number of confirmed transactions*, and *R: Sum of fee rates of all the confirmed transactions*.

All the N / S and two extra counters for confirmed transactions, like the failed transactions are keeping the decaying moving average with the same decay percentage.

See `TxConfirmStats::confAvg`, `TxConfirmStats::txCtAvg` and `TxConfirmStats::avg` in the source code.

## Extensions

Bitcoin use three data sets with different scales and maximum tracked confirmations.

* Short: The scale is 1. It tracks 12 blocks and decays the moving average 96.2% on each new height.
* Med: The scale is 2. It tracks 48 blocks and decays the moving average 99.52%.
* Long: The scale is 24. It tracks 1008 blocks and decays the moving average 99.931%.

Longer time horizon can estimate the fee rate with a high confirmation target but is less accurate for a low target.

Given a required confirmation target X, bitcoin chooses the data set with the shortest tracking confirmations which are greater than or equal to X. For example, it uses Short when X is 12, and Med when X is 13.

The first extension, named as `estimateCombinedFee`, is that Bitcoin also checks the shorter time horizons and gives the lowest estimation as the answer. For example, when X is 49, the estimator will run the core algorithm three times:

* Uses data set Long with target 49
* Uses data set Med with target 48
* Uses data set Short with target 12.

The second extension is that Bitcoin will run `estimateCombinedFee` with 3 different configurations and return the largest estimation given the confirmation target X.

* Half Estimation runs `estimateCombinedFee` with confirmation target X/2 and confirmation fraction threshold 60%.
* Actual Estimation runs `estimateCombinedFee` with confirmation target X and confirmation fraction threshold 85%.
* Double Estimation runs `estimateCombinedFee` with confirmation target 2X and confirmation fraction threshold 95%.
