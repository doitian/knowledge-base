---
comment: true
date: 2018-11-02 02:00:36
description: How various flatbuffers types are compatible when one is used as child in another
summary: How various flatbuffers types are compatible when one is used as child in another
katex: false
share: true
title: Flatbuffers Compatible Table
tags:
- flatbuffers
- serialization
---

# Flatbuffers Compatible Table

| parent | table | struct | union | vector | string | enum | scalar |
| ------ | ----- | ------ | ----- | ------ | ------ | ---- | ------ |
| root   | Y     | Y      |       |        |        |      |        |
| table  | Y     | Y      | Y     | Y      | Y      | Y    | Y      |
| struct |       | Y      |       |        |        | Y    | Y      |
| union  | Y     | Y      |       |        |        |      |        |
| vector | Y     | Y      | Y     |        | Y      | Y    | Y      |

If there is a `Y` in row A column B, B can be used as a child of A. If it is
blank, B is not allowed as a child of A.

Parent `root` means which type can be used as a root object.

---

• [the test
schema](https://github.com/doitian/flatbuffers_compatible_table/blob/master/compatible_test.fbs)
