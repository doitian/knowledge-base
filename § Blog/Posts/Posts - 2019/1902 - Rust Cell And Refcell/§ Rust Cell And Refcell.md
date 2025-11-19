---
comment: true
date: 2019-02-24 07:35:47
description: Talk about the differences between Cell and RefCell in Rust, and how to use them.
katex: false
share: true
title: Rust Cell and RefCell
tags:
- memory-management
- rust
---

# Rust Cell And Refcell

In Rust document, *Cell* is “A mutable memory location”, and *RefCell* is “A mutable memory location with dynamically checked borrow rules”.

They both provide “interior mutability”, where you can modify the value stored in cell via immutable reference of the cell.

They both have an API `get_mut` to return a mutable reference to the underlying data. This method requires a mutable reference to the cell, which guarantees that the callee has exclusive ownership of the cell.

```rust
pub fn get_mut(&mut self) -> &mut T
```

The difference is how they implement interior mutability. *Cell* copies or moves contained value, while *RefCell* allows both mutable and immutable reference borrowing. I will try to explain the difference via their APIs in this article.

<!--more-->

## Cell

In the old version of Rust, *Cell* requires the wrapped type to be *Copy*. Many articles still contain such outdated and misleading information. Indeed *Cell* has two different sets of APIs in a newer version.

The first set is the Copy API. It requires a *Copy* wrapper, and contains methods `get` and `set`.  The method `get` returns a copy of the contained value, and `set`  stores a copy of the argument `val` as the new value.

```rust
// impl<T: Copy> Cell<T>
pub fn get(&self) -> T

// impl<T> Cell<T>
pub fn set(&self, val: T)
```

Another set is the Move API. It has two methods `take` and `set`. The method `take` moves out the contained value, leaving `Default::default()` in its place. The call `set` also works for non-copyable type, where it moves the argument into the cell.

```rust
// impl<T: Default> Cell<T>
pub fn take(&self) -> T

// impl<T> Cell<T>
pub fn set(&self, val: T)
```

The method `replace` is an alternative of `take`, when `T` does not implement *Default* or the new value is known in advance when taking the value.

```rust
// impl<T> Cell<T>
pub fn replace(&self, val: T) -> T
```

An important property of *Cell* is that the cell cannot tell you what's contained in the cell via a reference. You either copy the contained value, or modify the cell and move out the value.

## RefCell

*RefCell* allows borrowing immutable or mutable reference to the contained value. It tracks the borrows at runtime, via `borrow` and `borrow_mut`.

```
pub fn borrow(&self) -> Ref<T>
pub fn borrow_mut(&self) -> RefMut<T>
```

The method `borrow` grants temporary access to the contained value via immutable reference. Multiple immutable borrows can be taken out at the same time. It panics if the value is currently mutably borrowed.

The API `borrow_mut` mutably borrows the wrapped value. It panics if the value is currently borrowed, either mutably or immutably.

The runtime tracking certainly has overheads, and `RefCell` also can lead to runtime panics.
