# Linux Hostname

#linux

⚡ Set only hostname

For example, `n1`

```
sudo hostname n1
echo n1 | sudo tee /etc/hostname
```

Edit `/etc/hosts`, and add `n1` for `127.0.1.1`

```
127.0.1.1 n1
```

⚡ Set fully qualified domain name 

For example, `n1.iany.me`

```
sudo hostname n1
echo n1 | sudo tee /etc/hostname
```

Edit `/etc/hosts`, and add both `n1` and `n1.iany.me` for `127.0.1.1`

```
127.0.1.1 n1 n1.iany.me
```
