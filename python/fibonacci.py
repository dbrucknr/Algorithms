# Base: Recursive
def fibonacci(index):
    # Base Case(s):
    if index == 0 or index == 1:
        return index
    return fibonacci(index - 1) + fibonacci(index - 2)

print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(11))