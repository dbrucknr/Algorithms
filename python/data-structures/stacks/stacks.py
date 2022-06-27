class Stack:
    def __init__(self) -> None:
        self._items = []

    def push(self, item):
        """
            Accepts item as a param and appends it to the end of the list.
            Returns None.
            * Runtime: O(1) Constant time.
        """
        self._items.append(item)

    def pop(self):
        """
            Removes and returns the last item from the list (top item in stack).
            * Runtime: O(1) Constant time.
        """
        return self._items.pop() if self._items else None

    def peek(self):
        """
            Returns last item in list (top item in stack).
            * Runtime: O(1) Constant time.
        """
        return self._items[-1] if self._items else None

    def size(self):
        """
            Returns length of the list that represents the stack.
            * Runtime: O(1) Constant time.
        """
        return len(self._items)

    def is_empty(self):
        """
            Returns boolean describing whether or not the stack contains values.
            * Runtime: O(1) Constant time.
        """
        return self._items == []


####
# the_stack = Stack()
# the_stack.peek()  # Error check
# the_stack.pop()  # Error check
# print(the_stack.is_empty())
# print(the_stack.size())
# the_stack.push("one")
# the_stack.push("two")
# print(the_stack.peek())
# print(the_stack.size())
# print(the_stack._items)
# the_stack.pop()
# print(the_stack._items)
# print(the_stack.size())
# print(the_stack.is_empty())
