---
date: 2020-10-11
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2020-10-11

Picks:

[做產品真是哭夭難！ — Marty Cagan 演講 70 分鐘中文逐字翻譯 | by Jason HOU](https://medium.com/3pm-lab/marty-cagan-producttank-taipei-speech-933e7dfc13af) ([Q&A 中文逐字翻譯](https://medium.com/3pm-lab/marty-cagan-producttank-taipei-speech-qna-f4c9a6434c7c) | [Video](https://www.youtube.com/watch?v=99go9sKp70I))

<!--more-->

## Product

* [Why This Opportunity Solution Tree is Changing the Way Product Teams Work](https://www.producttalk.org/2016/08/opportunity-solution-tree/)

    Work along both dimensions of product discovery

    * discovering opportunities
    * discovering solutions

* [Flavors of Prototypes](https://svpg.com/flavors-of-prototypes/)

    > There are in fact many very different forms of prototypes, each with different characteristics and each suited to testing different things.

## Programming

* [Fast Thread Locals In Rust](https://matklad.github.io//2020/10/03/fast-thread-locals-in-rust.html)

    * Rust thread-locals are slower than they could be.
    * Rust allows cross-language [**L**ink **T**ime **O**ptimization](https://doc.rust-lang.org/rustc/linker-plugin-lto.html).

* [Why I Scatter Use Statements Throughout My Rust](https://tarquin-the-brave.github.io/blog/posts/rust_use_statements/)

    I support limiting the scope of the extension traits:

    ```rust
    let input: Data = {
        use anyhow::Context as _;
        serde_yaml::from_reader(std::io::stdin()).context("couldn't read stdin")?
    };
    ```

## Security

* [We Hacked Apple for 3 Months: Here’s What We Found](https://samcurry.net/hacking-apple/)

## Interesting Stuff

* [有三分钟热度就有三分钟收获](https://twitter.com/doitian/status/1314481306852626433)
