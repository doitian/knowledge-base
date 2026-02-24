---
date: 2026-02-20T00:00:00+0800
draft: false
aliases:
  - Power of Monoid, Beauty of Simplicity
tags:
  - algorithm
  - math
  - programming
description: "Why the monoid—a set with an associative binary operation and identity—is both simple and surprisingly powerful: divide-and-conquer, finger trees, and the art of choosing the right abstraction."
obsidianFiles:
  - para/lets/c/Cryptography/Elliptic Curve Scalar Multiplication
katex: true
---
# Power of Monoid, Beauty of Simplicity

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2026-02-19]]
**URL**:: [blog.iany.me](https://blog.iany.me/2026/02/power-of-monoid-beauty-of-simplicity/)

A monoid is one of the smallest useful abstractions in algebra: a set closed under an associative binary operation, with an identity element. That simplicity is exactly why it shows up everywhere—from summing numbers and concatenating strings to powering divide-and-conquer algorithms and elegant data structures like finger trees. This post walks through what monoids are, why they give you "compute power" for free when you can phrase a problem in terms of them, and how to think about choosing the right monoid and predicate when you do.

<!--more-->


## What is a monoid?

A monoid is a set $S$ equipped with a binary operator $\bullet$ and an identity element $e$ ([Wikipedia](https://en.wikipedia.org/wiki/Monoid)).

- The operator is closed on $S$. For all $a, b \in S$, the result $a \bullet b$ is also in $S$.
- The operator is associative: For all $a,b,c \in S$, $(a \bullet b) \bullet c = a \bullet (b \bullet c)$
- The identity element $e$ satisfies $e \bullet a = a \bullet e = a$ for all $a \in S$.

For example, The integer numbers with the operator addition (`+`) is a monoid, where the identity element is `0`. The integer numbers with the operator multiplication (`x`) is also a monoid with the identity element `1`.

The set of finite lists with the operator concatenation is a monoid since:

- The operator is closed because concatenation of two finite lists is also a finite list.
- The operator is associative, because both $(a \bullet b) \bullet c$ and $a \bullet (b \bullet c)$ result in a new list by placing elements of $a, b, c$ consecutively.
- The identity element is the empty list.

The integer numbers with the operator `max` is a counterexample. The operator is closed and associative, but there is no identity element. Given any integer $e$, there's always a smaller integer $a$ such that $e \bullet a = e \ne a$. However, `max` on the integer set with a lower bound is a monoid, such as the non-negative integers where the identity element is the lower bound `0`.

## Divide and conquer: why associativity matters

At first glance, associativity may seem too trivial to be useful in programming. However, associativity is what enables powerful divide-and-conquer strategies, where problems can be split into parts, solved independently, and then safely recombined.

### Exponentiation by Squaring

Let’s begin with a simple application: repeatedly applying the binary operator to the same element.

$$
\underbrace{a \bullet a \bullet \cdots \bullet a}_{a \text{ appears } n \text{ times}}
$$

Instead of applying the binary operator $n-1$ times sequentially, we exploit associativity to group every two instances of $a$ together recursively. This gives us a smaller problem when n is even:

$$
\underbrace{(a \bullet a) \bullet \cdots \bullet (a \bullet a)}_{(a \bullet a) \text{ appears } \frac{n}{2} \text{ times}}
$$

When n is odd:

$$
a \bullet \underbrace{(a \bullet a) \bullet \cdots \bullet (a \bullet a)}_{(a \bullet a) \text{ appears } \frac{n-1}{2} \text{ times}}
$$

We only need to compute $a \bullet a$ once to turn the problem of size $n$ to size $n/2$. Repeating the process on $(a \bullet a)$ gives the [Exponentiation by Squaring](https://en.wikipedia.org/wiki/Exponentiation_by_squaring) algorithm, which requires at most $\displaystyle 2 \lfloor \log _{2}n\rfloor$ computations that is more efficient than $n-1$ when $n$ is greater than 4.

For integers or real numbers under multiplication (`×`), exponentiation by squaring is an efficient algorithm to compute positive integer powers. Since the set of elliptic curve points under point addition forms a monoid, this same method can also be used to compute [[Elliptic Curve Scalar Multiplication]].

### General Divide-and-Conquer Search Algorithm

We can generalize the divide-and-conquer method to search an element in a sequence based solely on associativity.

The result of applying the monoid operator to a sequence from left to right serves as a summary of that sequence. If a predicate can determine whether a given element is in the sequence based solely on this summary, we can devise a general divide-and-conquer search algorithm.

Let’s say we want to search for a target element in the sequence $t_1, \ldots, t_n$, where each $t_i$ belongs to a monoid $(S, \bullet, e)$. Here, $S$ is the underlying set, $\bullet$ is the binary operation, and $e$ is the identity element.

We don't know which kind of predicates works for the search algorithm. Let's give a best guess that the predicate $p$ is a function of the monoid "summary" that $p(t_1 \bullet \cdots \bullet t_n)$ is true if and only if $t$ is in the sequence $t_1, \dots, t_n$.

Assume that $p(t_1 \bullet \cdots \bullet t_n)$ is true, thus the target element $t$ is in the sequence. We divide the sequence into two halves: $t_1,\ldots,t_k$ and $t_{k+1},\ldots,t_n$, where $1 \le k \le n$. We then evaluate $p(t_1 \bullet \cdots \bullet t_k)$ to determine whether the target element lies in the first or second half, and continue the search.

Based on this observation, we can deduce the following property of the predicate: there exists an index $x$ such that

$$
p(t_1 \bullet \cdots \bullet t_k) := \begin{cases}
\text{false} & \text{if } k < x, \\
\text{true} & \text{if } k \ge x.
\end{cases}
$$

$t_x$ is the target element if such $x$ exists; otherwise, the target element does not exist in the sequence.

Intuitively, the target element is the turning point at which the predicate on the running summary changes from false to true.

![[Monoid search turning point.excalidraw.svg]]
%%[[Monoid search turning point.excalidraw|🖋 Edit in Excalidraw]]%%

Note that $p$ makes sense only on the summary of any prefix of the sequence. If we need to continue the search in the second half, we must remember the summary of the scanned prefix.

Now we can define the search algorithm $\mathrm{Search}(p, s, \{t_i,\ldots,t_j\})$ where

- $s$ is the summary of scanned prefix $t_1 \bullet \cdots \bullet t_{i-1}$ when $i > 1$ or the identity element $e$ otherwise.
- $t_i, \ldots, t_j$ is the sub-range to search next.
- $p$ is the predicate as defined above

The algorithm proceeds as follows:

- If $p(s \bullet t_i \bullet \cdots \bullet t_j$) is false, the target element does not exist. The algorithm aborts with an error.
- Otherwise, if there's only one element ($i = j$), $t_i$ is the target element. The algorithm aborts with the found result.
- Otherwise, choose a pivot index $i \le m \lt j$ to split the sequence into two nonempty halves: $t_i, \ldots, t_m$ and $t_{m+1},\ldots,t_j$. Test $p(s \bullet t_i \bullet \cdots \bullet t_m)$ that
    - If it is true, continue the search in the first half: $\mathrm{Search}(p, s, \{t_i,\ldots,t_m\})$
    - Otherwise, continue the search in the second half: $\mathrm{Search}(p, s \bullet (t_i \bullet \cdots \bullet t_m),\{t_{m+1},\ldots,t_j\})$

The algorithm starts with $\mathrm{Search}(p, e, \{t_1, \ldots, t_k\})$.

### Application: Random-Access Sequence

An application of the search algorithm is accessing the nth element in the sequence.

We initialize the sequence to all 1s and use the monoid of non-negative integers with addition $(\mathbb{N},+,0)$:


$$
\underbrace{1, \ldots, 1}_{n \text{ times}}
$$

The predicate to find the i-th (starting from 0) element is:

$$
p_i(s) := s > i
$$

It may seem silly to search for the i-th 1 in a sequence of 1s, but we can store any data in the sequence and attach the monoid values as annotations to guide the search algorithm.

![[Sequence Monoid Annotations.excalidraw.svg]]
%%[[Sequence Monoid Annotations.excalidraw.md|🖋 Edit in Excalidraw]]%%

### Application: Max-Priority Queue

Another application is finding the element with the max priority.

We use the monoid of non-negative integers with operator `max` $(\mathbb{N},\mathrm{max},0)$ and assume that the maximum value has the maximum priority.

The predicate to find the element with the max priority is

$$
p(s) := s = m
$$

Where $m$ is the monoid summary of the entire sequence—that is, the maximum value in the sequence. The predicate checks whether the summary equals to $m$.

### Annotated Search Tree

A natural way to support the divide-and-conquer search is an *annotated binary tree*. Store the sequence elements at the leaves, and at each node store the monoid summary of the subtree—e.g. the sum of lengths or the maximum priority in that subtree. The predicate can then be evaluated on the left subtree’s annotation to decide whether to descend left or right, and the prefix summary is updated when going right by combining it with the left subtree’s summary.

![[Annotated binary tree.excalidraw.svg]]
%%[[Annotated binary tree.excalidraw|🖋 Edit in Excalidraw]]%%

A plain binary tree can degenerate to a list in the worst case, so operations may become linear. A more advanced structure, the *finger tree*[^1], keeps the tree balanced and supports efficient access at both ends and in the middle; each node carries a monoidal “measure” of its subtree, and the same search strategy applies. In Haskell, [Data.Sequence](https://hackage-content.haskell.org/package/containers-0.8/docs/Data-Sequence.html) from the `containers` library implements sequences as finger trees with size (length) as the measure, giving $O(\log n)$ indexing, splitting, and concatenation.

[^1]: Hinze, R., & Paterson, R. (2006). Finger trees: A simple general-purpose data structure. *Journal of Functional Programming, 16*(2), 197–217. Cambridge University Press. <https://www.cs.ox.ac.uk/ralf.hinze/publications/FingerTrees.pdf>

### Utility of the Identity Element

The general divide-and-conquer algorithm does not require a monoid—only a semigroup. A semigroup is a fancy word for a set equipped with a closed, associative binary operator but lacking an identity element. The presence of an identity element makes monoids convenient to work with.

The identity element serves as a natural default value or starting point for algorithms. For instance, in the search algorithm, the summary of the scanned prefix is initialized to $e$. Without an identity element, we need an additional flag to indicate whether any prefix has been scanned, and the algorithm would have to branch conditionally based on that flag.

## The art of choosing monoid and predicate

In the random-access example we used $(\mathbb{N}, +, 0)$ and annotated each position with $1$—the summary of a segment is its length, and the predicate $s > i$ tells us whether the $i$-th element lies in the prefix we have so far. In the max-priority queue we used $(\mathbb{N}, \max, 0)$ (or a bounded variant): the summary is the maximum value in the segment, and the predicate $s = m$ identifies the segment that contains the global maximum. In both cases, the monoid was chosen so that the *combined* summary over a range is exactly what the predicate needs to decide where to go next.

The flip side is that finding both the right monoid and the right predicate can be tricky. At each step the search has access only to the monoid summary of the prefix (or segment) seen so far, so the predicate must be decided from that summary alone. The monoid must be rich enough to supply the information the predicate needs. Sometimes the natural summary (e.g. sum or max) suggests the predicate (e.g. $s > i$ or $s = m$). Sometimes you must try a different carrier or operation, or encode extra information into the monoid (e.g. pairs or custom types), so that the predicate can be expressed. There is no universal recipe—it is a matter of design and experimentation. Reframe the problem as: “What do I need to know about a segment to decide the next step?” Then choose a monoid that can represent that knowledge and a predicate that uses it.