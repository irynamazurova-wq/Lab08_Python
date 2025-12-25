from shop import Shop, Discount

print("--- Пункт A: Створення екземпляру")
store = Shop("Rozetka", "Інтернет-магазин")
print(f"Ім'я магазину: {store.shop_name}")
print(f"Тип магазину: {store.store_type}")
store.describe_shop()
store.open_shop()

print("\n--- Пункт B: Три різні магазини")
store1 = Shop("Nike", "Спортивний одяг")
store2 = Shop("BookUA", "Книжки")
store3 = Shop("Apple Store", "Електроніка")

store1.describe_shop()
store2.describe_shop()
store3.describe_shop()

print("\n--- Пункт C: Робота з атрибутом number_of_units")
print(f"Початкове значення units: {store.number_of_units}")
store.number_of_units = 10
print(f"Змінене значення units: {store.number_of_units}")

print("\n--- Пункт D: Методи зміни кількості")
store.set_number_of_units(500)
store.increment_number_of_units(25)

print("\n--- Пункт E: Знижки (спадкування)")
store_discount = Discount("Comfy", "Електроніка")
store_discount.discount_products = ["Смартфони", "Ноутбуки", "Планшети"]
store_discount.get_discounts_products()

print("\n--- Пункт F: Перевірка імпорту (all_store) ---")
all_store = Shop("TestImport", "Test")
all_store.open_shop()