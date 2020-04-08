---
comment: true
date: '2017-06-03T16:09:41+08:00'
description: Where to create properties files for TornadoFX in IntelliJ Gradle Project.
share: true
title: Resource Bundle in IntelliJ TornadoFX Gradle Project
---

# Resource Bundle In Intellij Tornadofx Gradle Project

#java

- Add properties files into `src/main/resources`
- Global messages location:
    - `src/main/resources/Messages.properties` is for default locale
    - `src/main/resources/Messages_en_US.properties` is for locale `en_US`
- Resource Bundle for component: Same directory structure to the class path. For example the resource bundle file for `views.Main` can be found in `src/main/resources/views/Main.properties`, or file name `Main_en_US.properties` for specific locale.
- [Enable native-to-ascii conversion](https://www.jetbrains.com/help/idea/configuring-encoding-for-properties-files.html) in IntelliJ to ease editing UTF-8 values.
