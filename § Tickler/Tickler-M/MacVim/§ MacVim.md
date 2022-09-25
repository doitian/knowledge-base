# MacVim

#software-usage #macos

┌ Fix python3 support

MacVim uses 3.7, but Homebrew has upgraded to 3.8

```
brew install python@3.7
```

then

```
ln -s /usr/local/Cellar/python@3.7/3.7.8_1/Frameworks/Python.framework/Versions/3.7 /usr/local/Frameworks/Python.framework/Versions/3.7
```
