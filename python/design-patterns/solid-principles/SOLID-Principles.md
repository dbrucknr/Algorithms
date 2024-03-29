5 Principles

Single Responsibility (Separation of Concerns)
- a class has one task / responsibility and should not take on more than that.

Open-Closed
- open for extension, closed for modification
- The Open-Closed Principle suggests that when you add new functionality, you add it via extension not via modification.

Liskov Substitution
- if you have some interface that takes some sort of base class you should be able
to stick a derived class in there and everything should work.
- Substitute a base type for a subtype.

Interface Segregation
- avoid too many methods, elements, or variables in a single interface.
- By reducing the scale of an interface, code becomes more modular, and can
be built as needed across many contexts.

Dependency Inversion
- Does not relate to dependency injection
- High level modules / classes should not depend on low level modules / classes. Instead,
they should depend on abstractions. You want to depend on interfaces rather than concrete
implementations because you can swap one for the other