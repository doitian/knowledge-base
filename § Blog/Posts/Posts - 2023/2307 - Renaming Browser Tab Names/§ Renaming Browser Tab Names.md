---
date: "2023-07-21T20:31:59+0800"
draft: false
aliases:
  - Renaming Browser Tab Names
tags:
- browser
- javascript
- productivity
---

# Renaming Browser Tab Names

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2023-07-21]]
**URL**:: [blog.iany.me](https://blog.iany.me/2023/07/renaming-browser-tab-names/)

Renaming browser tab names may seem like a simple task, but it can actually be quite challenging.

<!--more-->

Most browsers sync the tab name with the web page title. Therefore, it seems simple to set tab name by setting `document.title`:

```javascript
document.title = "Custom Tab Name";
```

However, many web pages use JavaScript to alter the page title, which would override the custom name. While [`Object.defineProperty`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty) in JavaScript can override the property setter function, it's not possible to access the original setter function for `document.title`. Fortunately, browsers sync page titles with the first `<title>` tag, so setting its content acts as a workaround to set the page title.

Here is the bookmark for renaming a tab. I also add `%t` as the token for the original page tab title. This is handy such as adding a custom prefix with `Work: %t`, or restoring the original title without reloading the page by using `%t`.

```javascript
// Rename the document title using a bookmarklet.
//
// As a user,
// - Once I have renamed the tab, it should not be overwritten.
// - I can include the token %t as placeholder for the real title.
// - To restore, I can rename the tab to %t
//
// Install: Copy the code to
//
//     https://caiorss.github.io/bookmarklet-maker/
//
// and generate the bookmarklet.

// Init only once
if (!("_renameTitle" in document)) {
  // Force creating the title tag.
  document.title = document.title || "";

  const titleEl = document.getElementsByTagName("title")[0];
  const titleTokenRegex = /%t/g;

  // Remembers the real title
  let titleWithoutRenaming = document.title;
  // User set title
  let titleWithRenaming = "";

  // Rename the document title to v.
  // If v contains the token %t, replace all occurences to the
  // real title.
  document._renameTitle = (v) => {
    titleWithRenaming = v;
    titleEl.innerText = v.replace(titleTokenRegex, titleWithoutRenaming);
  };

  Object.defineProperty(document, "title", {
    // Other code will use document.title setter to change the title.
    //
    // Remember the new value as the real title but still use the
    // title set by user.
    set: (v) => {
      titleWithoutRenaming = v;

      // Once document has defined the title property, its value is
      // not synchronized to the tab name.
      //
      // Here uses a workaround to set the title tag content.
      titleEl.innerText = titleWithRenaming.replace(titleTokenRegex, v);
    },
    get: () => titleEl.innerText,
  });
}

const title = prompt(
  "Rename tab (Use token %t for original title)",
  document.title
);
// title is null when user cancel the dialog.
if (title !== null) {
  document._renameTitle(title);
}
```
