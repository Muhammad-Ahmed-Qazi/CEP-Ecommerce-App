import os
import datetime
import pprint as pp

user_email = ""

def signup():
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
                password = input("Enter your password: ")
                while user["password"] != password:
                    print("Incorrect password. Please try again.")
                    password = input("Enter your password: ")
                return True

    return False

def show_pr():
    with open("./Files/products.txt", "r") as file:
        for line in file:
            pp.pprint(eval(line))
            print("\n")

def add_to_cart():
    global user_email

    products_input = input("Enter the product IDs and quantities (ID1xQuantity1,ID2xQuantity2,...): ")
    products = products_input.split(",")

    cart_file_path = os.path.join("./Files/Users/", user_email + ".txt")
    with open(cart_file_path, "r+") as cart_file:
        lines = cart_file.readlines()
        cart_file.seek(0)
        found_cart = False

        for line in lines:
            if line.strip() == "# Cart":
                found_cart = True
                cart_file.write(line)
                for product in products:
                    product_id, quantity = product.split("x")
                    cart_file.write(f"[{product_id}, {quantity}]\n")
            else:
                cart_file.write(line)

        if not found_cart:
            cart_file.write("# Cart\n")
            for product in products:
                product_id, quantity = product.split("x")
                cart_file.write(f"{product_id}: {quantity}\n")

        cart_file.truncate()

def view_cart():
    global user_email
    products = open("./Files/products.txt", "r").readlines()

    total = [0, 0]

    print("VIEWING CART")

    cart_file_path = os.path.join("./Files/Users/", user_email + ".txt")
    with open(cart_file_path, "r") as cart_file:
        lines = cart_file.readlines()

        for line in lines:
            if line.strip().startswith("["):
                product_id = eval(line)[0]
                quantity = eval(line)[1]
                for product in products:
                    product = eval(product)
                    if product["id"] == product_id:
                        product["quantity"] = quantity
                        pp.pprint(product)
                        print("\n")
                total[1] += int(quantity)
                total[0] += int(product["price"]) * int(quantity)
    
    print(f"Total: ${total[0]}")
    print(f"Total items: {total[1]}")


def remove_from_cart():
    global user_email

    product_id = input("Enter the product ID to remove from the cart: ")

    cart_file_path = os.path.join("./Files/Users/", user_email + ".txt")
    with open(cart_file_path, "r") as cart_file:
        lines = cart_file.readlines()
    cart_file.close()

    with open(cart_file_path, "w") as cart_file:
        for line in lines:
            if line.strip().startswith("[") and int(product_id) == int(eval(line)[0]):
                print("Found product")
                pass
            else:
                cart_file.write(line)

def checkout():
    global user_email
    cart = []
    flag = False

    cart_file_path = os.path.join("./Files/Users/", user_email + ".txt")

    with open(cart_file_path, "r") as cart_file:
        lines = cart_file.readlines()

    with open(cart_file_path, "w") as cart_file:
        for line in lines:
            if line.strip().startswith("# History"):
                flag = True

            if line.strip().startswith("[") and flag == False:
                cart.append(line.strip())
            else:
                cart_file.write(line)

    with open(cart_file_path, "a+") as cart_file:
        cart_file.write("\n")
        cart_file.write(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
        cart_file.write("\n")
        for item in cart:
            cart_file.write(item)
            cart_file.write("\n")



    print("Checkout completed. Items have been removed from the cart.")

def show_hist():
    global user_email

    hist_file_path = os.path.join("./Files/Users/", user_email + ".txt")

    with open(hist_file_path, "r") as hist_file:
        lines = hist_file.readlines()

    print("Shopping History:")
    found_history = False
    for line in lines:
        if found_history:
            product_info = eval(line.strip())
            product = product_info[1]
            quantity = product_info[2]
            print(f"Product: {product}, Quantity: {quantity}")
        elif line.strip().startswith("# History"):
            found_history = True

show_hist()

    


while True:
    # registered = login()

    # if not registered:
    #     print("This email is not registered. Please create an account below.")
    #     signup()
    #     print("Account created! Please login below.")
    #     login()

    user_email = "qmuhammadahmed@gmail.com" # COMMENT THIS OUT WHEN DONE TESTING
    
    # show_pr()
    # user_input = input("Do you want to add products to your cart? (y/n): ")
    # if user_input.lower() == "y":
    #     add_to_cart()

    # print("\n")
    # view_cart()
    # print("\n")

    # user_input = input("Do you want to remove products from your cart? (y/n): ")
    # if user_input.lower() == "y":
    #     remove_from_cart()

    # checkout()

    show_hist()

    input()
    