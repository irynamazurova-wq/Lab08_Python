from user import User
from admin_privileges import Admin

print("--- Пункт A: Створення користувачів")
user1 = User("Ivan", "Sobko", "ivan_p", "ivansobko@gmail.com")
user2 = User("Oksana", "Boyko", "oksana_b", "oksanaB@gmail.com")

user1.describe_user()
user1.greeting_user()

user2.describe_user()
user2.greeting_user()


print("\n--- Пункт B: Login Attempts ")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Перевірка значення: {user1.login_attempts}")

user1.reset_login_attempts()
print(f"Перевірка після скидання: {user1.login_attempts}")

print("\n--- Пункт C, D, E: Адміністратор і Привілеї ---")

my_admin = Admin("Dmytro", "Adminov", "super_admin", "admin@site.com")
my_admin.describe_user()

my_admin.privileges.show_privileges()