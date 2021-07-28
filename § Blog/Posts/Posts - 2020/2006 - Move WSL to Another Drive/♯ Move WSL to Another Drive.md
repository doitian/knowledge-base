---
date: '2020-06-26T16:51:34+0800'
---

# Move WSL to Another Drive

#windows #wsl

Following example moves the Ubuntu distribution to disk `D:\WSL\Ubuntu`.

<!--more-->

**Step 1**. Install Ubuntu in the store. Launch it to initialize the default instance. Create the user used in Ubuntu as prompted.

**Step 2**. Export the instance and import into the target directory.

```
cd D:\
mkdir WSL
cd WSL
wsl --export Ubuntu ubuntu.tar
wsl --unregister Ubuntu
mkdir Ubuntu
wsl --import Ubuntu Ubuntu ubuntu.tar 
```

The commands above also unregister the default instance.

Now it is also OK to uninstall Ubuntu.

**Step 3**. Set the default user for the moved Ubuntu.

In Step 1, you have created a user for Ubuntu. After export and import, the new instance will use root by default. If you want to continue to use that user, please configure it via registry table.

Find the directory in registry `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Lxss` which `DistributionName` is "Ubuntu". Set its `DefaultUid` to decimal 1000 (or hex 3e8).

**Step 4**. Try wsl

```
wsl -d Ubuntu
```

An alternative solution is using the tool [LxRunOffline](https://github.com/DDoSolitary/LxRunOffline).
