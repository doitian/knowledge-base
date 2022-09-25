---
date: '2020-05-03T22:50:53+0800'
---

# Pass, A Password Manager Utilizing GPG and Git

#app

A friend recommended [gopass](https://github.com/gopasspw/gopass) to manage passwords. After the trial, I decided to switch.

<!--more-->

Gopass is indeed an implementation which follows the protocols defined by [pass](https://www.passwordstore.org/). It utilizes gpg to encrypt files and git to synchronize. It is really fast to manage the password vault because I already used to the command line environment and text editing tools.

I also use [browserpass](https://github.com/browserpass/browserpass-extension) in Chrome and "Pass - Password Manager" in iOS.

I migrated from Enpass. There is a tool [pass-import](https://github.com/roddhjav/pass-import), but it does not work well on my exported Enpass vault, so I decide to build the pass store from scratch. Gopass indeed can encrypt and save any file, thus I just add the whole exported Enpass CSV file into the repository.

```
gopass edit enpass.csv
```

Copy and paste the exported Enpass CSV file into the opened editor and save. It is easy to search in the file using a pager or grep.

```
gopass show enpass.csv | less
gopass show enpass.csv | grep google
```

Now I can rebuild the password database with a create-on-use strategy: Whenever I want to use a password which has no its own entry yet, I search it in `enpass.csv` and create one.