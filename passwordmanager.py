import string
import random
import re

class PasswordManager:

    def __init__(self):
        self.password_records = []
        self.counter = 1

    def save_password(self, user_password):
        password_entry = {
            "ID": self.counter,
            "Password": user_password
        }
        self.password_records.append(password_entry)
        self.counter += 1
        return password_entry

    def display_passwords(self):
        return self.password_records


class PasswordChecker(PasswordManager):

    def __init__(self, test_password):
        super().__init__()
        self.valid_passwords = []
        self.test_password = test_password

    def check_password(self):
        length_pattern = re.compile(r'^.{8,}$')
        symbol_pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')

        if length_pattern.match(self.test_password):
            print("This password meets the length requirement.")
        else:
            print("This password is too short. Your password must be at least 8 characters long.")

        if symbol_pattern.search(self.test_password):
            print("This password contains special characters.")
        else:
            print("This password does not contain special characters.")

        if any(char.isupper() for char in self.test_password):
            print("This password contains capital letters.")
        else:
            print("This password does not contain capital letters.")

        if any(char.isdigit() for char in self.test_password):
            print("This password contains numbers.")
        else:
            print("This password does not contain numbers.")

        if length_pattern.match(self.test_password) and symbol_pattern.search(self.test_password) \
                and any(char.isupper() for char in self.test_password) \
                and any(char.isdigit() for char in self.test_password):
            self.valid_passwords.append(self.test_password)
            return print("\nThis password is valid to use!")
        else:
            return print("\nThis password is not valid!")

    def display_frequency(self):
        symbol_count = sum(1 for char in self.test_password if char in "!@#$%^&*(),.?\":{}|<>")
        capital_count = sum(1 for char in self.test_password if char.isupper())
        lower_count = sum(1 for char in self.test_password if char.islower())
        num_count = sum(1 for char in self.test_password if char.isdigit())

        frequency_info = (f"\nNumber of symbols: {symbol_count}"
                          f"\nNumber of capitals: {capital_count}"
                          f"\nNumber of lowercase: {lower_count}"
                          f"\nNumber of digits: {num_count}")

        return frequency_info


class PasswordGenerator(PasswordManager):

    def __init__(self):
        super().__init__()

    def generate_password(self, password_type):
        symbols_list = "!@#$%^&*()_-+=<>?"
        generated_password = ""

        if password_type == "short":
            capital_letters = random.choices(string.ascii_uppercase, k=1)
            lowercase_letters = random.choices(string.ascii_lowercase, k=3)
            numbers = random.choices(string.digits, k=3)
            symbols = random.choices(symbols_list, k=1)

            generated_password = capital_letters + lowercase_letters + numbers + symbols

        elif password_type == "medium":
            capital_letters = random.choices(string.ascii_uppercase, k=2)
            lowercase_letters = random.choices(string.ascii_lowercase, k=4)
            numbers = random.choices(string.digits, k=3)
            symbols = random.choices(symbols_list, k=3)

            generated_password = capital_letters + lowercase_letters + numbers + symbols

        elif password_type == "long":
            capital_letters = random.choices(string.ascii_uppercase, k=3)
            lowercase_letters = random.choices(string.ascii_lowercase, k=5)
            numbers = random.choices(string.digits, k=4)
            symbols = random.choices(symbols_list, k=4)

            generated_password = capital_letters + lowercase_letters + numbers + symbols

        else:
            print("You must input 'short', 'medium', or 'long' into the generate_password function")

        pass_str = ''.join(generated_password)

        self.password_records.append(pass_str)

        return pass_str


def main():
    user_choice = int(input("Select option (1, 2 or 3) to use our program \n 1. Save Password \n 2. Check Password \n 3. Generate Password: "))

    password_manager = PasswordManager()

    if user_choice == 1:
        num_passwords = int(input("How many passwords do you want to save? (Numeric): "))
        for _ in range(num_passwords):
            saved_password = password_manager.save_password(input("Enter the password you wish to save: "))
            print(saved_password)

        view_list = input("\nDo you want to view your password list? (Yes or No): ")
        if view_list.lower() == "yes":
            display_list = password_manager.display_passwords()
            print("\nPASSWORDS LIST: \n \n", display_list)

    elif user_choice == 2:
        check_password_manager = PasswordChecker(input("Enter the password you wish to check: "))
        check_password_manager.check_password()

        view_breakdown = input("\nDo you want to view the breakdown of your password (Yes or No): ")
        if view_breakdown.lower() == "yes":
            display_breakdown = check_password_manager.display_frequency()
            print(display_breakdown)

    elif user_choice == 3:
        generate_password_manager = PasswordGenerator()
        generated_password = generate_password_manager.generate_password(input("Enter password type (short, medium, long): "))
        print("Your generated password is " + generated_password)

    elif user_choice not in {1, 2, 3}:
        print("You must enter 1, 2, or 3")


if __name__ == '__main__':
    """
    This class calls the main() method to execute the prompt/commands for our program.
    """
    main()
