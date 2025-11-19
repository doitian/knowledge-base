---
comment: true
date: '2017-04-04T19:45:09+08:00'
description: ''
katex: false
share: true
title: OmniGraffle 绘制图片作为中心的思维导图
tags:
- diagram
- productivity
---

# Mindmap With Image As Center Topic

一图胜千言，通过截图加标注能够很直白的说明问题。不过有时候会碰到标注很多很复杂的情况，比如针对截图对 UI 或者游戏系统进行分析，这个时候结合思维导图就比较方便了。

OmniGraffle 是个图表绘制和图表绘制工具。通过结构化编辑，和自动图表风格，也可以作为思维导图工具。而使用锚点编辑的连接功能 ，可以在图片的对应位置上使用引导线来引出各个主题。

<!--more-->

下面是个成品的示例 [原图下载](https://raw.githubusercontent.com/doitian/assets/master/2020/YBCYsJ/demo-image-center-mindmap.png):

![[demo-image-center-mindmap-thumb.png|示例思维导图]]

## 制作步骤

使用自动图表风格来制作思维导图。默认的风格里 Lines 比较适合。使用自动图表风格会给子分支分配漂亮的颜色。

![[choose-diagram-style.png]]
![[choose-diagram-style-dialog.png|||Choose Diagram Style]]

Lines 默认把 Canvas 填充成黑色了，可以在 Canvas Inspector 里修改。

![[canvas-fill.png|Canvas 填充]]

使用 Outline 边栏，或者快捷键 <kbd>⌘}</kbd> 和 <kbd>⌥⌘'</kbd> 来快速创建思维导图。

![[outline.png|思维导图]]

最后就是插入图片，替换掉思维导图的中心点了。不过之前需要在 Canvas Inspector 里禁用掉图表风格的自动布局，之后再修改就需要手动调整布局了。

![[disable-auto-layout.png|禁用自动布局]]

插入图片， 用 Shape 画一个矩形覆盖在图片上。这个矩形要用来取代思维导图的中心点。不直接用图片是因为结点间的连线始终在结点下面，而我希望引导线显示在图片之上。为了能看到图片，需要把这个矩形的 Fill 和 Stroke 都设置成无。接着使用 Magnet Tool (m) 给矩形添加锚点。

![[image-anchors.png|图片锚点]]

把连接在原来中心点的连线一端连接到添加好锚点的矩形上。全部完成后就可以删除中心结点了。 最后再调整下 Layer 顺序和结点的位置就都到最后的结果的。

![[demo-salad.png|成品]]
