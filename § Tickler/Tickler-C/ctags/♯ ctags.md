# ctags

#commandLine

⚡ Markdown

```
  --langdef=markdown \
  --langmap=markdown:.md \
  --regex-markdown='/^# ([a-zA-Z0-9]+)/\1/' \
```

⚡ Ansible

```
  --langdef=ansible \
  --langmap=ansible:.yml.yaml \
  --regex-ansible=/^[ \t]*-[ \t]*name:[ \t]*(.+)/\1/k,tasks/ \
  --languages=ansible,ruby,python
```

⚡ Include file name as tag

```
--extra=f
```