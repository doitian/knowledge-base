---
date: '2020-04-11T21:08:33+0800'
draft: true
---

# Rust Pin

#rust

`Pin` is an obscure type in Rust because of the naming and indirect concepts.

In simple words, Pin is a pointer wrapper. When a pointer is trapped inside Pin, and the pointee type is `!Unpin`, there's no safe way to get a mut reference to the pointee.

<!--more-->



## Further Readings

The [pin module](https://doc.rust-lang.org/std/pin/index.html) document has explained why and the typical scenario.

> It is sometimes useful to have objects that are guaranteed not to move, in the sense that their placement in memory does not change, and can thus be relied upon. A prime example of such a scenario would be building self-referential structs, as moving an object with pointers to itself will invalidate them, which could cause undefined behavior.

`Pin` was suggested in [RFC#2349](https://github.com/rust-lang/rfcs/blob/master/text/2349-pin.md). It was also well explained 

