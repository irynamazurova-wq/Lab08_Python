# Батьківський клас Dog
class Dog:
    # Атрибути класу (спільні для всіх)
    mammal = True  # Ссавець
    nature = None
    breed = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"Кличка: {self.name}")
        print(f"Вік: {self.age}")
        print(f"Порода: {self.breed}")
        print(f"Характер: {self.nature}")

        print(f"Mammal (Ссавець): {self.mammal}")


class GermanShepherd(Dog):
    nature = "Відданий та уважний"
    breed = "Німецька вівчарка"

    def guard_house(self):
        print(f">> {self.name} пильно охороняє територію.")


class Bulldog(Dog):
    nature = "Впертий, але добрий"
    breed = "Англійський бульдог"

    def snore(self):
        print(f">> {self.name} голосно хропе.")


class Poodle(Dog):
    nature = "Активний та розумний"
    breed = "Пудель"

    def perform_trick(self):
        print(f">> {self.name} робить сальто.")


class Pets:
    def __init__(self):
        self.dogs_list = []

    def add_pet(self, dog):
        self.dogs_list.append(dog)

    def show_all_pets(self):
        print("\n--- СПИСОК МОЇХ ДОМАШНІХ ТВАРИН ---")
        for dog in self.dogs_list:
            dog.describe()

            if isinstance(dog, GermanShepherd):
                dog.guard_house()
            elif isinstance(dog, Bulldog):
                dog.snore()
            elif isinstance(dog, Poodle):
                dog.perform_trick()

            print("-" * 30)


dog1 = GermanShepherd("Рекс", 5)
dog2 = Bulldog("Бутч", 3)
dog3 = Poodle("Топаз", 2)

my_pets = Pets()
my_pets.add_pet(dog1)
my_pets.add_pet(dog2)
my_pets.add_pet(dog3)

my_pets.show_all_pets()