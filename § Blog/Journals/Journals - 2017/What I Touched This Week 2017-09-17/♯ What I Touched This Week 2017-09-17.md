---
date: 2017-09-17
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2017-09-17


- [wolfcw/libfaketime: libfaketime modifies the system time for a single application](https://github.com/wolfcw/libfaketime)

    Useful for test related to time.

- [How to increase root maximum file open limit (ulimit) in Ubuntu? - Stack Overflow](https://stackoverflow.com/questions/21515463/how-to-increase-neo4js-maximum-file-open-limit-ulimit-in-ubuntu/24796466#24796466)

    Limit for root user must be added explicity. Wildcard '*' does not match root.

- [Go process livereload for development](https://gist.github.com/doitian/b171d8b1bdd461ec7e362f3b10916a73)

- Decimal is consider as integer in MySQL, set scale explicitly.

    ```
    change_column :products, :discount_percentage, :decimal, precision: 5, scale: 2
    ```

## Projects

- [apiDoc - Inline Documentation for RESTful web APIs](http://apidocjs.com/#demo)

    Generate API Doc from comments.

- [NATS Documentation](https://docs.nats.io/)

    Message Queue using Golang.

- [Wilson’s Algorithm - bl.ocks.org](https://bl.ocks.org/mbostock/11357811)

    Algorithm to generate a maze using random walk.

- [Download/i18nline: Keep your translations in line](https://github.com/download/i18nline)

    I18n for Javascript.

- [substantial/updeep: Easily update nested frozen objects and arrays in a declarative and immutable manner.](https://github.com/substantial/updeep)

    Helper for Redux reducers.

- [google/re2: RE2 is a fast, safe, thread-friendly alternative to backtracking regular expression engines like those used in PCRE, Perl, and Python. It is a C++ library.](https://github.com/google/re2)
