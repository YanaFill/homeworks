# Патерни проектування: Абстрактна фабрика, Компоновщик, Стратегія
# Принципи SOLID: Інтерфейс-реалізація, Залежність від абстракцій, Інверсія залежностей, Однозначність відповідальності, Закритий/відкритий принцип

class ArrayElement:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class NumericArrayElement(ArrayElement):
    def __init__(self, value):
        super().__init__(value)

    def __float__(self):
        return float(self.value)

class Array:
    def __init__(self, elements):
        self.elements = elements

    def is_of_one_type(self):
        first_element_type = type(self.elements[0])
        for element in self.elements:
            if type(element) != first_element_type:
                return False
        return True

    def output_to_json(self, filename):
        with open(filename, "w") as f:
            f.write(json.dumps(self.elements))

    def output_to_txt(self, filename):
        with open(filename, "w") as f:
            for element in self.elements:
                f.write(str(element) + "\n")

    def output_to_console(self):
        for element in self.elements:
            print(element)

    def sort_ascending(self):
        self.elements.sort()

    def sort_descending(self):
        self.elements.sort(reverse=True)

    def add_element_to_beginning(self, element):
        self.elements.insert(0, element)

    def remove_element_from_beginning(self):
        self.elements.pop(0)

    def notify(self, message):
        print(message)

class ArrayFactory:
    def create_array(self, elements):
        if all(isinstance(element, NumericArrayElement) for element in elements):
            return NumericArray(elements)
        else:
            return Array(elements)

class NumericArray(Array):
    def find_elements_count(self, value):
        return sum(element == value for element in self.elements)

    def get_mean(self):
        if len(self.elements) > 0:
            return sum(element for element in self.elements) / len(self.elements)
        else:
            return None


# Створення масиву з рядків
array_of_strings = Array(["Hello", "World", "!"])

# Перевірка того, чи всі елементи масиву є рядками
# Alternative code
import itertools

if all(isinstance(element, str) for element in itertools.chain(array_of_strings)):
    print("Усі елементи масиву є рядками.")
else:
    print("У масиві є елементи, які не є рядками.")



# Створення масиву з числових елементів
array_of_numbers = Array([1, 2, 3, 4, 5])

# Виведення масиву у json-файл
array_of_numbers.output_to_json("array.json")

# Виведення масиву у txt-файл
array_of_numbers.output_to_txt("array.txt")

# Виведення масиву на екран
array_of_numbers.output_to_console()

# Сортування масиву за зростанням
array_of_numbers.sort_ascending()

# Сортування масиву за спаданням
array_of_numbers.sort_descending()

# Додавання елемента до початку масиву
array_of_numbers.add_element_to_beginning(0)

# Видалення елемента з початку масиву
array_of_numbers.remove_element_from_beginning()

# Знаходження кількості елементів у масиві, які дорівнюють 3
count = array_of_numbers.find_elements_count(3)
print(f"Кількість елементів у масиві, які дорівнюють 3: {count}")

# Знаходження середнього значення у масиві
mean = array_of_numbers.get_mean()
print(f"Середнє значення у масиві: {mean}")
