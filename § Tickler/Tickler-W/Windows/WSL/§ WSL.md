# WSL

#windows

**I started using WSL from version 2, so the following tips may only work for version 2.**

⚡ LxRunOffline

[LxRunOffline](https://github.com/DDoSolitary/LxRunOffline/wiki) is a command line tool to manage WSL instances. It also can install many Linux distributions that are not listed in Microsoft Store.

I also have written a [script wrapper](https://github.com/doitian/dotfiles-windows/blob/master/bin/Install-WSL.ps1) to manage the WSL instances.

⚡ Use Windows Executable

WSL can use Windows executable directly. For example

```
sudo ln -snf "$(which git.exe)" /usr/bin
```

This allows WSL to use the `git.exe` in Windows as `git`.

Another example is using `powershell` to get the host IP:

```
powershell.exe -NoProfile -Command "(Get-NetIPAddress -InterfaceAlias Wi-Fi -AddressFamily IPv4).IPAddress | Write-Host -NoNewLine"
```

⚡ Port Forward

The ports listened on 0.0.0.0 in WSL2 are automatically forwarded to Windows.

For example, running `python3 -m http.server` in WSL, the browser in Windows can open `http://localhost:8000` directly.

But this does not work reversely. WSL instance cannot access Windows ports via `localhost` nor `127.0.0.1`. An workaround is using the public IP of the Windows.
