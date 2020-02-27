---
date: 2017-04-16
description: My weekly review report.
series:
- What I Touched
---

# What I Touched This Week 2017-04-16


- [各种加密代理协议的简单对比 – Yachen Liu][1] 比较了常用的 HTTPS，SOCKS5-TLS 和 shadowsocks 等加密协议。
- [ChrisRx/dungeonfs: A FUSE filesystem and dungeon crawling adventure game engine][2]. Brilliant to map MUD game to filesystem.
- [TypeScript at Slack][3]. How Slack migrate to TypeScript and the migration guidance.
- [Fast Drawing for Everyone][4]. It can suggest nice clipart according to drawing.
- [Shields.io: Quality metadata badges for open source projects][5]. All in one place to find badges for the project.
- [Robert Haas: New Features Coming in PostgreSQL 10][6]. Many features for distributed PostgreSQL.
- Use JetBrains Rider as Unity3D C# IDE.
- [Wedding at Scale: How I Used Twilio, Python and Google to Automate My Wedding][7]
- [树莓派入门指南][8] 很详尽，很全面。
- [他热衷拍摄人与建筑的微妙关系，为了不同视角冒险爬上城市高空][9]。 热衷于「爬楼」拍摄的独立摄影师的访谈。
- [Read a specific length data from socket in Python][10]

``` python
Use a memoryview to wrap your bytearray:

buf = bytearray(toread)
view = memoryview(buf)
while toread:
    nbytes = sock.recv_into(view, toread)
    view = view[nbytes:] # slicing views is cheap
    toread -= nbytes
```

[1]:	https://medium.com/@Blankwonder/%E5%90%84%E7%A7%8D%E5%8A%A0%E5%AF%86%E4%BB%A3%E7%90%86%E5%8D%8F%E8%AE%AE%E7%9A%84%E7%AE%80%E5%8D%95%E5%AF%B9%E6%AF%94-1ed52bf7a803
[2]:	https://github.com/ChrisRx/dungeonfs?utm_content=buffer7ce99&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
[3]:	https://slack.engineering/typescript-at-slack-a81307fa288d
[4]:	https://www.blog.google/topics/machine-learning/fast-drawing-everyone/?utm_content=buffer8f0d7&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
[5]:	http://shields.io/?utm_content=buffer20283&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
[6]:	http://rhaas.blogspot.jp/2017/04/new-features-coming-in-postgresql-10.html?utm_content=buffer63dcd&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
[7]:	https://www.twilio.com/blog/2017/04/wedding-at-scale-how-i-used-twilio-python-and-google-to-automate-my-wedding.html?utm_content=buffer2dbb1&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
[8]:	https://sspai.com/post/38542?utm_campaign=buffer&utm_content=buffer46389&utm_medium=social&utm_source=twitter.com
[9]:	https://sspai.com/post/38802?utm_campaign=buffer&utm_content=bufferb966e&utm_medium=social&utm_source=twitter.com
[10]:	http://stackoverflow.com/a/15964489/667158
