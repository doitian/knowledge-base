# Cuckoo Hashing

#dataStructure

Cuckoo hashing is a perfect hashing algorithm. It has two tables T1, T2 and uses two different hash functions h1, h2.

If the hash table contains the value v, it is either in `T1[h1(v)]` or `T2[h2(v)]`.

Conflicting is resolved by kicking the existing value to the other table. If conflicting is a loop, choose two new hash functions and rehash all the values.

* 🐘 [Cuckoo Hashing](https://www.evernote.com/l/AAJSqXAAQ05PbYuuASVy0TLpwJGdG_F6QBM)
* [CS166: Data Structures](http://web.stanford.edu/class/cs166/)
