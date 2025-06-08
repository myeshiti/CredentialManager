from usernamemanager import UserCredentialsManager, CredentialsChecker, CredentialsGenerator

def main():
    print("Welcome to the Credential Manager\n")

    while True:
        try:
            print("Select an option:")
            print("1. Save Your Own Credentials")
            print("2. Check If a Credential Is Valid")
            print("3. Generate Random Credentials")
            print("4. View Saved Credentials")
            print("5. Load Credentials from File")
            print("6. Save Credentials to File")
            print("7. Exit")

            choice = input("Enter choice (1-7): ").strip()

            if choice == "1":
                manager = UserCredentialsManager()
                username = input("Enter a username: ")
                password = input("Enter a password (min 9 characters): ")
                saved = manager.save_credentials(username, password)
                print("✅ Saved:", saved)

            elif choice == "2":
                checker = CredentialsChecker()
                name = input("What is your name? ")
                username = input("Enter a username to check: ")
                password = input("Enter the password to check: ")

                valid, errors = checker.check_credentials(username, password, name)
                if valid:
                    print("✅ This username and password are valid!")
                else:
                    print("❌ Issues found:")
                    for err in errors:
                        print("-", err)

            elif choice == "3":
                generator = CredentialsGenerator()
                username_type = input("Choose username type (short, medium, long): ").lower()
                creds = generator.generate_credentials(username_type)
                print("✅ Generated Credentials:", creds)

            elif choice == "4":
                viewer = UserCredentialsManager()
                viewer.load_from_file()
                print("📄 Stored Credentials:")
                for cred in viewer.display_credentials():
                    print(cred)

            elif choice == "5":
                manager = UserCredentialsManager()
                manager.load_from_file()
                print("✅ Credentials loaded from file.")

            elif choice == "6":
                manager = UserCredentialsManager()
                manager.load_from_file()  # Load to avoid overwrite
                manager.save_to_file()
                print("✅ Credentials saved to file.")

            elif choice == "7":
                print("Goodbye!")
                break

            else:
                print("❗ Invalid choice. Please enter a number between 1 and 7.")

        except Exception as e:
            print("⚠️ Error:", e)

if __name__ == '__main__':
    main()
       
