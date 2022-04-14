---
date: '2010-08-25'
description: This article demonstrates how to quickly switch to a window using gpicker and wmctrl.
title: Switch Window Using Fuzz Matching
---

# Switch Window Using Fuzz Matching

#desktop #linux #productivity #script

This article demonstrates how to quickly switch to a window using **gpicker**
and **wmctrl**. You type significant letters of workspace name, application name
or title and gpicker provides a list of windows you most likely mean to pick.

<!--more-->

## Gpicker

> [Gpicker][] is a program that allows you to quickly and conveniently pick file
> in a (possibly very large) project. You type significant letters of file name
> (typically from the start of words) and gpicker provides you with a list of
> files you most likely mean to pick. The program filters and orders project's
> list of files in real-time as you type.

You need to [download](http://ftp.twaren.net/Unix/NonGNU/gpicker/) and install
it manually (for Ubuntu, you can download the Debian package).

Gpicker is designed as a filter, so it can be used to select item from an
arbitrary list. The selected item is printed on standard output.

For example, use gpicker to select a number between 1 and 10:

```
$ seq -w 1 10 | gpicker -n "\n" -
```

![[picker_1_to_10.png|Gpicker picks 1 to 10|fit]]


The last dash tells gpicker to read list from standard input, and option "-n"
sets the list separator. Gpicker uses "\0" as item separator by default.

## Wmctrl

**Wmctrl** is a command line utility to interact with a EWMH/NetWM compatible X
Window Manager. It can list all windows, switch to a window or bring a window to
current workspace. Wmctrl can be installed by package manager in most Linux
distribution.

Wmctrl lists all windows using option "-l". We can add "-x" to list windows
resource and class as well. The output of `wmctrl -l -x` looks like:

    0x03200009  0 urxvt.URxvt       ian-desktop urxvt
    0x0340008e  1 Navigator.Firefox ian-desktop Vimperator / test
    0x03e000a4  2 emacs.Emacs       ian-desktop Emacs: _theme.sass

The first column is the window ID. We can switch to or bring a window using the
ID.

    # switch to Emacs, raise and focus it
    wmctrl -i -a 0x03e000a4
    
    # bring Emacs to current workspace, raise and focus it
    wmctrl -i -R 0x03e000a4

## Windows Picker

Now we can use wmctrl to list windows, gpicker to select one window, and
wmctrl again to switch to the selected window.

    wmctrl -i -a `wmctrl -l -x | gpicker -n "\n" -d "\n" -`

The directory separator is set to "\n" in the first windows picker above,
because gpicker is designed to pick files primarily and it has special rules
in the matching algorithm.

First the item is split by directory separator. Before we enter a directory
separator ("/" by default), only the last component (it is the file name if the
item is a file path) is used in matching. For example, "bin" does not match item
"bin/ruby", but "bin/", even "b/" does match. If the window title contains the
directory separator, for example the Firefox in the `wmctrl -l -x` output above:

    0x0340008e  1 Navigator.Firefox    ian-desktop Vimperator / test

To match it, we must enter "firefox/". So I set directory separator to "\n" to
disable this feature, and the whole item is used to match.

However, we can take advantage of this feature. If we construct the window item
likes:

    id/workspace/window_class/window_title

I can match window title by type significant letters directory. I also can
use directory separator "/" to filter all windows in a specific workspace, or
windows with the same window class.

It is very useful for me. Because I uses tiling windows manager
[Xmonad](http://xmonad.org/) and places windows in different windows. Following
are some examples:

| I have entered | Windows I want to match                                     |
| -------------- | ----------------------------------------------------------- |
| www/ff/        | Firefox in workspace "2.www"                                |
| ruby           | Windows which title contains ruby                           |
| xpdf/ruby      | A document opened using xpdf and the title contains ruby    |
| sys/usrshare   | The terminal I opened visit /usr/share in workspace "1.sys" |


![[picker-windows-list.png|Windows list]]
![[picker-xpdf-ruby.png|Select Ruby document opened in Xpdf]]

Sure, we have to remove "/" from workspace name and window title.

I use a Ruby [script](https://gist.github.com/doitian/551432) to format the
list. Workspace name can be listed using `wmctrl -d`.

Now we can use the ruby script in the revised version:

    wmctrl -i -a `wlist.rb | gpicker - | sed 's;/.*$;;'`

Replace "-a" with "-R" to bring window to current workspace.

[gpicker]: http://savannah.nongnu.org/projects/gpicker "Gpicker"
