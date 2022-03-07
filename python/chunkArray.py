def chunkArray(array, chunkSize):
    return [array[i:i+chunkSize] for i in range(0, len(array), chunkSize)]

print(chunkArray([1, 2, 3, 4, 5, 6, 7], 3))

def roundUp(n):
    return int(-1 * n // 1 * -1)

def roundDown(n):
    return int(n // 1)

def chunkArrayIntoN(array, n):
    size = roundUp(len(array) / float(n))
    return [array[i:i+size] for i in range(0, len(array), size)]

print(chunkArrayIntoN([1, 2, 3, 4, 5, 6, 7], 4))