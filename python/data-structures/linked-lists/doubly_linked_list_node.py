class Doubly_Linked_List_Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self) -> str:
        return "DLL object: data={}".format(self.data)

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

    def get_previous(self):
        """Return instance path to previous Node (pointer)"""
        return self.previous

    def set_previous(self, new_previous):
        """Mutate instance previous property"""
        self.previous = new_previous


# first = Doubly_Linked_List_Node("first")
# second = Doubly_Linked_List_Node("second")
# third = Doubly_Linked_List_Node("third")

# first.set_next(second)

# second.set_previous(first)
# second.set_next(third)

# third.set_previous(second)

# print("First next:", first.get_next())
# print("Second next:", second.get_next())

# print("Second previous:", second.get_previous())
# print("Third previous:", third.get_previous())
