# To Avoid breaking the open-closed principle, you can use inheritance with
# the builder design pattern

class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} works as a {self.position}'

    @staticmethod
    def new():
        return PersonBuilder()

class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person

class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self

class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self

if __name__ == '__main__':
    # has access to all dot methods
    pb = PersonBirthDateBuilder()
    ex1 = pb\
        .called('Example')\
        .works_as_a('Builder')\
        .born('1/1/1980')\
        .build()
    print(ex1)

    # Has access to dot methods until PersonJobBuilder
    pj = PersonJobBuilder()
    ex2 = pj\
            .called("Example 2")\
            .works_as_a("Builder with no birth date")\
            .build()
    print(ex2)