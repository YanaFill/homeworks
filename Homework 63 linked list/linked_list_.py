class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data}, {self.next.data if self.next else None})"

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def append_to_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def iter(self):
        current = self.head
        while current:
            print(current, end=" ")
            current = current.next
        print()

    def append_at_a_location(self, data, value):
        current = self.head
        while current:
            if current.data == data:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def __contains__(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def delete_first_node(self):
        current = self.head
        if current is None:
            print("No data element to delete")
        else:
            self.head = current.next

    def delete_last_node(self):
        current = prev = self.head
        while current:
            if current.next is None:
                prev.next = None
            prev = current
            current = current.next

    def delete_value(self, data, count_dels):
        current = self.head
        left = None
        dels = 0
        while current:
            if current.data == data:
                if count_dels < dels:
                    if left:
                        left.next = current.next
                    else:
                        self.head = current.next
                    dels += 1
                else:
                    break
            left = current
            current = current.next

    def replace_value(self, old_value, new_vlue, replace_all=False):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_vlue
                if not replace_all:
                    break
            current = current.next

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

lst = LinkedList()
lst.append(4)
lst.append(6)
lst.append(8)
lst.append(10)
lst.append(12)
while True:
    menu = int(input("1| Додати елемент у хвіст списку\n"
                     "2| Додати елемент до списку на початок\n"
                     "3| Вставити новий елемент із деяким значенням безпосередньо після елемента із даними, що є у списку\n"
                     "4| Видалити елемент з хвоста списку\n"
                     "5| Видалити елемент з голови списку\n"
                     "6| Видалити елемент із деяким значенням у списку\n"
                     "7| Замінити значення у списку на нове значення\n"
                     "8| Визначте розмір списку\n"
                     "9| Показати вміст списку\n"
                     "10| Стоп\n"
                     "Введіть номер завдання: "))


    if menu == 1:
        num = int(input("Введіть елемент, який хочете додати у хвіст: "))
        lst.append(num)
        lst.iter()
        print()

    if menu == 2:
        num = int(input("Введіть елемент, який хочете додати на початок: "))
        lst.append_to_start(num)
        lst.iter()

    if menu == 3:
        a = int(input("Введіть елемент, після якого потрібно вставити нове число: "))
        b = int(input("Введіть число: "))
        if a in lst:
            lst.append_at_a_location(a, b)
            lst.iter()

    if menu == 4:
        lst.delete_last_node()
        lst.iter()

    if menu == 5:
        lst.delete_first_node()
        lst.iter()
    if menu == 6:
        n = int(input("Введіть елемент, який хочете видалити: "))
        x = int(input("Введіть кількість видалень:"))
        lst.delete_value(n, x)
        lst.iter()

    if menu == 7:
        val = int(input("Введіть елемент, який хочете замінити: "))
        new_val = int(input("Введіть новий елемент списку: "))
        lst.replace_value(val, new_val)
        lst.iter()

    if menu == 8:
        print(f"Довжина списку: {lst.size()}")

    if menu == 9:
        lst.iter()

    if menu == 10:
        break
