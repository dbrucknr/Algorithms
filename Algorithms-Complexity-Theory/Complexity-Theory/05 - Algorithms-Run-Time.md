![[Screen Shot 2022-06-07 at 3.09.30 PM.png]]

Constant time complexity is best possible O(1).

Linearithmic time complexity is the threshold, anything above that is impractical - too slow and unusable.


### Constant Time Complexity O(1) Example
* Swapping two numbers or deciding whether a number is odd or even.

```
function swapNums(num1, num2) {
	temp = num1;
	num1 = num2;
	num2 = temp;
	return (num1, num2)
}
```

### Logarithmic Time Complexity O(logN) Example
* Finding an arbitrary item in a sorted array
* Check whether there is a cycle in a graph when solving Kruskal-algorithm (with disjoint sets)

### Linear Time Complexity O(N) Example
* Finding the maximum value in an array of numbers
```
function findMax(a: number[]) {
	let max = a[0];
	for (let i = 0; i < a.length; i++) {
		if (a[i] > max) {
			max = a[i];
		}
	}
	return max
}
```

### Linearithmic Time Complexity O(N * logN) Example:
* Mergesort, Quicksort, Heapsort
* Finding closest pair of points with divide and conquer method

---
**These time complexities are not useful at scale / no practical applications:**

### Polynomial Time Complexity O(N^k)
Where k = 2 / Quadratic
* Bubble Sort, Insertion sort
* Finding closest pair of points with brute force approach

### Exponential Time Complexity O(c^N)
Where c is a constant
* Towers of Hanoi problem - c = 2 in this example
* Calculating fibonacci numbers with recursive manner - c = 2 in this example as well
* Traveling salesman problem with dynamic programming implementation.

### Factorial Time Complexity O(N!)  
**Worst Case: we don't know of any algorithms slower than this**. 
* Solving the traveling salesman problem with brute force search