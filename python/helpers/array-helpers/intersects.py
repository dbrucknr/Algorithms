from typing import List

def intersects(
    first_array: List, 
    second_array: List
) -> bool:
    for data in set(first_array):
        if data in set(second_array):
            return True
    return False
    # return 

print(intersects(['a', 'b'], ['b', 'c'])) # True
print(intersects(['a', 'b'], ['c', 'd'])) # False

def intersectsWithValues(
    first_array: List, 
    second_array: List
) -> List:
    return [value for value in set(second_array) if value in set(first_array)]

print(intersectsWithValues(['a', 'b'], ['b', 'c']))
print(intersectsWithValues(['a', 'b'], ['c', 'd']))