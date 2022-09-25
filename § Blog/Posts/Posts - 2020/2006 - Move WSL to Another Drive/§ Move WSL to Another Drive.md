---
date: '2020-06-26T16:51:34+0800'
---

# Move WSL to Another Drive

#windows #wsl

Following example moves the Ubuntu distribution to disk `D:\WSL\Ubuntu`.

<!--more-->

**Step 1**. Install Ubuntu in the Microsoft Store. Launch it to initialize the default instance. Create the user used in Ubuntu as prompted.

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

Command explanation:

- `wsl --export Ubuntu ubuntu.tar`: Export the WSL instance with name `Ubuntu` into the file `ubuntu.tar` in the current directory. So you will get the file `D:\WSL\ubuntu.tar`.
- `wsl --unregister Ubuntu`: Unregister the WSL instance with name `Ubuntu`.
- `wsl --import Ubuntu Ubuntu ubuntu.tar`: The first `Ubuntu` is the new created instance name. The second `Ubuntu` is the instance saved location. The last parameter is the file created by `wsl --export`. This will import `ubuntu.tar` and use `D:\WSL\Ubuntu` to save the WSL instance data.

Now it is also OK to uninstall Ubuntu in the store.

**Step 3**. Set the default user for the moved Ubuntu.

In Step 1, you have created a user for Ubuntu. After export and import, the new instance will use root by default. If you want to continue to use that user, please configure it via registry table.

Find the directory in registry `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Lxss` which `DistributionName` is "Ubuntu". Set its `DefaultUid` to decimal 1000 (or hex 3e8).

**Step 4**. Migrate to WSL2

Use `wsl -l -v` to check whether the new created instance use WSL2. The command `wsl --set-version Ubuntu 2` upgrades an instance with name `Ubuntu` to version 2.

**Step 5**. Try wsl

```
wsl -d Ubuntu
```

An alternative solution is using the tool [[§ LxRunOffline]].
