### Printing a sequence of letters or numbers in shell

[※ source](https://www.shell-tips.com/2008/01/14/printing-a-sequence-of-letters-or-numbers/)

Print a sequence of number

``` shell-session
$ seq 1 10
1 2 3 4 5 6 7 8 9 10

$ seq 0 2 10
0 2 4 6 8 10

$ echo {1..10}
1 2 3 4 5 6 7 8 9 10
```

Print a sequence of letters

``` shell-session
$ echo {a..g}
a b c d e f g
```