# ctags

#commandLine

Ctags will append options listed in `.ctags` file.

⚡ Markdown

```
--langdef=markdown
--langmap=markdown:.md
--regex-markdown=/^# ([a-zA-Z0-9]+)/\1/h,headings/
```

⚡ Ansible

```
--langdef=ansible
--langmap=ansible:.yml.yaml
--regex-ansible=/^[ \t]*-[ \t]*name:[ \t]*(.+)/\1/t,tasks/
--languages=ansible,ruby,python
```

⚡ Include file name as tag

```
--extra=f
```
