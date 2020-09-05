---
date: '2020-09-05T17:52:10+0800'
---

# Monero Dynamic Block Weight

#blockchain

Monero dynamic block weight is an interesting design. Instead of a fixed supply of transaction space, Monero uses the history blocks to determine the dynamic limit and use the median to control the increasing pace.

<!--more-->

The major reference of this article is chapter 7.3 Money supply in the book *Zero to Monero: Second Edition*.

## Block Weight Limit

The current block's `cumulative_weights_median` is the base limit for the next block. The max block weight of the next block is `2 ∗ cumulative_weights_median` and the block reward decays when the block weight is greater than `cumulative_weights_median`.

/block_reward.png "Block Reward decays when the weight is greater than cumulative_weights_median"

The definition of `cumulative_weights_median`  is

```
cumulative_weights_median = max{
  300kB,
  min{
    max{
      300kB,
      median_100blocks_weights
    },
    50 ∗ effective_longterm_median
  }
}
```

The item `300kB` is the lower bound of `cumulative_weights_median`, which can be removed to simplify the formula.

The term `effective_longterm_median` changes slowly and can be considered as a constant here. It acts as the upper bound.

The value of `cumulative_weights_median` indeed is the median of the last 100 blocks weights clamped between 300kB and `50 * effective_longterm_median`. In turn, the block weight is restricted by `cumulative_weights_median`.

The base limit `cumulative_weights_median` increases when there are at least 50 in the recent 100 blocks which weight is greater than `cumulative_weights_median`, indicating that at least half of the miners are willing to take the block reward penalty. Miners are incentivized to take the penalty because the transaction fees can cover the loss.

If the network runs at full load,  `cumulative_weights_median` doubles every 50 blocks and will reach the upper bound `50 * effective_longterm_median` eventually.

Pay attention that `cumulative_weights_median` falls immediately when the network load drops. If there are 50 in the last 100 blocks which weight is less than 300kB, `cumulative_weights_median` will become 300kB. Maintaining `cumulative_weights_median` at a value higher than 300kB requires continuous transaction traffic. 

/cumulative_weights_median.png "An example of how cumulative_weights_median changes"

## Long Term Limit

The value of `effective_longterm_median` caps the max block weight in the short term. As the name suggests, it is the median of the `longterm_block_weight` of the last 100,000 blocks.

```
effective_longterm_median = max { 300kB, median_100000blocks_longterm_weights }
```

The definition  `longterm_block_weight`  is

```
min { block_weight, 1.4 ∗ previous_effective_longterm_median }
```

The value of `effective_longterm_median` is the median of the last 100,000 blocks weights clamped between 300kB and `1.4 * previous effective_longterm_median`. Same with `cumulative_weights_median`, it increases slowly and drops sharply.
If all the blocks weights are greater than `1.4 ∗ previous_effective_longterm_median`, `effective_longterm_median` rises by 40% every 50,000 blocks.
