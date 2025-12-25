class Car:
    def __init__(self, make, model, year):
        # Ініціалізація атрибутів
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):

        self.speed += 5

    def brake(self):

        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def get_speed(self):

        return self.speed


my_car = Car("Porsche", "911", 2024)

print(f"Автомобіль: {my_car.make} {my_car.model} ({my_car.year})")
print("-" * 20)

print("Набирає швидкість:")
for i in range(5):
    my_car.accelerate()
    print(f"Поточна швидкість: {my_car.get_speed()}")

print("-" * 20)

print("Гальмує:")
for i in range(5):
    my_car.brake()
    print(f"Поточна швидкість: {my_car.get_speed()}")
