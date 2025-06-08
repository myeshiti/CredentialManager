import random
import re
import json
import hashlib

# File to store encrypted credentials
CREDENTIALS_FILE = "credentials_encrypted.json"

class UserCredentialsManager:
    def __init__(self):
        self.credentials_records = []
        self.counter = 1

    def hash_password(self, password):
        # Use SHA-256 to hash the password
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def save_credentials(self, user_username, user_password):
        hashed_password = self.hash_password(user_password)
        credentials_entry = {
            "ID": self.counter,
            "Username": user_username,
            "PasswordHash": hashed_password
        }
        self.credentials_records.append(credentials_entry)
        self.counter += 1
        return credentials_entry

    def check_password(self, user_password):
        return bool(re.match(r'^.{9,}$', user_password))

    def generate_password(self, length=12):
        symbols = "!@#$%^&*()_-+=<>?"
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" + symbols
        return ''.join(random.choice(characters) for _ in range(length))

    def display_credentials(self):
        return self.credentials_records

    def save_to_file(self, filename=CREDENTIALS_FILE):
        with open(filename, "w") as f:
            json.dump(self.credentials_records, f, indent=4)

    def load_from_file(self, filename=CREDENTIALS_FILE):
        try:
            with open(filename, "r") as f:
                self.credentials_records = json.load(f)
                self.counter = len(self.credentials_records) + 1
        except FileNotFoundError:
            self.credentials_records = []
            self.counter = 1


class CredentialsChecker(UserCredentialsManager):
    length_pattern = re.compile(r'^.{8,}$')
    symbol_pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')

    def check_credentials(self, username, password, actual_name):
        name_in_username = actual_name.lower() in username.lower()
        length_valid = self.length_pattern.match(username)
        has_symbol = self.symbol_pattern.search(username)
        has_upper = any(char.isupper() for char in username)
        has_digit = any(char.isdigit() for char in username)
        password_valid = self.check_password(password)

        errors = []
        if not name_in_username:
            errors.append("Username must include your name.")
        if not length_valid:
            errors.append("Username must be at least 8 characters long.")
        if not has_symbol:
            errors.append("Username must include a special character.")
        if not has_upper:
            errors.append("Username must contain an uppercase letter.")
        if not has_digit:
            errors.append("Username must include a digit.")
        if not password_valid:
            errors.append("Password must be at least 9 characters long.")

        return len(errors) == 0, errors


class CredentialsGenerator(UserCredentialsManager):
    def generate_username(self, username_type="medium"):
        symbols = "!@#$%^&*()_-+=<>?"
        if username_type not in {"short", "medium", "long"}:
            raise ValueError("Username type must be 'short', 'medium', or 'long'.")

        type_lengths = {
            "short": (1, 3, 3, 1),
            "medium": (2, 4, 3, 3),
            "long": (3, 5, 4, 4)
        }
        UPPER, LOWER, DIGIT, SYMBOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "0123456789", symbols
        upper_count, lower_count, digit_count, symbol_count = type_lengths[username_type]

        username = ''.join(random.choices(UPPER, k=upper_count) +
                           random.choices(LOWER, k=lower_count) +
                           random.choices(DIGIT, k=digit_count) +
                           random.choices(SYMBOL, k=symbol_count))
        return ''.join(random.sample(username, len(username)))  # Shuffle characters

    def generate_credentials(self, username_type="medium"):
        username = self.generate_username(username_type)
        password = self.generate_password()
        return self.save_credentials(username, password)


if __name__ == '__main__':
    main()
