---
date: '2013-07-16'
description: Gotcha of the three functions uniq, count and distince
title: ActiveRecord uniq, count and distinct
---

# Active Record Uniq Count And Distinct

#rails

`ActiveRecord` has two methods to remove duplicates. Method `uniq` and option `distinct: true` in method `count`. I thought `uniq.count` and `count(distinct: true)` were identical. Indeed, `uniq.count` still counts duplicates, and `count(distinct: true)` must be used here.

In simple words, use `uniq` to get unique result set, use `count(distinct: true)` to count unique result.

<!--more-->

For example, user has many activities, and I want to get all users having a specific type of activities:

``` ruby
users = User.joins(:activities).where(
  activities: { activity_type: 'purchase'}
)
```

Because a user may have multiple activities with the same type, the result above may contain duplicate users. Method `uniq` can be used here to remove the duplicates:

    users = users.uniq

But `users.uniq.count` generates SQL like below:

    SELECT DISTINCT COUNT(*) ...

This SQL counts all records with duplicates, and apply `DISTINCT` on the count, which has only one row. So `DISTINCT` has no effect here.

On the other hand, `users.count(distinct: true)` generates SQL below, which removes duplicates first, then count the result.

    SELECT COUNT(DISTINCT users.id) ...
