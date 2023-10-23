class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"

class Stack:
    def __init__(self, max_size=-1):
        self.head = None
        self.max_size = max_size
        self.size = 0  # Доданий атрибут для збереження розміру стеку

    def push(self, data):
        if self.max_size == 0:
            raise Exception("Stack is overflow")
        node = Node(data)
        node.next = self.head
        self.head = node
        self.max_size -= 1
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        value = self.head.data
        self.head = self.head.next
        self.max_size += 1
        self.size -= 1
        return value

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return self.max_size == 0

    def clear(self):
        self.head = None
        self.max_size = -1
        self.size = 0  # Оновлення розміру при повному очищенні стеку

    def iter(self):
        current = self.head
        while current:
            if current.next is None:
                print(current, end=" ")
            else:
                print(current, end=' ')
            current = current.next
        print()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.head.data

def menu():
    max_size = int(input("Введіть максимальний розмір стеку (або -1 для нефіксованого розміру): "))
    stack = Stack(max_size)
    while True:
        print("\t\tМеню:\n"
              "1. Додати рядок у стек\n"
              "2. Виштовхнути рядок із стеку\n"
              "3. Перевірити, чи порожній стек\n"
              "4. Перевірити, чи повний стек\n"
              "5. Розмір стеку\n"
              "6. Повністю очистити стек\n"
              "7. Отримати значення верхнього рядка без виштовхування\n"
              "0. Вийти\n")

        choice = int(input("Виберіть операцію: "))

        if choice == 1:
            data = int(input("Введіть рядок: "))
            stack.push(data)
            stack.iter()
        elif choice == 2:
            try:
                data = stack.pop()
                print(f"Виштовхнуто: {data}")
                stack.iter()
            except Exception as e:
                print(str(e))
        elif choice == 3:
            if stack.is_empty():
                print("Стек порожній")
            else:
                print("Стек не порожній")
        elif choice == 4:
            if stack.is_full():
                print("Стек повний")
            else:
                print("Стек не повний")
        elif choice == 5:
            print(f"Розмір стеку: {stack.size}")
        elif choice == 6:
            stack.clear()
            print("Стек повністю очищено")
        elif choice == 7:
            try:
                data = stack.peek()
                print(f"Значення верхнього рядка: {data}")
            except Exception as e:
                print(str(e))
        elif choice == 0:
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    menu()
