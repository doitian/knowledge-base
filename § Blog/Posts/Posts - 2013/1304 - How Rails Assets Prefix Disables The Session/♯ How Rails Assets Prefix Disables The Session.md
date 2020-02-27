---
date: '2013-04-28'
description: Introduce how we fix a bug, and what we learned about sprockets internals.
title: How Rails Assets Prefix Disables the Session
---

# How Rails Assets Prefix Disables The Session

#rails

This is original posted on
[intridea blog](http://www.intridea.com/blog/2013/3/20/rails-assets-prefix-may-disable-your-session).

I recently worked in a Rails project with [Peter (@sporkd)][Peter]. The
project is intended to be used as a sub-site, and should be served under
sub-URI. After google, we ended up by setting `config.assets.prefix` and
wrapped all routes in `scope`. The solution is simple and worked well. But
soon, some weird bugs were found, and Peter was successfully isolated the
problem to session (see demo
[sporkd/asset_prefix_test](https://github.com/sporkd/asset_prefix_test))

After several hours debugging, I finally found out the cause. To make a long
story short, the routes configured in `routes.rb` should not start with
`config.assets.prefix`, otherwise session save is skipped. The demo
`sporkd/asset_prefix_test` can be fixed by simply setting
`config.assets.prefix` to `/one/assets`. You also get a bonus by setting a
unique prefix for assets, since it is easy to add expiration header for assets
in web server.

<!--more-->

X-Cascade Header in Rails
-------------------------

I never knew `X-Cascade` header in Rails before. @soulcutter has a
[post][x-cascade-header-in-rails] that described its usage.

> The basic idea is this: if you return a response from a controller with the
> X-Cascade header set to "pass", it indicates that your controller thinks
> something else should handle the request. So rails (or is it rack? in any
> case...) will continue down your routes looking for the next rule that
> matches the request.

Indeed, `X-Cascade` is not only restricted in controller, if a mounted engine
sets this header, Rails also continues down the routes searching.

It is a feature of Rails. Since 3.2, Rails has moved the routes logic to
[journey][]. The `X-Cascade` trick can be found in
[journey/router.rb#L69](https://github.com/rails/journey/blob/master/lib/journey/router.rb#L69).

Pay attention that, the rack `env` object is shared when request is passed
on. So if `env` is changed by former route, the latter one is affected. This
is the root cause of the weird session issue, because session is controlled by
`env['rack.session.options']`.

Sprockets, who skips the session
--------------------------------

Sprockets, the gem for rails assets pipeline, mounts itself on
`config.assets.prefix` and [prepends](https://github.com/rails/rails/blob/3-2-stable/actionpack/lib/sprockets/bootstrap.rb#L27)
the route to Rails. So if user accesses a page which path starts with
`config.assets.prefix`, sprockets always processes the request first.

Maybe for performance, sprockets disables session save by changing
`env['rack.session.options']`:

    env['rack.session.options'] ||= {}
    env['rack.session.options'][:defer] = true
    env['rack.session.options'][:skip] = true

The options are changed even when asset is not found. If so, sprockets
returns 404 and sets the header `X-Cascade`. Then Rails passes the request to
controller, and correct page is rendered as expected. However, since the
session is already disabled by sprockets, the changed session in controller is
never saved.

Because `env` is a shared resource between routes when `X-Cascade` is set, it
should not be changed unless it has to. When asset is not found, sprockets
should just pass though without touching `env`, so I submit a
[PR](https://github.com/sstephenson/sprockets/pull/421) for it.

How we Debug
------------

Peter and I worked in different time zones. He first found the session issue
because several features related to session did not work. He made the demo
`sporkd/asset_prefix_test` to isolate the issue using minimum code at the end
of the day in his time zone and left me the message.

When my day started, I got the message and started debugging on session based on
the demo in
[doitian/asset_prefix_test](https://github.com/doitian/asset_prefix_test/compare/asset-prefix-one-deep).

Because session store class is customizable, I inherited one from default
cookie store and added breakpoints using [pry][]. Soon I found out that
`options[:skip]` was `true`, but I had no idea where it was set to
`true`. Then I did a grep (using [ag][]) in all gems, and fortunately, only
sprockets has set this option to `true`. The remaining work was just figuring
out why sprockets is invoked before controller action.

[x-cascade-header-in-rails]: http://teambandb.typepad.com/soultech/2011/10/x-cascade-header-in-rails.html
[journey]: https://github.com/rails/journey
[Peter]: https://twitter.com/sporkd
[pry]: https://github.com/pry/pry
[ag]: https://github.com/ggreer/the_silver_searcher
