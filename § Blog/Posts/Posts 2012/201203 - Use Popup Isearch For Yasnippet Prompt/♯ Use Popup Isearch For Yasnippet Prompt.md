---
date: '2012-03-30'
description: Use popup as a backend of yasnippet prompt
title: Use Popup isearch For Yasnippet Prompt
---

# Use Popup Isearch For Yasnippet Prompt

#emacs

[Yasnippet][] tries functions in `yas/prompt-functions` when it needs user to select one choice, such as selecting snippets with the same trigger key, such as helper method `yas/choose-value`.

[popup][] is a visual popup interface library extracted from [auto-complete][] by its author. It has better look and feel than all the built-in `yas/prompt-functions`. Also it is easy to customize, and its isearch mode is very efficient, the items are filtered on-the-fly when typing.

<!--more-->

/choises.png "Popup snapshot: choices"
/filter_by_keyword.png "Popup snapshot: filter"

The integration is easy. Load `popup.el`, implement one prompt function and
add it to `yas/prompt-functions`.

※ [yasnippet-popup-isearch-prompt.el](https://gist.github.com/doitian/2245733)

``` lisp
(require 'popup)
(require 'yasnippet)

;; add some shotcuts in popup menu mode
(define-key popup-menu-keymap (kbd "M-n") 'popup-next)
(define-key popup-menu-keymap (kbd "TAB") 'popup-next)
(define-key popup-menu-keymap (kbd "<tab>") 'popup-next)
(define-key popup-menu-keymap (kbd "<backtab>") 'popup-previous)
(define-key popup-menu-keymap (kbd "M-p") 'popup-previous)

(defun yas/popup-isearch-prompt (prompt choices &optional display-fn)
  (when (featurep 'popup)
    (popup-menu*
     (mapcar
      (lambda (choice)
        (popup-make-item
         (or (and display-fn (funcall display-fn choice))
             choice)
         :value choice))
      choices)
     :prompt prompt
     ;; start isearch mode immediately
     :isearch t
     )))

(setq yas/prompt-functions '(yas/popup-isearch-prompt yas/no-prompt))
```

[yasnippet]: http://capitaomorte.github.com/yasnippet/index.html
[popup]: https://github.com/m2ym/popup-el
[auto-complete]: https://github.com/m2ym/auto-complete
