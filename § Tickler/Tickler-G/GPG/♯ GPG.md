# GPG

#softwareUsage

## Tips

⚡ Import key from key server

```
gpg --auto-key-locate keyserver --locate-keys name@example.com
# or
gpg --search-keys name@example.com
```

⚡ Change key server

Add in `~/.gnupg/gpg.conf`

```
keyserver hkps://keys.openpgp.org
```

⚡ Sign

```
gpg -sab -o - --yes -u 0x... file

# -s: sign
# -a: ascii armored
# -b: detach (standalone signature file)
# -o -: write to stdout
# --yes: force overwriting existing signature
# -u 0x...: choose the key (gpg --keyid-format 0xshort)
# file: file to be signed
```

⚡ Purge master key

Find the keygrip

```
gpg --with-keygrip --list-secret-keys
```

Remove the key from `~/.gnupg/private-keys-v1.d/` by keygrip.

⚡ List subkey ids

```
gpg -k --keyid-format long
```

/GPG in Linux Server.md