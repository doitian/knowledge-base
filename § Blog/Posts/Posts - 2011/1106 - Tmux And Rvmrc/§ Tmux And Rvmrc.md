---
date: '2011-06-27'
description: Force rvm to load the file by appending cd .
lastmod: '2015-10-15'
title: '[Outdated] Tmux And Rvmrc'
tags:
- console
- ruby
- tmux
---

# Tmux And Rvmrc

> RVM has since moved to using .profile, so just put the "cd ." in .profile and it will work
>
> --- Mikael Wikman commented below

**Original Article**

[Tmux][] is a terminal multiplexer. I switched to Tmux from [GNU Screen][screen]
recently.

I work on several Ruby projects. I use [RVM] to manage gem set for different
projects, and use [rvmrc] file to switch gem set automatically. I usually start
a Tmux session for a project in its root directory, so all the windows and panes
in the session use the project root as default directory. The problem is, the
new created shell in the session does not load `.rvmrc` in the root directory. I
have to force loading the file using "`cd .`"

<!--more-->

I also use [Tmuxinator][]. It can specify a rvm gem set though project yml
file. But this setting only has effect on the windows and panes pre-configured
in the yml file, the new created shells do not load `.rvmrc`. Moreover, if the
project needs different gem sets for different branches, each gem set must has
its own tmuxinator project file.

Finally, I figured out a simple solution. Just append `cd .` to the end of the
shell init file (`.bashrc` for bash and `.zshrc` for zsh). Then all the new
shells will try to load the `.rvmrc` file in the default directory where it
starts, including shells in Tmux.

    # try loading .rvmrc, add it below the line loading RVM
    cd .

[tmux]: http://tmux.sourceforge.net/
[screen]: http://www.gnu.org/software/screen/
[rvm]: http://beginrescueend.com/
[rvmrc]: https://rvm.io/workflow/rvmrc
[tmuxinator]:  https://github.com/aziz/tmuxinator
