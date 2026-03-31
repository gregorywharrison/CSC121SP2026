class User:
    def __init__(self, first_name, last_name, username, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.location = location
        self.occupation = occupation
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nUser Profile: {self.username}")
        print(f"  Full Name: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

new_user = User('Gregory', 'Harrison', 'gregory_h', 'Asheville', 'Developer')

new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()

print(f"Login attempts: {new_user.login_attempts}")

new_user.reset_login_attempts()
print(f"Login attempts after reset: {new_user.login_attempts}")
