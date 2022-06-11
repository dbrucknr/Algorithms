from helpers import roundUp


def chunkArray(array, chunkSize):
    return [array[i:i+chunkSize] for i in range(0, len(array), chunkSize)]


chunked = chunkArray([1, 2, 3, 4, 5, 6, 7], 3)
print(chunked)


def chunkArrayIntoN(array, n):
    size = roundUp(len(array) / float(n))
    return [array[i:i+size] for i in range(0, len(array), size)]


N_chunks = chunkArrayIntoN([1, 2, 3, 4, 5, 6, 7], 4)
print(N_chunks)
