class NameLengthError(ValueError):
    pass

def check_name(name):
    if len(name) < 10:
        raise NameLengthError("Ім'я занадто коротке! Потрібно мінімум 10 символів.")




print("--- Тест 1: Вводимо 'Iryna'")
try:
    check_name("Alex")
except NameLengthError as e:

    print(f"Помилка: {e}")

print("\n--- Тест 2: Вводимо 'Mazurova_Iryna2005'")
try:
    check_name("Anastasiya_2025")
    print("Результат: Ім'я прийнято.")
except NameLengthError as e:
    print(f"Помилка: {e}")