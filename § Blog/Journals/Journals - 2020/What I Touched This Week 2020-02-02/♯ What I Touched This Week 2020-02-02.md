---
date: 2020-02-02
description: My weekly review report.
series:
- What I Touched
test: https://medium.com/qed-it/the-incredible-machine-4d1270d7363a
---

# What I Touched This Week 2020-02-02

## Zero-knowledge Proof

-   [The Incredible Machine - QEDIT - Medium](https://medium.com/qed-it/the-incredible-machine-4d1270d7363a)

-   [1998 - Jean-Jacques, Louis - How to Explain Zero-Knowledge Protocols to Your Children.pdf](http://pages.cs.wisc.edu/~mkowalcz/628.pdf)

-   [Zero Knowledge Proofs: An illustrated primer -- A Few Thoughts on Cryptographic Engineering](https://blog.cryptographyengineering.com/2014/11/27/zero-knowledge-proofs-illustrated-primer/)

    -   "Thus if the amount of information I can extract is identical in the 'real experiment' and the 'time machine experiment', yet the amount of information Google puts into the 'time machine' experiment is exactly zero --- then this implies that even in the real world the protocol must not leak any useful information."

-   [Zero Knowledge Proofs: An illustrated primer, Part 2 -- A Few Thoughts on Cryptographic Engineering](https://blog.cryptographyengineering.com/2017/01/21/zero-knowledge-proofs-an-illustrated-primer-part-2/)

    -   "We're asking that a protocol be both sound --- meaning that a bogus Prover can't trick some Verifier into accepting a statement unless it has special knowledge allowing it to prove the statement --- but we're also asking for the existence of an algorithm (the simulator) that can literally cheat. Clearly both properties can't hold at the same time. The solution to this problem is that both properties don't hold at the same time. "

    -   "A knowledge extractor (or just 'Extractor' for short) is a special type of Verifier that interacts with a Prover, and --- if the Prover succeeds in completing the proof --- the Extractor should be able to extract the Prover's original secret."

    -   "The Extractor is not required to exist during a normal run of the protocol."

-   [初识「零知识」与「证明」 - SECBIT Blog](https://sec-bit.github.io/blog/2019/07/31/zero-knowledge-and-proof/)

    -   "零知识证明是打通链上数据与链下计算的关键技术，也是实现链上数据隐私保护的重要途径"

    -   "证明不仅仅是一个严格推理，而且凝结了似乎很难机械化的创造性思维。证明中蕴含了大量的「知识」，每一次的突破，都将我们的认知提升到一个新的高度。"

-   [从「模拟」理解零知识证明：平行宇宙与时光倒流 - SECBIT Blog](https://sec-bit.github.io/blog/2019/08/06/understand-zero-knowledge-proof-by-simulator/)

-   [读心术：从零知识证明中提取「知识」 - SECBIT Blog](https://sec-bit.github.io/blog/2019/08/28/extractor-and-proof-of-knowledge/)

-   [亚瑟王的「随机」挑战：从交互到非交互式零知识证明 - SECBIT Blog](https://sec-bit.github.io/blog/2019/11/01/from-interactive-zkp-to-non-interactive-zkp/)

## Blockchain

-   [The Schnorr/Taproot proposal is now published as BIPs 340, 341, and 342](https://github.com/bitcoin/bips/)

-   [How the Nervos CKByte Gets its Value ](https://medium.com/nervosnetwork/how-the-nervos-ckbyte-gets-its-value-f0bd43333035?source=rss----4dab634dc673---4)

    This is a core question for any decentralized project, and it's one we've thought carefully about in designing the CKByte as the protocol token of the Nervos Network. Ultimately, we believe a token's value is derived from its core function or utility.

-   [Sunsetting Mist - Alex Van de Sande - Medium ](https://medium.com/@avsa/sunsetting-mist-da21c8e943d2)

    Why Mist team no longer builds a single app

-   [以太坊二层扩容之路：Plasma 衰落与 Rollup 崛起 - 链闻 ChainNews](https://www.chainnews.com/articles/321827333242.htm)

    -   "第一个问题是， 每个用户 必须监控和验证 Plasma MVP 链上的所有交易，以检测恶意运营商的行为并及时退出。然而，事务验证成本高昂，并且这种监视需求为参与 Plasma 链增加了大量开销。"

    -   "考虑到 Plasma 链可以任意增长，而以太坊区块已经接近其容量，几乎不可能将整个 Plasma 链倾倒到以太坊的主网上。因此，几乎可以肯定的是，大量退出会把以太坊挤爆。这就是所谓批量退出问题。"

## COVID-19

-   [The Lancet Coronavirus ](https://www.thelancet.com/coronavirus)

    "This hub page will house all articles, comments, and editorial...

-   [Complexity of the Basic Reproduction Number (R0) - Volume 25, Number 1---January 2019 - Emerging Infectious Diseases journal - CDC](https://wwwnc.cdc.gov/eid/article/25/1/17-1901_article)

-   [新型冠状病毒的来龙去脉](https://pic1cdn.luojilab.com/html/p/w42LM6M/rrpKM7BV4XIWLK3l8z2q.html?from=timeline&isappinstalled=0)

-   [关于印发新型冠状病毒感染的肺炎诊疗方案（试行第三版）的通知](http://www.nhc.gov.cn/xcs/zhengcwj/202001/f492c9153ea9437bb587ce2ffcbee1fa.shtml)

-   [试剂盒困局：为何确诊这么难？](https://mp.weixin.qq.com/s/Xq7jT0ErmFsIXZY5m3xoNQ)

-   [武汉封城后，这支上海的队伍进去了！沪首批重症和呼吸科医师已出征，今夜到达](http://wenhui.whb.cn/zhuzhanapp/yiliao/20200123/317060.html?from=timeline&isappinstalled=0)

-   Noisy Turtle (@NoisyTurtle2600): Updated Wuhan #2019-nCoV cases compared with other viruses. I managed to find some numbers on MERS, but that disease didn't rapidly rise from 100 like Wuhan, SARS and Swine Flu has. Lower cases and higher fatality rate makes that more like the two Ebola viruses (EVD). [Tweet](https://twitter.com/NoisyTurtle2600/status/1221365780849119233)
-   方舟子 (@fangshimin): 《柳叶刀》总编呼吁媒体不要夸大2019新型肺炎的危害，因为根据现在掌握的情况该新型病毒只有中等的传染性和较低的致病性，没必要夸大其词制造恐慌。[Tweet](https://twitter.com/fangshimin/status/1221287783714574336)
-   Dayomoses (@Dayo_Moses): 没错，不要小看明星后援会的组织能力和能动性，既有经验又有决心，在统筹分配方面有效率多了。[Tweet](https://twitter.com/Dayo_Moses/status/1221696130955612161)

## Remote and Management

-   [[Workflow Guide] Accomplish Your Big Goals With Don't Break the Chain ](https://doist.com/blog/dont-break-the-chain/)

    Don't Break the Chain (or The Seinfeld Method) is a productivity strategy coined after comedian Jerry Seinfeld. Curiously, he's claimed to have no part in its inception. The productivity method commits you to completing a daily goal for an extended period of time.

-   [The Ultimate Guide to Remote Work | Zapier](https://zapier.com/learn/remote-work/)

-   [How to collaborate across time zones ](https://zapier.com/blog/how-to-work-asynchronously/)

    My team is spread across four states and three time zones. People often ask me how we find good times to meet. My answer: it's not easy, but it's also rarely necessary. Working remotely, especially when your team is distributed across the globe, means working asynchronously. And it's a skill.

-   [9 Lessons That Made Me a Better Remote Worker](https://open.buffer.com/better-remote-worker/)

-   [How to Create A Remote Work Routine That Works](https://open.buffer.com/remote-work-routine/)

    -   "Changing locations once in a while can jumpstart creativity and productivity!"

-   [Remote Projects 101: The Remote Guide to Project Management | Twist](https://twist.com/remote-work-guides/remote-project-management)

## Programming

-   [A New Network Stack For Zcash](https://www.zfnd.org/blog/a-new-network-stack-for-zcash/)

    -   [ZcashFoundation/zebra ](https://github.com/ZcashFoundation/zebra)

        Zcash rewrote using Rust

-   [Tide Channels ](https://blog.yoshuawuyts.com/tide-channels/)

    Websockets in Tide

-   [Packaging a Rust project for Debian](https://blog.hackeriet.no/packaging-a-rust-project-for-debian/)

-   [Building a Functional Core in Elixir ](https://medium.com/@KevinHoffman/building-a-functional-core-in-elixir-6201ddcb4300)

    That's right, I'm that guy that reads a book multiple times. The first time I go through because I'm excited and inspired about some topic, and I don't want to lose the momentum by putting the book down --- without regard for the author's advice to do just that.

-   [Technical Debt Is like a Tetris Game - Fluent C++](https://www.fluentcpp.com/2020/01/17/technical-debt-is-like-a-tetris-game/?utm_source=Iterable&utm_medium=email&utm_campaign=the_overflow_newsletter&utm_content=01-22-20)

-   [Goodbye, Clean Code ](https://overreacted.io/goodbye-clean-code/)

    It was a late evening. My colleague has just checked in the code that they've been writing all week. We were working on a graphics editor canvas, and they implemented the ability to resize shapes like rectangles and ovals by dragging small handles at their edges.

-   [Shedding Some Light on Dark ](https://medium.com/@KevinHoffman/shedding-some-light-on-dark-9086b45988ed?source=rss-4a61baec208d------2)

    Trace-Driven Development

-   [The Throw Keyword was a Mistake ](https://hackernoon.com/the-throw-keyword-was-a-mistake-l9e532di)

    Exception Handling Decades ago when a program crashed you would see a dire error message This meant that something horrible had happened. Usually the problem was the software tried to read or write some memory outside its address space.

-   [NP-completeness - Wikiwand](https://www.wikiwand.com/en/NP-completeness)

    -   "A problem is said to be [NP-hard](https://www.diigo.com/en/NP-hard) if everything in NP can be transformed in polynomial time into it, and a problem is NP-complete if it is both in NP and NP-hard."

-   [NP (complexity) - Wikiwand](https://www.wikiwand.com/en/NP_(complexity))

    -   "NP is the [set](https://www.diigo.com/en/Set_(mathematics)) of decision problems for which the [problem instances](https://www.diigo.com/en/Computational_complexity_theory#Problem_instances), where the answer is "yes", have [proofs](https://www.diigo.com/en/Mathematical_proof) verifiable in [polynomial time](https://www.diigo.com/en/Polynomial_time)."

        There exists a verifier which can checks a solution is correct in polynomial time.

    -   "the complexity class [co-NP](https://www.diigo.com/en/Co-NP) for which the answer "no" can be verified in polynomial time."

        Verifier which checks the answer is wrong in polynomial time

## Other Readings

-   [疫情谣言满天飞，送你两个辟谣神器 - 少数派](https://sspai.com/post/58645)

-   [The Art of Manliness's Brett McKay on How He Stays Productive](https://doist.com/blog/brett-mckay-art-of-manliness-productivity-profile/)

-   ["Laser Mode" on your Mac --- make your workspace distraction-free with a simple keystroke.](https://medium.com/@miloszfalinski/laser-mode-on-your-mac-make-your-workspace-distraction-free-with-a-simple-keystroke-65938680cfac)

-   [How much longer will we trust Google's search results? ](https://www.theverge.com/tech/2020/1/24/21079696/google-serp-design-change-altavisa-ads-trust)

    Happy Friday to you! I have been reflecting a bit on the controversy du jour: Google's redesigned search results. Google is trying to foreground sourcing and URLs, but in the process it made its results look more like ads, or vice versa.

-   [The real reason Boeing's new plane crashed twice](https://www.youtube.com/watch?v=H2tuKiiznsY)

-   [所有的公共卫生问题 归根到底都起源于社会结构问题](https://c.m.163.com/news/a/F4051HER000189PS.html?spss=wap_refluxdl_2018&spssid=7ca4a87b91b56d31fbccd73f21de285e&spsw=1&isFromH5Share=article&from=timeline&isappinstalled=0)

    -   "这里面最严重的问题是：信任。货源是否可信，需求端是否可信，节点是否可信，大量的时间和精力花在了"确认"这个看起来简单的动作上面。因为自组织的方式聚起了弱连接的一帮人，信任度很难建立，也没有权威的可信第三方来实现"双向确认"，这导致大量的无交易和浪费，等待。虽然理论上我们知道这是没有价格指引下，去中心化协作的千古难题，但我们依然不得不经历这一切。"

    -   "任何命运赐予的礼物，都在暗中标好了价格"

-   [How to Compete With AWS -- tecosystems](https://redmonk.com/sogrady/2020/01/24/how-to-compete-with-aws/)

-   [Make the iPad more like the Mac](https://medium.com/@radutzan/make-the-ipad-more-like-the-mac-9a5c135b214f)

-   [I learned how to read my coworkers from an FBI spymaster - Work Life by Atlassian](https://www.atlassian.com/blog/teamwork/behavior-analysis-fbi-counterintelligence)

    -   "trust is less about integrity and more about predictability"

    -   "Just because I like you doesn't mean I can trust you"

    -   "Dreeke also places a high value on competence."

    -   "Finally, look for signs that they're keen to help you be successful."

-   [Elinor Ostrom and the solution to the tragedy of the commons | American Enterprise Institute - AEI](https://www.aei.org/articles/elinor-ostrom-and-the-solution-to-the-tragedy-of-the-commons/)

## Books

-   [ian yang's review of 解忧杂货店](https://www.goodreads.com/review/show/3158115675)

-   [ian yang's review of 腾讯传](https://www.goodreads.com/review/show/3147647526)

-   [ian yang's review of 血疫:埃博拉的故事](https://www.goodreads.com/review/show/3167841442)

## Bookmarks

-   [漢典](https://www.zdic.net/)

-   [World Edition - The Atlantic](https://www.theatlantic.com/world/)

-   [The Verge](https://www.theverge.com/)

-   [Polygon](https://www.polygon.com/)
