---
date: '2020-04-11T21:08:33+0800'
draft: false
description: "Pin is a pointer wrapper. When a pointer is trapped inside Pin, and the pointee type is !Unpin, there's no safe way to get a mut reference to the pointee."
---

# Rust Pin

#rust

`Pin` is an obscure type in Rust because of the naming and indirect concepts.

The first indirect concept is pointer. `Pin<X>` does not guarantee that X will not move. If X is a pointer which target type is T, `Pin<X>` guarantees that T will not move.

The second is "not move". It really means that the only way to get the mut reference to T is via unsafe interface.

The last is the `Unpin` mark trait. Pin forbids safe interface to get the mut reference to T only when T is `!Unpin`.

In simple words, Pin is a pointer wrapper. When a pointer is trapped inside Pin, and the pointee type is `!Unpin`, there's no safe way to get a mut reference to the pointee.

<!--more-->

The following diagram has listed what Pin provides and constraints on when we can use those functions.

/Rust Pin.png

In Rust, the pointer is indeed the trait `Deref` and `DerefMut`, from which we can get the shared or mut reference.

It is not very interesting when the pointer is `Deref`. The essential of Pin is when X is `DerefMut`. The yellow box shows that the safe interface to get the mut reference is available when T is `Unpin`.

`Unpin` is implemented for types by default. It acts as a safety which disables the core feature of Pin. Pin is only effective when the safety is turned off, a.k.a, when the type is explicitly marked as `!Unpin` via [PhantomPinned](https://doc.rust-lang.org/std/marker/struct.PhantomPinned.html).

Pin is a singal that a self reference type may appear here. It is also a contract. The type provider must mark the type as `!Unpin` if it is unsafe to move. The type user must promise not to move the `!Unpin` data in the unsafe block.

## Further Readings

The [pin module](https://doc.rust-lang.org/std/pin/index.html) document has explained why and the typical scenario.

> It is sometimes useful to have objects that are guaranteed not to move, in the sense that their placement in memory does not change, and can thus be relied upon. A prime example of such a scenario would be building self-referential structs, as moving an object with pointers to itself will invalidate them, which could cause undefined behavior.

`Pin` was suggested in [RFC#2349](https://github.com/rust-lang/rfcs/blob/master/text/2349-pin.md). It was also well explained in the book [Futures Explained in 200 Lines of Rust.](https://cfsamson.github.io/books-futures-explained/4_pin.html)



