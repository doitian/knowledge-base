---
comment: true
date: 2018-05-31 03:30:42
description: Use marks as a stack in Vim
katex: false
share: true
title: Vim Marks Stack
---

# Vim Marks Stack

#vim

I rarely used more than two marks in Vim, so why not use them as a stack and keep latest history?

The idea is that

- First shift existing marks in `a-y` to `b-z`, thus original mark `z` is dropped.
- Then save current position into mark `a`.

```
function! PushMark(is_global)
  if a:is_global
    let l:curr = char2nr('Z')
  else
    let l:curr = char2nr('z')
  endif
  let l:until = l:curr - 25
  while l:curr > l:until
    call setpos("'" . nr2char(l:curr), getpos("'" . nr2char(l:curr - 1)))
    let l:curr -= 1
  endwhile
  call setpos("'" . nr2char(l:curr), getpos("."))
endfunction

" Push to marks a-z
nnoremap <silent> m, :call PushMark(0)<CR>
" Push to marks A-Z
nnoremap <silent> m. :call PushMark(1)<CR>
```
