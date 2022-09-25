# FoundationDB Test Technologies

#software-test

## Repeatability

* Pseudo-concurrency
* Simulate external communication
* Deterministic

Eliminate any external randomness that cannot be controlled.

## Simulation Test

* Repeatable thus saving time to reproduce the bug.
* Explore the space more efficiently than the real world.
	* For example, simulating random network disconnection, power shortage.

## Challenges

* It takes efforts to keep deterministic
* Hard to implement test oracles in some apps to tell whether there's a bug.

## Interesting Observations

* Simply stopping and restarting in reverse order finds many bugs.

## References

* [Simulation and Testing — FoundationDB 6.2](https://apple.github.io/foundationdb/testing.html)
* [Testing Distributed Systems w/ Deterministic Simulation - Will Wilson - YouTube](https://www.youtube.com/watch?v=4fFDFbi3toc)
* [Autonomous Testing and the Future of Software Development - Will Wilson - YouTube](https://www.youtube.com/watch?v=fFSPwJFXVlw)
* [My Diigo Outline](https://www.diigo.com/outliner/irpef3/Archive---202004---FoundationDB-Test?key=tnfaeajeb1)