---
date: 2016-12-11
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2016-12-11


This week I worked on setting up gralog2 for logging search and analysis.

<!--more-->

## Graylog

## Gotchas

- Extractors cannot copy numeric fields.
- Timestamp cannot be overrided using numeric field which is Unix Epoch. Use GELF or a string field.

## URI configuration

It is confused to configure Graylog various URIs

- `rest_listen_uri` specifies interface, port and path that Graylog will bind and listen incoming API requests.
- `rest_transport_uri` is URI used by other nodes in a cluster. The default is `reset_listen_uri`, but if `rest_listen_uri` contains wild interface `0.0.0.0`, it is replaced with the first non-loopback IPv4 address.
- `web_listen_uri` specifies interface, port and path that Graylog will bind and listen incoming WEB interface requests.
- `web_endpoint_uri` specifies how JavaScript accesses Graylog API, it can be overrided in HTTP header `X-Graylog-Server-URL`.

Use case: the server intranet IP is 10.0.0.2, public IP is 1.2.3.4

```
# Listen on all interfaces so it can be accessed locally by NGINX, and other nodes in cluster
rest_listen_uri = http://0.0.0.0:9000/api/
# This is for other nodes in the intranet.
rest_transport_uri = http://10.0.0.2:9000/api/
# Also listen on all interfaces
web_listen_uri = http://0.0.0.0:9000/
# Set to NGINX or Load Balance address on all nodes
web_endpoint_uri = http://1.2.3.4:80/api/
```

## Shell

I had added helper scripts to use [fzf][1] this week:

- [fasd\_fzf][2] Use fzf to select recently frequently used files or directories saved by [fasd][3].
- [tmux-fzf-session][4] Select a tmux session.
- [tmux-fzf-pane][5] Select a tmux pane.

And their [zsh completions][6]

Also refactored a script to send text to tmux pane:

- [tt][7] tmux `send-keys` wrapper

And tips I learned when implementing the scripts:

- Indirect access variables in shell, zsh `${(P)a}`,  bash `${!a}`.
- Test if has prefix `[[ test = t* ]]`
- Delete from array, zsh `a[1]=()`, bash `unset a[1]`

Check a value is in array in zsh:

- `${v[(i)value]}` returns index of value in array
* `${v[(r)value]}` returns value if it is in array, returns empty otherwise

```
[ "${array[(i)value]}" -le "${#array[@]}" ]
```

[zsh-users/zsh-completions: Additional completion definitions for Zsh][8] is a good getting started manual for zsh completion. Helper `_arguments` is enough for most simple command completion.

## Misc

- [What can I do when my SSH session is stuck? - Ask Different][9]. I closed the terminal window before, that means I had to reopen the window to resume the work via SSH. Now I know I can close stuck session using <kbd>~.</kbd>. If I want to run some local commands I can suspend SSH using <kbd>^Z</kbd>.
- The first argument `indent` in syslog C API `openlog` must be valid in every `syslog` calls because only the pointer is saved locally to prepend program name to every log. So it cannot be a stack char array in initialization function.
- Service in skynet may call `release` before `init` returns in C service. I leads to segment fault if `init` accesses memory which is freed in `release`.
- [Koto][10], a d3js framework for reusable charts.
- [edvin/tornadofx: Lightweight JavaFX Framework for Kotlin][11]. We use JavaFX to develop internal GUI tools.
- [Script Filter JSON Format - Workflow Input Objects - Alfred Help and Support][12]. It is easier to develop a script filter in Alfred using JSON format now.
- [htop explained | peteris.rocks][13].
- [APT Cheat Sheet - Packagecloud Blog][14]. I have used Ubuntu for years, but I still don’t know when to use `apt-get`, when to use `apt-cache` and when to use `dpkg`. It is better to save it in Evernote for office reference.
- [Dear JavaScript, – Medium][15]. About open source community.

[1]:    https://github.com/junegunn/fzf
[2]:    https://github.com/doitian/dotfiles/blob/master/bin/fasd_fzf
[3]:    https://github.com/clvv/fasd
[4]:    https://github.com/doitian/dotfiles/blob/master/bin/tmux-fzf-session
[5]:    https://github.com/doitian/dotfiles/blob/master/bin/tmux-fzf-pane
[6]:    https://github.com/doitian/dotfiles/blob/master/zsh/completion.zsh
[7]:    https://github.com/doitian/dotfiles/blob/master/bin/tt
[8]:    https://github.com/zsh-users/zsh-completions
[9]:    http://apple.stackexchange.com/questions/35524/what-can-i-do-when-my-ssh-session-is-stuck
[10]:   https://github.com/kotojs/kotojs
[11]:   https://github.com/edvin/tornadofx
[12]:   https://www.alfredapp.com/help/workflows/inputs/script-filter/json/
[13]:   https://peteris.rocks/blog/htop/
[14]:   https://blog.packagecloud.io/eng/2015/03/30/apt-cheat-sheet/
[15]:   https://medium.com/@thejameskyle/dear-javascript-7e14ffcae36c#.rb5663a0s
