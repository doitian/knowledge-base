---
comment: true
date: 2017-10-14 03:43:07
description: 如何在其它服务中使用 Graylog 搜集的日志
katex: false
series:
- Centralized Logs Using Graylog
share: true
title: Graylog 集中日志管理 - 日志输出
tags:
  - devops
  - graylog
---

# Graylog 集中日志管理 - 日志输出

这是 Graylog 系列最后一篇。

日志集中保存到 Graylog 后就可以方便的使用搜索了。不过有时候还是需要对数据进行近一步的处理。主要有两个途径：

- 直接访问 Elastic 中保存的数据
- 通过 Graylog 的 Output 转发到其它服务

<!--more-->

## 访问 Elastic
Graylog 支持一些简单的统计，如果想做更复杂的统计，推荐使用 [Grafana](https://grafana.com)。

集成很简单，在 Grafana 添加下 Elasticsearch 数据源。Access 推荐 proxy，这样不用在公网暴露 Elastic 的端口，只要 Grafana 所在机器能通过 Url 访问就可以了。

Index name 根据 Graylog Index Set 中设置的前缀配置。Version 根据安装的 Elastic 版本选择。

![[graylog-grafana-data-source.png|Grayfana Data Source]]

然后创建图标选择 Elastic 的 Data Source 就可以了。

如果还有更复杂的需求，可以使用 Elastic 的各种语言的库，比如 Jupter Notebook 搭配 Python。

## Graylog Output

在 Graylog 中，可以选择将某个 Stream 通过 Output 转发给其他服务。内置了 GELF Output 使用 GELF 格式通过 TCP 或者 UDP 发到其它服务。在 Graylog Market 中可以搜索到很多现成的 [Output Plugin](https://marketplace.graylog.org/addons?kind=plugin&tag=output)，Github 上也有很多[现成](https://github.com/graylog-labs/graylog-plugin-slack/blob/master/src/main/java/org/graylog2/plugins/slack/output/SlackMessageOutput.java)的[例子](https://github.com/Graylog2/graylog-plugin-splunk/blob/master/src/main/java/com/graylog/splunk/output/SplunkOutput.java)可以仿照实现自己的 Output Plugin。不过 Plugin 需要用 Java 实现，然后要部署到 Graylog 的所有节点，修改调试都很不方便。如果 Market 中找不到现成的 Plugin，更推荐使用内置的 GELF Output，很多 GELF 库是支持作为服务接收 GELF 消息的，比如 Golang 的 [go-gelf](https://github.com/Graylog2/go-gelf)，使用 `gelf.NewReader` 就可以创建一个 UDP 服务。

``` go
package main

import (
	"log"

	"gopkg.in/Graylog2/go-gelf.v2/gelf"
)

func handleMessage(m *gelf.Message) {
	// handle m
}

func runUDPServer() {
	gelfReader, err := gelf.NewReader(":12201")
	if err != nil {
		log.Fatal(err)
	}
	for {
		message, err := gelfReader.ReadMessage()
		if err != nil {
			log.Error(err)
		}
		go func() {
			defer func() {
				if r := recover(); r != nil {
					log.Error(r)
				}
			}()
			handleMessage(message)
		}()
	}
}

func main() {
	runUDPServer()
}
```
