---
date: 2026-09-23T00:45:26+0800
draft: false
aliases:
  - Trigger Windows IME Voice Input from an English Keyboard Layout
tags:
  - automation
  - ime
  - shortcut
  - windows
description: Windows 下输入法的语音快捷键只在该输入法激活时才生效。用 AutoHotkey 可以实现自动切换，但是输入法必须支持使用软件模拟发送的快捷键才行。像豆包这种在 HID 驱动层监听快捷键的，就无法用纯软件方案解决。
---

# 让 Windows 输入法的语音快捷键在英文键盘下也能触发

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2026-09-23]]
**URL**:: [blog.iany.me](https://blog.iany.me/zh/2026/09/trigger-windows-ime-voice-input-from-an-english-keyboard-layout/)

中文输入法的语音输入通常有个全局快捷键，我用的是 <kbd>RAlt</kbd> + <kbd>Space</kbd>。问题是它只在这个输入法处于激活状态时才生效。我平时用英文键盘布局写代码，想说句话就得先切到中文。

我本来就在用 AutoHotkey，比如之前分享过[[§ Resolve the Annoying Shift + Space Shortcut in Windows Chinese Input Methods|解决 Windows 中文输入法下 Shift + Space 快捷键的困扰]]。我就想加上脚本去监听 <kbd>RAlt</kbd> + <kbd>Space</kbd>，如果当前是中文键盘就跳过不处理，让快捷键直接触发输入法的语音输入。如果是英文键盘就先切换然后模拟再发送一次快捷键。但实际发现，有些输入法的快捷键是没有办法通过 AutoHotkey 的 `Send` 触发的。搜索了一下，原因是这些输入法在 HID 驱动层监听快捷键，软件生成的键盘事件到不了这一层。我只测试了豆包输入法和微信输入法。豆包输入法无法使用 AutoHotkey 触发语音输入，而微信输入法可以。

AutoHotkey 配合微信输入法，就可以在任意键盘布局下一键激活语音输入了。

<!--more-->

## TL;DR

先配置微信输入法，修改快捷键。我使用按住 <kbd>RAlt</kbd> 来语音输入，或者使用 <kbd>RAlt</kbd> + <kbd>Space</kbd> 开启和结束语音输入。

下面的 AutoHotkey v2 脚本的效果是：英文布局下按 <kbd>RAlt</kbd> + <kbd>Space</kbd>，脚本自动切到中文输入法、补发一次快捷键触发语音，语音结束后再切回英文；中文布局下脚本完全不介入。

```ahk
#HotIf !ChineseIMEActive()
$>!Space::{
  prev := ForegroundHKL()
  ActivateIME("00000804")
  deadline := A_TickCount + 1000
  while !ChineseIMEActive() && A_TickCount < deadline
    Sleep 20
  Send "{Blind}{RAlt down}{Space}"
  RestoreLayoutAfterVoice(prev)
}
#HotIf

RestoreLayoutAfterVoice(hkl) {
  static panel := "语音输入 ahk_class wetype.flutter.setting"
  if !WinWait(panel, , 3)
    return
  if !WinWaitClose(panel, , 60)
    return
  if ChineseIMEActive()
    ApplyHKL(hkl)
}

ChineseIMEActive() => (ForegroundHKL() & 0xFFFF) = 0x0804

ForegroundHKL() {
  hwnd := DllCall("GetForegroundWindow", "ptr")
  tid := DllCall("GetWindowThreadProcessId", "ptr", hwnd, "ptr", 0, "uint")
  return DllCall("GetKeyboardLayout", "uint", tid, "ptr")
}

ActivateIME(klid) {
  if hkl := DllCall("LoadKeyboardLayout", "str", klid, "uint", 0x101, "ptr")
    ApplyHKL(hkl)
}

ApplyHKL(hkl) {
  hwnd := DllCall("GetForegroundWindow", "ptr")
  tid := DllCall("GetWindowThreadProcessId", "ptr", hwnd, "ptr", 0, "uint")
  me := DllCall("GetCurrentThreadId", "uint")
  DllCall("AttachThreadInput", "uint", me, "uint", tid, "int", 1)
  DllCall("ActivateKeyboardLayout", "ptr", hkl, "uint", 0)
  DllCall("AttachThreadInput", "uint", me, "uint", tid, "int", 0)
  PostMessage 0x0050, 0, hkl, , "ahk_id " hwnd
}
```

## 为什么英文布局下按了没反应

现代中文输入法是 TSF（Text Services Framework）的 text service。它的按键钩子只在这个输入法是当前窗口的活动输入法时才会挂上。英文布局下，输入法进程虽然在后台跑着，但它根本收不到你的按键。唯一的路是：先切输入法，再把快捷键补发一次。

## 中文状态下跳过

一开始我在热键里判断如果已经是中文就跳过切换，但按键依然被脚本接管再转发。更干净的做法是用 `#HotIf` 让这个热键在中文状态下不起作用。

```ahk
#HotIf !ChineseIMEActive()
$>!Space::{ ... }
#HotIf
```

这样中文态走的是 100% 原生路径，零延迟。`$` 前缀是必须的，它保证不会递归触发形成死循环。

## 切换输入法

切换用三件套。`LoadKeyboardLayout` 拿到 HKL，再通过 `AttachThreadInput` 把自己挂到前台线程上、调 `ActivateKeyboardLayout`，最后补一个 `WM_INPUTLANGCHANGEREQUEST`：

```ahk
DllCall("AttachThreadInput", "uint", me, "uint", tid, "int", 1)
DllCall("ActivateKeyboardLayout", "ptr", hkl, "uint", 0)
DllCall("AttachThreadInput", "uint", me, "uint", tid, "int", 0)
PostMessage 0x0050, 0, hkl, , "ahk_id " hwnd
```

`ActivateKeyboardLayout` 单独调只对自己的线程生效，所以必须先 `AttachThreadInput`。

要注意 HKL 层面分不出具体是哪个中文输入法：微软拼音、微信输入法、豆包的 langid 都是 `0x0804`，切过去的是上次用的那个。所以判断是否已经是中文，比较低 16 位就够了：

```ahk
ChineseIMEActive() => (ForegroundHKL() & 0xFFFF) = 0x0804
```

切换是异步的，`PostMessage` 发完不代表已经生效，所以要轮询等到真的切过去。

## 语音结束后切回英文

既然是英文布局下触发的，说完话自然应该回到英文。麻烦的是怎么知道说完了。

微信输入法的语音面板是一个独立的顶层窗口，等它关闭就行。找窗口类名的办法是写个脚本记录一段时间内新出现的所有窗口，然后去触发一次语音：

```
class=wetype.flutter.setting
title=语音输入
exe=wetype_update.exe
```

于是切回的逻辑就是等这个窗口出现、再等它消失：

```ahk
RestoreLayoutAfterVoice(hkl) {
  static panel := "语音输入 ahk_class wetype.flutter.setting"
  if !WinWait(panel, , 3)
    return
  if !WinWaitClose(panel, , 60)
    return
  if ChineseIMEActive()
    ApplyHKL(hkl)
}
```

三个判断的作用依次是：

1. 面板没出现，此时不切回。因为分不清真的失败和检测漏了。
2. 面板超过 60 秒还开着，同样不切回。避免逻辑一直挂着。
3. 切回前确认当前还是中文。

类名和标题是从微信输入法 2.1.4.6 抓的，升级后可能变。真变了的表现是切回功能静默失效（停在中文），不影响触发本身。