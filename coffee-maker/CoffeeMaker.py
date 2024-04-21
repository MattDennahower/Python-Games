# Requirements for Coffee Machine program

# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”\
    # a. Check the user’s input to decide what to do next.
    # b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
# 3. Print report of all coffee machine resources
# 4. Check resources sufficient?
# 5. Process coins
# 6. Check transaction successful?
# 7. Make Coffee
# 8. Deduct resources from report
# 9. Print “Here is your latte. Enjoy!”

# Cost and ingredients for each drink

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Coffee machine resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Money in the machine
money = 0

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

def print_report():
    """Prints the report of all coffee machine resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def check_resources(drink):
    """Check if the resources are sufficient"""
    for item in MENU[drink]["ingredients"]:
        if resources[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Process coins"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * coins["quarters"]
    total += int(input("How many dimes?: ")) * coins["dimes"]
    total += int(input("How many nickels?: ")) * coins["nickels"]
    total += int(input("How many pennies?: ")) * coins["pennies"]
    return total

def check_transaction_successful(money_received, drink):
    """Check if the transaction was successful"""
    if money_received >= MENU[drink]["cost"]:
        change = round(money_received - MENU[drink]["cost"], 2)
        print(f"Here is ${change} in change.")
        global money
        money += MENU[drink]["cost"]
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink):
    """Make coffee"""
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    print(f"Here is your {drink}. Enjoy!")
    
def coffee_machine():
    """Coffee Machine main function"""
    while True:
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink == "off":
            break
        elif drink == "report":
            print_report()
        else:
            if drink not in MENU:
                print("Invalid drink. Please select from the menu.")
                continue
            if check_resources(drink):
                money_received = process_coins()
                if check_transaction_successful(money_received, drink):
                    make_coffee(drink)

# Print the logo of the coffee machine
print("Welcome to the Coffee Machine!")
print("☕️")

# Start the coffee machine
coffee_machine()