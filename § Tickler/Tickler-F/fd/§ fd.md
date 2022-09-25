# fd

#command-line

> [fd](https://github.com/sharkdp/fd) is a program to find entries in your filesystem. It is a simple, fast and user-friendly alternative to [find](https://www.gnu.org/software/findutils/). While it does not aim to support all of find's powerful functionality, it provides sensible (opinionated) defaults for a majority of use cases.

I use fd as the my fzf default command using following configuration.

```shell
if command -v fd &> /dev/null; then
  export FZF_DEFAULT_COMMAND='fd --type f --hidden --follow --exclude ".git"'
  export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
  export FZF_ALT_C_COMMAND='fd --type d --no-ignore --hidden --follow --exclude ".git"'

  _fzf_compgen_path() {
    fd --type f --hidden --follow --exclude ".git" . "$1"
  }

  _fzf_compgen_dir() {
    fd --type d --no-ignore --hidden --follow --exclude ".git" . "$1"
  }
fi
```

It's convenient that it ignores files ignored by git, but sometimes I really want some ignored files appeared in the list. For example, we usually ignore config files and provide an example in the git repository, so changes to the config file will not mess up the repository.

Here is an example work directory that Git traces `config.ini.example` and ignores `config.ini`.

```shellsession
$ ls
config.ini
config.ini.example
```

There's a line in `.gitignore` that looks like

```
config.ini
```

I need to edit `config.ini` a lot, but my fzf list will not show it because git ignores it. The workaround is using the ignore file only supported by fd to negate the rule. Taking the example above, add the following line in file `.fdignore` or `.ignore`:

```
!config.ini
```

Now fzf will include `config.ini`.
