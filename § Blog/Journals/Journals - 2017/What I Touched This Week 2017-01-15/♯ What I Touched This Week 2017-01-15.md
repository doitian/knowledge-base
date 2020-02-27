---
date: 2017-01-15
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2017-01-15


This week I continue on cocos2d-x project automation build and dependencies management.

By default, tolua registers global variables. A trick to use fallback Lua implementation by default is:

    # config.lua
    if _G.config then
      return _G.config
    end
    return { lua = true }

<!--more-->


There is a gotcha to register tolua bindings in AppDelegate.cpp in Quick Community Edition, lua stack top is `package.preload` after `quick_module_register`.

- If prebuilt library is added as a reference to Xcode project and it is not in SRCROOT of any project, its parent directory must be added to library search header in build settings.
- Use `preBuild.dependsOn(copyAssets)` to do something before build in Android gradle project. It must be added to the gradle file which has added android plugin. For example, `preBuild` is not available in the top `build.gradle` in Quick Community 
- [Why copy the key when traverse table in Lua c API][1]

## Game

- [腾讯开源手游热更新方案：Unity3D下的XLua技术内幕（一）\_Gad-腾讯游戏开发者平台][2] GAD 上 XLua 的系列文章

## Misc

- 腾讯 Bugly 提供的 [Android SDK 代理][3]
- [MSDN, 我告诉你][4] 要下载微软老版本的开发工具可以来这找
- Use https proxy in Emacs

        export http_proxy=xxx https_proxy=xxx
        emacs -nw --insecure

[1]:    http://stackoverflow.com/a/6142700/667158
[2]:    http://gad.qq.com/article/detail/7182056
[3]:    http://android-mirror.bugly.qq.com:8080
[4]:    http://msdn.itellyou.cn/
