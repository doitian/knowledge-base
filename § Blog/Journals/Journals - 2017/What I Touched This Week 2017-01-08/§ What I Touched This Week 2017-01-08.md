---
date: 2017-01-08
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2017-01-08


This week I was setting up cocos2d-x project automation build and dependencies management using [masterless saltstack][1].

A minimum minion config, saved it as `config/minion`

    id: local
    file_client: local
    minion_id_caching: False
    root_dir: ./.salt
    file_roots:
      base:
        - ./states
    pillar_roots:
      base:
        - ./pillar

To include dynamic states and pillar roots, just generate the minion config file every time before invoking `salt-call`

## Game

- [Tencent/xLua: xLua is a hot-fix solution plugin for Unity3D, it supports android, ios, windows, osx, etc.][2] 腾讯开源的 Unity3d  Lua 解决方案

[1]:    https://docs.saltstack.com/en/latest/topics/tutorials/quickstart.html
[2]:    https://github.com/Tencent/xLua
