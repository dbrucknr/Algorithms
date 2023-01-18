from math import floor
from typing import List, Callable

def intersectionBy(_array: List, __array: List, fn: Callable) -> List:
    unique = set(map(fn, __array))
    return [
        value for value 
        in list(map(fn, _array)) if value in unique
    ]

print(
    intersectionBy(
        [2.1, 1.2], [2.3, 3.4], floor
    )
) # [2]

print(
    intersectionBy(
        [{ "title": 'Apple' }, { "title": 'Orange' }],
        [{ "title": 'Orange' }, { "title": 'Melon' }],
        lambda x: x["title"]
    )
) # ['Orange']