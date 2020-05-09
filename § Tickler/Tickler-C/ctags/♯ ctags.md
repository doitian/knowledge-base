# ctags

#commandLine

⚡ Markdown

```
ctags \
  --langdef=markdown \
  --langmap=markdown:.md \
  --regex-markdown='/^# ([a-zA-Z0-9]+)/\1/' \
  -R
```

⚡ Include file name as tag

```
--extra=f
```