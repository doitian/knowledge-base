---
date: 2024-04-10T19:32:40+0800
draft: false
aliases:
- Resolve the Annoying Shift + Space Shortcut in Windows Chinese Input Methods
tags:
- ime
- shortcut
- windows
---

# 解决 Windows 中文输入法下 Shift + Space 快捷键的困扰

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2024-04-10]]
**URL**:: [blog.iany.me](https://blog.iany.me/2024/04/resolve-the-annoying-shift-space-shortcut-in-windows-chinese-input-methods/)

最近我把主要的工作环境转移到了Windows系统。之前 Windows 最困扰我的是 <kbd>Shift</kbd> + <kbd>Space</kbd> 的快捷键。在中文输入法状态下稍微打字快一点，就会误触发切换半角全角的功能，打乱输入的节奏。既然我决定长期使用 Windows 系统，就花了一些时间全面解决了这个问题。

<!--more-->

## TL;DR

安装 [AutoHotkey](https://www.autohotkey.com/) v2 版。将以下代码加入到一个 `.ahk` 为后缀的文件中，比如“文档”目录中的 `main.ahk` 文件:

```
<+Space::Send (A_PriorKey = "LShift" ? "+{Space}" : "{Blind}{Shift up}{Space}{Shift down}{LWin}")  
>+Space::Send (A_PriorKey = "RShift" ? "+{Space}" : "{Blind}{Shift up}{Space}{Shift down}{LWin}")
```

双击文件 `main.ahk` 即可生效，如果要启动时自动生效，可以为这个文件创建一个快捷方式，然后将快捷方式移到到“启动”目录中。可以通过以下办法快速打开“启动”目录。

- 使用快捷键 <kbd>Win</kbd> + <kbd>r</kbd> 打开运行窗口
- 输入 `shell:startup` 并使用 <kbd>Enter</kbd> 确认

## 思路说明

<kbd>Shift</kbd> + <kbd>Space</kbd> 烦人的地方在于它会吞掉本想输入的空格。输入需要 <kbd>Shift</kbd> 组合键的符号时，通常在前或者在后要加上空格，比如 `:(){}` 这些符号。如果输入速度很快，很可能会在 <kbd>Shift</kbd> 尚未完全松开时按下 <kbd>Space</kbd> ，这时候没有输入空格反而是切换了半角全角，如果当前需要使用半角，还得再按一次切换回来。

基于上述分析，我想实现在按下 <kbd>Shift</kbd> 键后，如果在按下空格键之前按下了其他键，便视为 <kbd>Shift</kbd> 键没有及时松开，应该输入一个空格符号。如果在按下 <kbd>Shift</kbd> 键后立即按下空格键，应保留原来的半角全角切换功能。这样的配置不但能避免误触发，还可以被利用来快速输入 `) {` 这样的序列，因为全程 <kbd>Shift</kbd> 不用松开了。

上面的 AutoHotkey 代码即实现了这里描述的功能。

## 代码说明

代码有两行，分别对应的左右手 <kbd>Shift</kbd> 触发的情况。我尝试过合并成一条但失败了，具体原因我也不清楚，也不知道为什么分开就能工作了。

下面以左手的第一行为例说明：

```
<+Space::Send (A_PriorKey = "LShift" ? "+{Space}" : "{Blind}{Shift up}{Space}{Shift down}{LWin}")
```


| AutoHotkey 代码                                | 说明                                                                         |
| -------------------------------------------- | -------------------------------------------------------------------------- |
| `<+Space::`                                  | 为 <kbd>Shift</kbd> + <kbd>Space</kbd> 设置命令，并只有使用左手的 <kbd>Shift</kbd> 才能触发。 |
| `Send`                                       | 发送指定的按键序列。                                                                 |
| `(A_PriorKey = "LShift" ? X : Y)`            | 如果变量 `A_PriorKey` 的值等于 `LShift` 时返回 X 否则返回 Y。                              |
| `+{Space}`                                   | 发送组合按键 <kbd>Shift</kbd> + <kbd>Space</kbd> 以触发其原本的功能，即切换半角全角。              |
| `{Blind}{Shift up}{Space}{Shift down}{LWin}` | 这么一大串其实只是为了实现在 AutoHotkey 里在 <kbd>Shfit</kbd> 按下的情况下输入一个空格符号。              |

第一个比较重要的点是自动变量 [A_PriorHotkey](https://www.autohotkey.com/docs/v2/Variables.htm#PriorHotkey)。它记录的是组合键所有键被按下之前上一个按键状态有变化的键。因为组合键最后一个按下的一定是非修饰键，所以如果按下 <kbd>Shift</kbd> 后立即按下 <kbd>Space</kbd>，`A_PriorHotkey` 就是 <kbd>LShift</kbd> 或者 <kbd>RShift</kbd>。相反，如果 `A_PriorHotkey` 等于其它值就表示按下 <kbd>Shift</kbd> 到按下 <kbd>Space</kbd> 之间有按过其它按键。

第二个点是用来模拟输入空格的一长串  `{Blind}{Shift up}{Space}{Shift down}{LWin}`

- `{Blind}` 的作用是让 `{Shift up}` 强制修改 <kbd>Shift</kbd> 的状态改为松开保证后面 `{Space}` 输入一个空格符号。
- `{Shift down}` 是恢复 <kbd>Shift</kbd> 按下的状态，这样后面可以继续输入还 <kbd>Shift</kbd> 的组合键。
- `{LWin}` 不会触发任何操作。它的作用是如果在中文输入法里启用了点按 <kbd>Shift</kbd> 来切换中英文，在下面的按键序列中会正确输入 `: ` (冒号+空格) 并且不会误触发中英文切换：
    - 按下 <kbd>Shift</kbd>
    - 按下 <kbd>:</kbd>
    - 松开 <kbd>:</kbd>
    - 按下 <kbd>Space</kbd>
    - 松开 <kbd>Space</kbd>
    - 松开 <kbd>Shift</kbd>