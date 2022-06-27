class Queue:
    """
        First-in, First-out Data Type (FIFO).
        * Consider a waiting line at DMV. The order in which a person joins
            dictates when they will be seen.
        * Or, a printer queue -> documents are printed in the order they are sent.
        * Recursive Data Structure
    """

    def __init__(self) -> None:
        self._items = []

    def enqueue(self, item):
        """
            Inserts item param into the 0th index of the queue's list.
            * Runtime: O(n) Linear time.
        """
        self._items.insert(0, item)

    def dequeue(self):
        """
            Removes and returns the front-most item from the list 
            (first item in queue, last item in the list).
            * Runtime: O(1) Constant time.
        """
        return self._items.pop() if self._items else None

    def peek(self):
        """
            Returns last item in list (front-most item in queue).
            * Runtime: O(1) Constant time.
        """
        return self._items[-1] if self._items else None

    def size(self):
        """
            Returns length of the list that represents the queue.
            * Runtime: O(1) Constant time.
        """
        return len(self._items)

    def is_empty(self):
        """
            Returns boolean describing whether or not the queue contains values.
            * Runtime: O(1) Constant time.
        """
        return self._items == []


#####
# queue = Queue()
# queue.dequeue()  # Error check
# queue.peek()  # Error check
# print(queue.size())
# print(queue.is_empty())
# queue.enqueue("task-1")
# queue.enqueue("task-2")
# print(queue.peek())
# print(queue._items)
# print(queue.size())
# print(queue.is_empty())
# queue.dequeue()
# print(queue._items)
