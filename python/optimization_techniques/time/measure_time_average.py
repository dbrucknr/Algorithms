from timeit import timeit

items = {
    "a": 1,
    "b": 2
}
default = -1


def use_catch(key):
    """Use try / catch to get a key with a default if not found"""
    try:
        return items[key]
    except KeyError:
        return default


def use_get(key):
    """Use dict.get to get a key with a default if not found"""
    return items.get(key, default)


if __name__ == "__main__":
    # Key is in dictionary:
    print("catch", timeit('use_catch("a")', 'from __main__ import use_catch'))
    print("get", timeit('use_get("a")', 'from __main__ import use_get'))

    # Key is missing
    print("catch", timeit('use_catch("x")', 'from __main__ import use_catch'))
    print("get", timeit('use_get("x")', 'from __main__ import use_get'))

    # When key is present, catch is faster
    # when key is missing, get is faster
    # know which outcome is more common in your codebase.
