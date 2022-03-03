# Base: Recursive
def fibonacci(index):
    # Base Case(s):
    if index == 0 or index == 1:
        return index
    return fibonacci(index - 1) + fibonacci(index - 2)

print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(11))

# Recursive Memoization
#  - Optimized to reduce number of calculations required
def fibonacciMemoized(index, cache = None):
    # Check: Initialize cache
    if cache is None: 
        cache = {}
    # Check: Cache memory
    if index in cache: 
        return cache[index]

    result = index
    # Base Case(s)
    if result < 2: 
        result = index
    else: 
        result = fibonacciMemoized(index - 1) + fibonacciMemoized(index - 2)
    return result

print(fibonacciMemoized(5))
print(fibonacciMemoized(10))
print(fibonacciMemoized(11))

# Bottom-up 
# - Optimized to solve sub-problems for when they're needed
# - Throw away previous calculation to reduce memory (space complexity)

def fibonacciBottomUp(index):
    a = 1
    b = 1
    for i in range(2, index):
        a, b = b, a + b
    return b

print(fibonacciBottomUp(5))
print(fibonacciBottomUp(10))
print(fibonacciBottomUp(11))