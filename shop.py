class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"\nМагазин: '{self.shop_name}'")
        print(f"Тип: {self.store_type}")

    def open_shop(self):
        print(f"Онлайн-магазин '{self.shop_name}' відкритий.")

    def set_number_of_units(self, number):
        self.number_of_units = number
        print(f"Встановлено кількість видів товару: {self.number_of_units}")

    def increment_number_of_units(self, number):
        self.number_of_units += number
        print(f"Кількість видів збільшено на {number}. Разом: {self.number_of_units}")


class Discount(Shop):
    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = []

    def get_discounts_products(self):
        print(f"\nТовари зі знижкою в '{self.shop_name}': {self.discount_products}")