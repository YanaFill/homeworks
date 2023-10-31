from abc import ABC, abstractmethod
class Computer:
    def __init__(self):
        self.processor = None
        self.memory = None
        self.storage = None
        self.graphics_card = None
        self.operating_system = None

    def __str__(self):
        return f"{self.processor}, {self.memory}, {self.storage}, {self.graphics_card}, {self.operating_system}"


class Builder(ABC):

    @abstractmethod
    def add_processor(self, value):
        pass

    @abstractmethod
    def add_memory(self, value):
        pass

    @abstractmethod
    def add_storage(self, value):
        pass

    @abstractmethod
    def add_graphics_card(self, value):
        pass

    @abstractmethod
    def add_operating_system(self, value):
        pass


class ComputerBuilder(Builder):
    def __init__(self):
        self.computer = Computer()

    def get_computer(self) -> Computer:
        comp = self.computer
        self.computer = Computer()
        return comp

    def add_processor(self, value):
        self.computer.processor = value

    def add_memory(self, value):
        self.computer.memory = value

    def add_storage(self, value):
        self.computer.storage = value

    def add_graphics_card(self, value):
        self.computer.graphics_card = value

    def add_operating_system(self, value):
        self.computer.operating_system = value

class Director:
    def __init__(self, builder: ComputerBuilder) -> None:
        self.builder = builder

    def build_minimal_computer(self, specs: dict) -> None:
        self.builder.add_processor(specs['processor'])
        self.builder.add_memory(specs['memory'])
        self.builder.add_storage(specs['storage'])
        self.builder.add_graphics_card(specs['graphics_card'])

    def build_full_computer(self, specs: dict) -> None:
        self.builder.add_processor(specs['processor'])
        self.builder.add_memory(specs['memory'])
        self.builder.add_storage(specs['storage'])
        self.builder.add_graphics_card(specs['graphics_card'])
        self.builder.add_operating_system(specs['operating_system'])


specs = {
 'processor': 'Intel Core i5',
 'memory': '8GB',
 'storage': '512GB SSD',
 'graphics_card': 'Integrated',
 'operating_system': 'Windows 11'
}

specs2 = {
 'processor': 'Intel Core i5',
 'memory': '8GB',
 'storage': '512GB SSD',
 'graphics_card': 'Integrated'
}

builder = ComputerBuilder()
director = Director(builder)
director.build_minimal_computer(specs2)
computer_minimal = builder.get_computer()
print(computer_minimal)
print()
builder = ComputerBuilder()
director = Director(builder)
director.build_full_computer(specs)
computer_full = builder.get_computer()
print(computer_full)