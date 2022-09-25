# Encryption Tools

#security #cryptography

## Encryption

⚡ GPG

[※ source](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#limits-for-secrets)

Encrypt the file with passphrase

```
gpg --symmetric --cipher-algo AES256 my_secret.json
```

Decrypt the file

```
gpg --quiet --batch --yes --decrypt --passphrase="$GPG_PASSPHRASE" --output my_secret.json my_secret.json.gpg
```

⚡ Age

[FiloSottile/age: A simple, modern and secure encryption tool with small explicit keys, no config options, and UNIX-style composability.](https://github.com/FiloSottile/age)

⚡ Gocryptfs

[rfjakob/gocryptfs: Encrypted overlay filesystem written in Go](https://github.com/rfjakob/gocryptfs)

Mount encrypted files. This tool can be used to synchronize encrypted files via cloud services such as iCloud, Dropbox and etc.

⚡ Apple Encrypted Image

This is macOS Only.

* Create new blank image in Disk Utility

## Encrypt and Share

* [schollz/croc: Easily and securely send things from one computer to another](https://github.com/schollz/croc)
* [Firefox Send](https://send.firefox.com/)
