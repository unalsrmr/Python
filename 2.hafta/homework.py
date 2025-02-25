from requests import get
from pprint import pprint

endpoint = "https://jsonplaceholder.typicode.com/users"
response = get(url=endpoint)
data = response.json()

def printData(data):
    while True:
        name = input("Please enter username: ")
        user_found = False
        for item in data:
            if item.get("username") == name:
                user_found = True
                while True:
                    key = input("Enter the key you want to see: ")
                    try:
                        pprint(f"{key} : {item[key]}")
                        break
                    except KeyError:
                        print(f"KeyError: '{key}' is not a valid key. Please try again..!\n")
                break
        if user_found:
            break
        else:
            print(f"Username '{name}' not found. Please try again..!\n")
def printAll(data):
    for item in data:
        pprint(item)
def createData(data):
    data.append({
        "id": len(data)+1,
        "name": input("Name: "),
        "username": input("Username: "),
        "email": input("Email: "),
        "address": {
            "street": input("Street: "),
            "suite": input("Suite: "),
            "city": input("City: "),
            "zipcode": input("Zipcode: "),
            "geo": {
                "lat": input("Latitude: "),
                "lng": input("Longitude: ")
            }
        },
        "phone": input("Phone: "),
        "website": input("Website: "),
        "company": {
            "name": input("Company name: "),
            "catchPhrase": input("Catch phrase: "),
            "bs": input("BS: ")
        }
    })
    printAll(data)
def updateData(data):
    while True:
        userFound= False
        for item in data:
            name=input("Please enter username: ")
            if item.get("username") == name:
                userFound = True
                key = input("Enter the key you want to update: ")
                value = input("Enter the new value: ")
                item[key] = value
                pprint(item)
                break
        if userFound:
            break
        else:
            print(f"Username '{name}' not found. Please try again..!\n")
def deleteData(data):
    while "True":
        userFound = False
        name = input("Please enter username: ")
        for item in data:
            if item.get("username") == name:
                userFound = True
                data.remove(item)
                printAll(data)
                break
        if userFound:
            break
        else:
            print(f"Username '{name}' not found. Please try again..!\n")

while True:
    process = input("1-List\n2-Create\n3-Update\n4-Delete\n5-Exit\nSelect a process: ")
    match process:
        case "1": # List
            printData(data)
        case "2": # Create
            createData(data)
        case "3": # Update
            updateData(data)
        case "4": # Delete
            deleteData(data)
        case "5": # Exit
            print("Exiting..!")
            break
        case _:
            print("Invalid process name")