---
date: '2020-06-26T16:51:34+0800'
tags:
  - windows
  - wsl
obsidianFiles:
  - para/lets/w/Windows/LxRunOffline
---

# Move WSL to Another Drive

Following example moves the Ubuntu distribution to disk `D:\WSL\Ubuntu`.

<!--more-->

**Step 1**. Install Ubuntu in the Microsoft Store. Launch it to initialize the default instance. Create the user used in Ubuntu as prompted.

**Step 2**. Export the instance and import into the target directory.

```
cd D:\
mkdir WSL
cd WSL
mkdir Ubuntu
wsl --export Ubuntu .\Ubuntu\ext4.vhdx --vhd
wsl --unregister Ubuntu
wsl --import-in-place Ubuntu .\Ubuntu\ext4.vhdx
```

> [!hint]
> This is a faster version credited to Slawek. The old version has been moved to the chapter [[#Alternative Step 2 for WSL1]].

The commands above also unregister the default instance.

Command explanation:

- `wsl --export Ubuntu .\Ubuntu\ext4.vhdx --vhd`: Export the disk of the WSL instance with name `Ubuntu` into the file `ext4.vhdx` in the directory `.\Ubuntu\`. So you will get the file `D:\WSL\Ubuntu\ext4.vhdx`.
- `wsl --unregister Ubuntu`: Unregister the WSL instance with name `Ubuntu`.
- `wsl --import-in-place Ubuntu .\Ubuntu\ext4.vhdx`: The first `Ubuntu` is the new created instance name. This command will register a new instance using the disk file `.\Ubuntu\ext4.vhdx` in place. Keep in mind that if the disk file is deleted, the instance will crash and all the files within it will be permanently lost.

Now it is also OK to uninstall Ubuntu in the store.

**Step 3**. Set the default user for the moved Ubuntu.

In Step 1, you have created a user for Ubuntu. After export and import, the new instance will use root by default. If you want to continue to use that user, please configure it via registry table.

Find the directory in registry `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Lxss` which `DistributionName` is "Ubuntu". Set its `DefaultUid` to decimal 1000 (or hex 3e8).

Or create a file `/etc/wsl.conf` in the WSL instance with following contents:

```ini
[user]
default = yournamehere
```

**Step 4**. Migrate to WSL2

Use `wsl -l -v` to check whether the new created instance use WSL2. The command `wsl --set-version Ubuntu 2` upgrades an instance with name `Ubuntu` to version 2.

**Step 5**. Try wsl

```
wsl -d Ubuntu
```

An alternative solution is using the tool [[LxRunOffline]].

## Alternative Step 2 for WSL1

> [!info]
> This is the old version of step 2, which is slower but also works for WSL1.

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

Now it is also OK to uninstall Ubuntu in the store and continue to the **Step 3**.

