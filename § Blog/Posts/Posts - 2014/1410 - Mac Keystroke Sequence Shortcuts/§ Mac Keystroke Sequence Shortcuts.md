---
date: '2014-10-13'
description: Setup visual keystroke sequence shortcuts using Keyboard Maestro in Mac OS X.
title: Keystroke Sequence Shortcuts in Mac OS X
---

# Mac Keystroke Sequence Shortcuts

#macos #productivity

It is a headache to find an available keyboard shortcuts in Mac OS X.  I used <kbd>Option + Letter</kbd>  and <kbd>Shift + Option + Letter</kbd> before, since they are preserved for inputting special characters. It has some problems:

- Emacs and terminal require a modifier for <kbd>Meta</kbd>. I chose <kbd>Command</kbd>. It means if I want to use application shortcut with <kbd>Command</kbd> in these applications, such as <kbd>Command+Q</kbd> to quit the application, I have to use the right one.
- I always forget the shortcuts. Although I have listed them in a sheet, it is a pain to keep it synchronized with the shortcuts defined every where.

I switched to a new solution using keystroke sequence shortcuts recently. All my global shortcuts start with <kbd>Command+M</kbd> (<kbd>⌘M</kbd>). A menu is displayed when I typed prefix. If I forget the shortcut, I just need to glance through the menu.

<!--more-->

![[cmd-m-menu.png|The shortcuts menu shows all available commands and the corresponding keyboard binding.]]

## Disable System Default Shortcut

<kbd>⌘M</kbd> is a system default shortcut to minimize window. I never use it, and it is annoyed when typed by acident. So I disable it and use it as my personal keytroke sequence shortcuts prefix.

Run the following code[^1] in terminal to disable it.

    defaults write -g NSUserKeyEquivalents -dict-add 'Minimize' '\0'

The changes are applied only in new opened apps. Please reopen all applications, or just restart the system.

## Keyboard Maestro

The shortcuts and the menu in the snapshot are managed by [Keyboard Maestro][1]. There are two ways to implement keystroke sequence in Keyboard Maestro.

The first solution is setting the same keyboard shortcut for multiple macros. Keyboard Maestro auto detects conflicts and display a menu like the one above. It strips the common prefix, and use the first distinct letter in macro name as the shortcut. Thus, it does not support modifier (like <kbd>Shift</kbd>, <kbd>Command</kbd>) in subsequent shortcut. And it requires some trick to name your commands, such as “l) Read Later” and “v) Clipboard History”.

Since I want to use modifier, I use another solution: a group with the option “Shows a palette for one action when the hot key xxx is pressed”.

![[cmd-m-macro-group.png|Shows a pallete for one action when the hot key xxx is pressed.]]

It is tricky to display the shortcuts and align them to the right in the menu like in the snapshot. The shortcuts should be added in command name manually and are aligned by inserting tabs and spaces.

## Shortcuts Forwarding

Some application provides global shortcuts, but they cannot be used in Keyboard Maestro. The workaround is using a rarely used and hard to type  in the application preference, and forward using a simple shortcut through Keyboard Maestro.

For example, I defined the Alfred 2 clipboard manager shortcut to <kbd>Ctrl+Option+Shift+Command+F4</kbd>. I use <kbd>Command+M, Command+V</kbd> (Hold <kbd>Command</kbd>, type <kbd>M</kbd>, then <kbd>V</kbd>, and release <kbd>Command</kbd>) to show it, because I have a macro in the <kbd>Command+M</kbd> group which uses the action “Type a Keystroke”.

![[shortcut-forward.png|Send a global shortcut in an application from Keyboard Maestro by sending a keystroke.]]


[^1]: http://apple.stackexchange.com/a/73957

[1]: http://www.keyboardmaestro.com/main/ "Work Faster with Macros for Mac OS X"
