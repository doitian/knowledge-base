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
  - x
  - zettel/permanent
description: 微信输入法激活后会注册真正的全局语音快捷键，但英文键盘下识别的文字只能放到剪贴板。把它和 AutoHotkey 的快捷键分开，就能自动切到中文输入、再次按键结束后切回英文。
created: "[[2026-09-23]]"
url: "[blog.iany.me](https://blog.iany.me/zh/2026/09/trigger-windows-ime-voice-input-from-an-english-keyboard-layout/)"

---

# 让 Windows 输入法的语音快捷键在英文键盘下也能触发


我平时用英文键盘布局写代码，想说句话就得先切到中文输入法。我希望按 <kbd>RAlt</kbd> + <kbd>Space</kbd> 就能直接开始语音输入。

一开始我以为输入法的语音快捷键只在中文布局下才生效。后来发现，微信输入法只要激活过，就会注册一个真正的全局快捷键，切回英文也能触发。但这时它没有权限往当前窗口插入文本，只能把识别的文字放到剪贴板，还得自己粘贴一下。

我本来就在用 AutoHotkey，比如之前分享过[[§ Resolve the Annoying Shift + Space Shortcut in Windows Chinese Input Methods - Chinese|解决 Windows 中文输入法下 Shift + Space 快捷键的困扰]]。于是想让脚本先切到中文，再转发语音快捷键。但是微信输入法的全局快捷键优先级比 AutoHotkey 高。

解决办法是把两组快捷键分开：<kbd>RAlt</kbd> + <kbd>Space</kbd> 留给 AutoHotkey，微信输入法改用 <kbd>RWin</kbd> + <kbd>RAlt</kbd> + <kbd>Space</kbd>。平时只按前一组，切换布局和转发都交给脚本。

<!--more-->

## TL;DR

先把微信输入法里「开启和结束语音输入」的快捷键改成 <kbd>RWin</kbd> + <kbd>RAlt</kbd> + <kbd>Space</kbd>。

下面的 AutoHotkey v2 脚本的效果是：英文布局下按 <kbd>RAlt</kbd> + <kbd>Space</kbd>，自动切到中文输入法并触发语音；再按一次结束，等语音面板关闭后切回英文。原本就在中文布局下，则只转发开启和结束的快捷键，不切换布局。

```ahk
$>!Space::{
  static panel := "语音输入 ahk_class wetype.flutter.setting"
  static restoreHKL := 0

  ending := WinExist(panel)
  KeyWait "Space"
  KeyWait "RAlt"

  if ending {
    Send "{RAlt down}{RWin down}{Space}{RWin up}{RAlt up}"
    if WinWaitClose(panel, , 3) {
      if restoreHKL
        ApplyHKL(restoreHKL)
      restoreHKL := 0
    }
    return
  }

  restoreHKL := 0
  prev := ForegroundHKL()
  if !ChineseIMEActive() {
    ActivateIME("00000804")
    deadline := A_TickCount + 1000
    while !ChineseIMEActive() && A_TickCount < deadline
      Sleep 20
    if !ChineseIMEActive()
      return
    if (prev & 0x3FF) = 0x09
      restoreHKL := prev
  }
  Sleep 100
  Send "{RAlt down}{RWin down}{Space}{RWin up}{RAlt up}"
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

## 两组快捷键分工

<kbd>RAlt</kbd> + <kbd>Space</kbd> 是给自己按的，<kbd>RWin</kbd> + <kbd>RAlt</kbd> + <kbd>Space</kbd> 是给脚本发的。这样脚本就有机会先处理布局，再通知微信输入法。

```ahk
KeyWait "Space"
KeyWait "RAlt"
Send "{RAlt down}{RWin down}{Space}{RWin up}{RAlt up}"
```

先等手上的按键松开，再完整发送另一组组合键，避免物理按键和模拟按键混在一起。

中文状态下也不能再用 `#HotIf` 跳过整个热键了，因为微信输入法已经不认原来的组合键。现在中英文都由脚本接管，只在需要时切换布局。

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

切换是异步的，`PostMessage` 发完不代表已经生效，所以要轮询等到真的切过去。脚本最多等一秒，没切成功就直接返回，不再发送语音快捷键；成功后再留 100 毫秒缓冲。

## 语音结束后切回英文

既然是英文布局下触发的，说完话自然应该回到英文。现在用同一个快捷键开启和结束，就可以在第二次按键时处理切回，不用从开始录音起一直等着。

微信输入法的语音面板是一个独立的顶层窗口。每次按键先用 `WinExist` 看它在不在：不在就是开始，在就是结束。找窗口类名的办法是写个脚本记录一段时间内新出现的所有窗口，然后去触发一次语音：

```
class=wetype.flutter.setting
title=语音输入
exe=wetype_update.exe
```

开始时用 `static restoreHKL` 记住要恢复的布局，但只记英文：`(prev & 0x3FF) = 0x09` 判断的是主语言 ID，不限于某一种英文布局。原本就是中文则不记录，也就不会在结束后多切一次。

结束时先发快捷键，再等面板关闭：

```ahk
if ending {
  Send "{RAlt down}{RWin down}{Space}{RWin up}{RAlt up}"
  if WinWaitClose(panel, , 3) {
    if restoreHKL
      ApplyHKL(restoreHKL)
    restoreHKL := 0
  }
  return
}
```

最多等三秒。面板还没关就不切，避免在语音还没结束时抢先换掉输入法。这个版本只在再次按 <kbd>RAlt</kbd> + <kbd>Space</kbd> 结束时恢复布局；如果用鼠标关闭面板，不会自动切回。

类名和标题是从微信输入法 2.1.4.6 抓的，升级后可能变。真变了，脚本就分不清是在开启还是结束语音，自动切回也会失效，需要重新确认窗口信息。