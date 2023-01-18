from typing import List, Callable

def findIndex(array: List, func: Callable):
    for index, value in enumerate(array):
        if func(value):
            return index
    return -1

print(
    findIndex([3, 2, 9, 1, 5, 6], lambda v: v == 1) # 3
)