---
date: '2012-02-04'
description: Display line wrap indicator in gutter using CSS
title: CSS Line Wrap Indicator
---

# Css Line Wrap Indicator

#css #html

Many editor can wrap a line that reaches the window width and show an indicator in the margin, for example, Emacs.

/emacs.png "Emacs line wrap with bent arrow in fringe"

I want to add such line wrap indicators to the code block in HTML. It is easy to add indicators as background image in CSS. But the indicators should only be shown when the line is wrapped. And from the figure, the wrap indicator is not displayed on the last line in the right margin, and not on the first line in the left margin. There's a `:first-line` pseudo element selector, there's no `:last-line`. However, it can be achieved by using `:before` and `:after` with position trick.

You can check the result in this [jsfiddle](https://jsfiddle.net/doitian/97bfwx6q/5/). Resize the result panel to see the line wrap indicators. Following is a detailed explanation.

<!--more-->

## Add Line Markup ##

First, the code block in pre must be split by lines and add markup so that CSS can be applied.

    <pre><code>(font-lock-add-keywords
    'ruby-mode
    '(("\\(\\b\\sw[_a-zA-Z0-9]*:\\)\\(?:\\s-\\|$\\)" (1 font-lock-constant-face))))
    </code></pre>

is converted to

    <pre><code><span class="line">(font-lock-add-keywords
    </span><span class="line"> 'ruby-mode
    </span><span class="line"> '(("\\(\\b\\sw[_a-zA-Z0-9]*:\\)\\(?:\\s-\\|$\\)" (1 font-lock-constant-face))))
    </span></code></pre>

It is easy to do such conversion by replace new line character `\n` to `\n</span><span class="line">` and then wrap with first open tag and the last close tag.

Because I want to show indicators in left, right padding of `span.line`, it should be displayed as block to expand horizontally. Also enable line wrap on `pre`.

``` css
pre {
  white-space: pre-wrap;
}
pre code, span.line {
  display: block;
}
```

Pay attention to the new line position. It is included in the added
`span.line` elements. Otherwise extra empty line is added between lines.

## Add Indicators ##

The indicators are added through `:before` and `:after`. They have the same height with the line by setting `height` to `100%`.

To ensure the indicators are aligned to each wrapped line, the picture must be the same height with `line-height`.

I use following two icons. The height is 28px. So also set `span.line`
`line-height` to 28px.

- Left: ![left line wrap indicator](./line-left.png)
- Right: ![right line wrap indicator](./line-right.png)

``` css
span.line {
  line-height: 28px;
}
```

Then just add `:before` and `:after` and apply vertically repeat background on them. `position` of `span.line` is set to `relative` so `:before` and `:after` can be positioned relative to it. It is easy to add them in `span.line` padding. I use padding instead of margin because later I'll set overflow to hidden to hide indicators outside of `span.line`, where margin is considered outside.

``` css
span.line {
  padding: 0 13px; /* 8px for indicator, 5px for space around text */
  position: relative;
}
span.line:before, span.line:after {
  background-repeat: repeat-y;
  content: "";
  display: block;
  width: 10px;
  height: 100%;
  position: absolute;
}
span.line:before {
  background-image: url("line-left.png");
  top: 0;
  left: 1px;
}
span.line:after {
  background-image: url("line-right.png")
  top: 0;
  right: -1px;
}
```

Now the indicators are shown in left and right padding on all lines. Use `top` to shift down left indicators and `bottom` to shift up right indicators, so left indicator is not shown on the first line and right indicator is not shown on the last line. But some indicators are moved out, use `overflow:hidden` to hide them.

``` css
span.line {
  overflow: hidden;
}
span.line:before {
  top: 28px;
}
span.line:after {
  top: auto;
  bottom: 28px;
}
```

## Add Color to Padding

Use border and background on `pre` to add different color to indicators padding and code block. Use negative margin to align indicators to the
borders.

``` css
pre {
  border-style: solid;
  border-color: #EEE;
  border-width: 0 8px;
  background-color: #AAA;
}
span.line {
  margin: 0 -8px;
}
```
