class Task:
    def __init__(self, id, name, priority):
        self.id = id
        self.name = name
        self.priority = priority


class TaskNode:
    def __init__(self, task):
        self.task = task
        self.priority = task.priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.count_tasks = 0
        self.size = 0

    def enqueue(self, task):
        new_node = TaskNode(task)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                if current.next.priority < new_node.priority:
                    current = current.next
                else:
                    break
            if current.task.id == task.id:
                current.next = new_node
            else:
                new_node.next = current.next
                current.next = new_node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            raise ValueError("Queue is empty")

        # Знаходимо задачу з найвищим пріоритетом.
        highest_priority_task = self.head
        current = self.head
        while current.next is not None:
            if current.next.priority > highest_priority_task.priority:
                highest_priority_task = current.next
            current = current.next

        # Якщо найвищим пріоритетом мають кілька задач, то виводимо ту, яка була додана раніше.
        task = highest_priority_task
        if highest_priority_task.priority == self.head.priority:
            task = self.head

        # Видаляємо задачу з черги.
        if task is self.head:
            self.head = task.next
        else:
            current = self.head
            while current.next is not task:
                current = current.next
            current.next = task.next

        self.size -= 1
        self.count_tasks += 1

        return task

    def is_empty(self):
        return self.head is None

    def queue_size(self):
        return self.size

    def completed_tasks(self):
        return self.count_tasks


queue = PriorityQueue()

# список завдань
tasks = [
    Task(1, "Підготувати звіт про продажі", 1),
    Task(2, "Відправити заказ клієнту A", 1),
    Task(3, "Сформувати презентацію для команди.", 3),
    Task(4, "Зателефонувати постачальнику щодо поставки товару.", 2),
    Task(5, "Відправити заказ клієнту B", 1),
    Task(6, "Замовити нове обладнання для офісу.", 2),
]

# додаємо завдання
for task in tasks:
    queue.enqueue(task)

# виводимо виконані завдання по пріоритету
print("Завдання, які будуть виконані: ")
current = queue.head
while current is not None:
    print(current.task.id, current.task.name, current.task.priority)
    current = current.next

queue.dequeue()
queue.dequeue()
queue.dequeue()

print("\nЗавдання, які будуть виконані: ")
current = queue.head
while current is not None:
    print(current.task.id, current.task.name, current.task.priority)
    current = current.next

print(f"\nРозмір черги: {queue.queue_size()}")
print(f"Виконано завдань: {queue.completed_tasks()}")
