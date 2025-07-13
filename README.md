
# Password Manager

## Description
A simple password manager that allows users to store and retrieve passwords for various websites. The passwords are stored in a JSON file and can be accessed through a command-line interface.

## Features
- Store passwords securely in a JSON file.
- Retrieve stored passwords.
- Simple command-line interface.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Fedi6431/PasswordManager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd PasswordManager
   ```

## Usage
1. Run the script:
   ```bash
   python password_manager.py
   ```
2. Follow the on-screen instructions to add or retrieve passwords.

## Code Explanation
### Functions
- `load_passwords(filename)`: Loads existing passwords from a JSON file.
- `save_passwords(passwords, filename)`: Saves passwords to a JSON file.
- `add_password(passwords, website, username, password)`: Adds a new password to the dictionary.
- `get_password(passwords, website)`: Retrieves a password from the dictionary.

### Main Loop
The main loop provides a command-line interface for users to interact with the password manager. Users can choose to add a new password, retrieve a stored password, or quit the application.

## Example
```python
# Example usage
password_file = "passwords.json"
passwords = load_passwords(password_file)

# Add a new password
add_password(passwords, "example.com", "user123", "password123")
save_passwords(passwords, password_file)

# Retrieve a password
stored_password = get_password(passwords, "example.com")
print(stored_password)
```

## License
MIT

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contact
For any questions or suggestions, please contact [Fedi6431](https://github.com/Fedi6431).
