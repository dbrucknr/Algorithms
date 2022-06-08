# Analyzing Loops
* The number of bested loops is a good indicator for the running time complexity category.
	* The more, the slower it gets

## Constant Time Complexity O(1)
* Swapping two numbers or deciding whether a number is even or odd

```
function swapNums(num1, num2) {
	temp = num1;
	num1 = num2;
	num2 = temp;
	return (num1, num2)
}
```

Changes references - a very fast procedure.

---

## Linear Running Time O(N)
* When we have a for loop
	* Inside the loop we make O(1) running time operations

```
for item in iterable:
	do O(1) operation
```

Example:  When you sum up items, or check whether an item is equal to 10 in a 1-dimensional array

---

## Quadratic Running Time O(N^2)
* We have a for loop
	* We have a nested for loop
		* Inside the nested for loop we make O(1) running time operations

```
for nested_iterable in iterable:
	for nested_item in nested_iterable:
		do O(1) operation (ex: print nested_item, check value)
```

OR:

```
for item in iterable:
	for next_item in iterable:
		do some O(1) operation
```

---

### Polinomial Running Time O(N^k)
* More nested loops...