from enum import Enum
from abc import abstractmethod

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

# low level module:
class Person:
    def __init__(self, name) -> None:
        self.name = name

# The fix - interface
class RelationshipBrowser:
    @abstractmethod
    def find_all_chidren_of(self, name):
        pass

# low level module:
class Relationships(RelationshipBrowser):
    def __init__(self) -> None:
        self.relations = [] # Could change

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

# We are going to break the dependency inversion principle:
# high level module:
class Research:
    """This should not depend on lower-level modules/classes"""
    # def __init__(self, relationships) -> None:
    #     relations = relationships.relations
        # Big Problem: this Research module depends on the Relationships module have a list
        # (storage implementation) to iterate through...breaks the dependency inversion principle
        # for r in relations:
        #     if r[0].name == "John" and r[1] == Relationship.PARENT:
        #         print(f"John has a child called {r[2].name}")

        # How do we fix this?
        # - We could add an interface for the low level module (Should not depend on the concrete implementation, but an asbtraction)
        # move the search into the low level module

    def __init__(self, browser) -> None:
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p}")



parent = Person("John")
child1 = Person("Chris")
child2 = Person("Mathew")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)