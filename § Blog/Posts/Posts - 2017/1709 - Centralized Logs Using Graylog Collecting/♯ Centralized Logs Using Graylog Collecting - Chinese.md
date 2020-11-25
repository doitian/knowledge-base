---
comment: true
date: 2017-09-24 15:08:08
description: 如何收集日志发往 Graylog
katex: false
series:
- Centralized Logs Using Graylog
share: true
title: Graylog 集中日志管理 - 收集日志
---

# Graylog 集中日志管理 - 收集日志

#graylog #devops

{{TOC}}

Graylog 通过 *Inputs* 收集日志，方式以被动接收为主，需要在产生日志的地方将日志发送给 Graylog。比较常用的一些方式：

- 程序中直接集成可以发送日志给 Graylog 的库，在 Github 中搜索 GELF 可以找到大量各种语言、框架、环境下的库。
- 采用传统的文件来记录日志，在机器上启动一个 agent 程序抓取日志文件新的内容然后发给 Graylog。
- 使用 syslog 写日志，利用 rsyslog 的转发功能把日志发给 Graylog。

服务器端日志个人推荐最后一种方式，优点有

- 不依赖 Graylog，可以替换成任何能接收 syslog 的其它方案。
- 容易 Fallback，rsyslog 可以配置成同时保存到本地文件和转发 Graylog。当 Graylog 出现问题至少还有本地日志文件可以用。
- rsyslog 的日志保存，转发已经非常成熟和稳定。

