# The Big Ordo Notation (O)
-   Landau notation
-   It describes the limiting behavior of a function (i.e. run time (f) in terms of the input size (n)), when the argument tends towards a particular value or infinity.
-   It is used to classify algorithms by how they respond to input size.
-   Processing time or working space requirements.

We don't concern ourselves with small inputs, but rather the asymptotic behavior (millions / billions) of input values.

**Big Ordo Notation** is used to classify algorithms by how they respond in their processing time or working space requirements changes in relation to the input size.
* Recall that we tend not to concern ourselves with working space, but it's important in some contexts.

## Example:
Bubble sort:
-   Has an O(N^2) running time complexity (Bad - Quadratic)
-   It is also true that bubble sort is in O(N^3), or O(N^4), or O(N^5)....
	-   There’s no point in stating : O(N^3), or O(N^4), or O(N^5)....
	-   It is like stating that x < 10 - it is implicit that x < 100


