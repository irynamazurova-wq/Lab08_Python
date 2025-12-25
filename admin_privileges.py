from user import User

class Privileges:
    def __init__(self):
        self.privileges = [
            "Allowed to add message",
            "Allowed to delete users",
            "Allowed to ban users",
            "Allowed to modify settings"
        ]

    def show_privileges(self):
        print("--- Права адміністратора ---")
        for p in self.privileges:
            print(f"- {p}")

class Admin(User):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges()