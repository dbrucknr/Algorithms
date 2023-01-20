from typing import List, Dict, Callable
from math import floor

def groupBy(array: List, fn: Callable) -> Dict:
    return {
        fn(instance): [
            array[idx] for idx in range(len(array)) if fn(array[idx]) == fn(instance)
        ] 
        for instance in array
    }

print(groupBy([6.1, 4.2, 6.3], floor)) # {4: [4.2], 6: [6.1, 6.3]}
print(groupBy(['one', 'two', 'three'], len)) # {3: ['one', 'two'], 5: ['three']}
print(groupBy(['one', 'two', 'three', 'seven'], len)) # {3: ['one', 'two'], 5: ['three', 'seven']}
