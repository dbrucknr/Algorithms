from typing import List

def allEqual(array: List) -> bool:
    for value in array:
        if value != array[0]:
            return False
    return True

# print(allEqual([1, 1, 1]))
# print(allEqual([1, 3, 1]))

def allEqualComprehension(array: List) -> List:
    return [array[i] == array[0] for i, v in enumerate(array)]

print(allEqualComprehension([1, 1, 1]))
print(allEqualComprehension([1, 2, 1]))
print(allEqualComprehension([2, 3, 2, 1]))