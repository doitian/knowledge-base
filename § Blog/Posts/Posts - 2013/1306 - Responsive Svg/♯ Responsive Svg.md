---
date: '2013-06-16'
description: Introduction to make SVG responsive.
title: Responsive SVG
---

# Responsive Svg

#svg

SVG can use percentage as unit, but it is often more convenient to use px as unit. Framework such as d3 also uses px internally. However, it is still easy to scale an SVG using attributes `viewBox` and `preserveAspectRatio` even px is used as unit internally.

<!--more-->

## viewBox and preserveAspectRatio

The attribute [viewBox][] specifies viewpoint dimension. SVG can be scaled along with the parent container without changing the internal coordinates.

For example, the SVG below defines a viewpoint with width 100 and
height 100.

```
<svg viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="50" fill="blue">
</svg>
```

The figure below shows the same SVG in different container sizes: 50x50, 100x50, 100x100, 100x200, 200x200 from left to right.

![[same-svg-in-different-containers.png|Same SVG in Different Size Containers]]

Attribute [preserveAspectRatio][] controls how SVG is scaled according to parent container. There are many combinations, but the most frequently used are default (when the attribute is not specified, or set to `xMidYMid meet` explicitly) and **none**.

- default, preserve ratio, align center of SVG to the center of the container, scaled up as much as possible but ensure the entire `viewBox` is visible within the container.
- `none`, do not preserve ratio, scale SVG to fill the whole container.

See the figure similar to the previous one but setting `preserveAspectRatio` to `none`.

![[preserveaspectratio-none.png|`preserveAspectRatio="none"`]]

## Responsive SVG

First add following CSS:

``` css
svg {
  width: 100%;
  height: 100%;
}

svg * {
  vector-effect: non-scaling-stroke;
}
```

The first rule ensures SVG always fills parent container. And the second one sets a default `vector-effect` that when SVG is scaled, leave stroke width untouched.

If the SVG does not need to preserve ratio, set `preserveAspectRatio` to `none`, and set the height of the container. For example, the SVG below has a fixed height `50px`, and is half width of the whole page.

``` html
<div style="width:50%;height:50px;">
  <svg viewBox="0 0 100 100" preserveAspectRatio="none">
    <circle cx="50" cy="50" r="50" fill="blue">
  </svg>
</div>
```

<figure>
  <div style="width:50%;height:50px;">
    <svg viewBox="0 0 100 100" preserveAspectRatio="none">
      <circle cx="50" cy="50" r="50" fill="blue" />
    </svg>
  </div>
  <figcaption>Fixed With, Horizontal scalable</figcaption>
</figure>

If the SVG must preserve ratio, then we need a bit of JavaScript to change container height when window is resized.

```javascript
$.fn.preserveAspectRatio = function() {
  this.each(function() {
    var $this = $(this);
    var ratioSpec = $this.attr('data-preserveAspectRatio').split(':');
    var ratio = parseInt(ratioSpec[1], 10) / parseInt(ratioSpec[0], 10);
    $this.height($this.width() * ratio);
  });
};

var preserveAspectRatio = function() {
  $('[data-preserveAspectRatio]').preserveAspectRatio();
};

$(function() {
  preserveAspectRatio();
  $(window).on('resize', preserveAspectRatio);
  // Better to wrap preserveAspectRatio in underscore debounce or jquery-throttle-debounce.
  // $(window).on('resize', _.debounce(preserveAspectRatio, 200));
});
```

Then set `data-preserveAspectRatio` on any container that needs preserve aspect ratio. Following example sets the width height ratio to `1:1`:

``` html
<div style="width:50%;" data-preserveAspectRatio="1:1">
  <svg viewBox="0 0 100 100" preserveAspectRatio="none">
    <circle cx="50" cy="50" r="50" fill="blue">
  </svg>
</div>
```

See the demo in this [pen](https://codepen.io/doitian/pen/njmzrR).

## References

- [Making responsive SVG graphs][making-responsive-svg]
- [SVG Coordinate Systems, Transformations and Units](http://www.w3.org/TR/SVG/coords.html)

[viewBox]: http://www.w3.org/TR/SVG/coords.html#ViewBoxAttribute
[preserveAspectRatio]: http://www.w3.org/TR/SVG/coords.html#PreserveAspectRatioAttribute
[making-responsive-svg]: https://web.archive.org/web/20171114160758/http://meloncholy.com/blog/making-responsive-svg-graphs/
