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


def fibonacci_memoized(index, cache=None):
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
        result = fibonacci_memoized(index - 1) + fibonacci_memoized(index - 2)
    return result


print(fibonacci_memoized(5))
print(fibonacci_memoized(10))
print(fibonacci_memoized(11))

# Bottom-up
# - Optimized to solve sub-problems for when they're needed
# - Throw away previous calculation to reduce memory (space complexity)


def fibonacci_bottom_up(index):
    a = 1
    b = 1
    for i in range(2, index):
        a, b = b, a + b
    return b


print(fibonacci_bottom_up(5))
print(fibonacci_bottom_up(10))
print(fibonacci_bottom_up(11))
