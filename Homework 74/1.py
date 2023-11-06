class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

class Category:
    def __init__(self, name):
        self.name = name
        self.subcategories = []
        self.products = []

    def add_subcategory(self, subcategory):
        self.subcategories.append(subcategory)

    def remove_subcategory(self, subcategory):
        self.subcategories.remove(subcategory)

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product.get_price()
        for subcategory in self.subcategories:
            total_price += subcategory.get_total_price()
        return total_price

class Store:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def remove_category(self, category):
        self.categories.remove(category)

    def get_total_price(self):
        total_price = 0
        for category in self.categories:
            total_price += category.get_total_price()
        return total_price


category_1 = Category("Електроніка")
category_2 = Category("Бытовая техника")
category_3 = Category("Мобильные телефоны")


product_1 = Product("Смартфон iPhone 14", 30000)
product_2 = Product("Ноутбук MacBook Pro", 50000)
product_3 = Product("Пылесос Dyson V15", 20000)


category_3.add_product(product_1)
category_2.add_product(product_2)
category_2.add_product(product_3)


store = Store()
store.add_category(category_1)
store.add_category(category_2)
store.add_category(category_3)


print(store.get_total_price())
