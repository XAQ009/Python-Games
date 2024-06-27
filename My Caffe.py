my_name = "Zach"
menu = {
    "bold roast": 2,
    "mild roast": 3,
    "light roast": 3,
    "specialty roast": 4}
menu2 = {
    "bold": 2,
    "mild": 3,
    "light": 3,
    "specialty": 4}

evil_customers = ("Danica", "Nick", "Susan")

def greet_customer():
    print("Welcome to Latte Larry's")
    name = input("\nWhat is your name? ").strip()
    if name in evil_customers:
        evil_answer = input("Are you Evil? ").lower()
        if evil_answer in ("yes", "y"):
            good_deeds = int(input("How many people have you helped today?\n"))
            if good_deeds < 4:
                print(f"Get out of here EVIL {name} !!!!!!)")
                exit()
            else:
                print("I'm Glad you have changed your ways")
    print(f"\nWelcome {name}, my name is {my_name}")

def display_menu():
    print("\nHere is our roast menu:")
    for item, price in menu.items():
        print(f"- {item.capitalize()}: ${price:.2f}") 

def take_order():
    total = 0
    order = {}
    while True:
        display_menu()  # Allow user to see the menu again
        choice = input("\nWhat is looking good today? ").lower().strip()

        if choice in menu:
            try:
                quantity = int(input(f"How many {choice} would you like? "))
                if quantity > 0: 
                    total += menu[choice] * quantity
                    order[choice] = quantity
                    print(f"Adding {quantity} {choice} to your order.")
                else:
                    print("Please enter a positive quantity.")
            except ValueError:
                print("Invalid input. Please enter a number for quantity.")
        else:
            print("We do not have that.")

        another_order = input("Would you like anything else? (yes/no): ").lower()
        if another_order not in ("yes", "y"):
            break
    return order, total

# Main program flow
greet_customer()
order, total = take_order()
print("\nYour order:")
for item, quantity in order.items():
    print(f"- {quantity} {item.capitalize()}")
print(f"\nYour total is ${total:.2f}. Thank you!")
