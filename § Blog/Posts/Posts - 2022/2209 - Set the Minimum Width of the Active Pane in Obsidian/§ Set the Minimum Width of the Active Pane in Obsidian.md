---
date: '2022-09-23T16:44:51+0800'
aliases: ["Set the Minimum Width of the Active Pane in Obsidian"]
tags:
- css
- obsidian
- productivity
---

# Set the Minimum Width of the Active Pane in Obsidian

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2022-09-23]]
**Reference**:: [[Obsidian QuickAdd Plugin]]
**Reference**:: [[Obsidian Excalibrain Plugin]]
**Friend**:: [[Obsidian Min Width Plugin]]
**URL**:: [blog.iany.me](https://blog.iany.me/2022/09/set-the-minimum-width-of-the-active-pane-in-obsidian/)

> [!info] Updates
> I have created [an plugin](https://github.com/doitian/obsidian-min-width) for this feature.

A simple CSS rule sets the minimum width of the active pane in Obsidian.

<!--more-->


> [!file] min-width.css
> ```css
> .mod-root .mod-active {
>   min-width: min(88%, 40rem);
> }
> ```

It sets the minimum width to either 40 columns or 88% of the whole editing area, depending on which is smaller. Obsidian will auto resize the active pane to ensure it is wider enough and shrink other panes accordingly.

The snippet does not work in horizontal splits where panes stack vertically. See the chapter [[#JavaScript Helper]] below how to work around it.

## How to Add CSS Snippets in Obsidian

Save the CSS snippet as file `.obsidian/snippets/min-width.css` in the vault. Create the folder `.obsidian/snippets` if it does not exist.

Now the file should appear in the Appearance settings page. Toggle the switcher to enable the CSS snippet in the file.

![[enable-obsidian-min-width-css-snippet.png|Enable CSS Snippet in Obsidian]]

## JavaScript Helper

CSS is useless when it can not select the target elements. To make the snippet work in horizontal splits, the CSS rule has to select the `.mod-horizontal` node when it has a `.mod-active` child. However, the pseudo-class selector `:has()`[^1] is not available in Obsidian yet.

JavaScript can help to add classes and attributes to HTML elements.

I also want to make some panes wider, such as Excalibrain[^2]. The JavaScript code can also set the view type to the proper elements. The view type of the Excalibrain pane is `excalidraw`.

First, update the CSS snippet to make Excalibrain panes wider. Indeed, it makes all Excalidraw panes wider.


> [!file] min-width.css
> ```css
> .mod-root .mod-active {
>   min-width: min(88%, 40rem);
> }
>
> .mod-root .mod-active[data-type="excalidraw"] {
>   min-width: min(88%, 60rem);
> }
> ```

The last, let Obsidian run some code when the active pane has changed. I use QuickAdd[^3] to manage the scripts. Save the following code snippet as `min-width.js` in the vault.

> [!file]- min-width.js
> ```javascript
> const DATA_TYPE = "data-type";
>
> function setOrRemoveDataType(el, dataType) {
>   if (dataType !== undefined) {
>     el.setAttribute(DATA_TYPE, dataType);
>   } else {
>     el.removeAttribute(DATA_TYPE);
>   }
> }
>
> module.exports = async function ({ app }) {
>   app.workspace.on("active-leaf-change", (leaf) => {
>     // clear .mod-active on .mod-horizontal
>     for (const el of app.workspace.containerEl.getElementsByClassName(
>       "mod-active mod-horizontal"
>     )) {
>       el.classList.remove("mod-active");
>     }
>
>     // bubble up data-type
>     const dataType = leaf.containerEl
>       .getElementsByClassName("workspace-leaf-content")[0]
>       ?.getAttribute(DATA_TYPE);
>     setOrRemoveDataType(leaf.containerEl, dataType);
>
>     // add .mod-active and data-type to current horizontal split container
>     const parentNode = leaf.containerEl.parentNode;
>     if (parentNode.classList.contains("mod-horizontal")) {
>       parentNode.classList.add("mod-active");
>       setOrRemoveDataType(parentNode, dataType);
>     }
>   });
> };
> ```

Then run it when Obsidian starts by following these steps:

1. Click the button "Manage Macros" in the QuickAdd settings.
2. Add a new macro and add the user script "min-width" to the macro.
3. Save the macro and check the option "Run on plugin load".

![[add-obsidian-min-width-macro.png|Add a Macro]]
![[run-min-width-script-on-plugin-load.png|Run on plugin load|fit|Run JavaScript Code on Start With QuickAdd]]

That's it. Restart Obsidian and the code should be effective. See how it works in the screen recording below.

[Vimeo - Set the Minimum Width of the Active Pane in Obsidian](https://vimeo.com/752964835)

There are two extra plugins used in the video, Snippet Commands[^4] and Cycle through Panes.[^5]

## Similar Work

This work is inspired by the Vim option `winwidth`, one of my favorite feature of Vim.

The awesome plugin Sliding Panes[^6] provides the similar feature for Obsidian. However, it has three problems that I cannot stand.

The first, when the option "Leaf Width on Desktop/Mobile" is wider than the whole editing area, I have to scroll horizontally to see the current active pane. Although the plugin has separated the options for Desktop and Mobile, but different devices have different screen sizes. What's worser, the app window can be any size on Desktop. The option must be less than the smallest screen width when Obsidian Sync is in use, which is not a good choice for wider devices.

The second, the plugin does not play well with horizontal splits.

The last, I really want to set the different minimum widths for different windows.

## References

[^1]: MDN. (2016, October 27). :_has() - CSS: Cascading Style Sheets_. MDN. https://developer.mozilla.org/en-US/docs/Web/CSS/:has
[^2]: zsviczian. (2022, May). _Excalibrain: A Graph View to Navigate Your Obsidian Vault_. GitHub. https://github.com/zsviczian/excalibrain
[^3]: chhoumann. (2021, June). _QuickAdd for Obsidian_. GitHub. https://github.com/chhoumann/quickadd
[^4]: deathau. (2021, October). _Snippet Commands Obsidian Plugin_. GitHub. https://github.com/deathau/snippet-commands-obsidian
[^5]: phibr0. (2020, November). _Cycle Through Panes Obsidian Plugin_. GitHub. https://github.com/phibr0/cycle-through-panes
[^6]: deathau. (2020, October). _Sliding Panes (Andy Matuschak Mode) Obsidian Plugin_. GitHub. https://github.com/deathau/sliding-panes-obsidian
