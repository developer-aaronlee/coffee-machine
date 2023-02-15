import math

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

def check_resouces(order_ingredients):
    for x in order_ingredients:
        if order_ingredients[x] > resources[x]:
            print(f"Sorry there is not enough {x}.")
            return False
        else:
            return True

def inserted_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many dimes?: ")) * 0.01
    return total

def check_transaction(user_payment, menu_price):
    if user_payment >= menu_price:
        global money
        money += menu_price
        change = round(user_payment - menu_price,2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def calculate_resources(order_ingredients):
    for x in order_ingredients:
        resources[x] -= order_ingredients[x]
    print(f"Here is your {user_input} ☕️. Enjoy!")

money = 0
machine_on = True

while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        machine_on = False
    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f"money: ${money}")
    else:
        required_resources = MENU[user_input]["ingredients"]
        if check_resouces(required_resources):
            payment = inserted_coins()
            required_payment = MENU[user_input]["cost"]
            if check_transaction(payment, required_payment):
                calculate_resources(required_resources)







