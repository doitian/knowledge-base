---
date: '2014-01-17'
description: Automate disable/enable internal keyboard when an external keyboard is attached/detacched.
resources:
  name: feature
  src: keyboard-on-mac.png
title: Auto Toggle MacBook Internal Keyboard
---

# Auto Toggle Macbook Internal Keyboard

#mac #powerTool

I prefer using external keyboard with my MacBook. When no external monitors are used, a typical setup is placing the keyboard above the internal one, so I can still use the internal touchpad.

But sometimes the external keyboard may press some keys of the internal keyboard. There is a [solution](http://forums.macrumors.com/showthread.php?t=433407) to disable the internal keyboard, but it is tedious to run the command manually.

    # Disable, ignore the warning
    sudo kextunload /System/Library/Extensions/AppleUSBTopCase.kext/Contents/PlugIns/AppleUSBTCKeyboard.kext/
    # Enable
    sudo kextload /System/Library/Extensions/AppleUSBTopCase.kext/Contents/PlugIns/AppleUSBTCKeyboard.kext/

Fortunately, [Keyboard Maestro](http://www.keyboardmaestro.com/main/) supports executing scripts when a USB device is attached or detached.

<!--more-->

I have created two macros to enable and disable internal keyboard.

Before the macros can be used, you must setup sudoers to allow running the command without password.

    $ sudo visudo

And append following line to the file and save it.

    %admin ALL = NOPASSWD: /sbin/kextunload /System/Library/Extensions/AppleUSBTopCase.kext/Contents/PlugIns/AppleUSBTCKeyboard.kext, /sbin/kextload /System/Library/Extensions/AppleUSBTopCase.kext/Contents/PlugIns/AppleUSBTCKeyboard.kext

Then restart sudo session

    $ sudo -K
