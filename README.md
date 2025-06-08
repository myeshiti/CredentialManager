
# Credential Manager

A Python-based command-line tool that allows users to securely **generate**, **validate**, and **store** usernames and passwords with encryption.

---

## Features

- Save and display user credentials
- Validate usernames (special chars, digits, capitalization, name-inclusion)
- Validate strong passwords (min 9 characters)
- Generate random secure usernames and passwords (short/medium/long)
- Hash passwords before saving (SHA-256 encryption)
- Store credentials in encrypted JSON file (`credentials_encrypted.json`)
- Modular design using OOP (Python classes)
- Includes full `unittest` test suite

---

## 🖥️ Technologies Used

- Python 3
- `re` (regex validation)
- `random` (credential generation)
- `hashlib` (SHA-256 password hashing)
- `json` (data persistence)
- `unittest` (test framework)

---

## Project Structure

```
final_project/
│
├── usernamemanager.py # Core logic (OOP classes)
├── pseudo_finalProject.py # Command-line interface (interactive app)
├── usernamemanager_test.py # Unit tests
├── credentials_encrypted.json # Encrypted stored data
└── README.md # Project documentation
```

---

## How to Run the App

1. **Clone this repository**
2. Navigate to the project directory
3. Run:

```bash
python3 pseudo_finalProject.py


