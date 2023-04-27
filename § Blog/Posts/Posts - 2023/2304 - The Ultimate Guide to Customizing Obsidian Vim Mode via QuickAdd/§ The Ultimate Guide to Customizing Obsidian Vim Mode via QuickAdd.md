---
date: '2023-04-27T21:22:30+0800'
draft: false
aliases: ["The Ultimate Guide to Customizing Obsidian Vim Mode via QuickAdd"]
---

# The Ultimate Guide to Customizing Obsidian Vim Mode via QuickAdd

#obsidian #vim

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2023-04-27]]
**URL**:: [blog.iany.me](https://blog.iany.me/2023/04/the_ultimate_guide_to_customizing_obsidian_vim_mode_via_quick_add/)

Obsidian is my go-to note-taking app because of its availability on all desktop and mobile platforms with the bonus of Vim mode. In this guide, I'll show you how I customize the Vim mode in Obsidian to maximize my note-taking efficiency.

<!--more-->

## Setup User Launch Scripts via QuickAdd

To customize the Vim mode in Obsidian, JavaScript is the only solution. Obsidian allows running user scripts by implementing an plugin. I use an easy alternative to run a JavaScript file on launch via QuickAdd.

First, let’s create the JavaScript file in the vault. Save the skeleton below as the file `vimrc.js` in any folder in the vault. Keep in mind that Obsidian does not support editing JavaScript files, so use an external editor.

> [!file] vimrc.js
> ```javascript
> function notice(text) {
>   new Notice(text);
>   return text;
> }
>
> module.exports = async function (context) {
>   const vim = window.CodeMirrorAdapter?.Vim;
>   if (vim === undefined) {
>     new Notice(`🔴error: vim mode is disabled`);
>     return;
>   }
>
>   // Add customizations here.
>
>   console.log(`🔵info: vimrc loaded`);
> };
> ```

Then, install QuickAdd by browsing the community plugins in Settings and follow the instructions on the Obsidian help page [Community Plugins](https://help.obsidian.md/Extending+Obsidian/Community+plugins).

Finally, include the script in a QuickAdd macro and activate the option to execute the macro upon the plugin load.

1. Open the tab QuickAdd in Settings.
2. Click the button “Manage Macros”. In the pop-up dialog, fill in the macro name “vimrc” and click the button “Add macro“ to add a new macro vimrc.
3. Toggle the option “Run on plugin load” on under the newly created macro.
4. Configure the macro vimrc. Find the script file `vimrc` in the “User Scripts” section and add the script as the only step in the macro.

Attention that the script runs once on launch or reload. Running “Reload app without saving” via Command Palette will reload the file after changes,

## Vim Mode Customization Techniques

For the best tutorial on customizing Vim mode and what methods the `vim` object provides, refer to [how CodeMirror establishes the Vim mode](https://github.com/replit/codemirror-vim/blob/master/src/vim.js). I will only introduce the methods that I use in [my own customizations](https://github.com/doitian/quickadd-settings/blob/main/shore/quickadd/vimrc.js).

### `vim.defineEx`

The `defineEx` method enables users to execute a new ex command in Vim by typing `:` in normal mode. For instance, the ex command `:w` saves the file.

I introduce `defineEx` first because I need an ex command to run any Obsidian command so that I can use it to add key bindings later. I name this command `obr`, which is the abbreviation of **OB**sidian **R**un. The command requires the Obsidian command identifier as the argument, for example, `:obr app:open-settings` will open the Settings dialog.

```javascript
vim.defineEx("obr", "", function (cm, params) {
  if (params?.args?.length !== 1) {
    throw new Error(notice("🔴error: obr requires exactly 1 parameter"));
  }

  const command = params.args[0];
  context.app.commands.executeCommandById(command);
});
```

To find the command identifier, I add another ex command `:obl` to display a list of identifiers and copy the selected one. It accepts an argument to filter the result. For example, `obl open` will list identifiers that contain the word "open".

```javascript
vim.defineEx("obl", "", async function (cm, params) {
  let commands = Object.keys(context.app.commands.commands);
  for (const keyword of params?.args ?? []) {
    commands = commands.filter((command) => command.includes(keyword));
  }

  const choice = await context.quickAddApi.suggester(commands, commands);
  if (choice !== null) {
    await context.quickAddApi.utility.setClipboard(choice);
    new Notice(`🔵info: copied ${choice} to the clipboard`);
  }
});
```

### `vim.map`

The `vim.map` method takes two arguments,  `lhs` and `rhs`, which can both be either a key sequence or an ex command. The meaning of the method varies depending on the arguments passed.

- When both `lhs` and `rhs` are key sequence, it maps the key sequence `lhs` to `rhs`. For example, `vim.map('D', 'dd')` will redefine `D` to delete the whole line.
- When both `lhs` and `rhs` are ex commands, it creates a new ex command alias. For example, `vim.map(':Reload', ':obr app:reload')` adds the alias `:Reload` to run the Obsidian command `app:reload`.
- When `lhs` is a key sequence, and `rhs` is an ex command, it maps the key sequence to run the ex command. For example `vim.map('ZZ', ':obr app:reload')` allows reloading Obsidian by typing ZZ.
- When `lhs` is an ex command, and `rhs` is a key sequence, executing the ex command has the same effect as typing the key sequence.

I have a bunch of mappings from key sequences to `:obr`, for example, the z-family to operate on folds:

```javascript
vim.map("zo", ":obr editor:toggle-fold");
vim.map("zc", ":obr editor:toggle-fold");
vim.map("za", ":obr editor:toggle-fold");
vim.map("zR", ":obr editor:unfold-all");
vim.map("zM", ":obr editor:fold-all");
```

To use the space key as a key mapping prefix, it must first be `unmap`ped.

```javascript
vim.unmap("<Space>");
vim.map("<Space><Space>", ":obr switcher:open");
vim.map("<Space>n", ":nohl");
```

### `vim.defineAction` and  `vim.defineOperator`

We can use both action and operator in `vim.mapCommand`. The difference is that an operator performs upon text objects. See how CodeMirror defines the built-in [actions](https://github.com/replit/codemirror-vim/blob/7e70ff7d321f9aa6600616a4d2ee81327394533a/src/vim.js#L2450) and [operators](https://github.com/replit/codemirror-vim/blob/7e70ff7d321f9aa6600616a4d2ee81327394533a/src/vim.js#L2290).

I have an action `swapLine` to move lines around. It's not perfect, since undo will reverse one step only.

```javascript
vim.defineAction("swapLine", function(_cm, { repeat, down }) {
  const command = down ? "editor:swap-line-down" : "editor:swap-line-up";
  for (let i = 0; i < repeat; i++) {
    context.app.commands.executeCommandById(command);
  }
});
// undo after 5]e will only swap one line up.
vim.mapCommand("]e", "action", "swapLine", { down: true });
vim.mapCommand("[e", "action", "swapLine", { down: false });
```

The example for `vim.defineOperator` is `titleCase`, which formats the text in the [APA Title Case Capitalization](https://kb.iany.me/para/lets/w/Writing/Format+the+Title+Using+APA+Title+Case+Capitalization). For instance, `gzap` formats the current paragraph in the title case.

**Reference**:: [[Format the Title Using APA Title Case Capitalization]]

```javascript
function titleCase(str, options) {
  // See https://github.com/words/ap-style-title-case/blob/master/index.js how to format str to apa title case
}

// Following helper funnctions are borrowed from https://codemirror.net/5/keymap/vim.js
function cursorIsBefore(cur1, cur2) {
  if (cur1.line < cur2.line) {
    return true;
  }
  if (cur1.line == cur2.line && cur1.ch < cur2.ch) {
    return true;
  }
  return false;
}

function cursorMin(cur1, cur2) {
  return cursorIsBefore(cur1, cur2) ? cur1 : cur2;
}

function findFirstNonWhiteSpaceCharacter(text) {
  if (!text) {
    return 0;
  }
  var firstNonWS = text.search(/\S/);
  return firstNonWS == -1 ? text.length : firstNonWS;
}

vim.defineOperator("titleCase", function(cm, args, ranges, oldAnchor, newHead) {
  const selections = cm.getSelections();
  const newSelections = selections.map((s) =>
    titleCase(s, { keepSpaces: true })
  );
  cm.replaceSelections(newSelections);
  if (args.shouldMoveCursor) {
    return newHead;
  } else if (
    !cm.state.vim.visualMode &&
    args.linewise &&
    ranges[0].anchor.line + 1 == ranges[0].head.line
  ) {
    return {
      line: oldAnchor.line,
      ch: findFirstNonWhiteSpaceCharacter(cm.getLine(oldAnchor.line)),
    };
  } else if (args.linewise) {
    return oldAnchor;
  } else {
    return cursorMin(ranges[0].anchor, ranges[0].head);
  }
  return newHead;
});
vim.mapCommand("gz", "operator", "titleCase");
```
