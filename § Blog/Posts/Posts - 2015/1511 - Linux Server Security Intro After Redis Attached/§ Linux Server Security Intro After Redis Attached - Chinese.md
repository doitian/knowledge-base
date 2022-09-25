---
date: 2015-11-11
title: 从 Redis 攻击例子谈谈基本的 Linux 服务器安全
---

# Linux Server Security Intro After Redis Attached

#security

最近看到一篇文章详细说明了[如何通过 Redis 获得 SSH 登录权限](http://www.antirez.com/news/96)。简单来说就是如果 Redis 开放了外网端口访问，又没配置防火墙，也没有配置任何 Redis 的连接验证，而且还是用很高权限的用户在运行 Redis，就可以通过 dump 数据库把任意 key 注入到 `authorized_keys` 文件中，从而获得用户的 SSH 登录权限。条件很苛刻，但是很容易自动化，估计还是可以扫描到不少肉鸡的。

比较惭愧，最近部署的一台服务器就被该方法攻击了。主要原因是之前我已经书面说明了防火墙如何配置，所以想当然的认为拿到的机器已经配置好了。为了让 Redis 在内网内能访问，配置脚本中将监听的地址改成了 0.0.0.0，也没有配置连接验证，结果就是任何人都能连接上这个数据库。不过因为还是用的单独的 redis 用户运行，权限有限，攻击者并没有拿到 SSH 登录权限，只是把数据库清空了。所幸是测试服务器，数据库中的数据并不重要。

下面说明下我所了解的保护服务器安全的一些常识。

<!--more-->

## 禁止密码登录
只使用密码是不安全的。尤其是高权限用户，比如 root，无时无刻都有人在尝试暴力破解密码。不要以为改个 SSH 端口号就安全了，通过端口扫描很容易就能发现 SSH 端口。这个可以在 `sshd_config` 里禁止所有用户使用密码登录

```
PasswordAuthentication no
```

配置完重启 SSH 之前记得先确认可以通过钥匙对登录，不然就要悲剧了。

## 保护好私钥
添加 passphrase。因为有 ssh agent，基本上只需要登录后输入一次就行了。这样做主要是保证设备遗失后有充足的时间从服务器上的 `authorized_keys` 里删除对应的公钥。

在每台设备上单独生成不同的钥匙对，这样一台机器遗失只需要作废对应的公钥。尤其不要多个用户共享一个私钥。

重要的账号最好单独生成一对钥匙对，比如某机房中所有机器的最高权限管理账号。

## 保护好公钥
这个是指保护好 `authorized_keys` 文件。OpenSSH 默认就有强制的要求，在 `.ssh` 目录或者 `authorized_keys` 权限不正确的情况下都会忽略文件中的公钥。如果想更好的保护，可以使用 [chatter](https://wiki.archlinux.org/index.php/Access_Control_Lists) 把 `.ssh` 和 `authorized_keys` 都标记成只读，在共享某个账号时防止被任意修改。标记 `.ssh` 是为了防止删除整个目录重新创建。注意先创建 `known_hosts`，不然 `.ssh` 标记成只读后就没办法添加新文件了。

```
touch ~/.ssh/known_hosts
sudo chattr +i ~/.ssh ~/.ssh/authorized_keys
```

在需要修改的时候，先用 `chattr -i` 取消掉只读。

## 不要直接使用 root 用户
配置一个有 sudo 权限的用户来管理服务器。哪怕是不需要密码就可以 sudo 也比直接用 root 安全得多，因为你可以选择哪些命令 sudo 哪些不 sudo，而 root 所有的命令都是最高权限，需要时刻提心吊胆。

同时也可以在 `sshd_config` 是禁止 root 登录

```
PermitRootLogin yes
```

## 使用专门的用户来运行后台程序
并且只给该用户必要的权限来进行隔离，减少该程序被攻击时对机器上其它程序的影响。比如在这次 Redis 攻击中，如果是使用 root 权限运行的，就可以通过 dir 和 dbfilename 两个配置覆盖任何文件，而如果使用专门的 redis 用户，就只能是在 redis 用户有写权限的地方了。大部分包管理器安装的后台程序都会使用专门的用户来运行。要注意的是在自己编译安装服务时，一定不能嫌麻烦。

## 配置防火墙
只允许必要的端口被外网访问。在 Ubuntu 上，[ufw](https://wiki.ubuntu.com/UncomplicatedFirewall) 使用起来已经相当方便了，这次被攻击后也是使用 `ufw` 添加了防火墙。

```
sudo ufw allow ssh/tcp
sudo ufw allow http/tcp
sudo utw enable
```
