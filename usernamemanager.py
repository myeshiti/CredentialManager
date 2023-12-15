import random
import re

# Parent class to manager users credentials (username and password)

class UserCredentialsManager:
    def __init__(self):
        self.credentials_records = []   #a list to store credentials
        self.counter = 1    # counts how many IDs


    # Saves credentials of user's inputs into the list above

    def save_credentials(self, user_username, user_password):
        credentials_entry = {"ID": self.counter, "Username": user_username, "Password": user_password}
        self.credentials_records.append(credentials_entry)
        self.counter += 1
        return credentials_entry

    #Checks if a password meets it's length which is 9
    def check_password(self, user_password):
        length_pattern = re.compile(r'^.{9,}$')
        return length_pattern.match(user_password)

    #Generates a random password
    def generate_password(self):
        symbols_list = "!@#$%^&*()_-+=<>?"
        password_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789" + symbols_list
        generated_password = ''.join(random.choice(password_characters) for _ in range(12))  # Change the length as needed
        return generated_password

    #Displays saved credentials
    def display_credentials(self):
        return self.credentials_records

#checks and validates the credentials being input

class CredentialsChecker(UserCredentialsManager):
    length_pattern = re.compile(r'^.{8,}$')
    symbol_pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')

    def __init__(self, test_username, test_password):
        super().__init__()
        self.valid_credentials = []
        self.test_username = test_username
        self.test_password = test_password

    # checking for validity
    def check_credentials(self, user_name, user_password):
        while True:
            self.test_username = input(f"Hello {user_name}! Please enter the username you'd like to check: ")
            self.test_password = input(f"Please enter the password for the username '{self.test_username}': ") + user_password

            name_in_username = user_name.lower() in self.test_username.lower()
            password_length_valid = self.check_password(self.test_password)

            #Checks all the requirements 
            if all((name_in_username,
                    self.length_pattern.match(self.test_username),
                    self.symbol_pattern.search(self.test_username),
                    any(char.isupper() for char in self.test_username),
                    any(char.isdigit() for char in self.test_username),
                    password_length_valid)):
                self.valid_credentials.append({"Username": self.test_username, "Password": self.test_password})
                print("\nThis username and password are valid to use!")
                break
            else:
                print("\nThis username and/or password is not valid. Please correct the following issues:")
                if not name_in_username:
                    print(f"- Your name '{user_name}' is not included in the username. Make sure you do!")
                if not self.length_pattern.match(self.test_username):
                    print("- This username is too short. Your username must be at least 8 characters long.")
                if not self.symbol_pattern.search(self.test_username):
                    print("- This username does not contain special characters.")
                if not any(char.isupper() for char in self.test_username):
                    print("- This username does not contain capital letters.")
                if not any(char.isdigit() for char in self.test_username):
                    print("- This username does not contain numbers.")
                if not password_length_valid:
                    print("- The password is too short. It must be at least 8 characters long.")
                print("Please try again.")

# Class to genetate user credentials
class CredentialsGenerator(UserCredentialsManager):
    def __init__(self):
        super().__init__()
        self.credentials_records = [] 
        self.username_records = [] 

    # Using random, generates a username based on type (short, medium, long)
    def generate_username(self, username_type):
        symbols_list = "!@#$%^&*()_-+=<>?"
        generated_username = ""

        if username_type in {"short", "medium", "long"}:
            username_length = {"short": (1, 3, 3, 1), "medium": (2, 4, 3, 3), "long": (3, 5, 4, 4)}
            username_structure = [random.choices(category, k=length) for category, length in zip(
                ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "0123456789", symbols_list),
                username_length[username_type]
            )]

            generated_username = [char for sublist in username_structure for char in sublist]

        else:
            print("You must input 'short', 'medium', or 'long' into the generate_username function")

        username_str = ''.join(generated_username)

        self.username_records.append(username_str)

        return username_str

    def generate_password(self):
        symbols_list = "!@#$%^&*()_-+=<>?"
        password_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789" + symbols_list
        generated_password = ''.join(random.choice(password_characters) for _ in range(12))  # Change the length as needed
        return generated_password

    def generate_credentials(self, username_type):
        generated_username = self.generate_username(username_type)
        generated_password = self.generate_password()

        credentials_entry = {"Username": generated_username, "Password": generated_password}
        self.credentials_records.append(credentials_entry)

        return credentials_entry

def main():
    user_choice = int(input("Select option (1, 2, or 3) to use our program \n 1. Save Credentials \n 2. Check Credentials \n 3. Generate Credentials: "))

    credentials_manager = UserCredentialsManager()

    if user_choice == 1:
        num_credentials = int(input("How many credentials do you want to store? (Numeric): "))
        for _ in range(num_credentials):
            saved_credentials = credentials_manager.save_credentials(
                input("Enter the username you wish to store: "),
                input("Enter the password you wish to store: ")
            )
            print(saved_credentials)

        view_list = input("\nDo you want to view your credentials list? (Yes or No): ")
        if view_list.lower() == "yes":
            display_list = credentials_manager.display_credentials()
            print("\nCREDENTIALS LIST: \n \n", display_list)

    elif user_choice == 2:
        user_name = input("Enter your name: ")
        check_credentials_manager = CredentialsChecker(user_name, "")
        while True:
            check_credentials_manager.check_credentials(user_name, "")
            retry = input("\nDo you want to try again? (Yes or No): ")
            if retry.lower() != "yes":
                break

    elif user_choice == 3:
        generate_credentials_manager = CredentialsGenerator()
        generated_credentials = generate_credentials_manager.generate_credentials(
            input("Enter username type (short, medium, long): ")
        )
        print("Your generated credentials are: " + str(generated_credentials))

    elif user_choice not in {1, 2, 3}:
        print("You must enter 1, 2, or 3")


if __name__ == '__main__':
    main()
