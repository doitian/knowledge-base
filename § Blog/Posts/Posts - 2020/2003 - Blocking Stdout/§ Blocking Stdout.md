---
date: '2020-03-01T09:29:40+0800'
tags: [ async-programming ]
---

# Blocking Stdout

When I first read Stjepan's article [Blocking inside async code](https://web.archive.org/web/20200815123809/https://stjepang.github.io/2019/12/04/blocking-inside-async-code.html), I never though I will met the problem mentioned in the post.

<!--more-->

> … I bet we all most of the time assume printing to standard output does not block while it really could.
>
> In case you’re wondering why `println!()` can block, imagine we executed `program1 | program2` in a shell so that the output of `program1` is piped into `program2`. If `program2` is reading input very slowly, then `program1` will have to block whenever it prints something and the pipe is full.

Fortunately, my brain has stored the clue somewhere, and I can retrieve it and save my day when I heart a weird bug.

We have a GUI app **N** written in Node which bundles a service binary **C**. **N** starts **C** as a sub-process. **C** writes logs to a file. After 10 minutes, it stops writing the log file until restarted.

**C** uses a single thread to write logs. But default, it sends the logs to both stdout and log file. When the stdout buffer of **C** is full, the logging thread stuck, so it also stops writing the log file.

A simple fix is telling **C** not write to stdout. But the root cause is that the app **N** keeps the child process stdout pipe open and never read from the pipe. The best practice is that if you don't read from the pipe, close it.

Following is an example In Node to close both stdin and stdout via [option stdio](https://nodejs.org/api/child_process.html#child_process_options_stdio). The stderr is open because the parent process will read from the pipe.

``` javascript
const c = spawn('c', [], {
  stdio: ['ignore', 'ignore', 'pipe']
});

c.stderr.on('data', (data) => {
  console.log(`c: ${data}`);
});
```
