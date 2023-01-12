# Explore a complication of the Builder Design Pattern:
# Sometimes we have an object that is so complicated to create,
# you need more than one builder to do it.

# How can we get several builders participating in the process, and have a
# nice interface to do use them?

# Note: This example appears to break the open-closed principle

class Person:
    def __init__(self) -> None:
        print("Creating a person instance")
        # Name
        self.name = None
        # Address
        self.street_address = None
        self.postcode = None
        self.city = None
        # Employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return f"{self.name} has an" + f"address of {self.street_address}, {self.postcode}, {self.city}\n" +\
                    f"Employed at {self.company_name} as a {self.position} earning {self.annual_income}"

class PersonBuilder:
    "Base class"
    def __init__(self, person=None) -> None:
        if person is None:
            self.person = Person()
        else:
            self.person = person

    @property
    def has_name(self):
        return PersonNameBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)
    
    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person

class PersonNameBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)

    def of(self, name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self

# How to use
if __name__ == '__main__':
    person = PersonBuilder()
    derek = person\
                .has_name\
                    .of("Derek")\
                .lives\
                    .at("123 Example Rd")\
                    .in_city("Ann Arbor")\
                    .with_postcode("48103")\
                .works\
                    .at("The University of Michigan")\
                    .as_a("Software Engineer + Lecturer")\
                    .earning(123000)\
                .build()
    print(derek)

    placeholder = PersonBuilder().build()
    print(placeholder)