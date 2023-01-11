class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, position):
        del self.entries[position]

    def __str__(self) -> str:
        return '\n'.join(self.entries)

    # Begin breaking the Single Responsibility Principle:
    # The Journal object is now responsible for persistence
    # in addition to handling journal entries. Becomes problematic
    # if youy have more classes that need to be saved...
    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


instance = Journal()
instance.add_entry("I laughed at my dog today")
instance.add_entry("I smiled at the sun.")

print(f"Journal entries:\n{instance}")

filename = r"temp/journal.txt"
PersistenceManager.save_to_file(instance, filename)
with open(filename) as handle:
    print(handle.read())