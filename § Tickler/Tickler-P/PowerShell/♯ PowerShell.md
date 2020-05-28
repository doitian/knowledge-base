# PowerShell

#windows #commandLine

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
