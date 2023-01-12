from typing import List

def allEqual(array: List) -> bool:
    for value in array:
        if value != array[0]:
            return False
    return True

# print(allEqual([1, 1, 1]))
# print(allEqual([1, 3, 1]))

def allEqualComprehension(array: List) -> List[bool]:
    return [array[i] == array[0] for i, v in enumerate(array)]

print(allEqualComprehension([1, 1, 1]))
print(allEqualComprehension([1, 2, 1]))
print(allEqualComprehension([2, 3, 2, 1]))

array = [1, 1, 1, 1]

# Check if all values are equal to a specified value:
result = all(value == 1 for value in array)
print(result)

# Or:
result = array.count(1) == len(array)
print(result)

# Check if all values are equal when you don't know the array contents
result = len(set(array)) == 1
print(result)