---
date: '2020-06-20T16:39:57+0800'
tags:
- productivity
- tool
- windows
---

# Minimize any window into system tray in Windows

There are two apps both work for me in scoop extras bucket.

```
scoop bucket add extras
scoop install rbtray traymond
```

They both require running their background process first. Rbtray minimizes a window into system tray by right clicking the window minimization button, while traymond us shortcuts Win + Shift + Z。

Rbtray has no its own system tray icon. Minimize a window and right click it to quit rbtray. Traymond has its own tray icon, use it to exit or restore all windows.