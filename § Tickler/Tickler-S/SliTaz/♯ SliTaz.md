# SliTaz

#linux

[SliTaz](http://www.slitaz.org/en/) is a Linux distribution with a small size.

## Install in Parallels

Use `msdos` partition table.

The default kernel drivers does not support Virtio. Configure the virtual machine to use `Intel (R) PRO/1000 MT` first and install `linux-kvm`.

```
sudo tazpkg recharge
sudo tazpkg -gi linux-kvm
```

Then shutdown and switch back to `Virtio network adapter`.

Sometimes the host sets up network interface in `eth1` instead of `eth0` after clone. Update the interface name in `/etc/network.conf` and restart the network.

```
sudo /etc/init.d/network.sh restart
```

## Boot Configuration

The boot is configured in `/etc/rcS.conf`.

* Set `LOGIN_MANAGER=''` to disable X.
* Edit `RUN_DAEMONS` to change auto started services.