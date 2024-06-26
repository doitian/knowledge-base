---
date: 2017-10-14
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2017-10-14


- [[§ Centralized Logs Using Graylog Output - Chinese|Graylog 集中日志管理 - 日志输出]]
- [Streams: a new general purpose data structure in Redis. - antirez](http://antirez.com/news/114)

    Redis will support stream processing.

- [The 5 Types Of React Application State - James K Nelson](http://jamesknelson.com/5-types-react-application-state/)

    A pattern to categorize Redux State.

- [Developing a Redux Edge {Book}](https://www.amazon.com/Developing-Redux-Edge-Johannes-Lumpe-ebook/dp/B01KL5RJHU)

    A book recommended if you want to learn Redux in depth.

- Learned from the book above, delete a key from object:

    ```
    const {[id]: remove, ...rest} = state;
    return rest;
    ```

<!--more-->

## Projects

- [Ramda](http://ramdajs.com/#) Functional library for Javascript, It is pure, immutable and auto curried.
- [Heron](https://heron.incubator.apache.org/) Stream processing framework via Twitter, which API is compatible with Apache Storm.

## Shell, vim tips

- Fix quickfix hilight color

    ```
    hi! link QuickFixLine Search
    ```

- [Zsh 5.1 and bracketed paste](https://archive.zhimingwang.org/blog/2015-09-21-zsh-51-and-bracketed-paste.html)

    Fix `^[[?2004h` when using zsh in dump terminal

    ```
    if [[ $TERM == dumb ]]; then
        unset zle_bracketed_paste
    fi
    ```

- [Close disturbing windows in #vim](https://gist.github.com/doitian/3109eb0951415af317081bbdaf5363fc)

    ```
    function! s:CloseDisturbingWin()
    if &filetype == "help" || &filetype == "netrw"
        let l:currentWindow = winnr()
        if s:currentWindow > l:currentWindow
        let s:currentWindow = s:currentWindow - 1
        endif
        close
    endif
    endfunction
    command! Close :pclose | :cclose | :lclose |
        \ let s:currentWindow = winnr() |
        \ :windo call s:CloseDisturbingWin() |
        \ exe s:currentWindow . "wincmd w"
    ```
