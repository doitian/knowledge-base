---
date: '2016-10-15'
description: My weekly review report.
series:
- What I Touched

---

# What I Touched This Week 2016-10-15


## Programming

* [动作手游实时PVP技术揭密（服务器篇）][1] 帧同步、可靠 UDP和防作弊技术
* [Yarn: A new package manager for JavaScript][2] Like bundler for gems in Ruby
* [A Review of Immutability in Ruby][3] Use Immutability data in Ruby using standard libraries and gems.

<!--more-->

## Readings

* [How to read a book a week][4] Read every day. Focus on one book and make small progress daily.

## Tips

* [How do I remove an app from Security/Accessibility][5]

    ```
    sudo sqlite3 /Library/Application\ Support/com.apple.TCC/Tcc.db
    delete from access where client like "%appnamehere%"
Replace "appnamehere" with the name of the app as it appears in the Accessibility list (keep the % signs).
    ```
* Show hidden files in macOS Sierra Finder `Shift + Command + .`
* Install Python modules for ansible installed by Homebrew

    ```
      cd /usr/local/Cellar/ansible/2.1.2.0/libexec/lib/python2.7/site-packages
      PYTHONPATH=$(pwd) python easy_install.py -ad $(pwd) redis
      ```

* [Clearing the Icon Services cache in Yosemite][6]
* [Advanced Vim macros][7] Dump macro, edit and save back to register. Run macro on scope using `normal`
* [Vim anti-patterns | Arabesque][8] Usage of `gi`, `g;`, `g,`. Use `s` as motion after action. Use `@:` to repeat command, `&` and `g&` to repeat substitution.

## Tools

* [Launchpad Manager - Keep your Launchpad organised!][9] Manage macOS Launchpad with less pain
* [Tickeys | 找对打字的感觉 | YingDev][10]
* [docopt/docopt: Pythonic command line arguments parser, that will make you smile][11]

## Misc

* [A Javascript journey with only six characters][12] Create a Turing machine using only six characters `[`,`]`,`(`,`)`,`+` and `!`.
* [Dash and Apple: My Side of the Story][13] A popular app for developer has been [removed from apple store][14], and here is the story from the author.

[1]:    http://gad.qq.com/article/detail/7171237?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io
[2]:    https://code.facebook.com/posts/1840075619545360?utm_campaign=digest&utm_medium=email&utm_source=app
[3]:    https://blog.codeship.com/a-review-of-immutability-in-ruby/
[4]:    http://www.theverge.com/tldr/2016/9/25/12284400/how-to-read-more-books
[5]:    https://discussions.apple.com/thread/5522241?tstart=0
[6]:    http://furbo.org/2015/01/19/clearing-the-icon-services-cache-in-yosemite/
[7]:    https://sanctum.geek.nz/arabesque/advanced-vim-macros/
[8]:    https://sanctum.geek.nz/arabesque/vim-anti-patterns/
[9]:    http://launchpadmanager.com/
[10]:   http://www.yingdev.com/projects/tickeys
[11]:   https://github.com/docopt/docopt
[12]:   http://jazcash.com/a-javascript-journey-with-only-six-characters/
[13]:   https://blog.kapeli.com/dash-and-apple-my-side-of-the-story?utm_campaign=digest&utm_medium=email&utm_source=app
[14]:   https://blog.kapeli.com/apple-removed-dash-from-the-app-store#what-happened

