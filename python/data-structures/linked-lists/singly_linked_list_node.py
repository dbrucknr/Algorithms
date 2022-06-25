class Singly_Linked_List_Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return "SLL object: data={}".format(self.data)

    def get_data(self):
        """Access instance data property"""
        return self.data

    def set_data(self, new_data):
        """Mutate instance data property"""
        self.data = new_data

    def get_next(self):
        """Return instance path to next Node (pointer)"""
        return self.next

    def set_next(self, new_next):
        """Mutate instance next property"""
        self.next = new_next


# node = Singly_Linked_List_Node("Example")
# print(node.get_data())

# node.set_data(81)
# print(node.get_data())

# another_node = Singly_Linked_List_Node("Another")

# node.set_next(another_node)
# print(node.get_next())
