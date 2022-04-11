import os
import json

# Access to the files
os.chdir(os.path.dirname(__file__))

# Open json file
# Create a data.json
# If file doesn't exist, create it
if not os.path.exists('data.json'):
    with open('data.json', 'w') as f:
        data = {}
        json.dump(data, f)

with open('data.json', 'r+') as f:
    data = json.load(f)

def main():
    print("Welcome to Password Manager by Dajmond")
    print("1. Add a new password")
    print("2. View all passwords")
    print("3. Show password")
    print("4. Delete an password")
    print("5. Exit")
    choice = input("Enter your choice: ")
    print("")
    if choice == "1":
        add_password()
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        show_password()
    elif choice == "4":
        delete_password()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice, enter again")
        main()

def add_password():
    site = input("Enter the site url: ")
    login = input("Enter the login: ")
    password = input("Enter the password: ")
    data[site] = {
        "login": login,
        "password": password
    }
    with open('data.json', 'w') as f:
        json.dump(data, f)
    print("Password added")
    print("")
    main()

def view_passwords():
    for site in data:
        print(site)
    print("")
    main()

def delete_password():
    site = input("Enter the site: ")
    if site in data:
        del data[site]
        with open('data.json', 'w') as f:
            json.dump(data, f)
        print("Password deleted \n")
    else:
        print("Password not found")
    main()

def show_password():
    site = input("Enter the site: ")
    if site in data:
        print("Login: " + data[site]["login"])
        print("Password: " + data[site]["password"])
        print("")
    else:
        print("Password not found")
    main()

main()