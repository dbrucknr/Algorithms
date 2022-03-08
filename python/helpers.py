def roundUp(n):
    return int(-1 * n // 1 * -1)

def roundDown(n):
    return int(n // 1)

def some(array, callback):
    return any(callback(i) for i in array)

def every(array, callback):
    return all(callback(i) for i in array)

# I think this is the Python Equivalent of .some in JS
print(any(lambda x: x == 'b' for value in ['a', 'b', 'c']))
print(some(['a', 'b', 'c'], lambda x: x == 'b'))

# I think this is the Python Equivalent of .every in JS
print(all(lambda x: x == str(x) for value in ['a', 'b', 'c']))
print(every(['a', 'b', 'c'], lambda x: x == str(x)))