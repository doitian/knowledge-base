# Windows Proxy Setting

#windows #proxy

## System Proxy

/windows-system-proxy.png fit

## UWP

Open PowerShell as admin (<kbd>Win+X A</kbd>), find the UWP package, for example, Microsoft Store


```
Get-AppxPackage -Name '\*Store\*'
```

Once the target app is located, get its package family name.

```
$pkg = (Get-AppxPackage -Name Microsoft.WindowsStore).PackageFamilyName
```

Add it to loopback exempt list

```
CheckNetIsolation LoopbackExempt -a "-n=$pkg"
```

Reopen Windows Store to see whether it can load the page.

If it still does not work, try clearing the list first and add packages again.

```
CheckNetIsolation LoopbackExempt -c
CheckNetIsolation LoopbackExempt -a "-n=$pkg"
```

Some apps depend on `AuthHost`, such as Nebo. I have tried using the package family name to add `AuthHost` but failed, so I use SID instead:

```
CheckNetIsolation.exe loopbackexempt -a "-p=S-1-15-2-2750798217-1343590035-1234819260-1030354384-3318145141-3720257911-3461195215"
```

The SID is found by searching "AuthHost" inside the registry `HKEY_CURRENT_USER\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Mappings`.

See [Web authentication broker - UWP applications](https://docs.microsoft.com/en-us/windows/uwp/security/web-authentication-broker) for details.

## Scoop

```
scoop config proxy 127.0.0.1:7890
```

## Git

```
git config --global http.proxy http://127.0.0.1:7890
```

## Putty And Plink

/putty-proxy.png fit

## Aria2

```
aria2c --all-proxy 127.0.0.1:7890 http://path/to/file.txt
```

## WSL2

First bind the proxy on 0.0.0.0 and find the host IP address. It can be automated by calling `powershell.exe` in WSL2

```
IP="$(powershell.exe -NoProfile -Command "(Get-NetIPAddress -InterfaceAlias Wi-Fi -AddressFamily IPv4).IPAddress | Write-Host -NoNewLine")"

export https_proxy=http://$IP:7890
export http_proxy=http://$IP:7890
export all_proxy=http://$IP:7891
```
