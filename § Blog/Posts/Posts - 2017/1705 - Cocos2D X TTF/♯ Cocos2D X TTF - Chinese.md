---
date: '2017-05-13T17:43:59+08:00'
description: 介绍 Cocos2D-X 中用到的 FreeType 如何排版
title: Cocos2D-X TTF 字体排版
---

# Cocos2D X TTF 字体排版

#cocos2dx #typography

最近在公司的一个 Cocos2D-X 项目中碰到一个问题，TTF 文本加描边后会变宽，而且很明显没有对齐，字和描边之间没齐，每个字的水平基准线也没有对齐。最后发现是排版的代码有问题，官方分支上已经修复，但是这个项目使用的是 quick 分支出来的社区版，所以手动把修改做了个补丁提交了个[修复TTF 描边效果的 PR](https://github.com/u0u0/Quick-Cocos2dx-Community/pull/76)。

在 Cocos2D-X 是 TTF 的排版是使用的开源库 [FreeType 2](https://www.freetype.org/freetype2/docs/documentation.html)，核心的实现基本都在 `cocos/2d/CCFontFreeType.cpp` 中的 `FontFreeType::getGlyphBitmap`。原理是通过 FreeType 为每个字生成位图，然后通过 FreeType 返回的排版信息放到合适的位置，而问题就出现加了描边之后，位置计算的不正确。

为了弄清楚原因，又去看了下相关的文档，了解了下 Cocos2D-X 具体是如何排版 TTF 的。

<!--more-->

## Glyph Convention

FreeType 本身不光提供的 API 文档，而且还有很丰富的文档说明字体排版中的[各种概念](https://www.freetype.org/freetype2/docs/glyphs/index.html)。在排版中最小的单位是一个 Glyph，对应文本中的一个字符。Glyph 会有一个原点 (Original)，又被称为 pen cursor。在横向排版中，pen cursor 会在水平基准线上从左到右排列。

Glyph 中可见像素的最小包围框被称作 Bouncing Box (略作 bbox)。Bouncing Box 左上角相对原点会有一个偏移，即 `(horiBearingX, horiBearingY)`。这样导出位图的时候就不用包含空白了。而 `horiAdvance` 则是下一个字符的原点相对该字符的偏移。

![[freetype-glyph.png|FreeType Glyph [图片参考来源](https://www.freetype.org/freetype2/docs/glyphs/glyphs-3.html)]]


要显示一行文本只需要先确定第一个字符原点的位置，相对这个位置找到 bbox 左上角的点，然后把 Glyph 位图填充在这个位置。再根据 `horiAdvance` 确定下一个字符的原点，重复直到处理完所有字符。

![[freetype-glyphs-line.png|Glyphs Line]]

## Stroker

要添加描边的话，实际是每个字符用 FreeType 导出了两次位图，一次是字符本体，一次是描边。描边本身的位图是会比本体大的，如下如示。

![[freetype-glyph-outline.png|Glyphs 加描边]]

之前的代码比较粗暴地把本体和描边中心对齐，然后也没改位图左上角相对原点的偏移。因为不同的字符描边在各个方向多出的尺寸并不是一致的，放在一起就明显会不齐了。

![[freetype-glyph-invalid-position.png|Glyph 没对齐]]

## 测试代码

要测试的话，比较方便的是使用有 FreeType 库的脚本语言，比如 Python，下面的代码使用到了 freetype-py 来生成位图，然后使用 Pillow 生成图片。

※ [main.py](https://github.com/doitian/freetype-label-test/blob/master/main.py)

``` python
import freetype as ft
from PIL import Image


def main(stroke=0):
    """executable entry."""
    face = ft.Face('./WenQuanYiMicroHei.ttf')
    face.set_char_size(48*64)
    if stroke == 0:
        flags = ft.FT_LOAD_DEFAULT
    else:
        flags = ft.FT_LOAD_DEFAULT | ft.FT_LOAD_NO_BITMAP
    face.load_char('心', flags)
    slot = face.glyph
    glyph = slot.get_glyph()

    if stroke > 0:
        stroker = ft.Stroker()
        stroker.set(
            64,
            ft.FT_STROKER_LINECAP_ROUND,
            ft.FT_STROKER_LINEJOIN_ROUND,
            0
        )
        glyph.stroke(stroker, True)

    blyph = glyph.to_bitmap(ft.FT_RENDER_MODE_NORMAL, ft.Vector(0, 0), True)
    bitmap = blyph.bitmap
    width, rows, pitch = bitmap.width, bitmap.rows, bitmap.pitch

    print({
        'width': slot.metrics.width >> 6,
        'height': slot.metrics.height >> 6,
        'horiBearingX': slot.metrics.horiBearingX >> 6,
        'horiBearingY': slot.metrics.horiBearingY >> 6,
        'horiAdvance': slot.metrics.horiAdvance >> 6,
        'bitmapWidth': bitmap.width,
        'bitmapHeight': bitmap.rows
        })
    img = Image.new("L", (width, rows), "black")
    pixels = img.load()

    for y in range(img.size[1]):
        offset = y * pitch
        for x in range(img.size[0]):
            pixels[x, y] = 255 - bitmap.buffer[offset + x]

    img.show()


if __name__ == '__main__':
    main()
    main(2)
```

完整项目代码在 [GitHub - doitian/freetype-label-test](https://github.com/doitian/freetype-label-test)
