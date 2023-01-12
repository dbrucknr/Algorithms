def intersection(array, compare):
    result = []
    for value in array:
        if value in compare:
            result.append(value)
    return result

print(intersection([1, 2, 3], [4, 3, 2]))

intersection_alt = set([1, 2, 3, 4, 5]).intersection([3, 4, 5, 6, 7])
print(list(intersection_alt))

intersection_alt_2 = set([1, 2, 3, 4, 5]) & set([3, 4, 5, 6, 7])
print(list(intersection_alt_2))