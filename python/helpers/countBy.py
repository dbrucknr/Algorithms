from collections import Counter

def count_elements_by(array, fn=lambda x: x):
    return Counter(map(fn, array))

example_1 = ["apple", "banana", "cherry", "banana", "apple", "cherry"]

print(count_elements_by(example_1))
print(count_elements_by(example_1, len))

example_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(count_elements_by(example_2))
print(count_elements_by(example_2, lambda x: x%2 ==0))

def alt_count_elements_by(array, fn=lambda x: x):
    count = {}
    for item in map(fn, array):
        if item in count:
            count[item] = count.get(item, 0) + 1
    return count