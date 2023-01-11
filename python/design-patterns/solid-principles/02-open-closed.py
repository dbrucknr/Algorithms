from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size) -> None:
        self.name = name
        self.color = color
        self.size = size

# Imagine we need to filter the product by a color...
# The Open-Closed Principle
# suggests that when you add new functionality, you add it via extension
# not via modification - when we modify ProductFilter to have a new function 
# 'filter by size' we break the principle
class ProductFilter:
    def filter_by_color(self, products, color):
        for product in products:
            if product.color == color:
                yield product

    # Later, someone asks if we can add a size filter
    def filter_by_size(self, products, size) -> Product:
        for product in products:
            if product.size == size:
                yield product

    # This could theoretically go on forever...not scalable
    def filter_by_size_and_color(self, products, size, color):
        for product in products:
            if product.color == color and product.size == size:
                yield product

    # in addition to breaking the open-closed principle, we are also
    # causing a state space explosion - filter by size or color, the criteria
    # can continue to grow (combinations of attributes could grow)

# Specification Pattern as a scalable remedy. These (somewhat cryptic) set of classes
# allow you flexibility if you choose to change / add / modify functionality. You can simply inherit
# from the "base class" and over-write the functionality
class Specification:
    """
        Determines whether or not a particular item
        satisfies a particular criteria
    """
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        """Used to construct a combination of specs to be filtered"""
        return AndSpecification(self, other)

class Filter:
    def filter(self, items, spec):
        pass

class ColorSpecification(Specification):
    def __init__(self, color) -> None:
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size) -> None:
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    """Combination of Specs to be Filtered"""
    def __init__(self, *args) -> None:
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))

class BetterFilter(Filter):

    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    # Old Approach:
    pf = ProductFilter()
    print('Green Products (old):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f"- {p.name} is green")

    print("Large Products (old)")
    for p in pf.filter_by_size(products, Size.LARGE):
        print(f"- {p.name} is large")

    ######################################################################

    # New Approach (Open-Close Principle):
    # Note the API is slightly more complicated
    bf = BetterFilter()
    print("Green Products (new):")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f"- {p.name} is green")

    print("Large Products (new)")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f"- {p.name} is large")

    print("Large Blue Items")
    # large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    large_blue = large & ColorSpecification(Color.BLUE) #requires __and__ to be added to Specification class
    for p in bf.filter(products, large_blue):
        print(f"- {p.name} is large and blue")


    