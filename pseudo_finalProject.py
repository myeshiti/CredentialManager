import random
import re

# Parent class to manager users credentials (username and password)

class UserCredentialsManager:
    def __init__(self):
        self.credentials_records = []   #a list to store credentials
        #self.counter = 1   


    # Saves credentials of user's inputs into the list above

    def save_credentials(self, user_username, user_password):
        credentials_entry = {"ID": self.counter, "Username": user_username, "Password": user_password}


    #Checks if a password meets it's length which is 9
    def check_password(self, user_password):
        length_pattern = re.compile(r'^.{9,}$')
        

    #Generates a random password
    def generate_password(self):
        symbols_list = "!@#$%^&*()_-+=<>?"
    

#checks and validates the credentials being input

class CredentialsChecker(UserCredentialsManager):
    length_pattern = re.compile(r'^.{8,}$')
    symbol_pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')

    def __init__(self, test_username, test_password):
        super().__init__()
        self.valid_credentials = []
        
    # checking for validity
    def check_credentials(self, user_name, user_password):
        while True:
            self.test_username = input(f"Hello {user_name}! Please enter the username you'd like to check: ")
            self.test_password = input(f"Please enter the password for the username '{self.test_username}': ") + user_password

# Class to genetate user credentials
class CredentialsGenerator(UserCredentialsManager):
    def __init__(self):
        super().__init__()
    

    # Using random, generates a username based on type (short, medium, long)
    def generate_username(self, username_type):
        symbols_list = "!@#$%^&*()_-+=<>?"
        generated_username = ""


    def generate_password(self):
        symbols_list = "!@#$%^&*()_-+=<>?"
       

    def generate_credentials(self, username_type):
        generated_username = self.generate_username(username_type)
       