import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["test"]
collection = db["test"]


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
    # elif choice == "3":
    #     show_password()
    elif choice == "4":
        delete_password()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice, enter again")
        main()

def add_password():
    _id = input("Enter the id: ")
    login = input("Enter the login: ")
    password = input("Enter the password: ")
    data = {
        "_id": _id,
        "login": login,
        "password": password
    }
    collection.insert_one(data)
    print("Password added")
    print("")
    main()

def view_passwords():
    for _id in collection.find({},{"_id":1}):
        print(_id["_id"])
    print("")
    main()

def delete_password():
    _id = input("Enter the _id: ")
    if _id in collection.find({'_id':_id}):
        collection.delete_one({"_id":_id})
        print("Password deleted \n")
    else:
        print("Password not found")
        delete_password()
    main()














main()