---
comment: true
date: '2017-03-19T17:54:13+08:00'
description: 分享用来在各种 App 中收集任务的 macOS Javascript 自动化脚本
katex: false
series:
- macOS Automation
share: true
title: 使用 macOS Javascript 自动化来集成各种 App 的任务收集
---

# 使用 macOS Javascript 自动化来集成各种 App 的任务收集

#macOS

我写了不少 macOS 脚本来自动化我的工作。这个脚本可以是用的最多的。我用它来在各种 App 中，将当前选中的对象做为任务添加到 OmniFocus 中。通过捕获的链接可以在 OmniFocus 中直接打开相关的文档。

<!--more-->

目前该脚本仅支持我经常使用的一些 App，新的 App 只需要在 `capturers` 增加相应的捕获方法即可。

```javascript
var tasks = [];
var app = null;

// Uncomment following line to debug a specific app.
// var app = Application("Evernote");

(function(app, tasks) {
  var bundleIdentifier;

  if (app === null || app === undefined) {
    var systemEvents = Application("System Events");
    var bundleIdentifier = systemEvents.processes.whose({ frontmost: true })[0].bundleIdentifier();
    app = Application(bundleIdentifier);
  } else {
    bundleIdentifier = app.id();
  }

  if (tasks === null || tasks === undefined) {
    tasks = [];
  }

  var capturers = {
    Safari: function(app, tasks) {
      var tab = app.windows[0].currentTab();
      tasks.push({ name: tab.name(), note: tab.url() });
    },

    Chromium: function(app, tasks) {
      var tab = app.windows[0].activeTab();
      tasks.push({ name: tab.title(), note: tab.url() });
    },

    Finder: function(app, tasks) {
      app.selection().forEach(function(file) {
        var name = file.name();
        var url = file.url();
        var directory = file.container().url();

        tasks.push({ name: "[File] " + name, note: url + " in directory " + directory });
      });
    },

    Contacts: function(app, tasks) {
      app.selection().forEach(function(contact) {
        tasks.push({ name: "Contact " + contact.name(), note: "addressbook://" + contact.id() });
      });
    },

    Evernote: function(app, tasks) {
      app.selection().forEach(function(note) {
        var url = note.noteLink();
        var title = note.title();

        tasks.push({ name: "[Evernote] " + title, note: url });
      });
    },

    Mail: function(app, tasks) {
      app.selection().forEach(function(mail) {
        var url = encodeURI("message://<" + mail.messageId() + ">");
        var title = mail.sender() + ": " + mail.subject();

        tasks.push({ name: title, note: url });
      });
    }
  };

  capturers["Google Chrome"] = capturers.Chromium;

  var fluidCapturer = function(app, tasks) {
    var tab = app.browserWindows[0].selectedTab();
    var name = "[" + app.name() + "] " + tab.title();
    tasks.push({ name: name, note: tab.url() });
  };

  var defaultCapturer = function(app, tasks) {
    app.includeStandardAdditions = true;
    var url = encodeURI("file://" + app.pathTo().toString());
    tasks.push({ name: app.name(), note: url })
  };

  var capture = capturers[app.name()];
  if (capture === undefined) {
    if (bundleIdentifier.startsWith("com.fluidapp.FluidApp.")) {
      capture = fluidCapturer;
    } else {
      capture = defaultCapturer;
    }
  }

  capture(app, tasks);

  return tasks;
})(app, tasks);

// Then send tasks to OmniFocus or other app which supported apple scripts automation.
var of = Application("OmniFocus");
var inbox = of.quickEntry().inboxTasks;
tasks.forEach(function(task) {
  inbox.push(of.Task(task));
});

of.quickEntry().open();
```

我使用的是 [Keyboard Maestro](https://www.keyboardmaestro.com/main/) 通过快捷键来执行该脚本。
