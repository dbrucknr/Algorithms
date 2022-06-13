# O(N) Linear Run time
def reverse_array(array):
    """Reverse given array in linear running time using constant memory"""

    start_index = 0
    end_index = len(array) - 1  # Indices start at 0, -1 to offset

    while end_index > start_index:
        # Swap indices
        array[start_index], array[end_index] = array[end_index], array[start_index]
        start_index += 1
        end_index -= 1

    return array


print(reverse_array([1, 2, 3, 4, 5]))
