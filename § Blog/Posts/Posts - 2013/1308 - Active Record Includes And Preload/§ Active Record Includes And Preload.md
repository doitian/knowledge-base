---
date: '2013-08-23'
description: Post about the differences of includes and preload
title: ActiveRecord includes and preload
---

# Active Record Includes And Preload

#rails

`ActiveRecord` has two [query methods][] to eager load associations, [includes][] and [preload][].  Although the documentation of `preload` says

> Allows preloading of args, in the same way that includes does.

Indeed the two methods have some differences.

In simple words, prefer `includes` to eager load associations. Use `preload` only when

- you want to customize `select` columns, or
- you meet error "Can not eagerly load the polymorphic association".

<!--more-->

Both of the two methods eager load associations to avoid N+1 queries. However, `includes` is more aggressive. If it detects that the associations tables are already joined, through explicitly `joins` or implicit references in `where`, it overwrites `select` fields from the joined query and construct result set from it, rather than loading associations in a separate query. See the generated SQL statement below and the fields aliases like `t0_r0`.

```
irb(main):049:0> User.includes(:articles).joins(:articles)
  SQL (0.7ms)  SELECT "users"."id" AS t0_r0,
    "users"."login" AS t0_r1,
    "users"."name" AS t0_r2,
    "users"."created_at" AS t0_r3,
    "users"."updated_at" AS t0_r4,
    "articles"."id" AS t1_r0,
    "articles"."title" AS t1_r1,
    "articles"."content" AS t1_r2,
    "articles"."user_id" AS t1_r3,
    "articles"."created_at" AS t1_r4,
    "articles"."updated_at" AS t1_r5
  FROM "users"
  INNER JOIN "articles"
  ON "articles"."user_id" = "users"."id"
```

However, if the table is not joined yet, `includes` will fallback to `preload`, which loads association in a separate query. See the SQL in log below that articles are eager loaded in another `SELECT` query.

```
irb(main):050:0> User.includes(:articles)
  User Load (0.1ms)  SELECT "users".* FROM "users"
  Article Load (0.2ms)  SELECT "articles".* FROM "articles"
    WHERE "articles"."user_id" IN (1, 2)
```

Because `includes` may (or may not) overwrite `select`, if you have your own `select` clause, use `preload` instead. See example below:

``` ruby
users = User.joins(:articles).select(
  'users.*, articles.created_at as last_posted_at'
)
users.includes(:articles).first.last_posted_at
# NoMethodError: undefined method `last_posted_at'
users.preload(:articles).first.last_posted_at
# => "2013-08-23 11:20:36.536968"
```

Older version of Rails has trouble to `includes` polymorphic associations. It seems the newer version of Rails is smart enough to fallback to `preload`. However if you still see the error "Can not eagerly load the polymorphic association", try switching to `preload`.

## References ##

- [ActiveRecord QueryMethods][query methods]
- [ActiveRecord Eater Loading Associations](http://guides.rubyonrails.org/active_record_querying.html#eager-loading-associations)

[query methods]: http://apidock.com/rails/ActiveRecord/QueryMethods
[includes]: http://apidock.com/rails/v3.2.13/ActiveRecord/QueryMethods/includes
[preload]: http://apidock.com/rails/v3.2.13/ActiveRecord/QueryMethods/preload
