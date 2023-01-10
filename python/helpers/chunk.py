from itertools import zip_longest

def group(iterable, group_size, fill=None):
    args = [iter(iterable)] * group_size
    return zip_longest(*args, fillvalue=fill)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

chunks = group(data, 5)
print(list(chunks))


