## GPG in Linux Server

I tried to setup GPG in a Linux server and met problems when performing
commands that require passphrase. It turns out that I have to set the
`GPG_TTY` to tell `gpg-agent` that it should ask password from current
console.

First kill the `gpg-agent`. Because it may already hang in the background to wait for
a password.

```
pkill -9 gpg-agent
```

Then set the environment variable for the current session

```
export GPG_TTY=$(tty)
```

Or save it for future sessions

```
echo 'export GPG_TTY=$(tty)' >> ~/.profile
```