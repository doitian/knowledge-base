---
date: '2017-02-12'
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2017-02-12


This week I have worked on Lua API of Sentry using its Objective-C and Android client.

- Add `extern "C"` around Lua C function in header compiled as Objective-C.
- [LuaJavaBridge - Lua 与 Java 互操作的简单解决方案][1] 是很详细的在 Cocos2d-x Lua 中调用 Java 方法的文章。不过有个地方已经过时了，就是 Java 的方法可以接收和返回 `HashMap`, 和 `Vector` (用 `ArrayList` 也可以）两种复杂变量的。有一些限制，调用的时候 Lua 不能传 `nil`，`HashMap` 对应的 Lua table 的 key 和 value 都会转成 String，在 Java 中可以强转成 `HashMap<String, String>`。`Vector` 对应的 Lua table 会当成是 list，所有成员也会转成 String，在 Java 中可以强转成 `Vector<String>`。对应的类型签名如下
    - `Ljava/util/HashMap;`
    - `Ljava/util/Vector;`
    - `Ljava/util/ArrayList;`
- [Sentry-Android][2] is an open source library to report errors in Android apps to Sentry. It is better than official Java library in my opinion.

<!--more-->

## Misc

- Install gems using system Ruby when installed rbenv/rvm.

        sudo /usr/bin/gem install --bindir /usr/local/bin --no-env-shebang cocoapods 

  - `--bindir`: the default `/usr/bin` is not allowed to be modified.
    - `--no-env-shebang`: just use system Ruby explicitly.
- [webmachine: A REST-based system for building web applications][3], A RESTful framework for Erlang.
- [Iris]( https://docs.iris-go.com/install.html ), A go web framework.
- In Lua, following two statements are identicated:

        require “xx.” .. foo
        (require “xx.”) .. foo


- 写了篇[游戏分享：Shenzhen IO](/zh/games/2017/02/shenzhen-io/)。花了一个多月备案，现在放在腾讯云上，改成了用 Hugo，加上了英文，中文多语言支持。      

[1]:    http://dualface.github.io/blog/2013/01/01/call-java-from-lua/
[2]:    https://github.com/joshdholtz/Sentry-Android
[3]:    https://github.com/webmachine/webmachine
