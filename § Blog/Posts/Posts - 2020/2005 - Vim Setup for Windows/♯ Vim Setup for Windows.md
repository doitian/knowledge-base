---
date: '2020-05-05T10:28:26+0800'
---

# Vim Setup for Windows

#windows

I used to use Visual Studio Code in Windows as mentioned in a [previous post](ia-writer://open?path=/Locations/_Publish/§%20Blog/Posts/Posts%20-%202020/2005%20-%20My%20Windows%20Environment%20Setup/♯%20My%20Windows%20Environment%20Setup.md). But its startup time is terrible on Surface Go, so I decide to give vim another try.

<!--more-->

First install vim via scoop

```
scoop install vim
```

The most important difference of the Windows vim is that it uses different paths:

```
.vimrc -> _vimrc
.gvimrc -> _gvimrc
.vim -> vimfiles
```

For example [plug.vim](https://github.com/junegunn/vim-plug) has to be saved as `~/vimfiles/autoload/plug.vim`.

Following are some Windows specific options:

``` vim
" Force color and encoding. Put these near the top of the config file.
if has("win32")
  set t_Co=256
  set encoding=utf-8
endif

if has("win32")
  " Support different cursor shapes in Windows Terminal
  let &t_SI="\<CSI>5 q"
  let &t_EI="\<CSI>1 q"

  " Disable fzf preview because it is broken in PowerShell
  let g:fzf_preview_window = ''

  " Use PowerShell as the shell
  set shell=powershell.exe
  set shellcmdflag=-NoLogo\ -NoProfile\ -NonInteractive\ -command
endif
```

And options in `_gvimrc` for gvim:

``` vim
set guifont=JetBrains_Mono:h11
set guioptions-=m

" Show ligatures. It is not perfect and requires C-L to manually refresh.
set renderoptions=type:directx

" Fix the ugly cursor color
hi Cursor guibg=#005f87 guifg=#eeeeee
```

## 2 linked references to "Vim Setup for Windows"

* [➫ Windows](ia-writer://open?path=/Locations/_Publish/§%20Tickler/Tickler-W/Windows/♯%20Windows.md)
* [➫ What I Touched This Week 2020-05-10](ia-writer://open?path=/Locations/_Publish/§%20Blog/Journals/Journals%20-%202020/What%20I%20Touched%20This%20Week%202020-05-10/♯%20What%20I%20Touched%20This%20Week%202020-05-10.md)
