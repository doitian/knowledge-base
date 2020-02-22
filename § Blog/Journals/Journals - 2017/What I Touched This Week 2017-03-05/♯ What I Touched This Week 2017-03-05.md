---
date: 2017-03-05
description: My weekly review report.
series:
- What I Touched

---

# What I Touched This Week 2017-03-05


- Allow password input in `go get`

```
env GIT_TERMINAL_PROMPT=1 go get xxxx
```

- [Getting the source directory of a Bash script from within][1]
- [Vcpkg updates: Static linking is now available][2]
- and how to [replace MD with MT][3] when using static linking. 
- [Rancher][4] is a self hosted platform to run containers.
- [Pushpin][5] is a reverse proxy to handle websocket connections.

Configure max number of open files in:

supervisor

	[supervisord]
	minfds = 1000000

upstart

	limit nofile 1000000 1000000

/etc/security/limits.conf

	* hard nofile 1000000
	* soft nofile 1000000

[1]:	http://stackoverflow.com/a/246128/667158
[2]:	https://blogs.msdn.microsoft.com/vcblog/2016/11/01/vcpkg-updates-static-linking-is-now-available/
[3]:	http://stackoverflow.com/a/14172871/667158
[4]:	http://rancher.com/
[5]:	http://pushpin.org/docs/about/

