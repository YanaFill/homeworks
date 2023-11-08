class HotDog:
    def __init__(self, name, ingredients, toppings, price):
        self.name = name
        self.ingredients = ingredients
        self.toppings = toppings
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.ingredients} + {self.toppings}): {self.price}"


class Order:
    def __init__(self, hotDogs, paymentType):
        self.hotDogs = hotDogs
        self.paymentType = paymentType
        self.total_price = 0

        for hotDog in hotDogs:
            total_ingredient_cost = sum(1 for _ in hotDog.ingredients)
            self.total_price += hotDog.price + total_ingredient_cost

    def __str__(self):
        return f"Замовлення: {self.hotDogs} ({self.total_price})"




class Kiosk:
    def __init__(self, hotDogs, ingredients):
        self.hotDogs = hotDogs
        self.ingredients = ingredients
        self.orders = []

    def getHotDogs(self):
        return self.hotDogs

    def getIngredients(self):
        return self.ingredients

    def createOrder(self):
        order = Order([], "cash")
        while True:
            print("Оберіть рецепт хот-догу:")
            for hotDog in self.hotDogs:
                print(f"{hotDog.name} ({hotDog.price})")

            choice = input("Введіть номер рецепта: ")
            if not choice.isdigit():
                print("Неправильний ввід.")
                continue

            choice = int(choice)
            if choice < 1 or choice > len(self.hotDogs):
                print("Немає такого рецепта.")
                continue

            hotDog = self.hotDogs[choice - 1]

            print("Оберіть інгредієнти:")
            for ingredient in self.ingredients:
                print(f"{ingredient} (1 грн.)")

            ingredients = []
            while True:
                choice = input("Введіть номер інгредієнту (0 - закінчити): ")
                if not choice.isdigit():
                    print("Неправильний ввід.")
                    continue

                choice = int(choice)
                if choice < 0 or choice > len(self.ingredients):
                    print("Немає такого інгредієнту.")
                    continue

                ingredients.append(self.ingredients[choice - 1])

                if choice == 0:
                    break

            order.hotDogs.append(
                HotDog(hotDog.name, hotDog.ingredients + ingredients, [], hotDog.price + len(ingredients)))

            print("Чи хочете замовити ще один хот-дог? (Y/N): ")
            choice = input()
            if choice != "Y":
                break

        return order

    def addOrder(self, order):
        self.orders.append(order)

    def getOrders(self):
        return self.orders

    def getProfit(self):
        profit = 0
        for order in self.orders:
            profit += order.total_price
        return profit

    def getNumberOfOrders(self):
        return len(self.orders)

    def getNumberOfHotDogs(self):
        numberOfHotDogs = 0
        for order in self.orders:
            numberOfHotDogs += len(order.hotDogs)
        return numberOfHotDogs


if __name__ == "__main__":

    hotDogs = [
        HotDog("Класичний", ["булка", "сосиска", "кетчуп", "гірчиця"], [], 50),
        HotDog("Чізбургер", ["булка", "сосиска", "сир", "кетчуп", "гірчиця"], [], 60),
        HotDog("Мексиканський", ["булка", "сосиска", "кетчуп", "гірчиця", "томат", "огірок", "перець"], [], 70),
    ]
    ingredients = ["кетчуп", "гірчиця", "майонез", "томат", "огірок", "перець", "халапеньйо"]

    kiosk = Kiosk(hotDogs, ingredients)

    while True:
        order = kiosk.createOrder()
        kiosk.addOrder(order)

        print("Замовлення:")
        for hotDog in order.hotDogs:
            print(hotDog)

        print("Вартість замовлення:", order.total_price)

        break
    print("Загалом продано", kiosk.getNumberOfHotDogs(), "хот-догів на суму", kiosk.getProfit(), "грн.")

