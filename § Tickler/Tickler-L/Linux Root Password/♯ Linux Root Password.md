# Linux Root Password

#linux #systemAdmin

## Fedora

Edit Grub line by pressing `e` in the bootstrap screen. Add following options to the `linux` line.

```
rd.break enforcing=0
```

This will boot the system into root shell. Mount the system root and `chroot` into it.

```
mount -o remount,rw /sysroot/
chroot /sysroot
```

Now use `passwd` to change the root password, or perform other maintenance tasks.
