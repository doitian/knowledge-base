---
date: '2020-06-23T16:43:25+0800'
description: 'I use Alpine in WSL2 to run podman. The tool LxRunOffline can help to install Alpine, and podman is in the Alpine edge testing repository.'
---

# Podman on Windows via WSL2

#windows #wsl #container

I prefer using a dedicated WSL instance to run containers. So I'll install a minimal distribution, Alpine, to run podman.

Install the tool `LxRunOffline` first via scoop

```
scoop bucket add extras
scoop install lxrunoffline
```

Download Alpine root package from `https://lxrunoffline.apphb.com/download/Alpine`. See more distributions in [LxRunOffline Wiki](https://github.com/DDoSolitary/LxRunOffline/wiki).

Then create a WSL instance from the package

```
lxrunoffline.exe i -n Alpine -f alpine-minirootfs-3.12.0-x86_64.tar.gz -d "D:\WSL\Alpine" -v 2 -r .
```

This will install Alpine into folder `D:\WSL\Alpine`. Although `-v 2` is specified, but when I'm running it, the installed instance is still v1. It's easy to fix by migrating to version 2.

```
wsl --set-version Alpine 2
```

Now start the instance

```
wsl ~ -d Alpine
```

Edit `/etc/apk/repositories` to switch to edge and add testing repository.

```
http://dl-cdn.alpinelinux.org/alpine/edge/main
http://dl-cdn.alpinelinux.org/alpine/edge/community
http://dl-cdn.alpinelinux.org/alpine/edge/testing
```

Install `podman`

```
apk update
apk add podman
```

It's time to run Alpine inside Alpine

```
podman run --rm -it docker.io/alpine ash
```
