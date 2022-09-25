# Pandoc

#command-line

┌ Clean Markdown

```
pandoc --wrap=none --markdown-headings=atx --from html --to markdown_strict-raw_html-native_divs-native_spans
```

┌ Offline HTML


```
pandoc --from html --to html5 --self-contained
```

┌ Readable HTML

```
pandoc --from html --to html5 --standalone
```
