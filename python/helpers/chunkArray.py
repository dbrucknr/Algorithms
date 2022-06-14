from helpers import roundUp
import sys


def chunk_array(array, chunk_size):
    return [array[i:i+chunk_size] for i in range(0, len(array), chunk_size)]


chunked = chunk_array([i * 2 for i in range(10000)], 3)
print("Non-Generator Memory Size:", sys.getsizeof(chunked))
# print(chunked)


def chunked_generator(array, chunk_size):
    """Produces a memory-efficient chunked array"""
    return (array[i:i+chunk_size] for i in range(0, len(array), chunk_size))


generator_chunks = chunked_generator([i * 2 for i in range(10000)], 3)
print("Generator Memory Size:", sys.getsizeof(generator_chunks))
# print(list(generator_chunks))


def chunk_array_into_n(array, n):
    size = roundUp(len(array) / float(n))
    return [array[i:i+size] for i in range(0, len(array), size)]


N_chunks = chunk_array_into_n([1, 2, 3, 4, 5, 6, 7], 4)
print(N_chunks)
