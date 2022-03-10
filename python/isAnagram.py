def isAnagram(word, compareTerm):
    return sorted(word) == sorted(compareTerm)

print(isAnagram('cinema', 'iceman'))
print(isAnagram('sadder', 'dreads'))
print(isAnagram('fried', 'fired'))

def isAnagramRefined(word, compareTerm):
    if len(word) != len(compareTerm):
        return False

    normalizedWord = word.lower()
    normalizedCompare = compareTerm.lower()

    return sorted(word) == sorted(compareTerm)

print(isAnagramRefined('aa', 'a'))
print(isAnagramRefined('cinema', 'iceman'))