---
date: '2013-01-31'
title: A trick to use just jasmine gem to test Javascript in Rails
---

# Rails Javascript Test With Jasmine Gem

#rails #javascript #software-test

> [Jasmine][] is a behavior-driven development framework for testing JavaScript
> code. It does not depend on any other JavaScript frameworks. It does not
> require a DOM. And it has a clean, obvious syntax so that you can easily write
> tests.

It is very easy to integrate Jasmine into Rails, since the team provides the [jasmine gem][]. The jasmine gem also supports assets pipeline, just prepend `assets/` to file path. For example, `app/assets/javascripts/application.js.coffee` can be referred as `assets/application.js` in `jasmine.yml` `src_files`.

However, `spec_files` does not support assets pipeline, so the files in `spec/javascripts` cannot be written in CoffeeScript. But if `spec/javascripts` is appended to assets pipeline paths, the spec files can be added to `src_files` in jasmine.yml.

This post explains how to apply such trick, and how to integrate jasmine gem with [guard-jasmine][] and [travis][].

I also created a demo repository, see its [commits][] for integration steps.

<!--more-->

## Jasmine Integration

Jasmine 1.3.1 [removes](https://github.com/pivotal/jasmine-gem/issues/120) the ability to load `jasmine_config.rb` before executing specs. Although it is possible to load the file by [adding a rake dependency][jasmine-1-3-1-load-jasmine-config], but the trick does not work for `rake jasmine:ci`. So please use Jasmine 1.3.0 until a new version is released.

-   First add jasmine in Gemfile

    ``` ruby
    group :development, :test do
      gem "jasmine", "1.3.0"
    end
    ```

    and run `bundle install`.

-   Then generate config files:

    ```
    rails g jasmine:install
    ```

-   Append `spec/javascripts` to assets paths by creating file
    `spec/javascripts/support/jasmine_config.rb` and add following line to the
    file:

    ``` ruby
    Rails.application.assets.append_path File.expand_path('../..', __FILE__)
    ```

-   Edit `spec/javascripts/support/jasmine.yml`. Append `assets/specs.js` to
    `src_files`. Also set `spec_files` and `helpers` to `[]`, otherwise the
    JavaScript files may be included twice.

    ``` yaml
    src_files:
      - assets/application.js
      - assets/specs.js

    stylesheets:
      - stylesheets/**/*.css

    helpers: []
    spec_files: []
    src_dir:
    spec_dir:
    ```

-   Create the file `spec/javascripts/specs.js`. Usually, it just needs include
    all the js files in directory `spec/javascripts`.

    ``` javascript
    // Ensure helpers are loaded first. Remove the following line if
    // helpers directory is not created yet.
    //= require_tree ./helpers
    //= require_tree ./
    ```

-   Create a spec file to test the integration, e.g.,
    `spec/javascripts/foobar_spec.js.coffee`

    ``` coffeescript
    # spec/javascripts/foobar_spec.js.coffee
    describe "foobar", ->
      it 'works', -> expect(1 + 1).toEqual(2);
    ```

-   Start jasmine server by `rake jasmine` and visit the test page
    <span>http://localhost:8888</span>.

## Guard

The defult config of [guard-jasmine][] is intended to be used with [jasminerice][]. But it also allows starting jasmine gem server as well.

-    Add guard and guard-jasmine in Gemfile.

     ``` ruby
     group :development do
       gem 'guard'
       gem 'guard-jasmine'
     end
     ```

-   `bundle install`

-   Add following jasmine guard config in Guardfile

    ``` ruby
    require 'guard/jasmine'
    port = ::Guard::Jasmine.find_free_server_port
    guard :jasmine, :server => :jasmine_gem, :port => port, :jasmine_url => "http://localhost:#{port}/" do
      watch(%r{spec/javascripts/support/.+\.(?:rb|yml)$}) { 'spec/javascripts' }
      watch(%r{spec/javascripts/helpers/.+\.rb$}) { 'spec/javascripts' }
      watch(%r{spec/javascripts/spec\.(?:js\.coffee|js|coffee)$}) { 'spec/javascripts' }
      watch(%r{spec/javascripts/.+_spec\.(?:js\.coffee|js|coffee)$})
      watch(%r{app/assets/javascripts/(.+?)\.(js\.coffee|js|coffee)(?:\.\w+)*$}) { |m| "spec/javascripts/#{ m[1] }_spec.#{ m[2] }" }
    end
    ```

Now `guard-jasmine` will start the server provided by `jasmine-gem` and visit the test page using [phantomjs][].

## CI

The jasmine gem has another task `rake jasmine:ci` for continuous integration environments. To run the test on server without GUI, `xvfb` can be used.

See the following `.travis.yml`, in `before_install`, `xvfb` is started and `DISPLAY` is set so GUI applications know where to render their window.

``` yaml
language: ruby
script: bundle exec rake jasmine:ci
before_install:
  - "/sbin/start-stop-daemon --start --quiet --pidfile /tmp/custom_xvfb_99.pid --make-pidfile --background --exec /usr/bin/Xvfb -- :99 -ac -screen 0 1280x1024x16"
  - "export DISPLAY=:99.0"
  - "export JASMINE_BROWSER=firefox"
```

## References

- [jasmine gem][]
- [#261 Testing JavaScript with Jasmine - RailsCasts][RailsCasts #261]
- [#261 Testing JavaScript with Jasmine (revised) - RailsCasts][RailsCasts #261 revised]
- [Travis CI: GUI & Headless browser testing on travis-ci.org][gui-and-headless-browsers]

[jasmine]: http://pivotal.github.com/jasmine/
[jasmine gem]: https://github.com/pivotal/jasmine-gem "jasmine-gem"
[jasminerice]: https://github.com/bradphelan/jasminerice "bradphelan/jasminerice"
[guard-jasmine]: https://github.com/netzpirat/guard-jasmine "netzpirat/guard-jasmine"
[travis]: https://travis-ci.org/ "Travis CI"
[railscasts #261]: http://railscasts.com/episodes/261-testing-javascript-with-jasmine "#261 Testing JavaScript with Jasmine - RailsCasts"
[railscasts #261 revised]: http://railscasts.com/episodes/261-testing-javascript-with-jasmine-revised "#261 Testing JavaScript with Jasmine (revised) - RailsCasts"
[jasmine-gem issue #120]: https://github.com/pivotal/jasmine-gem/issues/120 "jasmine_config.rb is not read in Jasmine 1.3.1"
[jasmine-1-3-1-load-jasmine-config]: http://log.iany.me/post/41885818751/ "Load jasmine_config.rb in jasmine 1.3.1"
[phantomjs]: http://phantomjs.org/ "PhantomJS: Headless WebKit with JavaScript API"
[gui-and-headless-browsers]: http://about.travis-ci.org/docs/user/gui-and-headless-browsers/ "Travis CI: GUI & Headless browser testing on travis-ci.org"
[commits]: https://github.com/doitian/rails-jasmine-demo/commits/master
