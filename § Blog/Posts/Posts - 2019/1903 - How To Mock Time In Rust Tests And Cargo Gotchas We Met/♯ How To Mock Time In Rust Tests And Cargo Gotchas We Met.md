---
comment: true
date: 2019-03-31 06:22:22
description: I'm working in a team developing a big Rust project recently. The project has some features depending on time. We, the developers, want to be able to mock the time in test. In this post, I'll talk about the problems we have met, mostly related to Cargo.
katex: false
share: true
title: How to Mock Time in Rust Tests and Cargo Gotchas We Met
---

# How To Mock Time In Rust Tests And Cargo Gotchas We Met

#rust #cargo

How to mock time in Rust tests and Cargo gotchas we met.
I'm working in a team developing a big Rust project recently. The project has some features depending on time. We, the developers, want to be able to mock the time in the test. In this post, I'll talk about the problems we have met, mostly related to Cargo.

<!--more-->

I have created a GitHub repository [doitian/rust-mock-time-demo](https://github.com/doitian/rust-mock-time-demo), which contains all the following examples.

## The First Attempt
The requirement looks straightforward at first glance since Rust supports [conditional compilation](https://doc.rust-lang.org/book/conditional-compilation.html) and cfg `test` is only active in the test. We can implement a function telling us current time, and the whole program must fetch the current time from it. The function has two different versions, in the non-test code, it just returns the real current time. In the test, it is possible to mock the current time through a thread local variable.

```rust
/// cfg-test/src/main.rs
use std::thread;
use std::time::{Duration, SystemTime, SystemTimeError};

#[cfg(not(test))]
pub fn now() -> SystemTime {
    SystemTime::now()
}

#[cfg(test)]
pub mod mock_time {
    use super::*;
    use std::cell::RefCell;

    thread_local! {
        static MOCK_TIME: RefCell<Option<SystemTime>> = RefCell::new(None);
    }

    pub fn now() -> SystemTime {
        MOCK_TIME.with(|cell| {
            cell.borrow()
                .as_ref()
                .cloned()
                .unwrap_or_else(SystemTime::now)
        })
    }

    pub fn set_mock_time(time: SystemTime) {
        MOCK_TIME.with(|cell| *cell.borrow_mut() = Some(time));
    }

    pub fn clear_mock_time() {
        MOCK_TIME.with(|cell| *cell.borrow_mut() = None);
    }
}

#[cfg(test)]
pub use mock_time::now;
```

Let's try it in both `cargo run` and `cargo test`:

```
cargo run -p cfg-test
cargo test -p cfg-test
```

Work as expected, let's call it a day.

## Gochas of cfg test

However, we immediately found the issue when we try to add the mockable `now` into the project. The project is complex and organized into many crates, so we create a crate for this utility as well. However, the compiler complains that it cannot find the function `mock_time::set_mock_time` when using the `cfg(test)` only functions in the test in another crate.  Since Cargo builds each file under tests directory in a standalone crate, see how it can reproduce the issue, see `cfg-test/tests/test_mock_time.rs` reproduces this issue using the command below

```
RUSTFLAGS='--cfg cfg_test_crate_tests' cargo test -p cfg-test
```

The cause is that `cfg(test)` does not pass though dependencies. The crate `test_mock_time` in tests is built with `cfg(test)`, but in its dependency, the crate `cfg-test` , `cfg(test)` is not set. In simple words, `cfg(test)` is only set for the crate current in test.

## Feature

"Feature" is a well-known feature of Cargo, where a crate can customize how to build its dependencies. It is easy to switch to feature, just change `cfg(test)` to `cfg(feature = "...")`, for example:

```rust
use std::time::SystemTime;

#[cfg(not(feature = "mock-time"))]
pub fn now() -> SystemTime {
    SystemTime::now()
}
```

The full example is in the `cfg-feature-lib` directory in the repository.

Since the feature does not turn on in test automatically, we have to remember to enable the feature when running test. What's worse, the command line argument `--features` does not pass to workspace members, it is only for the top project. Take the repository as an example:

Running following command in the top directory does not enable feature `mock-time` in `cfg-feature-test-manual` crate.

```
cargo test --features mock-time -p cfg-feature-test-manual
```

Instead, it must be executed inside `cfg-feature-test-manual`:

```
cd cfg-feature-test-manual && cargo test --features mock-time
```

After research, a trick comes out, which adds the dependency in both `dependencies` and `dev-dependencies`. The feature is only enabled in `dev-dependencies`. See example `cfg-feature-test-auto/Cargo.toml`.

```
[dependencies]
cfg-feature-lib = { path = "../cfg-feature-lib" }

[dev-dependencies.cfg-feature-lib]
path = "../cfg-feature-lib"
features = ["mock-time"]
```

We expect that `mock-time` is automatically enabled in tests, but it turns out to be where weird things happen.

In simple words:

- If the top workspace project has added the conditional dependencies in Cargo.toml, than the feature is always enabled, no matter in tests or final executables. See a demo in [this PR](https://github.com/quake/cargo-test/pull/1).
- If the top workspace does not have such trick, then cargo behaves differently when whether `--all`  is specified or not. [Another PR](https://github.com/quake/cargo-test/pull/2) demonstrates this.

The feature based solution also has a inconvenient drawback. The feature can only be passed from a crate to its direct dependencies. To allow the time mock, a crate must be aware of whether its dependency depending on `time` directly or indirectly.

For example, if the crate `time` has a feature `mock-time`, and

- package foo depends on bar, and bar depends on time.
- package root depends on foo, bar and time.

Then here is what root's `Cargo.toml` looks like:

```
[dependencies]
foo = "0.1.0"
bar = "0.1.0"

[features]
mock-time = ["foo/mock-time", "bar/mock-time", "time/mock-time"]
```

# Final Solution
Because of the weird behavior of  `--all`, and how disturbing to set up the feature chain between dependencies, we decide to adopt `RUSTFLAGS`. Indeed, I have used it once in an example above. `RUSTFLAGS` is automatically enabled for all crates, no matter how deep the dependency is.

However, there is another gotcha about `RUSTFLAGS`. The doc test does not observe `RUSTFLAGS`, it uses `RUSTDOCFLAGS`.

We have built a crate [faketime](https://github.com/nervosnetwork/faketime) from our experiences. Take a look if you are interested in mocking time in tests.
