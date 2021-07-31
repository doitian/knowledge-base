# Fedora on Parallels

#linux #macos

## Apply Patch on Parallels Tools

[※ source](https://forum.parallels.com/threads/patch-for-kernel-5-6.349625/#post-866127)

Copy the iso content out

```
cp -r /run/mnt/cdrom/* ~/pt
```

Extract

```
tar xvf prl_mod.tar.gz
```

Apply patch

```
patch -p1 < pt-15.1.4.47270-linux-5.6.txt
```

Package

```
tar zcvf prl_mod.tar.gz . dkms.conf Makefile.kmods
```

Install

```
sudo ./install
```