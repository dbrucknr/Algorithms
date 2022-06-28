
class Deque:
    """
        Deque = Double Ended Queue
            * An abstract data type that resembles both a stack and a queue.
            * Items in the deque can be added to and removed from both the front and back.
            * FIFO and LIFO models can be used here (at the same time).
            * Can only access from either end of the list.
    """

    def __init__(self) -> None:
        self._items = []

    def add_front(self, item):
        """
            Takes item param and inserts it at the 0th index of the list representing the deque.
            * Runtime: O(N) Linear - all (previous) items must shift their index.
        """
        self._items.insert(0, item)

    def add_rear(self, item):
        """
            Takes item param and appends it to the list representing the deque.
            * Runtime: O(1) Constant.
        """
        self._items.append(item)

    def remove_front(self):
        """
            Removes and returns the item at the front of the deque.
            * Runtime: O(N) Linear - all (previous) items must shift their index.
        """
        return self._items.pop(0) if self._items else None

    def remove_rear(self):
        """
            Removes and returns the last item in the deque.
            * Runtime: O(1) Constant.
        """
        return self._items.pop() if self._items else None

    def peek_front(self):
        """
            Returns the value found at the front of the deque. 
            * Runtime: O(1) Constant.
        """
        return self._items[0] if self._items else None

    def peek_rear(self):
        """
            Returns the value found at the rear of the deque. 
            * Runtime: O(1) Constant.
        """
        return self._items[-1] if self._items else None

    def size(self):
        """
            Returns length of the list that represents the deque.
            * Runtime: O(1) Constant time.
        """
        return len(self._items)

    def is_empty(self):
        """
            Returns boolean describing whether or not the deque contains values.
            * Runtime: O(1) Constant time.
        """
        return self._items == []


####
# example = Deque()
# print(example._items)
# print(example.is_empty())
# print(example.size())
# example.remove_front()  # Error check
# example.remove_rear()  # Error check

# example.peek_front()  # Error check
# example.peek_rear()  # Error check

# example.add_front("Great Pyrenees")
# example.add_front("German Shepherd")
# print(example._items)
# example.add_rear("Schnauzer")
# print(example._items)

# print(example.peek_front())
# print(example.peek_rear())

# print(example.is_empty())
# print(example.size())

# example.remove_front()
# print(example._items)
# example.remove_rear()
# print(example._items)
