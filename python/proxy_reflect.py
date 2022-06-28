from helpers.chunkArray import chunked_generator


class Reactive:
    """
        Enables responsive functions to be called when data is accessed, or updated.
        Currently only printing values
    """

    def __init__(self) -> None:
        self._total_changes = 0

    def _track(self, target, prop) -> None:
        print("track - Data get:", target, prop)

    def _watch(self, target, key, value) -> None:
        print("State is being changed: (old values)",
              target, "\n Key:", key, "\n new value:", value)

    def _trigger(self, target, key, value) -> None:
        self._total_changes += 1
        print("State has been changed, Total changes: {}".format(self._total_changes))


class Reflect(Reactive):
    def __init__(self) -> None:
        super(Reflect, self).__init__()

    def _get(self, target, key):
        self._track(self._target, key)
        return target[key]

    def _set(self, target, key, value):
        self._watch(self._target, key, value)
        if (self._target[key] != value):
            self._trigger(self._target, key, value)
        target[key] = value

    def method(self, class_instance):
        def decorator(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            setattr(class_instance, func.__name__, wrapper)
            return func
        return decorator


class Proxy(Reflect):
    """
        Enables ability to intercept and dynamically redefine 
        fundamental operations for a target variable.
    """

    def __init__(self, target, handler=None):
        super(Proxy, self).__init__()
        self._target = target
        self._handler = handler


data = {
    "array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}

handler = {
    "chunk": chunked_generator,
    "yield": lambda func: list(func)
}

proxy = Proxy(data, handler)
print("Proxy Handler:", proxy._handler)
print("Proxy Target", proxy._target)

property = proxy._handler["chunk"](data["array"], 3)
# print(list(property))
print("Yield From:", proxy._handler["yield"](property))


@proxy.method(proxy)
def example():
    print("Dynamically added to Proxy")


proxy.example()


@proxy.method(proxy)
def some(self, array, callback):
    return any(callback(i) for i in self._target[array])


test = proxy.some(proxy, "array", lambda x: x == 1)
print(test)

proxy._get(data, "array")
proxy._set(data, "array", [0])
print(proxy._total_changes)
# @proxy.method(proxy)
# def every(array, callback):
#     return all(callback(i) for i in array)
