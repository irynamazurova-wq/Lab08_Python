import random

class Coin:
    def __init__(self):
        self.__sideup = 'heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'heads'
        else:
            self.__sideup = 'tails'

    def get_sideup(self):
        return self.__sideup

my_coin = Coin()


n = 10
print(f"Підкидаємо монету {n} разів:")

for i in range(n):
    my_coin.toss()
    print(f"Кидок {i+1}: {my_coin.get_sideup()}")