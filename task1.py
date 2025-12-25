class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Покладено на рахунок: {amount}")
        else:
            print("Сума має бути більше 0")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Знято з рахунку: {amount}")
        else:
            print("Недостатньо коштів або помилка суми")

    def check_balance(self):
        print(f"Поточний баланс: {self.__balance}")

#перевірка
account = Bank(100)
account.deposit(50)
account.withdraw(30)
account.check_balance()