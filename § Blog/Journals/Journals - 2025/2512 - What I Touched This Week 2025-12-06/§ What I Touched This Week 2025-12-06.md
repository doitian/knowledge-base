---
date: 2025-12-06
description: My weekly review report.
series:
- What I Touched
obsidianFiles:
- robot/Readwise Library/Articles/Aleksey Kladov - A Tale of Four Fuzzers (Highlights)
- robot/Readwise Library/Articles/Aleksey Kladov - Generate All the Things (Highlights)
- robot/Readwise Library/Articles/Aleksey Kladov - Swarm Testing Data Structures (Highlights)
- robot/Readwise Library/Articles/Stephen DeLorme - Lightning Self-Custody Works Why Mobile Nodes Are the Future of Bitcoin (Highlights)
- robot/Readwise Library/Articles/Ines Lee - Think First, AI Second (Highlights)
---
# What I Touched This Week 2025-12-06

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2025-12-06]]
**URL**:: [blog.iany.me](https://blog.iany.me/2025/12/what-i-touched-this-week-2025-12-06/)
**Highlights**:: [[Readwise Sync 2025-12-06]]

## Fuzzing Strategies from TigerBeetle

This week I dove deep into TigerBeetle's fuzzing philosophy through several articles by Aleksey Kladov. The collection reveals a systematic approach to building testable systems from the ground up.

- **Design for Fuzzability First**: You don't build a system and then add a fuzzer—the process is almost reversed. Start by sketching minimal interfaces that yield themselves to efficient fuzzing. Minimize the interface by eliminating accidental dependencies and leaving only essential ones.
- **Data-Oriented Design**: Apply data-oriented design principles—think in terms of input data, output data, and the fundamental data transformation the system implements. This makes the code more easily fuzzable.
- **Avoid Modeling When Possible**: Inspired by the PCC paper, avoid modeling altogether. Instead, go and *do* something, then measure the relevant result directly, Grace Hopper style. For example, accept an `Instant` (a `u64` number of nanoseconds) rather than modeling time—this is a major simplification for fuzzing.
- **Four Fuzzer Strategy**: Use multiple fuzzing approaches: (1) positive space fuzzing with ideal lab environments to verify correctness, (2) negative space fuzzing calling all public methods in random order to break things, (3) boundary testing for valid vs. almost-valid-but-invalid codes, and (4) whole subsystem fuzzing.
- **Randomness in Tests**: Don't always use hard-coded seeds. Zig's approach is best—provide `std.testing.random_seed` that's different per run but generated outside the test process. Run tests twice: once with a hard-coded seed for regression testing, and once with a truly random seed for coverage.

**Sources**:
- [A Tale of Four Fuzzers](https://tigerbeetle.com/blog/2025-11-28-tale-of-four-fuzzers/)
- [Generate All the Things](https://matklad.github.io/2021/11/07/generate-all-the-things.html)
- [Swarm Testing Data Structures](https://tigerbeetle.com/blog/2025-04-23-swarm-testing-data-structures/)

## Lightning Network Mobile Nodes and Self-Custody

Stephen DeLorme's article on Lightning self-custody and mobile nodes provided valuable insights into the future of Bitcoin payments, with direct relevance to my work on CKB Fiber.

- **Mobile Receiving Nodes**: For receiving-only nodes, you don't need routing, meaning you don't need all that database storage. This was pioneered by projects like Breez, Phoenix, Mutiny wallet, Blixt, and newer versions of Zeus.
- **Offline Payments Problem**: Even the sharpest performing mobile lightning wallets suffer from a lack of offline payments, which has severely tarnished the perception of Lightning. BIP-353 user names distributed via DNS and recent LDK PRs for async payments are addressing this.
- **Capital Efficiency**: Splicing is a powerful tool for easing capital constraints for LSPs. The `option_zero_reserve` allows channel partners to choose not to use a channel reserve balance—great for UX, though it requires solving minimal capacity restrictions (relevant for CKB Fiber).
- **Graduated Wallet Model**: A wallet that begins with a custodial service or trust-minimized technology, then graduates to a Lightning channel when the balance grows to a certain threshold. This helps LSPs avoid opening "non-productive" channels to users just experimenting with the app.
- **Dust Limit Considerations**: Amounts below the dust limit (like a 21 sat Nostr zap) wouldn't be claimable on-chain anyway, suggesting alternative approaches for micro-transactions.

**Source**: [Lightning Self-Custody Works: Why Mobile Nodes Are the Future of Bitcoin](https://www.voltage.cloud/blog/lightning-self-custody-works)

## Think First, AI Second

Ines Lee's article on using AI as a thinking partner rather than a solution generator resonated deeply with my own experience using AI tools.

- **Active vs. Passive AI Use**: Active AI use means building understanding while collaborating with the model. Frame the problem yourself, make an initial pass, then use AI to challenge assumptions, uncover blind spots, and sharpen arguments. Studies show this approach maintains cognitive engagement even while using AI.
- **AI as Coach, Not Cheerleader**: Shift AI from talking to you about your work (where it's sycophantic) to talking to other editors about your work (where it's professionally candid). You're no longer the audience, so it drops the protective politeness.
- **Combat Illusion of Understanding**: AI explains things in ways that are easy to follow, making us susceptible to the "illusion of understanding." We overestimate what we've learned. Real comprehension emerges when forced to articulate thinking, because explaining reveals gaps we didn't know existed.
- **Practical Prompts**: Use prompts like "Ask exactly 5 high-leverage questions before proposing solutions," "Act as an editor recommending whether to publish this piece," "Analyze my reasoning and create an architecture of my thinking," "Switch to devil's advocate mode and dismantle my thesis," and "Ask me to explain this as if teaching it to someone else."

**Source**: [Think First, AI Second](https://every.to/emails/think-first-ai-second)

---

## Obsidian Links

- [[Aleksey Kladov - A Tale of Four Fuzzers (Highlights)]]
- [[Aleksey Kladov - Generate All the Things (Highlights)]]
- [[Aleksey Kladov - Swarm Testing Data Structures (Highlights)]]
- [[Stephen DeLorme - Lightning Self-Custody Works Why Mobile Nodes Are the Future of Bitcoin (Highlights)]]
- [[Ines Lee - Think First, AI Second (Highlights)]]
