---
date: '2021-09-11T21:21:30+0800'
feature: cartograph-cf.png
---

# Use Italic Font for Coding

I discovered [Noctis] theme recently and found that the font [Cartograph CF] is really interesting.

[Noctis]: https://marketplace.visualstudio.com/items?itemName=liviuschera.noctis

[Cartograph CF]: https://connary.com/[cartograph.html](cartograph.html)

> Cartograph is a handsome monospaced font family featuring lush italics, code-friendly ligatures

It’s funny to see those handwriting like italic characters while coding, so I purchased the font and integrated it into my tools.

For Visual Studio Code, I use Noctis. But it uses too much italic style, which decreases the readability. Here are my customizations:

```json
  “editor.tokenColorCustomizations”: {
    “[Noctis]”: {
      “textMateRules”: [
        {
          “scope”: “markup.list”,
          “settings”: { “fontStyle”: “” }
        },
        {
          “scope”: “text.markdown.notes.tag”,
          “settings”: { “fontStyle”: “italic” }
        }
      ]
    }
  },
```

![[vscode.png|Visual Studio Code|wide]]

It's handy to inspect the syntax highlight scope under cursor using the command "Developer: Inspect Editor Tokens and Scopes".

In macOS Terminal, I can use the escape code `\e[3m` to enable italic and `\e[23m` to reset.

```
printf “\e[3mitalic\e[23m”
```

Or using echo

```
echo “^[[3mitalic^[[23m”
```

Where the `^[` is indeed how the terminal displays Esc. One way to insert Esc is via `Ctrl-v Esc`.

I switched to [starship] recently, so I don't need to bother setting up the italic fonts in my shell prompt by myself. Here is my starship config file:

[starship]: https://starship.rs/

```
format = “[$all](italic)”

[directory]
format = ‘[%\(4~|%-1~/…/%2~|%~\)]($style)[$read_only]($read_only_style) ‘

[git_branch]
symbol = “±”
style = “purple bold italic”

[status]
disabled = false

[nodejs]
symbol = ‘🤖 ‘
```

I changed the nodejs symbol, because Cartograph CF has no the nerd font icons.

I'm a heavy user of tmux, it's tricky to enable italics in tmux. The secret is setting `default-terminal` to tmux.

```
set -g default-terminal “tmux”
```

Then set back the terminal to `xterm-256color` via `default-command` because macOS Terminal does not understand what is the *tmux* terminal.

```
set -g default-command “env TERM=xterm-256color zsh”
```

I only configure the session name to be italic.

```
set -g status-left “#[fg=white,bg=colour31,nobold,italics] #S ”
```

I cannot find a cross-platform way to show italic font in vim, so I manually enable it when I want to see the funny italic characters in the comment:

```
function! s:Italic(enable)
  if a:enable
    hi Comment cterm=italic gui=italic
    hi Folded cterm=italic gui=italic
    let &t_ZH = “\e[3m”
    let &t_ZR = “\e[23m”
  else
    hi Comment cterm=none gui=none
    hi Folded cterm=none gui=none
    let &t_ZH = ‘’
    let &t_ZR = ‘’
  endif
endfunction

command! ItalicEnable call s:Italic(1)
command! ItalicDisable call s:Italic(0)
```

![[shell-tmux-vim.png|Shell, Tmux and Vim|wide]]

The last tool is [Obsidian], I use the CSS snippet to customize the appearance:

[Obsidian]: [https://obsidian.md/](https://obsidian.md/)

```css
:root {
  --font-monospace: ‘Cartograph CF’, monospace;
}

.cm-meta, .cm-hmd-frontmatter, .tag, .image-embed[alt]:after {
  font-style: italic;
  font-family: var(--font-monospace);
}
.cm-meta.cm-formatting-task {
  font-style: normal;
  font-family: var(--default-font);
}
```

Fortunately, it also works on iOS after installing the fonts to the system via [Fontcase].

[Fontcase]: https://apps.apple.com/us/app/fontcase-manage-your-type/id1205074470

I have also tested several frequently used iOS apps.

[Textastic] can use the fonts installed by Fontcase, and Cartograph CF works perfect.  The app [a-Shell] is also fine to use the self installed fonts.

But [Blink] does not support system fonts. Although it can install fonts via CSS, I cannot make Blink display Cartograph CF using the correct line height. It also makes Blink sluggish and unstable.

[Textastic]: https://www.textasticapp.com/
[a-Shell]: https://holzschu.github.io/a-Shell_iOS/
[Blink]: https://blink.sh/

I use an Android phone currently, but I give up the joy to use Cartograph CF on my phone. Because I don't use it for work and it seems hard to install fonts on Android. I tried to make it work in Obsidian, by copying fonts to Obsidian vault and using remote font URL, but both failed.
