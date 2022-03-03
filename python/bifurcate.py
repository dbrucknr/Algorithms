
def bifurcate(array, filterRef):
    result = []
    discarded = []
    for index, element in enumerate(array):
        if filterRef[index]:
            result.append(element)
        else:
            discarded.append(element)
    return [result, discarded]

print(bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])) # [['beep', 'boop', 'bar'], ['foo']]

def bifurcateWithoutDiscarded(array, filterRef):
    return [element for index, element in enumerate(array) if filterRef[index]]

print(bifurcateWithoutDiscarded(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])) # ['beep', 'boop', 'bar']

def bifurcateBy(array, function):
    result = []
    discarded = []
    for element in array:
        if function(element):
            result.append(element)
        else:
            discarded.append(element)
    return [result, discarded]

print(bifurcateBy(['beep', 'boop', 'foo', 'bar'], lambda x: x.startswith('b')))