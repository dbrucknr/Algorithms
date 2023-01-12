from math import floor
from typing import List, Callable

def difference(_array: List, __array: List) -> List:
    """Calculates difference between two arrays"""
    unique = set(__array)
    return [value for value in _array if value not in unique]

print(
    difference([1, 2, 3, 3], [1, 2, 4])
)

def differenceBy(_array: List, __array: List, fn: Callable) -> List:
    unique = set(map(fn, __array))
    return [
        value for value 
        in list(map(fn, _array)) if value not in unique
    ]

print(
    differenceBy(
        [2.1, 1.2], [2.3, 3.4], floor
    )
)

print(
    differenceBy(
        [{ "x": 2 }, { "x": 1 }], [{ "x": 1 }], lambda v: v["x"]
    )
)