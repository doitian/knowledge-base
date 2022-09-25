# Integer Longest Common Prefix

#algorithm

```
lcp(m, n) = w - 1 - msb(m xor n)
```

where w is the number of bits in a word, and `msb` is [[§ Most-Significant Bit]].
