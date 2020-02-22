---
date: 2017-11-12
description: My weekly review report.
series:
- What I Touched

---

# What I Touched This Week 2017-11-12


- [A tour of Postgres Index Types](https://www.citusdata.com/blog/2017/10/17/tour-of-postgres-index-types/)

    > * *B-Tree* - For most datatypes and queries
    > * *GIN* - For JSONB/hstore/arrays which allow multiple values.
    > * *GiST* - For full text search and geospatial datatypes, for rows that overlap values
    > * *SP-GiST* - For larger datasets with natural but uneven clustering
    > * *BRIN* - For really large datasets that line up sequentially
    > * *Hash* - For equality operations, and generally B-Tree still what you want here

- [Why We Switched from Python to Go | The Stream Blog](https://getstream.io/blog/switched-python-go/)

    - [pkg/errors: Simple error handling primitives](https://github.com/pkg/errors)
    - ... [errcheck](https://github.com/kisielk/errcheck) and [megacheck](https://github.com/dominikh/go-tools/tree/master/cmd/megacheck) are handy to avoid making these mistakes.

<!--more-->

- [Solidarity — The CLI for Developer Sanity – Red Shift](https://shift.infinite.red/solidarity-the-cli-for-developer-sanity-672fa81b98e9)

    Snapshot environment requirements and verify later.

- [Stop using .IO Domain Names for Production Traffic – Hacker Noon](https://hackernoon.com/stop-using-io-domain-names-for-production-traffic-b6aa17eeac20)

    .IO DNS Server outage.

- [k88hudson/git-flight-rules: Flight rules for git](https://github.com/k88hudson/git-flight-rules)

    Git FAQ

## AI

- [Building AI That Can Build AI – The New York Times – Medium](https://medium.com/the-new-york-times/building-ai-that-can-build-ai-7a0546be97bf)
- How to calculate derivatives using [backpropation](https://www.youtube.com/watch?v=Ilg3gGewQ5U), and the [calculus explanation](https://www.youtube.com/watch?v=tIeHLnjs5U8)

## Productivity

- [How to Break Through Any Learning Plateau and Never Stop Growing](https://www.nateliason.com/learning-plateau/)

    > As soon as you see that you’re stuck, you should figure out how you can modify your practice to deal with the weakest part of your skillset..  

    - Take challenge, get out of comfort zone.
    - Mix up learned skills
    - Find week parts and improve

- [How to Improve Your Life in Just a Month – Thrive Global](https://journal.thriveglobal.com/how-to-improve-your-life-in-just-a-month-eed6c90ee6c4)

    > You can’t change what you not ready to quit.  

    > ... make small improvements every day that will gradually lead to the change you want.Each day.  

    > Take 20 minutes each night to make your mornings easier.  

    > Stop doing what average people do.  

    Also mentioned in [Five Unproductive Habits I’ve QUIT So I Can Get More Done](https://medium.com/personal-growth/five-unproductive-habits-ive-quit-so-i-can-get-more-done-830c6836e694)

    Actions:

    - Think what are worth to do.
    - Plan at the night instead of morning.
    - Contribute the most productive time slots to the most important things.

## Life

- [Rules for Happier Parents: Children Change — When We Let Them](https://betterhumans.coach.me/rules-for-happier-parents-children-change-when-we-let-them-cb93816b41ce)

    > Stick to describing your child’s behavior on any one occasion as nothing more than that.

## Projects

- [Poly](https://poly.google.com/)

    3D Model galery.

