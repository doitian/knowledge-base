# Yubico (Fedora)

#linux #gpg #ssh

[※ reference](https://stafwag.github.io/blog/blog/2015/06/16/using-yubikey-neo-as-gpg-smartcard-for-ssh-authentication/)

Γ Install dependencies

```
sudo dnf install -y ykpers pcsc-tools opensc pcsc-lite
```

Γ Edit udev rules

Edit file `/usr/lib/udev/rules.d/69-yubikey.rules`

``` diff
ACTION!="add|change", GOTO="yubico_end"

# Udev rules for letting the console user access the Yubikey USB
# device node, needed for challenge/response to work correctly.

# Yubico Yubikey II
-ATTRS{idVendor}=="1050", ATTRS{idProduct}=="0010|0110|0111|0114|0116|0401|0403|0405|0407|0410"
+ATTRS{idVendor}=="1050", ATTRS{idProduct}=="0010|0110|0111|0114|0116|0401|0403|0405|0407|0410", OWNER="ian", MODE="0600"

LABEL="yubico_end"
```

Reload and check whether it works

```
udevadm control --reload
udevadm trigger
ykinfo -v
```

Γ Configure GPG agent

Edit `~/.gnupg/gpg-agent.conf`

```
default-cache-ttl 600
max-cache-ttl 7200
enable-ssh-support
```

Γ Enable and start the service

```
systemctl start pcscd
systemctl enable pcscd
```

Γ Troubleshooting

```
gpg-connect-agent updatestartuptty /bye
```
