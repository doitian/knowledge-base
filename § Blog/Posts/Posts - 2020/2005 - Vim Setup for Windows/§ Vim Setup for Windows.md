---
date: '2020-05-05T10:28:26+0800'
---

# Vim Setup for Windows

#windows

I used to use Visual Studio Code in Windows as mentioned in a previous post, [[§ My Windows Environment Setup]]. But its startup time is terrible on Surface Go, so I decide to give vim another try.

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

## Linked mentions

%%+BEGIN: #dataviewx%%
```dataviewx
LIST WITHOUT ID "(Backlinks:: [[" + file.name + "]])"
FROM [[]] and "output"
WHERE !contains(Backlinks, [[]])
SORT file.name
```

- (Backlinks:: [[§ What I Touched This Week 2020-05-10]])
- (Backlinks:: [[§ Windows]])
%%+END%%