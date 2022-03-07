def chunkArray(array, chunkSize):
    return [array[i:i+chunkSize] for i in range(0, len(array), chunkSize)]

print(chunkArray([1, 2, 3, 4, 5, 6, 7], 3))