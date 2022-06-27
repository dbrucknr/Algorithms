from stacks import Stack


def balanced_symbols(symbol_string):
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    openers = pairs.keys()
    stack = Stack()
    index = 0

    while index < len(symbol_string):
        symbol = symbol_string[index]
        print("Current symbol", symbol)
        if symbol in openers:
            print("Symbol is an opener")
            stack.push(symbol)
        else:
            # The symbol is a closer
            print("Symbol is a closer")
            # If the stack is already empty, the symbols are unbalanced
            if stack.is_empty():
                return False

            # If items still exist in stack, check for mis-match
            else:
                top = stack.pop()
                if symbol != pairs[top]:
                    return False

        index += 1

        if stack.is_empty():
            return True


print(balanced_symbols('([{}])'))
print(balanced_symbols('([{}]])'))
