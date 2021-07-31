# Bash

#command-line

⚡ Shebang

```
#!/usr/bin/env bash

set -e
set -u
[ -n "${DEBUG:-}" ] && set -x || true
```

⚡ Read array

```
readarray -t FILES < <(ls)
```

⚡ If string like

```
[[ "$x"  == *"foo"* ]]
```
