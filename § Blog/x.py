#!/usr/bin/env python3

import os
from pathlib import Path

CONTENT_DIR = Path.home() / "codebase" / "my" / "iany.me" / "content"
print(CONTENT_DIR)

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.startswith('♯'):
            print(Path(root))
    print(root, "consumes", end=" ")
    print("bytes in", len(files), "non-directory files")
    if 'CVS' in dirs:
        dirs.remove('CVS')  # don't visit CVS directories
