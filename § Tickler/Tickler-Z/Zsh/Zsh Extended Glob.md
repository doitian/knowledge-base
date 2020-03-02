## Zsh Extended Glob

[※ source](http://zsh.sourceforge.net/Doc/Release/Expansion.html#Glob-Operators)

* `*`, `?`: same with `.*` and `.` in regular expression.
* `[[:digit:]]`, `[^[:digit:]]`: char class.
* `<x-y>`: number in the range x to y, inclusive.
* `##` `#`: similar to the `+` and `*` in regular expression.
* `(...)`: group
* `x|y`: x or y
* `x-y`: x but not y
* `^x`: not x