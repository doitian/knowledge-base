### How to get the source directory of a Bash script from within the script itself?

[※ source](https://stackoverflow.com/a/246128/667158)

``` shell
#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
```