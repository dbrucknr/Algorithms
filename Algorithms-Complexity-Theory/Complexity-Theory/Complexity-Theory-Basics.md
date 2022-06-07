# 2 Types of Complexity

1. Space Complexity - how much memory an algorithm needs.
2. Time Complexity - how much time an algorithm needs

Currently memory (space) is very cheap, so we tend not to focus on optimizing it unless you need to (software for a small embedded computer).

Running time tends to be the main focus, as it tends to result in the best experience.

## Time Complexity
* How to measure absolute time?
	* An new computer will be faster than an old computer
	* Super computers vs. smart-phones or raspberry-pi
* **Solution**: Consider the number of steps. This approach is generic, machine independent.

For analyzing algorithsm we have to consider the number of items, or the input size:
* Sorting 10 items -> 100ms
* Sorting 1000 items -> 1000ms

IMPORTANT: 
* **Order of Growth** - We want to make a good guess on how the algoirthm will scale and behave with input size.

**Example: we want a sorting algorithm where the algorithm is approximately linear in terms of the input size. (Ideally a deterministic algorithm where run times are approximately linear).**

* Sorting 100 items -> 100ms
* Sorting 1000 items -> ~1000ms **GOOD**
* Sorting 1000 items -> ~10000ms **BAD**
	* This instance is not scaling well. We like deterministic algorithms where the running times are approximately linear in terms of input.

### Compare Algorithms:

**First**: (Linear / Deterministic time complexity - twice the number of items, results in twice the amount of time. This is a O(N) notation example)
* Sorting 10 items -> 1 ms
* Sorting 20 items -> 2 ms
* Sorting 100 items -> 10 ms

**Second**: (Quadratic / Non-linear - twice the number of items results in four times the amount of time, and ten times the items results in 100 times the amount of time. This is a O(N^2) notation example)
* Sorting 10 items -> 1 ms
* Sorting 20 items -> 4 ms
* Sorting 100 items -> 100 ms


**Asymptotic Analysis** - we evaluate the performance of an algorithm in terms of input size (we don't measure the actual running time). We calculate how the time (or space) taken by an algorithm increases with the input size. 
-  We don’t care about the performance of 10 items, but millions and millions…
