from singly_linked_list_node import Singly_Linked_List_Node


class Singly_Linked_List():
    def __init__(self) -> None:
        self.head = None

    def __repr__(self) -> str:
        return "SLL object: head={}".format(self.head)

    def is_empty(self):
        """Returns true if SLL instance is empty"""
        return self.head is None

    def add_to_front(self, new_data):
        """Add Node to the front of the linked list"""
        temp_node = Singly_Linked_List_Node(new_data)
        temp_node.set_next(self.head)
        self.head = temp_node

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
        previous = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return "A node with specified data value is not present."
                else:
                    previous = current
                    current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


sll = Singly_Linked_List()
print(sll.is_empty())

node = Singly_Linked_List_Node(1)
print(sll.remove("Non-Exist"))
sll.head = node
print(sll.remove(1))
node = Singly_Linked_List_Node("woah!")
sll.head = node
print("Empty?", sll.is_empty())
print("Head?", sll.head)
print("Size?", sll.size())

sll.add_to_front("test")
print(sll.head)
print("check new head's next value:", sll.head.get_next())
print(sll.size())

print(sll.search("test"))
print(sll.remove("test"))
print(sll.size())
