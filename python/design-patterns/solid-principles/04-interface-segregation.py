from abc import abstractmethod
class Machine:
    """Base Class"""
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError

class MultiFunctionPrinter(Machine):

    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

# What happens when you want to make an old fashion printer?

class OldFashionPrinter(Machine):

    def print(self, document):
        # ok - old fashion printers do this
        pass

    # What to do about these?
    # - Nothing: not great because someone might infer the methods actually work / do something
    # - Raise an Error: maybe okay for small scripts, but in large apps these will effectively crash the app - why are these here?
    def fax(self, document):
        # not ok - old fashion printers can't do this
        pass

    def scan(self, document):
        # not ok - old fashion printers can't do this
        pass

# The basic idea of Interface Segregation is - instead of having one interface with a bunch of methods in it
# you want to keep things granular. You'll want to split the interface into separate parts that can be implemented
# as needed:

class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class FaxMachine:
    @abstractmethod
    def fax(self, document):
        pass

# Combine them as needed:

class MyPrinter(Printer):
    def print(self, document):
        return print(document)

class PhotoCopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass

# If you really want a Machine-like (class above) interface:
class MultiFunctionDevice(Printer, Scanner, FaxMachine):
    # Instead of just over-writing, decorate the inherited methods:

    @abstractmethod
    def print(self, document):
        raise NotImplementedError

    @abstractmethod
    def fax(self, document):
        raise NotImplementedError

    @abstractmethod
    def scan(self, document):
        raise NotImplementedError

class MultiFunctionMachine(MultiFunctionDevice):

    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError

    ...

# OR:
class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner) -> None:
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        self.scanner.scan(document)