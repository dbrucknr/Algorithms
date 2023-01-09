from typing import List
from functools import reduce

def deepFlatten(array: List) -> List:
    return (
        deepFlatten(array[0]) + deepFlatten(array[1:]) 
        if isinstance(array[0], list)
        else [array[0]] + deepFlatten(array[1:])
    ) if len(array) > 0 else []


print(deepFlatten([1, [2], [[3], 4], 5]))
print(deepFlatten([1, [2, [3, [4, [5]]]]]))

def flatten(array: List):
    return reduce(lambda res, x: res + (flatten(x) if isinstance(x, list) else [x]), array, [])

print(flatten([1, [2], [[3], 4], 5]))
print(flatten([1, [2, [3, [4, [5]]]]]))