缺点是 rsyslog 日志会把整条日志作为 `message` 字段保存。Graylog 内部每条日志是作为 Elastic 的 Document 保存的，细化出更多的字段能满足复杂查询和数据分析的需求。所以 Graylog 基于 JSON 制定了 [GELF](http://docs.graylog.org/en/2.3/pages/gelf.html) 协议，使用 GELF 协议的 Input 可以在产生日志时直接设置各种字段。不过 Graylog 还提供了 *Extractor*，和 [fluentd](https://www.fluentd.org), [logstash](https://www.elastic.co/products/logstash) 中的 filter 相似，可以从日志中提取结构化字段出来，比如 JSON Extractor 可以解析 JSON 格式日志。使用过类似工具的应该对 Grok 很熟悉，Graylog 也提供了支持。所以使用 rsyslog 也只需要制定下日志格式，然后配置下 Extractor。

Graylog [自带了](http://docs.graylog.org/en/2.3/pages/sending_data.html)丰富的 Inputs 可供使用，同时可以通过[插件扩展](https://marketplace.graylog.org/addons?kind=plugin&tag=input)，可以结合自己的使用场景选择合适的方式。

本文接下来会介绍日志收集需要注意的地方，以及如何基于 rsyslog 来打造集中日志系统。

<!--more-->

## 日志处理队列

Graylog 内部使用 [Kafka](https://kafka.apache.org)  实现了称为 Journal 的队列系统，来缓存接收的日志。这个对集中日志系统相当重要。日志的特性决定了量大，并且分布不平均，会突发地集中在某个时间段产生大量日志。队列能有效的防止突发大数据量输入导致系统瘫痪，将闲时利用起来处理积压的日志。同时还能作为是否要扩充集群提高 Elastic 写入速度的指标。

Graylog 集群每个节点有自己独立的 Journal，扩展 Graylog 本身节点数量不但可以提升日志处理速度，还可以提升队列缓存的容量。

当 Elastic 写入出现瓶颈，Journal 的队列长度会一直增长，Graylog 设置了俩个阀值，当积压的日志超过 12 小时未处理，或者占用磁盘超过 5G 就会开始丢弃新接收到的日志。通过配置 `message_journal_max_age` 和 `message_journal_max_size` 可以修改。Graylog 还提供了 [API 查询状态](http://docs.graylog.org/en/2.3/pages/configuration/load_balancers.html) 可以和负载均衡系统集成。

## Graylog 创建 syslog input

首先要在 Graylog 中通过 `System / Inputs` 创建 input 来接收日志。可以选 Syslog UDP 或者 Syslog TCP，俩者区别不大，TCP 的话 rsyslog 是[能保证日志不会丢失](http://www.rsyslog.com/doc/v8-stable/tutorials/reliable_forwarding.html)，UDP 的话开销相对更小，但是可能丢数据。TCP 的话负载均衡选择也更多，如果不知道用哪个就选 TCP。

/graylog-syslog-tcp-input.png "Create Graylog Syslog TCP Input"

大部分不需要改，`Global` 的话会在所有 Graylog 节点上启动，Bind address 使用默认的 `0.0.0.0` 这样其它机器才能转发日志过来。Port 需要配置一个大于 1024 的端口。

如果启用了集群，还需要使用负载均衡将 rsyslog 转发的日志分发给 Graylog 节点。如果用 TCP，可以用  HAProxy，很多云服务也提供了现成甚至免费的内网 TCP 负载均衡产品。如果用 UDP，可以参考我之前写的 [使用 Nginx 作 UDP 负载均衡](ia-writer://open?path=/Locations/_Publish/§%20Blog/Posts/Posts%20-%202017/1708%20-%20Nginx%20Udp%20Load%20Balance/♯%20Nginx%20Udp%20Load%20Balance%20-%20Chinese.md)。

## 日志发往 rsyslog

Syslog 是一套记录日志的协议，rsyslog 是具体的一个实现。在 Debian 和 Ubuntu 中预装的就是 rsyslog。Rsyslog 用很多扩展功能，不如不限制单条日志大小，可以转发日志。

日志不是直接发往 Graylog  的 syslog input，而是发往本地的 rsyslog，然后 rsyslog 负责转发给 Graylog。这样网络或者 Graylog 出现问题，Rsyslog 可以缓存未发送的日志，等待问题恢复。同时还可以在本地保存一份副本。

将日志发往 syslog 可以使用系统提供的 C 库中的 syslog (see [man 3 syslog](https://linux.die.net/man/3/syslog))。很多语言标准库都集成了 syslog，比如 [Ruby](https://ruby-doc.org/stdlib/libdoc/syslog/rdoc/Syslog/Logger.html)，[Python](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SysLogHandler), [Go](https://golang.org/pkg/log/syslog/)。没有的也可以通过 C 集成，比如用于 [skynet](https://gist.github.com/6de6d7ce01a7930dfba1b6aa5e76ac3f)

注意几个比较重要的可配置参数，能方便之后日志的过滤和转发。可以在 `man 3 syslog` 看到

```
void openlog(const char *ident, int logopt, int facility);
```

其中 `indent` 在不同的地方可能又被称为 `programname`, `tag`。一般用这个来区分日志是哪个服务或者进程产生的。另一个是 `facility`，推荐统一使用 `LOCAL6`，在 rsyslog 只转发 `LOCAL6` 的日志到 Graylog。

Facility 的配置都比较直接，不过 indent 的配置就比较混乱了，像 Python 的 `SysLogHandler` 就一直不支持自定义 ident，Python 3 直到 [3.3 版本中才可以通过 class-level attribute 来配置](https://bugs.python.org/issue12419)。所以分别说明下

- Ruby: `Syslog::Logger.new(program_name = 'ruby', facility = nil)` 中 `program_name` 就是 ident
- Python: Python 不管哪个版本 `SysLogHandler` 默认都不传 ident 的，而 ident 在 syslog 标准中其实就是日志中以非特殊字符开头，`: ` 结尾的一串字符，所以可以在设置 formatter 的时候添加，见下面的代码。

```python
import logging
from logging.handlers import SysLogHandler

ident = 'myprogname'
h = SysLogHandler(address='/dev/log')
h.setFormatter(logging.Formatter(ident + ': %(message)s'))
logging.getLogger().addHandler(h)

logging.error('hi')
```

- Go: log/syslog 的 `Dial(network, raddr string, priority Priority, tag string) (*Writer, error)` 中的 tag 就是 ident。

## Rsyslog 配置

以 Ubuntu 14.04 为例。先上配置，保存为 `/etc/rsyslog.d/00-graylog.conf`，具体文件名不重要，但必须 `00` 开头，`.conf` 为后缀。

```
$template GLFile,"/data/log/%programname%.log"
$FileOwner syslog
$FileGroup syslog
$CreateDirs on
$DirCreateMode 0755
$FileCreateMode 0640
$RepeatedMsgReduction off
local6.* ?GLFile;RSYSLOG_SyslogProtocol23Format
local6.* @@logs-internal.example.com:1514;RSYSLOG_SyslogProtocol23Format
& stop
```

`$` 开头的都是 rsyslog 的配置的 Directive。如果对日志可靠性要求高，可以参考[Rsyslog Reliable Forwarding](http://www.rsyslog.com/doc/v8-stable/tutorials/reliable_forwarding.html) 的文档。

配置中 `$RepeatedMsgReduction` 是不删除重复的日志，其它全部都是配置本地文件副本的。`$template GLFile` 配置了文件名命名模版。模版可以使用一些变量，比如 `%programname%` 是日志的 ident，如果之前正确设置了 ident，这里可以把不同的服务的日志存到不同的文件中。模版是完整的路径，注意权限，用户 syslog 需要有创建文件的权限。因为 rsyslog 没有 root 权限，`FileOwner` 和 `$FileGroup` 可选值不多，如果想让其它用户查看文件，可以把 `$FileGroup` 设置成 `syslog`，然后添加用户到 `syslog` 组。例子:

```
sudo mkdir -p /data/log
sudo chown syslog:adm /data/log
# 允许 deploy 查看本地日志副本
sudo gpasswd -a deploy syslog
```

倒数第三行  `local6.* ?GLFile;RSYSLOG_SyslogProtocol23Format` 是把 facility 是 `LOCAL6` 的日志按照模版 `GLFile` 保存到文件中。如果不想要本地副本，删掉本行即可。

倒数第二行俩个 `@` 的 `@@logs-internal.example.com:1514;RSYSLOG_SyslogProtocol23Format` 表示通过 TCP 转发日志到 `logs-internal.example.com` 的1514端口。如果是 UDP 改成一个 `@`。如果用了负载均衡这里应该填负载均衡的地址和端口。

最后一行的 `& stop` 表示匹配之前规则的日志，也就是所有 `LOCAL6` 的日志不再判断配置中剩余的规则。这也是配置必须用 `00` 开头的原因。默认的 Ubuntu 配置中，`LOCAL6` 的日志也会保存到 `/var/log/syslog` 中，重复浪费空间，而且日志量很大的话，`/var/log/syslog` 默认的 logrotate 的配置会导致占用大量的磁盘。

配置里选择把日志保存在 `/data/log`  目录下，主要是为了单独配置 `logrotate`。访问量大的服务会产生海量日志，所以需要优化避免写爆磁盘。

这是一个每天不压缩大概会产生 100G 左右日志的推荐配置，保存为 `/etc/logrotate.d/syslog-graylog`

```
/data/log/*.log
{
        rotate 40
        daily
        maxage 5
        maxsize 10G
        missingok
        notifempty
        compress
        postrotate
                reload rsyslog >/dev/null 2>&1 || true
        endscript
}
```

- `daily` 每天 rotate 一次，`maxsize 10G`  超过 10G 立即 rotate。
- `rotate 40` 和 `maxage 5` 保留最多 40 份，最多 5 天内的历史日志。过期的删除。
- `compress` 用 gzip 压缩历史日志，不配置 `delaycompress`

这样大概保存最近 5 天的日志，如果日志量太大，就保存最近 40 x 10 共 400G 日志。天数根据需要配置，因为是副本，不用设置太长时间。`rotate 40` 和 `maxsize 10G` 根据磁盘大小确定，GZIP 压缩比大概是 1/10，40 x 10 的配置大概占用 40G 磁盘。

Logrotate 默认是每天运行的，`maxsize 10G` 其实不起作用，可以配置 cron 每小时手动执行下，这样能及时 rotate 日志并压缩。把下面文件保存为 `/etc/cron.hourly/syslog-graylog`

```
#!/bin/sh

logrotate /etc/logrotate.d/syslog-graylog
```

注意权限

```
chmod +x /etc/cron.hourly/syslog-graylog
```


## 测试

测试可以使用命令行工具 `logger` ，`-p` 指定 facility 和 priority，`-t` 指定 ident

```
logger -p local6.error -t programname test
```

一切正常的话 Graylog 中就会显示这条日志了。

另外说下 macOS，虽说提供了 syslog 接口，不过坑很多，配置可以在 `/etc/syslog.conf` 里添加，比如

```
local6.* @127.0.0.1:1514
```

然后重启下服务

```
sudo launchctl unload /System/Library/LaunchDaemons/com.apple.syslogd.plist
sudo launchctl load /System/Library/LaunchDaemons/com.apple.syslogd.plist
```

不过 macOS 的 syslog 还受 `/etc/asl.conf` 影响，比如 `notice` 级别以下的日志是全部忽略，根本就不会处理到 `/etc/syslog.conf` 的。优点是可以在 Console 里查看 syslog。
