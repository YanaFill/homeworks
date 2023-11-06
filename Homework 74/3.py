class Command:
    def execute(self):
        pass

    def undo(self):
        pass


class Order:
    def __init__(self):
        self.is_placed = False
        self.items = []

    def place_order(self):
        self.is_placed = True
        print("Замовлення розміщено.")

    def cancel_order(self):
        self.is_placed = False
        self.items = []
        print("Замовлення відмінено.")

    def add_item(self, item):
        self.items.append(item)
        print(f"Елемент {item} додано до замовлення.")

    def remove_item(self, item):
        self.items.remove(item)
        print(f"Елемент {item} видалено з замовлення.")


class PlaceOrderCommand(Command):
    def __init__(self, order):
        self.order = order

    def execute(self):
        self.order.place_order()

    def undo(self):
        self.order.cancel_order()


class AddItemCommand(Command):
    def __init__(self, order, item):
        self.order = order
        self.item = item

    def execute(self):
        self.order.add_item(self.item)

    def undo(self):
        self.order.remove_item(self.item)


class RemoveItemCommand(Command):
    def __init__(self, order, item):
        self.order = order
        self.item = item

    def execute(self):
        self.order.remove_item(self.item)

    def undo(self):
        self.order.add_item(self.item)


class CommandController:
    def __init__(self):
        self.commands = []

    def execute_command(self, command):
        command.execute()
        self.commands.append(command)

    def undo_last_command(self):
        if self.commands:
            last_command = self.commands.pop()
            last_command.undo()
        else:
            print("Немає команд для відміни")


# Приклад використання
order = Order()
place_order_command = PlaceOrderCommand(order)
add_item_command = AddItemCommand(order, "Стейк")
remove_item_command = RemoveItemCommand(order, "Стейк")

controller = CommandController()
controller.execute_command(place_order_command)
controller.execute_command(add_item_command)
controller.undo_last_command()
controller.undo_last_command()

