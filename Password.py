import json
import os

#Function to load existing passwords from a file
def load_passwords(filename):
    try:
        with open(filename, 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}
    return passwords

#Function to save passwords to a file
def save_passwords(passwords, filename):
    with open(filename, 'w') as file:
        json.dump(passwords, file, indent=4)

#Function to add a new password
def add_password(passwords, website, username, password):
    passwords[website] = {"username": username, "password": password}

#Function to retrieve a password
def get_password(passwords, website):
    return passwords.get(website, None)

if __name__ == "__main__":
    password_file = "passwords.json"
    passwords = load_passwords(password_file)

    while True:
        os.system("cls")
        print("\nOptions:")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Quit")
        print("                              Made by Fedi6431")

        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter the website: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            add_password(passwords, website, username, password)
            save_passwords(passwords, password_file)
            print("Password added successfully.")
        elif choice == "2":
            website = input("Enter the website: ")
            stored_password = get_password(passwords, website)
            if stored_password:
                print(f"Website: {website}")
                print(f"Username: {stored_password['username']}")
                print(f"Password: {stored_password['password']}")
            else:
                print("Password not found.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
