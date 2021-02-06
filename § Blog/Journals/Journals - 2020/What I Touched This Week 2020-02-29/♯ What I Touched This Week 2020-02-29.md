---
date: 2020-02-29
description: My weekly review report.
katex: true
series:
- What I Touched
---

# What I Touched This Week 2020-02-29

In the last week, I have posted 2 articles and recommended two web pages.

* [[♯ Excel as Diagram Maker]]
* [Paste Markdown as Code Block in Evernote](https://gist.github.com/9be340cba58cb459ed265f49202a05bf)
* [Mundo - Visualize your Vim Undo Tree](https://simnalamburt.github.io/vim-mundo/)
    I use Gundo before. This one can search though the changes history.
* [nervosnetwork/slice-cheatcheat](https://github.com/nervosnetwork/slice-cheatcheat)
    The trivial differences in the slice syntaxes are really disturbing when switching programming languages.

<!--more-->

# What Helped Me to Build the Blog

I have migrated a Ghost theme to Hugo for my blog.

-   [reuixiy/hugo-theme-meme](https://github.com/reuixiy/hugo-theme-meme)
    I often lost how to do a thing in Hugo. This theme often helps me to find the way.
-   [Ghost Theme Features: The Editor - Documentation](https://ghost.org/docs/api/v3/handlebars-themes/editor/)
    Since I migrated the theme from Ghost, this is a good reference to create the Hugo template which matches the CSS.
-   [The best Favicon Generator (completely free) | Favicon.io](https://favicon.io/favicon-generator/)
    I use this to generate a new favicon.
-   [Taxonomies | Hugo](https://gohugo.io/content-management/taxonomies/)
    -   I want to keep the "post" section before others in the home page, so I can create the file `content/post/_index.md` and set weight to -99 in Front Matters.
-   Hugo introduces page resources and image processing in newer versions. I can keep the images along with the post and it is also possible to resize the images to create responsive src set.
    -   [Page Bundles | Hugo](https://gohugo.io/content-management/page-bundles/)
    -   [Image Processing | Hugo](http://gohugo.io/content-management/image-processing/)
    -   [Hugo Page Resources, and how to use them... | Regis Philibert](https://regisphilibert.com/blog/2018/01/hugo-page-resources-and-how-to-use-them/)
-   [Custom Search Element Control API | Google Developers](https://developers.google.com/custom-search/docs/element)
    -   I use Google Custom Search in my blog. The API allows me to trigger the search by JavaScript.
        -   Use `google.search.cse.element.getElement` to find the element and use `element.execute('news')` to start a search.
        -   Setup the callback `__gcse.searchCallbacks.ready` to process the search result, and return `true` in the callback to prevent rendering the HTML in its own search page.
        -   Hide the custom search box and result page via CSS.

# What I Have Learned
-   [zsh: File Expansion](http://zsh.sourceforge.net/Doc/Release/Expansion.html)
    The extended file expansion is useful in zmv.

-   [Printing a sequence of letters or numbers | Shell Tips!](https://www.shell-tips.com/2008/01/14/printing-a-sequence-of-letters-or-numbers/)

    ```
    echo {a..g}
    ```

-   [Excel Array Formula Examples – Simple to Advanced](https://www.vertex42.com/blog/excel-formulas/array-formula-examples.html)

    <kbd>Ctrl+Shift+Enter</kbd>

-   [4 Ls Exercise](https://trello.com/templates/personal/4-ls-exercise-Bay7DwxN)
    The 4 L's exercise is designed for YOU as a LEADER or ROLE MODEL. How do you be the best version of YOU. Start by doing it for yourself first and then do it as a team.
-   [5 fun sprint retrospective ideas with templates - Work Life by Atlassian](https://www.atlassian.com/blog/jira-software/5-fun-sprint-retrospective-ideas-templates)
-   [Waveform – FFmpeg](https://trac.ffmpeg.org/wiki/Waveform)
    -   [A list of examples on how you can use filters to make visual representations of audio using ffmpeg](https://gist.github.com/seyoum/4455e9bed74241bfbd640a8083fd38b3)
-   [Using Filename Template Editor in Lightroom](https://photographylife.com/using-filename-template-editor-in-lightroom)
    Difference between Sequence \# and Image \#
-   [OpenPGP - The almost perfect key pair | Blog Eleven Labs](https://blog.eleven-labs.com/en/openpgp-almost-perfect-key-pair-part-1/)
-   [Geometric progression - Wikipedia](http://en.wikipedia.org/wiki/Geometric_progression)
    I have to use the formula to find the solution of a quiz in the Game Theory course.

    $$ \sum _{i=1} ^{n} {ar^{i-1}} = \frac{a(1 - r^n)}{1 - r} $$

    When p is between 0 and 1, and the sequence is infinite, the sum is

    $$ \sum _{i=1} ^{\infty} {ar^{i-1}} = \frac{a}{1 - r} $$

-   [How To Correctly Use AP (and APA) Style Title Case](https://www.bkacontent.com/how-to-correctly-use-apa-style-title-case/)

# What I Have Read
-   [作为一名本科生，我如何用 MarginNote 3 拆书](https://sspai.com/post/58621)
-   [2019 我的写作桌面清单推荐](https://sspai.com/post/58833)
-   [996 和 GTD 是同一块硬币的两面：对当代生活时间感知的反思 | 年度征文](https://sspai.com/post/58829)

# Related to COVID-19

-   [新冠病毒疫情与本世纪其他传染病疫情（非典，猪流感，中东呼吸综合症，埃博拉）时间点对比](https://twitter.com/doitian/status/1231077127765872641)

# Funny Things
-   [@sprezzaa: 哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈天津出租车](https://twitter.com/doitian/status/1228704476497879046)
-   [I Draw Like A Printer ( Drawing Will Smith ) - DP Truong](https://www.youtube.com/watch?v=qyW12gDeWPI)
    > Many people say that I can draw as if I were a printer. However, I think I still don't paint like a real printer. Today I'm going to draw the same way a printer does.

# Bookmarks I Saved
-   [yudai/gotty](https://github.com/yudai/gotty)
    Share your terminal as a web application
-   [Download Editable Video Templates - Envato Elements](https://elements.envato.com/video-templates/compatible-with-final-cut-pro?_ga=2.21989499.1362849140.1582036564-1530649263.1582036564&_gac=1.82340580.1582036564.Cj0KCQiAs67yBRC7ARIsAF49CdW27V0CoORg_po279xQMz_hIboHKSI8iY8dqXac94QJerBXlyTRLCkaAhagEALw_wcB)
-   [Premiere Pro and After Effects Templates, Stock Music, and more. | Motion Array](https://motionarray.com/browse?date_added=last-6-months&sort_by=most-popular&categories=final-cut-pro-templates&page=1&gclid=Cj0KCQiAs67yBRC7ARIsAF49CdWyiyz0rfky95TcmZJpB3MDW4JiCR0JuceuEH3swrYWOs2aLxio11waAjTCEALw_wcB)

