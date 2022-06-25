from doubly_linked_list_node import Doubly_Linked_List_Node


class Double_Linked_List:
    def __init__(self) -> None:
        self.head = None

    def __repr__(self) -> str:
        return "DLL object: head={}".format(self.head)

    def is_empty(self):
        """Returns true if DLL instance is empty"""
        return self.head is None

    def size(self):
        """
            Traverse Linked-List and returns value for # of nodes in the Linked-List
            * O(N) Time Complexity
                * Each node in Linked-List must be visited.
        """
        total = 0
        if self.head is None:
            return total

        current = self.head
        # While there are still Nodes left to count
        while current is not None:
            total += 1
            current = current.get_next()
        return total

    def search(self, data):
        """
            Traverses Linked List. Returns True if search param "data" is present in one of the nodes.
            * O(N) Time Complexity
        """
        if self.head is None:
            return "Linked List is empty. No nodes to search."

        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            current = current.get_next()
        return False

    def add_front(self, new_data):
        """Add Node to the front of the linked list"""
        temp_node = Doubly_Linked_List_Node(new_data)
        temp_node.set_next(self.head)

        if self.head is not None:
            self.head.set_previous(temp_node)

        self.head = temp_node

    def remove(self, data):
        """
            Remove first occurence of a Node that contains the data param as its self.data
            variable. Returns nothing.
            * O(N) Time Complexity
                * Worst case: Data is last index in Linked List. (Must visit every node in Linked List collection.)
        """
        if self.head is None:
            return "Linked List is empty. No nodes to remove."
        current = self.head
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "A node with specified data value is not present."
                else:
                    current = current.get_next()
        if current.previous is None:
            self.head = current.get_next()
        else:
            current.previous.set_next(current.get_next())
            current.next.set_previous(current.get_previous())


dll = Double_Linked_List()
print(dll.size())
print(dll.remove("Nothing"))

dll.add_front(1)
print(dll.head)
print(dll.size())


print(dll.head.previous)
print(dll.head.next)

dll.add_front(2)
print(dll.head)
print(dll.size())

print(dll.head.previous)
print(dll.head.next)

print(dll.head.next.next)
dll.add_front(3)
print(dll.remove("Nothing"))

dll.remove(2)
print(dll.size())
print(dll.head)
print(dll.head.next)
print(dll.head.next.previous)
