from collections import deque
from typing import Dict, Generator

def find(data: Dict, tag: str) -> Generator:
    """Returns matched values for a selected key recursively"""
    try:
        if isinstance(data, list):
            for value in data:
                for instance in find(value, tag):
                    yield instance
        elif isinstance(data, dict):
            if tag in data:
                yield data[tag]
            for value in data.values():
                for instance in find(value, tag):
                    yield instance
    except TypeError:
        return {}
    except AttributeError:
        return {}

complex = {
    "first": {
        "nested_first": 1,
        "nested_second": 2,
        "nested_complex": {
            "a": "key is a",
            "b": "key is b",
            "further_complex": {
                "level_three": "Made it"
            }
        }
    },
    "second": {
        "one": "woah",
        "two": "who?",
        "nested": {
            "a": "this is in 'first'"
        }
    }
}

print("Find tag of further_complex", list(find(complex, "further_complex"))) # [{'level_three': 'Made it'}]
print("Find tag of copied tag of a", list(find(complex, "a"))) # ['key is a', "this is in 'first"]

def find_tag_track_steps(data: Dict, tag: str) -> Generator:
    stack = deque(
        [
            (data, [])
        ]
    )
    while stack:
        current, steps = stack.pop()
        for key, value in current.items():
            if key == tag:
                yield steps + [key]
            if isinstance(value, dict):
                stack.append(
                    (value, steps + [key])
                )

my_dict = {
    "key1": {
        "key2": {
            "key3": "valuable",
            "key4": "nice"
        }
    }
}

for steps in find_tag_track_steps(complex, "further_complex"):
    print("Found value with steps:", *steps)