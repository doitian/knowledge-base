---
date: '2020-10-11T12:03:32+0800'
draft: false
---

# Gotchas to Publish Rust Crates in a Workspace

#rust

It is recommended to split a huge Rust project into crates and manage them in a workspace. I'm currently working on a project which consists of about 60 crates. It works well so far until I try to publish these crates to crates.io.

I will list the problems I have met and solutions or workarounds I have adopted.

<!--more-->

## Update *Cargo.toml*

Crates.io has some requirements on Cargo.toml files:

* Fields like license, authors, description, homepage, and repository are required.
* Local crates via `path` must specify the version as well so the dependencies can be resolved via crates.io.

The command `cargo publish --dry-run` will verify whether the file Cargo.toml is valid.

## There's No `cargo publish --all`

Cargo [does not support publishing all local packages yet](https://github.com/rust-lang/cargo/issues/1169). It means that I have to cd into each crate and publish them separately.

There are two major issues here.

The first, if a crate `foo` depends on `bar`, a version of `bar` satisfying `foo`'s requirement must be available in crates.io before publishing `foo`. In the project I'm working on, all crates share the same version, and they lock the local dependencies using the exact version such as `bar = "= 0.0.1"`. If I want to publish these crates, I must topologically sort them by dependencies first and publish them in that order. The newly published crate has a delay of up to 10 seconds before it is searchable. In my publish script, I'll retry several times when `cargo` complaints that it fails to resolve a dependency.

Second, it is not atomic to publish the whole workspace. If I successfully published `bar 0.0.1` and later fails to publish `foo 0.0.1` because of a bug in `bar 0.0.1`, I have to yank `bar 0.0.1`, bump the version, and re-publish both `foo` and `bar`.

## Cyclic Dependencies

The `dev-dependencies` may introduce cyclic dependencies. Take the example again that the crate `foo` depends on `bar`. This time the test cases of `bar` depend on `foo`. Cargo can resolve these cyclic dependencies because it does not need the `dev-dependencies` to build both `foo` and `bar`, so it can build `bar`, `foo`, and then `bar` test cases in order.

But `cargo publish` requires both dependencies and `dev-dependencies` are available in crates.io, now cyclic dependencies will cause problems.

It's tedious to arrange the crates to resolve the cyclic dependencies, so I adopted [this workaround](https://github.com/rust-lang/cargo/issues/4242) to remove all the `dev-dependencies` before publish and run `cargo publish --allow-dirty` to ignore the dirty git working directory.

## It Is Very Slow to Publish

Finally, it is really slow to publish 60 crates in a big project. It seems that they will not share the target directory and each crate uses its own directory inside `target/publish`. If the workspace has three crates, `foo`, `bar`, `baz`, where `foo` depends on `bar`, and `bar` depends on `baz`, cargo will take quadratic time to publish all the crates:

* Build `baz` and publish `baz`.
* Build `baz` and `bar`, then publish `bar`.
* Build `baz`, `bar`, and `foo`, then publish `foo`.

The `target/publish` also takes a lot of disk space. After I published 60 crates, the folder occupied about 80G storage. If the publish host has limited disk space, the script must clean up the folder regularly.
