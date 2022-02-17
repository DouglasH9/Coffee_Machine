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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True if there is a sufficient amount of resources to make drink"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * .25
    total += int(input("How many dimes?: ")) * .10
    total += int(input("How many nickels?: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True if payment accepted, or return False if insufficient payment."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that wasn't enough money, pal. Take your change back, ya filthy animal")


def make_drink(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


profit: int = 0
is_on = True

while is_on:
    choice = input("What would you like to drink? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}mL")
        print(f"Milk: {resources['milk']}mL")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])
