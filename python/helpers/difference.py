from typing import List

def difference(_array: List, __array: List) -> List:
    """Calculates difference between two arrays"""
    unique = set(__array)
    return [value for value in _array if value not in unique]

print(
    difference([1, 2, 3, 3], [1, 2, 4])
)