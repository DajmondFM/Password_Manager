import os
import json

# Access to the files
os.chdir(os.path.dirname(__file__))

# Open json file
with open('data.json', 'r+') as f:
    data = json.load(f)

# def main():
#     print("Welcome to Password Manager")
#     print("1. Add a new password")
#     print("2. View all passwords")
#     print("3. Delete an password")
#     print("4. Exit")
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         add_password()
#     elif choice == "2":
#         view_passwords()
#     elif choice == "3":
#         delete_password()
#     elif choice == "4":
#         exit()
#     else:
#         print("Invalid choice")
#         main()

# main()

print("What would you like to do?")
print("1. Add a password")
print("2. View a passwords")
print("3. Delete a password")



a = int(input("Enter a number: "))
if a == 1:
    print("You have chosen to add a password")
    print("Enter the name of the password")
    name = input("Name: ")
    print("Enter the password")
    password = input("Password: ")
    data["Nazwa1"]["Haslo"] = password
    json.dump(data, open('data.json', 'w'))