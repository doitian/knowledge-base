# Windows OpenSSH Server

#windows #ssh

⚡ Default Shell

```
New-ItemProperty -Path "HKLM:\SOFTWARE\OpenSSH" -Name DefaultShell -Value "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -PropertyType String -Force
```

[※ source](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_server_configuration)

⚡ Authorized Keys

The `authorized_keys` for users with administrator permissions is `C:\ProgramData\ssh\administrators_authorized_keys`. The following snippet fix the file permission

```
$acl = Get-Acl C:\ProgramData\ssh\administrators_authorized_keys
$acl.SetAccessRuleProtection($true, $false)
$administratorsRule = New-Object system.security.accesscontrol.filesystemaccessrule("Administrators","FullControl","Allow")
$systemRule = New-Object system.security.accesscontrol.filesystemaccessrule("SYSTEM","FullControl","Allow")
$acl.SetAccessRule($administratorsRule)
$acl.SetAccessRule($systemRule)
$acl | Set-Acl
```

[※ source](https://www.concurrency.com/blog/may-2019/key-based-authentication-for-openssh-on-windows)
