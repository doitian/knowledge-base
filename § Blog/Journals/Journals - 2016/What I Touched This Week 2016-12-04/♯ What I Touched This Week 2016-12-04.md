---
date: 2016-12-04
description: My weekly review report.
hljs: true
hljsLanguages:
- yaml
series:
- What I Touched

---

# What I Touched This Week 2016-12-04


This week I setup servers using [SaltStack][1] and continue automate building and deployment using Gitlab CI.

<!--more-->

## Saltstack
- Pillar cannot access data in another pillar file.
	* Reference pillar name instead, just like `contents_pillar` in `file.managed`.
* `mount.mounted` does not format the disk, use `blockdev.formatted` first.
* `salt-call —id custom_id` can overrides minion ID in command line, handful for test.

### Hour to test Saltstack states

- Create a docker image, install `salt-minion`  and  [bats][2] on it.
* Configure minion to use local file client
* Allow overriding pillar using an YAML file in test.
* Use `salt-call` to apply states.
* Use [bats][3] to verify.

A sample minion config:

```
file_client: local

file_roots:
  base:
    - /srv/states
    - /srv/test/states
    - /srv/formulas/users-formula

pillar_roots:
  base:
    - /srv/test/pillar
    - /srv/pillar
    
ext_pillar:
  - cmd_yaml: cat /srv/test/pillar.yml
```

Mount the project to `/srv` and run bats in docker.

## Misc
- In `.gitlab-ci.yml`, `environment:url` cannot contain invalid characters like `{` and `}`. Use `$CI_BUILD_REF_NAME` instead of `${CI_BUILD_REF_NAME}` in URL .
- Gitlab CI Runner on Mac sometimes stucks at fetching repository from gitlab because it asks to access login keychain and requires interactive password input.
- Python3 version of curl

        python3 -c 'import urllib.request; print(urllib.request.urlopen("http://example.com”).read().decode("utf-8"))'

    and POST
    
        python3 -c 'import urllib.request; urllib.request.urlopen("https://gitlab.com/api/v3/projects/ID/trigger/builds", "token=TOKEN&ref=REF".encode("utf-8"));'

- [How to avoid Go gotchas ·  divan’s blog][4]. Delve into details to avoid gotchas.
* [Python: 会打扮的装饰器 · FunHacks][5]
* Configure bundle gem mirror `bundle config mirror.https://rubygems.org https://gems.ruby-china.org` via  [gems.ruby-china.org][6]
* Use root to read file but authenticate using another user `/usr/local/bin/rsync -e "sudo -H -u user ssh" -av file server:`

[1]:	https://saltstack.com
[2]:	https://github.com/sstephenson/bats
[3]:	https://github.com/sstephenson/bats
[4]:	https://divan.github.io/posts/avoid_gotchas/
[5]:	https://funhacks.net/2016/11/22/decorator/?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io
[6]:	https://gems.ruby-china.org

