### How to obtain the first letter in a Bash variable?


[※ source](https://stackoverflow.com/questions/10218474/how-to-obtain-the-first-letter-in-a-bash-variable)

``` shell
word='tiger'
echo "${word::1}"
echo "${word}" | cut -c 1
echo "${word:0:1}"
```
