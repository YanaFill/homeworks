from abc import ABC, abstractmethod
class IShape(ABC):
    @abstractmethod
    def get_area(self) -> float:
        pass

class Shape(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def info(self):
        pass


class Pizza(Shape):
    def __init__(self, name: str, price: float, shape: IShape):
        super().__init__(name)
        self.price = price
        self.shape = shape

    def get_price(self) -> float:
        return self.price

    def get_shape_class(self) -> str:
        return type(self.shape).__name__

    def cut_pizza(self):
        print(f"Піца {self.name} нарізана")

    def info(self):
        print(f"Піца {self.name} коштує {self.price} і має форму {type(self.shape).__name__}")


class Square(Shape):
    def __init__(self, name: str, side: float):
        super().__init__(name)
        self.side = side

    def info(self):
        print(f"Квадратна піца {self.name} має сторону {self.side}")

    def get_area(self) -> float:
        return self.side * self.side


class Circle(Shape):
    def __init__(self, name: str, radius: float):
        super().__init__(name)
        self.radius = radius

    def info(self):
        print(f"Колоподібна піца {self.name} має радіус {self.radius}")

    def get_area(self) -> float:
        return 3.14 * self.radius * self.radius


circle = Circle("Circle", 5)
square = Square("Square", 9)

print(circle.get_area())
print(square.get_area())

circle.info()
square.info()

# square_pizza = Pizza("Квадратна піца", 100, Square("Квадратна", 10))
# circle_pizza = Pizza("Колоподібна піца", 200, Circle("Колоподібна", 5))
#
# print(square_pizza.get_shape_class())
# print(circle_pizza.get_shape_class())
#
# circle = Circle("Circle", 5)
# square = Square("Square", 9)
# print(circle.info())
# print(square.info())