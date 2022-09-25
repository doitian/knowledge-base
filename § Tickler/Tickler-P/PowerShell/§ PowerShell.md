# PowerShell

#windows #command-line

⚡ Familiar key bindings

```
Set-PSReadLineOption -EditMode emacs
```

⚡ Default config file

```
$PROFILE
```

⚡ Quick Start

```
Get-Help
Get-Member
Where-Object (alias ?)
ForEach-Object (alias %)
Select-Object
Format-List
Out-GridView -PassThru
```

⚡ Gotchas

* Require `,` to separate multiple arguments: `rm a, b, c`

⚡ Count

```
Measure-Object
```

⚡ Write and Append

```
Set-Content
Add-Content
```

⚡ String Operators

String operators uses regular expressions.

```
"test" -Replace '^t', 'T'
```

⚡ Stop script on the first error

```
$ErrorActionPreference = "Stop"
```

[※ source](https://stackoverflow.com/a/9949909/667158)

⚡ `cd -`

Install PowerShell 7.0

```
iex "& { $(irm https://aka.ms/install-powershell.ps1) } -UseMSI"
```
