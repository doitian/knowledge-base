# Integer Longest Common Prefix

#algorithm

```
lcp(m, n) = w - 1 - msb(m xor n)
```

where w is the number of bits in a word, and `msb` is [♯ Most-Significant Bit](ia-writer://open?path=/Locations/iCloud/§%20Tickler/Tickler-M/Most-Significant%20Bit/♯%20Most-Significant%20Bit.md).
