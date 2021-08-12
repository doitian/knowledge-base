# Windows Chinese Environment

#windows #lang/zh

## Telegram

Set the Windows region to China, then Telegram will choose correct Chinese fonts.


Alternatively, download [FontMod.dll](https://github.com/ysc3839/FontMod) as `winmm.dll` and place it under the same directory with `Telegram.exe`.

In my Windows 10, I'm using English locale and have to edit the `FontMod.yaml` and replace following fonts.

```
  DAOpenSansRegular:
    <<: *zh-cn-font
  DAVazirRegular:
    <<: *zh-cn-font
```

## Vim

The following options work in commands such as `!date` and `r !date`.

```
set encoding=utf-8
set shell=powershell.exe
set shellcmdflag=-NoLogo\ -NoProfile\ -NonInteractive\ -command
set shellquote=\"
set shellxquote=
set shellslash
```

But `system()` function returns string in the encoding according to the system region setting. For example, when the region is set to China, it will return string in GBK encoding. A workaround is enabling UTF-8 in Administrative language setting "Language for non-Unicode programs".
