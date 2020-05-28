# Windows Terminal

#windows

⚡ Config file location

```
$WindowsTerminalSetting = "$env:USERPROFILE\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
vim $WindowsTerminalSetting
```

⚡ Font

The default font is `Cascadia Code` but the ligature is not enabled. It is easy to enable it by set the font explicitly in any profile.

```
"fontFace": "Cascadia Code",
```

⚡ Cursor

The cursor settings are not in the `colorScheme`.

```
"cursorColor": "#005f87",
"cursorShape": "vintage",
```
