---
date: '2012-03-31'
description: There are two TAB's in Emacs, it is hard to make the TAB keybinding works as expected in Emacs.
title: Fix TAB Binding For yasnippet And auto-complete
---

# Fix Tab Binding For Yasnippet And Auto Complete

#emacs

There are two TAB's in Emacs, `(kbd "TAB")` (`\t`, `[9]`) and `(kbd "<tab>")` (`[tab]`). If modes like [yasnippet][] and [auto-complete][] want to bind on `TAB`, their trigger key must be the same with the original Tab command. Since Emacs binds `indent-for-tab-command` on `(kbd "TAB")`, so it's better to use it as the trigger key. Yasnippet binds to it by default, It is also easy to setup `auto-complete` to trigger using Tab.

``` lisp
;; trigger using TAB and disable auto start
(custom-set-variables
 '(ac-trigger-key "TAB")
 '(ac-auto-start nil)
 '(ac-use-menu-map t))
```

But in some modes (`ruby-mode`, `markdown-mode`, `org-mode`), the command is bind to `(kbd "<tab>")`, when the real Tab key is typed, the function bind on `(kbd "<tab>)` has higher priority, so yasnippet and auto-complete are not invoked. It is easy to fix by moving the keybinding:

``` lisp
(defun iy-tab-noconflict ()
  (let ((command (key-binding [tab]))) ; remember command
    (local-unset-key [tab]) ; unset from (kbd "<tab>")
    (local-set-key (kbd "TAB") command))) ; bind to (kbd "TAB")
(add-hook 'ruby-mode-hook 'iy-ac-tab-noconflict)
(add-hook 'markdown-mode-hook 'iy-ac-tab-noconflict)
(add-hook 'org-mode-hook 'iy-ac-tab-noconflict)
```

[yasnippet]: https://github.com/joaotavora/yasnippet
[auto-complete]: https://github.com/m2ym/auto-complete
