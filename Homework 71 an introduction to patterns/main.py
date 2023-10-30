class Shape:
    def fill_color(self, color):
        pass
    def draw(self):
        pass
    def erase(self):
        pass


class Circle(Shape):
    def __init__(self, radius, color):
        self.color = color
        self.radius = radius

    def draw(self):
        print("Малюємо круг радіусом: ", self.radius)

    def fill_color(self, color):
        self.color = color

    def erase(self):
        print("Витираємо круг")


class Rectangle(Shape):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        print("Малюємо пряиокутник із шириною: ", self.width, "та довжиною: ", self.height)

    def erase(self):
        print("Витираємо прямокутник")


class Creator:
    def createProduct(self):
        pass

    def render(self):
        figure = self.createProduct()
        figure.draw()
        figure.fill_color(self.color)

class CircleCreator(Creator):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def createProduct(self):
        return Circle(self.radius, self.color)


class RectangleCreator(Creator):
    def __init__(self, width, height, color):
        self.width = width
        self.heigth = height
        self.color = color


    def createProduct(self):
        return Rectangle(self.width, self.heigth, self.color)

circle_creator = CircleCreator(10, "red")
rectangle_creator = RectangleCreator(20, 30, "green")

circle = circle_creator.createProduct()
rectangle = rectangle_creator.createProduct()

circle.draw()
rectangle.draw()

circle.fill_color("blue")
rectangle.fill_color("yellow")

circle.erase()
rectangle.erase()
