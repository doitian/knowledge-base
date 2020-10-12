# Neomutt

#mail #commandLine

## GPG

Start with the default config (`/etc/neomuttrc.d/gpg.rc` in Ubuntu). This config uses a helper executable `pgpewrap`. It can be found as `/usr/lib/neomutt/pgpewrap` in Ubuntu, and `/usr/local/Cellar/neomutt/*/libexec/neomutt/pgpewrap` in macOS Homebrew.

I added following extra options:

```
# Extra options
set crypt_autosign
# set crypt_opportunistic_encrypt
set crypt_replysign
set crypt_replysignencrypted
set postpone_encrypt
```

Use shortcut `p` to show the PGP menu and choose the operations.

To encrypt the email, sender and all recipients must have the trusted public keys in the local key chain.

Example to trust a key:

```
$ gpg --edit-key KEYID

gpg> trust
```
