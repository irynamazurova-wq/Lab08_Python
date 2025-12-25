class Buffer:
    def __init__(self):
        # Створюємо пустий список для накопичення чисел
        self.storage = []

    def add(self, *a):

        self.storage.extend(a)


        while len(self.storage) >= 5:
            part = self.storage[:5]


            part_sum = sum(part)

            print(f"Сума обчислення п'ятірки: {part}, Сума: {part_sum}")

            self.storage = self.storage[5:]

    def get_current_part(self):

        return self.storage


buf = Buffer()

print("Етап 1: Додаємо 1, 2, 3")
buf.add(1, 2, 3)
print(f"Залишок у буфері: {buf.get_current_part()}")

print("Етап 2: Додаємо 4, 5, 6")
# Тут список стане [1, 2, 3, 4, 5, 6].
# Програма має забрати [1, 2, 3, 4, 5], порахувати суму (15) і залишити [6].
buf.add(4, 5, 6)
print(f"Залишок у буфері: {buf.get_current_part()}")

print("Етап 3: Додаємо 7, 8, 9, 10")
# Було [6]. Додаємо 7,8,9,10. Стане [6, 7, 8, 9, 10].
# Сума: 40. Залишок: [].
buf.add(7, 8, 9, 10)
print(f"Залишок у буфері: {buf.get_current_part()}")

print("Етап 4: Додаємо багато чисел (15 штук по 1)")
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(f"Залишок у буфері: {buf.get_current_part()}")