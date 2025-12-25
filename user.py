class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0  # Пункт (b)

    def describe_user(self):
        print(f"\nКористувач: {self.first_name} {self.last_name}")
        print(f"Нікнейм: {self.username} | Email: {self.email}")

    def greeting_user(self):
        print(f"Привіт, {self.first_name}! Раді бачити тебе знову.")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Спроба входу... (Всього спроб: {self.login_attempts})")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Лічильник спроб скинуто до 0.")