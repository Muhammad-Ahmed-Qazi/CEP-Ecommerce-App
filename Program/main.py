import os
import pprint as pp

user_email = ""

def signup():
    print("# SIGN UP FORM")
    user = {
        "email": input("Enter your email: "),
        "password": input("Enter your password: "),
        "first_name": input("Enter your first name: "),
        "last_name": input("Enter your last name: "),
        "address": input("Enter your address: "),
        "phone_number": input("Enter your phone number: "),
        "age": int(input("Enter your age: ")),
        "is_admin": input("Are you an admin? (Y/n): ").lower() == "y"
    }

    with open("./Files/authentication.txt", "a") as file:
        file.write(str(user) + "\n")

    user_file_path = os.path.join("./Files/Users/", user["email"] + ".txt")
    with open(user_file_path, "w") as user_file:
        user_file.write("# Data\n" + str(user) + "\n\n# Cart\n\n\n# History")

def login():
    global user_email

    email = input("Enter your email: ")

    with open("./Files/authentication.txt", "r") as file:
        for line in file:
            user = eval(line)
            if user["email"] == email:
                user_email = email
                password = ""
                while user["password"] != password:
                    print("Incorrect password. Please try again.")
                    password = input("Enter your password: ")
                return True

    return False

def gallery():
    with open("./Files/products.txt", "r") as file:
        for line in file:
            pp.pprint(eval(line))
            print("\n")

def add_to_cart():
    global user_email
    


while True:
    # registered = login()

    # if not registered:
    #     print("This email is not registered. Please create an account below.")
    #     signup()
    #     print("Account created! Please login below.")
    #     login()
    
    gallery()

    input()
    