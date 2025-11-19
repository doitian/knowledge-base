---
comment: true
date: "2017-03-19T17:54:08+08:00"
description: Share scripts to capture anything using macOS Javascript automation
katex: false
series:
- macOS Automation
share: true
title: Capture Anything using macOS Javascript automation
tags:
- automation
- javascript
- macos
---

# Capture Anything using macOS Javascript automation

I have written many scripts to automate the work in macOS. This one is the most frequently used one. The script can capture the current selection in frontend most app in OmniFocus, and I can jump back to the app using URL.

<!--more-->

It only supports apps I frequently use. New app support can be added in `capturers` map.

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

// Then send tasks to OmniFocus or other app which supports Applescript automation.
var of = Application("OmniFocus");
var inbox = of.quickEntry().inboxTasks;
tasks.forEach(function(task) {
  inbox.push(of.Task(task));
});

of.quickEntry().open();
```

I use [Keyboard Maestro](https://www.keyboardmaestro.com/main/) to invoke the script using keyboard shortcut.
