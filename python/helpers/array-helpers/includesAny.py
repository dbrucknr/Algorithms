def includesAny(array, values):
    return any(i for i in array if i in values)

print(includesAny([1, 2, 3, 4], [2, 9]))
print(includesAny([1, 2, 3, 4], [8, 9]))

def includesFun(array, callback):
    return any(i for i in array if callback(i))

print(includesFun([0, 1, 2, 0], lambda x: x >= 2))